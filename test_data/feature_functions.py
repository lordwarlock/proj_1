import re

def first_cap(data):
    no, word, pos_tag, ne_tag = data
    if (word[0] >= 'A' and word[0] <= 'Z'):
        return 1
    else:
        return 0

def first_word(data):
    no, word, pos_tag, ne_tag = data
    return int(no) == 0

def get_feature_functions_list():
    return [first_cap,first_word,first_name,last_name]

def csv_extract(file,column=0,func=lambda x:str.upper(x),separator='\s+'):
    result=set()
    with open(file) as f:
        for line in f:
            columns=re.split(separator,line)
            if len(columns) > column:
                result.add(func(columns[column]))
    return result


last_name_list=csv_extract('dist.all.last')
first_name_list=csv_extract('dist.male.first').union(csv_extract('dist.female.first'))

def first_name(data):
    no, word, pos_tag, ne_tag = data
    return str.upper(word) in first_name_list

def last_name(data):
    no, word, pos_tag, ne_tag = data
    return str.upper(word) in last_name_list
