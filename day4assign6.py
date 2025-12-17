a=[105,110,108,112,115,116,114]


for i in range(len(a)-2):
    b=a[i:i+3]
    avg_set=[]
avg=sum(a)/3
avg_set.append(avg)
print(avg_set)
print("average of 3 days of stock is ",a[0:3])
