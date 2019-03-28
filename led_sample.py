import RPi.GPIO as GPIO, time

def blink_led(pin, interval, qnt_times):
    counter=0
    while counter < qnt_times:
        counter +=1
        time.sleep(interval)
        GPIO.output(pin, True)
        time.sleep(interval)
        GPIO.output(pin, False)

GREEN_LED = 23
RED_LED = 18
QNT_GREEN=4
QNT_RED=6
INTERVAL_SEC=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

print ("Blinking Green")
blink_led(GREEN_LED, INTERVAL_SEC, QNT_GREEN)

print ("Blinking Red")
blink_led(RED_LED, INTERVAL_SEC, QNT_RED)

raw_input("Pressione Enter para Terminar.")

