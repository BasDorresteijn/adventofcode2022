local file = 'file.txt'

local mappedResults = {};
local mappedTodo = {};

for line in io.lines(file) do
    local a, b = string.match(line, "(%a+): (%d+)");
    if a ~= nil then
        mappedResults[a] = b;
    else
        local c, d, e, f = string.match(line, "(%a+): (%a+) (.) (%a+)");
        mappedTodo[c] = {
            left = d,
            operation = e,
            right = f
        }
    end
end

while next(mappedTodo) do
    for key, value in pairs(mappedTodo) do
        local valueA = mappedResults[value.left];
        local valueB = mappedResults[value.right];

        if valueA ~= nil and valueB ~= nil then
            if value.operation == "+" then
                mappedResults[key] = valueA + valueB;
            elseif value.operation == "-" then
                mappedResults[key] = valueA - valueB;
            elseif value.operation == "*" then
                mappedResults[key] = valueA * valueB;
            elseif value.operation == "/" then
                mappedResults[key] = math.ceil(valueA / valueB);
            end

            mappedTodo[key] = nil;
        end
    end
end

print("Answer 1:", mappedResults['root']);
