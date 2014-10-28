#!/usr/bin/python

import RPi.GPIO as GPIO
import pygame
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
from time import sleep
pygame.init()
currState = False
prevState = False

while True:
    try:
        sleep(0.1)
        prevState = currState
        currState = GPIO.input(7)
        if currState != prevState:
            newState = "HIGH" if currState else "LOW"
            print "GPIO pin %s is %s" % (7, newState)
            GPIO.output(18, True)
            sleep(1)
            pygame.mixer.music.load("/home/pi/halloween_scarer/zombie_roar.ogg")
            pygame.mixer.music.play()
            sleep(5)
            GPIO.output(18, False)
            sleep(5)
    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        print ("Keyboard stop")
        exit()
    except:
        # report error and proceed
        GPIO.cleanup()
        print ("FUBAR")
        exit()


