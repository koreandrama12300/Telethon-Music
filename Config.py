import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 9339644529:AAE_Ug83a1BOGbqWl9vQ6cmTAnNz2ycwB5s)
    STRING_SESSION = os.environ.get("STRING_SESSION", BQAmCkokq9hFVY1cIDltCdPn_35HGg11zmXkaaZe5K8jxHI0Mr7wEG8_7Yj4cjlHO6vPRNFdQQ65R3txN2o3ghIDG8d4XvxGLw-49CGD2XmzD7zvG4QNJHlXqfuOSdf4WR4FmS6VIyoymceSFVqt_nzbIaOq2PhjpcKEkqezxvfJ1Sl9zYvAq55RaAWXxmTysz_HL8S1GhfMQM-O0-3bedEFS_Bvr-WdYAGNlSsC5XOc8fHNq1DP_5tSTH-GQyik_LSMFhebYt9lLCWL2_sFBkmi8sIYml5IYfZiBx154siJcU57yRNMXOdwT61JcfyUhujdIE1mzAAN26aQ1i2uvcDhAAAAAVrwuVEA)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "koreandrama1230bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
