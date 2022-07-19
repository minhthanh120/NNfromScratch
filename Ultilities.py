def make_label(x, label):
  temp = label
  if type(temp) is not list:
      temp = temp.tolist()
  return temp.index(x)

def make_binarylabel(x,label):
  if x == label:
    return 0
  return 1