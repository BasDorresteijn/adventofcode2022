import * as fs from 'fs';
import * as path from 'path';

const text = fs.readFileSync(path.join(__dirname, './file.txt'), 'utf-8');

const uniqueCharsIndex = (uniqueChars: number): number => {
    for(let i = uniqueChars; i < text.length; i++) {
        let temp = new Set(text.substring(i - uniqueChars, i));
        if(temp.size === uniqueChars) {
            return i;
        }
    }

    return 0;
}

console.log('Answer 1: ', uniqueCharsIndex(4));
console.log('Answer 2: ', uniqueCharsIndex(14));
