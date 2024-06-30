import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23695696"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fb8710f5ea9c2f87dd77c90352371f12")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://atlas-sample-dataset-load-6681874267bd38197b6112c2:AQR11nThlqGcIaag@cluster0.hswulu7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
