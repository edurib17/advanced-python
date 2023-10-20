def myDecorator(function):
    def wrapper(*args, **kwargs):
        print("I am decorating your function!")
        return function(*args, **kwargs)

    return wrapper


@myDecorator
def hello_client(clientName):
    return f"Hello {clientName}!"


print(hello_client("Mike"))
