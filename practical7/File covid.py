import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.getcwd()
os.chdir("C:\cygwin64\home\wjw\Practical7")
#read the csv file
covid_data=pd.read_csv("full_data.csv")
covid_data.info()
covid_data.describe()
covid_data.iloc[0:12:2,:]
#judge whether the location is Afghanistan, if true, output as Adganistan_data
Afghanistan_data=covid_data[covid_data['location']=="Afghanistan"]
#find the total_cases in Afghanistan
print(Afghanistan_data.loc[:,"total_cases"])
#similarly,find all the data in World
world_data=covid_data[covid_data['location']=="World"]
#similarly, find new_cases in world
world_new_cases=world_data.loc[:,"new_cases"]
world_date=world_data.loc[:,"date"]
print(world_new_cases)
print(world_date)
#print the mean and median of the world new cases
print(np.mean(world_new_cases))
print(np.median(world_new_cases))
#draw a boxplot with meanline and box, and without outliers
plt.figure()
labels=["World new cases"]
plt.boxplot(world_new_cases,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,
            showmeans=True,
            showbox=True,
            showcaps=True,
            showfliers=False,
            notch=False,
            labels=labels
            )

plt.figure()
#create a title for plot
plt.title('Covid 19 in worldwide')
world_new_deaths=world_data.loc[:,'new_deaths']
#the new case is drawn with blue"*" and the new death is drawn with red. x-axis is date and y-axis is cases or deaths.
plt.plot(world_date,world_new_cases,'b*',label='New cases')
plt.plot(world_date,world_new_deaths,'r*',label='New deaths')
#place the legend in the best location automatically
plt.legend(loc='best')
# show accurate date in x-axis
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)

plt.figure()
plt.title("New cases in China and the UK")
#label two axis
plt.xlabel("date")
plt.ylabel("new cases")
#similarly choose data in China
China_data=covid_data[covid_data['location']=="China"]
China_date=China_data.loc[:,"date"]
#similary find the new cases data in China and UK
China_new_cases=China_data.loc[:,"new_cases"]
#draw new cases in China and UK with different colour in the same figure
plt.plot(China_date,China_new_cases,'b+',label="China")
United_Kingdom_data=covid_data[covid_data['location']=="United Kingdom"]
United_Kingdom_date=United_Kingdom_data.loc[:,"date"]
United_Kingdom_new_cases=United_Kingdom_data.loc[:,"new_cases"]
plt.plot(United_Kingdom_date,United_Kingdom_new_cases,'r+',label="the UK")
plt.legend(loc='best')

plt.figure()
Spain_data=covid_data[covid_data['location']=="China"]
Spain_date=Spain_data.loc[:,"date"]
Spain_new_cases=Spain_data.loc[:,"new_cases"]
Spain_total_cases=Spain_data.loc[:,"total_cases"]
plt.title("Covid 19 in Spain")
plt.xlabel("date")
plt.ylabel("cases in Spain")
plt.plot(Spain_date,Spain_total_cases,'ro',label='Total cases')
plt.plot(Spain_date,Spain_new_cases,'bo',label='New cases')
plt.legend(loc='best')
plt.xticks(Spain_date.iloc[0:len(Spain_date):4],rotation=90)
plt.show()
