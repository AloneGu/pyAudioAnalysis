import numpy as np

data = [1,2,3,4,5]

print np.var(data)
print np.mean(data)
print max(data)
print min(data)

content = open('log_data.txt').readlines()
data = []
for row in content:
    row = row.strip()
    index=row.rfind(':')
    sn=row[index+1:]
    data.append(float(sn))

print np.var(data)
print np.mean(data)
print max(data)
print min(data)



