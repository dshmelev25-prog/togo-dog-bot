import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение токена бота из переменных окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я бот для ToGo Dog. Чем могу помочь?"
    )

# Обработчик текстовых сообщений
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    await update.message.reply_text(f"Вы написали: {text}")

# Обработчик фотографий
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Спасибо за фото!")

# Обработчик стикеров
async def handle_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Классный стикер!")

def main() -> None:
    # Создание приложения бота
    application = Application.builder().token(TOKEN).build()

    # Регистрация обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(MessageHandler(filters.STICKER, handle_sticker))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
