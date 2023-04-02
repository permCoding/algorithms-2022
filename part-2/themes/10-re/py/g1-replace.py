import re

def ex_a():
    s = '2023-02-12'
    print(s.replace('-', '.', 1))  # .replace('-', '.'[, limit])
    print(re.sub(r"-", '.', s, 1))

    s = '2023 -   02  -12'
    s = re.sub(r"\s*-\s*", ".", s)
    print(s)

    s = '-   10 256 999 ₽'
    s = re.sub(r"[^0-9\-]", "", s)
    print(s)
    
    s = '-   10 256 999 ₽'
    s = re.sub(r"\-\s*(?=[0-9])", "", s)
    print(s)

    
    s = '<a href="https://kukuku.com">текст ссылки</a>'
    s = re.sub(r"(<a\s+href[^\>]*>)(?=[^<]*)", "", s)
    s = re.sub(r"(?=[^<]*)(\</a\>)", "", s)
    print(s)
    
    s = '<a href="https://kukuku.com">текст ссылки</a>'
    ptn = r"\<a\s+[^\>]*\>([^<]*)\</a\>"
    tag_a = re.search(ptn, s).group(0)
    text = re.search(ptn, s).group(1)
    print(tag_a) 
    print(text)


    s = """
        <a href="https://kukuku.com">текст ссылки 1</a>
                <a href="https://kukuku.com">текст ссылки 2</a>
                        <a href="https://kukuku.com">текст ссылки 3</a>
    """
    ptn = r"\<a\s+[^\>]*\>([^<]*)\</a\>"
    tags = re.findall(ptn, s)
    for tag in tags: print(tag)


def ex_b():
    s = '      2023 -   02  -12         '
    s = re.sub(r"\s*-\s*", ".", s)
    
    sa = re.sub(r"\s*-\s*", ".", s)
    sb = re.sub(r"^\s*", "", s)
    sc = re.sub(r"\s*$", "", s)
    sd = re.sub(r"(^\s*|\s*$)", "", s)
    
    print(f'|{sa}|{sb}|{sc}|{sd}|')


def ex_c():
    s = """
        Длинная строка с текстом, взятая парсером с           какого-то
        сайта,                           с большим количеством пробелов   
        и         переносов           строк      ...                """
    
    s = s.replace('\n', ' ').replace('  ', ' ')
    # while s.find('  ') > -1: s = s.replace('  ', ' ')    
    
    # s = re.sub(r"\n", " ", s)
    # s = re.sub(r"\s+", " ", s)
    
    # s = re.sub(r"(\n|\s)+", " ", s)

    print(s.strip())


def ex_d():
    ini = r"""
    Initial params for prog:
    velisity: 88
    prop- 234523
      value- 666
      title: reg-exp
    """

    ptn = r"^\s*([a-z]+)\s*[-:]\s*(\w+-*\w+)"
    reg = re.compile(ptn, re.M)
    print(reg.findall(ini))
    print(reg.sub(': ', ini))

    def change(m):
        return f"{m.group(1)}: {m.group(2)}"
        
    print(reg.sub(change, ini))

    print(reg.sub(lambda m: f"{m.group(1)}: {m.group(2)}", ini))

    print(reg.sub(lambda m: f"{m[1]}: {m[2]}", ini))


ex_a()
