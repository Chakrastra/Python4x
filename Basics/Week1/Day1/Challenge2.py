#You have a list ['10', '20.5', '30']. Write a Python function to convert each element into a float and calculate their sum. 

list=['10', '20.5','30']
sum=0
for i in list:
    sum+=float(i)
print(sum)