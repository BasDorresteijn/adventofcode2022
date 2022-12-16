local file = 'file.txt';
local maxX = 4000000;

local parsedRows = {};

local function parseRows()
    for line in io.lines(file) do
        local a, b, c, d = string.match(line, "(%-?%d+).-(%-?%d+).-(%-?%d+).-(%-?%d+)");
        local sensorX, sensorY, beaconX, beaconY = tonumber(a, 10), tonumber(b, 10), tonumber(c, 10), tonumber(d, 10);

        local xDifference = 0;
        if sensorX < 0 and beaconX > 0 then
            xDifference = math.abs(beaconX - sensorX);
        elseif beaconX < 0 and sensorX > 0 then
            xDifference = math.abs(sensorX - beaconX);
        else
            xDifference = math.abs(sensorX - beaconX);
        end

        local yDifference = 0;
        if sensorY < 0 and beaconY > 0 then
            yDifference = math.abs(beaconY - sensorY);
        elseif beaconY < 0 and sensorY > 0 then
            yDifference = math.abs(sensorY - beaconY);
        else
            yDifference = math.abs(sensorY - beaconY);
        end

        local manhattan = xDifference + yDifference;

        table.insert(parsedRows, {
            sensorX = sensorX,
            sensorY = sensorY,
            manhattan = manhattan
        })
    end
end

local function checkRowPrecise(toCheckRow)
    local pointsOnRow = {};
    local leftToRight = {};
    for line in pairs(parsedRows) do
        local value = parsedRows[line];
        local sensorX = value.sensorX;
        local sensorY = value.sensorY;
        local manhattan = value.manhattan;

        if (sensorY > toCheckRow and sensorY - manhattan > toCheckRow) or
            (sensorY < toCheckRow and sensorY + manhattan < toCheckRow) then
            goto continue
        end

        local deltaX = manhattan
        if sensorY > toCheckRow then
            deltaX = sensorY - manhattan - toCheckRow
        end
        if sensorY < toCheckRow then
            deltaX = sensorY + manhattan - toCheckRow
        end

        local rightX = sensorX + deltaX;
        local leftX = sensorX - deltaX;

        if leftX > rightX then
            leftX, rightX = rightX, leftX;
        end

        if leftX < 0 then
            leftX = 0;
        end

        if rightX > maxX then
            rightX = maxX
        end

        table.insert(pointsOnRow, leftX);
        if leftToRight[leftX] == nil then
            leftToRight[leftX] = rightX;
        else
            if leftToRight[leftX] < rightX then
                leftToRight[leftX] = rightX
            end
        end

        ::continue::
    end

    table.sort(pointsOnRow);

    local highestRightValue = 0;
    for nextValue in pairs(pointsOnRow) do
        local leftValue = pointsOnRow[nextValue];
        if highestRightValue == 0 then
            highestRightValue = leftToRight[pointsOnRow[nextValue]];
        else
            if leftValue <= highestRightValue + 1 then
                local rightValue = leftToRight[leftValue];
                if rightValue > highestRightValue then
                    highestRightValue = rightValue;
                end
            end
        end
    end

    if highestRightValue ~= maxX then
        return highestRightValue + 1;
    end

    return -1;
end

local function checkRow(toCheckRow)
    local pointsOnRow = {};
    for line in pairs(parsedRows) do
        local value = parsedRows[line];
        local sensorX = value.sensorX;
        local sensorY = value.sensorY;
        local manhattan = value.manhattan;

        if (sensorY > toCheckRow and sensorY - manhattan > toCheckRow) or
            (sensorY < toCheckRow and sensorY + manhattan < toCheckRow) then
            goto continue
        end

        local deltaX = manhattan
        if sensorY > toCheckRow then
            deltaX = sensorY - manhattan - toCheckRow
        end
        if sensorY < toCheckRow then
            deltaX = sensorY + manhattan - toCheckRow
        end

        local rightX = sensorX + deltaX;
        local leftX = sensorX - deltaX;

        if leftX > rightX then
            leftX, rightX = rightX, leftX;
        end

        if leftX < 0 then
            leftX = 0;
        end

        if rightX > maxX then
            rightX = maxX
        end

        table.insert(pointsOnRow, leftX);
        table.insert(pointsOnRow, rightX);

        ::continue::
    end

    table.sort(pointsOnRow);

    local prevValue = 1;
    for nextValue in pairs(pointsOnRow) do
        if math.abs(pointsOnRow[nextValue] - pointsOnRow[prevValue]) == 2 then
            return checkRowPrecise(toCheckRow)
        end

        prevValue = nextValue
    end

    return -1;
end

parseRows();

for y = 0, maxX, 1 do
    if y % 1000 == 0 then
        print('checking y:', y)
    end
    local result = checkRow(y)
    if result ~= -1 then
        print('x', result, 'y', y)
        print('answer 2', result * maxX + y)
        break
    end
end

-- 831012 MIN
-- 6853792 TO HIGH

-- 2523555 MIN
