x = "Hello World"                                #we can use str("Hello World") instead of this
print(type(x))

y=  20                                           #we can use int(20) instead of this
print(type(y))

z =  20.5                                        #we can use  float(20.5) instead of this
print(type(z))

a =  1j                                          #we can use complex(1j)  instead of this
print(type(a))

b = ["apple", "banana", "cherry"]                #we can use list(("apple", "banana", "cherry")) instead of this 
print(type(b))

c = range(6)                                     
print(type(c))

d = {"name" : "John", "age" : 36}                #we can use dict(name="John", age=36) instead of this
print(type(d))

e = {"apple", "banana", "cherry"}                #we can use set(("apple", "banana", "cherry"))  instead of this
print(type(e))

f = frozenset({"apple", "banana", "cherry"})     #we can use frozenset(("apple", "banana", "cherry")) instead of this
print(type(f))

g = True                                         #we can use bool(5) instead of this
print(type(g))

h = b"Hello"                                     #we can use bytes(5) instead of this
print(type(h))

i = bytearray(5)                                 #we can use bytearray(5) instead of this
print(type(i))

j = memoryview(bytes(5))                         #we can use bytearray(5) instead of this
print(type(j))

k = None  
print(type(k))