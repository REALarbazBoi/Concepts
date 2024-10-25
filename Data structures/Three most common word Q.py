from collections import Counter

import re

a = '''Python is an easy programming language. Python syntax is like an English language. Python language is easy to learn like Java and C. In Python language, the same task can be performed using fewer line of code. Its easy learning and easy to code.
'''
# b = a.split(" ")
# print(b)
# c = Counter(b)
# print(c)
# print(c.most_common(4))

b = re.findall("\w+", a)
count = Counter(b)
print(count)
print(count.most_common(4))