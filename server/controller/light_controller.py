from datetime import datetime
from inspect import getmembers, isfunction
import logging
from multiprocessing import Process
from threading import Thread
from time import sleep

from server.controller.blinkt.common import set_all_pixels_to_rgb


class LightController:

    def __init__(self):
        self.process = None
        self.process_start_date = None
        logging.basicConfig(filename='light_controller.log', encoding='utf-8', level=logging.DEBUG)

    def start_loop(self, function, parameters) -> None:
        logging.debug(f'starting loop, replacing process {self.process}')
        self.process = Process(target=self.perform_loop, args=(function, parameters))
        self.process.start()
        self.process_start_date = datetime.now()
        logging.debug(f'started loop as process {self.process} at {self.process_start_date}')

    def start_loop_with_ttl(self, function, parameters) -> None:
        time_to_live_secs = parameters.time_to_live
        delattr(parameters, 'time_to_live')
        self.start_loop(function, parameters)
        if time_to_live_secs > 0:
            countdown = Thread(target=self.perform_countdown, args=(time_to_live_secs,))
            countdown.start()

    def perform_loop(self, function, parameters) -> None:
        while True:
            self.apply_light_programme(function, parameters)

    def stop_loop(self) -> None:
        logging.debug('stopping loop')
        if self.is_on():
            self.process.terminate()
            logging.debug(f'stopped loop as process {self.process}')
            set_all_pixels_to_rgb(0, 0, 0)

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
        logging.debug(f'starting countdown from {seconds}')
        sleep(seconds)
        logging.debug('initiating loop stop')
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
