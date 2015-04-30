package com.company;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.sun.xml.internal.fastinfoset.util.StringArray;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.HasWord;
import edu.stanford.nlp.process.CoreLabelTokenFactory;
import edu.stanford.nlp.process.DocumentPreprocessor;
import edu.stanford.nlp.process.PTBTokenizer;

public class StanfordTokenizer {

    public static ArrayList<String> getTokensByToken(String filePath) throws IOException {
        ArrayList<String> tokens = new ArrayList<String>();
        PTBTokenizer ptbt = new PTBTokenizer(new FileReader(filePath),
                new CoreLabelTokenFactory(), "");
        for (CoreLabel label; ptbt.hasNext(); ) {
            label = (CoreLabel) ptbt.next(); //(CoreLabel) Added by me
            tokens.add(label.toString());
        }
        return tokens;
    }

    //Notice that each sentence is a list of string.
    public static ArrayList<String> getTokensBySentence(String filePath) {
        ArrayList<String> sentences = new ArrayList<String>();
        DocumentPreprocessor dp = new DocumentPreprocessor(filePath);
        for (List sentence : dp) {
            StringBuffer sentenceStr = new StringBuffer();
            for (int i = 0; i < sentence.size(); i++) {
                sentenceStr.append(sentence.get(i)+" ");
            }
            sentences.add(sentenceStr.toString());
        }
        return sentences;
    }
}
