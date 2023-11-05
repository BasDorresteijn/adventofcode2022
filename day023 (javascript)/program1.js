const fs = require('fs');

const data = fs.readFileSync('file.txt', { encoding: 'utf8', flag: 'r' });
const rows = data.split("\r\n");

const width = rows[0].length;
const extraSpace = 20;
const roundCount = 10;
let map = []

for (let i = 0; i < extraSpace; i++) {
    map.push(Array(2 * extraSpace + width).fill('.'))
}

for (const row of rows) {
    const mapRow = [];
    for (let i = 0; i < extraSpace; i++) {
        mapRow.push('.')
    }

    for (const char of row) {
        mapRow.push(char)
    }

    for (let i = 0; i < extraSpace; i++) {
        mapRow.push('.')
    }
    map.push(mapRow)
}

for (let i = 0; i < extraSpace; i++) {
    map.push(Array(2 * extraSpace + width).fill('.'))
}

let moves = [];

function moveNorth(xIdx, yIdx) {
    const canMove = map[yIdx - 1][xIdx] !== '#' && map[yIdx - 1][xIdx + 1] !== '#' && map[yIdx - 1][xIdx - 1] !== '#'
    if (canMove) {
        moves.push({ xOld: xIdx, yOld: yIdx, xNew: xIdx, yNew: yIdx - 1 })
        return true;
    }
    return false;
}

function moveEast(xIdx, yIdx) {
    const canMove = map[yIdx][xIdx + 1] !== '#' && map[yIdx + 1][xIdx + 1] !== '#' && map[yIdx - 1][xIdx + 1] !== '#'
    if (canMove) {
        moves.push({ xOld: xIdx, yOld: yIdx, xNew: xIdx + 1, yNew: yIdx })
        return true;
    }
    return false;
}

function moveSouth(xIdx, yIdx) {
    const canMove = map[yIdx + 1][xIdx] !== '#' && map[yIdx + 1][xIdx + 1] !== '#' && map[yIdx + 1][xIdx - 1] !== '#'
    if (canMove) {
        moves.push({ xOld: xIdx, yOld: yIdx, xNew: xIdx, yNew: yIdx + 1 })
        return true;
    }
    return false;
}

function moveWest(xIdx, yIdx) {
    const canMove = map[yIdx][xIdx - 1] !== '#' && map[yIdx + 1][xIdx - 1] !== '#' && map[yIdx - 1][xIdx - 1] !== '#'
    if (canMove) {
        moves.push({ xOld: xIdx, yOld: yIdx, xNew: xIdx - 1, yNew: yIdx })
        return true;
    }
    return false;
}

function shouldMove(xIdx, yIdx) {
    return map[yIdx + 1][xIdx] === '#' || map[yIdx - 1][xIdx] === '#' || map[yIdx + 1][xIdx + 1] === '#' || map[yIdx - 1][xIdx + 1] === '#' ||
        map[yIdx][xIdx - 1] === '#' || map[yIdx][xIdx + 1] === '#' || map[yIdx - 1][xIdx - 1] === '#' || map[yIdx + 1][xIdx - 1] === '#'
}

let moveOrder = [
    moveNorth,
    moveSouth,
    moveWest,
    moveEast,
]

for (let round = 1; round <= roundCount; round++) {
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[i].length; j++) {
            if (map[i][j] === '#' && shouldMove(j, i)) {
                for (const move of moveOrder) {
                    if (move(j, i)) {
                        break;
                    }
                }
            }
        }
    }

    let actualMoves = []
    for (const move of moves) {
        if (moves.filter(x => x.xNew === move.xNew && x.yNew === move.yNew).length === 1) {
            actualMoves.push(move)
        }
    }

    for (const actualMove of actualMoves) {
        map[actualMove.yOld][actualMove.xOld] = '.'
        map[actualMove.yNew][actualMove.xNew] = '#'
    }

    moves = [];
    moveOrder.push(moveOrder.shift())
}

while (map[0].indexOf('#') === -1) {
    map.shift()
}

while (map[map.length - 1].indexOf('#') === -1) {
    map.pop() === '#'
}

let outerEdgeL = 100000;
for (let i = 0; i < map.length; i++) {
    for (let j = 0; j < map[i].length; j++) {
        if (map[i][j] === '#' && j < outerEdgeL) {
            outerEdgeL = j;
            break;
        }
    }
}

for (let i = 0; i < map.length; i++) {
    for (let j = 0; j < outerEdgeL; j++) {
        if (map[i].shift() === '#') {
            console.log('error??!');
        }
    }
}

let outerEdgeR = 100000;
for (let i = 0; i < map.length; i++) {
    for (let j = map[i].length; j > 0; j--) {
        if (map[i][j] === '#' && (map[i].length - 1 - j) < outerEdgeR) {
            outerEdgeR = map[i].length - 1 - j;
            break;
        }
    }
}

for (let i = 0; i < map.length; i++) {
    for (let j = 0; j < outerEdgeR; j++) {
        if (map[i].pop() === '#') {
            console.log('error??!');
        }
    }
}

for (const row of map) {
    console.log(row.join(""))
}

let counter = 0;
for (const row of map) {
    for (const i of row) {
        if (i === '.') {
            counter++;
        }
    }
}

console.log("Result 1:", counter);
