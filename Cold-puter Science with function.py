Temp = 5
num = [-14, -5, -39, -5, -7]

def FinalOutput():
	ans=0
	for number in num:
		if int(number) < 0:
			ans +=1
		print (ans)
FinalOutput()