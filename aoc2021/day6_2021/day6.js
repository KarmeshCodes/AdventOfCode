function day6part1(fileLocation) {
    const data = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split(",")
        .map((x) => parseInt(x));
    for (let i = 0; i < 18; i++) {
        for (let j = 0; j < data.length; j++) {
            if (data[j] != 0) {
                data[j]--;
            } else {
                data[j] = 6;
                data.push(9);
            }
        }
    }
    return data.length;
}
function day6part2(fileLocation) {
    const data = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split(",")
        .map((x) => parseInt(x));
    let fishCounterMap = new Map();
    for (let i = 0; i < data.length; i++) {
        if (!fishCounterMap.has(data[i])) {
            fishCounterMap.set(data[i], 1);
        } else {
            fishCounterMap.set(data[i], fishCounterMap.get(data[i]) + 1);
        }
    }

    for (let i = 0; i < 256; i++) {
        let newMap = new Map();
        for (let key of fishCounterMap.keys()) {
            if (key === 0) {
                if (newMap.has(6)) {
                    newMap.set(6, newMap.get(6) + fishCounterMap.get(key));
                } else {
                    newMap.set(6, fishCounterMap.get(key));
                }
                newMap.set(8, fishCounterMap.get(key));
            } else {
                if (newMap.has(key - 1)) {
                    newMap.set(
                        key - 1,
                        newMap.get(key - 1) + fishCounterMap.get(key)
                    );
                } else {
                    newMap.set(key - 1, fishCounterMap.get(key));
                }
            }
        }
        console.log(newMap);
        fishCounterMap = newMap;
    }
    //console.log(fishCounterMap);
    let fishCounter = 0;
    for (key of fishCounterMap.keys()) {
        fishCounter += fishCounterMap.get(key);
    }
    return fishCounter;
}

//console.log(day6part1("./day6Input.txt"));
console.log(day6part2("./day6Input.txt"));
