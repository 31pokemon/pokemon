import os
from nltk.parse.stanford import StanfordDependencyParser

os.environ['STANFORD_PARSER_PATH']="C:\\Users\\user\\Desktop\\stanford\\stanford-parser-full-2015-12-09"
os.environ['CLASSPATH']="C:\\Users\\user\\Desktop\\stanford\\stanford-parser-full-2015-12-09\\stanford-parser.jar"
os.environ['STANFORD_MODELS']="C:\\Users\\user\\Desktop\\stanford\\stanford-parser-full-2015-12-09\\stanford-parser-3.6.0-models.jar"

eng_parser = StanfordDependencyParser(model_path=u'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
#print(list(eng_parser.parse("the quick brown fox jumps over the lazy dog".split())))

res = list(eng_parser.parse("the quick brown fox jumps over the lazy dog".split()))
for row in res[0].triples():
    print(row)
res[0].tree().draw()