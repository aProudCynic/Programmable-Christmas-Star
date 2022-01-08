from model.star import Star
from threading import Thread


class StarController:
    
    def __init__(self) -> None:
        self.star = Star(pwm=True)
        self.on = False
        self.star.off()
    
    def start_loop(self, function):
        self.on = True
        self.thread = Thread(target=self._perform_loop, args=(function,))
        self.thread.start()

    def stop(self):
        if self.thread and self.thread.is_alive():
            self.on = False
            self.star.off()

    def _perform_loop(self, function):
        while self.on:
            function(self.star)
            if not self.on:
                break
