import os
from functools import partial
from telegram import Update
from telegram.ext import (Application, CommandHandler, MessageHandler, filters, CallbackContext)
from Currencies import CurrencyFetcher
import Const

TOKEN = os.environ.get("TOKEN", Const.TOKEN)
PORT = int(os.environ.get("PORT", "8443"))

fetcher = CurrencyFetcher()

async def ping(update: Update, context: CallbackContext):
    await update.message.reply_text("Çalışmaya devam ediyorum.")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Merhaba! Döviz ve altın kurlarını sorgulayabilirsin. Komutları incele."
    )

async def get_currency(update: Update, context: CallbackContext, name: str, code: str):
    message = fetcher.get_currency(name, code)
    await update.message.reply_text(message)

async def get_metal(update: Update, context: CallbackContext, name: str, code: str):
    message = fetcher.get_metal(name, code)
    await update.message.reply_text(message)

async def unknown(update: Update, context: CallbackContext):
    await update.message.reply_text("Böyle bir komut bulunmamaktadır.")

def main():
    # Create the Application and pass it your bot's token.
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("start", start))

    # Currencies
    currencies = {
        "dolar": ("ABD Doları", "USD"),
        "euro": ("Euro", "EUR"),
        "sterlin": ("İngiliz Sterlini", "GBP"),
        "cinyuani": ("Çin Yuanı", "CNY"),
        "isvicrefrangi": ("İsviçre Frangı", "CHF"),
        "kanadadolari": ("Kanada Doları", "CAD"),
        "rusrublesi": ("Rus Rublesi", "RUB"),
        "japonyeni": ("Japon Yeni", "JPY"),
        "hindistanrupisi": ("Hindistan Rupisi", "INR"),
        "kuveytdinari": ("Kuveyt Dinarı", "KWD"),
        "zloti": ("Polonya Zlotisi", "PNL"),
        "ukraynagrivnasi": ("Ukrayna Grivnası", "UAH"),
    }

    # Register the currencies...
    for cmd, (name, code) in currencies.items():
        app.add_handler(CommandHandler(cmd, partial(get_currency, name=name, code=code)))

    # Metals
    metals = {
        "gramaltin": ("Gram Altın", "gram-altin"),
        "ceyrekaltin": ("Çeyrek Altın", "ceyrek-altin"),
        "yarimaltin": ("Yarım Altın", "yarim-altin"),
        "tamaltin": ("Tam Altın", "tam-altin"),
        "ons": ("Altın ONS", "ons"),
        "18ayaraltin": ("18 Ayar Altın", "18-ayar-altin"),
        "22ayarbilezik": ("22 Ayar Bilezik", "22-ayar-bilezik"),
        "gumus": ("Gümüş", "gumus"),
    }

    # Register the metals...
    for cmd, (name, code) in metals.items():
        app.add_handler(CommandHandler(cmd, partial(get_metal, name=name, code=code)))

    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    # For local
    # Start the Bot
    app.run_polling()

    # For heroku
    # Start the Bot
    #app.run_webhook(
    #    listen="0.0.0.0",
    #    port=PORT,
    #    url_path=Const.TOKEN,
    #    webhook_url=Const.HOST + Const.TOKEN,
    #)

if __name__ == "__main__":
    main()
