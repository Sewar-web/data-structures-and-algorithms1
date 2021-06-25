def multi_bracket_validation(strings):
      
    open = tuple('({[')
    close = tuple(')}]') 
    map = dict(zip(open, close)) 
    # print(map)
    arr_multi = [] 
    for i in strings:
        if i in open:
            arr_multi.append(map[i])
        elif i in close:
            if not arr_multi or i != arr_multi.pop():
                return False
    if not arr_multi:
        return True
    else:
        return False



if __name__ == "__main__":
    print(multi_bracket_validation('(){}'))
    print(multi_bracket_validation('()[[Extra Characters]]'))
    print(multi_bracket_validation('({()}'))
    print(multi_bracket_validation('({()})'))
    print(multi_bracket_validation('({())))'))
    print(multi_bracket_validation('([{()}])'))
    print(multi_bracket_validation('({()})'))
