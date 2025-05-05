# 🐍🤖 teleFuria

Um bot do Telegram desenvolvido em Python para interagir com usuários, acumular FURIA Cash e fornecer acesso a conteúdos exclusivos da FURIA.

## ⚙️ Pré-requisitos

- Python 3.x instalado
- Conta no [Telegram](https://telegram.org/) com um bot criado via [BotFather](https://core.telegram.org/bots#6-botfather)
- Banco de dados (como **PostgreSQL**) configurado com a tabela de usuarios e saldo_furiacash.

## 🚀 Tecnologias

- Python 3.x
- [Telegram Bot API](https://core.telegram.org/bots/api)
- python-dotenv
- [asyncpg](https://github.com/MagicStack/asyncpg) para interação com o banco de dados PostgreSQL.

## 📦 Instalação

1. **Clone o repositório**

```bash
git clone https://github.com/hrvieira/hrvieira-FURIA-TeleBot.git
cd hrvieira-FURIA-TeleBot
```

2. **Crie o ambiente virtual e ative**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
- Crie um arquivo **.env** baseado no **.env.example**:

```bash
cp .env.example .env
```
- Edite o **.env** e insira sua chave da API do Telegram, além das configurações de banco de dados (usuário, senha, host, etc.).

5. **Configure o banco de dados**

Configure um banco de dados PostgreSQL (ou outro de sua escolha) e crie a tabela usuarios para armazenar os dados dos usuários e o saldo do FURIA Cash.

## ▶️ Uso

```bash
python main.py
```

## 🛠️ Desenvolvimento

- As configurações de variáveis de ambiente estão centralizadas em **utils/config.py**

- As imagens utilizadas estão na pasta **/img**

## 📝 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

## 🤝 Contribuição
Pull requests são bem-vindos! Para mudanças importantes, abra uma issue antes para discutir o que você gostaria de mudar.