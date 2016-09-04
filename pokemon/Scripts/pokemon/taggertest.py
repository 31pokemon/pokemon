import os
from nltk.tag import StanfordPOSTagger

os.environ['STANFORD_POSTAGGER_PATH']='C:\\Users\\user\\Desktop\\stanford-postagger-full-2015-12-09'
os.environ['CLASSPATH']='C:\\Users\\user\\Desktop\\stanford-postagger-full-2015-12-09\\stanford-postagger.jar'
os.environ['STANFORD_POSTAGGER']=os.environ['CLASSPATH']

eng_tagger=StanfordPOSTagger('C:\\Users\\user\\Desktop\\stanford-postagger-full-2015-12-09\\models\\english-bidirectional-distsim.tagger')
print(eng_tagger.tag('What is the airspeed of an unladen swallow ?' .split()))