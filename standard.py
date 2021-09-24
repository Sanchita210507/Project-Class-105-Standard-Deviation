import csv
import math
with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    fileData=list(reader)
data=fileData[0]

def mean(data):
    n=len(data)
    total=0

    for x in data:
        total+=int(x)
    mean=total/n
    return mean

sqaure=[]

for s in data:
    a=int(s)-mean(data)
    a=a*2
    sqaure.append(a)
sum=0

for num in sqaure:
    sum+=num

result=sum/(len(data)-1)
standard_deviation=math.sqrt(result)
print(f"Standard deviation is: {standard_deviation}")
