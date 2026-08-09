def add(a,b):
    return a + b

def dev(a,b):
    return a - b

# find dup in the list
def chek_dup(a:list ,b:list) -> list:

    g = []

    for i1 in a :
        for i2 in b:
            if i1 == i2:
                g.append(i1)
    print(g) 


a = [1,2,3]
b = [1,3,4]
chek_dup(a,b)
                


