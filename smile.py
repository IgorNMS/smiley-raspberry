#!/usr/bin/python

import board
import busio
import digitalio
import adafruit_ssd1306
import subprocess

from time import sleep
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
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)
# Clear display.
oled.fill(0)
oled.show()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

displayOnOff = True


def display_on_off():
    global displayOnOff
    displayOnOff = not displayOnOff


def display_func():
    while True:
        while displayOnOff:
            # Draw a black filled box to clear the image.
            draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
            draw.image = Image.open('smile.ppm').convert('1')
            # Display image
            oled.image(image)
            oled.show()
            sleep(1)
        else:
            # Clear display.
            oled.fill(0)
            oled.show()
            sleep(1)


try:
    button.when_pressed = display_on_off
    display_func()
    pause()

finally:
    pass
