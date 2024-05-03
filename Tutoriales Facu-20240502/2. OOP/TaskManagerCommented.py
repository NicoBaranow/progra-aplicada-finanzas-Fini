# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:02:57 2024

@author: gbasa

CON ESTRUCTURA DE DATAFRAMES ES MAS EFICIENTE PERO ACA QUEREMOS HACER DE 0
LO MAS QUE SE PUEDA

"""
#%%

class taskmanager():
    def __init__(self, lista=[]):
        """
        Inicializa el gestor de tareas con una lista opcional de tareas.
        
        Argumentos:
            lista (list, opcional): Una lista de tareas para iniciar el gestor. Por defecto es una lista vacía.
        """
        self.tareas = lista.copy()
        
    def add_task(self, tarea=None):
        """
        Añade una nueva tarea al gestor. Si no se proporciona una tarea, se solicitará al usuario
        que introduzca los detalles de la tarea.
        
        Argumentos:
            tarea (task, opcional): La tarea a añadir. Si es None, se creará una nueva tarea. Por defecto es None.
        """
        if tarea is None or not(isinstance(tarea, task)):
            # Solicitar detalles de la nueva tarea al usuario
            name = input('Nombre de la Tarea:\t')
            responsable = input('Responsable:\t')
            due = input('Fecha Límite (dd/mm/aaaa):\t')
            due = (int(due[0:2]), int(due[3:5]), int(due[6:10]))
            aux = ['baja', 'media', 'alta']
            priority = aux[int(input('Prioridad (0=baja, 1=media, 2=alta):\t'))]
            horas = int(input('Horas Estimadas:\t'))
            tarea = task(name=name, responsable=responsable, priority=priority, due=due, est_hours=horas)
        self.tareas.append(tarea)
        return None
    
    def import_tm(self, filename):
        """
        Importa un gestor de tareas desde un archivo.
        
        Argumentos:
            filename (str): El nombre del archivo desde el que importar.
        """
        import pickle
        try:
            with open(filename, 'rb') as f:
                salida = pickle.load(f)
        except Exception as ex:
            print('Error al deserializar el objeto', ex)
        self.tareas = salida.tareas.copy()
        return None

    def export_tm(self, filename):
        """
        Exporta el gestor de tareas a un archivo.
        
        Argumentos:
            filename (str): El nombre del archivo al que exportar.
        """
        import pickle
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as ex:
            print('Error al serializar el objeto', ex)
        return None
    
    def past_due(self):
        """
        Muestra las tareas vencidas, es decir, aquellas cuya fecha límite ha pasado y aún no están completadas.
        """
        lista = [i for i in range(len(self.tareas)) if self.tareas[i].daystodue() < 0 and self.tareas[i]._avance < 1]
        
        if len(lista) == 0:
            print("NO HAY TAREAS VENCIDAS")
        else:    
            for i in lista:
                self.tareas[i].myprint()
        return None
    
    def pending(self):
        """
        Muestra las tareas pendientes, es decir, aquellas que aún no están completadas.
        """
        lista = [i for i in range(len(self.tareas)) if self.tareas[i]._avance < 1]
        if len(lista) == 0:
            print("NO HAY TAREAS PENDIENTES")
        else:    
            print("TAREAS PENDIENTES")
            for i in lista:
                self.tareas[i].myprint()
        return None

class task():
    def __init__(self,
                 name="Object Oriented Programming ", 
                 responsable="John Doe", 
                 start =(1,1,2000),
                 due   =(31,12,2100), 
                 priority='low', 
                 est_hours=1):
        """
        Inicializa una tarea con los detalles proporcionados.
        
        Argumentos:
            name (str): El nombre de la tarea.
            responsable (str): La persona responsable de la tarea.
            start (tuple): La fecha de inicio de la tarea en formato (día, mes, año).
            due (tuple): La fecha límite de la tarea en formato (día, mes, año).
            priority (str): La prioridad de la tarea, puede ser 'baja', 'media' o 'alta'.
            est_hours (int): Las horas estimadas para completar la tarea.
        """
        self._taskname = name
        self._responsable = responsable
        self._start_date = start
        self._start_date_num = start
        self._due_date = due
        self._due_date_num = self.date2num(due)
        self._priority = priority
        self._estimated_time = est_hours         # Budget
        self._horas = 0                          # Ejecucion
        self._avance = self.avance()
        self._completed = self.completed()
        
    def date2num(self, fecha):
        """
        Convierte una fecha en formato (día, mes, año) a un número entero que representa la cantidad de días
        desde el inicio del calendario utilizado por esta clase.

        Argumentos:
            fecha (tuple): La fecha en formato (día, mes, año) a convertir.

        Retorna:
            int: El número de días desde el inicio del calendario hasta la fecha dada.
        """
        
        def __bisiesto(anyo):
            """
            Determina si un año es bisiesto o no.

            Argumentos:
                anyo (int): El año a verificar.

            Retorna:
                int: 1 si el año es bisiesto, 0 en caso contrario.
            """
            if anyo % 400 == 0:
                salida = 1
            elif anyo % 100 == 0:
                salida = 0
            elif anyo % 4 == 0:
                salida = 1
            else:
                salida = 0
            return salida
            
        diasxmes=[31,28,31,30,31,30,31,31,30,31,30,31]
        dia=fecha[0]
        mes=fecha[1]
        anyo=fecha[2]
        numero = 0
        for anio in range(1,anyo):
            numero+=365+__bisiesto(anio)
        for mez in range(1,mes):
            numero+= diasxmes[mez-1]
            if (mez==2): numero+=__bisiesto(anyo)
        numero += dia    
        return numero
    
    def change_priority(self):
        """
        Permite al usuario cambiar la prioridad de la tarea actual.
        El usuario debe ingresar el nuevo valor de prioridad.
        """
        aux = ['baja', 'media', 'alta']
        self._priority = aux[int(input("Ingrese la nueva prioridad (0=baja, 1=media, 2=alta):"))]

    def daystodue(self):
        """
        Calcula los días restantes hasta la fecha límite de la tarea.

        Retorna:
            int: Los días restantes hasta la fecha límite de la tarea.
        """
        from datetime import date
        today = date.today()
        return self._due_date_num - self.date2num((today.day, today.month, today.year))

    def daysfromstart(self):
        """
        Calcula los días transcurridos desde la fecha de inicio de la tarea.

        Retorna:
            int: Los días transcurridos desde la fecha de inicio de la tarea.
        """
        from datetime import date
        today = date.today()
        return self.date2num((today.day, today.month, today.year)) - self.date2num(self._start_date)

    def avance(self):
        """
        Calcula el avance de la tarea en función de las horas trabajadas y las horas estimadas.

        Retorna:
            float: El porcentaje de avance de la tarea.
        """
        return self._horas / self._estimated_time

    def myprint(self):
        """
        Imprime los detalles de la tarea, incluyendo nombre, responsable, prioridad, fechas, horas estimadas y trabajadas,
        avance y horas restantes.
        """
        print('')
        print('Tarea             : ', self._taskname)
        print('Responsable       : ', self._responsable)
        print('Prioridad         : ',self._priority)
        
        print('Fecha de Inicio   : ',self._start_date)
        print('Fecha de Final    : ', self._due_date)
        print('Dias desde inicio : ',self.daysfromstart())
        print('Dias al due date  : ',self.daystodue())
        
        
        print('Horas Proyectadas : ',self._estimated_time)
        print('Horas Ejecutadas  : ',self._horas)
        print('Avance            : ',self._avance)
        print('Horas restantes   : ',self._estimated_time*(1-self._avance))
        print('')

        return None
    def add_hours(self, hours):
        """
        Añade horas trabajadas a la tarea.

        Argumentos:
            hours (int): Las horas a añadir a las horas ya trabajadas en la tarea.
        """
        if self._horas + hours <= self._estimated_time: 
            self._horas += hours
            self._avance = self.avance()
            self._completed = self.completed()

    def completed(self):
        """
        Verifica si la tarea ha sido completada.

        Retorna:
            int: 0 si la tarea no está completada, 1 si está completada.
        """
        return 0 if self._horas < self._estimated_time else 1


#%%

tp1_matematica = task(name = 'TP1 Mate', 
                      responsable = 'Facundo Kuzis', 
                      start=(9,3,2024), 
                      due=(18, 3, 2024), 
                      priority='high', 
                      est_hours = 5)

parcial_estadistica = task(name = 'Parcial Estadística', 
                      responsable = 'Facundo Kuzis', 
                      start=(20,4,2024), 
                      due=(25, 4, 2024), 
                      priority='med', 
                      est_hours = 15)

my_task_manager = taskmanager([tp1_matematica, parcial_estadistica])

my_task_manager.pending()

my_task_manager.past_due()

#%%
my_task_manager.add_task()


    
#%% Necesitamos colgar las funciones de fechas para poder hacer que la fecha de fin sea mayor que la de inicio

def bisiesto(anyo):
    if (anyo%400 ==0):
        salida = 1
    elif (anyo%100 ==0):
        salida = 0
    elif (anyo%4 ==0):
        salida = 1
    else:
        salida=0
    return salida

def date2num(fecha):
            
    diasxmes=[31,28,31,30,31,30,31,31,30,31,30,31]
    dia=fecha[0]
    mes=fecha[1]
    anyo=fecha[2]
    numero = 0
    for anio in range(1,anyo):
        numero+=365+bisiesto(anio)
    for mez in range(1,mes):
        numero+= diasxmes[mez-1]
        if (mez==2): numero+=bisiesto(anyo)
    numero += dia    
    return numero

def num2date(numero):
    
    diasxmes=[31,28,31,30,31,30,31,31,30,31,30,31]
    
    counter=0
    anio = 1
    newcounter = counter+365+bisiesto(anio)  
    while (newcounter<numero):
        counter+= 365+bisiesto(anio)
        anio +=1
        newcounter = counter+365+bisiesto(anio)  

    mez = 1
    newcounter = counter + diasxmes[mez-1]
    while (newcounter<numero):
        counter+= diasxmes[mez-1]
        if (mez==2): counter+=bisiesto(anio)
        mez +=1
        newcounter = counter+diasxmes[mez-1]   
        if (mez==2): newcounter+=bisiesto(anio)

    dia = numero - counter
     
    salida = (dia,mez,anio)
  
    return salida

if __name__ == "__main__" :
    
    import random as rndm
    
    Nombres = ['Gabriel', 'Lucas','Francesca','Federico','Ezequiel','Facundo','Santiago']
    Apellidos = ['Basaluzzo','Castiglione','Paruolo','Harari','Kuzis','Kestler']
    
    Materias = ['F210-Progra','F324-Derivados','A451-Mercados Capitales','F311-POMA','F337-Mate Aplicada']
    Trabajito = ['TP1','TP2','TP3','Presentacion','EXAMEN PARCIAL','EXAMEN FINAL']
        
    Ntareas = 100
    
    DESDEN = date2num((1,1,2024))
    HASTAN = date2num((31,12,2024))
    
    b = taskmanager()

    for j in range(Ntareas):
        who = rndm.sample(Nombres,k=1)[0]+' '+ rndm.sample(Apellidos,k=1)[0]
        what = rndm.sample(Trabajito,k=1)[0]+'-'+ rndm.sample(Materias,k=1)[0] 
        
        desde_n = rndm.sample(range(DESDEN,HASTAN),k=1)[0]
        desde = num2date(desde_n)
        hasta_n = rndm.sample(range(desde_n+1,HASTAN+1),k=1)[0]
        hasta=num2date(hasta_n)
        
        horas_proyectadas = rndm.sample(list(range(1,101)),k=1)[0]
        horas_ejecutadas =rndm.sample(list(range(horas_proyectadas)),k=1)[0]
        
        prioridad = rndm.sample(['low','med','high'],k=1)[0]
                
        a = task(name=what,responsable=who,start=desde,due=hasta,est_hours=horas_proyectadas,priority=prioridad)
        a.add_hours(horas_ejecutadas)
        a.myprint()
        b.add_task(tarea=a)
        
        