def my_decorator(func):
    def wrapper(*args):
        print("Call the function")
        result = func(*args)
        print("Bye")
        return result
    return wrapper
@my_decorator
def greet(name):
    print ("Hello have a good day "+name+".")

greet("anon")