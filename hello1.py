from myhdl import Signal, delay, always, now, Simulation

def HelloWorld():
    intervel = delay(10)
    
    @always(intervel)
    def SayHello():
        print "%s Hello World!!" %now()
        
    return SayHello

inst = HelloWorld()
sim = Simulation(inst)
sim.run(30)
