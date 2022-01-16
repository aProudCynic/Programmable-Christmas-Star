from inspect import getmembers, isfunction
from multiprocessing import Process
from threading import Thread
from time import sleep


class LightController:

    def __init__(self):
        self.process = None

    def start_loop(self, function, parameters) -> None:
        self.process = Process(target=self.perform_loop, args=(function, parameters))
        self.process.start()

    def start_loop_with_ttl(self, function, parameters) -> None:
        self.start_loop(function, parameters)
        time_to_live_secs = 10
        if time_to_live_secs > 0:
            countdown = Thread(target=self.perform_countdown, args=(time_to_live_secs,))
            countdown.start()

    def perform_loop(self, function, parameters) -> None:
        while True:
            self.apply_light_programme(function, parameters)

    def stop_loop(self) -> None:
        if self.is_on():
            self.process.terminate()

    def get_light_programmes(self):
        return self.__not_imported_functions_from(
            self.get_light_programme_module()
        )

    def get_light_programme_by(self, light_programme_name):
        return getattr(self.get_light_programme_module(), light_programme_name)

    def get_light_programme_module(self):
        pass

    def apply_light_programme(self, function, parameters) -> None:
        pass

    def is_on(self):
        return hasattr(self, 'process') and self.process and self.process.is_alive()

    def perform_countdown(self, seconds):
        sleep(seconds)
        self.stop_loop()

    def __not_imported_functions_from(self, module):
        function_tuples = getmembers(module, isfunction)
        # this could be – as originally it was – a list comprehension, however it had become a bit incomprehensible
        result = []
        for function_data in function_tuples:
            if self.__is_not_imported(function_data, module):
                function_name = function_data[0]
                function_parameters = function_data[1].__code__.co_varnames
                result.append({'name': function_name, 'parameters': function_parameters})
        return result

    def __is_not_imported(self, function_data, module):
        return function_data[1].__module__ == module.__name__
