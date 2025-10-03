import os

## Code Written By @ItsMeMaster (modified to support env vars)

class Config(object):
    # Bot token from BotFather
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8434843795:AAFamCgCGaQXXvTDkJ4FWpHnu_Dv4MmKxxE")

    # MongoDB database name
    DB_NAME = os.getenv("DB_NAME", "txtbot")

    # Telegram API credentials (from https://my.telegram.org)
    API_ID = int(os.getenv("API_ID", "22849789"))
    API_HASH = os.getenv("API_HASH", "0fc127c6055acd59f00ec6c229e1e3c4")

    # Admin user ID
    ADMIN_ID = int(os.getenv("ADMIN_ID", "7296271316"))

    # MongoDB connection string
    DB_URL = os.getenv(
        "DB_URL",
        "mongodb+srv://autoappx750:Yash2835P@autoappx.drvhbnu.mongodb.net/?retryWrites=true&w=majority&appName=Autoappx"
    )

    # Log channel ID
    LOG_CHANNEL = os.getenv("LOG_CHANNEL", "-1002477114210")

    # Optional links
    USERLINK = os.getenv("USERLINK", "")
    TUTORIAL_VIDEO = os.getenv("TUTORIAL_VIDEO", "")
