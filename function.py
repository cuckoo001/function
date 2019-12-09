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

#  return 回传 ，function如果有return,就可以把执行结果存下来
def add(x, y):
	return x + y
result = add(4, 5)
print(result)

def average(numbers):
	return sum(numbers) / len(numbers)  #算出numbers清单的平均值
print(average([1, 2, 3]))
print(average([10, 2, 30]))
print(average([100, 20, 325]))

