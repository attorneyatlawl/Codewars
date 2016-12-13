''' The function should return "hello, my love for Johnny,
but just return Hello [name] for anyone else'''

def greet(name):    
    if name == 'Johnny':
        return 'Hello, my love!'
    else:
        return 'Hello, {name}!'.format(name=name)

# creative solution
def greet(name):
    return "Hello, {name}!".format(name = ('my love' if name == 'Johnny' else name));