# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

fruits = ['banana', 'orange', 'mango', 'lemon'] 
print(fruits[0:4]) # it returns all the fruits
# this is also give the same result as the above
print(fruits[0:]) # if we don't set where to stop it takes all the rest
print(fruits[1:3]) # it does not include the end index
print(fruits[1:])