tpl = tuple()
brothers = ('Tiago', 'Teste2')
sisters = ('Teste', 'XPTO')
simblings = brothers + sisters
print('Number of simblings is ',simblings)
familyMembers = simblings + ('Paulo', 'Ceu')
print('Family members: ',familyMembers)
simbling, *parents = familyMembers
print('Simbling ',simbling)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Is Estonia a nordic country?','Estonia' in nordic_countries)
print('Is Iceland a nordic country?','Iceland' in nordic_countries)