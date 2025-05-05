from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from bot.keyboards.onboarding_keyboard import termos_keyboard, confirmacao_keyboard
from bot.utils.validators import validar_nome, validar_email, validar_cpf
from bot.handlers.menu import enviar_menu
from bot.database import cadastrar_usuario, aceitar_termos, usuario_ja_cadastrado, atualizar_dados_usuario, verificar_e_atualizar_saldo_furiacash, obter_saldo_furiacash
from datetime import date

TERMO, NOME, CONF_NOME, EMAIL, CONF_EMAIL, CPF, CONF_CPF, FINAL = range(8)

dados_usuario = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    telegram_id = user.id
    nome = user.full_name
    username = user.username

    await cadastrar_usuario(telegram_id, nome, username)
    
    if await usuario_ja_cadastrado(telegram_id):
        await update.message.reply_text("🐾 Você já está cadastrado! Vamos direto ao menu. 👇")
        await enviar_menu(update, context)
        return ConversationHandler.END
    
    mensagem_inicial = (
        "🐾 Fala, guerreiro(a)! Aqui é o contato inteligente da FURIA!\n\n"
        "Quer ficar por dentro de tudo? Desde a história da FURIA, nossos times, acompanhar jogos ao vivo, "
        "campeonato de clipadores, vagas de trabalho, trend topics, comunidade, até acompanhar os streamers ao vivo? "
        "Tá tudo aqui!\n\nAinda rola pedir dicas de looks na lojinha e agilizar suas compras!\n\n"
        "E o melhor: várias interações fazem você acumular FURIA Cash, que podem virar prestígio, recompensas, "
        "experiências exclusivas e muito mais! 🖤🔥\n\nVem ganhar junto com a FURIA! 👊"
    )
    await update.message.reply_text(mensagem_inicial)

    mensagem_termos = (
        "🚨 Pra começar essa resenha, só falta você aceitar os termos aqui embaixo! 👇\n"
        "https://terms.furia.gg/"
    )
    await update.message.reply_text(mensagem_termos, reply_markup=termos_keyboard())
    return TERMO

async def tratar_termos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id

    if query.data == "aceito_termos":
        await aceitar_termos(user_id)
        
        dados_usuario[user_id] = {}
        await query.edit_message_text("🐾 Show! Agora manda aí... Qual o teu nome completo?")
        return NOME
    else:
        await query.edit_message_text("🚨 Que pena! Se mudar de ideia, é só chamar a gente aqui! 🖤🔥")
        return ConversationHandler.END

async def receber_nome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.message.text.strip()
    if not validar_nome(nome):
        await update.message.reply_text("❌ Nome inválido. Informe seu nome completo (nome e sobrenome).")
        return NOME

    dados_usuario[update.message.from_user.id]['nome'] = nome
    await update.message.reply_text(f"Podemos confirmar a sua informação: {nome}?", reply_markup=confirmacao_keyboard("nome"))
    return CONF_NOME

async def tratar_nome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == "confirmar_nome":
        await query.edit_message_text("E qual é o seu email?")
        return EMAIL
    else:
        await query.edit_message_text("Qual o seu nome completo?")
        return NOME

async def receber_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    email = update.message.text.strip()
    if not validar_email(email):
        await update.message.reply_text("❌ Email inválido. Informe um email válido (exemplo: nome@email.com).")
        return EMAIL

    dados_usuario[update.message.from_user.id]['email'] = email
    await update.message.reply_text(f"Podemos confirmar a sua informação: {email}?", reply_markup=confirmacao_keyboard("email"))
    return CONF_EMAIL

async def tratar_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == "confirmar_email":
        await query.edit_message_text("Opcional: Quer inserir seu CPF e ganhar recompensas 🎁 e prestígio 🏆 na nossa comunidade?")
        return CPF
    else:
        await query.edit_message_text("Qual o seu email?")
        return EMAIL

async def receber_cpf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cpf = update.message.text.strip()
    if not validar_cpf(cpf):
        await update.message.reply_text("❌ CPF inválido. Informe um CPF com 11 dígitos (só números ou com pontos/traço).")
        return CPF

    dados_usuario[update.message.from_user.id]['cpf'] = cpf
    await update.message.reply_text(f"Podemos confirmar a sua informação: {cpf}?", reply_markup=confirmacao_keyboard("cpf"))
    return CONF_CPF

async def tratar_cpf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == "confirmar_cpf":
        await query.edit_message_text("✅ Cadastro finalizado!")

        # ✨ Atualiza os dados no banco
        nome = dados_usuario[user_id].get('nome', '')
        email = dados_usuario[user_id].get('email', '')
        cpf = dados_usuario[user_id].get('cpf', '')
        await atualizar_dados_usuario(user_id, nome, email, cpf)

        await finalizar_cadastro(update, context, user_id)
        return ConversationHandler.END
    else:
        await query.edit_message_text("Qual o seu CPF?")
        return CPF

async def finalizar_cadastro(update: Update, context: ContextTypes.DEFAULT_TYPE, user_id):
    nome = dados_usuario[user_id].get('nome', 'Nome não encontrado')
    cpf = dados_usuario[user_id].get('cpf', None)
    
    saldo_atualizado = await verificar_e_atualizar_saldo_furiacash(user_id, cpf)
    saldo = await obter_saldo_furiacash(user_id)
    
    if saldo_atualizado:
        await update.effective_chat.send_message("Seu saldo foi atualizado! 🎉")
    
    await update.effective_chat.send_message("⚠️ Esse contato inteligente está na versão beta e pode conter bugs e informações imprecisas. ⚠️")
    await update.effective_chat.send_message(
        f"E aí, FUR {nome} 🇧🇷\n"
        f"Seu saldo é de ${saldo:.2f} FURIA Cash.\n\n"
        "Agora você já pode acessar nosso menu e interagir com tudo! 🖤🔥"
    )
    await enviar_menu(update, context)

onboarding_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Command("start"), start)],
    states={
        TERMO: [CallbackQueryHandler(tratar_termos, pattern="^aceito_termos$|^recusar_termos$")],
        NOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_nome)],
        CONF_NOME: [CallbackQueryHandler(tratar_nome, pattern="^confirmar_nome$|^alterar_nome$")],
        EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_email)],
        CONF_EMAIL: [CallbackQueryHandler(tratar_email, pattern="^confirmar_email$|^alterar_email$")],
        CPF: [MessageHandler(filters.TEXT & ~filters.COMMAND, receber_cpf)],
        CONF_CPF: [CallbackQueryHandler(tratar_cpf, pattern="^confirmar_cpf$|^alterar_cpf$")],
    },
    fallbacks=[],
)