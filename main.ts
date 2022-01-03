function showStick () {
    basic.showLeds(`
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        . . # . .
        `)
}
function stickCheck () {
    if (pins.analogReadPin(AnalogPin.P2) > 550 && (pins.analogReadPin(AnalogPin.P1) > 400 && pins.analogReadPin(AnalogPin.P1) < 600)) {
        radio.sendValue("forward", pins.analogReadPin(AnalogPin.P2))
        basic.showLeds(`
            . . # . .
            . # . # .
            # . # . #
            . . . . .
            . . # . .
            `)
    } else if (pins.analogReadPin(AnalogPin.P2) < 450 && (pins.analogReadPin(AnalogPin.P1) > 400 && pins.analogReadPin(AnalogPin.P1) < 600)) {
        radio.sendValue("backward", pins.analogReadPin(AnalogPin.P2))
        basic.showLeds(`
            . . # . .
            . . . . .
            # . # . #
            . # . # .
            . . # . .
            `)
    } else if (pins.analogReadPin(AnalogPin.P1) < 450 && (pins.analogReadPin(AnalogPin.P2) > 400 && pins.analogReadPin(AnalogPin.P2) < 600)) {
        radio.sendValue("left", pins.analogReadPin(AnalogPin.P1))
        basic.showLeds(`
            . . # . .
            . # . . .
            # . # . #
            . # . . .
            . . # . .
            `)
    } else if (pins.analogReadPin(AnalogPin.P1) > 550 && (pins.analogReadPin(AnalogPin.P2) > 400 && pins.analogReadPin(AnalogPin.P2) < 600)) {
        radio.sendValue("right", pins.analogReadPin(AnalogPin.P1))
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
function setVarsToPins () {
    if (pins.digitalReadPin(DigitalPin.P15) == 0) {
        forwardButton = true
    } else if (pins.digitalReadPin(DigitalPin.P13) == 0) {
        backwardButton = true
    } else if (pins.digitalReadPin(DigitalPin.P14) == 0) {
        rightButton = true
    } else if (pins.digitalReadPin(DigitalPin.P16) == 0) {
        leftButton = true
    }
}
function showButtons () {
    basic.showLeds(`
        . # # # .
        # . # . #
        # # . # #
        # . # . #
        . # # # .
        `)
}
function setPins () {
    pins.setPull(DigitalPin.P15, PinPullMode.PullUp)
    pins.setPull(DigitalPin.P13, PinPullMode.PullUp)
    pins.setPull(DigitalPin.P14, PinPullMode.PullUp)
    pins.setPull(DigitalPin.P16, PinPullMode.PullUp)
}
function buttonCheck () {
    setVarsToPins()
    if (forwardButton) {
        radio.sendString("310")
        images.arrowImage(ArrowNames.North).showImage(0)
        basic.pause(100)
    } else if (backwardButton) {
        radio.sendString("410")
        images.arrowImage(ArrowNames.South).showImage(0)
        basic.pause(100)
    } else if (rightButton) {
        radio.sendString("210")
        images.arrowImage(ArrowNames.East).showImage(0)
        basic.pause(100)
    } else if (leftButton) {
        let LEFT = 0
        radio.sendString("" + LEFT + "10")
        images.arrowImage(ArrowNames.West).showImage(0)
        basic.pause(100)
    } else {
        sendStop()
    }
}
let stickControl = false
let leftButton = false
let rightButton = false
let backwardButton = false
let forwardButton = false
radio.setGroup(1)
setPins()
basic.forever(function () {
    if (input.buttonIsPressed(Button.AB)) {
        if (stickControl) {
            stickControl = false
        } else {
            stickControl = true
        }
    }
    if (stickControl) {
        showStick()
        stickCheck()
    } else if (input.buttonIsPressed(Button.B)) {
        showButtons()
    } else {
        showButtons()
        buttonCheck()
    }
})
