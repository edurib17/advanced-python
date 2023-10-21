
def infinite_sequence():
    result = 1
    while True:
        yield result
        result += 1


values = infinite_sequence()

print(next(values))
