function day5part1(fileLocation) {
    let totalPoints = 0;
    let cordsMap = new Map();
    const data = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split("\r\n")
        .map((x) => {
            return x.replace(/\s+/g, "").split("->"); //review this later
        });
    for (let i = 0; i < data.length; i++) {
        let coordinate1 = data[i][0];
        let coordinate2 = data[i][1];
        let coordinate1Nums = coordinate1.split(",").map((x) => parseInt(x));
        let coordinate2Nums = coordinate2.split(",").map((x) => parseInt(x));
        if (coordinate1Nums[0] === coordinate2Nums[0]) {
            if (coordinate2Nums[1] > coordinate1Nums[1]) {
                for (let j = coordinate1Nums[1]; j <= coordinate2Nums[1]; j++) {
                    if (cordsMap.has(coordinate1Nums[0] + "," + j)) {
                        if (!cordsMap.get(coordinate1Nums[0] + "," + j)) {
                            cordsMap.set(coordinate1Nums[0] + "," + j, true);
                            totalPoints++;
                        }
                    } else {
                        cordsMap.set(coordinate1Nums[0] + "," + j, false);
                    }
                }
            } else if (coordinate2Nums[1] < coordinate1Nums[1]) {
                for (let j = coordinate2Nums[1]; j <= coordinate1Nums[1]; j++) {
                    if (cordsMap.has(coordinate2Nums[0] + "," + j)) {
                        if (!cordsMap.get(coordinate2Nums[0] + "," + j)) {
                            cordsMap.set(coordinate2Nums[0] + "," + j, true);
                            totalPoints++;
                        }
                    } else {
                        cordsMap.set(coordinate2Nums[0] + "," + j, false);
                    }
                }
            }
        }
        if (coordinate1Nums[1] === coordinate2Nums[1]) {
            if (coordinate2Nums[0] > coordinate1Nums[0]) {
                for (let j = coordinate1Nums[0]; j <= coordinate2Nums[0]; j++) {
                    if (cordsMap.has(j + "," + coordinate1Nums[1])) {
                        if (!cordsMap.get(j + "," + coordinate1Nums[1])) {
                            cordsMap.set(j + "," + coordinate1Nums[1], true);
                            totalPoints++;
                        }
                    } else {
                        cordsMap.set(j + "," + coordinate1Nums[1], false);
                    }
                }
            } else if (coordinate2Nums[0] < coordinate1Nums[0]) {
                for (let j = coordinate2Nums[0]; j <= coordinate1Nums[0]; j++) {
                    if (cordsMap.has(j + "," + coordinate2Nums[1])) {
                        if (!cordsMap.get(j + "," + coordinate2Nums[1])) {
                            cordsMap.set(j + "," + coordinate1Nums[1], true);
                            totalPoints++;
                        }
                    } else {
                        cordsMap.set(j + "," + coordinate2Nums[1], false);
                    }
                }
            }
        }
    }
    return totalPoints;
}

function day5part2(fileLocation) {
    let totalPoints = 0;
    let cordsMap = new Map();
    const data = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split("\r\n")
        .map((x) => {
            return x.replace(/\s+/g, "").split("->"); //review this later
        });
    for (let i = 0; i < data.length; i++) {
        let coordinate1 = data[i][0];
        let coordinate2 = data[i][1];
        let coordinate1Nums = coordinate1.split(",").map((x) => parseInt(x));
        let coordinate2Nums = coordinate2.split(",").map((x) => parseInt(x));
        if (coordinate1Nums[0] === coordinate2Nums[0]) {
            // vertical line
            if (coordinate2Nums[1] > coordinate1Nums[1]) {
                for (let j = coordinate1Nums[1]; j <= coordinate2Nums[1]; j++) {
                    if (cordsMap.has(coordinate1Nums[0] + "," + j)) {
                        if (!cordsMap.get(coordinate1Nums[0] + "," + j)) {
                            cordsMap.set(coordinate1Nums[0] + "," + j, true);
                            totalPoints++;
                        }
                    } else {
                        cordsMap.set(coordinate1Nums[0] + "," + j, false);
                    }
                }
            } else if (coordinate2Nums[1] < coordinate1Nums[1]) {
                for (let j = coordinate2Nums[1]; j <= coordinate1Nums[1]; j++) {
                    if (cordsMap.has(coordinate2Nums[0] + "," + j)) {
                        if (!cordsMap.get(coordinate2Nums[0] + "," + j)) {
                            cordsMap.set(coordinate2Nums[0] + "," + j, true);
                            totalPoints++;
                        }
                    } else {
                        cordsMap.set(coordinate2Nums[0] + "," + j, false);
                    }
                }
            }
        } else if (coordinate1Nums[1] === coordinate2Nums[1]) {
            //horizontal line
            if (coordinate2Nums[0] > coordinate1Nums[0]) {
                for (let j = coordinate1Nums[0]; j <= coordinate2Nums[0]; j++) {
                    if (cordsMap.has(j + "," + coordinate1Nums[1])) {
                        if (!cordsMap.get(j + "," + coordinate1Nums[1])) {
                            cordsMap.set(j + "," + coordinate1Nums[1], true);
                            totalPoints++;
                        }
                    } else {
                        cordsMap.set(j + "," + coordinate1Nums[1], false);
                    }
                }
            } else if (coordinate2Nums[0] < coordinate1Nums[0]) {
                for (let j = coordinate2Nums[0]; j <= coordinate1Nums[0]; j++) {
                    if (cordsMap.has(j + "," + coordinate2Nums[1])) {
                        if (!cordsMap.get(j + "," + coordinate2Nums[1])) {
                            cordsMap.set(j + "," + coordinate1Nums[1], true);
                            totalPoints++;
                        }
                    } else {
                        cordsMap.set(j + "," + coordinate2Nums[1], false);
                    }
                }
            }
        } else {
            //this is a diagonal line
            let temp1 = coordinate1Nums[0];
            let temp2 = coordinate1Nums[1];
            while (temp1 != coordinate2Nums[0] && temp2 != coordinate2Nums[1]) {
                if (cordsMap.has(temp1 + "," + temp2)) {
                    if (!cordsMap.get(temp1 + "," + temp2)) {
                        cordsMap.set(temp1 + "," + temp2, true);
                        totalPoints++;
                    }
                } else {
                    cordsMap.set(temp1 + "," + temp2, false);
                }
                if (temp1 > coordinate2Nums[0]) {
                    temp1--;
                } else if (temp1 < coordinate2Nums[0]) {
                    temp1++;
                }
                if (temp2 > coordinate2Nums[1]) {
                    temp2--;
                } else if (temp2 < coordinate2Nums[1]) {
                    temp2++;
                }
            }
            if (cordsMap.has(temp1 + "," + temp2)) {
                if (!cordsMap.get(temp1 + "," + temp2)) {
                    cordsMap.set(temp1 + "," + temp2, true);
                    totalPoints++;
                }
            } else {
                cordsMap.set(temp1 + "," + temp2, false);
            }
        }
    }
    return totalPoints;
}

console.log(day5part1("./day5Input.txt"));
console.log(day5part2("./day5Input.txt"));
