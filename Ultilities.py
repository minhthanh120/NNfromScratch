def make_label(x, sample):
    
    if type(sample) is not list:
        temp = sample.tolist()
    temp = sample
    return temp.index(x)