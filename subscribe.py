#!/usr/bin/env python3
import paho.mqtt.client as mqtt

TOPIC = "sensors/temp"

def on_message(client, userdata, msg):
    print(f"{msg.topic} → {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe(TOPIC)
client.loop_forever()
