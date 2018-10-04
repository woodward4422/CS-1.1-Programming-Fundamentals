

class Virus(object):

    def __init__(self,name,mortality_rate,repro_rate):
        self.name = name
        self.mortality_rate = mortality_rate
        self.repro_rate = repro_rate


# Test that checks to make sure the virus object is created correctly
def test_virus_instantiation():
    test_virus = Virus("Ebola",0.8,0.3)
    assert test_virus.name == "Ebola"
    assert test_virus.mortality_rate == 0.8
    assert test_virus.repro_rate == 0.3



    