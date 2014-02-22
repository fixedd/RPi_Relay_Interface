#! /usr/bin/python
import RPi.GPIO as GPIO

relay_pins = {'one': 12, 'two':16, 'three':18, 'four':22}

GPIO.setmode(GPIO.BOARD)  # use P1 header pin numbering convention
GPIO.setwarnings(False)   # don't want to hear about how pins are already in use

for relay_pin, board_pin in relay_pins.iteritems():
	GPIO.setup(board_pin, GPIO.OUT)
	GPIO.output(board_pin, GPIO.LOW)

