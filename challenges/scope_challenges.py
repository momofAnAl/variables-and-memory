def challenge_01():
    # 1
    outer_value = 42

    print(f"The value from outside is: {outer_value}")

def challenge_02():
    # 2
    print(f"The value from outside is: {outer_value}")

def challenge_03():
    # 3
    #inner_value = 42 #move the value before the print
    print(f"The value from outside is: {inner_value}")

    inner_value = 42

def challenge_04():
    # 4
    # Python prioritizes local varible before global variable with the same name
    # so in this case it interprets outer_value here to be local outer_value  
    print(f"The value from outside is: {outer_value}")

    outer_value = 42

outer_value = 1729