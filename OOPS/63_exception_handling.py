a = 5
b = 2

try:
    print("Open")
    print(a / b)
    k = int(input("Enter Integer"))
    print(k)
except ZeroDivisionError as e:
    print('Cannot devide by zero')
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print("Something Going wrong")
finally:
    print('Closed')
