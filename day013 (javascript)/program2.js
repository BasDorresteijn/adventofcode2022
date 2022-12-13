const fs = require('fs');

const data = fs.readFileSync('file.txt', { encoding: 'utf8', flag: 'r' });

const rows = data.split("\r\n").filter(x => x).map(x => eval(x));

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

dividerPackage2 = [[2]]
dividerPackage6 = [[6]]
rows.push(dividerPackage2, dividerPackage6)
sortedRows = [];

for (const row of rows) {
    let insertBefore = sortedRows.findIndex(x => compareTrees(row, x) === ReturnType.IncorrectOrder);
    if (insertBefore === -1) {
        insertBefore = sortedRows.length;
    }
    sortedRows.splice(insertBefore, 0, row);
}

sortedRows.reverse();
console.log("Answer 2:", (sortedRows.indexOf(dividerPackage2) + 1) * (sortedRows.indexOf(dividerPackage6) + 1));
