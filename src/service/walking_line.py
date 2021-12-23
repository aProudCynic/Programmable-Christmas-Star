from model.star import Star
from time import sleep

star = Star(pwm=True)
leds = star.leds

step_time = 1
line_length = 6

for i in range(1, line_length + 1):
    led = star.leds[i]
    led.on()
sleep(step_time)
for i in range(1, len(star.leds) - line_length):
    led_to_turn_off = star.leds[i]
    led_to_turn_on = star.leds[line_length + i]
    led_to_turn_off.off()
    led_to_turn_on.on()
    sleep(step_time)
