# 10/2/2018 at 5:17 PM, TODO: I need to do the time step in the simulation, Questions: Why does it say for each infected person in the time_step, I thought we were doing only 100 random interactions in total.  

# Simulation says to set the infected attribute to true on the person in the list. However, there is no infected attribute its only the infection attribute which either has a virus object or is None


# I am having trouble following the trace of the program and need to retrace the stack, it appears as if when it is checking in the did_survive_infection that none of the people have an infection, maybe look to where we declare that that person has an infection? Im also feeling uneasy about the tight coupledness of this code that is being developed, might refactor so that its not like this, but who knows?? Also, looking to add more 

# What is the cryptic issue where I cant import other classes from another file? Its really strange and I cant figure it out