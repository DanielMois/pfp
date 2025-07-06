# 🔒 Guia de Segurança - PFP

Este documento contém informações importantes sobre segurança e proteção de credenciais para o projeto PFP.

## 🚨 Proteção de Credenciais

### ✅ O que está protegido pelo .gitignore

- **Arquivo `.env`**: Contém todas as credenciais do banco de dados
- **Ambiente virtual**: Pasta `venv/` com dependências
- **Cache Python**: Arquivos `__pycache__/`
- **Logs**: Arquivos de log da aplicação
- **Certificados SSL**: Chaves e certificados de segurança
- **Backups**: Arquivos de backup do banco de dados

### 🔐 Variáveis de Ambiente

O projeto usa as seguintes variáveis de ambiente (definidas no arquivo `.env`):

```bash
# Banco de Dados
DB_HOST=localhost
DB_PORT=3306
DB_NAME=pfp
DB_USER=seu_usuario
DB_PASSWORD=sua_senha

# Aplicação
SECRET_KEY=sua_chave_secreta_muito_segura
```

### 📋 Checklist de Segurança

Antes de fazer push para o GitHub:

- [ ] Verificar se o arquivo `.env` está no `.gitignore`
- [ ] Confirmar que não há credenciais hardcoded no código
- [ ] Verificar se o arquivo `.env.example` existe com valores de exemplo
- [ ] Testar se a aplicação funciona com as variáveis de ambiente

## 🛡️ Boas Práticas

### 1. Nunca commitar credenciais
```bash
# ❌ ERRADO
app.config['SECRET_KEY'] = 'minha_chave_secreta'

# ✅ CORRETO
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
```

### 2. Usar variáveis de ambiente
```bash
# Sempre usar os.getenv() para credenciais
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
```

### 3. Arquivo .env.example
- Sempre manter um arquivo `.env.example` com a estrutura
- Nunca incluir valores reais, apenas placeholders
- Documentar todas as variáveis necessárias

## 🔍 Verificação de Segurança

### Comandos para verificar se está seguro:

```bash
# Verificar se .env está sendo ignorado
git status --ignored

# Verificar se há credenciais no código
grep -r "password\|senha\|secret" . --exclude-dir=venv --exclude-dir=.git

# Verificar arquivos que serão commitados
git add .
git status
```

### Se encontrar credenciais expostas:

1. **Imediatamente**: Remover do histórico do Git
2. **Alterar**: Todas as senhas e chaves expostas
3. **Verificar**: Se houve comprometimento
4. **Documentar**: O incidente e as ações tomadas

## 🚀 Deploy Seguro

### Desenvolvimento
```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar com suas credenciais
nano .env

# Verificar se está funcionando
python app.py
```

### Produção
- Usar variáveis de ambiente do servidor
- Nunca usar arquivo `.env` em produção
- Usar chaves secretas fortes e únicas
- Configurar HTTPS obrigatório

## 📞 Suporte de Segurança

Se você encontrar vulnerabilidades de segurança:

1. **NÃO** abra uma issue pública
2. Entre em contato diretamente com o mantenedor
3. Descreva detalhadamente o problema
4. Aguarde a correção antes de divulgar

## 🔄 Atualizações de Segurança

- Manter dependências atualizadas
- Verificar regularmente por vulnerabilidades
- Seguir as melhores práticas de segurança
- Fazer auditorias periódicas do código

---

**⚠️ Lembre-se**: A segurança é responsabilidade de todos. Sempre verifique antes de commitar! 