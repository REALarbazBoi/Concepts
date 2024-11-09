import heapq


def heapsort(a):
    n = []
    for i in range(len(a)):
        heapq.heapify(a)
        k = heapq.heappop(a)
        n.append(k)
    return n #sorted list

a = [10, 15, 2, 20, 68, 1, 99]
print(heapsort(a))