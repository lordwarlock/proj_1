import re
import nltk
from feature_functions import get_feature_functions_list
class FeatureExtraction(object):
    def __init__(self):
        self.data = []
        self.feat = []
    def read_origin_train(self,filename):
        with open(filename,'r') as indata:
            for line in indata:
                self.separate_store_train(line)

    def separate_store_train(self,line):
        if (line != '\n') :
            match = re.match('(.*)\t(.*)\t(.*)\t(.*)\n',line)
            if (match != None):
                self.data.append(match.groups())

    def feature_extraction(self):
        if ( self.data == [] ): return
        else:
            feat_func_list = get_feature_functions_list()
            for line in self.data:
                self.feat.append(  list(line[:-1])\
                                 + [func(line) for func in feat_func_list]
                                 + [line[-1]])
if __name__ == '__main__':
    fe = FeatureExtraction()
    fe.read_origin_train('dev.gold')
    fe.feature_extraction()
    print fe.feat
