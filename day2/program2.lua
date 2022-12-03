local file = 'file.txt'
local score = 0
local pickEnum = {
    Rock = 'Rock',
    Paper = 'Paper',
    Scissors = 'Scissors'
}

local outcomeEnum = {
    Win = 'Win',
    Draw = 'Draw',
    Lose = 'Lose'
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
    A = pickEnum.Rock,
    B = pickEnum.Paper,
    C = pickEnum.Scissors
}

local transformOutcome = {
    X = outcomeEnum.Lose,
    Y = outcomeEnum.Draw,
    Z = outcomeEnum.Win
}

local loseOptionScore = {
    Rock = myPickScore[pickEnum.Scissors],
    Paper = myPickScore[pickEnum.Rock],
    Scissors = myPickScore[pickEnum.Paper],
}

local winOptionScore = {
    Rock = myPickScore[pickEnum.Paper],
    Paper = myPickScore[pickEnum.Scissors],
    Scissors = myPickScore[pickEnum.Rock],
}

for line in io.lines(file) do
    local opponentPick = transformOpponentPick[string.sub(line, 1, 1)]
    local outcome = transformOutcome[string.sub(line, 3, 3)]

    if outcome == outcomeEnum.Lose then
        score = score + loseOptionScore[opponentPick]
    elseif outcome == outcomeEnum.Draw then
        score = score + myPickScore[opponentPick]
    else
        score = score + winOptionScore[opponentPick]
    end

    score = score + outcomeScore[outcome]
end

print(score)