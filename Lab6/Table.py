from Row import Row
from constants import *

class Table:
    
    def __init__(self):
        self.keys = set([])
        self.values = [Row()]*SIZE
        
    def get_hash(self,key):    
        V = 0
        for i in range(len(key[:2])):
            index = ALPHABET.find(key[i])
            V+=index**i
            
        return V,V%SIZE
        
    def check_if_full(self):
        return len(self.keys)==SIZE
        
    def add(self,key,info):
        if not self.check_if_full():
            V,h = self.get_hash(key)
            while self.values[h].U and not self.values[h].D:
                h = (h+1)%SIZE
            self.values[h] = Row(V,h,info,key)
            self.keys.add(key)
            
    def get(self,key):
        if key not in self.keys:
            raise KeyError
        
        V,h = self.get_hash(key)
        
        while not self.values[h].key == key:
            h = (h+1)%SIZE
        
        return self.values[h].Pi
    
    def delete(self,key):
        V,h = self.get_hash(key)
        
        if V in self.keys:
            raise KeyError
        
        while not self.values[h].key == key:
            h = (h+1)%SIZE
            
        self.values[h].D = 1
        self.keys.remove(key)
        
    def update(self,key,value):
        V,h = self.get_hash(key)
        
        while self.values[h].key != key:
            h = (h+1)%SIZE
            
        self.values[h].Pi = value
        
        
    
    def __getitem__(self,key):
        return self.get(key)
        
    
    def __setitem__(self, key, value):
        if key in self.keys:
            self.update(key,value)
            
        else: self.add(key,value)
    
    def __str__(self):
        res = ""
        for i in range(len(self.values)):
            res+=f'Строка: [{i}]: {str(self.values[i])}\n'
        return res
    
    def __delitem__(self,key):
        self.delete(key)