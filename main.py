#!/usr/bin/python3
config = open("config.txt", 'r')
ConfigValuePlaces = [5,9,12,15,19,23,26,31,35,39,43]
configSplit = config.read().split("\n")
for i in ConfigValuePlaces:
  print(configSplit[i])
exit()


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