from time import sleep

from controller.blinkt.common import (
    set_all_pixels_to_random_color,
    show,
    walk_through_pixels_with,
)

def blink_random_colour():
    set_all_pixels_to_random_color()
    show()
    sleep(0.05)

def walk_through_pixels(red, green, blue):
    walk_through_pixels_with(red, green, blue)
