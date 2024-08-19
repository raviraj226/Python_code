#normal practice
name = "Raviraj Verma"
age = 33
print("My name is:",name)
print("My age is:", age)

#type of variables
print(type(name))
print(type(age))
old = False
a = None
print(type(old))
print(type(a))

#Arithmetic operators.
a = 10
b = 5
add = a+b
subs = a-b
multi = a*b                      # (a) & (b) are operants.
devide = a/b                     # (+)(-)(*)(/) are operators.
mod = a%b                        # modulor operator(%)remainder.
rem = a**b                       # power operator (**) to the power (a^B).
print("Addition of a&b:",add)
print("substrction of a&b:",subs)
print("multiplication of a&b:",multi)
print("Division of a&b:",devide)
print("modulor of a&b:",mod)
print("remainder b/w a&b:",rem)

#Relational operators.
a = 10
b = 20
print(a==b)         #False
print(a!=b)         #True
print(a>=b)         #False
print(a>b)          #False
print(a<=b)         #True
print(a<b)          #True

#Assignment Operators

num = 10
#num = num+10       #20
#num += 10          #20
#num -= 10          #0
#num /= 10          #1.0
#num *= 10          #100
#num %= 10          #0
num **= 3           #1000
print("num:",num)

#Loogical Operators (works on boolean values only)
print(not True)
print(not False)

val1 = True
val2 = False
print("AND operator:", val1 and val2)
print("OR operator:", val1 or val2)