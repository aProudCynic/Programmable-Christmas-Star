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
        return self.__not_imported_functions_from(
            self.get_light_programme_module()
        )

    def get_light_programme_by(self, light_programme_name):
        return getattr(self.get_light_programme_module(), light_programme_name)

    def get_light_programme_module():
        pass

    def apply_light_programme(self, function) -> None:
        pass

    def __not_imported_functions_from(self, module):
        function_tuples = getmembers(module, isfunction)
        print(function_tuples)
        # this could be – as originally it was – a list comprehension, however it had become a bit incomprehensible
        result = []
        for function_data in function_tuples:
            if self.__is_not_imported(function_data, module):
                function_name = function_data[0]
                function_parameters = function_data[1].__code__.co_varnames
                result.append({'name': function_name, 'parameters': function_parameters})
        return result

    def __is_not_imported(self, function_data, module):
        print(function_data[0], function_data[1].__module__ == module.__name__)
        return function_data[1].__module__ == module.__name__
