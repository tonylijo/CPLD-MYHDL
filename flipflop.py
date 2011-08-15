from myhdl import *

def dff(q,d,clk):
    @always(clk.posedge)
    def logic():
        q.next = d
    return logic

from random import randrange

def test_dff():

    q,d,clk = [Signal(bool(0)) for i in range(3)]
    dff_inst = dff(q,d,clk)
    @always(delay(10))
    def clkgen():
        clk.next = not clk
        
    @always(clk.negedge)
    def simulus():
        d.next = randrange(2)
        
    return dff_inst,clkgen,simulus

def simulate(timesteps):
    tb = traceSignals(test_dff)
    sim = Simulation(tb)
    sim.run(timesteps)

simulate(2000)
