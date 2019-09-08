import RPi.GPIO as GPIO
import Adafruit_BMP.BMP085 as BMP085
import time, requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

p = GPIO.PWM(13, 50)
p.start(7.5)

sensor = BMP085.BMP085()
threshold = 101000

def toDispense():
	p.ChangeDutyCycle(10)
	
def toHold():
	p.ChangeDutyCycle(7.5)

def dispense():
	toDispense()
	time.sleep(2)
	toHold()

try:
	while True:
		pressure = sensor.read_pressure()
		if(pressure > threshold):
			r = requests.get("http://10.251.90.88:5000/beat/")
		
		should = requests.get("http://10.251.90.88:5000/shouldDispense")

		if(should.text == "True"):
			dispense()

		time.sleep(2)

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
