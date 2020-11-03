#!/usr/bin/python3
#created by Everett
#MESS around with this this stuff:
#————————————————————————————
#Presets: ["None", "Everett's", "Limited Resources", "my favorite"]
Preset = "None"
#how many generations are simulated
generations = 50
#how many fruits are produced by a plant:
fruitsPerPlant = 2
#the number of seeds in a fruit:
SeedsPerFruit = 1
# chance of seeds sucsessfully creating a plant
SeedSurvivalRate = 1 #must be between 0 and 1
#how many plants are there in the beginning:
PlantsAtTheBeginning = 1


smoothing = True #looks nicer if True but can be misleading


#here put the amout of plants that the area can house. if the number goes over then some will die.
NumberOfPlantsBeforeDeath = 10000 #0 = disabled
DeathChance = 1 #chance of death if maximum occupancy is exceeded

randomization = False #adds some random chance to seed survival and death chance.

SmoothNearLimit = True 

#————————————————————————————
#MESS WITH THE NUMBERS ABOVE^ 
#ONCE UR DONE PRESS THE GREEN BUTTON AT THE TOP THAT SAYS RUN
#       /|\
#      / | \
#     /  |  \
#    /   |   \
#        | 
#        |
#        |
#        |










#---------------------------------------
#dont change this stuff:

#imports
import matplotlib, random
from matplotlib import pyplot
from scipy import interpolate
import numpy as np

#Loading Presets
["None", "Everett's", "Limited Resources"]
if Preset.lower() == "none":
    None == None
elif Preset.lower() == "Everett's":
    None == None
elif Preset.lower() == "Limited Resources":
    None == None
else:
    Exception("invalid preset")


#defining some variables
PlantsInGen = PlantsAtTheBeginning
TotalFruits = 0
TotalSeeds = 0
plantsovertime = []
#the math that calculates the numbers
for i in range(generations):
    if PlantsInGen > NumberOfPlantsBeforeDeath:
        if NumberOfPlantsBeforeDeath == 0:
            TotalFruits = PlantsInGen * fruitsPerPlant
            TotalSeeds = TotalFruits * SeedsPerFruit
            PlantsInGen = TotalSeeds * SeedSurvivalRate
            plantsovertime.append(PlantsInGen)
        else:
            #generation is too big
            PlantsInGen = PlantsInGen - (int(PlantsInGen - NumberOfPlantsBeforeDeath) *2) * DeathChance
            plantsovertime.append(PlantsInGen)
    else:
        TotalFruits = PlantsInGen * fruitsPerPlant
        TotalSeeds = TotalFruits * SeedsPerFruit
        PlantsInGen = TotalSeeds * SeedSurvivalRate
        plantsovertime.append(PlantsInGen)
    if PlantsInGen < 0:
        print("Simulation dead: all plants died")
        generations = i + 1
        plantsovertime[i] = 0
        TotalFruits = 0
        TotalSeeds = 0
        break
    if randomization == True:
        PlantsInGen = PlantsInGen + int(random.random()*2)
from pylab import *
import numpy as np



if smoothing == True:
    #prevent smoothing prediction drops
    t = arange(0.0, float(generations+1), 1)
    plantsovertime.append(plantsovertime[generations-1])
    print(plantsovertime)
    print(t)
    s = np.array(plantsovertime)
    #smooth lines
    x_new = np.linspace(1, float(generations), 300)
    a_BSpline = interpolate.make_interp_spline(t, s)
    y_new = a_BSpline(x_new)
    #plot graph
    plt.plot(x_new, y_new)
else:
    t = arange(0.0, float(generations), 1)
    print(plantsovertime)
    print(t)
    s = np.array(plantsovertime)
    plot(t, s)#plot
if not(NumberOfPlantsBeforeDeath == 0):
    dline = [NumberOfPlantsBeforeDeath, NumberOfPlantsBeforeDeath]
    dlinetime = [0, generations]
    plot(dlinetime, dline, color='r')


minorticks_on()

xlabel('Time')
ylabel('Plants')
title('Plants over time')
grid(True)
show()