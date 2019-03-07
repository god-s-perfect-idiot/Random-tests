import random

bots=[]
n=0
value={}


def bcreate(i,iter):
	global n
	n+=1
	bots.append(n)
	print(str(i)+" created "+str(n)+" at iteration "+str(iter))


bcreate(0,0)
bcreate(0,0)

iter=0
while(1):
	iter+=1
	for i in bots:
		value[i]=random.randint(0,9999)

	for i in bots:
		if(value.get(i)==6789):
			bcreate(i,iter)
