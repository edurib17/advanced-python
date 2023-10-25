def myfunction(myparameter: int) -> str:
    return f"{myparameter + 10}"


def otherfunction(otherparameter: str):
    print(otherparameter)


print(myfunction(10))

otherfunction(myfunction(20))
