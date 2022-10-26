# Pametna Uticnica
Pametna Uticnica is a Smart Plug project, consisting of:

- ESP8266 microcontroller code, that gets "Home" Wi-Fi information from a mobile app and gets and sends orders using [MQTT](https://mqtt.org) protocol to control the plug,
- A mobile app, that sends "Home" Wi-Fi information to the ESP8266 microcontroller, 
and enables the user to control (turn on/off) the smart plug,
- And a simple electrical circuit that represents the smart plug.

## ESP8266 code

The ESP8266 microcontroller has two network options: station (when the ESP8266 connects to a router),
and access point (for other devices to connect to the ESP8266), so the code works as follows:
- The ESP8266 opens its access point with a specific SSID and password and waits for "Home" Wi-Fi information,
- When it gets the Wi-Fi information, 
if the information is correct it connects to the "Home" Wi-Fi and waits for commands sent using [MQTT](https://mqtt.org) protocol from the mobile app, 
otherwise, it informs the mobile app about connection failure and waits for new information,
- When it gets an [MQTT](https://mqtt.org) command it forwards it to the plug.

The code is written in [MicroPython](https://micropython.org), 
an efficient implementation of the Python 3 programming language that is optimized to run on microcontrollers.

The files that are flashed to the ESP8266 microcontroller are "boot.py", "main.py" and "mqtt.py".

## Mobile application

The used mobile application connects to the ESP8266 microcontrollers' access point, sends "Home" Wi-Fi information, 
and then sends "on" and "off" commands using [MQTT](https://mqtt.org) protocol to the ESP8266 microcontroller.
 
Two screenshots of the application are shown below, 
for remaining screenshots see [documentation](https://docs.google.com/viewer?url=https://github.com/Yaly0/Pametna-Uticnica/files/9860687/rad.pdf).

|<img width="200" alt="scr2" src="https://user-images.githubusercontent.com/44165518/197779345-dfe13773-57ef-487d-b347-e4bc89c4770a.jpeg">|<img width="200" alt="scr3" src="https://user-images.githubusercontent.com/44165518/197779349-55da0071-47e0-4b6a-9a22-3bed54fffb22.jpeg">|
|-|-|

The mobile application is developed using [MIT App Inventor](https://appinventor.mit.edu), 
a visual programming environment, that uses a drag-drop system to construct the code.

<img width="441" alt="blocks" src="https://user-images.githubusercontent.com/44165518/197784384-7ccea4ee-fb8d-4026-8405-c7a8400ebcf5.png">

## Electrical circuit

For testing the smart plug, a simple electrical circuit was made, consisting of NodeMCU, 
a relay module, and a light bulb for testing, as shown in the figure below.

<img width="441" alt="scheme" src="https://user-images.githubusercontent.com/44165518/197784387-89652fa3-03c3-489f-8e0f-23c793befd96.jpg">

---
For all detailed information see [documentation](https://docs.google.com/viewer?url=https://github.com/Yaly0/Pametna-Uticnica/files/9860687/rad.pdf)
(written in Bosnian language).
