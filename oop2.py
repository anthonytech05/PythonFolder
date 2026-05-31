
from oop import Person

# inheritance
class Player(Person):
    
    def __init__(self, name, gender,nationality,speed=20):
        super().__init__(name, gender)
        self.nationality = nationality
        self.speed = speed 
        self.position = None
        self.shot_power = 15
        self.attack = 5
        self.defense = 5
        self.club = None 
        self.__goals = 0 

    def retrieveGoalsScored(self)->int :
        return self.__goals
    
    def updatePlayerGoalScored(self,goal_count:int, against_club : str) -> bool : 
        '''
            This method ensures the user is attached to a club and is involved in a 
            particular match against a club..
            if all this condition are met , the user goal count is increased
        '''
        if self.club == None :
            return False 
        if against_club == None or against_club == '':
            return False
        self.__goals += goal_count
        return True 

player1 = Player('Ahmed Musa','m', "nigeria")

print(f'Player 1 : {player1.fullname}')
player1.updateFullname("Peter Musa")
print(f'Player 1 : {player1.fullname}')
print(f"Nationality:{player1.nationality}")

# player1.__goals = 50000
print(f'Goals Scored : {player1.retrieveGoalsScored()}')
was_documented = player1.updatePlayerGoalScored(2,'Arsenal')
print(f'Player score was documented : {was_documented}')
print(f'Goals Scored : {player1.retrieveGoalsScored()}')

player1.club = 'Arsenal'
# prevent own goa.. scoring against your preset club should not be documented as a goal
was_documented = player1.updatePlayerGoalScored(2,'Arsenal')
print(f'Player score was documented : {was_documented}')
print(f'Goals Scored : {player1.retrieveGoalsScored()}')