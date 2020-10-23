def checkwin(recordboard,player):
    ans_set=[[0,1,2],[3,4,5],[6,7,8],[2,5,8],[1,4,7],[0,3,6],[0,4,8],[2,4,6]]
    checkindex1=[]
    
    
    for i in range(0,len(recordboard)-1):
        if(recordboard[i]==player):
            checkindex1.append(i)
            
                
    for l in ans_set:
        ctr=0
        for z in checkindex1:
            if(z in l):
                ctr+=1
                if(ctr==3):
                    return("win")
    return(-1)
            



#--------------------------------------------------------------

def tttboard(run,player, index ):
    recordboard=[0,1,2,3,4,5,6,7,8]
    #for first run

    if(run==0):
        k=0
        for j in range(0,3):
            if(j>0):
                print("    -----------------------------------------")    
            for i in range(0,3):
                print("\t", end="")
                print("{}\t".format(k), end="")
                if(k not in [2,5,8]):
                    print("|", end="")
                k+=1  
            print()
        print("\n \n")
        return 0
    
    #Changing recordboard with X or O
    for l in range(0,(len(recordboard)-1)):
        if(index == recordboard[l]):
            recordboard[l]=player
     #checkwin
    ans=checkwin(recordboard,player)
     #Display board and continue
    if(ans==-1):    
        print("ehh")
        return 0
    else:
        print("It's a win!!!")         
        
    
    

        




    


#-------------------------------------------------------------- 

def Welcome():
    ctr=-1
    print("Hello player! Welcome to TicTacToe game")
    tttboard(0,"a",0)
    
    while(ctr==-1):
        P1=str(input("\nWhat do you want (X or O)? "))
        if(P1=="X"):
            P2="O"
            ctr=1
        elif(P1=="O"):
            P2="X"
            ctr=1
        else:
            print("Wrong input, choose again(X or O)")
    return(P1,P2)

#--------------------------------------------------------------
def Gameplay(p1, p2):
    ctr=1
    index=-1
    while(ctr<10):
        while(index not in [0,1,2,3,4,5,6,7,8]):
            index=int(input("Choose a valid index "))
                
        if(ctr%2==0):
            print(p2)
            tttboard(ctr,p2, index)
            index=-1
            ctr+=1
        else:
            print(p1)
            tttboard(ctr,p1,index)
            index=-1
            ctr+=1

p1,p2=Welcome()
Gameplay(p1,p2)
