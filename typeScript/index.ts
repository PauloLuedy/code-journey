class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    speak(): void {
        console.log(`${this.name} makes a noise.`);
    }
}

class Dog extends Animal {
    constructor(name: string) {
        super(name);
    }

    speak(): void {
        console.log(`${this.name} barks.`);
    }
}

class Cat extends Animal {
    constructor(name: string) {
        super(name);
    }

    speak(): void {
        console.log(`${this.name} meows.`);
    }
}

class Bird extends Animal {
    constructor(name: string) {
        super(name);
    }

    speak(): void {
        console.log(`${this.name} chirps.`);
    }
}

// Example usage:
const cat = new Cat('Whiskers');
cat.speak(); // Output: Whiskers meows. 

const dog = new Dog('Rex');
dog.speak(); // Output: Rex barks.

const bird = new Bird('Tweety');
bird.speak(); // Output: Tweety chirps.
