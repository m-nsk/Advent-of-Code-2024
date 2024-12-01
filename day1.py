from collections import defaultdict

# PART ONE
input = open("./input1.txt", "r")

l1, l2 = [], []

for line in input:
    nums = line.split()
    l1.append(int(nums[0]))
    l2.append(int(nums[1]))

l1.sort()
l2.sort()

total = 0

while len(l1) > 0:
    total += abs(l1.pop(0) - l2.pop(0))

print(f"Part one: {total}")


# PART TWO
input = open("./input1.txt", "r")

l1, l2 = [], []

for line in input:
    nums = line.split()
    l1.append(int(nums[0]))
    l2.append(int(nums[1]))

# l2_count = defaultdict(int)
# for num in l2:
#     l2_count[num] += 1

total = 0

for num in l1:
    total += num * l2.count(num)

print(f"Part two: {total}")
