var input = File.ReadAllText(@"file.txt");
var splitInput = input.Split("\r\n");
var previousTrees = new List<Tree>();
var allTrees = new List<Tree>();
foreach (var row in splitInput)
{
    var treeHeights = row.ToCharArray().Select(x => x - '0').ToList();
    var currentItems = new List<Tree>();
    for (var i = 0; i < treeHeights.Count; i++)
    {
        var tree = new Tree { Height = treeHeights[i] };
        if (currentItems.LastOrDefault() != null)
        {
            tree.Left = currentItems.Last();
            currentItems.Last().Right = tree;
        }

        if (previousTrees.Any())
        {
            tree.Top = previousTrees[i];
            previousTrees[i].Bottom = tree;
        }

        currentItems.Add(tree);
    }

    previousTrees = currentItems;
    allTrees.AddRange(currentItems);
}

Console.WriteLine("Answer 1: " + allTrees.Count(x => x.Visible));
Console.WriteLine("Answer 2: " + allTrees.Max(x => x.ScenicScore));

class Tree
{
    public int Height { get; set; }
    public Tree? Top { get; set; }
    public Tree? Bottom { get; set; }
    public Tree? Right { get; set; }
    public Tree? Left { get; set; }

    private bool TopVisible
    {
        get
        {
            var topItem = Top;
            while (topItem != null)
            {
                if (topItem.Height >= Height) return false;
                topItem = topItem.Top;
            }

            return true;
        }
    }

    private bool BottomVisible
    {
        get
        {
            var bottomItem = Bottom;
            while (bottomItem != null)
            {
                if (bottomItem.Height >= Height) return false;
                bottomItem = bottomItem.Bottom;
            }

            return true;
        }
    }

    private bool LeftVisible
    {
        get
        {
            var leftItem = Left;
            while (leftItem != null)
            {
                if (leftItem.Height >= Height) return false;
                leftItem = leftItem.Left;
            }

            return true;
        }
    }

    private bool RightVisible
    {
        get
        {
            var rightItem = Right;
            while (rightItem != null)
            {
                if (rightItem.Height >= Height) return false;
                rightItem = rightItem.Right;
            }

            return true;
        }
    }

    private int TreesVisibleTop
    {
        get
        {
            var treesVisible = 0;
            var topItem = Top;
            while (topItem != null)
            {
                treesVisible++;
                if (topItem.Height >= Height) return treesVisible;
                topItem = topItem.Top;
            }

            return treesVisible;
        }
    }

    private int TreesVisibleBottom
    {
        get
        {
            var treesVisible = 0;
            var bottomItem = Bottom;
            while (bottomItem != null)
            {
                treesVisible++;
                if (bottomItem.Height >= Height) return treesVisible;
                bottomItem = bottomItem.Bottom;
            }

            return treesVisible;
        }
    }

    private int TreesVisibleLeft
    {
        get
        {
            var treesVisible = 0;
            var leftItem = Left;
            while (leftItem != null)
            {
                treesVisible++;
                if (leftItem.Height >= Height) return treesVisible;
                leftItem = leftItem.Left;
            }

            return treesVisible;
        }
    }

    private int TreesVisibleRight
    {
        get
        {
            var treesVisible = 0;
            var topItem = Right;
            while (topItem != null)
            {
                treesVisible++;
                if (topItem.Height >= Height) return treesVisible;
                topItem = topItem.Right;
            }

            return treesVisible;
        }
    }

    public bool Visible => TopVisible || BottomVisible || LeftVisible || RightVisible;
    public int ScenicScore => TreesVisibleTop * TreesVisibleBottom * TreesVisibleLeft * TreesVisibleRight;
}
