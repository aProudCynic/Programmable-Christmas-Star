from model.star import Star
from threading import Thread

from controller.light_controller import LightController


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

    def _perform_loop(self, function):
        while self.on:
            function(self.star)
            if not self.on:
                break
