def accuracy(gold_filename,rslt_filename):
    gold_file = open(gold_filename,'r')
    rslt_file = open(rslt_filename,'r')
    gold = []
    result = []
    for line in gold_file:
        data = line.split('\t')
        gold.append( data[-1] )
    for line in rslt_file:
        data = line.split('\t')
        result.append( data[-1] )
    correct_g = 0.0
    total_BI_g = 0.0
    for i in range(len(gold)):
        if (gold[i] != 'O\n' or result[i] != 'O\n'):
            total_BI_g += 1
            if (gold[i] == result[i]):
                correct_g += 1
            else:
                print gold[i],result[i]

    print correct_g
    print total_BI_g
    print correct_g/total_BI_g

if __name__ == '__main__':
    accuracy('zzh_test.gold','zzh_test.result')
