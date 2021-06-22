
def multi_bracket_validation(strings):

    arr = []
    obj = { '(':')', '[':']', '{':'}' }

    for x in strings:
        if (x == '(' or x == '{' or x == '['):
            arr.append(x)
        elif x in obj.values():
            if len(arr) == 0:
                return False
            item = arr.pop()
            if x != obj[item]:
                return False

    if len(arr) != 0:
        return False
    
    return True

if __name__ == "__main__":
    print(multi_bracket_validation('(){}'))
    print(multi_bracket_validation('()[[Extra Characters]]'))
    print(multi_bracket_validation('({()}'))
    print(multi_bracket_validation('({()})'))
    print(multi_bracket_validation('({())))'))
    print(multi_bracket_validation('([{()}])'))
    print(multi_bracket_validation('({()})'))