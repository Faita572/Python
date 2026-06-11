###A smart home system
# Scenario:
#Imagine you are writing a smart home system that can control various devices like lights, thermostats, and security cameras
# The first step is to set up the abstract blueprint
# every device has an on/off switch, but a light turns on differently than a thermostat does... create an abstract rule that forces every device to have a turn_on action

from abc import ABC, abstractmethod
class SmartDevice(ABC):
    def __init__(self, device_name):
        self.device_name = device_name
        self.__is_connected = True  # Encapsulation: Protected connection status

    @abstractmethod
    def turn_on(self):
        pass