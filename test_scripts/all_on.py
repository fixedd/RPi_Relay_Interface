#! /usr/bin/python
import RPi.GPIO as GPIO

relay_pins = {'one': 11, 'two':7, 'three':12, 'four':16, 'five':18, 'six':22, 'seven':15, 'eight':13}

GPIO.setmode(GPIO.BOARD)  # use P1 header pin numbering convention
GPIO.setwarnings(False)   # don't want to hear about how pins are already in use

for relay_pin, board_pin in relay_pins.iteritems():
	GPIO.setup(board_pin, GPIO.OUT)
	GPIO.output(board_pin, GPIO.HIGH)

