import re
import nltk
from feature_functions import get_feature_functions_list
class FeatureExtraction(object):
    def __init__(self,raw_flag=0):
        self.data = []
        self.feat = []
        self.raw_flag = raw_flag
        self.feat_length = 4 - raw_flag
    def read_origin_train(self,filename):
        with open(filename,'r') as indata:
            for line in indata:
                self.separate_store_train(line)

    def separate_store_train(self,line):
        if (line != '\n') :
            if self.raw_flag:
                match = re.match('(.*)\t(.*)\t(.*)\n',line)
                if (match != None):
                    self.data.append(match.groups()+tuple(['']))
            else:
                match = re.match('(.*)\t(.*)\t(.*)\t(.*)\n',line)
                if (match != None):
                    self.data.append(match.groups())

    def feature_extraction(self):
        if ( self.data == [] ): return
        else:
            feat_func_list = get_feature_functions_list()
            self.feat_length += len(feat_func_list)
            for line in self.data:
                if self.raw_flag:
                    self.feat.append(  [line[0],line[1],line[2]]\
                                     + [func(line) for func in feat_func_list])
                else:
                    self.feat.append(  [line[0],line[1],line[2]]\
                                     + [func(line) for func in feat_func_list]
                                     + [line[-1]])            

    def output_feat(self,filename):
        with open(filename,'w') as output_file:
            flag = 1
            for line in self.feat:
                i = 0
                for feat in line:
                    i += 1
                    if flag : flag = 0
                    else:
                        if (i == 1 and feat == '0'): output_file.write('\n')
                    output_file.write(str(feat))
                    if (i != self.feat_length):
                        output_file.write('\t')
                    else:
                        output_file.write('\n')
     
if __name__ == '__main__':
    fe = FeatureExtraction()
    fe.read_origin_train('train.gold')
    fe.feature_extraction()
    fe.output_feat('zzh_train.gold')
    fe = FeatureExtraction()
    fe.read_origin_train('dev.gold')
    fe.feature_extraction()
    fe.output_feat('zzh_test.gold')
    fe1 = FeatureExtraction(1)
    fe1.read_origin_train('dev.raw')
    fe1.feature_extraction()
    fe1.output_feat('zzh_test.raw')

