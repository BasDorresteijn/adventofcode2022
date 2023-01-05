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

mappedResults['humn'] = nil;
mappedTodo['root'].operation = '=';

local calculationDone = true;

while calculationDone do
    calculationDone = false;
    for key, value in pairs(mappedTodo) do
        local valueA = mappedResults[value.left];
        local valueB = mappedResults[value.right];
        local valueC = mappedResults[key];

        if valueA ~= nil and valueB ~= nil then
            if value.operation == "+" then
                mappedResults[key] = valueA + valueB;
            elseif value.operation == "-" then
                mappedResults[key] = valueA - valueB;
            elseif value.operation == "*" then
                mappedResults[key] = valueA * valueB;
            elseif value.operation == "/" then
                mappedResults[key] = math.ceil(valueA / valueB);
            else
                goto continue
            end

            mappedTodo[key] = nil;
            calculationDone = true;
        elseif key == 'root' then
            if valueA ~= nil then
                mappedResults[value.right] = valueA
            elseif valueB ~= nil then
                mappedResults[value.left] = valueB
            else
                goto continue
            end

            mappedTodo[key] = nil;
            calculationDone = true;

        elseif valueC ~= nil and valueA ~= nil then
            if value.operation == "+" then
                mappedResults[value.right] = math.abs(valueC - valueA);
            elseif value.operation == "-" then
                mappedResults[value.right] = valueA - valueC;
            elseif value.operation == "*" then
                mappedResults[value.right] = math.ceil(valueC / valueA);
            elseif value.operation == "/" then
                mappedResults[value.right] = math.ceil(valueA / valueC);
            else
                goto continue
            end

            mappedTodo[key] = nil;
            calculationDone = true;
        elseif valueC ~= nil and valueB ~= nil then
            if value.operation == "+" then
                mappedResults[value.left] = math.abs(valueC - valueB);
            elseif value.operation == "-" then
                mappedResults[value.left] = valueC + valueB;
            elseif value.operation == "*" then
                mappedResults[value.left] = math.ceil(valueC / valueB);
            elseif value.operation == "/" then
                mappedResults[value.left] = valueC * valueB;
            else
                goto continue
            end

            mappedTodo[key] = nil;
            calculationDone = true;
        end

        ::continue::
    end
end

print("Answer 2:", mappedResults['humn']);
