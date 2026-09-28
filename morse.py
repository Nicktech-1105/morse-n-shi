#morse parser (v1.1) by nicktech_1105
#works for esp8266
from machine import Pin
from time import sleep
#define all variables needed
led = Pin(2, Pin.OUT) #LED pin, modify this if you want
speed = 0.75
abc = {"a" : ".-","b" : "-...","c" : "-.-.","d" : "-..","e" : ".","f" : "..-.","g" : "--.","h" : "....","i" : "..","j" : ".---","k" : "-.-","l" : ".-..","m" : "--","n" : "-.","o" : "---","p" : ".--.","q" : "--.-","r" : ".-.","s" : "...","t" : "-","u" : "..-","v" : "...-","w" : ".--","x" : "-..-","y" : "-.--","z" : "--..","0" : "-----","1" : ".----","2" : "..---","3" : "...--","4" : "....-","5" : ".....","6" : "-....","7" : "--...","8" : "---..","9" : "----."," " : "space"}
def blank():
    led.value(1) #turn off the onboard LED
    sleep(speed*0.1)
def parser():
    while True:
        word = input("enter your word(s). only alphanumerical characters (a-z, A-Z, 0-9):\n >")
        word.split()
        for i in word:
            i = i.lower()
            if i in abc:
                print(i, ":", abc[i])
                cc = abc[i]
                cc.split()
                for j in cc:
                    if j == "-":
                        led.value(0)
                        sleep(speed*0.15)
                        led.value(1)
                        blank()
                    elif j == ".":
                        led.value(0) #turn on the onboard LED
                        sleep(speed*0.05)
                        led.value(1)
                        blank()
                    elif j == " ":
                        led.value(1)
                        sleep(speed*0.2)
            elif i not in abc:
                print("no special characters allowed (', ?, ¡, \, ¿, *, +, etc)")
parser()










#sup kyle
