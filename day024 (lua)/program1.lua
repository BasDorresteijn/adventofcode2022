local file = 'file.txt'
local map = {}
local winds = {}
local locations = {
    x2y1 = {
        x = 2,
        y = 1
    }
}
local start_location_x = 2
local start_location_y = 1
local end_location_x = 0
local end_location_y = 0

local file_index = 1
for line in io.lines(file) do
    local row = {};
    for i = 1, string.len(line) do
        local value = string.sub(line, i, i)
        if value == '>' or value == '<' or value == '^' or value == 'v' then
            table.insert(winds, {
                x = i,
                y = file_index,
                direction = value
            })
            value = '.'
        end

        if value == 'E' then
            end_location_x = i
            end_location_y = file_index
        end

        table.insert(row, value)
    end

    table.insert(map, row)
    file_index = file_index + 1;
end

local width = 0
for _ in pairs(map[1]) do
    width = width + 1
end

local function drawWinds()
    for _, wind in pairs(winds) do
        if map[wind.y][wind.x] ~= '.' then
            if type(map[wind.y][wind.x]) == "number" then
                map[wind.y][wind.x] = map[wind.y][wind.x] + 1
            else
                map[wind.y][wind.x] = 2
            end
        else
            map[wind.y][wind.x] = wind.direction
        end
    end
end

local function updateWinds()
    for _, wind in pairs(winds) do
        if wind.direction == '>' then
            if map[wind.y][wind.x + 1] == '#' then
                wind.x = 2
            else
                wind.x = wind.x + 1
            end
        elseif wind.direction == '<' then
            if map[wind.y][wind.x - 1] == '#' then
                wind.x = width - 1
            else
                wind.x = wind.x - 1
            end
        elseif wind.direction == '^' then
            if map[wind.y - 1][wind.x] == '#' then
                wind.y = file_index - 2
            else
                wind.y = wind.y - 1
            end
        else
            if map[wind.y + 1][wind.x] == '#' then
                wind.y = 2
            else
                wind.y = wind.y + 1
            end
        end
    end
end

local function drawMap()
    for _, row in pairs(map) do
        local rowValues = ''
        for _, value in pairs(row) do
            rowValues = rowValues .. value
        end
        print(rowValues)
    end
end

local function resetMap()
    for idxY, row in pairs(map) do
        for idxX, value in pairs(row) do
            if value ~= '#' then
                map[idxY][idxX] = '.'
            end
        end
    end
end

local function updateLocations()
    local next_locations = {}
    for _, location in pairs(locations) do
        local x = location.x
        local y = location.y

        if map[y][x] == '.' then
            next_locations['x' .. x .. 'y' .. y] = {
                x = x,
                y = y
            }
        end

        if y > 1 and map[y - 1][x] == '.' then
            next_locations['x' .. x .. 'y' .. y - 1] = {
                x = x,
                y = y - 1
            }
        end

        if y < end_location_y and map[y + 1][x] == '.' then
            next_locations['x' .. x .. 'y' .. y + 1] = {
                x = x,
                y = y + 1
            }
        end

        if map[y][x + 1] == '.' then
            next_locations['x' .. x + 1 .. 'y' .. y] = {
                x = x + 1,
                y = y
            }
        end

        if map[y][x - 1] == '.' then
            next_locations['x' .. x - 1 .. 'y' .. y] = {
                x = x - 1,
                y = y
            }
        end
    end
    locations = next_locations
end

local function end_reached()
    for _, location in pairs(locations) do
        if location.y == end_location_y and location.x == end_location_x then
            return true
        end
    end
    return false
end

local function start_reached()
    for _, location in pairs(locations) do
        if location.y == start_location_y and location.x == start_location_x then
            return true
        end
    end
    return false
end

local function round()
    resetMap()
    updateWinds()
    drawWinds()
    updateLocations()
    -- drawMap()
end

local total_round_count = 0

for round_count = 1, 100000 do
    round()
    if end_reached() then
        print('Result 1:', round_count)
        total_round_count = round_count
        break
    end
end

local end_location = 'x' .. end_location_x .. 'y' .. end_location_y
locations = {}
locations[end_location] = {
    x = end_location_x,
    y = end_location_y
}

for round_count = 1, 100000 do
    round()
    if start_reached() then
        total_round_count = total_round_count + round_count
        break
    end
end

locations = {
    x2y1 = {
        x = 2,
        y = 1
    }
}

for round_count = 1, 100000 do
    round()
    if end_reached() then
        print('Result 2:', total_round_count + round_count)
        break
    end
end
