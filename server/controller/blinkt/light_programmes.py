from time import sleep

from controller.blinkt.common import (
    set_all_pixels_to_random_color,
    show,
)

def blink_random_colour():
    set_all_pixels_to_random_color()
    show()
    sleep(0.05)
