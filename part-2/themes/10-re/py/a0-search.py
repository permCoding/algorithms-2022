import re


line = "- кооперация;"

reg = re.compile("(О|о)пераци(и|ю|я)")

print(reg.search(line))
