# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:39:30 2021

@author: ASUS
"""

#create subplots of multiple plots in one figure
#import pyplot
#open the files in read mode and read lines
# Import the pyplot
import matplotlib.pyplot as plt
f =open('salesdata2.csv','r')
salefile= f.readlines()
#create sales list
sale_list =[]
s_list=[]
c_list=[]
#append all the records from files to the saleslist since it will be in str
for records in salefile:
    sale,cost =records.split(sep=',')
    s_list.append(int(sale))
    c_list.append(int(cost))
    
#create list of lists
sale_list.append(s_list)
sale_list.append(c_list) 
#Scatter plot
#subplot(rows,columns)
plt.subplot(2,2,1)
plt.title('sales vs cost')
plt.xlabel("sales")
plt.ylabel("cost")
plt.scatter(s_list,c_list)

#boxplot
plt.subplot(2,2,2)
plt.title('boxplot of sales')
plt.ylabel("USD")
plt.boxplot(sale_list)

#histogram
plt.subplot(2,2,3)
plt.title("Histogram of Sales")
plt.ylabel("USD")
plt.hist(s_list, bins=5, rwidth=0.9, color='c')
# lineplot of stock
plt.subplot(2,2,4)
x_days  = [1,2,3,4,5]
y_price1 = [9,9.5,10.1,10,12]

plt.title("Stockprice History")
plt.ylabel("Price")
plt.xlabel("Day")
plt.plot(x_days,y_price1)

#show plot
plt.show()