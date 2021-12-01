from collections import defaultdict
import pprint as pp

dicts = [
  {'a':1, 'b':2, 'c':3},
  {'a':1, 'd':2, 'c':'foo'},
  {'e':57, 'c':3}
]

super_dict = defaultdict(set)  # uses set to avoid duplicates

for d in dicts:
  for k, v in d.items():  # use d.iteritems() in python 2
    super_dict[k].add(v)

print("The value of 'dicts' is:")

pp.pprint(dicts)

pp.pprint(super_dict)
