const fs = require('fs');

const data = fs.readFileSync('file.txt', { encoding: 'utf8', flag: 'r' });
const rows = data.split("\r\n");

const maxSize = 25;

box = [];

for (let i = 0; i < maxSize; i++) {
    rowX = []
    for (let j = 0; j < maxSize; j++) {
        rowY = []
        for (let k = 0; k < maxSize; k++) {
            rowY.push(undefined)
        }
        rowX.push(rowY)
    }
    box.push(rowX)
}

const addedNodes = []

for (const row of rows) {
    const result = /(\d*),(\d*),(\d*)/g.exec(row);
    coordX = parseInt(result[1]);
    coordY = parseInt(result[2]);
    coordZ = parseInt(result[3]);
    box[coordX][coordY][coordZ] = { x: coordX, y: coordY, z: coordZ };
    addedNodes.push(box[coordX][coordY][coordZ]);
}

let sidesExposed = 0;
for (const node of addedNodes) {
    // Negative sides
    if (node.x === 0 || !box[node.x - 1][node.y][node.z]) {
        sidesExposed++;
    }

    if (node.y === 0 || !box[node.x][node.y - 1][node.z]) {
        sidesExposed++;
    }

    if (node.z === 0 || !box[node.x][node.y][node.z - 1]) {
        sidesExposed++;
    }

    // Positive sides 
    if (node.x === maxSize || !box[node.x + 1][node.y][node.z]) {
        sidesExposed++;
    }

    if (node.y === maxSize || !box[node.x][node.y + 1][node.z]) {
        sidesExposed++;
    }

    if (node.z === maxSize || !box[node.x][node.y][node.z + 1]) {
        sidesExposed++;
    }
}

console.log('Answer 1:', sidesExposed);

// Mark all outside air as 'lava'

const randomX = 0;
const randomY = 0;
const randomZ = 0;
if (box[randomX][randomY][randomZ]) {
    throw new Error('random node occupied with lava, choose another random space')
}

box[randomX][randomY][randomZ] = { x: randomX, y: randomY, z: randomZ };

let nodesToCheck = [box[randomX][randomY][randomZ]];

while (nodesToCheck.length !== 0) {
    const nextNodes = [];
    for (const nodeToCheck of nodesToCheck) {
        // Negative sides
        if (nodeToCheck.x > 0) {
            if (!box[nodeToCheck.x - 1][nodeToCheck.y][nodeToCheck.z]) {
                box[nodeToCheck.x - 1][nodeToCheck.y][nodeToCheck.z] = { x: nodeToCheck.x - 1, y: nodeToCheck.y, z: nodeToCheck.z }
                nextNodes.push(box[nodeToCheck.x - 1][nodeToCheck.y][nodeToCheck.z])
            }
        }

        if (nodeToCheck.y > 0) {
            if (!box[nodeToCheck.x][nodeToCheck.y - 1][nodeToCheck.z]) {
                box[nodeToCheck.x][nodeToCheck.y - 1][nodeToCheck.z] = { x: nodeToCheck.x, y: nodeToCheck.y - 1, z: nodeToCheck.z }
                nextNodes.push(box[nodeToCheck.x][nodeToCheck.y - 1][nodeToCheck.z])
            }
        }

        if (nodeToCheck.z > 0) {
            if (!box[nodeToCheck.x][nodeToCheck.y][nodeToCheck.z - 1]) {
                box[nodeToCheck.x][nodeToCheck.y][nodeToCheck.z - 1] = { x: nodeToCheck.x, y: nodeToCheck.y, z: nodeToCheck.z - 1 }
                nextNodes.push(box[nodeToCheck.x][nodeToCheck.y][nodeToCheck.z - 1])
            }
        }

        // Positive sides 
        if (nodeToCheck.x < maxSize - 1) {
            if (!box[nodeToCheck.x + 1][nodeToCheck.y][nodeToCheck.z]) {
                box[nodeToCheck.x + 1][nodeToCheck.y][nodeToCheck.z] = { x: nodeToCheck.x + 1, y: nodeToCheck.y, z: nodeToCheck.z }
                nextNodes.push(box[nodeToCheck.x + 1][nodeToCheck.y][nodeToCheck.z])
            }
        }

        if (nodeToCheck.y < maxSize - 1) {
            if (!box[nodeToCheck.x][nodeToCheck.y + 1][nodeToCheck.z]) {
                box[nodeToCheck.x][nodeToCheck.y + 1][nodeToCheck.z] = { x: nodeToCheck.x, y: nodeToCheck.y + 1, z: nodeToCheck.z }
                nextNodes.push(box[nodeToCheck.x][nodeToCheck.y + 1][nodeToCheck.z])
            }
        }

        if (nodeToCheck.z < maxSize - 1) {
            if (!box[nodeToCheck.x][nodeToCheck.y][nodeToCheck.z + 1]) {
                box[nodeToCheck.x][nodeToCheck.y][nodeToCheck.z + 1] = { x: nodeToCheck.x, y: nodeToCheck.y, z: nodeToCheck.z + 1 }
                nextNodes.push(box[nodeToCheck.x][nodeToCheck.y][nodeToCheck.z + 1])
            }
        }

        nodesToCheck = [...new Set(nextNodes)]
    }

}

let insideSides = 0;
for (const node of addedNodes) {
    // Negative sides
    if (node.x !== 0 && !box[node.x - 1][node.y][node.z]) {
        insideSides++;
    }

    if (node.y !== 0 && !box[node.x][node.y - 1][node.z]) {
        insideSides++;
    }

    if (node.z !== 0 && !box[node.x][node.y][node.z - 1]) {
        insideSides++;
    }

    // Positive sides 
    if (node.x !== maxSize && !box[node.x + 1][node.y][node.z]) {
        insideSides++;
    }

    if (node.y !== maxSize && !box[node.x][node.y + 1][node.z]) {
        insideSides++;
    }

    if (node.z !== maxSize && !box[node.x][node.y][node.z + 1]) {
        insideSides++;
    }
}

// Outside exposed sides is first answer minus inside 'exposed' sides
console.log('Answer 2:', sidesExposed - insideSides);
