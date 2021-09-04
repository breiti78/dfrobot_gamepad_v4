LEFT = 0
RIGHT = 1
FORWARD = 2
BACKWARD = 3
DAMAGE = 4

def showStick():
    basic.show_leds("""
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        . . # . .
    """)
def incramental():
    global forwardButton, backwardButton, rightButton, leftButton
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
def setVarsToPins():
    global forwardButton, backwardButton, rightButton, leftButton
    forwardButton = pins.digital_read_pin(DigitalPin.P15)
    backwardButton = pins.digital_read_pin(DigitalPin.P13)
    rightButton = pins.digital_read_pin(DigitalPin.P14)
    leftButton = pins.digital_read_pin(DigitalPin.P16)
def showButtons():
    basic.show_leds("""
        . # # # .
        # . # . #
        # # . # #
        # . # . #
        . # # # .
    """)
def setPins():
    pins.set_pull(DigitalPin.P15, PinPullMode.PULL_UP)
    pins.set_pull(DigitalPin.P13, PinPullMode.PULL_UP)
    pins.set_pull(DigitalPin.P14, PinPullMode.PULL_UP)
    pins.set_pull(DigitalPin.P16, PinPullMode.PULL_UP)
def loop():
    global stickControl
    if input.button_is_pressed(Button.A):
        if stickControl:
            stickControl = False
        else:
            stickControl = True
    if stickControl:
        showStick()
        stickCheck()
    elif input.button_is_pressed(Button.B):
        showButtons()
        incramental()
    else:
        showButtons()
        buttonCheck()
def buttonCheck():
    global forwardButton, backwardButton, rightButton, leftButton
    setVarsToPins()
    if forwardButton == 0:
        radio.send_string("210")
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
        radio.send_string("310")
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
        radio.send_string("110")
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
        radio.send_string("010")
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
stickControl = False
radio.set_group(1)
stickControl = False
setPins()

def on_forever():
    loop()
basic.forever(on_forever)
