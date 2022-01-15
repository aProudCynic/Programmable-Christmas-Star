from time import sleep

from controller.blinkt.common import (
    set_all_pixels_to_random_color,
    show,
    walk_through_pixels_with,
)
from model.colour import Colour

def blink_random_colour():
    set_all_pixels_to_random_color()
    show()
    sleep(0.05)

def perform_walk_through_pixels(colour: Colour):
    walk_through_pixels_with(colour.red, colour.green, colour.blue)
