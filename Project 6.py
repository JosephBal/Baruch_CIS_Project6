# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:12:07 2023

@author: Joseph Balbuena
"""
# oranges 65875
# converts symbol to NATO phonetic alphabet
def nato(symbol):
    if symbol == 'o' :
        return '---'
    elif symbol == 'r': 
        return '.-.'
    elif symbol == 'a' :
        return '.-'
    elif symbol == 'n' :
        return '-.'
    elif symbol == 'g' :
        return '--.'
    elif symbol == 'e' :
        return '.'
    elif symbol == 's' :
        return '...'    
    elif symbol == '6' :
        return '-....'
    elif symbol == '5' :
        return '.....'
    elif symbol == '8' :
        return '---..'
    elif symbol == '7' :
        return '--...'
    
    else:
        return None
    
    
    
### main body of my program ###

# translate Abc
output = nato('o') + ' ' + nato('r') + ' ' + nato('a') + ' ' + nato('n') + ' ' + nato('g') + ' ' + nato('e') + ' ' + nato('s') + ' ' + nato('6') + ' ' + nato('5') + ' ' + nato('8') + ' ' + nato('7') + ' ' + nato('5') 

# display result
print(output) 
