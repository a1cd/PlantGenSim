#!/usr/bin/python3
#created by Everett
#MESS around with this this stuff:
#————————————————————————————
#how many generations are simulated
generations = 10
#how many fruits are produced by a plant:
fruitsPerPlant = 2
#the number of seeds in a fruit:
SeedsPerFruit = 2
# chance of seeds sucsessfully creating a plant
SeedSurvivalRate = 1.0 #must be between 0 and 1
#how many plants are there in the beginning:
PlantsAtTheBeginning = 1 

#——>> [ xkcd MODE!!!! ] <<––
xkcd = False
#————————————————————————————
#MORE ADVANCED FEATURES :) (not finished so they dont work)
#————————————————————————————
#if you want to use them set this to "adv = True"
adv = False
# all of the following is ignored if the above is not True
randomization = False #adds some random chance to seed survival and death chance.
#here put the amout of plants that the area can house. if the number goes over then some will die.
NumberOfPlantsBeforeDeath = 10000 #0 means limitless
DeathChance = 0.5 #chance of death if maximum occupancy is exceeded
#————————————————————————————
#MESS WITH THE NUMBERS ABOVE^ 
#ONCE UR DONE PRESS THE GREEN BUTTON AT THE TOP THAT SAYS RUN
#    /|\
#  /  | \
# /   |  \
#/    |   \
#     | 
#     |
#     |
#     |







#---------------------------------------
#dont change this stuff:

#imports
import matplotlib
from matplotlib import pyplot
from scipy import interpolate
import numpy as np
import os
os.system('cls' if os.name == 'nt' else 'clear')

if xkcd == True:
    pyplot.xkcd()

PlantsInGen = PlantsAtTheBeginning
#defining some variables
TotalFruits = 0
TotalSeeds = 0
plantsovertime = []
#the math that calculates the numbers
for i in range(generations):
    TotalFruits = PlantsInGen * fruitsPerPlant
    TotalSeeds = TotalFruits * SeedsPerFruit
    PlantsInGen = TotalSeeds * SeedSurvivalRate
    plantsovertime.append(PlantsInGen)
from pylab import *
import numpy as np


t = arange(0.0, float(generations), 1)
for i in plantsovertime:
  print(i)
s = np.array(plantsovertime)

x_new = np.linspace(1, float(generations), 300)
a_BSpline = interpolate.make_interp_spline(t, s)
y_new = a_BSpline(x_new)

plt.plot(x_new, y_new)


xlabel('Time')
ylabel('Plants')
title('Plants over time')
grid(True)
savefig("line_chart.png")
print("if you want a better version, message me.")
print("I can send you an app verion that you can")
print("run on your computer.")
print("")
show()