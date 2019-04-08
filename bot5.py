import random,time

crowd = []

n=1
iter=1

while(1):
    a = random.randint(0,99)
    if(a>10):
        crowd.append("subject"+str(n))
        print(str(iter)+": wave surged subject"+str(n))
        n+=1
    else:
        if(crowd!=[]):
            crowd.remove("subject"+str(n-1))
            print(str(iter)+": wave killed subject"+str(n-1))
            n-=1
        if(a==7):
            crowd=[]
            print("meltdown! Everyone's dead")            
            n=1        


    time.sleep(0.3)
    iter+=1