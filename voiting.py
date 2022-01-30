'''
Created on 30 янв. 2022 г.

@author: oooooo2000@gmail.com
'''
#import numpy as np
import pandas as pd
import ctypes  # An included library with Python install.  
df = pd.read_csv("rezgol.csv", header=0, delimiter=',', keep_default_na=False)
print(df)
# voitings = []
y = 0


#print(voitings)
def countitog(voitings,Iter):

    itog = {}
    for x in voitings:
        print(voitings[voitings[x] <= Iter])

        # print(Iter)
        itog.update({x:voitings[voitings[x] <= Iter].shape[0]})
        # for y in x:        
        #     print(y)
        #     if x.get(y)in Iters:           
        #         itog.update({y:itog.setdefault(y,0)+1})
        #     print(itog)\/
    return itog

#sorted(my_dict, key=my_dict.get, )[:3]  


# def deleteAuts(ItogNameAut,voitings):    
#     for x in voitings:               
#         del x[ItogNameAut]
#
#     return voitings    

Iter = 0
Iters = []
while Iter <df.shape[1]:
    Iter +=1
    Iters.append(Iter)
    
    #print('Итерация: ' + str(Iters)) 
    itog = countitog(df,Iter) 
    print(itog)
    itogname = sorted(itog,key=itog.get,reverse=True)[:1][0]
    ItogNameAut = sorted(itog,key=itog.get,)[:1][0]
       
    if itog.get(itogname)> df.shape[1]/2:
        print('Найден победитель на итерации ' + str(Iter))        
        print(itogname,' голосов ' ,itog.get(itogname))
         
        ctypes.windll.user32.MessageBoxW(0, 'Найден победитель на итерации ' + str(Iter) + ' Победил: ' + itogname + ', набрав   ' + str(itog.get(itogname)) + ' голосов', "Разультаты голосования", 0)
        ##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | No 
##  6 : Cancel | Try Again | Continue
        break
    #quit()
    
        #print('next')
        
    #voitings = deleteAuts(ItogNameAut,voitings)   

#print(voitings)