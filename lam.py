hey=lambda  x : x + 20
print(hey(20))
print(hey)

z = lambda a, b: a*b
print(z(5,6))
print(z)

li=[1,2,3,4,5,6,7,8,9]
print(tuple(filter(lambda x:x % 2==0,li)))