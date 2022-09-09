# import cmath

#%%  Defining of Branch class

class Branch:
    def __init__(self,to_bus, Iine_Connectsions, Data_Settings):
        Sbase = Data_Settings[1,2]
        Vbase = Data_Settings[0,2]
        Zbase = (Vbase**2)/Sbase
#        load_power_factor =  Data_Settings[0,2]
#        gen_power_factor =  Data_Settings[1,2]
#        Ibase=Sbase/(Vbase*(cmath.sqrt(3)))
        if Iine_Connectsions[to_bus+1,2] == 0:     #Transformer impedance calculation:
            self.resistance = 0
            self.reactance = (Iine_Connectsions[to_bus+1,10]*0.01)*(((Iine_Connectsions[to_bus+1,9]*1000)/Vbase)**2)*(Sbase/(Iine_Connectsions[to_bus+1,7]*1000000))
            self.capacitaance = 0
            self.branch_number = Iine_Connectsions[to_bus+1,1]
            self.i_max = Iine_Connectsions[to_bus+1,7]#/((cmath.sqrt(3))*(Iine_Connectsions[to_bus+1,8]))
            self.from_bus = Iine_Connectsions[to_bus+1,0]
            self.to_bus = Iine_Connectsions[to_bus+1,1]
            self.impedance = complex(self.resistance,self.reactance)
            self.current = 0
            self.suppling_buses= []
        if Iine_Connectsions[to_bus+1,2]== 1:     #lines impedance calculation:
            self.resistance = Iine_Connectsions[to_bus+1,3]/Zbase
            self.reactance = Iine_Connectsions[to_bus+1,4]/Zbase
            self.capacitaance = Iine_Connectsions[to_bus+1,6]*Zbase
            self.branch_number = Iine_Connectsions[to_bus+1,1]
            self.i_max = Iine_Connectsions[to_bus+1,5]
            self.impedance = complex(self.resistance,self.reactance)
            self.from_bus = Iine_Connectsions[to_bus+1,0]
            self.to_bus = Iine_Connectsions[to_bus+1,1]
            self.current =  0  
            self.suppling_buses= []
            
            
#%%  Defining of Bus class
           

class Bus:
#    print(to_bus)
    def __init__(self, to_bus, Loads, Data_Settings,Iine_Connectsions):
        Sbase=Data_Settings[1,2]
#        Vbase=Data_Settings[2,2]
#        Zbase=(Vbase**2)/Sbase
#        load_power_factor = Data_Settings[0,2]
#        gen_power_factor = Data_Settings[1,2]
#        load_power_factor = Data_Settings[0,2]
#        gen_power_factor = Data_Settings[1,2]
#        Ibase=Sbase/(Vbase*(cmath.sqrt(3)))
        if Loads[to_bus,1] == 0:     #Loads
    #        print(to_bus)
            self.bus_number = Iine_Connectsions[to_bus+1,1]
            self.V_initial = 1
            self.voltage = self.V_initial
            self.previous_voltage = self.V_initial
            self.P_load =  (1000/Sbase) * Loads[to_bus,2]#*load_power_factor
            self.Q_load = (1000/Sbase) * Loads[to_bus,3]#*(cmath.sqrt(1-load_power_factor**2))
            self.P_gen = 0
            self.Q_gen = 0
            self.is_genarator = False 
            self.is_load = True 
            self.P_net = self.P_load + self.P_gen
            self.Q_net = self.Q_load + self.Q_gen
            self.injection = complex (self.P_net, self.Q_net )
            self.suppling_branch = [] 
            self.parent_bus = [] 
            self.children_buses = []
        #   self.supplied_by= Loads[to_bus, ]
        #   self.supplied=       
        #   self.type= 
        if Loads[to_bus,1] == 1:     #Genarators
  #          print(to_bus)
            self.bus_number = Iine_Connectsions[to_bus+1,1]
            self.V_initial = 1
            self.voltage = self.V_initial
            self.previous_voltage = self.V_initial
            self.P_load = 0
            self.Q_load = 0
            self.P_gen = (1000/Sbase)* Loads[to_bus,2]#*gen_power_factor
            self.Q_gen = (1000/Sbase)*Loads[to_bus,3]#*(cmath.sqrt(1-gen_power_factor**2))
            self.is_genarator = True
            self.is_load = False 
            self.P_net = self.P_load + self.P_gen
            self.Q_net = self.Q_load + self.Q_gen
            self.injection = complex (self.P_net, self.Q_net )
            self.suppling_branch = []
            self.parent_bus = [] 
            self.children_buses = []

    
        