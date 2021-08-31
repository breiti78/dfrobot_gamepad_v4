leftButton2 = 0
rightButton2 = 0
backwardButton2 = 0
radio.set_group(1)
forwardButton = 1
backwardButton = 1
rightButton = 1
leftButton = 1

def on_forever():
    global forwardButton, backwardButton2, rightButton2, leftButton2
    forwardButton = pins.digital_read_pin(DigitalPin.P15)
    backwardButton = pins.digital_read_pin(DigitalPin.P13)
    rightButton = pins.digital_read_pin(DigitalPin.P14)
    leftButton = pins.digital_read_pin(DigitalPin.P16)
    if forwardButton == 0:
        radio.send_string("FA")
        forwardButton = 1
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
        basic.pause(100)
    elif pins.digital_read_pin(DigitalPin.P13) == 0:
        radio.send_string("BA")
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
        basic.pause(100)
    elif pins.digital_read_pin(DigitalPin.P14) == 0:
        radio.send_string("RA")
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        basic.pause(100)
    elif pins.digital_read_pin(DigitalPin.P16) == 0:
        radio.send_string("LA")
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        basic.pause(100)
    elif pins.analog_read_pin(AnalogPin.P2) > 550 and (pins.analog_read_pin(AnalogPin.P1) > 400 and pins.analog_read_pin(AnalogPin.P1) < 600):
        radio.send_value("F", pins.analog_read_pin(AnalogPin.P2))
        basic.show_leds("""
            . . # . .
                        . # . # .
                        # . . . #
                        . . . . .
                        . . . . .
        """)
    elif pins.analog_read_pin(AnalogPin.P2) < 450 and (pins.analog_read_pin(AnalogPin.P1) > 400 and pins.analog_read_pin(AnalogPin.P1) < 600):
        radio.send_value("B", pins.analog_read_pin(AnalogPin.P2))
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . #
                        . # . # .
                        . . # . .
        """)
    elif pins.analog_read_pin(AnalogPin.P1) < 450 and (pins.analog_read_pin(AnalogPin.P2) > 400 and pins.analog_read_pin(AnalogPin.P2) < 600):
        radio.send_value("L", pins.analog_read_pin(AnalogPin.P1))
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # . . . .
                        . # . . .
                        . . # . .
        """)
    elif pins.analog_read_pin(AnalogPin.P1) > 550 and (pins.analog_read_pin(AnalogPin.P2) > 400 and pins.analog_read_pin(AnalogPin.P2) < 600):
        radio.send_value("R", pins.analog_read_pin(AnalogPin.P1))
        basic.show_leds("""
            . . # . .
                        . . . # .
                        . . . . #
                        . . . # .
                        . . # . .
        """)
    else:
        radio.send_string("S")
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)
