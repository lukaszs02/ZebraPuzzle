from utils import generateRandomSolution
from utils import lastIndex
from utils import randomInt

key = ["nation", "color", "drink", "smoke", "pet"]

class solution(object):

    def __init__(self):
        self.solution = generateRandomSolution()
        self.fitnes = 0.0
        self.hasTestYet = False
        self.mutationProbabily = 300

    def toString(self):
        for row in self.solution:
            print(row)
        print('Fitnes {fitnes}'.format(fitnes=self.fitnes))

    def mutate(self):
        tempValueIndex = randomInt(0, lastIndex(key))
        newIndex = randomInt(0, lastIndex(key))
        while tempValueIndex == newIndex:
            newIndex = randomInt(0, lastIndex(key))
            pass
        if(newIndex != tempValueIndex):
            keyToMutate = key[randomInt(0, lastIndex(key))]
            tempValue = self.solution[tempValueIndex][keyToMutate]
            self.solution[tempValueIndex][keyToMutate] = self.solution[newIndex][keyToMutate]
            self.solution[newIndex][keyToMutate] = tempValue
            return True

    def reproduce(self, solutionA, solutionB):
        for i in key:
            pivot = randomInt(0, 100)
            for j in range(0, 5):
                if(pivot < 50):
                    tempSolution = solutionA.getSolutionTab()
                else:
                    tempSolution = solutionB.getSolutionTab()
                self.solution[j][i] = tempSolution[j][i]
        if(randomInt(1, 1000) <= self.mutationProbabily):
             self.mutate()

    def checkSingleHouseRule(self, key1, value1, key2, value2):
        for i in self.solution:
            if(i[key1] == value1 and i[key2] == value2):
                return True
        return False

    def checkNeighborhoodRules(self, House1_key, House1_value, House2_key, House2_value):
        for i in range(0, 5):
            if(self.solution[i][House1_key] == House1_value):
                if(i + 1) % 5 :
                    if(self.solution[(i + 1)][House2_key] == House2_value):
                        return True
        return False

    def checkRuleForExactHouse(self, house, key, value):
        return self.solution[house][key] == value

    def getFitnes(self):
        if(self.hasTestYet == False):
            self.test()
        return self.fitnes

    def test(self):
        sum = 0
        if(self.checkSingleHouseRule('nation', 'Englishman', 'color', 'Red')):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule('nation', 'Spaniard', 'pet', 'Dog')):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule('drink', 'Coffe', 'color', 'Green')):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule("nation", "Ukrainian", "drink", "Tea")):
            sum += 1
        else:
            sum -= 1
        if(self.checkNeighborhoodRules("color", "Ivory", "color", "Green")):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule("smoke", "Old Gold", "pet", "Snails")):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule("smoke", "Kools", "color", "Yellow")):
            sum += 1
        else:
            sum -= 1
        if(self.checkRuleForExactHouse(2, "drink", "Milk")):
            sum += 1
        else:
            sum -=1
        if(self.checkRuleForExactHouse(0, "nation", "Norwegian")):
            sum += 1
        else:
            sum -= 1
        if(self.checkNeighborhoodRules("pet", "Fox", "smoke", "Chesterfield")):
            sum += 1
        else:
            sum -=1
        if(self.checkNeighborhoodRules("smoke", "Kools", "pet", "Horse")):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule("smoke", "Lucky Strike", "drink", "Orange juice")):
            sum += 1
        else:
            sum -= 1
        if(self.checkSingleHouseRule("nation", "Japanese", "smoke", "Parliaments")):
            sum += 1
        else:
            sum -= 1
        if(self.checkNeighborhoodRules("nation", "Norwegian", "color", "Blue")):
            sum += 1
        else:
            sum -= 1

        self.fitnes = round((sum / 14) * 100, 3)
        self.hasTestYet = True

    def getSolutionTab(self):
        return self.solution

