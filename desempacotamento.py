
#Extrair Olá

d = {'k1':[1,2,3,{'café':['banana','mulher', 'colher',{'alvo':[1,2,3,'olá']}]}]}

l1 = d.values()
print(l1)
dk = dict()
for i in l1:
	for i2 in i:
		print(i2)
		if type(dk) == type(i2):
			dk1 = i2.values()
			for a in dk1:
				print(a)
				for b in a:
					print(b)
					if type(dk) == type(b):
						dk2 = b.values()
						for c in dk2:
							for c1 in c:
								print(c1)

