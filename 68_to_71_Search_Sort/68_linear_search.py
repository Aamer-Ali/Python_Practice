# ===========================================With While loop================================================
arr = [5, 8, 4, 6, 9, 2]
n = 5
pos = -1


def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False


if search(arr, n):
    print("From While loop Found at {}".format(pos + 1))
else:
    print("Not Found")

# ===========================================With For loop================================================

list = [5, 8, 4, 6, 9, 2]
n = 5
pos = -1


def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False


if search(list, n):
    print("From For Loop Found at {} ".format(pos + 1))
else:
    print("Not Found")

# =================================Simplest Method======================================
list = [5, 8, 4, 6, 9, 2]
n = 5

if n in list:
    print("From Simple method Found at {}".format(list.index(n) + 1))
else:
    print("Not Found")
