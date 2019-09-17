# function that takes a string and reverses it

def flipit(string):
    newstring = ""
    for n in string:
        newstring = n + newstring
    return newstring
print(flipit('hello'))

def shout(string):
    return string.upper()
    

# function that takes a string and returns it in all caps
