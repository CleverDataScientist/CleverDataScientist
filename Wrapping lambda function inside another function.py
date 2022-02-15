def mywrapper(n):
	return lambda a:a*n
mulfive=mywrapper(5)
print(mulfive(2))	