import json


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

user = json.loads(objs)
# print(user)
print(user["address"])
print(user["address"]["city"])
s = json.dumps(user["address"], indent=4, ensure_ascii=False)
print(s)
