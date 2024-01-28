import random
import hashlib

numbers = [1,2,3,4,5,6,7,8,100]

result = [number for number in numbers if number >5 and number <50 ]
print(result)

numbers2 = [10,20,30,40]

result2 = [number for number in numbers2 if number >6 and number <26 ]
print(result2)

spisok = [1998,2000,2001,1995]
result1 = []
for i in spisok:
    if i >1999:
        result1.append(i)
print(result1)

result3 = [ i for i in spisok if i >1999]
print(result3)

names = ['leo','max','kate','mag']

upnames = [o.upper()for o in names]
print(upnames)

m_names = [name for name in names if name[0]=='m']
print(m_names)

result01 = [1 if number >5 else 0 for number in numbers]
print(result01)

result011 = {random.randint(1,100)for i in range(100)}
print(result011)

result012 = {i:i**2 for i in range(1,20)}
print(result012)
hash_object = hashlib.md5(b'hi')
print(hash_object.hexdigest())