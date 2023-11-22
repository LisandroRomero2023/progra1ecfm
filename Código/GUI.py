'''
Proyecto Final Programación Matemática 1
Segundo Semestre
Lisandro Romero
'''
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import gi

from ejemplo import Simulador

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gio, Gtk


def swap(A,i,j):
    if i != j:
        A[i], A[j] = A[j], A[i]

def bubblesort(A):
    if len(A) == 1:
        return
    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A

def mergesort(A, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A

def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A

def quicksort(A, start, end):
    if start >= end:
        return
    pivot = A[end]
    pivotIdx = start
    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)



class Ordenamientos:
    def bubbleSort(self, vector):
        permutation = True
        iteración = 0
        while permutation == True:
            permutation = False
            iteración = iteración + 1
            for actual in range(0, len(vector) - iteración):
                if vector[actual] > vector[actual + 1]:
                    permutation = True
                    # Intercambiamos los dos elementos
                    vector[actual], vector[actual + 1] = \
                    vector[actual + 1],vector[actual]
        return vector

    def mergeSort(self, lista):
        if len(lista) > 1:
            pm = len(lista)//2
            izquierda = lista[:pm]
            derecha = lista[pm:]
            self.mergeSort(izquierda)
            self.mergeSort(derecha)
        
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

    def quickSort(self, vector):
        if not vector:
            return []
        else:
            pivote = vector[-1]
            menor = [x for x in vector     if x <  pivote]
            mas_grande = [x for x in vector[:-1] if x >= pivote]
            return self.quickSort(menor) + [pivote] + self.quickSort(mas_grande)

class Handler():
    def __init__(self):
        self.archivo=None
        self.lista=[]
        self.vector=[]
        self.prom=[]
        self.tmpBub=0
        self.tmpMer=0
        self.tmpQui=0
        self.contBub=0
        self.contMer=0
        self.contQui=0
        
        self.cantiBub=0
        self.cantiMer=0
        self.cantiQui=0
        
        self.objetoOrdenador = Ordenamientos()
        
    def getLista(self):
        return self.lista
    
    def onAdvertencia0(self, *args, **kwargs):
        advertencia = Gtk.MessageDialog(
            transient_for= cons.get_object("ventanaInit") ,
            flags=0,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.OK,
            text="Advertencia",
        )
            
        advertencia.format_secondary_text("Debe subir un archivo al programa.")
        
        advertencia.run()
        advertencia.destroy()
    
    def onAdvertencia1(self, *args, **kwargs):
        advertencia = Gtk.MessageDialog(
            transient_for= cons.get_object("ventanaInit") ,
            flags=0,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.OK,
            text="Advertencia",
        )
            
        advertencia.format_secondary_text("Debe seleccionar al menos uno de los métodos de ordenamiento.")
        
        advertencia.run()
        advertencia.destroy()
    
    def onAdvertencia2(self, *args, **kwargs):
        advertencia = Gtk.MessageDialog(
            transient_for= cons.get_object("ventanaInit") ,
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Advertencia",
        )
            
        advertencia.format_secondary_text("Debe subir un archivo que contenga 5 o más archivos.")
        
        advertencia.run()
        advertencia.destroy()
    
    ## Callback() de la opción cargar archivo
    def onArchivoNuevo(self, *args, **new_kwargs):
        dialog = Gtk.FileChooserDialog(
            title="Por favor elija un archivo", parent=ventanaInit, action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            cons.get_object("etiqueta1").set_label("Su archivo fue guardado correctamente. Por favor, elija el método de ordenamiento")
            self.archivo=open("{valor:}".format(valor=dialog.get_filename()))
            self.getArchivo()
        elif response == Gtk.ResponseType.CANCEL:
            self.onAdvertencia0()
        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)
    
    def getArchivo(self):
        temporal = self.archivo.read().split(' ')
        for i in temporal:
            temp=i.split('\n')
            for j in temp:
                if j != '':
                    self.lista.append(j)
    
    ## Callback() de la opción Cerrar del menú
    def onQuit(self, *args):
        Gtk.main_quit()
    
    ## Callback() de la opción Generar estadísiticas
    def onGenerarEst(self, *args):
        if self.archivo != None:
            
            cons.get_object("cantidadBub").set_label("{var}".format(var=self.cantiBub))
            cons.get_object("cantidadMer").set_label("{var}".format(var=self.cantiMer))
            cons.get_object("cantidadQui").set_label("{var}".format(var=self.cantiQui))
            
            cons.get_object("tiempoBub").set_label("{var}".format(var=self.tmpBub))
            cons.get_object("tiempoMer").set_label("{var}".format(var=self.tmpMer))
            cons.get_object("tiempoQui").set_label("{var}".format(var=self.tmpQui))
            
            
            if self.contBub == 0:
                self.prom.append(0)
            else:
                self.prom.append(self.tmpBub/self.contBub)
            
            if self.contMer == 0:
                self.prom.append(0)
            else:
                self.prom.append(self.tmpMer/self.contMer)
                
            if self.contQui == 0:
                self.prom.append(0)
            else:
                self.prom.append(self.tmpQui/self.contQui)
            
            fig, ax = plt.subplots()
            ax.bar(['Bubble Sort', 'Merge Sort', 'Quick Sort'], self.prom)
            plt.show()
            
        else:
            cons.get_object("etiqueta1").set_label("Por favor, cargue un archivo primero.")
        
        
    ## Callback() de la opción Acerca de
    def onAbout(self, *args):
        about=Gtk.AboutDialog()
        about.show_all()
        about.set_program_name("Algoritmos para ordenar listas")
        about.set_version("0.1")
        about.set_copyright("(c) Lerl")
        about.set_comments("Este es un programa diseñado para proporcionar una simulación sobre cómo se realizan los tipos de ordenamientos según la lista y el tipo de ordenamiento seleccionado; así mismo ofrece una comparación en la eficiencia entre los distintos métodos implementados; siendo los mismos: ordenamiento de burbuja, ordenamiento de fusión y ordenamiento rápido.\n Python 3.9.2 \n GTK 3.0")
        
        about.run()
        about.destroy()
        
    
    ## Callback() de la opción Código fuente
    def onCodigo(self, *args, **kwargs):
        codigo = Gtk.AboutDialog()
        codigo.show_all()
        codigo.set_program_name("Código fuente")
        codigo.set_comments("A continuación encuentra el link al código fuente:")
        codigo.set_website_label("Enlace al código fuente")
        codigo.set_website("https://github.com/LisandroRomero2023/progra1ecfm/tree/3ace1d80547bb4bfd4d46e37c15ff6eb4cca3745/C%C3%B3digo")
        
        codigo.run()
        codigo.destroy()
        
        
    ## Callback() de la opción Simulación
    def obtenerTexto(self, vector):
        texto=''
        for i in range(len(vector)):
            texto+='{var:}    '.format(var=vector[i])
        return texto + '\n'
    
    def updage_fig(self, vector, rects, i):
        for rect, val in zip(rects, A):
            rect.set_height(val)

        i[0] += 1
        noOfOperations.set_text("No. of operations:"+str(i[0]))
        # timeTaken.set_text("Time taken:"+str(time.time()-start_time)[:4]+"sec")
        time_elapsed=(time.time()-start_time)
        time_elapsed=float("{0:.2f}".format(time_elapsed))
        time_elapsed=str(time_elapsed)
        timeTaken.set_text("Time taken:"+time_elapsed+" sec")
    
    def simulacionBubbleSort(self, vector):
        fig, ax = plt.subplots()
        ax.set_title("Bubble Sort")
        bar_rects= ax.bar(range(len(vector)), vector, align="edge")
        
        ax.set_xlim(0, len(vector))
        ax.set_ylim(0, int(1.2*len(vector)))
        
        noOfOperations = ax.text(0.02, 0.95, "", transform=ax.transAxes)
        timeTaken = ax.text(0.02, 0.91, "", transform=ax.transAxes)
        interval= ax.text(0.02, 0.87, "Interval duration:"+str(speedofSort)+"ms", transform=ax.transAxes)
        
        i = [0]
        
        startTime = time.time()
        
        
        anim = animation.FuncAnimation(fig, func=self.update_fig,
            fargs=(bar_rects, i), frames=generator, interval=speedofSort,
            repeat=False)
        plt.show()
        
    
    
    
    def onSimulacion(self, *args, **kwargs):
        if self.archivo == None:
            self.onAdvertencia0()
        else:
            ver1=cons.get_object("bubbleSort").get_active()
            ver2=cons.get_object("mergeSort").get_active()
            ver3=cons.get_object("quickSort").get_active()
            
            if len(self.lista) <5:
                self.onAdvertencia2()
            elif len(self.lista) == 5:
                m = 5
            elif len(self.lista) in range(6,20):
                z = random.choice(range(len(self.lista)-5))
                m= z+5
            elif len(self.lista)>20:
                m = random.choice(range(5, 20))
            ## m funciona como el acotador de cuántos elementos del archivo tomaremos
        
            if len(self.lista) == 5:
                k = 0
            elif len(self.lista) < 20:
                k = len(self.lista)-m
            else:
                k = len(self.lista)-m
        
            ## k actúa como la cota de la indexación que puede tomarse.
        
            if len(self.lista) == 5:
                l = 0
            elif len(self.lista) in range(6,21):
                l = random.choice(range(k))
            else:
                l = random.choice(range(k))
            ## l elige a partir de qué índice se toman los elementos.
        
            if ver1!= True and ver2!=True and ver3!=True:
                self.onAdvertencia1()
            else:
                self.sublista=self.lista[l:l+m]
                self.sublista1=self.lista[l:l+m]
                
                if ver1 == True: ## Simulación de la burbuja
                    
                    inicio0 = time.time()
                    
                    self.sublistaOrd=self.objetoOrdenador.bubbleSort(self.sublista)
                    
                    fin0 = time.time()
                    
                    self.tmpBub += fin0-inicio0
                    self.contBub += 1
                    self.cantiBub += len(self.sublistaOrd)
                    
                    self.objetoSimulador= Simulador(self.sublista1, 1)
                    self.objetoSimulador.preparacion()
                    
                    
                    if ver2 == True: ## Simulación de la fusión
                        inicio1 = time.time()
                    
                        self.sublistaOrd=self.objetoOrdenador.mergeSort(self.sublista)
                    
                        fin1 = time.time()
                        
                        self.tmpMer += fin1-inicio1
                        self.contMer += 1
                        self.cantiMer+= len(self.sublista)
                        
                        self.objetoSimulador= Simulador(self.sublista1, 2)
                        
                        
                    if ver3 == True: ## Simulación quick sort
                        inicio2 = time.time()
                    
                        self.sublistaOrd=self.objetoOrdenador.quickSort(self.sublista)
                    
                        fin2 = time.time()
                        
                        self.tmpQui += fin2-inicio2
                        self.contQui += 1
                        self.cantiQui += len(self.sublista)
                        
                        self.objetoSimulador= Simulador(self.sublista1, 3)
                        
                        
                elif ver2 == True:## simulación de la fusión
                    inicio3 = time.time()
                    
                    self.sublistaOrd=self.objetoOrdenador.mergeSort(self.sublista)
                    
                    fin3 = time.time()
                    
                    self.tmpMer += fin3-inicio3
                    self.contMer += 1
                    self.cantiMer += len(self.sublista)
                    
                    self.objetoSimulador= Simulador(self.sublista1, 2)
                    
                    
                    if ver3 == True: ##  Simulación quick sort
                        inicio4 = time.time()
                    
                        self.sublistaOrd=self.objetoOrdenador.quickSort(self.sublista)
                    
                        fin4 = time.time()
                    
                        self.tmpQui += fin4-inicio4
                        self.contQui += 1
                        self.cantiQui += len(self.sublista)
                        
                        self.objetoSimulador= Simulador(self.sublista1, 3)
                        
                        
                elif ver3 == True: ## simulación quicksort
                    inicio5 = time.time()
                    
                    self.sublistaOrd=self.objetoOrdenador.bubbleSort(self.sublista)
                    
                    fin5 = time.time()
                    
                    self.tmpQui += fin5-inicio5
                    self.contQui += 1
                    self.cantiQui += len(self.sublista)
                    
                    self.objetoSimulador= Simulador(self.sublista1, 3)
                    
    
cons = Gtk.Builder()
cons.add_from_file("apariencia.glade")
cons.connect_signals(Handler())

ventanaInit = cons.get_object("ventanaInit")
ventanaInit.connect("destroy", Gtk.main_quit)
ventanaInit.show_all()



Gtk.main()
