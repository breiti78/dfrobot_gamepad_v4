function showStick () {
    basic.showLeds(`
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        . . # . .
        `)
}
function readPins () {
    x = pins.analogReadPin(AnalogPin.P1) - 512
    y = pins.analogReadPin(AnalogPin.P2) - 512
    if (pins.digitalReadPin(DigitalPin.P15) == 0) {
        radio.sendString("P15")
        last_button = "P15"
        basic.pause(50)
    } else if (pins.digitalReadPin(DigitalPin.P13) == 0) {
        radio.sendString("P13")
        last_button = "P13"
        basic.pause(50)
    } else if (pins.digitalReadPin(DigitalPin.P14) == 0) {
        radio.sendString("P14")
        last_button = "P14"
        basic.pause(50)
    } else if (pins.digitalReadPin(DigitalPin.P16) == 0) {
        radio.sendString("P16")
        last_button = "P16"
        basic.pause(50)
    } else if (x > 10 || x < -10) {
        radio.sendValue("x", x)
    } else if (y > 10 || y < -10) {
        radio.sendValue("y", y)
    } else if (pins.digitalReadPin(DigitalPin.P8) == 0) {
        radio.sendString("P8")
        last_button = "P8"
        basic.pause(50)
    } else {
        sendStop()
    }
}
input.onButtonPressed(Button.A, function () {
    radio.sendString("A")
    last_button = "A"
    basic.pause(50)
})
function sendStop () {
    radio.sendString("S")
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
input.onButtonPressed(Button.AB, function () {
    radio.sendString("A+B")
    last_button = "A+B"
    basic.pause(50)
})
function setPins () {
    pins.setPull(DigitalPin.P15, PinPullMode.PullUp)
    pins.setPull(DigitalPin.P13, PinPullMode.PullUp)
    pins.setPull(DigitalPin.P14, PinPullMode.PullUp)
    pins.setPull(DigitalPin.P16, PinPullMode.PullUp)
    pins.setPull(DigitalPin.P8, PinPullMode.PullUp)
}
input.onButtonPressed(Button.B, function () {
    radio.sendString("B")
    last_button = "B"
    basic.pause(50)
})
function buttonCheck () {
    readPins()
    if (last_button == "P15") {
        images.arrowImage(ArrowNames.North).showImage(0)
    } else if (last_button == "P13") {
        images.arrowImage(ArrowNames.South).showImage(0)
    } else if (last_button == "P14") {
        images.arrowImage(ArrowNames.East).showImage(0)
    } else if (last_button == "P16") {
        images.arrowImage(ArrowNames.West).showImage(0)
    } else {
    	
    }
}
let last_button = ""
let y = 0
let x = 0
radio.setGroup(1)
setPins()
basic.forever(function () {
    readPins()
})
