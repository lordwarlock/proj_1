import re
class FeatureExtraction(object):
    def __init__(self):
        self.data = []
    def read_origin_train(self,filename):
        with open(filename,'r') as indata:
            for line in indata:
                self.separate_store_train(line)

    def separate_store_train(self,line):
        if (line != '\n') :
            match = re.match('(.*)\t(.*)\t(.*)\t(.*)\n',line)
            if (match != None):
                self.data.append(match.groups())

if __name__ == '__main__':
    fe = FeatureExtraction()
    fe.read_origin_train('dev.gold')
    print fe.data
