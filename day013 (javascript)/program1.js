const fs = require('fs');

const data = fs.readFileSync('file.txt', { encoding: 'utf8', flag: 'r' });

const rows = data.split("\r\n");

const ReturnType = {
    CorrectOrder: 0,
    IncorrectOrder: 1,
    Next: 2,
    Error: 3
}

const compareTrees = (tree1, tree2) => {
    if (typeof tree1 === 'number' && typeof tree2 === 'number') {
        if (tree1 === tree2) {
            return ReturnType.Next;
        } else if (tree1 < tree2) {
            return ReturnType.CorrectOrder;
        } else {
            return ReturnType.IncorrectOrder;
        }
    }

    if (typeof tree1 === 'number') {
        tree1 = [tree1]
    }

    if (typeof tree2 === 'number') {
        tree2 = [tree2]
    }

    let i = 0;
    while (true) {
        let item1 = tree1[i]
        let item2 = tree2[i]
        if (item1 === undefined && item2 === undefined) {
            return ReturnType.Next;
        }
        if (item1 === undefined) {
            return ReturnType.CorrectOrder;
        }
        if (item2 === undefined) {
            return ReturnType.IncorrectOrder;
        }

        let result = compareTrees(tree1[i], tree2[i])
        if (result !== ReturnType.Next) {
            return result;
        }

        i++;
    }
}

let i = 0;
let total = 0
while (i < rows.length) {
    let treeA = eval(rows[i]);
    let treeB = eval(rows[i + 1]);

    i += 3;

    if (compareTrees(treeA, treeB) === ReturnType.CorrectOrder) {
        total += i / 3
    }
}

console.log("Answer 1:", total);
