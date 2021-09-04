def showStick():
    basic.show_leds("""
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        . . # . .
    """)
def setPins():
    pins.set_pull(DigitalPin.P15, PinPullMode.PULL_UP)
    pins.set_pull(DigitalPin.P13, PinPullMode.PULL_UP)
    pins.set_pull(DigitalPin.P14, PinPullMode.PULL_UP)
    pins.set_pull(DigitalPin.P16, PinPullMode.PULL_UP)
def setVarsToPins():
    if pins.digital_read_pin(DigitalPin.P15) == 0:
        forwardButton = True
    elif pins.digital_read_pin(DigitalPin.P13) == 0:
        backwardButton = True
    elif pins.digital_read_pin(DigitalPin.P14) == 0:
        rightButton = True
    elif pins.digital_read_pin(DigitalPin.P16) == 0:
        leftButton = True
def incremental():
    setVarsToPins()
    if forwardButton == 0:
        radio.send_string("200")
        basic.show_leds("""
            . . # . .
            . # . # .
            # . . . #
            . . . . .
            . . . . .
        """)
        basic.pause(100)
        forwardButton = 1
    elif backwardButton == 0:
        radio.send_string("300")
        backwardButton = 1
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . #
            . # . # .
            . . # . .
        """)
        basic.pause(100)
    elif rightButton == 0:
        radio.send_string("100")
        rightButton = 1
        basic.show_leds("""
            . . # . .
            . . . # .
            . . . . #
            . . . # .
            . . # . .
        """)
        basic.pause(100)
    elif leftButton == 0:
        radio.send_string("000")
        leftButton = 1
        basic.show_leds("""
            . . # . .
            . # . . .
            # . . . .
            . # . . .
            . . # . .
        """)
        basic.pause(100)
    else:
        sendStop()
def stickCheck():
    if pins.analog_read_pin(AnalogPin.P2) > 550 and (pins.analog_read_pin(AnalogPin.P1) > 400 and pins.analog_read_pin(AnalogPin.P1) < 600):
        radio.send_value("forward", pins.analog_read_pin(AnalogPin.P2))
        basic.show_leds("""
            . . # . .
            . # . # .
            # . # . #
            . . . . .
            . . # . .
        """)
    elif pins.analog_read_pin(AnalogPin.P2) < 450 and (pins.analog_read_pin(AnalogPin.P1) > 400 and pins.analog_read_pin(AnalogPin.P1) < 600):
        radio.send_value("backward", pins.analog_read_pin(AnalogPin.P2))
        basic.show_leds("""
            . . # . .
            . . . . .
            # . # . #
            . # . # .
            . . # . .
        """)
    elif pins.analog_read_pin(AnalogPin.P1) < 450 and (pins.analog_read_pin(AnalogPin.P2) > 400 and pins.analog_read_pin(AnalogPin.P2) < 600):
        radio.send_value("left", pins.analog_read_pin(AnalogPin.P1))
        basic.show_leds("""
            . . # . .
            . # . . .
            # . # . #
            . # . . .
            . . # . .
        """)
    elif pins.analog_read_pin(AnalogPin.P1) > 550 and (pins.analog_read_pin(AnalogPin.P2) > 400 and pins.analog_read_pin(AnalogPin.P2) < 600):
        radio.send_value("right", pins.analog_read_pin(AnalogPin.P1))
        basic.show_leds("""
            . . # . .
            . . . # .
            # . # . #
            . . . # .
            . . # . .
        """)
    else:
        sendStop()
def sendStop():
    radio.send_string("S")

def showButtons():
    basic.show_leds("""
        . # # # .
        # . # . #
        # # . # #
        # . # . #
        . # # # .
    """)

def buttonCheck():
    setVarsToPins()
    if forwardButton == 0:
        radio.send_string("310")
        forwardButton = 1
        basic.show_leds("""
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
        """)
        basic.pause(100)
    elif backwardButton == 0:
        radio.send_string("410")
        backwardButton = 1
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
        """)
        basic.pause(100)
    elif rightButton == 0:
        radio.send_string("210")
        rightButton = 1
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
        """)
        basic.pause(100)
    elif leftButton == 0:
        radio.send_string("110")
        leftButton = 1
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
        """)
        basic.pause(100)
    else:
        sendStop()

leftButton = 0
rightButton = 0
backwardButton = 0
forwardButton = 0
LEFT = 0
DAMAGE = 0
BACKWARD = 0
FORWARD = 0
RIGHT = 0

LEFT = 1
RIGHT = 2
FORWARD = 3
BACKWARD = 4
DAMAGE = 5
leftButton = 1
rightButton = 1
backwardButton = 1
forwardButton = 1
radio.set_group(1)
setPins()

def on_forever():
    stickControl = False
    if input.button_is_pressed(Button.A):
        if stickControl == True:
            stickControl = False
        else:
            stickControl = True
    if stickControl == True:
        showStick()
        stickCheck()
    elif input.button_is_pressed(Button.B):
        showButtons()
        incremental()
    else:
        showButtons()
        buttonCheck()
basic.forever(on_forever)
