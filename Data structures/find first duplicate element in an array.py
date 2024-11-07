import array


def find_duplicate(para):
    num_set = set()
    for i in nums:
        if i in num_set:
            return i
        else:
            num_set.add(i)
    else:
        return -1


nums = array.array("i", [10, 20, 13, 14, 15, 13, 17, 10, 20, 13])

print(find_duplicate(nums))
