package com.company;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import java.io.File;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by Greyjoy on 4/26/15.
 */
public class UsefulInformationExtractor {
    private String jobPath;

    public ArrayList<String> listFilesForFolder(final File folder) {
        ArrayList<String> fileNames = new ArrayList<String>();
        for (final File fileEntry : folder.listFiles()) {
            if (fileEntry.isDirectory()) {
                listFilesForFolder(fileEntry);
            } else {
                fileNames.add(fileEntry.getName());
            }
        }

        ArrayList<String> filePaths = new ArrayList<String>();
        for (int i = 1; i < fileNames.size(); i++) {
            filePaths.add(jobPath+"/"+fileNames.get(i));
        }
        return filePaths;
    }

    /**
     *     Attention, two consecutive fileds not taken into consideration.
     *     e.g.
     NOTE O
     : O
     you Ix
     might Iy
     suggest O
     to O
     */
    public Map<String, ArrayList<String>> getFields(String pageContent) {
        Map<String, ArrayList<String>> fieldMap = new HashMap<String,ArrayList<String>>();
        String[] contentList = pageContent.split("\n");

        boolean inTheMiddleOfAField = false;
        String fieldName = "";
        String fieldContent = "";

        for (int i = 1; i < contentList.length; i++) {
            String line = contentList[i];
            if (line.trim().isEmpty()){
                continue;
            }
            if (line.split("\t| ").length != 2){
                System.out.println("This line is labeled wrong!");
                System.out.println("This line is: "+line);
            }
            String token = line.split("\t| ")[0];
            String tag = line.split("\t| ")[1];
            //If current tag is not O
            if (tag.equals("O") == false){
                if (inTheMiddleOfAField == false) {
                    inTheMiddleOfAField = true;
                    fieldName = tag;
                    fieldContent = token;
                }
                else {
                    fieldContent = fieldContent + " "+token;
                }
            }

            //Current tag is O
            else {
                if (inTheMiddleOfAField == false) {
                    //Nothing needs to be done.
                }
                else {
                    inTheMiddleOfAField = false;
                    if (fieldMap.containsKey(fieldName)) {
                        ArrayList<String> listOfFields = fieldMap.get(fieldName);
                        listOfFields.add(fieldContent);
                        fieldMap.put(fieldName,listOfFields);
                    }
                    else {
                        ArrayList<String> listOfFields = new ArrayList<String>();
                        listOfFields.add(fieldContent);
                        fieldMap.put(fieldName, listOfFields);
                    }
                    fieldName = "";
                    fieldContent = "";
                }
            }

        }
        return fieldMap;
    }

    public void savePageInformationsToJsonFormat(String filePath) {
        String pageContent = ProcessFile.readStringFromFile(filePath);
        String url = pageContent.split("\n")[0];
        pageContent = pageContent.substring(pageContent.indexOf("\n")+1);

        Map<String, ArrayList<String>> labeledMap = getFields(pageContent);
        Map<String, ArrayList<String>> stanfordFieldMap = new HashMap<String, ArrayList<String>>();

        Stanford7ClassInformationExtractor class7Information = new Stanford7ClassInformationExtractor(url);
        ArrayList<String> sentences = class7Information.getThePageContentBySentences();
        ArrayList<String> sentencesAnnotated =  class7Information.getSentencesAnnotatedWithNER();
        StringBuffer sentencesAnnotatedChunk = new StringBuffer();
        for (String sentence:sentencesAnnotated) {
            sentencesAnnotatedChunk.append(sentence + "\n");
        }
        stanfordFieldMap = getFields(sentencesAnnotatedChunk.toString());

//        for (String key: stanfordFieldMap.keySet()) {
//            System.out.println(key+" is: "+stanfordFieldMap.get(key));
//        }

        String[] filePathList = filePath.split("/");
        String universityName = filePathList[filePathList.length-1];
        saveToJson(universityName,labeledMap,stanfordFieldMap,sentences);
    }

    //Save location is defined here.
    private void saveToJson(String fileName, Map<String, ArrayList<String>> labeledMap,
                            Map<String, ArrayList<String>> stanfordMap, ArrayList<String> sentences) {
        String filePath = "/Users/Greyjoy/Documents/HomeWork"+
                               "/NLP_Project/Data/BeautifulData/"+fileName;

        JSONObject obj = new JSONObject();

        for (String key: labeledMap.keySet()){
            ArrayList<String> answerList = labeledMap.get(key);
            JSONArray answerArr = new JSONArray();
            for (String answer : answerList) {
                answerArr.add(answer);
            }
            obj.put(key,answerArr);
        }

        for (String key: stanfordMap.keySet()){
            ArrayList<String> answerList = stanfordMap.get(key);
            JSONArray answerArr = new JSONArray();
            for (String answer : answerList) {
                answerArr.add(answer);
            }
            obj.put(key,answerArr);
        }

        JSONArray sentenceArr = new JSONArray();
        for (String sentence : sentences) {
            sentenceArr.add(sentence);
        }
        obj.put("Sentences",sentenceArr);

        ProcessFile.writeToFile(obj.toJSONString(), filePath);

    }

    public UsefulInformationExtractor(String jobPath) {
        this.jobPath = jobPath;
        File folder = new File(jobPath);
        ArrayList<String> filePaths = listFilesForFolder(folder);
        for (int i = 0; i < filePaths.size(); i++) {
            System.out.println("Dealing with: " + String.valueOf(i) + "'th university " + filePaths.get(i));
            savePageInformationsToJsonFormat(filePaths.get(i));
        }
//        System.out.println(ProcessFile.readStringFromFile(filePaths.get(0)));

    }
}
