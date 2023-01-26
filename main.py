import logging
import config
from requests import get
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Commands:
async def locate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("IP request received")
    public_ip = get('https://api.ipify.org').text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{config.HOSTNAME} is at {public_ip}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(config.TOKEN).build()
    
    # Handlers
    where_handler = CommandHandler('locate', locate, filters.Chat(chat_id=config.CHAT_ID))
    application.add_handler(where_handler)

    application.run_polling()
