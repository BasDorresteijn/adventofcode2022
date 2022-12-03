local file = 'file.txt'
local score = 0
local textEnum = {
    Rock = 'Rock',
    Paper = 'Paper',
    Scissors = 'Scissors'
}

local outcomeScore = {
    Win = 6,
    Draw = 3,
    Lose = 0
}

local myPickScore = {
    Rock = 1,
    Paper = 2,
    Scissors = 3
}

local transformOpponentPick = {
    A = textEnum.Rock,
    B = textEnum.Paper,
    C = textEnum.Scissors
}

local transformMyPick = {
    X = textEnum.Rock,
    Y = textEnum.Paper,
    Z = textEnum.Scissors
}

for line in io.lines(file) do
    local opponentPick = transformOpponentPick[string.sub(line, 1, 1)]
    local myPick = transformMyPick[string.sub(line, 3, 3)]

    if opponentPick == myPick then
        score = score + outcomeScore.Draw;
    else
        if (opponentPick == textEnum.Rock and myPick == textEnum.Paper) or
            (opponentPick == textEnum.Paper and myPick == textEnum.Scissors) or
            (opponentPick == textEnum.Scissors and myPick == textEnum.Rock) then
            score = score + outcomeScore.Win
        end
    end

    score = score + myPickScore[myPick]
end

print(score)