#! /usr/bin/python
import RPi.GPIO as GPIO
import time


sleep_time = 0.05
relay_pins = {'one': 11, 'two':7, 'three':12, 'four':16, 'five':18, 'six':22, 'seven':15, 'eight':13}



def float_pin(off, on):
	if (on != None):
		GPIO.output(on, GPIO.HIGH)
		time.sleep(sleep_time);
	if (off != None):
		GPIO.output(off, GPIO.LOW)
		time.sleep(sleep_time);



GPIO.setmode(GPIO.BOARD)  # use P1 header pin numbering convention
GPIO.setwarnings(False)   # don't want to hear about how pins are already in use



for relay_pin, board_pin in relay_pins.iteritems():
	GPIO.setup(board_pin, GPIO.OUT, GPIO.LOW)
	GPIO.output(board_pin, GPIO.LOW)

for b in xrange(2):
	float_pin(None	             , relay_pins['one']  )
	float_pin(relay_pins['one']  , relay_pins['two']  )
	float_pin(relay_pins['two']  , relay_pins['three'])
	float_pin(relay_pins['three'], relay_pins['four'] )
	float_pin(relay_pins['four'] , relay_pins['five'] )
	float_pin(relay_pins['five'] , relay_pins['six']  )
	float_pin(relay_pins['six']  , relay_pins['seven'])
	float_pin(relay_pins['seven'], relay_pins['eight'])
	float_pin(relay_pins['eight'], relay_pins['seven'])
	float_pin(relay_pins['seven'], relay_pins['six']  )
	float_pin(relay_pins['six']  , relay_pins['five'] )
	float_pin(relay_pins['five'] , relay_pins['four'] )
	float_pin(relay_pins['four'] , relay_pins['three'])
	float_pin(relay_pins['three'], relay_pins['two']  )
	float_pin(relay_pins['two']  , relay_pins['one']  )
	float_pin(relay_pins['one']  , None               )

