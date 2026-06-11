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

# Now we can create specific devices that inherit from the SmartDevice class
# but they implement turn_on using polymorphism because they do different things when activated

class SmartLight(SmartDevice):
    def turn_on(self):
        print(f"{self.device_name} is turned on. Setting brightness to 100%")

class SmartThermostat(SmartDevice):
    def turn_on(self):
        print(f"{self.device_name} is turned on. Adjusting temperature to 72°F")

# Now we can control all devices with a single loop

# Create our real objects
living_room_light = SmartLight("Living Room Light")
hallway_nest = SmartThermostat("Hallway Thermostat")

# Put them into a single list
my_home_devices = [living_room_light, hallway_nest]

print("--- Activating Smart Home 'Away Mode' ---")
for device in my_home_devices:
    device.turn_on() # Polymorphism makes the light shine and the thermostat adjust!