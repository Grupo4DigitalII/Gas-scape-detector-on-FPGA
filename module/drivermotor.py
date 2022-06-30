from migen import *
from migen.genlib.cdc import MultiReg
from litex.soc.interconnect.csr import *
from litex.soc.interconnect.csr_eventmanager import *

class DriverMotor(Module, AutoCSR):
    def __init__(self, inSnr, move):
    	self.clk = ClockSignal()
    	#self.reset = ResetSignal()
    	
    	self.inSnr = inSnr
    	self.move = move
    	
    	# Registros Mapa de memoria
    	
    	self.statusM = CSRStatus(2)
    	self.ena = CSRStorage(1)
    	
    	self.specials +=Instance("driverMotor", #<-- Nombre del modulo verilog
	    i_clk = self.clk,
	    i_inSnr = self.inSnr,
	    i_ena = self.ena.storage,
	    o_statusM = self.statusM.status,
	    o_move = self.move
    	)    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
