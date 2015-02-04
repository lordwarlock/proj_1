import re
def is_cap(char):
    if (char >= 'A' and char <= 'Z'):
        return 1
    else:
        return 0

def feat_first_cap(data):
    no, word, pos_tag, ne_tag = data
    return is_cap(word[0])

def feat_first_word(data):
    no, word, pos_tag, ne_tag = data
    if (no == '0'): return 1
    else: return 0

def feat_cap_period(data):
    no, word, pos_tag, ne_tag = data
    cap_flag = 0
    per_flag = 0
    for char in word:
        if is_cap(char) : 
            cap_flag = 1
        if (char == '.' or char == ',') :
            per_flag = 1
    return cap_flag*per_flag
def get_feature_functions_list():
    return [up_case,feat_first_cap,feat_first_word,first_name,last_name,\
            org_name,loc_name,misc_name,\
            feat_cap_period,per_name,no_lower_case,\
            brown_cluster]

def csv_extract(file,column=0,func=lambda x:str.upper(x),separator='\s+'):
    result=set()
    with open(file) as f:
        for line in f:
            columns=re.split(separator,line)
            if len(columns) > column:
                result.add(func(columns[column]))
    return result

def ned_extract(file,offset=4,func=lambda x:str.upper(x),separator='\s+'):
    result=set()
    with open(file,'r') as f:
        for line in f:
            name = line[offset:]
            name_eles = re.split(separator,name)
            for name_ele in name_eles:
                result.add(func(name_ele))
    return result

last_name_list=csv_extract('dist.all.last')
first_name_list=csv_extract('dist.male.first').union(csv_extract('dist.female.first'))
per_name_list = last_name_list.union(first_name_list)
org_name_list = ned_extract('ned.list.ORG',1)
loc_name_list = ned_extract('ned.list.LOC',1)
misc_name_list = ned_extract('ned.list.MISC',1)


def per_name(data):
    no, word, pos_tag, ne_tag = data
    return str.upper(word) in per_name_list

def first_name(data):
    no, word, pos_tag, ne_tag = data
    return str.upper(word) in first_name_list

def last_name(data):
    no, word, pos_tag, ne_tag = data
    return str.upper(word) in last_name_list

def org_name(data):
    no, word, pos_tag, ne_tag = data
    return str.upper(word) in org_name_list

def loc_name(data):
    no, word, pos_tag, ne_tag = data
    return str.upper(word) in loc_name_list

def misc_name(data):
    no, word, pos_tag, ne_tag = data
    return str.upper(word) in misc_name_list

def no_lower_case(data):
    no, word, pos_tag, ne_tag = data
    flag = 1
    for char in word:
        if (word <= 'z' and word >= 'a'): flag = 0
    return flag

def up_case(data):
    no, word, pos_tag, ne_tag = data
    return word.upper()

def get_cluster_list(file):
    result = dict()
    with open(file,'r') as f:
        for line in file:
            data = line.split('\t')
            if (len(data)<2): print data
            if(data[1] in result) : print 'Cluster Dup Error\n'
            result[data[1]] = data[0]
    return result

cluster_list = get_cluster_list('cluster_data')
def brown_cluster(data):
    no, word, pos_tag, ne_tag = data
    return cluster_list[word]
