#!/usr/bin/env python3
import sys
import paho.mqtt.client as mqtt

TOPIC = "sensors/temp"
MESSAGE = sys.argv[1] if len(sys.argv) > 1 else "22.0"

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.publish(TOPIC, MESSAGE)
client.disconnect()

print(f"Published '{MESSAGE}' to topic '{TOPIC}'")
