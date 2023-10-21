def my_function(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    if len(args) > 4:
        print(args[4], 'oi')

    print(kwargs['KEY_1'])
    print(kwargs['KEY_2'])


my_function('hello,', True, 1.56, 'hello_1', '213123', KEY_1='Key 1', KEY_2='Key 2')
