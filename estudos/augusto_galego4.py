# 4- Diff between = and is

x = 4000

x is 4000

print(id(4000))
print(id(x))
# São objetos diferentes na memória

x = None
print(id(None))
print(id(x))

