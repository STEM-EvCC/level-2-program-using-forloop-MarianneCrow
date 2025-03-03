mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
totalMissions = 0
successfulMissions = 0
missionsbefore2000=[]

#number of missions
for i in range(len(mission_names)):
    totalMissions += 1
    if mission_success[i] == True:
      successfulMissions += 1
    if mission_years[i]<2000:
      missionsbefore2000.append(mission_names[i])
   
#Calculate percentage
successrate = (successfulMissions / totalMissions) * 100

#Print output
print("\n"+"Total number of missions: " + str(totalMissions)+"\n")
print("Number of successful missions: " + str(successfulMissions)+"\n")
print("Success rate: {:.2f}%".format(successrate)+"\n")
print("Missions launched before the year 2000:"+"\n")

for mission_years in missionsbefore2000: 
  print("- " + str(mission_years)+"\n")