import paho.mqtt.client as mqtt


def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = mqtt.Client()
client.on_publish = on_publish
client.loop_start()

client.connect("HOSTNAME", "PORT", 60)
