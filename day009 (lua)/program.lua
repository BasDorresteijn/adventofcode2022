local file = 'file.txt'

local function getTailTraversedNodeCount(ropeLength)
    local passedPoints = {}
    local snakePoints = {}

    local function determinePosTail(indexToCompare)
        if indexToCompare + 1 > ropeLength then
            return
        end

        local firstNode = snakePoints[indexToCompare];
        local secondNode = snakePoints[indexToCompare + 1];

        local deltaX = firstNode.x - secondNode.x
        local deltaY = firstNode.y - secondNode.y
        if math.abs(deltaX) > 1 or math.abs(deltaY) > 1 then
            if (deltaX > 0) then
                secondNode.x = secondNode.x + 1
            end

            if (deltaX < 0) then
                secondNode.x = secondNode.x - 1
            end

            if (deltaY > 0) then
                secondNode.y = secondNode.y + 1
            end

            if (deltaY < 0) then
                secondNode.y = secondNode.y - 1
            end
        end

        determinePosTail(indexToCompare + 1)
    end

    for _ = 1, ropeLength do
        table.insert(snakePoints, {
            x = 100,
            y = 100
        });
    end

    for line in io.lines(file) do
        local direction = string.sub(line, 1, 1)
        local amount = string.sub(line, 3, -1)

        for _ = 1, amount do
            if direction == 'R' then
                snakePoints[1].x = snakePoints[1].x + 1;
            elseif direction == 'L' then
                snakePoints[1].x = snakePoints[1].x - 1;
            elseif direction == 'D' then
                snakePoints[1].y = snakePoints[1].y - 1;
            elseif direction == 'U' then
                snakePoints[1].y = snakePoints[1].y + 1;
            end

            determinePosTail(1)
            local tail = snakePoints[ropeLength]
            passedPoints[tail.x .. ':' .. tail.y] = true
        end
    end

    local count = 0
    for _ in pairs(passedPoints) do
        count = count + 1
    end

    return count;
end

print('Answer 1:', getTailTraversedNodeCount(2))
print('Answer 2:', getTailTraversedNodeCount(10))
