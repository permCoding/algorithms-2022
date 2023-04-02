import re


objs = """
    {
        "id": "59761",
        "isActive": true,
        "age": 35,
        "name": "Кошмар Кошмаров",
        "gender": "male",
        "company": "CEDWARD",
        "email": "koshma@cedward.com",
        "phone": "+8 (890) 543-2508",
        "address": {
            "city": "Кунгур",
            "street": "Ленина",
            "residence": {
                "home": 2,
                "apartment": 21
            }
        }
    }
"""

def a():
    ptn = r"\"(email)\":\s\"([^\"]+)\""
    reg = re.compile(ptn, re.I)
    res = reg.search(objs)
    print(res)
    if res:

        for i in range(res.lastindex+1):
            print(res[i])
        
        for group in res.groups():
            print(group)


def b():
    ptn = r"(?<=\"email\":\s\")([^\"]+)(?=\")"
    reg = re.compile(ptn, re.I)
    res = reg.search(objs)
    print(res)
    if res:
        for i in range(res.lastindex+1):
            print(res[i])


def c():
    ptn = r"(?<=\"email\":\s\")(?P<email>([^\"]+))(?=\")"
    reg = re.compile(ptn, re.I)
    res = reg.search(objs)
    if res:
        dct = res.groupdict()
        print(dct)
        for key in dct:
            print(f"{key}: {dct[key]}")


# a()
# b()
c()
