# Standford Named Entity Recognizer 
https://nlp.stanford.edu/software/CRF-NER.shtml  
input
```
University of California is located in California, United States. 
Hangzhou is a great place to go.
```
output
```
{'LOCATION': ['California', 'United States', 'Hangzhou'], 'ORGANIZATION': ['University of California']}
```

setp1  
Executing the fellow code under .\stanford-ner-2018-10-16 by cmd
```
java -mx1000m -cp stanford-ner.jar edu.stanford.nlp.ie.NERServer -loadClassifier classifiers/english.muc.7class.distsim.crf.ser.gz -port 8080 -outputFormat inlineXML
```
setp2  
Run the NER.py
