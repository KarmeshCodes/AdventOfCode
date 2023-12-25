function day2part1(fileLocation) {
    let horizontalCount = 0;
    let verticalCount = 0;
    let fileData = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split("\r\n");

    for (let i = 0; i < fileData.length; i++) {
        let [dir, num] = fileData[i].split(" ");
        if (dir === "forward") {
            horizontalCount += parseInt(num);
        } else if (dir === "up") {
            verticalCount -= parseInt(num);
        } else {
            verticalCount += parseInt(num);
        }
    }

    return horizontalCount * verticalCount;
}

function day2part2(fileLocation) {
    let horizontalCount = 0;
    let verticalCount = 0;
    let aim = 0;
    let fileData = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split("\r\n");

    for (let i = 0; i < fileData.length; i++) {
        let [dir, num] = fileData[i].split(" ");
        if (dir === "forward") {
            horizontalCount += parseInt(num);
            verticalCount += aim * num;
        } else if (dir === "up") {
            aim -= parseInt(num);
        } else {
            aim += parseInt(num);
        }
    }
    return horizontalCount * verticalCount;
}

console.log(day2part1("./day2Input.txt"));
console.log(day2part2("./day2Input.txt"));
