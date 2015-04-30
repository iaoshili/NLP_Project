package com.company;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Greyjoy on 4/20/15.
 * Just use stanford tokenizer to get sentences and annotated sentences.
 */
public class Stanford7ClassInformationExtractor {
//    class AdmissionInformation{
//        String deadLine;
//
//        @Override
//        public String toString(){
//            return ("Deadline is: "+deadLine+"\n"
//            );
//        }
//    }

    private String universityLink;
    private ArrayList<String> sentences = new ArrayList<String>();
    private ArrayList<String> sentencesAnnotatedWithNER = new ArrayList<String>();

    private ArrayList<String> potentialDeadlines = new ArrayList<String>();
    private String deadLine;

    public Stanford7ClassInformationExtractor(String link) {
        this.universityLink = link;
    }

    public ArrayList<String> getSentencesAnnotatedWithNER(){

        sentences = getThePageContentBySentences();
        ArrayList<String> sentencesAnnotatedWithNER = new ArrayList<String>();

        try{
            sentencesAnnotatedWithNER = StanfordNER.getNER(sentences);
        }
        catch (Exception e) {
            System.out.println(e.toString());
        }

        return sentencesAnnotatedWithNER;
    }

    public  ArrayList<String> getThePageContentBySentences(){
        String admissionPageContent = PreprocessURLs.extractTextFromUrl(universityLink);
        String tempFilePath = "/Users/Greyjoy/Desktop/temp";
        ProcessFile.writeToFile(admissionPageContent,tempFilePath);
        ArrayList<String> sentences = new ArrayList<String>();
        try {
            sentences = StanfordTokenizer.getTokensBySentence(tempFilePath);
        }
        catch (Exception e){
            System.out.println(e.toString());
        }
        return sentences;
    }


}
