a = 'a = {0!r}\nb = {1!r}\nprint(a.format(a, b))'
b = 'a = {1!r}\nb = {0!r}\nprint(b.format(b, a))'
print(a.format(a, b))