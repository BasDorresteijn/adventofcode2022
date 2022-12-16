local file = 'file.txt'
local toCheckRow = 2000000;
local pointsOnRow = {};

for line in io.lines(file) do
    local a, b, c, d = string.match(line, "(%-?%d+).-(%-?%d+).-(%-?%d+).-(%-?%d+)");
    local sensorX, sensorY, beaconX, beaconY = tonumber(a, 10), tonumber(b, 10), tonumber(c, 10), tonumber(d, 10);

    if beaconY == toCheckRow then
        pointsOnRow[beaconX] = false
    end

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

    if (sensorY > toCheckRow and sensorY - manhattan > toCheckRow) or
        (sensorY < toCheckRow and sensorY + manhattan < toCheckRow) then
        goto continue
    end

    local deltaX = 0
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

    for i = leftX, rightX, 1 do
        if pointsOnRow[i] ~= false then
            pointsOnRow[i] = true
        end
    end

    ::continue::
end

local count = 0
for v in pairs(pointsOnRow) do
    if pointsOnRow[v] then
        count = count + 1
    end
end

print(count)
