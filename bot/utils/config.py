import os
from dotenv import load_dotenv

load_dotenv()

def get_telegram_api_key() -> str:
    telegram_api_key = os.getenv('TELEGRAM_API_KEY')
    if not telegram_api_key or not telegram_api_key.strip():
        raise EnvironmentError("❌ A chave da API do Telegram não foi encontrada ou está vazia. Verifique se o arquivo .env contém a variável TELEGRAM_API_KEY.")
    return telegram_api_key.strip()

bot_token = get_telegram_api_key();
