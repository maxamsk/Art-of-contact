import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Для себя"],
        ["Для пары"],
        ["События"],
        ["О Марии"]
    ]

    await update.message.reply_text(
        "💜 Добро пожаловать в Искусство контакта\n\nВыберите раздел:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Для себя":
        answer = "💜 Self Tantra\n\n• Запись практики\n• Индивидуальная практика 1:1"

    elif text == "Для пары":
        answer = "💜 Практики для пары\n\n• Онлайн запись\n• Индивидуальная сессия для пары"

    elif text == "События":
        answer = "💜 События\n\n• Мастер-класс Искусство контакта\n• Каддл / практика осознанного контакта"

    elif text == "О Марии":
        answer = "Мария Маевская 💜\n\nФасилитатор осознанного контакта"

    else:
        answer = "Выберите раздел ниже 💜"

    await update.message.reply_text(answer)


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message))

app.run_polling()