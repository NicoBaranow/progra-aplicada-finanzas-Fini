import datetime
import keyboard

class Clock(object):
    def __init__(self, hour=0, minute=0, second=0, is_24_hour=True, am_pm='AM'):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.is_24_hour = is_24_hour
        self.am_pm = am_pm

    def onesec(self):
        N = 40000000  
        for _ in range(N):
            pass  # No hace nada, solo consume tiempo

    def update(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.is_24_hour:
                    if self.hour == 24:
                        self.hour = 0
                else:
                    if self.hour == 13:
                        self.hour = 1
                    elif self.hour == 12:
                        self.am_pm = 'PM' if self.am_pm == 'AM' else 'AM'
                        

    def printCurrentTime(self):
        # Obtiene la hora actual del sistema
        now = datetime.datetime.now()

        # Formatea la hora del reloj
        clock_time = f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
        if not self.is_24_hour:
            clock_time += f' {self.am_pm}'

        # Formatea la hora actual del sistema
        system_time = now.strftime('%H:%M:%S')

        # Compara y muestra ambos tiempos
        print(f'The current time is: {clock_time}')
        print(f'The system time is: {system_time}')

    def setClock(self, time_tuple=None):
        if time_tuple is None:
            now = datetime.datetime.now()
            self.hour, self.minute, self.second = now.hour, now.minute, now.second
        else:
            self.hour, self.minute, self.second = time_tuple

    def work(self, time_tuple=None):
        self.setClock(time_tuple)
        try:
            while True:
                self.onesec()
                self.update()
                if keyboard.is_pressed('p'):
                    self.printCurrentTime()
                elif keyboard.is_pressed('q'):
                    print("Clock stopped.")
                    break
        except KeyboardInterrupt:
            print("Clock stopped by user.")

# Ejemplo de uso
clock = Clock()
clock.work()

#%%

class Cronometro(Clock):
    def __init__(self):
        super().__init__()
        self.start_time = datetime.datetime.now()
        self.lap_times = []

    def update(self):
        now = datetime.datetime.now()
        self.total_time = now - self.start_time
        if self.lap_times:
            self.lap_time = now - self.lap_times[-1]
        else:
            self.lap_time = self.total_time

    def printCurrentTime(self):
        print(f'Lap time: {self.lap_time}')
        print(f'Total time: {self.total_time}')

    def work(self):
        self.start_time = datetime.datetime.now()
        try:
            while True:
                self.onesec()
                self.update()
                if keyboard.is_pressed('p'):
                    self.printCurrentTime()
                    self.lap_times.append(datetime.datetime.now())
                elif keyboard.is_pressed('q'):
                    self.printCurrentTime()
                    print("Cronometro stopped.")
                    break
        except KeyboardInterrupt:
            print("Cronometro stopped by user.")


cronometro = Cronometro()
cronometro.work()

#%%

class Temporizador(Clock):
    def __init__(self, time_tuple):
        super().__init__(*time_tuple)
        self.start_time = datetime.datetime.now()
        self.end_time = self.start_time + datetime.timedelta(hours=time_tuple[0], minutes=time_tuple[1], seconds=time_tuple[2])

    def update(self):
        now = datetime.datetime.now()
        self.remaining_time = self.end_time - now
        if self.remaining_time.total_seconds() <= 0:
            self.remaining_time = datetime.timedelta(0)

    def printCurrentTime(self):
        elapsed_time = datetime.datetime.now() - self.start_time
        print(f'Elapsed time: {elapsed_time}')
        print(f'Remaining time: {self.remaining_time}')

    def work(self):
        try:
            while True:
                self.onesec()
                self.update()
                if keyboard.is_pressed('p'):
                    self.printCurrentTime()
                elif keyboard.is_pressed('q'):
                    self.printCurrentTime()
                    print("Temporizador stopped.")
                    break
                if self.remaining_time.total_seconds() <= 0:
                    print("Time's up!")
                    break
        except KeyboardInterrupt:
            print("Temporizador stopped by user.")


temporizador = Temporizador((0, 1, 0))  # 1 minuto
temporizador.work()

