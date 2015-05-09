package com.company;

import org.jsoup.Jsoup;
import org.jsoup.helper.Validate;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import javax.lang.model.element.Name;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class Main {

    public static void main(String[] args) throws IOException {
        /**
         *     	Notice that to save time, I manually put this location in the usefulinformationextractor.
         *     	Change this field here has nothing to do with the extracted data's location.
         */
        String filePath = "/Users/Greyjoy/Documents/HomeWork"+
                               "/NLP_Project/Data/AI_News/";
        String savePath = filePath;

    	//Extract useful information. Including sentences, Ideadline... DATE, LOCATION ... in json form to BeautifulData.
//        UsefulInformationExtractor usefulInformationExtractor = new UsefulInformationExtractor("/Users/Greyjoy/Documents/HomeWork" +
//                "/NLP_Project/Data/AllWithUrl");

        Boolean isTrash = true;
        if (isTrash) {
            savePath += "trash";
        }
        else {
            savePath += "useful";
        }
        String url =
"http://www.dailymail.co.uk/sciencetech/article-2812292/Word-TWEET-Shazam-birds-app-lets-identify-birdsong-real-time.html?ITO=1490&ns_mchannel=rss&ns_campaign=1490"
                ;



        Random rand = new Random();

        // nextInt is normally exclusive of the top value,
        // so add 1 to make it inclusive
        int randomNum = rand.nextInt((99999 - 0) + 1) + 0;
        savePath += String.valueOf(randomNum);

        PreprocessURLs.SaveMainContent(url, savePath);

    }
}

