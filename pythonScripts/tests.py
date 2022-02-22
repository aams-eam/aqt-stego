
text = "algo de texto"
l = ['a', 'b', 'c']
print(l)

def modify_something(sometext, somelist):

    del somelist[-1]

    return text[::-1]



fl = modify_something(text, l)

print(l)
