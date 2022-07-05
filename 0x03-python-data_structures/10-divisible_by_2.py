#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return(None)
    _ans = []
    for i in my_list:
        if i % 2 == 0:
            _ans.append(True)
        else:
            _ans.append(False)
    return _ans
