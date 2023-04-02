import re


lines = [
    "tast",
    "teost",
    "test",
    "tost",
    "toster",
    "testing",
    "cotest",
    "Test",
    "TOST",
    "TOST ",
    "traktat"
];

for i in range(len(lines)):
    line = lines[i]
    
    ptn_a = r"t[e|o]st"
    ptn_b = r"^t.*t$"
    ptn_c = r"\s*t.*t\s*"
    ptn_d = "\\s*t.*t\\s*"  # без r все слеши нужно экранировать
    ptn_e = r"\bt[^t]*t\b"
    ptn_f = r"\w*"
    ptn_g = r"^[a-z]+$"
    
    r = re.compile(ptn_g, re.I);

    if r.search(line):  # Match | None
        print(i, line.rjust(12, ' '))
