
# person, player

# CREATING A TEMPLATE
class Person:

    # constructor
    def __init__(self, name, gender):
        self.fullname = name 
        self.gender = gender
    
    def updateFullname(self,new_name):
        """
            updates the user fullname 
            @param
                new_name : str 
                This represent the new name the user wants to be identified as 
            @returns None 
        """
        self.fullname = new_name

if __name__ == "__main__": 
    # INSTANTIATING AN OBJECT FROM A CLASS
    person1 = Person('Jordin Alba','m')
    person2 = Person('Theresa Quindot', 'f')
    person3 = Person('Mavina Wisk','f')

    print(person1.fullname, person1.gender)

    person1.updateFullname('Micheal Stockings')
    print(person1.fullname, person1.gender)


    print(person2)
    print(person3)  