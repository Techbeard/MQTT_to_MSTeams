import paho.mqtt.client as mqtt
import pymsteams
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('DEBUG'))



myTeamsMessage = pymsteams.connectorcard("<Microsoft Webhook_URL>")
myTeamsMessage.text("this is my text")
myTeamsMessage.send()