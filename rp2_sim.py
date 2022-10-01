def asm_pio(*args, **kwargs):
    """ 
    Decorador que recibe los parametros del programa (parametros para una ejecucion en una FMS
    Finite state machine de rapsberry pico) y llama al programa con las instruccioens
    """        
    def decorador(programa):
        def compilador():
            print("Parámetros", kwargs) 
            programa()
            return None
        return compilador
    return decorador

def decorador_instr(fun_inst):
    """ 
    Decorador que ejecuta las instrucciones de la FSM
    """ 
    def decoracion_instr(self,*args, **kwargs):
        fun_inst(self,*args, **kwargs)
        return None 
    return decoracion_instr

pins='pins'

class PIO():
    """ 
    Clase que guarda constantes de la rapsberry pico de los tipos de entrada y salida del los pines
    """ 
    OUT_LOW='PIO.OUT_LOW'
    

class StateMachine:
	""" 
	Clase que analiza y ejecuta instrucciones propias de una FSM de rapberry pico
	""" 
	def __init__(self, id_, program, freq=125000000, **kwargs):
		""" 
		Metodod que inicializa la clase StateMachine creando la instancia de la FSM en 
		el arreglo de FMS's de la rapsberry pico y mostrando las isntrucciones
		""" 
		global sm_iniciandose,fsms
		sm_iniciandose=self
		#print('StateMachine.__init__',id_, program, freq, kwargs)
		self.lista_instr=[]
		program()
		print('Fueron leidas',len(self.lista_instr), 'instrucciones')
		sm_iniciandose=None
		fsms[id_]=self
		pass
      
        
	def active(self, x=None):
		""" 
		Funcion que enciende y apaga la maquina de estados
		""" 
		'''Esta rutina simula exclisivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
		if x==1:
			print('Está pendiente de realizar la simulacón')

fsms=[None]*8

sm_iniciandose=None    


class nop:
    """
    Clase de la cual extienden las funcionalidades que se encarga que esperar n numero de ciclos para continuar
    """
    @decorador_instr
    def __init__(self,*args, **kwargs):
        """ 
		Metodo que inicializa la clase nop, muestra quien se incializo (sea un hijo de herencia o la misma clase)
        y añade la instruccion
		""" 
        global sm_iniciandose
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass
        
    def __getitem__(self,name):
        """ 
		Metodo que se ejecuta el intenter llegar al elemento nsimo de la clase (como si fuera una lista) 
        ejem:  nopInstance[0]
        y que se encarga que gestionar la cantidad de ciclos que espera una instruccion
		""" 
        #print('nop.__getattr__',name)
        pass
        
class set(nop):
    """
    Clase que extiende de nop y que debe pasar corriente o no por un pin
    """
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
   
class wrap_target(nop):
    """
    Clase que extiende de nop y que marca el fin  de un ciclo y devuelve las instrucciones al principio del ciclo
    """
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass 
  
class wrap(nop):
    """
    Clase que extiende de nop y que marca el principio de un ciclo
    """
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass 
         
         
