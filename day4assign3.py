def overlapping(list1,list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1=[1,2,3,4,5,6]
list2=[7,8,9]

print(overlapping(list1,list2))