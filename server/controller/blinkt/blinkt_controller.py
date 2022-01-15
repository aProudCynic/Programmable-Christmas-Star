from controller.light_controller import LightController
import controller.blinkt.light_programmes as light_programmes
from controller.blinkt.common import shut_down_all_pixels

class BlinktController(LightController):

    def apply_light_programme(self, function, parameters):
        function(parameters) if parameters else function()

    def stop_loop(self):
        super(BlinktController, self).stop_loop()
        shut_down_all_pixels()

    def get_light_programme_module(self):
        return light_programmes    
