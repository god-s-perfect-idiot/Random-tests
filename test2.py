import random

bots=[]
n=0
locn={}

def conjure():
    global n
    n+=1
    bots.append(str(n))
    print("bot "+str(n)+" is live now")

def seat(n):
    x=str(random.randint(0,999))
    y=str(random.randint(0,999))
    locn[n]=[x,y]

live=1
while(live):
    inp=input("1.start new bot\n2.skip\n3.exit\n")
    if(inp=="1"):
        conjure()
    elif(inp=="2"):
        pass
    elif(inp=="3"):
        live=0
    #for i in range(4):
    for ite in range(10000):     
        clashed=0
        for i in bots:
            seat(i)
            for j in bots:
                if(locn.get(i)==locn.get(j) and i!=j):
                    print(str(i)+" just blinked to where "+str(j)+" is seated on iteration "+str(ite))
                    clashed=1
            #if(clashed==0):
                #print(str(i)+" just blinked to ("+str(locn.get(i)[0])+","+str(locn.get(i)[1])+")")