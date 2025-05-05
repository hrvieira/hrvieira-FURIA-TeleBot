import asyncpg
import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT'))
}

async def get_db_connection():
    return await asyncpg.connect(**DB_CONFIG)

async def cadastrar_usuario(telegram_id, nome, username):
    conn = await get_db_connection()
    
    await conn.execute('''
        INSERT INTO usuarios (telegram_id, nome, username, saldo_furiacash)
        VALUES ($1, $2, $3, $4)
        ON CONFLICT (telegram_id) DO NOTHING;
    ''', telegram_id, nome, username, 0.99)
    await conn.close()

async def aceitar_termos(telegram_id):
    conn = await get_db_connection()
    await conn.execute('''
        UPDATE usuarios
        SET aceitou_termos = TRUE,
            ultima_interacao = NOW()
        WHERE telegram_id = $1;
    ''', telegram_id)
    await conn.close()

async def atualizar_dados_usuario(telegram_id, nome, email, cpf):
    cpf_limpo = ''.join(filter(str.isdigit, cpf))

    conn = await get_db_connection()
    await conn.execute('''
        UPDATE usuarios
        SET nome = $1,
            email = $2,
            cpf = $3,
            ultima_interacao = NOW()
        WHERE telegram_id = $4;
    ''', nome, email, cpf_limpo, telegram_id)
    await conn.close()
    
async def obter_saldo_furiacash(telegram_id):
    conn = await get_db_connection()
    resultado = await conn.fetchrow('''
        SELECT saldo_furiacash
        FROM usuarios
        WHERE telegram_id = $1;
    ''', telegram_id)
    await conn.close()

    if resultado:
        return resultado['saldo_furiacash']
    else:
        return None
    
async def verificar_e_atualizar_saldo_furiacash(telegram_id, cpf):
    conn = await get_db_connection()

    if not cpf:
        await conn.close()
        return False, None

    resultado = await conn.fetchrow('''
        SELECT ultima_interacao, saldo_furiacash
        FROM usuarios
        WHERE telegram_id = $1;
    ''', telegram_id)

    if resultado:
        ultima_interacao = resultado['ultima_interacao']
        saldo_atual = resultado['saldo_furiacash']

        if ultima_interacao and ultima_interacao.date() == date.today():
            await conn.close()
            return False, saldo_atual

        novo_saldo = saldo_atual + 0.10
        await conn.execute('''
            UPDATE usuarios
            SET saldo_furiacash = $1,
                ultima_interacao = NOW()
            WHERE telegram_id = $2;
        ''', novo_saldo, telegram_id)

        await conn.close()
        return True, novo_saldo

    await conn.close()
    return False, None