import sys


params = sys.argv

for prm in params[1:]:
    print(prm.split('='))


"""
python test-02.py cat=smart count=5 direct=desc

"""