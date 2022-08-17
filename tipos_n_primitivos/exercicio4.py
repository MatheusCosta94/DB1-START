# Escreva um programa que conte o número de caracteres de uma string ( Exemplo: 'google.com' Resultado Esperado: {'o': 3,'g': 2,'.': 1,'e': 1,'l': 1,'m': 1,'c': 1} )
def removeDuplicates(s):
    chars = []
    prev = None
 
    for c in s:
        if prev != c:
            chars.append(c)
            prev = c
 
    return ''.join(chars)
 
 
if __name__ == '__main__':
 
    s = 'google'
    
    
newlist = list(removeDuplicates(s))

for i in (newlist)
    i = 

print(newlist[0])
