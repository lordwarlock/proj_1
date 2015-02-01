def first_cap(data):
    no, word, pos_tag, ne_tag = data
    if (word[0] >= 'A' and word[0] <= 'Z'):
        return 1
    else:
        return 0

def get_feature_functions_list():
    return [first_cap]
