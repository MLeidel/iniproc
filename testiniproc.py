# testiniproc.py

import iniproc

a, b, c = iniproc.read("test.ini", 'Size', 'Background', 'Font')

print(a, b, c)


