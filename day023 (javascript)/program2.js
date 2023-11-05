const fs = require('fs');

const data = fs.readFileSync('file.txt', { encoding: 'utf8', flag: 'r' });
const rows = data.split("\r\n");

const width = rows[0].length;
const extraSpace = 100;
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

let roundCount = 1;
while (true) {
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

    if (actualMoves.length === 0) {
        break;
    }

    moves = [];
    moveOrder.push(moveOrder.shift())

    roundCount++;
}

console.log("Result 2:", roundCount);