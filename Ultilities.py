def make_label(x, sample):
  temp = sample
  if type(temp) is not list:
      temp = temp.tolist()
  return temp.index(x)