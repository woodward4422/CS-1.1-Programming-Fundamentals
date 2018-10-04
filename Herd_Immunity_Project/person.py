import random
# TODO: Import the virus class
from virus import Virus

class Person(object):
    '''
    Person objects will populate the simulation.

    _____Attributes______:

    _id: Int.  A unique ID assigned to each person.

    is_vaccinated: Bool.  Determines whether the person object is vaccinated against
        the disease in the simulation.

    is_alive: Bool. All person objects begin alive (value set to true).  Changed
        to false if person object dies from an infection.

    infection:  None or Virus object.  Set to None for people that are not infected.
        If a person is infected, will instead be set to the virus object the person
        is infected with.

    _____Methods_____:

    __init__(self, _id, is_vaccinated, infection=None):
        - self.alive should be automatically set to true during instantiation.
        - all other attributes for self should be set to their corresponding parameter
            passed during instantiation.
        - If person is chosen to be infected for first round of simulation, then
            the object should create a Virus object and set it as the value for
            self.infection.  Otherwise, self.infection should be set to None.

    did_survive_infection(self):
        - Only called if infection attribute is not None.
        - Takes no inputs.
        - Generates a random number between 0 and 1.
        - Compares random number to mortality_rate attribute stored in person's infection
            attribute.
            - If random number is smaller, person has died from disease.
                is_alive is changed to false.
            - If random number is larger, person has survived disease.  Person's
            is_vaccinated attribute is changed to True, and set self.infection to None.
    '''

    def __init__(self, _id, is_vaccinated, infection=None):
        # TODO:  Finish this method.  Follow the instructions in the class documentation
        # to set the corret values for the following attributes.
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection
        


    def did_survive_infection(self):
        # TODO:  Finish this method. Follow the instructions in the class documentation
        # for resolve_infection.  If person dies, set is_alive to False and return False.
        # If person lives, set is_vaccinated = True, infection = None, return True.  
        
        if self.infection:
          random_number = random.uniform(0, 1) 
          virus_mortality_rate = self.infection.mortality_rate
          if random_number < virus_mortality_rate:
              self.is_alive = False
          else:
              self.infection = None
              self.is_vaccinated = True
        else:
            print("The person is not infected!")

# Tests to see whether or not the person instantiation is correct 
def test_person_instantiation():
    test_person = Person(123,True)
    assert test_person._id == 123
    assert test_person.is_vaccinated == True
    assert test_person.is_alive == True 
    # Didnt set a virus, just set the vaccination here to be False and an Infection to be true just to check
    test_person_two = Person(124,False,True)
    assert test_person_two._id == 124
    assert test_person_two.is_vaccinated == False 
    assert test_person_two.infection == True
# Tests to see if the logic in the person method of did_survive_simulation to see if it is correct
def test_person_did_survive_simulation():
    test_person = Person(124,False,Virus("Ebola",1.5,0.8))
    assert test_person._id == 124
    assert test_person.is_vaccinated == False
    assert test_person.is_alive == True
    assert test_person.infection.name == "Ebola"
    assert test_person.infection.repro_rate == 0.8
    test_person.did_survive_infection()
    assert test_person.is_alive == False
    test_person_two = Person(125,False,Virus("Ebola",-1.0,0.5))
    test_person_two.did_survive_infection()
    test_person_two.is_alive == True 
    
    




    

