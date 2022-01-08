from inspect import getmembers, isfunction
from typing import List
from model.star import Star
from threading import Thread

from controller.light_controller import LightController
import controller.star.light_programmes as light_programmes


class StarController(LightController):
    
    def __init__(self) -> None:
        super(StarController, self).__init__()
        self.star = Star(pwm=True)
        self.on = False
        self.star.off()
    
    def start_loop(self, function) -> None:
        self.on = True
        self.thread = Thread(target=self._perform_loop, args=(function,))
        self.thread.start()

    def stop_loop(self) -> None:
        if self.thread and self.thread.is_alive():
            self.on = False
            self.star.off()

    def get_light_programmes(self) -> List[function]:
        function_tuples = getmembers(light_programmes, isfunction)
        return [function_tuple[0] for function_tuple in function_tuples]

    def _perform_loop(self, function):
        while self.on:
            function(self.star)
            if not self.on:
                break
