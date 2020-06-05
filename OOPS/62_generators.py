# def topten():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     yield 6
#     yield 7
#     yield 8
#
#
# value = topten()
# # print(value.__next__())
#
# for i in value:
#     print(i)


# Top ten perfect squre

def topten():
    n = 1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1


value = topten()

for i in value:
    print(i)
