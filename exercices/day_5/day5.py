lst = list()
lst2 = [1,2,3,4,5]
print('Length: ', len(lst2))
print('First: ', lst2[0])
print('Middle: ', lst2[2])
print('Last: ',lst2[len(lst2)-1])
mixedDataTypes = ['Miguel',23,180,'Single','Teste']
itCompanies = ['Facebook','Google','Microsoft','Apple',
    'IBM','Oracle','Amazon']
print('It companies: ',itCompanies)
print('First: ', itCompanies[0])
print('Middle: ', itCompanies[int(len(itCompanies)/2)])
print('Last: ',itCompanies[len(itCompanies)-1])
itCompanies[0] = 'Switch'
print('It companies ',itCompanies)
itCompanies.append('Facebook')
print('It companies ',itCompanies)
middleList = int(len(itCompanies)/2)
itCompanies.insert(middleList,'Tlantic')
print('It companies ',itCompanies)
itCompanies[0] = 'switch'.upper()
print('It companies ',itCompanies)
print('#; '.join(itCompanies))
print('Does SWITCH exist in it companies: ','SWITCH' in itCompanies)
print('Companies1 : ',itCompanies[3:])
print('Companies2 :',itCompanies[:-3])
itCompanies.pop(0)
print('It companies ',itCompanies)
itCompanies.pop(int(len(itCompanies)/2))
print('It companies ',itCompanies)
itCompanies.pop()
print('It companies ',itCompanies)
itCompanies.clear()
print('It companies ',itCompanies)
del itCompanies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joiningList = front_end + back_end
print('Joined List: ',joiningList)
fullstack = joiningList.copy()
reduxIndex = fullstack.index('Redux')
fullstack.insert(reduxIndex, 'Python')
fullstack.insert(reduxIndex, 'SQL')
print('FullStack: ',fullstack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print('Ages ',ages)
agesMidle = int(len(ages)/2)
medianAge = ages[agesMidle:agesMidle+1]
print(medianAge)
average = sum(ages)/len(ages)
print('Average: ',average)
minRange = min(ages)
maxRange = max(ages)
print('Min age: ',minRange)
print('Min age: ',maxRange)
print('Min age minus average: %.2f' %abs(minRange-average))
print('Max age minus average is %.2f ' %abs(maxRange-average))
