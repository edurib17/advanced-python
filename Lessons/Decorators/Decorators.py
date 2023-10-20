def myDecorator(function):
    def wrapper():
        print("I am decorating your function!")
        function()

    return wrapper


def hello_word():
    print("Hello Word")


myDecorator(hello_word)()
