import RPi.GPIO as GPIO
from time import sleep

#inpired by instructable https://www.instructables.com/id/Ultimate-Arduino-Paper-Piano/

#buzzer pin
BUZZER_PIN=25

#key pins
NOTE_F_PIN=2
NOTE_FS_PIN=3
NOTE_G_PIN=4
NOTE_GS_PIN=7
NOTE_A_PIN=9
NOTE_AS_PIN=10
NOTE_B_PIN=11
NOTE_C_PIN=17
NOTE_CS_PIN=22
NOTE_D_PIN=23
NOTE_DS_PIN=24
NOTE_E_PIN=27

#notes
NOTE_F=123
NOTE_FS=116
NOTE_G=110
NOTE_GS=104
NOTE_A=98
NOTE_AS=92
NOTE_B=87
NOTE_C=82
NOTE_CS=77
NOTE_D=73
NOTE_DS=69
NOTE_E=65



#the multiply voltageue is defined. This voltageue determines the octave that is being played and can be changed to get higher or lower pitched octaves


MULTIPLY=4

def is_key_e(voltage) :
    return voltage > 70 and voltage < 80

def is_key_ds(voltage) :
    return voltage > 145 and voltage < 165

def is_key_d(voltage) :
    return voltage > 230 and voltage < 240

def is_key_cs(voltage) :
    return voltage > 305 and voltage < 320

def is_key_c(voltage) :
    return voltage > 385 and voltage < 395

def is_key_b(voltage) :
    return voltage > 465 and voltage < 475

def is_key_as(voltage) :
    return voltage > 545 and voltage < 555

def is_key_a(voltage) :
    return voltage > 625 and voltage < 635

def is_key_gs(voltage) :
    return voltage > 700 and voltage < 715

def is_key_g(voltage) :
    return voltage > 770 and voltage < 790

def is_key_fs(voltage) :
    return voltage > 860 and voltage < 875

def is_key_f(voltage) :
    return voltage > 935 and voltage < 955



def is_interval_tone(pin, voltage):
    return voltage > 70 and voltage < 955


def generate_note(voltage):
    note = 0
    if is_key_e(voltage):
        note = NOTE_E * MULTIPLY
    elif is_key_ds(voltage):
        note = NOTE_DS * MULTIPLY
    elif is_key_d(voltage):
        note = NOTE_D * MULTIPLY
    elif is_key_cs(voltage):
        note = NOTE_CS * MULTIPLY
    elif is_key_c(voltage):
        note = NOTE_C * MULTIPLY
    elif is_key_b(voltage):
        note = NOTE_B * MULTIPLY
    elif is_key_as(voltage):
        note = NOTE_AS * MULTIPLY
    elif is_key_a(voltage):
        note = NOTE_A * MULTIPLY
    elif is_key_gs(voltage):
        note = NOTE_GS * MULTIPLY
    elif is_key_g(voltage):
        note = NOTE_G * MULTIPLY
    elif is_key_fs(voltage):
        note = NOTE_FS *  MULTIPLY
    elif is_key_f(voltage):
        note = NOTE_F * MULTIPLY
    
    return note



def play_key(pin, voltage, duration_in_micro):
    if is_interval_tone(pin, voltage):
        note = generate_note(voltage)  
        play_tone(pin, note, duration_in_micro)
    else:
        sleep(duration_in_micro)

def setup() :
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
       

def play_buzzer(buzzer, delay_in_micro) :
    GPIO.output(buzzer, GPIO.HIGH)
    delay_micro(delay_in_micro)
    GPIO.output(buzzer, GPIO.LOW)
    delay_micro(delay_in_micro)

def play_tone(pin, note, duration):
  print("tone "+str(note))  
  if note == 0 :
    return 

  #This is the semiperiod of each note.
  beepDelay = long(1000000.0/note)
  
  #This is how much time we need to spend on the note.
  time = long((duration*1000.0)/(beepDelay*2))
  
  i = 0
  while i < time:
    play_buzzer(pin,beepDelay)
    i += 1
  
  GPIO.output(pin, GPIO.LOW)  
  
  DELAY_IN_MS = 20*1000
  delay_micro(DELAY_IN_MS)



def delay_micro(delay_in_micro) :
  sleep(delay_in_micro/1000000.0)


MAX = 10
DEFAULT_DELAY_IN_MS = 300 
DEFAULT_DELAY_MICRO=DEFAULT_DELAY_IN_MS * 1000
counter = 0

try: 

    setup()
    keyboard_keys = [71, 146, 231, 306, 386, 466, 546, 626, 701, 771, 861, 936] 

    while counter < MAX :
        print ("Execucao "+str(counter+1) )  
        for keyboard_key  in keyboard_keys:
            play_key(BUZZER_PIN, keyboard_key, 200)
            sleep(0.5)
        counter += 1
        sleep(0.5)


except Exception as ex:
    print(ex)

finally:
    GPIO.cleanup()
    raw_input("Press any key to end")

     





