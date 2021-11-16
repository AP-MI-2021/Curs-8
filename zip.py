lst1 = [1, 2, 7, 4,  2, 8, 21]
lst2 = [23,43,12,543,23,435, 33]

zipped = list(zip(lst1, lst2))
print(zipped)

unzipped = list(zip(*zipped))
"""
zip(*unzipped) = zip(zipped[0], zipped[1], ...)
= zip((1, 23), (2, 43), (7, 12), ...)
= (1, 2, 7, ...), (23, 43, 12, ...), ...
"""
print(unzipped[0])
print(unzipped[1])

zip_LC = [(lst1[x], lst2[x]) for x in range(len(lst1))]
print(zip_LC)