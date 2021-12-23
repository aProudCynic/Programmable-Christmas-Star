from time import sleep


def explode(star):
    leds = star.leds
    step_time = 0.1
    star.inner.on()
    sleep(step_time)
    for i in range(3, len(leds) - 1, 5):
        leds[i].on()
        leds[i + 1].on()
    sleep(step_time)
    for i in range(2, len(leds) - 1, 5):
        leds[i].on()
        leds[i + 3].on()
    sleep(step_time)
    for i in range(1, len(leds) - 1, 5):
        leds[i].on()
    sleep(step_time)
    star.off()
    sleep(step_time)

def all_on(star):
    star.on()
