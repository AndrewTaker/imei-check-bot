import os
from imeicheck.api_calls import ImeiService
from bot.handlers import start
from telegram.ext import ApplicationBuilder, CommandHandler

# print(imei_service.check_device("869908051763278").model_dump_json(by_alias=True))

if __name__ == "__main__":
    IMEI_TOKEN: str | None = os.getenv("IMEI_TOKEN")
    TELEGRAM_BOT_TOKEN: str | None = os.getenv("TELEGRAM_BOT_TOKEN")

    imei_service = ImeiService("https://api.imeicheck.net", IMEI_TOKEN)

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    application.bot_data["imei"] = imei_service

    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.run_polling()
