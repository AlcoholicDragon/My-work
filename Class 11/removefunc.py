a=[1,2,3,2,3,4,4,4,5,7,6,9,8]
def Remove(a): 
    final_list = [] 
    for num in a: 
        if num not in final_list: 
            final_list.append(num) 
    print(final_list)
Remove(a)
