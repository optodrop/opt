import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import asyncio
import nest_asyncio  # Додаємо цю бібліотеку

nest_asyncio.apply()  # Додаємо цю строку перед запуском вашого бота

# Налаштовуємо журналювання
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

import os
TOKEN = os.getenv('TOKEN')  # Читаємо токен із змінної оточення

# Функція, яка запускається при команді /start
async def start(update: Update, context: CallbackContext):
    try:
        # Отримуємо ім'я користувача
        user_first_name = update.effective_user.first_name

        # Надсилаємо фотографію
        await context.bot.send_photo(chat_id=update.effective_chat.id,
                                     photo='https://optodrop.com.ua/image/catalog/blog/blog5.jpg')

        # Створюємо кнопки
        keyboard = [
            [InlineKeyboardButton("Перейти на сайт", url='https://optodrop.com.ua/')],
            [InlineKeyboardButton("Зв'язатися з менеджером", url='https://t.me/ibanan_ua')],
            [InlineKeyboardButton("Підписатись на канал", url='https://t.me/+_XAQaKaIPMcwZjMy')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Текст привітання
        welcome_text = f"""
👋 {user_first_name}, раді вітати вас у боті OPTODROP!

🔹 OPTODROP — перший у світі магазин мобільних аксесуарів та інших товарів за найкращими цінами!
🔹 Широкий асортимент: Понад 10,000+ товарів для будь-якого смаку та бюджету.
🔹 Найкращі ціни: Прямий імпорт від брендів Hoco, Baseus, iNobi, Borofone, Remax та інші.
🔹 Швидка доставка: Замовляйте сьогодні — отримуйте вже завтра!
🔹 Професійна підтримка: Наші менеджери завжди на зв'язку й готові допомогти!

👇 Оберіть одну з опцій, щоб продовжити!
"""
        # Надсилаємо повідомлення
        await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text, reply_markup=reply_markup)

    except Exception as e:
        logger.error(f"Error occurred while sending photo or message: {e}")

# Основна функція для запуску бота
async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    print("Бот працює. Натисни Ctrl+C для зупинки.")
    await application.run_polling()

# Запуск основної функції
if __name__ == '__main__':
    asyncio.run(main())  # Використовуємо asyncio.run() для запуску
