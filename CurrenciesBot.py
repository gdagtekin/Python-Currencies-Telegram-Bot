import os
import logging
import Currencies
import Const
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

PORT = int(os.environ.get("PORT", "8443"))


def ping(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Çalışmaya devam ediyorum."
    )


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Merhaba! Döviz ve altın kurlarını sorgulayabilirsin. Komutları incele. ",
    )


def getUSD(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("ABD Doları", "USD")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getEUR(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("Euro", "EUR")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getGBP(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("İngiliz Sterlini", "GBP")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getCHF(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("İsviçre Frangı", "CHF")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getCAD(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("Kanada Doları", "CAD")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getRUB(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("Rus Rublesi", "RUB")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getJPY(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("Japon Yeni", "JPY")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getKWD(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("Kuveyt Dinarı", "KWD")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getPNL(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("Polonya Zlotisi", "PNL")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getCNY(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("Çin Yuanı", "CNY")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getUAH(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("Ukrayna Grivnası", "UAH")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getINR(update: Update, context: CallbackContext):
    message = Currencies.getCurrency("Hindistan Rupisi", "INR")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getGram(update: Update, context: CallbackContext):
    message = Currencies.getMetal("Gram Altın", "gram-altin")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getCeyrek(update: Update, context: CallbackContext):
    message = Currencies.getMetal("Çeyrek Altın", "ceyrek-altin")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getYarim(update: Update, context: CallbackContext):
    message = Currencies.getMetal("Yarım Altın", "yarim-altin")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getTam(update: Update, context: CallbackContext):
    message = Currencies.getMetal("Tam Altın", "tam-altin")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def get18Ayar(update: Update, context: CallbackContext):
    message = Currencies.getMetal("18 Ayar Altın", "18-ayar-altin")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def get22Ayar(update: Update, context: CallbackContext):
    message = Currencies.getMetal("22 Ayar Bilezik", "22-ayar-bilezik")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getGumus(update: Update, context: CallbackContext):
    message = Currencies.getMetal("Gümüş", "gumus")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def getOns(update: Update, context: CallbackContext):
    message = Currencies.getMetal("Altın ONS", "ons")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Böyle bir komut bulunmamaktadır."
    )


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(token=Const.TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the commands...
    dispatcher.add_handler(CommandHandler("ping", ping))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("dolar", getUSD))
    dispatcher.add_handler(CommandHandler("euro", getEUR))
    dispatcher.add_handler(CommandHandler("sterlin", getGBP))
    dispatcher.add_handler(CommandHandler("cinyuani", getCNY))
    dispatcher.add_handler(CommandHandler("isvicrefrangi", getCHF))
    dispatcher.add_handler(CommandHandler("kanadadolari", getCAD))
    dispatcher.add_handler(CommandHandler("rusrublesi", getRUB))
    dispatcher.add_handler(CommandHandler("japonyeni", getJPY))
    dispatcher.add_handler(CommandHandler("hindistanrupisi", getINR))
    dispatcher.add_handler(CommandHandler("kuveytdinari", getKWD))
    dispatcher.add_handler(CommandHandler("zloti", getPNL))
    dispatcher.add_handler(CommandHandler("ukraynagrivnasi", getUAH))
    dispatcher.add_handler(CommandHandler("gramaltin", getGram))
    dispatcher.add_handler(CommandHandler("ceyrekaltin", getCeyrek))
    dispatcher.add_handler(CommandHandler("yarimaltin", getYarim))
    dispatcher.add_handler(CommandHandler("tamaltin", getTam))
    dispatcher.add_handler(CommandHandler("ons", getOns))
    dispatcher.add_handler(CommandHandler("18ayaraltin", get18Ayar))
    dispatcher.add_handler(CommandHandler("22ayarbilezik", get22Ayar))
    dispatcher.add_handler(CommandHandler("gumus", getGumus))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # for local or polling
    # Start the Bot
    # updater.start_polling()

    # for heroku
    # Start the Bot
    updater.start_webhook(
         listen="0.0.0.0",
         port=PORT,
         url_path=Const.TOKEN,
         webhook_url=Const.HOST + Const.TOKEN,
    )

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
