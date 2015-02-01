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
        if (char == '.') :
            per_flag = 1
    return cap_flag*per_flag

def get_feature_functions_list():
    
    return [feat_first_cap,feat_first_word,feat_cap_period]
