import re
import nltk
from feature_functions import get_local_feature_functions,get_global_feature_functions,gf_zone

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
        else:
            self.data.append(None)

    def feature_extraction(self):
        if ( self.data == [] ): return
        else:
            local_ffunc_list = get_local_feature_functions()
            global_ffunc_list = get_global_feature_functions()
            global_features=[]
            f_zone,d_range=gf_zone(self.data)
            global_features.append(f_zone)
            for func in global_ffunc_list:
                gf_list=func(self.data,d_range)
                if len(gf_list) != len(self.data):
                    print "Error result of" + str(func) + "returned inconsistent values"
                global_features.append(gf_list)
            for index,line in enumerate(self.data):
                if line==None:
                    self.feat.append(None)
                else:
                    self.feat.append(  [line[0],line[1],line[2]] \
                                     + [str(func(line)) for func in local_ffunc_list] \
                                     + [str(global_feature[index]) for global_feature in global_features] \
                                     + ([] if self.raw_flag else [line[-1]]))


    def output_feat(self,filename):
        with open(filename,'w') as output_file:
            for line in self.feat:
                if line==None:
                    output_file.write('\n')
                else:
                    output_file.write('\t'.join(line) + '\n')
     
if __name__ == '__main__':
    fe = FeatureExtraction()
    fe.read_origin_train('train.gold')
    fe.feature_extraction()
    fe.output_feat('zzh_train.gold')
    """fe1 = FeatureExtraction()
    fe1.read_origin_train('dev.gold')
    fe1.feature_extraction()
    fe1.output_feat('zzh_test.gold')
    fe2 = FeatureExtraction(1)
    fe2.read_origin_train('dev.raw')
    fe2.feature_extraction()
    fe2.output_feat('zzh_test.raw')"""
    fe1 = FeatureExtraction()
    fe1.read_origin_train('./project1-test/test.gold')
    fe1.feature_extraction()
    fe1.output_feat('zzh_test.gold')
    fe2 = FeatureExtraction(1)
    fe2.read_origin_train('./project1-test/test.raw')
    fe2.feature_extraction()
    fe2.output_feat('zzh_test.raw')
