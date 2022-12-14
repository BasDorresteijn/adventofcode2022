import * as fs from 'fs';
import * as path from 'path';

interface Coord {
    x: number;
    y: number;
}

enum Item {
    Nothing = 0,
    Rock = 1,
    Sand = 2
}

const text = fs.readFileSync(path.join(__dirname, './file.txt'), 'utf-8');
const rows = text.split('\r\n');
const parsedRows: Coord[][] = [];
const map: Item[][] = [];
let minX: number = 0;
let maxX: number = 1000;
let minY: number = 0;
let maxY: number = 0;

for (const row of rows) {
    const coords = row.split(' -> ');
    const parsedRow: Coord[] = [];
    for (const coord of coords) {
        const coordSplit = coord.split(',');
        const x = parseInt(coordSplit[0]);
        const y = parseInt(coordSplit[1]);
        if (y > maxY) {
            maxY = y;
        }

        const parsedCoord = <Coord>{ x: x, y: y }
        parsedRow.push(parsedCoord);
    }

    parsedRows.push(parsedRow);
}

maxY++;

for (let i = minY; i <= maxY; i++) {
    const row: Item[] = [];
    for (let j = minX; j <= maxX; j++) {
        row.push(Item.Nothing);
    }
    map.push(row);
}

maxY++;

const row: Item[] = [];
for (let j = minX; j <= maxX; j++) {
    row.push(Item.Rock);
}
map.push(row);


for (const parsedRow of parsedRows) {
    for (let i = 1; i < parsedRow.length; i++) {
        const a = parsedRow[i - 1];
        const b = parsedRow[i];
        let toUpdateItems: Coord[];
        if (a.x === b.x) {
            if (a.y > b.y) {
                toUpdateItems = Array.from({ length: a.y - b.y + 1 }, (_, k) => <Coord>{ x: b.x, y: b.y + k });
            } else {
                toUpdateItems = Array.from({ length: b.y - a.y + 1 }, (_, k) => <Coord>{ x: a.x, y: a.y + k });
            }
        } else {
            if (a.x > b.x) {
                toUpdateItems = Array.from({ length: a.x - b.x + 1 }, (_, k) => <Coord>{ x: b.x + k, y: b.y });
            } else {
                toUpdateItems = Array.from({ length: b.x - a.x + 1 }, (_, k) => <Coord>{ x: a.x + k, y: a.y });
            }
        }

        for (const toUpdateItem of toUpdateItems) {
            map[toUpdateItem.y - minY][toUpdateItem.x - minX] = Item.Rock;
        }
    }
}


for (const mapRow of map) {
    let mapRowDrawn = '';
    for (const mapItem of mapRow) {
        let icon = '.';
        if (mapItem === Item.Rock) {
            icon = '#';
        } else if (mapItem === Item.Sand) {
            icon = '0';
        }
        mapRowDrawn += icon;
    }
    console.log(mapRowDrawn);
}

const sandStartX = 500 - minX;
const sandStartY = 0;

let sandCount = 0;

while (true) {
    let sandX = sandStartX;
    let sandY = sandStartY;

    if (map[sandY][sandX] === Item.Sand) {
        break;
    }

    while (true) {
        let nextPoint = map[sandY + 1][sandX];
        if (nextPoint === Item.Nothing) {
            sandY += 1;
            continue;
        }
        nextPoint = map[sandY + 1][sandX - 1];
        if (nextPoint === Item.Nothing) {
            sandY += 1;
            sandX -= 1;
            continue;
        }
        nextPoint = map[sandY + 1][sandX + 1];
        if (nextPoint === Item.Nothing) {
            sandY += 1;
            sandX += 1;
            continue;
        }

        map[sandY][sandX] = Item.Sand;
        break;
    }

    sandCount++;
}
console.log("Answer 2: ", sandCount);
