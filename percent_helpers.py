def msg_percent(d):
  """
  d = {'pablo': 236, 'Ezequiel': 120, 'andy': 78}
  
  rule of three: float((236 * 100) / (236 + 120 +78)
  """
  total_msg = 0
  for x in d:
    total_msg += d[x]
  
  result = {}
  for x in d:
    percent = float((d[x] * 100) / total_msg)
    result[x] = round(percent, 2)

  return result


def sort_dict(d):
  pass 


def axis_percent():
  pass


#print(str(sort_dict({'Ezequiel': 120, 'pablo': 236, 'andy': 78})))
