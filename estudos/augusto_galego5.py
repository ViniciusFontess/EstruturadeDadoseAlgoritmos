#5- List comprehension

# Normal list
x = []

for i in range(0,100):
    x.append(i)
print(x) 

# List comprehension (mais rápida)

l = [x for x in range (0,100)]
print(l)

