def recall(gold,result,note):
    correct_g = 0.0
    total_BI_g = 0.0
    for i in range(len(gold)):
        if (gold[i] != 'O\n'):
            #if (gold[i][0] == 'I' or result[i][0] == 'I'): continue
            total_BI_g += 1
            if (gold[i] == result[i]):
                correct_g += 1
            else:
                #print gold[i][:-1],result[i][:-1]
                pass
    print correct_g
    print total_BI_g
    print mode,correct_g/total_BI_g
    return correct_g/total_BI_g

def accuracy(gold_filename,rslt_filename):
    err_file = open('zzh_test.err','w')
    gold_file = open(gold_filename,'r')
    rslt_file = open(rslt_filename,'r')
    word_file = open('dev.gold','r')
    word = []
    gold = []
    result = []
    for line in word_file:
        if (line == '\n'): continue
        data = line.split('\t')
        word.append(data[1])

    for line in gold_file:
        if (line == '\n'): continue
        data = line.split('\t')
        #word.append(data[1])
        gold.append( data[-1] )
    for line in rslt_file:
        if (line == '\n'): continue
        data = line.split('\t')
        result.append( data[-1] )


    r_score = recall(gold,result,'recall')
    p_score = recall(result,gold,'precision')
    print 'f-score', 2*r_score*p_score/(r_score+p_score)
    correct_g = 0.0
    total_BI_g = 0.0

    for i in range(len(gold)):
        if (gold[i] != 'O\n' and result[i]=='O\n'):
            #if (gold[i][0] == 'I' or result[i][0] == 'I'): continue
            total_BI_g += 1
            if (gold[i] == result[i]):
                correct_g += 1
            else:
                err_file.write( word[i-1]+' '+word[i]+' '+word[i+1]+'\n')
                err_file.write(gold[i][:-1]+' '+result[i][:-1]+'\n')
                pass
    print 'BI-O'
    #print correct_g
    print total_BI_g
    #print correct_g/total_BI_g

    correct_g = 0.0
    total_BI_g = 0.0
    for i in range(len(gold)):
        if (gold[i]=='O\n' and result[i] != 'O\n'):
            #if (gold[i][0] == 'I' or result[i][0] == 'I'): continue
            total_BI_g += 1
            if (gold[i] == result[i]):
                correct_g += 1
            else:
                #print word[i-1],word[i],word[i+1]
                #print gold[i][:-1],result[i][:-1]
                pass
    print 'O-BI'
    #print correct_g
    print total_BI_g
    #print correct_g/total_BI_g
if __name__ == '__main__':
    accuracy('zzh_test.gold','zzh_test.result')
