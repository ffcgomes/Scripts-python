import datetime

def months(d1, d2):
    return d1.month - d2.month + 12*(d1.year - d2.year)+1


d1 = datetime.datetime(2022, 1, 1)  
d2 = datetime.datetime(2000, 1, 1) 

print(months(d1, d2))