package com.company;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;


/**
 * Created by Greyjoy on 4/7/15.
 */
public class PreprocessURLs {
    private String urlFilePath;
    private String writeToDirectoryPath;

    public PreprocessURLs(String urlFilePath, String writeToDirectoryPath) {
        this.urlFilePath = urlFilePath;
        this.writeToDirectoryPath = writeToDirectoryPath;
    }

    public void generateTokensFromFile() {
        String filePath = urlFilePath;
        String collegeAndItsUrlString = ProcessFile.readStringFromFile(filePath);
        String[] collegeAndItsUrlList = collegeAndItsUrlString.split("\n");
        for (int i = 23; i < collegeAndItsUrlList.length; i++) {
            String collegeAndItsUrl = collegeAndItsUrlList[i];
            String[] currentCollegeAndItsUrlInList = collegeAndItsUrl.split(" |\t");
            int currentLineLength = currentCollegeAndItsUrlInList.length;
            String collegeName = ListToString(currentCollegeAndItsUrlInList,0,currentLineLength-1);
            String url = currentCollegeAndItsUrlInList[currentLineLength-1];

            if (url.contains("pdf")) {
                System.out.println(url+" temporarily not supported");
                continue;
            }
            System.out.println("Feching "+url);

            generateTokens(url, collegeName);
        }
    }

    //以后要处理这个方法的异常
    private static String ListToString(String[] strList, int startIndex, int endIndex) {
        StringBuffer result = new StringBuffer();
        for (int i = startIndex; i < endIndex; i++) {
            result.append(strList[i]+" ");
        }
        return result.toString();
    }

    public void generateTokens(String url, String collgeName) {
        URL almaMater = null;
        ArrayList<String> tokenList = null;

        try {
            almaMater = new URL(url);  // I went to Cinnaminson High School in New Jersey :)

        }
        catch (MalformedURLException e) {
            System.out.println(e.toString());
        }

        StringBuffer finalTextToBeLabeled = new StringBuffer();

        String text = extractTextFromUrl(url);

        String tempFilePath = "/Users/Greyjoy/Desktop/temp";
        ProcessFile.writeToFile(text,tempFilePath);
        try {
             tokenList = StanfordTokenizer.getTokensByToken(tempFilePath);
        }
        catch (IOException e) {
            System.out.println(e.toString());
        }

        for (String token : tokenList) {
            finalTextToBeLabeled.append(token+ " O" + "\n");
        }

        String filePath = writeToDirectoryPath+"/"+collgeName;
        ProcessFile.writeToFile(finalTextToBeLabeled.toString(),filePath);
    }

    public static String extractTextFromUrl(String url){
        Document doc = null;
        String text = null;

        try {
            doc = Jsoup.connect(url).userAgent("Mozilla").get();
            text = doc.text();
        }
        catch (IOException e){
            System.out.println(e.toString());
        }
        catch (Exception e) {
            System.out.println(e.toString());
        }
        return text;
    }

}

