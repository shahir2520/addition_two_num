lis = [1,2,3,4,5,6]
print([i*i for i in lis])

print({i: i*i for i in lis})

print({i.upper(): i*3 for i in 'python'})