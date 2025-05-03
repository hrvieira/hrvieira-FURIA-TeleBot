import telebot;
from telebot import types;

bot = telebot.TeleBot('');

dados_usuario = {}

@bot.message_handler(commands=['start'])
def start(msg: telebot.types.Message):
    """
    Função para lidar com o comando /start. Apresenta o bot e os termos de uso.
    """
    markup = types.InlineKeyboardMarkup()
    btn_aceito_termos = types.InlineKeyboardButton(text="Aceito", callback_data="aceito_termos")
    btn_recusar_termos = types.InlineKeyboardButton(text="Não aceito", callback_data="recusar_termos")
    markup.add(btn_aceito_termos, btn_recusar_termos)

    mensagem_inicial = ("🐾 Fala, guerreiro(a)! Aqui é o contato inteligente da FURIA!\n\n"
                        "Quer ficar por dentro de tudo? Desde a história da FURIA, nossos times, acompanhar jogos ao vivo, "
                        "campeonato de clipadores, vagas de trabalho, trend topics, comunidade, até acompanhar os streamers ao vivo? "
                        "Tá tudo aqui!\n\nAinda rola pedir dicas de looks na lojinha e agilizar suas compras!\n\n"
                        "E o melhor: várias interações fazem você acumular FURIA Cash, que podem virar prestígio, recompensas, "
                        "experiências exclusivas e muito mais! 🖤🔥\n\nVem ganhar junto com a FURIA! 👊")
    bot.reply_to(msg, mensagem_inicial)

    mensagem_termos = ("🚨 Pra começar essa resenha, só falta você aceitar os termos aqui embaixo! 👇\n"
                       "https://terms.furia.gg/")
    bot.send_message(msg.chat.id, mensagem_termos, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["aceito_termos", "recusar_termos"])
def termos_furia(call: types.CallbackQuery):
    """
    Função para lidar com a resposta aos termos de uso (aceitar ou recusar).
    """
    if call.data == "aceito_termos":
        bot.send_message(call.message.chat.id, "🐾 Show! Agora manda aí... Qual o teu nome completo?")
        # Armazena o ID do chat para usar nas próximas interações
        dados_usuario['chat_id'] = call.message.chat.id
        bot.register_next_step_handler(call.message, nome_usuario)
    elif call.data == "recusar_termos":
        bot.send_message(call.message.chat.id, "🚨 Que pena! Se mudar de ideia, é só chamar a gente aqui! 🖤🔥")

def nome_usuario(msg: telebot.types.Message):
    """
    Função para obter e confirmar o nome do usuário.
    """
    nome = msg.text
    dados_usuario['nome'] = nome #armazena o nome
    markup = types.InlineKeyboardMarkup()
    btn_confirmar_nome = types.InlineKeyboardButton(text="Confirmar nome", callback_data="confirmar_nome")
    btn_alterar_nome = types.InlineKeyboardButton(text="Alterar nome", callback_data="alterar_nome")
    markup.add(btn_confirmar_nome, btn_alterar_nome)
    bot.send_message(msg.chat.id, f"Podemos confirmar a sua informação: {nome}?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["confirmar_nome", "alterar_nome"])
def tratar_nome(call: types.CallbackQuery):
    """
    Função para tratar a confirmação ou alteração do nome do usuário.
    """
    if call.data == "confirmar_nome":
        bot.send_message(call.message.chat.id, "E qual é o seu email?")
        bot.register_next_step_handler(call.message, email_usuario)
    elif call.data == "alterar_nome":
        bot.send_message(call.message.chat.id, "Qual o seu nome completo?")
        bot.register_next_step_handler(call.message, nome_usuario)

def email_usuario(msg: telebot.types.Message):
    """
    Função para obter e confirmar o email do usuário.
    """
    email = msg.text
    dados_usuario['email'] = email #armazena o email
    markup = types.InlineKeyboardMarkup()
    btn_confirmar_email = types.InlineKeyboardButton(text="Confirmar email", callback_data="confirmar_email")
    btn_alterar_email = types.InlineKeyboardButton(text="Alterar email", callback_data="alterar_email")
    markup.add(btn_confirmar_email, btn_alterar_email)
    bot.send_message(msg.chat.id, f"Podemos confirmar a sua informação: {email}?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["confirmar_email", "alterar_email"])
def tratar_email(call: types.CallbackQuery):
    """
    Função para tratar a confirmação ou alteração do email do usuário.
    """
    if call.data == "confirmar_email":
        bot.send_message(call.message.chat.id, "Opcional: Quer inserir seu CPF e ganhar recompensas 🎁 e prestígio 🏆 na nossa comunidade? (uso exclusivo para isso).")
        bot.register_next_step_handler(call.message, cpf_usuario)
    elif call.data == "alterar_email":
        bot.send_message(call.message.chat.id, "Qual o seu Email?")
        bot.register_next_step_handler(call.message, email_usuario)

def cpf_usuario(msg: telebot.types.Message):
    """
    Função para obter e confirmar o CPF do usuário.
    """
    cpf = msg.text
    dados_usuario['cpf'] = cpf #armazena o cpf
    markup = types.InlineKeyboardMarkup()
    btn_confirmar_cpf = types.InlineKeyboardButton(text="Confirmar CPF", callback_data="confirmar_cpf")
    btn_alterar_cpf = types.InlineKeyboardButton(text="Alterar CPF", callback_data="alterar_cpf")
    markup.add(btn_confirmar_cpf, btn_alterar_cpf)
    bot.send_message(msg.chat.id, f"Podemos confirmar a sua informação: {cpf}?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["confirmar_cpf", "alterar_cpf"])
def tratar_cpf(call: types.CallbackQuery):
    """
    Função para tratar a confirmação ou alteração do CPF do usuário.
    """
    if call.data == "confirmar_cpf":
        # Agora que temos os dados do usuário, podemos usar um dicionário
        nome = dados_usuario.get('nome', 'Nome não encontrado')
        email = dados_usuario.get('email', 'Email não encontrado')
        cpf = dados_usuario.get('cpf', 'CPF não encontrado')

        alerta_bot = ("⚠️ Esse contato inteligente está na versão beta e pode conter bugs e informações imprecisas. ⚠️")
        mensagem_final = (
            f"E aí, FUR {nome} 🇧🇷\n"  # Usa o nome armazenado
            "Seu saldo é de $0,99 FURIA Cash.\n\n"
            "⚡ Acompanhe jogos ao vivo\n\n"
            "🎯 Campeonato de Clipadores\n\n"
            "📅 Calendário de Jogos\n\n"
            "🛒 Lojinha da Pantera\n\n"
            "📰 Esports News / Trend Topics\n\n"
            "🎥 Criadores de Conteúdo e Streamers\n\n"
            "🤑 FURIA Cash\n\n"
            "💬 Ligar Modo Bate Papo"
        )
        bot.send_message(call.message.chat.id, alerta_bot)
        bot.send_message(call.message.chat.id, mensagem_final)
        menu(call.message) #chama o menu
    elif call.data == "alterar_cpf":
        bot.send_message(call.message.chat.id, "Qual o seu CPF?")
        bot.register_next_step_handler(call.message, cpf_usuario)

def menu(msg: telebot.types.Message):
    """
    Função para exibir o menu principal do bot.
    """
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    btn_acompanhe_jogos = types.KeyboardButton(text="Acompanhe jogos ao vivo")
    btn_campeonato_clipadores = types.KeyboardButton(text="Campeonato de Clipadores")
    btn_calendario_jogos = types.KeyboardButton(text="Calendário de Jogos")
    btn_lojinha = types.KeyboardButton(text="Lojinha da Pantera")
    btn_esports_news = types.KeyboardButton(text="Esports News / Trend Topics")
    btn_criadores = types.KeyboardButton(text="Criadores de Conteúdo e Streamers")
    btn_furia_cash = types.KeyboardButton(text="FURIA Cash")

    markup.add(btn_acompanhe_jogos, btn_campeonato_clipadores, btn_calendario_jogos, 
               btn_lojinha, btn_esports_news, btn_criadores, btn_furia_cash)

    mensagem_menu = "Selecione uma opção no menu ou me mande uma mensagem (texto) que eu te passo a call!"
    bot.send_message(msg.chat.id, mensagem_menu, reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text in [
    "Acompanhe jogos ao vivo",
    "Campeonato de Clipadores",
    "Calendário de Jogos",
    "Lojinha da Pantera",
    "Esports News / Trend Topics",
    "Criadores de Conteúdo e Streamers",
    "FURIA Cash"
])
def opcoes_menu(msg: telebot.types.Message):
    """
    Função para lidar com as opções escolhidas no menu principal.
    """
    opcoes = {
        "Acompanhe jogos ao vivo": "Aqui você pode acompanhar os jogos ao vivo da FURIA!",
        "Campeonato de Clipadores": "Aqui você pode acompanhar o campeonato de clipadores!",
        "Calendário de Jogos": "Aqui você pode acompanhar o calendário de jogos!",
        "Lojinha da Pantera": "Aqui você pode acessar a lojinha da Pantera!",
        "Esports News / Trend Topics": "Aqui você pode acompanhar as notícias e trend topics do mundo dos esports!",
        "Criadores de Conteúdo e Streamers": "Aqui você pode acompanhar os criadores de conteúdo e streamers da FURIA!",
        "FURIA Cash": "Aqui você pode acompanhar seu saldo de FURIA Cash!"
    }
    # Busca a resposta no dicionário, se não encontrar, retorna uma mensagem padrão
    resposta = opcoes.get(msg.text, "Opção não reconhecida.")
    bot.send_message(msg.chat.id, resposta)

bot.infinity_polling();
