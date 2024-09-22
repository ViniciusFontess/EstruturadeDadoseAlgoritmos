

# 8- shallow VS deep copy

a = [1,2,3]
b = a
#b is a (TRUE)
b.append(4)
print(b)
print(a)

import copy

b = copy.copy(a)
print(a)
print(b)
b.append(5)
print(b)
print(a)
#b is a (FALSE)
