from Table import Table
import unittest

if __name__ == "__main__":
    a=Table()
    a['Moskow'] = "1"
    a['Mozir'] = '2'
    a['Mogilev'] = '3'
    a['Molodechno'] = '4'
    print(a)
    del a['Mogilev']
    a['Minsk'] = "Capital"
    a['Moba'] = '5'
    print(a)