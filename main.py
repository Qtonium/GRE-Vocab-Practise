import pandas as pdimport numpy as npimport random kk = input("enter book no. ")df = pd.read_csv("Book"+kk+".csv").to_numpy()words = []means = []for i in range(len(df)):    means.append(str(df[i][15]).lower())    words.append(str(df[i][14]).lower())s = ""ckar = []for i in range(len(means)):    ckar.append(0)ctr = 0while(s!="quit"):    p = random.randint(0, len(means)-1)    kl = 0    if(ckar[p]==0):        ty = 0        while(ty!=4):            if kl==0:                print(words[p].upper())            s = input("enter input : ").lower()            if(s==means[p]):                print("Bravo u are right!")                ckar[p] = 1                print("*******************************************\n")                break            elif ty<3:                print("Oops wrong try again " + str(ty+1))                ty += 1            else:                print("*******************************************\nskipping word\n")                ty+=1            kl+=1    else:        while(ckar[p%len(ckar)]!=0):            p+=1        p = p%len(ckar)                ty = 0        while(ty!=4):            if kl==0:                print(words[p].upper())            s = input("enter input : ").lower()            if(s==means[p]):                print("Bravo u are right!")                ckar[p] = 1                print("*******************************************\n")                break            elif ty<3:                print("Oops wrong try again " + str(ty+1))                ty += 1            else:                print("*******************************************\nskipping word\n")                ty+=1            kl+=1    ctr+=1    if(ctr==len(ckar)):        break                    