def linearsearch(l,x):
    i = 0
    for i in l:
        if i == x:
            return"the element is found"
    return "element is not found"
l =[1,2,3,4,5,6]
x = 4
print(linearsearch(l,x))



