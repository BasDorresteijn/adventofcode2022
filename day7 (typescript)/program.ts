import * as fs from 'fs';
import * as path from 'path';
type TreeType = { folders: { [key: string]: TreeType }, files: { name: string, size: number }[] }

const text = fs.readFileSync(path.join(__dirname, './file.txt'), 'utf-8');
const tree: TreeType = { folders: {}, files: [] };
let treePath: TreeType[] = [tree];
const outputSplit = text.split('\r\n');
outputSplit.forEach(x => {
    if (x.startsWith('$')) {
        if (x.startsWith('$ cd /')) {
            treePath = [tree];
        } else if (x.startsWith('$ cd ..')) {
            treePath.pop();
        } else if (x.startsWith('$ cd')) {
            const folderName = x.replace('$ cd ', '');
            const tree = treePath[treePath.length - 1].folders[folderName] ??= { folders: {}, files: [] };
            treePath.push(tree)
        }
    } else {
        const info = x.split(' ');
        const size = parseInt(info[0], 10)
        if (!isNaN(size)) {
            treePath[treePath.length - 1].files.push({ name: info[1], size: size })
        }

    }
})

let masterTotal = 0;
let totalsPerFolder: number[] = [];
const getDirectoryTotal = (subTree: TreeType): number => {
    let total = 0;
    for (const key of Object.keys(subTree.folders)) {
        total += getDirectoryTotal(subTree.folders[key]);
    }
    for (const file of subTree.files) {
        total += file.size;
    }

    if (total <= 100000) {
        masterTotal += total;
    }
    totalsPerFolder.push(total)

    return total;
}

const rootDirectorySize = getDirectoryTotal(tree);
const sizeAvailable = 70000000 - rootDirectorySize;
const sizeRequired = 30000000 - sizeAvailable;

console.log('Answer 1: ', masterTotal);

let smallestFittingFolder = rootDirectorySize;
for (const totalOfFolder of totalsPerFolder) {
    if (totalOfFolder >= sizeRequired && totalOfFolder < smallestFittingFolder) {
        smallestFittingFolder = totalOfFolder;
    }
}

console.log('Answer 2: ', smallestFittingFolder);
