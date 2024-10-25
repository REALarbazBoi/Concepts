import heapq


# h =[]
#
# heapq.heappush(h, 20)
# heapq.heappush(h, 30)
# heapq.heappush(h, 40)
# heapq.heappush(h, 10)
# heapq.heappush(h, 50)
# heapq.heappush(h, 60)
# print(h)
# heapq.heappop(h)
# print(h)

# l = [50, 30, 40, 60, 70, 20, 10]
# heapq.heapify(l)
# print(l)
# print(heapq.nlargest(2, l))
# heapq.heapreplace([2,3],l)
# print(l)


lst = [28, 2, 32, 22, 10, 1]

print("Original list - ", lst)

heapq.heapify(lst)

print("Heapified list - ", lst)

print("Calling heapreplace() ----")
pop_item = heapq.heapreplace(lst, 0)

print("The popped item - ", pop_item)
print("List after heapreplace call - ", lst)
