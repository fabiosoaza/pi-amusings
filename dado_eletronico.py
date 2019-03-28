import RPi.GPIO as GPIO, random

#Dice layout
#1   2   3
#    7    
#4   5   6

#Led to PIN mappings
LED1=8
LED2=25
LED3=18
LED4=17
LED5=11
LED6=22
LED7=23
BOTAO=10


def botao_pressionado(channel):
    apagar_todos_leds()
    numero_sorteado = random.randint(1,6) 
    exibir_numero(numero_sorteado)
    print ("Numero sorteado "+str(numero_sorteado))

def apagar_todos_leds() :
    GPIO.output(LED1, False)
    GPIO.output(LED2, False)
    GPIO.output(LED3, False)
    GPIO.output(LED4, False)
    GPIO.output(LED5, False)
    GPIO.output(LED6, False)
    GPIO.output(LED7, False)

def inicializar() :
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False) 
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)
    GPIO.setup(LED3, GPIO.OUT)
    GPIO.setup(LED4, GPIO.OUT)
    GPIO.setup(LED5, GPIO.OUT)
    GPIO.setup(LED6, GPIO.OUT)
    GPIO.setup(LED7, GPIO.OUT)
    GPIO.setup(BOTAO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BOTAO, GPIO.RISING, callback=botao_pressionado)
    

def ligar_led(pin) :
    GPIO.output(pin, True)

def desligar_led(pin) :
    GPIO.output(pin, False)

def exibir_numero(numero) :
    if numero == 1: 
        ligar_led(LED7)             
    elif numero == 2:  
        ligar_led(LED3)
        ligar_led(LED4)
    elif numero == 3: 
        ligar_led(LED3)
        ligar_led(LED4)
        ligar_led(LED7)
    elif numero == 4: 
        ligar_led(LED1)
        ligar_led(LED3)
        ligar_led(LED4)
        ligar_led(LED6)
    elif numero == 5: 
        ligar_led(LED1)
        ligar_led(LED3)
        ligar_led(LED4)
        ligar_led(LED6)
        ligar_led(LED7) 
    elif numero == 6: 
        ligar_led(LED1)
        ligar_led(LED2)
        ligar_led(LED3)
        ligar_led(LED4)
        ligar_led(LED5)
        ligar_led(LED6)


inicializar()

apagar_todos_leds()
raw_input("Pressione Enter para Terminar.")
apagar_todos_leds()    
GPIO.cleanup()

