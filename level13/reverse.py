s = "boe]!ai0FB@.:|L6l@A?>qJ}I"
key = "0123456"

result = ""

for i, c in enumerate(s):
    k = ord(key[i % 6])
    if i % 2 == 0:
        for _ in range(k):
            c = chr(ord(c) - 1)
            if ord(c) == 31:
                c = "~"
    else:
        for _ in range(k):
            c = chr(ord(c) + 1)
            if ord(c) == 127:
                c = " "
    result += c

print(result)
