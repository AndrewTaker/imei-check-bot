from telegram import Update
from telegram.ext import ContextTypes
from imeicheck.api_calls import ImeiService

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    service: ImeiService = context.application.bot_data.get("imei")

    if service:
        message = service.time()
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("NOPE")

