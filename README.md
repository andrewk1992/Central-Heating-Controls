# Central-Heating-Controls

This script uses the 'W1ThermSensor' class from the 'w1thermsensor' library to read temperature data from the DS18B20 sensors, 
and the 'pywemo.discovery.device_from_description' method from the pywemo library to find the wifi-controlled radiator valves. 
The main control loop uses the set_state method of the pywemo library to control the radiator valves. 
Note that the IP addresses used in the location argument of the device_from_description method will 
need to be changed to match the IP addresses of the wifi-controlled radiator valves on your own network.

In each room (10 in this case) there is a DS18B20 paired with a valve. The script reads data from each sensor in, and based on the result of the if statement 
will adjust the paired valve.

The set_temperature function takes a room name and a temperature as arguments, and updates the corresponding setpoint temperature in the setpoints list. 
To use this function, you can call it with the desired room name and temperature values, as follows:
    set_temperature("Living Room", 18.0
    
   
Futher user functionality is added by allowing input times when the system is on/off.



This is a Work in Progress.
