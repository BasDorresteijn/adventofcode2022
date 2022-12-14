"use strict";
exports.__esModule = true;
var fs = require("fs");
var path = require("path");
var Item;
(function (Item) {
    Item[Item["Nothing"] = 0] = "Nothing";
    Item[Item["Rock"] = 1] = "Rock";
    Item[Item["Sand"] = 2] = "Sand";
})(Item || (Item = {}));
var text = fs.readFileSync(path.join(__dirname, './file.txt'), 'utf-8');
var rows = text.split('\r\n');
var parsedRows = [];
var map = [];
var minX = 0;
var maxX = 1000;
var minY = 0;
var maxY = 0;
for (var _i = 0, rows_1 = rows; _i < rows_1.length; _i++) {
    var row_1 = rows_1[_i];
    var coords = row_1.split(' -> ');
    var parsedRow = [];
    for (var _a = 0, coords_1 = coords; _a < coords_1.length; _a++) {
        var coord = coords_1[_a];
        var coordSplit = coord.split(',');
        var x = parseInt(coordSplit[0]);
        var y = parseInt(coordSplit[1]);
        if (y > maxY) {
            maxY = y;
        }
        var parsedCoord = { x: x, y: y };
        parsedRow.push(parsedCoord);
    }
    parsedRows.push(parsedRow);
}
maxY++;
for (var i = minY; i <= maxY; i++) {
    var row_2 = [];
    for (var j = minX; j <= maxX; j++) {
        row_2.push(Item.Nothing);
    }
    map.push(row_2);
}
maxY++;
var row = [];
for (var j = minX; j <= maxX; j++) {
    row.push(Item.Rock);
}
map.push(row);
for (var _b = 0, parsedRows_1 = parsedRows; _b < parsedRows_1.length; _b++) {
    var parsedRow = parsedRows_1[_b];
    var _loop_1 = function (i) {
        var a = parsedRow[i - 1];
        var b = parsedRow[i];
        var toUpdateItems = void 0;
        if (a.x === b.x) {
            if (a.y > b.y) {
                toUpdateItems = Array.from({ length: a.y - b.y + 1 }, function (_, k) { return ({ x: b.x, y: b.y + k }); });
            }
            else {
                toUpdateItems = Array.from({ length: b.y - a.y + 1 }, function (_, k) { return ({ x: a.x, y: a.y + k }); });
            }
        }
        else {
            if (a.x > b.x) {
                toUpdateItems = Array.from({ length: a.x - b.x + 1 }, function (_, k) { return ({ x: b.x + k, y: b.y }); });
            }
            else {
                toUpdateItems = Array.from({ length: b.x - a.x + 1 }, function (_, k) { return ({ x: a.x + k, y: a.y }); });
            }
        }
        for (var _e = 0, toUpdateItems_1 = toUpdateItems; _e < toUpdateItems_1.length; _e++) {
            var toUpdateItem = toUpdateItems_1[_e];
            map[toUpdateItem.y - minY][toUpdateItem.x - minX] = Item.Rock;
        }
    };
    for (var i = 1; i < parsedRow.length; i++) {
        _loop_1(i);
    }
}
for (var _c = 0, map_1 = map; _c < map_1.length; _c++) {
    var mapRow = map_1[_c];
    var mapRowDrawn = '';
    for (var _d = 0, mapRow_1 = mapRow; _d < mapRow_1.length; _d++) {
        var mapItem = mapRow_1[_d];
        var icon = '.';
        if (mapItem === Item.Rock) {
            icon = '#';
        }
        else if (mapItem === Item.Sand) {
            icon = '0';
        }
        mapRowDrawn += icon;
    }
    console.log(mapRowDrawn);
}
var drawMap = function () {
    for (var _i = 0, map_2 = map; _i < map_2.length; _i++) {
        var mapRow = map_2[_i];
        var mapRowDrawn = '';
        for (var _a = 0, mapRow_2 = mapRow; _a < mapRow_2.length; _a++) {
            var mapItem = mapRow_2[_a];
            var icon = '.';
            if (mapItem === Item.Rock) {
                icon = '#';
            }
            else if (mapItem === Item.Sand) {
                icon = '0';
            }
            mapRowDrawn += icon;
        }
        console.log(mapRowDrawn);
    }
};
var sandStartX = 500 - minX;
var sandStartY = 0;
var sandCount = 0;
while (true) {
    var sandX = sandStartX;
    var sandY = sandStartY;
    if (map[sandY][sandX] === Item.Sand) {
        break;
    }
    while (true) {
        var nextPoint = map[sandY + 1][sandX];
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
drawMap();
console.log("Answer 1: ", sandCount);
// 1004 TO HIGH
