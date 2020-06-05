def person(name, **data):  #Keyword Variable Length Arguments
    print(name)
    print(data)

    for i,j  in data.items():
        print(i,j)


person('Aamer',age = 28,ciity= 'Aurangabad',mobile = 9028030984)