function day1part1(fileLocation) {
    const fileData = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split("\r\n")
        .map((x) => parseInt(x));
    let counter = 0;
    let prevValue;
    for (let i = 0; i < fileData.length; i++) {
        if (!prevValue) {
            prevValue = fileData[i];
        } else {
            if (fileData[i] > prevValue) {
                counter++;
            }
            prevValue = fileData[i];
        }
    }
    return counter;
}

function day1part2(fileLocation) {
    const fileData = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split("\r\n")
        .map((x) => parseInt(x));
    let counter = 0;
    let prevValue;
    for (let i = 0; i < fileData.length; i++) {
        if (!prevValue) {
            prevValue = fileData[i] + fileData[i + 1] + fileData[i + 2];
        } else {
            currWindowValue = fileData[i] + fileData[i + 1] + fileData[i + 2];
            if (currWindowValue > prevValue) {
                counter++;
            }
            prevValue = currWindowValue;
        }
    }
    return counter;
}
console.log(day1part1("./day1Part1Input.txt"));
console.log(day1part2("./day1Part1Input.txt"));
