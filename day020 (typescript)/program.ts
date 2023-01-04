import * as fs from 'fs';
import * as path from 'path';

interface Item {
    value: number;
    moved: boolean;
}

const text = fs.readFileSync(path.join(__dirname, './file.txt'), 'utf-8');
const rows = text.split('\r\n');
const filePayload = rows.map(x => <Item>{ moved: false, value: parseInt(x, 10) })

const payloadSize = filePayload.length;
let toMoveItemIndex = 0;

while (toMoveItemIndex !== -1) {
    const toMoveItem = filePayload[toMoveItemIndex];
    let newPosition = toMoveItemIndex;
    if (toMoveItem.value > 0) {
        newPosition = (toMoveItemIndex + toMoveItem.value) % (payloadSize - 1);
    } else if (toMoveItem.value < 0) {
        newPosition = (toMoveItemIndex + toMoveItem.value) % (payloadSize - 1);
        if (newPosition < 0) {
            newPosition = payloadSize - 1 + newPosition;
        }
    }

    if (newPosition === 0) {
        newPosition = payloadSize - 1;
    }

    filePayload.splice(toMoveItemIndex, 1);
    filePayload.splice(newPosition, 0, toMoveItem);
    toMoveItem.moved = true;

    toMoveItemIndex = filePayload.findIndex(x => !x.moved)
}

const zeroIdx = filePayload.findIndex(x => x.value === 0);

const firstItem = filePayload[((zeroIdx + 1000) % payloadSize)].value;
const secondItem = filePayload[((zeroIdx + 2000) % payloadSize)].value;
const thirdItem = filePayload[((zeroIdx + 3000) % payloadSize)].value;

console.log('Answer 1:', firstItem + secondItem + thirdItem)
