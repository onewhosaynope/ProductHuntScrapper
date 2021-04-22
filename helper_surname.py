def check(familyname):
    suffixes = ['ov', 'ova', 'aya', 'ev', 'eva', 
    'in', 'ina', 'sky', 'skaya', 'ykh', 'qızı',
    'yan', 'ian',
    'vych', 'chuk', 'enko', 'ko', 'ka', 'shyn', 'uk'] 
    return familyname.endswith(tuple(suffixes))


def check_custom(familyname, suffix): 
    return familyname.endswith(suffix)