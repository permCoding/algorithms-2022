import sys


params = sys.argv

obj = {}
for prm in params[1:]:
    pair = prm.split('=')
    obj[pair[0]] = pair[1]

print(obj)

"""
python test-03.py cat=smart count=5 direct=desc
{'cat': 'smart', 'count': '5', 'direct': 'desc'}
"""