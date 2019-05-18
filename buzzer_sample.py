import RPi.GPIO as GPIO
from time import sleep

def setup() :
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False) 
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

def play(buzzer, delay) :
    GPIO.output(buzzer, GPIO.HIGH)
    sleep(delay)
    GPIO.output(buzzer, GPIO.LOW)
    sleep(delay)


BUZZER_PIN=25
MAX = 3
DEFAULT_DELAY=0.3
counter = 0

try: 

    setup()

    while counter < MAX :
        play(BUZZER_PIN, DEFAULT_DELAY)
        counter += 1


except Exception as ex:
    print(ex)

finally:
    GPIO.cleanup()
    raw_input("Press any key to end")

     





