#morse parser by nicktech_1105
#works for esp8266

#import all necesary modules
from machine import Pin
from time import sleep

#set all pins
led = Pin(2, Pin.OUT)

#define variables
speed = 1

#lines, dots, blanks and abreviations

def blank():
    led.value(1) #turn off the onboard LED
    sleep(speed*0.1)
    
def space():
    led.value(1) #turn off the onboard LED
    sleep(speed*0.2)
    

def dot():
    led.value(0) #turn on the onboard LED
    sleep(speed*0.05)
    blank()
   
def d_dot():
    dot()
    dot()
  
def line():
    led.value(0)
    sleep(speed*0.15) #the line function turns on the LED for a longer time than the dot function 
    blank()

def d_line():
    line()
    line()

#alphabet
def _a():
    dot()
    line()
    print("a")

def _b():
    line()
    d_dot()
    dot()
    print("b")
    
def _c():
    line()
    dot()
    line()
    dot()
    print("c")
    
def _d():
    line()
    d_dot()
    print("d")
    
def _e():
    dot()
    print("e")
    
def _f():
    d_dot()
    line()
    dot()
    print("f")
    
def _g():
    d_line()
    dot()
    print("g")
    
def _h():
    d_dot()
    d_dot()
    print("h")
    
def _i():
    d_dot()
    print("i")
    
def _j():
    dot()
    d_line()
    line()
    print("i")
    
def _k():
    line()
    dot()
    line()
    print("k")
    
def _l():
    dot()
    line()
    d_dot()
    print("l")
    
def _m():
    d_line()
    print("m")
    
def _n():
    line()
    dot()
    print("n")
    
def _o():
    d_line()
    line()
    print("o")
    
def _p():
    dot()
    d_line()
    dot()
    print("p")
    
def _q():
    d_line()
    dot()
    line()
    print("q")
    
def _r():
    dot()
    line()
    dot()
    print("r")
    
def _s():
    d_dot()
    dot()
    print("s")
    
def _t():
    line()
    print("t")
    
def _u():
    d_dot()
    line()
    print("u")
    
def _v():
    d_dot()
    dot()
    line()
    print("v")
    
def _w():
    dot()
    d_line()
    print("w")
    
def _x():
    line()
    d_dot()
    line()
    print("x")
    
def _y():
    line()
    dot()
    d_line()
    print("y")
    
def _z():
    d_line()
    d_dot()
    print("z")
    
#numbers (0-9)
def _0():
    d_line()
    d_line()
    line()
    print("0")
    
def _1():
    d_dot()
    d_line()
    d_line()
    print("1")
    
def _2():
    d_dot()
    d_line()
    line()
    print("2")
    
def _3():
    d_dot()
    dot()
    d_line()
    print("3")
    
def _4():
    d_dot()
    d_dot()
    line()
    print("4")
    
def _5():
    d_dot()
    d_dot()
    dot()
    print("5")
    
def _6():
    line()
    d_dot()
    d_dot()
    dot()
    print("6")
    
def _7():
    d_line
    d_dot()
    dot()
    print("7")
    
def _8():
    d_line()
    line()
    d_dot()
    print("8")
    
def _9():
    d_line()
    d_line()
    dot()
    print("9")


#parser loop
def parser():
    while True:
        word = input("enter your word below (no special characters plez):\n >")
        word.split(" ")
        for i in word:
            if i == "a":
                _a()
            elif i == "b":
                _b()
            elif i == "c":
                _c()
            elif i == "d":
                _d()
            elif i == "e":
                _e()
            elif i == "f":
                _f()
            elif i == "g":
                _g()
            elif i == "h":
                _h()
            elif i == "i":
                _i()
            elif i == "j":
                _j()
            elif i == "k":
                _k()
            elif i == "l":
                _l()
            elif i == "m":
                _m()
            elif i == "n":
                _n()
            elif i == "o":
                _o()
            elif i == "p":
                _p()
            elif i == "q":
                _q()
            elif i == "r":
                _r()
            elif i == "s":
                _s()
            elif i == "t":
                _t()
            elif i == "u":
                _u()
            elif i == "v":
                _v()
            elif i == "w":
                _w()
            elif i == "x":
                _x()
            elif i == "y":
                _y()
            elif i == "z":
                _z()
            elif i == "0":
                _0()
            elif i == "1":
                _1()
            elif i == "2":
                _2()
            elif i == "3":
                _3()
            elif i == "4":
                _4()
            elif i == "5":
                _5()
            elif i == "6":
                _6()
            elif i == "7":
                _7()
            elif i == "8":
                _8()
            elif i == "9":
                _9()
            elif i == " ":
                space()
            else:
                print("no special characters allowed")
                
parser()











#sup kyle