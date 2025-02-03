import os
from imeicheck.api_calls import ImeiService

IMEI_TOKEN: str | None = os.getenv("IMEI_TOKEN")
TELEGRAM_BOT_TOKEN: str | None = os.getenv("TELEGRAM_BOT_TOKEN")

imei_service = ImeiService("https://api.imeicheck.net", IMEI_TOKEN)
print(imei_service)
