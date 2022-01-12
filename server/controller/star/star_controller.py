from inspect import getmembers, isfunction
from typing import List
from model.star import Star
from threading import Thread

from controller.light_controller import LightController
import controller.star.light_programmes as light_programmes


class StarController(LightController):
    
    def __init__(self):
        super(StarController, self).__init__()
        self.star = Star(pwm=True)
        self.star.off()

    def stop_loop(self):
        super(StarController, self).stop_loop()
        self.star.off()

    def get_light_programmes(self):
        function_tuples = getmembers(light_programmes, isfunction)
        return [function_tuple[0] for function_tuple in function_tuples]

    def apply_light_programme(self, function):
        function(self.star)
