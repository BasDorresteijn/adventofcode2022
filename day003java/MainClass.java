package day003java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.stream.IntStream;

public class MainClass {

    public static int GetIntValueForChar(char inputChar) {
        if (Character.isLowerCase(inputChar)) {
            return inputChar - 'a' + 1;
        } else {
            return inputChar - 'A' + 1 + 26;
        }
    }

    public static void main(String[] args) {
        var path = MainClass.class.getResource("file.txt");
        var file = new File(path.getFile());
        try (Scanner myReader = new Scanner(file)) {
            var total = 0;

            while (myReader.hasNextLine()) {
                var data = myReader.nextLine();
                if (data == "\n")
                    continue;
                var dataLength = data.length();
                var leftSide = data.substring(0, dataLength / 2);
                var rightSide = data.substring(dataLength / 2, dataLength);
                for (var leftChar : leftSide.toCharArray()) {
                    if (rightSide.indexOf(leftChar) != -1) {
                        total += GetIntValueForChar(leftChar);
                        break;
                    }
                }
            }
            myReader.close();
            System.out.println("answer 1: " + total);

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        try (Scanner myReader = new Scanner(file)) {
            var total = 0;

            while (myReader.hasNextLine()) {
                var sortedBackpackKeys = IntStream.concat(
                        IntStream.concat(
                                myReader.nextLine().chars().distinct(),
                                myReader.nextLine().chars().distinct()),
                        myReader.nextLine().chars().distinct()).sorted().toArray();

                var previousKey = 0;
                var count = 0;
                for (int key : sortedBackpackKeys) {
                    if (key == previousKey) {
                        count++;
                    } else {
                        previousKey = key;
                        count = 1;
                    }

                    if (count == 3) {
                        break;
                    }
                }

                total += GetIntValueForChar((char) previousKey);
            }
            myReader.close();
            System.out.println("answer 2: " + total);

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

    }
}