nums = [11,16,18,21,22]
for num in nums:
    if num%5 == 0:
        print(num) #Just show first number and break the loop
        break;
    else:
        print('Not Found') #Print not found till loop ends


nums1 = [11,16,18,21,22]
for num in nums1:
    if num%5 == 0:
        print(num) #Just show first number and break the loop
        break;
else:
    print('For Else ---- Not Found') #Print only ones