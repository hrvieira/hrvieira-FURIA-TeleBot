# 🐍🤖 teleFuria

Um bot do Telegram desenvolvido em Python.  
O objetivo é automatizar o envio de mensagens e facilitar a interação com usuários diretamente no chat do Telegram.

## ⚙️ Pré-requisitos

- Python 3.x instalado
- Conta no [Telegram](https://telegram.org/) com um bot criado via [BotFather](https://core.telegram.org/bots#6-botfather)

## 🚀 Tecnologias

- Python 3.x
- [Telegram Bot API](https://core.telegram.org/bots/api)
- python-dotenv

## 📦 Instalação

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/teleFuria.git
cd teleFuria
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
- Edite o **.env** e insira sua chave da API do Telegram.

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