# f = open('MyData', mode='r')
# f1 = open('CopyMyData',mode='w')
#
# for i in f:
#     f1.write(i)

f = open('img1.png', mode='rb')
f1 = open('img2.png',mode='wb')

for i in f:
   f1.write(i)