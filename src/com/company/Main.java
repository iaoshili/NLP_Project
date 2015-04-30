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

public class Main {

    public static void main(String[] args) throws IOException {
        /**
         *     	Notice that to save time, I manually put this location in the usefulinformationextractor.
         *     	Change this field here has nothing to do with the extracted data's location.
         */
        String filePath = "/Users/Greyjoy/Documents/HomeWork"+
                               "/NLP_Project/Data/BeautifulData/";

    	//Extract useful information. Including sentences, Ideadline... DATE, LOCATION ... in json form to BeautifulData.
        UsefulInformationExtractor usefulInformationExtractor = new UsefulInformationExtractor("/Users/Greyjoy/Documents/HomeWork" +
                "/NLP_Project/Data/1-25WithUrl");

        TrainModel trainModel = new TrainModel(filePath);
        trainModel.train();
    }
}

