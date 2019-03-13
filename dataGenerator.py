#Generate the clustered mock data
#put columns of x,y mock data into txt format

import random

datalength = 100
x,y = [],[]

random.seed(random.random())

for i in range(0,datalength):
    x.append(random.random() * 100)
    y.append(random.random() * 100)

f = open('mockdata.txt','w')
for i in range(0,len(x)):
    f.write(str(x[i]) + '        ' + str(y[i]) + '\n')
f.close()
