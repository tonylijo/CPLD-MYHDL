from myhdl import Signal, now, delay, Simulation, instance, always_comb, bin

def half_adder(A,B,S,C):
    """{A,B} inputs
       {S,C} outpus
       S - sum output
       C - carry out
       """
    @always_comb
    def logic():
        S.next = A ^ B
        C.next = A & B
    return logic

from random import randrange

def testBench():
    """function to test the half adder module"""
    A,B,S,C = [Signal(bool(0)) for i in range(4)]
    add_inst = half_adder(A,B,S,C)
    
    @instance
    def simulus():
        for i in range(10):
            A.next = randrange(2)
            B.next = randrange(2)
            yield delay(10)
            print "A: " + bin(A,1) + "B: " + bin(B,1) + "|S: " + bin(S,1) + "C: " + bin(C,1)
    return add_inst, simulus

inst = testBench()
sim = Simulation(inst)
sim.run()
