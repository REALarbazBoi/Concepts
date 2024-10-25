from collections import deque


l = [1, 2, 3, 4, 5]
q = deque(l)
print(q)
q.append(6)
print(q)
q.appendleft(7)
print(q)
# print(sorted(q))
q.pop()
print(q)
q.popleft()
print(q)
q.extend([10, 20, 30])
print(q)
q.extendleft([100, 200, 300])
print(q)
q.insert(0,1)
print(q)
q.remove(300)
print(q)
