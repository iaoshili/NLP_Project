package com.company;
import java.io.*;

/**
 * Created by Greyjoy on 4/7/15.
 */
public class ProcessFile {

    public static void writeToFile(String contentToWriteToFile, String filePath) {
        BufferedReader br = null;
        BufferedWriter bw = null;
        try{
            bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filePath), "utf-8"));
            bw.write(contentToWriteToFile.toString());
        }
        catch (FileNotFoundException e) {
            System.out.println(e.toString());
        }
        catch (IOException e) {
            System.out.println(e.toString());
        }

        finally {
            try {
                if (bw != null) {
                    bw.close();
                }
            }
            catch (IOException e) {
                System.out.println(e.toString());
            }
        }
    }

    public static String readStringFromFile(String filePath) {
        BufferedReader br = null;
        StringBuffer fileContent = new StringBuffer();
        try {
            br = new BufferedReader(new FileReader(filePath));
            String line;
            while ((line = br.readLine()) != null) {
                fileContent.append(line.trim() + "\n");
            }
        }
        catch (FileNotFoundException e) {
            System.out.println(e.toString());
        }
        catch (IOException e) {
            System.out.println(e.toString());
        }
        finally {
            try {
                if (br != null){
                    br.close();
                }
            }

            catch (IOException e) {
                System.out.println(e.toString());
            }
        }

        return fileContent.toString();
    }
}
