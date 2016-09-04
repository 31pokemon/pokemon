import os
from nltk.tag import StanfordNERTagger

os.environ['STANFORD_NER_PATH'] = 'C:\\Users\\user\\Desktop\\stanford\\stanford-ner-2015-12-09'
os.environ['STANFORD POSTAGGER PATH']="C:\\Users\\user\\Desktop\\stanford\\stanford-postagger-full-2014-08-27"
os.environ['CLASSPATH']="C:\\Users\\user\\Desktop\\stanford\\stanford-ner-2015-12-09\\stanford-ner.jar;C:\\Users\\user\\Desktop\\stanford\\stanford-postagger-full-2014-08-27\\stanford-postagger.jar"

eng_tagger = StanfordNERTagger('C:\\Users\\user\\Desktop\\stanford\\stanford-ner-2015-12-09\\classifiers\\english.conll.4class.distsim.crf.ser.gz')
print(eng_tagger.tag('Rami Eid is studying at Stony Brook University in NY'.split()))