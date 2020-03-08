"""Turn on red, yellow, and green LEDs like a stoplight"""
import RPi.GPIO as GPIO
import time

# Setup our pins and board
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

# Run the stoplight script
print("Running script...")

for i in range(10):
    print(i + 1)
    GPIO.output(27,False)
    GPIO.output(4,True)
    time.sleep(0.5)
    GPIO.output(4,False)
    GPIO.output(17,True)
    time.sleep(0.5)
    GPIO.output(17,False)
    GPIO.output(27,True)
    time.sleep(0.5)

print("Script complete!")
GPIO.cleanup()
