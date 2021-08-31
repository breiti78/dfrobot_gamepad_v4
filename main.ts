function setVarToPin () {
    forwardButton = pins.digitalReadPin(DigitalPin.P15)
    backwardButton = pins.digitalReadPin(DigitalPin.P13)
    rightButton = pins.digitalReadPin(DigitalPin.P14)
    leftButton = pins.digitalReadPin(DigitalPin.P16)
}
function incramental () {
    if (forwardButton == 0) {
        radio.sendString("slowForward")
        forwardButton = 1
        basic.showLeds(`
            . . # . .
            . # . # .
            # . . . #
            . . . . .
            . . . . .
            `)
        basic.pause(100)
    } else if (backwardButton == 0) {
        radio.sendString("slowBackward")
        backwardButton = 1
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . #
            . # . # .
            . . # . .
            `)
        basic.pause(100)
    } else if (rightButton == 0) {
        radio.sendString("oneDegreeRight")
        rightButton = 1
        basic.showLeds(`
            . . # . .
            . . . # .
            . . . . #
            . . . # .
            . . # . .
            `)
        basic.pause(100)
    } else if (leftButton == 0) {
        radio.sendString("oneDegreeLeft")
        leftButton = 1
        basic.showLeds(`
            . . # . .
            . # . . .
            # . . . .
            . # . . .
            . . # . .
            `)
        basic.pause(100)
    } else {
        sendStop()
    }
}
function stickCheck () {
    if (pins.analogReadPin(AnalogPin.P2) > 550 && (pins.analogReadPin(AnalogPin.P1) > 400 && pins.analogReadPin(AnalogPin.P1) < 600)) {
        radio.sendValue("F", pins.analogReadPin(AnalogPin.P2))
        basic.showLeds(`
            . . # . .
            . # . # .
            # . # . #
            . . . . .
            . . # . .
            `)
    } else if (pins.analogReadPin(AnalogPin.P2) < 450 && (pins.analogReadPin(AnalogPin.P1) > 400 && pins.analogReadPin(AnalogPin.P1) < 600)) {
        radio.sendValue("B", pins.analogReadPin(AnalogPin.P2))
        basic.showLeds(`
            . . # . .
            . . . . .
            # . # . #
            . # . # .
            . . # . .
            `)
    } else if (pins.analogReadPin(AnalogPin.P1) < 450 && (pins.analogReadPin(AnalogPin.P2) > 400 && pins.analogReadPin(AnalogPin.P2) < 600)) {
        radio.sendValue("L", pins.analogReadPin(AnalogPin.P1))
        basic.showLeds(`
            . . # . .
            . # . . .
            # . # . #
            . # . . .
            . . # . .
            `)
    } else if (pins.analogReadPin(AnalogPin.P1) > 550 && (pins.analogReadPin(AnalogPin.P2) > 400 && pins.analogReadPin(AnalogPin.P2) < 600)) {
        radio.sendValue("R", pins.analogReadPin(AnalogPin.P1))
        basic.showLeds(`
            . . # . .
            . . . # .
            # . # . #
            . . . # .
            . . # . .
            `)
    } else {
        sendStop()
    }
}
function sendStop () {
    radio.sendString("S")
}
function buttonCheck () {
    if (forwardButton == 0) {
        radio.sendString("FA")
        forwardButton = 1
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
        basic.pause(100)
    } else if (backwardButton == 0) {
        radio.sendString("BA")
        backwardButton = 1
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
        basic.pause(100)
    } else if (rightButton == 0) {
        radio.sendString("RA")
        rightButton = 1
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
        basic.pause(100)
    } else if (leftButton == 0) {
        radio.sendString("LA")
        leftButton = 1
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
        basic.pause(100)
    } else {
        sendStop()
    }
}
function setPin () {
    pins.setPull(DigitalPin.P13, PinPullMode.PullUp)
    pins.setPull(DigitalPin.P14, PinPullMode.PullUp)
    pins.setPull(DigitalPin.P15, PinPullMode.PullUp)
    pins.setPull(DigitalPin.P16, PinPullMode.PullUp)
}
let leftButton = 0
let rightButton = 0
let backwardButton = 0
let forwardButton = 0
radio.setGroup(1)
forwardButton = 1
backwardButton = 1
rightButton = 1
leftButton = 1
let stickControl = false
setPin()
basic.forever(function () {
    setVarToPin()
    if (input.buttonIsPressed(Button.A)) {
        if (stickControl) {
            stickControl = false
            basic.showLeds(`
                . # # # .
                # . # . #
                # # . # #
                # . # . #
                . # # # .
                `)
        } else {
            stickControl = true
            basic.showLeds(`
                . # # # .
                # # # # #
                . # # # .
                . . # . .
                . . # . .
                `)
        }
    }
    if (stickControl) {
        stickCheck()
        basic.showLeds(`
            . # # # .
            # # # # #
            . # # # .
            . . # . .
            . . # . .
            `)
    } else if (input.buttonIsPressed(Button.B)) {
        incramental()
    } else {
        buttonCheck()
        basic.showLeds(`
            . # # # .
            # . # . #
            # # . # #
            # . # . #
            . # # # .
            `)
    }
})
