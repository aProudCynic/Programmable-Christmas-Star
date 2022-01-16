from time import sleep

from controller.blinkt.common import (
    set_all_pixels_to_random_color,
    show,
    walk_through_pixels_with,
    set_all_pixels_to_rgb,
    radiate_pixel_brightness,
)
from model.colour import Colour

def perform_blink_random_colour():
    set_all_pixels_to_random_color()
    show()
    sleep(0.05)

def perform_walk_through_pixels(colour: Colour):
    walk_through_pixels_with(colour.red, colour.green, colour.blue)

def perform_radiate_colour(colour: Colour):
    set_all_pixels_to_rgb(colour.red, colour.green, colour.blue)
    radiate_pixel_brightness()
