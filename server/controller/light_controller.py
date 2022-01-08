from threading import Thread
from typing import List


class LightController:

    def start_loop(self, function) -> None:
        self.on = True
        self.thread = Thread(target=self.perform_loop, args=(function,))
        self.thread.start()


    def stop_loop(self) -> None:
        pass

    def get_light_programmes(self) -> List[function]:
        pass

    def perform_loop(self, function) -> None:
        pass
