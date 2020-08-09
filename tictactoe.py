print('T I C   T A C  T O E')
print('THE BOX NUMBERS ARE:\n0  1  2 \n3  4  5\n6  7  8\n\n')
import random
avail=[0,1,2,3,4,5,6,7,8]
lst=[['-','-','-'],['-','-','-'],['-','-','-']]
def check(i,j):
	if (lst[0][j]==lst[1][j]==lst[2][j]):
		return True
	elif (lst[i][0]==lst[i][1]==lst[i][2]):
		return True
def diagon(ele):
	if lst[0][0]==lst[1][1]==lst[2][2]==ele:
		return True
	elif lst[0][2]==lst[1][1]==lst[2][0]==ele:
		return True
def ck(ele):
	for i in range(3):
		for j in range(3):
			if lst[i][j]==ele:
				if(check(i,j)):
					return True
def fprint():
	for i in range(3):
		print(lst[i])
it=0
while it<=8:
	print('\nU S E R',it)
	box=int(input('enterbox no.'))
	lst[box//3][box%3]='x'
	avail.remove(box)
	fprint()
	if ck('x') or diagon('x'):
		print('\nuser wins')
		break
	box=random.choice(avail)
	lst[box//3][box%3]='o'
	avail.remove(box)
	print('\nC O M P U T E R',it)
	fprint()
	if ck('o') or diagon('o'):
		print('\ncomputer wins')
		break
	it+=1
if it==9:
	print('\ndraw')