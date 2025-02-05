from machine import Pin, TouchPad
import time

# --- Configuration ---
touch_pin = 4  # GPIO pin for the capacitive touch sensor
 # Sensitivity threshold for touch detection
pin = Pin(14, Pin.OUT)
pin.value(1)
# Initialize the TouchPad object for GPIO pin 4
touch_button = TouchPad(Pin(touch_pin))
touch_threshold = touch_button.read()-20
print(f'set to {touch_threshold}')
count =0 
# --- Main Loop ---
while True:
    #print(f"Touch value: {touch_value}")  # Print the touch value
    if touch_button.read() < touch_threshold:
        while (touch_button.read() < touch_threshold):
            #print(touch_button.read())
            continue
        count +=1
        print(count)
        if pin.value() == 0:
            pin.value(1)
        else:
            pin.value(0)
        time.sleep(0.5)  # Delay to prevent excessive readings (100ms)
    #time.sleep(0.2)
