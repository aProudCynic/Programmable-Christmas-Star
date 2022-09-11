export class Colour {
    red: number;
    green: number;
    blue: number;

    constructor(hexCode?: string) {
        if (!hexCode) {
            this.red = 0;
            this.green = 0;
            this.blue = 0;
        } else {
            if (!hexCode.match(/#[a-fA-F0-9]{6}/)) {
                throw new Error(`Hex code is invalid: ${hexCode}`)
            }
            this.red = parseInt(hexCode.slice(1, 3), 16);
            this.green = parseInt(hexCode.slice(3, 5), 16);
            this.blue = parseInt(hexCode.slice(5, 7), 16);
        }
    }
}
