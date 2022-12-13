const fs = require('fs');

const data = fs.readFileSync('day004/file.txt', { encoding: 'utf8', flag: 'r' });
const result1 = data.split('\n').filter(x => {
    if (!x) return false;
    const sections = x.split(',');
    const sectionA = sections[0].split('-');
    const sectionB = sections[1].split('-');
    const minContainRangeA = parseInt(sectionA[0], 10);
    const maxContainRangeA = parseInt(sectionA[1], 10);
    const minContainRangeB = parseInt(sectionB[0], 10);
    const maxContainRangeB = parseInt(sectionB[1], 10);
    return (minContainRangeA <= minContainRangeB && maxContainRangeA >= maxContainRangeB) || (minContainRangeB <= minContainRangeA && maxContainRangeB >= maxContainRangeA)
})

console.log('Answer 1: ', result1.length);

const result2 = data.split('\n').filter(x => {
    if (!x) return false;
    const sections = x.split(',');
    const sectionA = sections[0].split('-');
    const sectionB = sections[1].split('-');
    const minContainRangeA = parseInt(sectionA[0], 10);
    const maxContainRangeA = parseInt(sectionA[1], 10);
    const minContainRangeB = parseInt(sectionB[0], 10);
    const maxContainRangeB = parseInt(sectionB[1], 10);
    return (minContainRangeA >= minContainRangeB && minContainRangeA <= maxContainRangeB) || (minContainRangeB >= minContainRangeA && minContainRangeB <= maxContainRangeA) ||
        (minContainRangeB >= minContainRangeA && minContainRangeB <= maxContainRangeA) || (minContainRangeA >= minContainRangeB && minContainRangeA <= maxContainRangeB)
})

console.log('Answer 2: ', result2.length);
