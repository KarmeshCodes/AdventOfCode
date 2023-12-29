function day7part1(fileLocation) {
    const data = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split(",")
        .map((x) => parseInt(x));
    let lowestFuel = Number.MAX_VALUE;
    for (let i = 0; i < 2000; i++) {
        let cost = 0;
        data.forEach((element) => {
            cost += Math.abs(element - i);
        });
        if (cost < lowestFuel) {
            lowestFuel = cost;
        }
    }
    return lowestFuel;
}

function day7part2(fileLocation) {
    const data = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split(",")
        .map((x) => parseInt(x));
    let lowestFuel = Number.MAX_VALUE;
    for (let i = 0; i < 2000; i++) {
        let cost = 0;
        data.forEach((element) => {
            cost += (Math.abs(element - i) * (Math.abs(element - i) + 1)) / 2;
        });
        if (cost < lowestFuel) {
            lowestFuel = cost;
        }
    }
    return lowestFuel;
}

console.log(day7part1("./day7Input.txt"));
console.log(day7part2("./day7Input.txt"));
