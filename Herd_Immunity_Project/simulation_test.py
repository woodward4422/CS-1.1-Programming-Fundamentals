import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation

def test_simulation_instantiation():
    ebola_simulation = Simulation(1000,0.8,"Ebola",0.7,0.3)
    assert ebola_simulation.population_size == 1000
    assert ebola_simulation.total_infected == 1
    assert ebola_simulation.virus_name == "Ebola"
    assert ebola_simulation.mortality_rate == 0.7
    assert ebola_simulation.basic_repro_num == 0.3
    assert ebola_simulation.vacc_percentage == 0.8
    print(len(ebola_simulation.population))
    assert len(ebola_simulation.population) == 1000




