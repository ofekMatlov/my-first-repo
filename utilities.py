def digitisok(param):
    if param.isdigit():
        return True
    else:
        print("Error: " + param + " is not a number ")
        return  False