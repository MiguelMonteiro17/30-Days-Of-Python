# Day2: 30 Days of python programming
firstName = 'Miguel'
lastName= 'Monteiro'
fullName = 'Miguel Ângelo Botelho Monteiro'
country = 'Portugal'
city = 'Porto'
age = 23
year = 2020
isMarried = False
isTrue = True
isLightOn= False
day, month, year, sign = 17, 8 ,1996, 'Lion'

print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(isMarried))
print(type(isTrue))
print(type(isLightOn))
print(type(day))
print(type(month))
print(type(year))
print(type(sign))

print('First name length is',len(firstName), ' and last name length is', len(lastName))

numOne, numTwo = 5,4
total = numOne+numTwo
diff = numOne-numTwo
product = numOne*numTwo
division = numOne/numTwo
remainder = numOne% numTwo
exp= numOne**numTwo
floorDivision = numOne//numTwo

radius = 30
pi = 3.14
areaOfCircle = pi*radius**2
print('Area of circle is: ',areaOfCircle)
circumOfCircle=2*pi*radius
print('Circum of circle is: ',circumOfCircle)
radius = int(input('What is the radius of the circle: '))
areaOfCircle = pi*radius**2
print('Area of circle is: ',areaOfCircle)
firstName = input('First Namme: ')
print(firstName)
firstName = input('Last Namme: ')
print(firstName)