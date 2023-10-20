def myDecorator(function):
    def wrapper():
        print("I am decorating your function!")
        function()

    return wrapper


@myDecorator
def hello_word():
    print("Hello Word")


hello_word()
