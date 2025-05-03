import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

def get_telegram_api_key() -> str:
    """
    Retorna a chave da API do Telegram validada.
    Lança um erro se a variável não estiver definida.
    """
    telegram_api_key = os.getenv('TELEGRAM_API_KEY')
    if telegram_api_key is None:
        raise EnvironmentError("❌ A chave da API do Telegram não foi encontrada. Verifique se o arquivo .env contém a variável TELEGRAM_API_KEY.")
    return telegram_api_key


""" def get_database_url() -> str:
    db_url = os.getenv('DATABASE_URL')
    if db_url is None:
        raise EnvironmentError("❌ DATABASE_URL não encontrada.")
    return db_url """
