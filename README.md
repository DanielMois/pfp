# PFP - Controle Financeiro

Uma aplicação web moderna e responsiva para controle de gastos financeiros, desenvolvida em Flask com interface elegante, modo escuro e funcionalidades completas de CRUD.

## 🚀 Funcionalidades

### 🏠 Dashboard Principal
- **Visão Geral**: Cards interativos com saldos (Disponível, Guardado, Investido, Dinheiro Físico)
- **Estatísticas em Tempo Real**: Parcelas do mês atual, saldo total, compras do mês
- **Gráfico Histograma**: Gastos por categoria em formato de barras
- **Modo Escuro**: Alternância entre tema claro e escuro
- **Histórico**: Log automático de todas as alterações

### 💳 Controle de Crédito
- **Cadastro Completo**: Compras no cartão de crédito com data, descrição, categoria, banco e valor
- **Categorização**: 15 categorias predefinidas (Alimentação, Transporte, Saúde, etc.)
- **Bancos Suportados**: Nubank (roxo) e Itaú (laranja)
- **Gráficos Interativos**: 
  - Histograma de gastos por categoria
  - Gráfico de gastos por banco
- **Filtros Avançados**: Por mês/ano, categoria, banco, data de início/fim
- **Tabela Dinâmica**: Ordenação por data mais recente
- **Exportação CSV**: Dados filtrados para análise externa

### 💰 Controle de Débito
- **Compras à Vista**: Registro de gastos em dinheiro ou débito
- **Mesma Categorização**: Categorias e bancos consistentes com crédito
- **Gráficos Separados**: Análise independente dos gastos à vista
- **Filtros Idênticos**: Mesma funcionalidade de filtros do crédito
- **Estatísticas Específicas**: Métricas dedicadas para gastos à vista

### 📈 Resumo Financeiro
- **Distribuição de Saldos**: Gráfico de barras ordenado por valor
- **Gastos por Categoria**: Histograma com cores suaves
- **Evolução Mensal**: Gráfico de linha com tendência dos gastos
- **Histórico Detalhado**: Log completo de alterações com tipos de operação
- **Análise Temporal**: Visualização da evolução financeira

### 🎨 Modo Escuro
- **Alternância Suave**: Botão na navbar com ícone dinâmico
- **Persistência**: Preferência salva no navegador
- **Cores Harmoniosas**: Paleta otimizada para uso noturno
- **Gráficos Adaptados**: Chart.js com cores do tema
- **Interface Consistente**: Todos os elementos adaptados

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask, SQLAlchemy, PyMySQL
- **Frontend**: Bootstrap 5, Chart.js, JavaScript ES6+
- **Banco de Dados**: MySQL
- **Design**: Interface responsiva com gradientes, animações e modo escuro
- **Ícones**: Bootstrap Icons
- **Cores**: Paleta suave em famílias azul, roxo, cinza e preto

## 📋 Pré-requisitos

- Python 3.8+
- MySQL Server
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd PFP
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure o banco de dados**
   - Crie um banco MySQL chamado `pfp`
   - Configure as credenciais no arquivo `.env`:
     ```
     DB_HOST=localhost
     DB_PORT=3306
     DB_NAME=pfp
     DB_USER=root
     DB_PASSWORD=sua_senha
     ```

6. **Execute a aplicação**
   ```bash
   python app.py
   ```

7. **Acesse a aplicação**
   - Abra o navegador e acesse: `http://localhost:5000`

## 📁 Estrutura do Projeto

```
PFP/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── .env                  # Variáveis de ambiente
├── templates/            # Templates HTML
│   ├── base.html         # Template base com modo escuro
│   ├── index.html        # Dashboard principal
│   ├── resumo.html       # Página de resumo financeiro
│   ├── credito.html      # Controle de crédito
│   └── debito.html       # Controle de débito
├── static/               # Arquivos estáticos
│   └── js/
│       └── config.js     # Configurações e cores da aplicação
└── models/               # Modelos SQLAlchemy
    ├── __init__.py
    ├── saldo.py          # Modelo de saldos
    ├── compra.py         # Modelo de compras
    └── historico.py      # Modelo de histórico
```

## 🗄️ Modelos do Banco de Dados

### Saldo
- **Tipos**: Disponível, Guardado, Investido, Dinheiro Físico
- **Campos**: id, tipo, valor, data_atualizacao
- **Histórico**: Log automático de alterações

### Compra (Crédito e Débito)
- **Campos**: id, data, gasto, categoria, banco, valor
- **Categorias**: 15 opções predefinidas
- **Bancos**: Nubank e Itaú
- **Tabelas**: compras (crédito) e compras_debito (débito)

### HistoricoSaldo
- **Campos**: id, saldo_id, valor_anterior, valor_novo, data_alteracao, tipo_operacao
- **Operações**: criação, atualização, exclusão
- **Auditoria**: Rastreamento completo de mudanças

## 🎨 Características da Interface

### Design Responsivo
- **Desktop**: Layout otimizado com múltiplas colunas
- **Tablet**: Adaptação automática para telas médias
- **Mobile**: Interface touch-friendly

### Modo Escuro
- **Alternância**: Botão na navbar com ícone dinâmico
- **Cores**: Fundo escuro (#1a1a1a, #2d2d2d)
- **Texto**: Branco e cinza claro
- **Elementos**: Cards, tabelas, modais e gráficos adaptados

### Elementos Visuais
- **Gradientes**: Cabeçalhos com gradientes azul/roxo
- **Animações**: Transições suaves e efeitos hover
- **Ícones**: Bootstrap Icons em toda a interface
- **Gráficos**: Chart.js com cores temáticas

### Navegação
- **Menu Fixo**: Navbar com navegação principal
- **Indicadores**: Páginas ativas destacadas
- **Breadcrumbs**: Navegação intuitiva

## 🔄 Funcionalidades CRUD

### Saldos
- ✅ **Create**: Adicionar novos tipos de saldo
- ✅ **Read**: Visualizar em cards interativos
- ✅ **Update**: Editar valores com histórico automático
- ✅ **Delete**: Remover com confirmação

### Compras (Crédito e Débito)
- ✅ **Create**: Cadastrar compras com todos os dados
- ✅ **Read**: Listar com filtros avançados
- ✅ **Update**: Editar informações completas
- ✅ **Delete**: Remover com confirmação

### Histórico
- ✅ **Automático**: Log de todas as alterações
- ✅ **Consulta**: Visualização em tabela
- ✅ **Auditoria**: Rastreamento completo

## 📊 Relatórios e Análises

### Dashboard
- **Métricas Principais**: Parcelas do mês, saldo total, compras do mês
- **Gráfico Rápido**: Histograma de gastos por categoria
- **Ações Rápidas**: Links para funcionalidades principais

### Resumo Financeiro
- **Distribuição de Saldos**: Gráfico de barras ordenado
- **Evolução Temporal**: Gráfico de linha mensal
- **Histórico Detalhado**: Log de alterações

### Filtros Avançados
- **Temporais**: Mês/ano, data de início/fim
- **Categóricos**: Categoria, banco
- **Aplicação Global**: Filtros afetam cards, tabelas e gráficos

### Exportação
- **Formato CSV**: Dados filtrados
- **Personalização**: Nome do arquivo com data
- **Notificação**: Confirmação de exportação

## 🎨 Sistema de Cores

### Paleta Principal
- **Azul**: #1E3A8A, #3B82F6, #60A5FA
- **Roxo**: #8B5CF6, #A855F7, #C084FC
- **Cinza**: #6B7280, #9CA3AF, #D1D5DB
- **Preto**: #1F2937, #111827, #000000

### Cores Específicas
- **Nubank**: Roxo (#8A2BE2)
- **Itaú**: Laranja (#FF8C00)
- **Gradientes**: Cabeçalhos e elementos especiais

## 🔒 Segurança e Validação

### Frontend
- **Validação**: Campos obrigatórios e formatos
- **Confirmações**: Operações críticas
- **Sanitização**: Inputs limpos

### Backend
- **Validação**: Dados verificados no servidor
- **Transações**: Operações atômicas
- **Histórico**: Auditoria completa

## 🚀 Deploy

### Desenvolvimento
```bash
python app.py
```

### Produção
1. **Servidor Web**: nginx/apache
2. **WSGI**: gunicorn/uwsgi
3. **HTTPS**: Certificado SSL
4. **MySQL**: Configurações de segurança
5. **Variáveis**: Configuração de ambiente

## 🤝 Contribuição

1. **Fork**: Faça um fork do projeto
2. **Branch**: Crie uma branch para sua feature
3. **Commit**: Commit suas mudanças
4. **Push**: Push para a branch
5. **Pull Request**: Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🆘 Suporte

Para dúvidas ou problemas:
- Abra uma issue no repositório
- Descreva detalhadamente o problema
- Inclua screenshots se necessário

## 🔄 Changelog

### Versão Atual
- ✅ Modo escuro completo
- ✅ Gráficos adaptados ao tema
- ✅ Histograma de categorias
- ✅ Filtros globais
- ✅ Cores harmoniosas
- ✅ Interface responsiva
- ✅ CRUD completo
- ✅ Exportação CSV
- ✅ Histórico automático 