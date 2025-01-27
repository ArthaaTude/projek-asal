import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import requests

# Setup logging untuk debug
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Mendapatkan data dari CoinGecko
def get_crypto_price(crypto_name):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    if crypto_name in data:
        return data[crypto_name]["usd"]
    else:
        return None

# Start Command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Halo! Saya bot cryptocurrency. Tanyakan harga coin dengan format: /price <coin_name>")

# Price Command
async def price(update: Update, context: CallbackContext) -> None:
    if context.args:
        crypto_name = context.args[0].lower()
        price = get_crypto_price(crypto_name)
        if price:
            await update.message.reply_text(f"Harga {crypto_name} saat ini adalah ${price}.")
        else:
            await update.message.reply_text(f"Maaf, saya tidak bisa menemukan harga untuk {crypto_name}.")
    else:
        await update.message.reply_text("Silakan masukkan nama cryptocurrency setelah /price.")

# Error handling
async def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f"Update {update} caused error {context.error}")

def main():
    # Masukkan token API bot yang diberikan oleh BotFather
    application = Application.builder().token("7869705949:AAEaM7AjFhCOuJiQ3GKo_ICjvKnSey6L6QQ").build()
    
    # Daftarkan handler untuk /start dan /price
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("price", price))

    # Log semua error
    application.add_error_handler(error)

    # Mulai bot
    application.run_polling()

if __name__ == '__main__':
    main()