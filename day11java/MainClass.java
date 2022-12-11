package day11java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.function.Function;

public class MainClass {

        public static class Monkey {
                public ArrayList<Long> items;
                public Function<Long, Long> operation;
                public int modulo;
                public int testTrueIdx;
                public int testFalseIdx;
                public int inspection = 0;

                public Monkey(ArrayList<Long> items, Function<Long, Long> operation,
                                int modulo,
                                int testTrueIdx, int testFalseIdx) {
                        this.items = items;
                        this.operation = operation;
                        this.modulo = modulo;
                        this.testTrueIdx = testTrueIdx;
                        this.testFalseIdx = testFalseIdx;
                }
        }

        public static ArrayList<Monkey> GetMonkeys() {
                var monkeys = new ArrayList<Monkey>();
                monkeys.add(new Monkey(
                                new ArrayList<Long>(Arrays.asList(63l, 57l)),
                                f -> f * 11,
                                7,
                                6,
                                2));

                monkeys.add(new Monkey(
                                new ArrayList<Long>(Arrays.asList(82l, 66l, 87l, 78l, 77l, 92l, 83l)),
                                f -> f + 1,
                                11,
                                5,
                                0));

                monkeys.add(new Monkey(
                                new ArrayList<Long>(Arrays.asList(97l, 53l, 53l, 85l, 58l, 54l)),
                                f -> f * 7,
                                13,
                                4,
                                3));

                monkeys.add(new Monkey(
                                new ArrayList<Long>(Arrays.asList(50l)),
                                f -> f + 3,
                                3,
                                1,
                                7));

                monkeys.add(new Monkey(
                                new ArrayList<Long>(Arrays.asList(64l, 69l, 52l, 65l, 73l)),
                                f -> f + 6,
                                17,
                                3,
                                7));

                monkeys.add(new Monkey(
                                new ArrayList<Long>(Arrays.asList(57l, 91l, 65l)),
                                f -> f + 5,
                                2,
                                0,
                                6));

                monkeys.add(new Monkey(
                                new ArrayList<Long>(Arrays.asList(67l, 91l, 84l, 78l, 60l, 69l, 99l, 83l)),
                                f -> f * f,
                                5,
                                2,
                                4));
                monkeys.add(new Monkey(
                                new ArrayList<Long>(Arrays.asList(58l, 78l, 69l, 65l)),
                                f -> f + 7,
                                19,
                                5,
                                1));

                return monkeys;
        }

        public static long CalculateMonkeyBusiness(int roundCount) {
                return CalculateMonkeyBusiness(roundCount, 1);
        }

        public static long CalculateMonkeyBusiness(int roundCount, int stressReducer) {
                var monkeys = GetMonkeys();
                var reductionModulo = 1;
                for (var monkey : monkeys) {
                        reductionModulo *= monkey.modulo;
                }
                for (int i = 0; i < roundCount; i++) {
                        for (var x : monkeys) {
                                for (var y : x.items) {
                                        x.inspection++;
                                        var newValue = x.operation.apply(y);
                                        if (stressReducer != 1) {
                                                newValue = (long) Math.floor((double) newValue / stressReducer);
                                        }

                                        var testResult = newValue % x.modulo == 0;
                                        newValue = newValue % reductionModulo;
                                        if (testResult) {
                                                monkeys.get(x.testTrueIdx).items.add(newValue);
                                        } else {
                                                monkeys.get(x.testFalseIdx).items.add(newValue);
                                        }
                                }

                                x.items.clear();
                        }
                }

                monkeys.sort((o1, o2) -> o2.inspection - o1.inspection);

                return (long) monkeys.get(0).inspection * (long) monkeys.get(1).inspection;
        }

        public static void main(String[] args) {
                System.out.println("Answer 1: " + CalculateMonkeyBusiness(20, 3));
                System.out.println("Answer 2: " + CalculateMonkeyBusiness(10000));
        }
}