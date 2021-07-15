import math
import csv
import random

with open('voice.csv','r') as file:
    data_table = list(csv.reader(file))

a=.0000000324

told=1
t0=1
for i in range(0,4000):
    sum_told=0
    sum_told0=0
    lsum=1

    for item in data_table[85:1585]:
        sum_told0 = sum_told0+(1/(1+math.exp(t0+(told*(float(item[0]))))))
        sum_told = sum_told+((float(item[0]))*(1/(1+math.exp(-(t0+(told*(float(item[0]))))))))

    for item in data_table[1585:3065]:
        sum_told0 = sum_told0+(1/(1+math.exp(-(t0+(told*(float(item[0])))))))
        sum_told = sum_told - ((float(item[0]))*((1/1+math.exp(-(t0+(told*(float(item[0])))))))

    for item in data_table[85:1585]:
        lsum = lsum * (1/(1+math.exp(-( t0 + ( told * (float(item[0])))))))

    for item in data_table[1585:3085]:
        lsum=lsum*(1-(1/(1+math.exp(-(t0+(told(*float((item[0])))))))))

        if math.log((lsum,math.e)) < -307 :
            break

    tupdated =told + (a*sum_told)
    told=tupdated
    t0updated=(sum_told0*a)+t0
    t0=t0updated
