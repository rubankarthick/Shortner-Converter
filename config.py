# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25632035"))
API_HASH = os.environ.get("API_HASH", "896d8f9929d3e00d2dae14646329fe3b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6280177829:AAFm9UqIH2Dej-7Vth0XTLRML8n723nnJcc")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "RubanShort")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://ruban9820:karthi9820@shortner.cx4lgyv.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6094386527")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(6094386527)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001721952363")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "re_offcial") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/0988488e0d6fcf7bb3fd3.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "True"
