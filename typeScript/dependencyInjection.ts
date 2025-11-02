class Lamp {
    turnOn(): void {
        console.log("Lamp is turned on");
    }
}

class Switch {
    private lamp: Lamp;

    constructor(lamp: Lamp) {
        this.lamp = lamp;
    }

    operate(): void {
        this.lamp.turnOn();
    }
}

// Usage
const myLamp = new Lamp();
const mySwitch = new Switch(myLamp);
mySwitch.operate();