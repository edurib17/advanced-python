# Definindo um decorator para fazer cache dos resultados das funções
def cache_decorator(function):
    cache = {}  # Dicionário para armazenar os resultados em cache

    def wrapper(*args):
        if args in cache:
            print(f"Retornando resultado em cache para {function.__name__}{args}.")
            return cache[args]
        else:
            result = function(*args)
            cache[args] = result
            print(f"Calculando e armazenando em cache resultado para {function.__name__}{args}.")
            return result

    return wrapper


# Aplicando o decorator a duas funções
@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Chamando as funções decoradas
print(fibonacci(10))  # Os resultados intermediários são armazenados em cache
print(fibonacci(5))  # Estes resultados são recuperados do cache
