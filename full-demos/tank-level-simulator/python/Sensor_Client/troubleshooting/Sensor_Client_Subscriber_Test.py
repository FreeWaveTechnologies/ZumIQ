import paho.mqtt.client as mqtt
''' This client is only a subscriber to see/monitor
    what is being published from "demo/sensors" topic '''

def on_connect(client, userdata, rc):
    ''' We subscribe to topics only after a successful 
    connection because if connection is lost and regained,
     subscriptions will be renewed. '''
    print("Connected with result code", str(rc))
    client.subscribe("demo/sensors")
    
def on_message(client, userdata, msg):
    ''' callback for when messages are published to
     broker on any channel we are subscribed to. '''
    print  (msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1890, 60)

client.loop_forever()
