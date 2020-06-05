list = [4, 7, 8, 12, 45, 909, 122, 3324, 5466574, 768769, 670, 7089708, 98, 56, 64, 6, 45, 34, 6475754, 845, 745, 6]
n = 845
pos = -1


def search(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


if search(list, n):
    print("Found at {}".format(pos + 1))
else:
    print("Not Found")
