using System.Text.RegularExpressions;

void program1()
{
    var input = File.ReadAllText(@"file.txt");
    var inputSplit = input.Split("\n").ToList();
    var emptyRowIndex = inputSplit.FindIndex(x => x == "\r");
    var treeInput = inputSplit.Take(emptyRowIndex).ToList();

    var findTreeSize = new Regex(".*(\\d).*?\\s");

    var treeSize = int.Parse(findTreeSize.Match(treeInput.Last()).Groups.Values.Skip(1).First().Value);

    var tree = new List<Stack<char>>();
    for (var i = 0; i < treeSize; i++)
    {
        tree.Add(new Stack<char>());
    }

    treeInput.Reverse();
    foreach (var treeItem in treeInput.Skip(1).ToList())
    {
        for (var i = 0; i < treeItem.Length; i++)
        {
            if (i % 4 == 1)
            {
                var c = treeItem[i];
                if (c != ' ')
                {
                    var treeIndex = (i - 1) / 4;
                    tree[treeIndex].Push(c);
                }
            }
        }
    }

    var getMovement = new Regex("move (\\d*) from (\\d*) to (\\d*)");
    var instructions = inputSplit.Skip(emptyRowIndex + 1).ToList();
    foreach (var instruction in instructions)
    {
        var instructionResult = getMovement.Match(instruction);
        if (!instructionResult.Success) continue;
        var amount = int.Parse(instructionResult.Groups.Values.Skip(1).First().Value);
        var from = int.Parse(instructionResult.Groups.Values.Skip(2).First().Value) - 1;
        var to = int.Parse(instructionResult.Groups.Values.Skip(3).First().Value) - 1;

        for (var i = 0; i < amount; i++)
        {
            var toMoveItem = tree[from].Pop();
            tree[to].Push(toMoveItem);
        }
    }

    var result = new string(tree.Select(x => x.Pop()).ToArray());

    Console.WriteLine("Answer 1: " + result);
}

void program2()
{
    var input = File.ReadAllText(@"file.txt");
    var inputSplit = input.Split("\n").ToList();
    var emptyRowIndex = inputSplit.FindIndex(x => x == "\r");
    var treeInput = inputSplit.Take(emptyRowIndex).ToList();

    var findTreeSize = new Regex(".*(\\d).*?\\s");

    var treeSize = int.Parse(findTreeSize.Match(treeInput.Last()).Groups.Values.Skip(1).First().Value);

    var tree = new List<List<char>>();
    for (var i = 0; i < treeSize; i++)
    {
        tree.Add(new List<char>());
    }

    treeInput.Reverse();
    foreach (var treeItem in treeInput.Skip(1).ToList())
    {
        for (var i = 0; i < treeItem.Length; i++)
        {
            if (i % 4 == 1)
            {
                var c = treeItem[i];
                if (c != ' ')
                {
                    var treeIndex = (i - 1) / 4;
                    tree[treeIndex].Add(c);
                }
            }
        }
    }

    var getMovement = new Regex("move (\\d*) from (\\d*) to (\\d*)");
    var instructions = inputSplit.Skip(emptyRowIndex + 1).ToList();
    foreach (var instruction in instructions)
    {
        var instructionResult = getMovement.Match(instruction);
        if (!instructionResult.Success) continue;
        var amount = int.Parse(instructionResult.Groups.Values.Skip(1).First().Value);
        var from = int.Parse(instructionResult.Groups.Values.Skip(2).First().Value) - 1;
        var to = int.Parse(instructionResult.Groups.Values.Skip(3).First().Value) - 1;

        var fromTree = tree[from];
        var toMoveItems = fromTree.Skip(fromTree.Count - amount).ToList();
        fromTree.RemoveRange(fromTree.Count - amount, amount);
        tree[to].AddRange(toMoveItems);
    }

    var result = new string(tree.Select(x => x.Last()).ToArray());

    Console.WriteLine("Answer 2: " + result);
}

program1();
program2();
