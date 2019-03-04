import random

i=1
sample=random.randint(1000,9999)

while(1):
	b=random.randint(1000,9999)
	if(sample==b):
		print("Bot "+str(i)+" hit")
	i+=1
