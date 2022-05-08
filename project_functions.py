input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(x, k = []):
    for i in range(len(x)):
        if type(x[i]) is list:
            flatten(x[i])
        else:
            k.append(x[i])
    return k
    
print(flatten(input))

input1 = [[1, 2,3], [3, 4], [5, 6, 7]]

def reverse_list(x):
    
    x.reverse()
    for i in range(len(x)):
        if type(x[i]) is list:
            reverse_list(x[i])
    return x

print(reverse_list(input1))

