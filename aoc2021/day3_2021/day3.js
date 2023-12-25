function day1part1(fileLocation) {
    data = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split("\r\n");
    let gamma = "";
    let epsilon = "";
    for (let i = 0; i < data[0].length; i++) {
        let zeroCounter = 0;
        let oneCounter = 0;
        for (let j = 0; j < data.length; j++) {
            if (data[j][i] == 0) {
                zeroCounter++;
            } else if (data[j][i] == 1) {
                oneCounter++;
            }
        }
        if (zeroCounter > oneCounter) {
            gamma += "0";
            epsilon += "1";
        } else {
            gamma += "1";
            epsilon += "0";
        }
    }
    return parseInt(gamma, 2) * parseInt(epsilon, 2);
}

function day1part2(fileLocation) {
    data = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split("\r\n");
    let oxygenRating = parseInt(findOxygenRating(data, 0), 2);
    let coRating = parseInt(findCoRating(data, 0), 2);
    return oxygenRating * coRating;
}

function findOxygenRating(nums, index) {
    if (nums.length === 1) {
        //this is the base case
        return nums[0];
    } else {
        let zeroCounter = 0;
        let oneCounter = 0;
        let zeroNumbers = [];
        let oneNumbers = [];
        for (let i = 0; i < nums.length; i++) {
            if (nums[i][index] == 0) {
                zeroCounter++;
                zeroNumbers.push(nums[i]);
            } else if (nums[i][index] == 1) {
                oneCounter++;
                oneNumbers.push(nums[i]);
            }
        }
        if (zeroCounter > oneCounter) {
            return findOxygenRating(zeroNumbers, index + 1);
        } else if (oneCounter > zeroCounter) {
            return findOxygenRating(oneNumbers, index + 1);
        } else if (oneCounter == zeroCounter) {
            return findOxygenRating(oneNumbers, index + 1);
        }
    }
}

function findCoRating(nums, index) {
    if (nums.length === 1) {
        //this is the base case
        return nums[0];
    } else {
        let zeroCounter = 0;
        let oneCounter = 0;
        let zeroNumbers = [];
        let oneNumbers = [];
        for (let i = 0; i < nums.length; i++) {
            if (nums[i][index] == 0) {
                zeroCounter++;
                zeroNumbers.push(nums[i]);
            } else if (nums[i][index] == 1) {
                oneCounter++;
                oneNumbers.push(nums[i]);
            }
        }
        if (zeroCounter > oneCounter) {
            return findCoRating(oneNumbers, index + 1);
        } else if (oneCounter > zeroCounter) {
            return findCoRating(zeroNumbers, index + 1);
        } else if (oneCounter == zeroCounter) {
            return findCoRating(zeroNumbers, index + 1);
        }
    }
}

console.log(day1part1("./day3Input.txt"));
console.log(day1part2("./day3Input.txt"));
