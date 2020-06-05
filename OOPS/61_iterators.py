# nums = [1, 2, 3, 4, 5]
#
# mIter = iter(nums)
# print(mIter.__next__())
#
# print(next(mIter))
#
# for i in nums:
#     print(i)



class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration


values = TopTen()
for i in values:
    print(i)
