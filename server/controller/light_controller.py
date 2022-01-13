from inspect import getmembers, isfunction
from multiprocessing import Process
from typing import List


class LightController:

    def __init__(self) -> None:
        self.on = False

    def start_loop(self, function) -> None:
        self.on = True
        self.process = Process(target=self.perform_loop, args=(function,))
        self.process.start()

    def perform_loop(self, function) -> None:
        while self.on:
            self.apply_light_programme(function)
            if not self.on:
                break

    def stop_loop(self) -> None:
        if self.process and self.process.is_alive():
            self.process.terminate()

    def get_light_programmes(self):
        return self.__not_imported_function_names_from(
            self.get_light_programme_module()
        )

    def get_light_programme_by(self, light_programme_name) -> List:
        return getattr(self.get_light_programme_module(), light_programme_name)

    def get_light_programme_module():
        pass

    def apply_light_programme(self, function) -> None:
        pass

    def __not_imported_function_names_from(self, module):
        function_tuples = getmembers(module, isfunction)
        return [function_tuple[0] for function_tuple in function_tuples if function_tuple[1].__module__ == module.__name__]
