from collections import deque

#FIFO

customer = deque()

def walk_in(para):
    customer.append(para)


walk_in("arbaz")
walk_in("vikesh")
walk_in("noor")
walk_in("adnan")
print(customer)


def serviced():
    a = customer.popleft()
    print(a, " leaves the shop")

(serviced())
(serviced())

print(customer)