def wash(dry=False, water=8):
	print('加水',water,'分满')
	print('加洗衣液')
	print('旋转')
	if dry:
		print('烘干')
wash(water=10)
print('-----------')
print('^ == ^')
wash()
wash(True, water=7)
print('==========')
def add(x=0, y=0):
	print(x + y)
add(5)
add(y=6)
add(x=5, y=6)



