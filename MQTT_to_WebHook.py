import paho.mqtt.client as mqtt
import pymsteams
import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

load_dotenv()
print(os.getenv('DEBUG'))

myTeamsMessage = pymsteams.connectorcard(os.getenv('MS_WebHook'))

def on_connect(mqttc, obj, flags, rc):
    print("Connected to %s:%s" % (mqttc._host, mqttc._port))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    myTeamsMessage.text(msg.payload.decode())
    myTeamsMessage.send()

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

mqttc.connect(os.getenv('MQTT_Server'), os.getenv('MQTT_Port'))
mqttc.subscribe(os.getenv('Sub_Topic'), 0)


rc = 0
while rc == 0:
    rc = mqttc.loop()



