import RPi.GPIO as GPIO
import Adafruit_BMP.BMP085 as BMP085
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

p = GPIO.PWM(13, 50)
p.start(10)

sensor = BMP085.BMP085()

def toDispense():
	p.ChangeDutyCycle(10)
	
def toHold():
	p.ChangeDutyCycle(7.5)

try:
	while True:
		print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
		toDispense()
		time.sleep(1)
		toHold()
		time.sleep(1)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
