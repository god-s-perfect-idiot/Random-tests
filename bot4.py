import random

hit=[]
upper=9
iteration=0

def gen():
	a=random.randint(0,upper)
	return a

while(1):
	p=gen()
	while p in hit:
		p=gen()
	print(str(p))
	hit.append(p)
	iteration+=1
	if iteration==upper:
		upper=str(upper)
		upper=upper+"9"
		upper=int(upper)