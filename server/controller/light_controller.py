from threading import Thread
from typing import List


class LightController:

    def __init__(self) -> None:
        self.on = False

    def start_loop(self, function) -> None:
        self.on = True
        self.thread = Thread(target=self.perform_loop, args=(function,))
        self.thread.start()

    def perform_loop(self, function) -> None:
        while self.on:
            self.apply_light_programme(function)
            if not self.on:
                break

    def stop_loop(self) -> None:
        if self.thread and self.thread.is_alive():
            self.on = False

    def get_light_programmes(self) -> List:
        pass

    def get_light_programme_by(self, light_programme_name) -> List:
        pass

    def apply_light_programme(self, function) -> None:
        pass

