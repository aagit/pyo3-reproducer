#!/usr/bin/env python

import libreproducer

# ClassB doesn't work, unless b.a is first assigned to a local and then dereferenced

b = libreproducer.ClassB()
print('case1 B', b.a.x)
b.a.x = 1
print(b.a.x, b.a.x == 1)

a = libreproducer.ClassA()
print('case2 A', a.x)
a.x = 1
print(a.x, a.x == 1)

b = libreproducer.ClassB()
print('case3 B', b.a.x)
a = b.a
a.x = 1
print(b.a.x, b.a.x == 1)

# it's confusing why the above doesn't work

b = libreproducer.ClassB()
print('case4 B', b.a.x)
a = b.a
a.x = 1
b.a = a
del a
print(b.a.x, b.a.x == 1)
# it's confusing why the above works but the below still doesn't work
b.a.x = 2
print(b.a.x, b.a.x == 2)

# ClassB2 below always works but cannot derive Serialized/Deserialize

b = libreproducer.ClassB2()
print('case1 B2', b.a.x)
b.a.x = 1
print(b.a.x, b.a.x == 1)

b = libreproducer.ClassB2()
print('case3 B2', b.a.x)
a = b.a
a.x = 1
print(b.a.x, b.a.x == 1)

b = libreproducer.ClassB2()
print('case4 B2', b.a.x)
a = b.a
a.x = 1
b.a = a
del a
print(b.a.x, b.a.x == 1)
b.a.x = 2
print(b.a.x, b.a.x == 2)

# it's not clear what's the right way to implement a python object in
# rust that references another python object, ClassB with the
# workaround() below, or ClassB2.

b = libreproducer.ClassB()
print('case4 B workaround', b.a.x)
b.workaround(1)
print(b.a.x, b.a.x == 1)
