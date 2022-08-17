# Escreva um programa que conte o número de caracteres de uma string ( Exemplo: 'google.com' Resultado Esperado: {'o': 3,'g': 2,'.': 1,'e': 1,'l': 1,'m': 1,'c': 1} )
def removeDuplicates(frase):
    chars = []
    prev = None
 
    for c in frase:
        if prev != c:
            chars.append(c)
            prev = c
 
    return ''.join(chars)
 
 
if __name__ == '__main__':
 
    frase = 'google'
    
    
newlist = list(removeDuplicates(frase))
listcont = []

while len(frase) < max(frase):
    incluir = ('a')
    listcont.append(incluir)

print(listcont)
