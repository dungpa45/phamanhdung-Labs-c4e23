
def get_even_list(l):
    new_l=[]
    for i in range(len(l)):
        if l[i]%2==0:
            new_l.append(l[i])
    print(new_l)
    return new_l
    
get_even_list([1, 4, 5, -1, 10])

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
