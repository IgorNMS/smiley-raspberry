#!/usr/bin/python

import board
import busio
import digitalio
import adafruit_ssd1306
import subprocess
import time

from PIL import Image, ImageDraw, ImageFont
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
disp = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

disp.fill(0)
disp.show()
image = Image.open("smile.ppm").convert("1")
disp.image(image)
disp.show()

