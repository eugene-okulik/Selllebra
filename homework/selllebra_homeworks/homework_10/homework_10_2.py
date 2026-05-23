def repeat(times=1):
    def decorator(func):
        def wrapper():
            for i in range(times):
                result = func()
            return result
        return wrapper
    return decorator


@repeat(5)
def day():
    print('What a wonderful day!')


day()
