using System.Text.RegularExpressions;
List<MineralMiningExpedition> Expeditions = new List<MineralMiningExpedition>();

var input = File.ReadAllText(@"file.txt");
var splitInput = input.Split("\r\n");
var total = 0;
var readRowRegex = new Regex("Blueprint \\d*: Each ore robot costs (\\d*) ore. Each clay robot costs (\\d*) ore. Each obsidian robot costs (\\d*) ore and (\\d*) clay. Each geode robot costs (\\d*) ore and (\\d*) obsidian\\.");

for (int i = 0; i < splitInput.Length; i++)
{
    var row = splitInput[i];
    var regexResult = readRowRegex.Match(row);

    var startItem1 = new MineralMiningExpedition()
    {
        NextMiner = MinerType.Ore,
        Expeditions = Expeditions,
        OreMinerOreCost = int.Parse(regexResult.Groups.Values.ElementAt(1).Value),
        ClayMinerOreCost = int.Parse(regexResult.Groups.Values.ElementAt(2).Value),
        ObsidianMinerOreCost = int.Parse(regexResult.Groups.Values.ElementAt(3).Value),
        ObsidianMinerClayCost = int.Parse(regexResult.Groups.Values.ElementAt(4).Value),
        GeodeMinerOreCost = int.Parse(regexResult.Groups.Values.ElementAt(5).Value),
        GeodeMinerObsidianCost = int.Parse(regexResult.Groups.Values.ElementAt(6).Value)
    };
    var startItem2 = new MineralMiningExpedition()
    {
        NextMiner = MinerType.Clay,
        Expeditions = Expeditions,
        OreMinerOreCost = int.Parse(regexResult.Groups.Values.ElementAt(1).Value),
        ClayMinerOreCost = int.Parse(regexResult.Groups.Values.ElementAt(2).Value),
        ObsidianMinerOreCost = int.Parse(regexResult.Groups.Values.ElementAt(3).Value),
        ObsidianMinerClayCost = int.Parse(regexResult.Groups.Values.ElementAt(4).Value),
        GeodeMinerOreCost = int.Parse(regexResult.Groups.Values.ElementAt(5).Value),
        GeodeMinerObsidianCost = int.Parse(regexResult.Groups.Values.ElementAt(6).Value)
    };
    Expeditions.Add(startItem1);
    Expeditions.Add(startItem2);

    for (int j = 0; j < 24; j++)
    {
        Expeditions.ToList().ForEach(x => x.DoCycle());
    }

    var highestCount = Expeditions.Max(x => x.Geode);
    var subResult = (i + 1) * highestCount;
    Console.WriteLine($"Id {i + 1}, Geodes {highestCount}, SubResult {subResult}");
    total += subResult;

    Expeditions.Clear();
}

Console.WriteLine($"Answer 1: {total}");

enum MinerType
{
    Ore = 0,
    Clay = 1,
    Obsidian = 2,
    Geode = 3
}

class MineralMiningExpedition
{
    public List<MineralMiningExpedition> Expeditions { init; private get; } = new List<MineralMiningExpedition>();
    public MinerType NextMiner { init; private get; }
    public Action BuildMiner = () => { };
    private int CycleCount;

    private int Ore;
    private int Clay;
    private int Obsidian;
    public int Geode { private set; get; }

    private int OreMinerCount = 1;
    private int ClayMinerCount;
    private int ObsidianMinerCount;
    private int GeodeMinerCount;

    // Costs
    public int OreMinerOreCost { init; private get; }
    public int ClayMinerOreCost { init; private get; }
    public int ObsidianMinerOreCost { init; private get; }
    public int ObsidianMinerClayCost { init; private get; }
    public int GeodeMinerOreCost { init; private get; }
    public int GeodeMinerObsidianCost { init; private get; }

    public override string ToString()
    {
        return @$"
            Ores: {Ore} | {OreMinerCount}
            Clay: {Clay} | {ClayMinerCount}
            Obsidian: {Obsidian} | {ObsidianMinerCount}
            Geode: {Geode} | {GeodeMinerCount}
            CycleCount: {CycleCount}
        ";
    }

    public string Log = "";

    public void DoCycle()
    {
        CycleCount++;
        TryBuyMiner();
        UpdateResources();
        BuildMiner();
    }

    private void UpdateResources()
    {
        Ore += OreMinerCount;
        Clay += ClayMinerCount;
        Obsidian += ObsidianMinerCount;
        Geode += GeodeMinerCount;
    }

    private void TryBuyMiner()
    {
        BuildMiner = () =>
        {
            Log += ToString();
        };
        switch (NextMiner)
        {
            case MinerType.Ore:
                if (Ore >= OreMinerOreCost)
                {
                    BuildMiner = () =>
                    {
                        Ore -= OreMinerOreCost;
                        OreMinerCount++;
                        Log += ToString();
                        AddScenarios();
                    };
                }
                break;
            case MinerType.Clay:
                if (Ore >= ClayMinerOreCost)
                {
                    BuildMiner = () =>
                    {
                        Ore -= ClayMinerOreCost;
                        ClayMinerCount++;
                        Log += ToString();
                        AddScenarios();
                    };
                }
                break;
            case MinerType.Obsidian:
                if (Ore >= ObsidianMinerOreCost && Clay >= ObsidianMinerClayCost)
                {
                    BuildMiner = () =>
                    {
                        Ore -= ObsidianMinerOreCost;
                        Clay -= ObsidianMinerClayCost;
                        ObsidianMinerCount++;
                        Log += ToString();
                        AddScenarios();
                    };
                }
                break;
            case MinerType.Geode:
                if (Ore >= GeodeMinerOreCost && Obsidian >= GeodeMinerObsidianCost)
                {
                    BuildMiner = () =>
                    {
                        Ore -= GeodeMinerOreCost;
                        Obsidian -= GeodeMinerObsidianCost;
                        GeodeMinerCount++;
                        Log += ToString();
                        AddScenarios();
                    };
                }
                break;
        }
    }

    private void AddScenarios()
    {
        if (NextMiner != MinerType.Ore)
        {
            var costs = new List<int?> { OreMinerOreCost, ClayMinerOreCost, ObsidianMinerOreCost, GeodeMinerOreCost };
            int? maxOreCost = costs.Max();
            if (OreMinerCount < maxOreCost)
            {
                AddScenario(MinerType.Ore);
            }
        }

        if (NextMiner != MinerType.Clay && ClayMinerCount < ObsidianMinerClayCost)
            AddScenario(MinerType.Clay);
        if (ClayMinerCount > 0 && NextMiner != MinerType.Obsidian && ObsidianMinerCount < GeodeMinerObsidianCost)
            AddScenario(MinerType.Obsidian);


        if (ObsidianMinerCount > 0 && NextMiner != MinerType.Geode)
            AddScenario(MinerType.Geode);
    }

    private void AddScenario(MinerType minerType)
    {
        Expeditions.Add(new MineralMiningExpedition()
        {
            Log = Log,
            NextMiner = minerType,
            Expeditions = Expeditions,
            CycleCount = CycleCount,
            Ore = Ore,
            Clay = Clay,
            Obsidian = Obsidian,
            Geode = Geode,
            OreMinerCount = OreMinerCount,
            ClayMinerCount = ClayMinerCount,
            ObsidianMinerCount = ObsidianMinerCount,
            GeodeMinerCount = GeodeMinerCount,
            OreMinerOreCost = OreMinerOreCost,
            ClayMinerOreCost = ClayMinerOreCost,
            ObsidianMinerOreCost = ObsidianMinerOreCost,
            ObsidianMinerClayCost = ObsidianMinerClayCost,
            GeodeMinerOreCost = GeodeMinerOreCost,
            GeodeMinerObsidianCost = GeodeMinerObsidianCost
        });
    }
}

