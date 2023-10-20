def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            f.write(f"{fname} returned value {value}\n")
            return value

    return wrapper


@logged
def addSum(x, y):
    return x + y


print(addSum(10, 20))
print(addSum(30, 20))
print(addSum(90, 20))
