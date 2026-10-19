# Biblioteca

Aplicação Python para gerenciamento de uma biblioteca.

## Preparação

Crie e ative o ambiente virtual no PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

## Execução

```powershell
python main.py
```

## Configuração

Use o arquivo `.env` para configurações locais. Evite versionar chaves, senhas ou tokens; prefira manter um `.env.example` sem dados sensíveis caso o projeto passe a usar essas variáveis.
