#!/usr/bin/python

import board
import busio
import digitalio
import adafruit_ssd1306
import subprocess
import time

from PIL import Image
from signal import pause
from gpiozero import Button

# Define display on/off button
button = Button(21)
# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)
# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5
# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_128_64(rst=oled_reset)


oled.begin()

oled.clear()
oled.display

image = Image.open('smile.ppm').convert('1')

oled.image(image)
oled.display()

