from random import randint
from time import sleep

from blinkt import (
    set_pixel,
    set_brightness,
    clear,
    show,
)

NUMBER_OF_PIXELS = 8
MAXIMUM_COLOUR_INTENSITY = 255


def reset():    
    set_brightness(1)
    clear()

def set_pixel_to_colour(i, rgb_color):
    red = rgb_color.red
    green = rgb_color.green
    blue = rgb_color.blue
    print(i, red, green, blue)
    set_pixel(i, red, green, blue)
    show()

def set_all_pixels_to_color(rgb_color):
    red, green, blue = rgb_color
    set_all_pixels_to_rgb(red, green, blue)

def set_all_pixels_to_rgb(red, green, blue):
    for i in range(NUMBER_OF_PIXELS):
        set_pixel(i, red, green, blue)

def generate_random_intensity():
    return randint(0, MAXIMUM_COLOUR_INTENSITY)

def generate_random_colour():
    return (generate_random_intensity(), generate_random_intensity(), generate_random_intensity())

def set_all_pixels_to_random_color():
    for i in range(NUMBER_OF_PIXELS):
        red, green, blue = generate_random_colour()
        set_pixel(i, red, green, blue)

def walk_through_pixels_with(red, green, blue):
    while (True):
        for i in range(NUMBER_OF_PIXELS):
            clear()
            set_pixel(
                i,
                red,
                green,
                blue
            )
            show()
            sleep(0.05)

def adjust_colour_intensity(colour_intensity, adjust_coluur_intensity_by_maximum):
    new_colour_intensity = colour_intensity + randint(adjust_coluur_intensity_by_maximum * -1, adjust_coluur_intensity_by_maximum)
    if new_colour_intensity >= MAXIMUM_COLOUR_INTENSITY:
        return MAXIMUM_COLOUR_INTENSITY
    elif new_colour_intensity <= 0:
        return 0
    else:
        return new_colour_intensity

def radiate_pixel_brightness(granularity: int):
    while (True):
        sleep_time = 0.01
        for i in range(0, granularity):
            set_brightness(i/granularity)
            show()
            sleep(sleep_time)
        for i in range(granularity, 0, -1):
            set_brightness(i/granularity)
            show()
            sleep(sleep_time)

def shut_down_all_pixels():
    clear()
    show()
