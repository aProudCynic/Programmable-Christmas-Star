from model.star import Star
from random import randint

star = Star(pwm=True)
leds = star.leds
try:
    while True:
        led = star.leds[randint(1, len(leds) - 1)]
        led.pulse(fade_in_time=1, fade_out_time=1, n=1, background=False)
except KeyboardInterrupt:
    star.close()