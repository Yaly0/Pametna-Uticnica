import network
import socket
import binascii
import machine
from mqtt import MQTTClient
from machine import Pin, PWM
import time


# the function that gets executed after a message is received, which is detected by client.check_msg()
def sub_cb(topic, msg):
    if msg != b'0':
        print(msg)
    if msg == b'OFF':
        relay.off()
        led.duty(1013)  # pin 2 is inverted, so 0 is max, and 1023 is min
    elif msg == b'ON':
        relay.on()
        led.duty(0)


def get_creds():
    ap_ssid = 'Puticnica'
    ap_password = '123456789'
    ap_auth_mode = 3
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ap_ssid, password=ap_password, authmode=ap_auth_mode)
    s = socket.socket()
    s.bind(('', 80))
    s.listen(5)

    while 1:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)
        if request.find("--->") == -1:  # mobile app sends credentials as: --->ssid,password
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.close()
            continue
        else:
            creds = request[request.find("--->") + 4:-1]
            ssid = creds.split(",")[0]
            password = creds.split(",")[1]
            station.active(False)  # this line is needed if first connection fails and user needs to try again
            station.active(True)
            start = time.time()
            station.connect(ssid, password)
            print('before: ' + str(station.status()))
            while not station.isconnected():
                if time.time() - start > 20:  # timeout = 20s
                    break
            print('after: ' + str(station.status()))
            print(ssid, password)
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/plain\n')
            conn.send('Content-Length: 1')
            conn.send('Connection: close\n\n')
            conn.send(str(station.status()))
            conn.close()
            if station.status() != 5:  # status 5: connection successful
                continue
            print('Connection successful')
            print(station.ifconfig())
            break


def mqtt_connect(address, port):
    client_id = binascii.hexlify(machine.unique_id())
    client = MQTTClient(client_id, address, port)
    client.connect()
    client.set_callback(sub_cb)
    client.subscribe("test")
    while 1:
        client.check_msg()


relay = Pin(5, Pin.OUT)
led = PWM(Pin(2, Pin.OUT), freq=1, duty=512)

station = network.WLAN(network.STA_IF)
print("\n" + str(station.status()))
while station.status() == 1:  # status 1: connecting in progress
    pass
print(str(station.status()) + "\n")

if not station.isconnected():  # if there is no saved Wi-Fi data
    get_creds()

led.freq(1000)
relay.on()
led.duty(0)

print('after after: ' + str(station.status()))
print('Ready')

mqtt_connect("91.121.93.94", 1883)  # has infinite loop
