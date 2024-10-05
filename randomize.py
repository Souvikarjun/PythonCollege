import random

listOfExperiment = [1,2,3,4,5,6,7,16,9,17,18,19,13,20]
listOfTeams = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]


print("Team \t Experiment")

for i in range(1,15):
    Experiment = random.choice(listOfExperiment)
    Team = random.choice(listOfTeams)
    print(Team," \t ", Experiment)
    listOfExperiment.remove(Experiment)
    listOfTeams.remove(Team)

