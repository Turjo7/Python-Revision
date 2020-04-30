
import math
from math import fabs
course = "Python's Course for Beginners"
print(course)
course_a = 'Python Course for "Beginners"'
print(course_a)

message = '''
Hi Turjo,
How are you? It's the multi line.
Thank You.

 '''

print(message)


message_a = "Python for Beginners"
print(message_a[0])
print(message_a[1])
print(message_a[2])
print(message_a[-1])
print(message_a[-2])
print(message_a[0:3])
print(message_a[0:])
print(message_a[1:])
print(message_a[:5])
print(message_a[:])
another = message_a[:]
print(another)

t = "Turjo"
print(t[1:-1])

first_name = "Turjo"
last_name = "Ahmed"

msg = f'{first_name} [{last_name}] is a good programmer'
print(msg)
length = "turjo"
print(len(length))
print(length.upper())
print(length)
print(length.lower())
print(length.find('u'))
print(length.replace('o', 'u'))
print('T' in length)
print(length.title())

print(10/3)
print(10//3)
print(10 % 3)
print(10*3)
print(10**3)
x = 10
x = x+3
print(x)
y = 10+3*2**2

print(y)
z=(2+3)*10-3
print(z)

aa=2.9
print(round(aa))
bb=-2.9
print(abs(aa))


print(math.ceil(5.99))
print(math.floor(5.99))
print(math.factorial(5))
print(math.copysign(5,-6))
n=3
k=2
print(fabs(aa))
#print(math.comb(n,k)) # combs work in Python Version 3.8

print(math.fmod(10,3))
print(math.frexp(10))
print(math.fsum([1,2,3,4,5]))
print(math.gcd(10,5))
print(math.isnan(50))
print(math.sqrt(16))
print(math.ldexp(16,4))
print(math.exp(2))
print(math.log(2))
print(math.pow(2,3))
print(math.sin(0))
print(math.degrees(30))
print(math.radians(30))
print("-------------------------")

print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)
