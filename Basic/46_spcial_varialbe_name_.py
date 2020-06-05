# print(__name__)

# if you are running the file it prints _main_
# if you add this module to another one then it will print the module name
# So you  can check by adding condition that it is the __main__ or added module and perform some operations

if __name__ == "__main__":
    print("This is Main")
