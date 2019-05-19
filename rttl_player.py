import RPi.GPIO as GPIO
import time 

from rtttl import parse_rtttl
import pprint


def setup() :
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False) 
    GPIO.cleanup()
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    

def delay_micro(delay_in_micro) :
  time.sleep(delay_in_micro/1000000.0)
  #print("delay in micro: "+str(delay_in_micro))

def delay_ms(delay_in_millis) :
  time.sleep(delay_in_millis/1000)
  #print("delay ms: "+str(delay_in_millis))


def play_buzzer(buzzer, delay) :
    GPIO.output(buzzer, GPIO.HIGH)
    delay_micro(delay)
    GPIO.output(buzzer, GPIO.LOW)
    delay_micro(delay)
    

def play_tone(note, duration):

  if note == 0:
    return
  
  #This is the semiperiod of each note.
  beepDelay = long(1000000.0/note)
  
  #This is how much time we need to spend on the note.
  time = long((duration*1000.0)/(beepDelay*2))
  
  i = 0
  while i < time:
    play_buzzer(BUZZER_PIN,beepDelay)
    i += 1
  
  GPIO.output(BUZZER_PIN, GPIO.LOW)  
  delay_ms(20)
  
#  print("frequencia: "+str(note)+" duracao: "+str(duration) )

 

songs_rttl = [
'btears:d=4,o=5,b=125:16a#,16f,16f6,16f,16d#6,16f,16c#6,16f,16c6,16f,16c#6,16f,16c6,16f,16a#,16f,16c6,16f,16c#6,16f,16d#6,16f,16c#6,16f,16c6,16f,16g#,16f,16c6,16f,16a#,16f,16a#,16f,16f6,16f,16d#6,16f,16c#6,16f,16c6,16f,16c#6,16f,16c6,16f,16a#,16f,16c6,16f,16c#6,16f,16d#6,16f,16c#6,16f,16c6,16f,16g#,16f,16c6,16f,16a#,16f,8d#,16g#,2f,8d#,8c#,8d#.,8g#.,f.,8d#,8c#,8d#,16g#,2f,8d#,8f,8f#.,g#.,8f.,f#',

'Zelda1:d=4,o=5,b=125:a#,f.,8a#,16a#,16c6,16d6,16d#6,2f6,8p,8f6,16f.6,16f#6,16g#.6,2a#.6,16a#.6,16g#6,16f#.6,8g#.6,16f#.6,2f6,f6,8d#6,16d#6,16f6,2f#6,8f6,8d#6,8c#6,16c#6,16d#6,2f6,8d#6,8c#6,8c6,16c6,16d6,2e6,g6,8f6,16f,16f,8f,16f,16f,8f,16f,16f,8f,8f,a#,f.,8a#,16a#,16c6,16d6,16d#6,2f6,8p,8f6,16f.6,16f#6,16g#.6,2a#.6,c#7,c7,2a6,f6,2f#.6,a#6,a6,2f6,f6,2f#.6,a#6,a6,2f6,d6,2d#.6,f#6,f6,2c#6,a#,c6,16d6,2e6,g6,8f6,16f,16f,8f,16f,16f,8f,16f,16f,8f,8f',

'Popeye:d=4,o=5,b=140:16g.,16f.,16g.,16p,32p,16c.,16p,32p,16c.,16p,32p,16e.,16d.,16c.,16d.,16e.,16f.,g,8p,16a,16f,16a,16c6,16b,16a,16g,16a,16g,8e,16g,16g,16g,16g,8a,16b,32c6,32b,32c6,32b,32c6,32b,8c6',
'tetris3go:d=4,o=5,b=63:16p,16a#,8d#.6,16f6,16f#6,16f6,16d#6,16a#,8g#.,16b,8d#6,16f6,16d#6,8a#.,16b,16a#,16g#,16f,16f#,d#'

]




BUZZER_PIN=25
SONG_TO_PLAY = 0 

try: 

    setup()
 
    for index, songs in enumerate(songs_rttl):      
      song = parse_rtttl(songs_rttl[index])
      for notes in song['notes']:      
        play_tone(notes['frequency'], notes['duration'])
    
except Exception as ex:
    print(ex)

finally:
    GPIO.cleanup()
    #raw_input("Press any key to end")

     





