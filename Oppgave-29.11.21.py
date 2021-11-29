for i in range(5): #ytre løkke
    print("rad",i,end=" : ")
    for j in range(4): #indre løkke
        print("x",end=" ")
    print() #tom print-funksjon for å starte ny linje

    #range-funskjon stopper FØR verdien tilstop-argumentet
    for i in range(1,2): #Ytre for-løkke: bestemmer antall rader
        for j in range(1,11): #Indre for-løkke: bestemmer antall kolonner
            print(i*j, end=" ") #
    
