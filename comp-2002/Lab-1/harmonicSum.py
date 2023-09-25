
def harmonicSum (input):
    if input == 1:
        return 1
    elif input == 0:
        return 0
    
    return 1 / input - 1 + harmonicSum(input - 1)