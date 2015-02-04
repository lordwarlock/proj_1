def preprocess(file,mode):
    output = open('../brown_input.txt',mode)
    with open(file,'r') as f:
        for line in f:
            if(line == '\n'):
                output.write('\n')
                continue
            data = line.split('\t')
            output.write(data[1] + ' ')
    output.close()

if __name__ == '__main__':
    preprocess('train.gold','w')
    preprocess('dev.gold','a')
