

class Row:
    
    def __init__(self,V=None,h=None,data=None,key=None):
        self.key = key
        self.V = V
        self.h = h
        self.C: int = 0 # Произошла ли коллизия
        self.U: int = 1 if V else 0 # Занята ли 
        self.T: int = 0 # Конечная ли эта запись в цепочке записей
        self.L: int = 0 # В поле Pi данные или только указатель (0 = данные)
        self.D: int = 0 # Запись удалена
        self.P0: int = None # Следующая запись в цепочке
        self.Pi: str = data
        
    def __str__(self):
        return f'V:{self.V},h:{self.h},U:{self.U},Pi:{self.Pi}'