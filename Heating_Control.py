from w1thermsensor import W1ThermSensor
import pywemo
import time

# Setpoint temperatures for each room
setpoints = [20.0] * 10

# Initialize timer
on_time = 6 # hours
off_time = 18 # hours
on_time_secs = on_time * 60 * 60
off_time_secs = off_time * 60 * 60
current_time = time.time()

# Define room names
room_names = ["Room 1", "Room 2", "Room 3", "Room 4", "Room 5", "Room 6", "Room 7", "Room 8", "Room 9", "Room 10"]

# Find temperature sensors
sensors = [W1ThermSensor.get_available_sensors([Sensor.DS18B20]), "0000:00:0a.0" + str(i)) for i in range(10)]

for sensor in W1ThermSensor.get_available_sensors([Sensor.DS18B20]):
    print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))


# Find wifi-controlled radiator valves
valves = [pywemo.discovery.device_from_description(location="http://192.168.1.1" + str(i) + ":49153/setup.xml", ssdp_st="urn:Belkin:device:controllee:1") for i in range(10)]

# Function to set temperature for a named room
def set_temperature(room_name, temperature):
    room_index = room_names.index(room_name)
    setpoints[room_index] = temperature

# Main control loop
while True:
    # Check if heating should be on or off
    if (current_time - int(current_time / (on_time_secs + off_time_secs)) * (on_time_secs + off_time_secs)) < on_time_secs:
        heating_on = True
    else:
        heating_on = False
    
    # Read temperature data for each room
    temperatures = []
    for sensor in sensors:
        temp = sensor.get_temperature()
        temperatures.append(temp)
    
    # Control radiator valves based on temperature data and heating status
    for i in range(10):
        if heating_on and temperatures[i] < setpoints[i]:
            # Open valve if temperature is below setpoint and heating is on
            valves[i].set_state(1)
            print(f"Heating {room_names[i]} ({temperatures[i]:.1f} C)")
        else:
            # Close valve if temperature is above setpoint or heating is off
            valves[i].set_state(0)
            print(f"Cooling {room_names[i]} ({temperatures[i]:.1f} C)")
    
    # Wait for next control cycle
    time.sleep(5)
    current_time = time.time()