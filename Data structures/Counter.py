from collections import Counter


l = ["Mark", "Jonny", "David", "Mark", "Jonny", "Mark", "James", "Mathew"]
p = {}

# for i in l:
#     if i not in p:
#         p[i] = 1
#     else:
#         p[i] += 1
#
# print(p)
c= Counter(l)
# print(c)
# print(c["Mark"])
# print(c.get("Mark"))
# print(c.keys())
# print(c.values())
# c.update({"Arbaz": 4})
# print(c)
# print(c.elements())
# for i in c.elements():
#     print(i)
# for i in c.items():
#     print(i)
#
# c.pop("Arbaz")
# print(c)
print(c.most_common(1))

# c.update({"Arbaz":4})
print(c.most_common(2))
c.clear()
print(c)