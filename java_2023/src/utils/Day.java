package utils;

import java.io.File;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;

public abstract class Day {
    public String readFile(String path) {
        // Specify the file name or path
        String fileName = "input/" + path;
        // Assuming the file is in the same directory as the Java class

        File file = new File(fileName);
        List<String> fileContent = new ArrayList<>();

        try {
            fileContent = Files.readAllLines(file.toPath(), StandardCharsets.UTF_8);

        } catch (Exception e) {
            e.printStackTrace();
        }
        return String.join("\n", fileContent);
    }
}
