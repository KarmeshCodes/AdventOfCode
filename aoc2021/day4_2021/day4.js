function day4part1(fileLocation) {
    data = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split("\r\n");
    randomNumbers = data[0].split(",");
    let currBoard = [];
    let listOfBoards = [];
    for (let i = 2; i < data.length; i++) {
        let currLineNumbers = data[i]
            .split(" ")
            .filter((x) => x != "")
            .map((x) => ({ value: x, found: false }));
        if (currLineNumbers.length > 0) {
            currBoard.push(currLineNumbers);
            if (i === data.length - 1) {
                listOfBoards.push(new Board(currBoard));
                currBoard = [];
            }
        } else {
            listOfBoards.push(new Board(currBoard));
            currBoard = [];
        }
    }
    for (const num of randomNumbers) {
        for (const theBoard of listOfBoards) {
            if (theBoard.detectWin(num)) {
                return theBoard.getWinningScore(num);
            }
        }
    }
}

function day4part2(fileLocation) {
    data = require("fs")
        .readFileSync(fileLocation, { encoding: "utf-8" })
        .split("\r\n");
    randomNumbers = data[0].split(",");
    let lastWinningBoardScore;
    let currBoard = [];
    let listOfBoards = [];
    for (let i = 2; i < data.length; i++) {
        let currLineNumbers = data[i]
            .split(" ")
            .filter((x) => x != "")
            .map((x) => ({ value: x, found: false }));
        if (currLineNumbers.length > 0) {
            currBoard.push(currLineNumbers);
            if (i === data.length - 1) {
                listOfBoards.push(new Board(currBoard));
                currBoard = [];
            }
        } else {
            listOfBoards.push(new Board(currBoard));
            currBoard = [];
        }
    }
    for (const num of randomNumbers) {
        for (const theBoard of listOfBoards) {
            if (!theBoard.hasWon) {
                if (theBoard.detectWin(num)) {
                    lastWinningBoardScore = theBoard.getWinningScore(num);
                }
            }
        }
    }
    return lastWinningBoardScore;
}

class Board {
    boardNumbers;
    hasWon;
    constructor(boardNumbers) {
        this.boardNumbers = boardNumbers;
    }
    detectWin(num) {
        for (let i = 0; i < this.boardNumbers.length; i++) {
            for (let j = 0; j < this.boardNumbers[i].length; j++) {
                if (this.boardNumbers[i][j].value == num) {
                    this.boardNumbers[i][j].found = true;
                    //only check for win if more than 4 numbers have been drawn
                    if (this.checkVertical(j)) {
                        this.hasWon = true;
                        return true;
                    }
                    if (this.checkHorizontal(i)) {
                        this.hasWon = true;
                        return true;
                    }
                }
            }
        }
        return false;
    }

    checkHorizontal(num) {
        for (let i = 0; i < this.boardNumbers[num].length; i++) {
            if (this.boardNumbers[num][i].found) {
                continue;
            } else {
                return false;
            }
        }
        return true;
    }

    checkVertical(num) {
        for (let i = 0; i < this.boardNumbers[num].length; i++) {
            if (this.boardNumbers[i][num].found) {
                continue;
            } else {
                return false;
            }
        }
        return true;
    }

    getWinningScore(num) {
        let unmarkedCounter = 0;
        for (let i = 0; i < this.boardNumbers.length; i++) {
            for (let j = 0; j < this.boardNumbers[i].length; j++) {
                if (!this.boardNumbers[i][j].found) {
                    unmarkedCounter += parseInt(this.boardNumbers[i][j].value);
                }
            }
        }
        return num * unmarkedCounter;
    }
}

console.log(day4part1("./day4Input.txt"));
console.log(day4part2("./day4Input.txt"));
