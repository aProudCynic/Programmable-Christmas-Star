from inspect import getmembers, isfunction

from controller.light_controller import LightController
import controller.blinkt.light_programmes as light_programmes
from controller.blinkt.common import shut_down_all_pixels


class BlinktController(LightController):

    def get_light_programmes(self):
        function_tuples = getmembers(light_programmes, isfunction)
        print([function_tuple[0] for function_tuple in function_tuples])
        return [function_tuple[0] for function_tuple in function_tuples]

    def apply_light_programme(self, function):
        function()

    def stop_loop(self):
        super(BlinktController, self).stop_loop()
        shut_down_all_pixels()

    # TODO hoist
    def get_light_programme_by(self, light_programme_name):
        return getattr(light_programmes, light_programme_name)
