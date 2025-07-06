from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime, date
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave_padrao_para_desenvolvimento')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

# Modelos do banco de dados
class Saldo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)  # 'disponivel', 'guardado', 'investido', 'dinheiro_fisico'
    valor = db.Column(db.Float, nullable=False)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'valor': self.valor,
            'data_atualizacao': self.data_atualizacao.strftime('%Y-%m-%d %H:%M:%S')
        }

class HistoricoSaldo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    saldo_id = db.Column(db.Integer, db.ForeignKey('saldo.id'), nullable=False)
    valor_anterior = db.Column(db.Float, nullable=False)
    valor_novo = db.Column(db.Float, nullable=False)
    data_alteracao = db.Column(db.DateTime, default=datetime.utcnow)
    tipo_operacao = db.Column(db.String(20), nullable=False)  # 'criacao', 'atualizacao', 'exclusao'

class CompraCredito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    gasto = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    banco = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data.strftime('%Y-%m-%d'),
            'gasto': self.gasto,
            'categoria': self.categoria,
            'banco': self.banco,
            'valor': self.valor
        }

class CompraDebito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    gasto = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    banco = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data.strftime('%Y-%m-%d'),
            'gasto': self.gasto,
            'categoria': self.categoria,
            'banco': self.banco,
            'valor': self.valor
        }



# Rotas principais
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resumo')
def resumo():
    return render_template('resumo.html')



@app.route('/credito')
def credito():
    return render_template('credito.html')

@app.route('/debito')
def debito():
    return render_template('debito.html')



# API Routes para Saldos
@app.route('/api/saldos', methods=['GET'])
def get_saldos():
    saldos = Saldo.query.all()
    return jsonify([saldo.to_dict() for saldo in saldos])

@app.route('/api/saldos', methods=['POST'])
def criar_saldo():
    data = request.get_json()
    
    # Verificar se já existe um saldo deste tipo
    saldo_existente = Saldo.query.filter_by(tipo=data['tipo']).first()
    if saldo_existente:
        return jsonify({'error': 'Já existe um saldo deste tipo'}), 400
    
    novo_saldo = Saldo(
        tipo=data['tipo'],
        valor=data['valor']
    )
    
    db.session.add(novo_saldo)
    db.session.commit()
    
    # Registrar no histórico
    historico = HistoricoSaldo(
        saldo_id=novo_saldo.id,
        valor_anterior=0,
        valor_novo=data['valor'],
        tipo_operacao='criacao'
    )
    db.session.add(historico)
    db.session.commit()
    
    return jsonify(novo_saldo.to_dict()), 201

@app.route('/api/saldos/<int:saldo_id>', methods=['PUT'])
def atualizar_saldo(saldo_id):
    saldo = Saldo.query.get_or_404(saldo_id)
    data = request.get_json()
    
    valor_anterior = saldo.valor
    saldo.valor = data['valor']
    saldo.data_atualizacao = datetime.utcnow()
    
    # Registrar no histórico
    historico = HistoricoSaldo(
        saldo_id=saldo.id,
        valor_anterior=valor_anterior,
        valor_novo=data['valor'],
        tipo_operacao='atualizacao'
    )
    db.session.add(historico)
    db.session.commit()
    
    return jsonify(saldo.to_dict())

@app.route('/api/saldos/<int:saldo_id>', methods=['DELETE'])
def deletar_saldo(saldo_id):
    saldo = Saldo.query.get_or_404(saldo_id)
    
    # Registrar no histórico antes de deletar
    historico = HistoricoSaldo(
        saldo_id=saldo.id,
        valor_anterior=saldo.valor,
        valor_novo=0,
        tipo_operacao='exclusao'
    )
    db.session.add(historico)
    
    db.session.delete(saldo)
    db.session.commit()
    
    return jsonify({'message': 'Saldo deletado com sucesso'})

@app.route('/api/saldos/historico')
def get_historico_saldos():
    historico = HistoricoSaldo.query.order_by(HistoricoSaldo.data_alteracao.desc()).all()
    return jsonify([{
        'id': h.id,
        'saldo_id': h.saldo_id,
        'valor_anterior': h.valor_anterior,
        'valor_novo': h.valor_novo,
        'data_alteracao': h.data_alteracao.strftime('%Y-%m-%d %H:%M:%S'),
        'tipo_operacao': h.tipo_operacao
    } for h in historico])

# API Routes para Compras
@app.route('/api/compras', methods=['GET'])
def get_compras():
    compras = CompraCredito.query.order_by(CompraCredito.data.desc()).all()
    return jsonify([compra.to_dict() for compra in compras])

@app.route('/api/compras', methods=['POST'])
def criar_compra():
    data = request.get_json()
    
    nova_compra = CompraCredito(
        data=datetime.strptime(data['data'], '%Y-%m-%d').date(),
        gasto=data['gasto'],
        categoria=data['categoria'],
        banco=data['banco'],
        valor=data['valor']
    )
    
    db.session.add(nova_compra)
    db.session.commit()
    
    return jsonify(nova_compra.to_dict()), 201

@app.route('/api/compras/<int:compra_id>', methods=['PUT'])
def atualizar_compra(compra_id):
    compra = CompraCredito.query.get_or_404(compra_id)
    data = request.get_json()
    
    compra.data = datetime.strptime(data['data'], '%Y-%m-%d').date()
    compra.gasto = data['gasto']
    compra.categoria = data['categoria']
    compra.banco = data['banco']
    compra.valor = data['valor']
    
    db.session.commit()
    
    return jsonify(compra.to_dict())

@app.route('/api/compras/<int:compra_id>', methods=['DELETE'])
def deletar_compra(compra_id):
    compra = CompraCredito.query.get_or_404(compra_id)
    
    db.session.delete(compra)
    db.session.commit()
    
    return jsonify({'message': 'Compra deletada com sucesso'})

# API Routes para Compras em Débito
@app.route('/api/compras-debito', methods=['GET'])
def get_compras_debito():
    compras = CompraDebito.query.order_by(CompraDebito.data.desc()).all()
    return jsonify([compra.to_dict() for compra in compras])

@app.route('/api/compras-debito', methods=['POST'])
def criar_compra_debito():
    data = request.get_json()
    
    nova_compra = CompraDebito(
        data=datetime.strptime(data['data'], '%Y-%m-%d').date(),
        gasto=data['gasto'],
        categoria=data['categoria'],
        banco=data['banco'],
        valor=data['valor']
    )
    
    db.session.add(nova_compra)
    db.session.commit()
    
    # Atualizar saldo disponível (descontar o valor da compra)
    saldo_disponivel = Saldo.query.filter_by(tipo='disponivel').first()
    if saldo_disponivel:
        valor_anterior = saldo_disponivel.valor
        saldo_disponivel.valor -= data['valor']
        saldo_disponivel.data_atualizacao = datetime.utcnow()
        
        # Registrar no histórico
        historico = HistoricoSaldo(
            saldo_id=saldo_disponivel.id,
            valor_anterior=valor_anterior,
            valor_novo=saldo_disponivel.valor,
            tipo_operacao='atualizacao'
        )
        db.session.add(historico)
        db.session.commit()
    
    return jsonify(nova_compra.to_dict()), 201

@app.route('/api/compras-debito/<int:compra_id>', methods=['PUT'])
def atualizar_compra_debito(compra_id):
    compra = CompraDebito.query.get_or_404(compra_id)
    data = request.get_json()
    
    # Calcular diferença no valor para ajustar o saldo
    diferenca_valor = data['valor'] - compra.valor
    
    compra.data = datetime.strptime(data['data'], '%Y-%m-%d').date()
    compra.gasto = data['gasto']
    compra.categoria = data['categoria']
    compra.banco = data['banco']
    compra.valor = data['valor']
    
    # Atualizar saldo disponível se houve mudança no valor
    if diferenca_valor != 0:
        saldo_disponivel = Saldo.query.filter_by(tipo='disponivel').first()
        if saldo_disponivel:
            valor_anterior = saldo_disponivel.valor
            saldo_disponivel.valor -= diferenca_valor
            saldo_disponivel.data_atualizacao = datetime.utcnow()
            
            # Registrar no histórico
            historico = HistoricoSaldo(
                saldo_id=saldo_disponivel.id,
                valor_anterior=valor_anterior,
                valor_novo=saldo_disponivel.valor,
                tipo_operacao='atualizacao'
            )
            db.session.add(historico)
    
    db.session.commit()
    
    return jsonify(compra.to_dict())

@app.route('/api/compras-debito/<int:compra_id>', methods=['DELETE'])
def deletar_compra_debito(compra_id):
    compra = CompraDebito.query.get_or_404(compra_id)
    
    # Restaurar o valor da compra no saldo disponível
    saldo_disponivel = Saldo.query.filter_by(tipo='disponivel').first()
    if saldo_disponivel:
        valor_anterior = saldo_disponivel.valor
        saldo_disponivel.valor += compra.valor
        saldo_disponivel.data_atualizacao = datetime.utcnow()
        
        # Registrar no histórico
        historico = HistoricoSaldo(
            saldo_id=saldo_disponivel.id,
            valor_anterior=valor_anterior,
            valor_novo=saldo_disponivel.valor,
            tipo_operacao='atualizacao'
        )
        db.session.add(historico)
    
    db.session.delete(compra)
    db.session.commit()
    
    return jsonify({'message': 'Compra deletada com sucesso'})



# API Routes para estatísticas
@app.route('/api/estatisticas/resumo')
def get_estatisticas_resumo():
    # Calcular saldo total
    saldos = Saldo.query.all()
    saldo_total = sum(saldo.valor for saldo in saldos)
    
    # Calcular gasto total do mês atual
    hoje = datetime.now()
    primeiro_dia_mes = date(hoje.year, hoje.month, 1)
    ultimo_dia_mes = date(hoje.year, hoje.month + 1, 1) if hoje.month < 12 else date(hoje.year + 1, 1, 1)
    
    # Buscar compras do mês atual (crédito e débito)
    compras_credito_mes = CompraCredito.query.filter(
        CompraCredito.data >= primeiro_dia_mes,
        CompraCredito.data < ultimo_dia_mes
    ).all()
    
    compras_debito_mes = CompraDebito.query.filter(
        CompraDebito.data >= primeiro_dia_mes,
        CompraDebito.data < ultimo_dia_mes
    ).all()
    
    # Calcular gasto total do mês (crédito + débito)
    gasto_credito = sum(compra.valor for compra in compras_credito_mes)
    gasto_debito = sum(compra.valor for compra in compras_debito_mes)
    gasto_total = gasto_credito + gasto_debito
    
    # Calcular gastos por categoria do mês (combinando crédito e débito)
    categorias = {}
    for compra in compras_credito_mes + compras_debito_mes:
        if compra.categoria not in categorias:
            categorias[compra.categoria] = 0
        categorias[compra.categoria] += compra.valor
    
    return jsonify({
        'saldo_total': saldo_total,
        'gasto_medio_mensal': gasto_total,  # Representa o gasto do mês atual
        'gastos_por_categoria': [{'categoria': cat, 'total': float(total)} for cat, total in categorias.items()]
    })



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 