#NMT parameters
import numpy as np
import random
from matplotlib import pyplot as plt
from statistics import mean
import seaborn as sns
import matplotlib

#Normal Cell Parameters
N_area = 			38.89723427
N_perimeter =		24.34161486
N_circularity =		0.796163666
N_maxcaliper =		8.661751735
N_mincaliper =		6.091906725
N_eccentricity =	0.651192842


#Senescent Cell Parameters
S_area = 			57.479797979798
S_perimeter =		30.0912616161616
S_circularity =		0.774628282828283
S_maxcaliper =		10.4962
S_mincaliper =		7.37436767676767
S_eccentricity =	0.683340404040404

#Percentual change from both states
abs_area = abs(100-((S_area/N_area)*100))
abs_perimeter = abs(100-((S_perimeter/N_perimeter)*100))
abs_circularity = abs(100-((S_circularity/N_circularity)*100))
abs_maxcaliper = abs(100-((S_maxcaliper/N_maxcaliper)*100))
abs_mincaliper = abs(100-((S_mincaliper/N_mincaliper)*100))
abs_eccentricity = abs(100-((S_eccentricity/N_eccentricity)*100))

summation= float(abs_area) + float(abs_perimeter) + float(abs_circularity) + float(abs_maxcaliper) + float(abs_mincaliper) + float(abs_eccentricity)
print(summation)

def Average(l): 
    avg = mean(l) 
    return avg

import xlrd
import xlsxwriter
book = xlrd.open_workbook('X.xlsx')
sheet = book.sheet_by_name('Sheet1')
data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
# Profit !
del data[0]
result=[]
for row in data:
	row=row[2:8]
	row[0]=(((row[0]-N_area)/(S_area-N_area))*(abs_area/summation))
	row[1]=(((row[1]-N_perimeter)/(S_perimeter-N_perimeter))*(abs_perimeter/summation))
	row[2]=(((row[2]-N_circularity)/(S_circularity-N_circularity))*(abs_circularity/summation))
	row[3]=(((row[3]-N_maxcaliper)/(S_maxcaliper-N_maxcaliper))*(abs_maxcaliper/summation))
	row[4]=(((row[4]-N_mincaliper)/(S_mincaliper-N_mincaliper))*(abs_mincaliper/summation))
	row[5]=(((row[5]-N_eccentricity)/(S_eccentricity-N_eccentricity))*(abs_eccentricity/summation))
	test=Average(row)/0.166667
	result.append(test)
	#print (result)


with open('XData.txt', 'w') as f:
    for item in result:
        f.write("%s\n" % item)
listt=[]
final_list=[]
final_list2=[]
with open('XData.txt') as f:
    lines = f.readlines()
    #print(lines)
    for i in lines:
    	i=i.strip()
    	#print(i)
    	i=float(i)
    	final_list.append(i)
    	print(i)
    print(final_list)

    if i in final_list:
    	o=sum(i>0 and i<1 for i in final_list)/len(final_list)
    	final_list2.append(o)
    	X=sum(i>0 and i<2 for i in final_list)/len(final_list)
    	final_list2.append(X)
    	X=sum(i>0 and i<3 for i in final_list)/len(final_list)
    	final_list2.append(X)
    	X=sum(i>0 and i<4 for i in final_list)/len(final_list)
    	final_list2.append(X)
    	X=sum(i>0 and i<5 for i in final_list)/len(final_list)
    	final_list2.append(X)
    	X=sum(i>1 and i<2 for i in final_list)/len(final_list)
    	final_list2.append(X)
    	X=sum(i>2 and i<3 for i in final_list)/len(final_list)
    	final_list2.append(X)
    	o8=sum(i>3 and i<4 for i in final_list)/len(final_list)
    	final_list2.append(o8)
    	o9=sum(i>4 and i<5 for i in final_list)/len(final_list)
    	final_list2.append(o9)
    	X0=sum(i>1 and i<5 for i in final_list)/len(final_list)
    	final_list2.append(X0)
    	X1=sum(i>2 and i<5 for i in final_list)/len(final_list)
    	final_list2.append(X1)
    	X2=sum(i>3 and i<5 for i in final_list)/len(final_list)
    	final_list2.append(X2)
    	X3=sum(i>1 and i<4 for i in final_list)/len(final_list)
    	final_list2.append(X3)
    	X4=sum(i>1 and i<3 for i in final_list)/len(final_list)
    	final_list2.append(X4)
    	X5=sum(i>2 and i<4 for i in final_list)/len(final_list)
    	final_list2.append(X5)
    	print(final_list2)

    	#Check if final_list is a list
    	check_list=isinstance(final_list2, list)
    	print(check_list) 

    	with open('XData_parameters.txt', 'w') as f:
    		for item in final_list2:
        		f.write("%s\n" % item)
    	
#Now I have the final list, which only needs to be moved to txt of excel and will be ready to go. Now, you can add graphs and stuff.
