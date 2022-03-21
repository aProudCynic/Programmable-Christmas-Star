from time import sleep

from controller.blinkt.common import (
    set_all_pixels_to_random_color,
    show,
    walk_through_pixels_with,
    set_all_pixels_to_rgb,
    radiate_pixel_brightness,
    set_pixel_to_colour,
)
from model.colour import Colour

def perform_blink_random_colour():
    set_all_pixels_to_random_color()
    show()
    sleep(0.05)

def perform_walk_through_pixels(colour: Colour):
    walk_through_pixels_with(colour.red, colour.green, colour.blue)

def perform_radiate_colour(colour: Colour, granularity: int):
    set_all_pixels_to_rgb(colour.red, colour.green, colour.blue)
    radiate_pixel_brightness(granularity)

def perform_different_colours(
    colour_1: Colour,
    colour_2: Colour,
    colour_3: Colour,
    colour_4: Colour,
    colour_5: Colour,
    colour_6: Colour,
    colour_7: Colour,
    colour_8: Colour,
):
    set_pixel_to_colour(0, colour_1)
    set_pixel_to_colour(1, colour_2)
    set_pixel_to_colour(2, colour_3)
    set_pixel_to_colour(3, colour_4)
    set_pixel_to_colour(4, colour_5)
    set_pixel_to_colour(5, colour_6)
    set_pixel_to_colour(6, colour_7)
    set_pixel_to_colour(7, colour_8)
