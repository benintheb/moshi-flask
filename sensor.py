import RPi.GPIO as GPIO
import time
import os

sensor = 16

isLightOn = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)

os.system("./light.sh off")


print("IR Sensor Ready.....")
print(" ")

try: 
   while True:
      if GPIO.input(sensor):
          print("Object Detected")
          if isLightOn == False:
              os.system("./light.sh on")
              isLightOn = True
          elif isLightOn == True:
              os.system("./light.sh off")
              isLightOn = False
          while GPIO.input(sensor):
              time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
