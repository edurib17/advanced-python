import sys
def my_generator(n):
    for x in range(n):
        yield x ++ 1


values = my_generator(3)
print(sys.getsizeof(values))


for x in values:
    print(x)