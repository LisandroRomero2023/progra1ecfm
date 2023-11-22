class sorteo():
    def __init__(self):
        nombre = ''
    
    def mergeSort(lista):
    if len(lista) > 1:
        pm = len(lista)//2
        izquierda = lista[:pm]
        derecha = lista[pm:]
        mergeSort(izquierda)
        mergeSort(derecha)
        
        i=j=k=0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i+=1
            else:
                lista[k] = derecha[j]
                j+=1
            k+=1
                
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k+=1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j+=1
            k+=1
