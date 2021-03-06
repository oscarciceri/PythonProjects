
#env\Scripts\activate.bat

# **** Hast Table *****

#In Python, the Dictionary data types represent the implementation of hash tables. The Keys in the dictionary satisfy the following requirements:
#The keys of the dictionary are hashable i.e. the are generated by hashing function which generates unique result for each unique value supplied to the hash function.
#The order of data elements in a dictionary is not fixed.

dic = {'llave1':'valor1', 'llave2':'valor1'}

dic['llave3'] = 'valor3'

print(dic)
for i in dic.keys():
	print(i)

for i in dic.values():
	print(i)

for i in dic.items():
	print(i)

print(dic.get('llave1'))


# ****Garbage collector *****




# *** deepcopy vs copy *** 

import copy

l1 = [[1,2,3], [4,5,6], [7,8,9]]

l2 = l1

l2[0][0] = 10

print("l1 = ", l1, "l2 = ", l2)
print("id l1 = ", id(l1), "id l2 = ", id(l2))

l1 = [[1,2,3], [4,5,6], [7,8,9]]

# copy
l1 = [[1,2,3], [4,5,6], [7,8,9]]
l2 = copy.copy(l1)
l2[0] = [-1,-2,-3]

print("l1 = ", l1, "l2 = ", l2)
print("id l1 = ", id(l1), "id l2 = ", id(l2))

l1 = [[1,2,3], [4,5,6], [7,8,9]]
l2 = copy.copy(l1)
l2[0][2] = -3
print("l1 = ", l1, "l2 = ", l2)
print("id l1 = ", id(l1), "id l2 = ", id(l2))
#copy creates a copy of the object but still references each element

l1 = [[1,2,3], [4,5,6], [7,8,9]]
l2= copy.deepcopy(l1)
l2[0][2] = -3
print("l1 = ", l1, "l2 = ", l2)
print("id l1 = ", id(l1), "id l2 = ", id(l2))

# OOP in python

class Clase:
	def testing(seft):
		if seft.score>10:
			return True
		else:
			return False

	def __init__(self, name, score):
		self.name = name
		self.score = score


objeto1 = Clase("name1", 11)

print(objeto1.name)
print(objeto1.score)
print(objeto1.testing())


class Complex:

	def add(self, value):
		self.real += value
		self.img += value

	def __init__(self, real, img):
		self.real = real
		self.img = img

n1 = Complex(10,10)
n2 = Complex(1,1)

n1.add(5)
n2.add(5)

print(n1.real)
print(n2.real)

# Inheritance in Python
# https://www.codigofuente.org/herencia-en-python/
class Vehicle:
	def same_name_method(self):
		print("This method is v")

	def vehicle_method(self):
		print("This method is Vehicle")

	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

class Motorbike(Vehicle):
	def same_name_method(self):
		print("This method is m")

		Vehicle.same_name_method(self)
		super().same_name_method() #elegant

	def motor_method(self):
		print("This method is Motorbike")

class Car(Vehicle):
	def same_name_method(self):
		print("This method is c")

	def car_method(self):
		print("This method is Car")



moto = Motorbike(10,11)
moto.vehicle_method()
moto.motor_method()
moto.same_name_method()

carro = Car(10,11)
carro.vehicle_method()
carro.car_method()
carro.same_name_method()

# multiple Inheritance
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

print(MultiDerived.mro())

# multi-level Inheritance
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass

print(Derived2.mro())


#Example multi-level and multiple Inheritance

class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass

print(M.mro())

#SOLID
# Single responsibility
# Open-closed
# Liskov substitution
# Interface segregation 
# Dependency inversion
#https://twitter.com/ManuelZapata/status/1483642516901613568?t=DsgXQSppCWy5qpvthc97Wg&s=08
#https://es.wikipedia.org/wiki/SOLID


#Pthon Exception Handling:
n1 = 10
n2 = 0

try:
	print(n1/n2)
except:
	print("Error")

# Iterators in Python 
# For an object to be iterator need: iter and next
number = [12,25,33,43]
value = number.__iter__()

nextvalue = value.__next__()
print(nextvalue)

nextvalue = value.__next__()
print(nextvalue)

nextvalue = value.__next__()
print(nextvalue)

#Other way
number = [12,25,33,43]
value_elegant = iter(number)

nextvalue_elegant = next(value_elegant)
print(nextvalue_elegant)

nextvalue_elegant = next(value_elegant)
print(nextvalue_elegant)

nextvalue_elegant = next(value_elegant)
print(nextvalue_elegant)


#Generator
def even_generator():
	n=0
	yield n

	n+=2
	yield n

	n+=2
	yield n


	n+=2
	yield n


number = even_generator()
print(next(number))
print(next(number))
print(next(number))
print(next(number))

def even_generatorx(max):
	n=0


	while(n<=max):
		yield n
		n+=2



numberx = even_generatorx(4)
print(next(numberx))
print(next(numberx))
print('end')


def generate_fibonacci():
	n1 = 0
	n2 = 1

	while True:
		yield n1
		n2, n1 = n1, n1+ n2
		

seq = generate_fibonacci()
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))

#Decorators
# is a functions that takes another function add some
# functionallity to it and then return it
print("\n*** Decorators ***")
def inc(x):
	return x + 1


def operate(func, x):
	result = func(x)
	return result

value = operate(inc, 10)
print(value)


def print_msg(message):
	x = "Hello"

	def other_message():
		print(x , message)

	other_message()

print_msg("Python is awesome")



def print_msgx(message):
	x = "Hello"

	def other_messagex():
		print(x , message)

	return other_messagex

funcion = print_msgx("Python is awesome")
funcion()


def printer():
	print("Hello world")

def display_func(func):

	def inner():
		print("Executing", func.__name__)
		func()
		print("End")

	return inner

decorator = display_func(printer)
decorator()


#Elegant way
def display_funcx(func):

	def inner():
		print("Executing", func.__name__)
		func()
		print("End")

	return inner

@display_funcx
def printerx():
	print("Hello world")


printerx()


# Python lambda (anonymous) Functions
# Are single line fuction, defined without a name
print("\n Python lambda Functions")
def multiple(x):
	x = x*2
	return x
y = multiple(10)
print(y)


z = lambda n : n*2
print(z(2))

names = ["sdc", "dsaf", "aad", "safaf", "asdc", "dsaf",]

names.sort(key = lambda x: len(x))

print(names)