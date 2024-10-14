import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Налаштовуємо журналювання
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота
TOKEN = ''  # Замініть на свій токен

# Функція, яка запускається при команді /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ласкаво просимо до бота!")

# Основна функція для запуску бота
async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))

    logger.info("Бот працює. Натисни Ctrl+C для зупинки.")
    await application.run_polling()

# Запуск основної функції
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
