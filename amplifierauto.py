from paho.mqtt import client as mqtt_client
import random
import time

testing = False

broker = '10.0.1.10'
port = 1883
topic = "python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, file_to_open):
    msg_count = 0
    last_result = "initialized"
    new_info = False
    while True:
        time.sleep(1)

        with open(file_to_open) as f:
            lines = f.readline()
            print(lines)

        audio_running = state_of_audio(lines)

        if last_result == audio_running:
            new_info = False
        elif not last_result == audio_running:
            new_info = True

        msg = f"messages: {msg_count}"
        # result = client.publish(topic, msg)
        # result: [0, 1]
        # status = result[0]
        if new_info:
            print(f"Send `{msg}` to topic `{topic}`")
            print(f"[{msg_count}] {audio_running}")
            last_result = audio_running
            if audio_running == "On":
                msg = "On"
                client.publish(topic, msg)
            elif audio_running == "Off":
                msg = "Off"
                client.publish(topic, msg)
        else:
            print(f"[{msg_count}] State of amplifier has not changed. No news to publish")
        msg_count += 1

def state_of_audio(input):
    if "state: RUNNING" in input:
        return "On"
    elif "closed" in input:
        return "Off"


def main():
    if testing:
        file_to_open = "test.txt"
        # with open("test.txt") as f:
        #     lines = f.readline()
        #     status(lines)
    else:
        file_to_open = "/proc/asound/card1/pcm0p/sub0/status"
        # with open("/proc/asound/card1/pcm0p/sub0/status") as f:
        #     lines = f.readline()
        #     status(lines)
    client = connect_mqtt()
    client.loop_start()
    publish(client, file_to_open)

if __name__ == "__main__":
    main()