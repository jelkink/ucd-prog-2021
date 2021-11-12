from simulation import Simulation

# create simulation with 1000 voters 
sim = Simulation(1000)

# add 5 parties at random locations 
sim.add_party("random")
sim.add_party("sticker")
sim.add_party("hunter")
sim.add_party("aggregator")
sim.add_party("predator")

# run 1 election to report on starting point
sim.run(1)
sim.print_parties_list()

# show results after 100 elections
sim.run(99)
sim.print_parties_list()

# show results after 1000 elections
sim.run(900)
sim.print_parties_list()