from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def termos_keyboard():
    buttons = [
        [InlineKeyboardButton("Aceito", callback_data="aceito_termos")],
        [InlineKeyboardButton("Não aceito", callback_data="recusar_termos")],
    ]
    return InlineKeyboardMarkup(buttons)

def confirmacao_keyboard(tipo):
    data_confirmar = f"confirmar_{tipo}"
    data_alterar = f"alterar_{tipo}"
    buttons = [
        [InlineKeyboardButton("Confirmar", callback_data=data_confirmar)],
        [InlineKeyboardButton("Alterar", callback_data=data_alterar)],
    ]
    return InlineKeyboardMarkup(buttons)