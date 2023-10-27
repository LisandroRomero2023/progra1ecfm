import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from totitoJugador import Jugador
from totitoTablero import Tablero

class InterfazTotito:
    def __init__(self):
        self.ventanaInit = tk.Tk()
        self.entradadatos()
        self.canvas1=tk.Canvas(self.ventanaInit, width = 600, height=600, bg="gray")
        self.canvas1.grid(column=0, row=1)
        self.marcoJugadas = tk.LabelFrame(self.ventanaInit, text="Jugada")
        self.marcoJugadas.grid(column=2, row=0, sticky="w")
        self.ventanaInit.mainloop()
    
    def entradadatos(self):
        # Marco de selección del tipo de juego
        self.titulo=ttk.LabelFrame(self.ventanaInit, text="Datos")
        self.titulo.grid(column=0, row=0, sticky="w")
        # Request para la información sobre cuántos jugadores habrá
        self.label1=ttk.Label(self.titulo, text="¿Jugarán 1 o 2 jugadores? Responda con el número de jugadores")
        self.label1.grid(column=0,row=0, padx=5, pady=5)
        
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.titulo, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        ## Boton para validacion de datos
        self.boton1=ttk.Button(self.titulo, text="Siguiente", command=self.validacionJuego)
        self.boton1.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky="we")
        self.entry1.focus()
    
    def desabilitarEntrada(self, entrada):
        entrada.config(state='disable')
    
    def validacionJuego(self):
        try:
            self.jugadores = int(self.dato1.get())
            if self.jugadores == 1:
                self.desabilitarEntrada(self.entry1)
                # Crea un segundo marco
                self.titulo2=ttk.LabelFrame(self.titulo, text="Nombre del jugador")
                self.titulo2.grid(column=0, row=1)
                # Request sobre el nombre del jugador y el estilo de juego de la máquina
                self.dato2=tk.StringVar()
                self.entry2=ttk.Entry(self.titulo2, textvariable=self.dato2) ## .config(state=disable)
                self.entry2.grid(column=1, row=1, padx=5, pady=5)
                # Botón para iniciar el juego
                self.boton2=ttk.Button(self.titulo2, text="Comenzar", command=self.tablero)
                self.boton2.grid(column=2, row=1, columnspan=2, padx=5, pady=5, sticky="we")
                self.entry2.focus()
            elif self.jugadores == 2:
                self.desabilitarEntrada(self.entry1)
                # Crea un segundo marco
                self.titulo2=ttk.LabelFrame(self.titulo, text="Jugadores")
                self.titulo2.grid(column=0, row=1)
                # Requeste con los nombres de los jugadores
                self.label2=ttk.Label(self.titulo2, text="Primer jugador")
                self.label2.grid(column=1, row=1, padx=5, pady=5)
                self.dato2=tk.StringVar()
                self.entry2=ttk.Entry(self.titulo2, textvariable=self.dato2)
                self.entry2.grid(column=1, row=2, padx=5, pady=5)
                self.label3=ttk.Label(self.titulo2, text="Segundo jugador")
                self.label3.grid(column=2, row=1, padx=5, pady=5)
                self.dato3=tk.StringVar()
                self.entry3=ttk.Entry(self.titulo2, textvariable=self.dato3)
                self.entry3.grid(column=2, row=2, padx=5, pady=5)
                # Botón para iniciar el juego
                self.boton2=ttk.Button(self.titulo2, text="Comenzar", command=self.tablero)
                self.boton2.grid(column=3, row=1, columnspan=2, padx=5, pady=5, sticky="we")
                self.entry2.focus()
                self.entry3.focus()
            
        except ValueError:
            self.dato1.set("Introduzca un valor entero")
    
    def tablero(self):
        self.canvas1.create_rectangle(150,150,450,450)
        self.canvas1.create_line(250,150,250,450)
        self.canvas1.create_line(350,150,350,450)
        self.canvas1.create_line(150,250,450,250)
        self.canvas1.create_line(150,350,450,350)
        self.definicionesPrevias()
    
##############################################################################################################################################################################################################################
    
    ## Sección donde se definen asuntos relevantes a la lógica del juego
    
    def imprimirGanador(self, tablero, victoria):
        if victoria == False:
            return print("Empate")
        else:
            return print("El ganador es", tablero.getGanador().getNombre())

    def advertencias(self, jugador1, jugador2, tablero):
        cont=0
        if jugador1.getAdvertencias()>2:
            tablero.setGanador(jugador2)
            cont +=1
            return True
        elif jugador2.getAdvertencias()>2:
            tablero.setGanador(jugador1)
            cont+=1
            return True
        if cont==0:
            return False

    def ganador(self, jugador1, jugador2, tablero):
        pos= tablero.getPosicionesGanadorasHor() + tablero.getPosicionesGanadorasVer() + tablero.getPosicionesGanadorasDia()
        cont= 0
        m1 = jugador1.getCaracter()
        m2 = jugador2.getCaracter()
        for i in pos:
            if i == [m1, m1, m1]:
                tablero.setGanador(jugador1)
                cont +=1
                return True
            elif i == [m2, m2, m2]:
                tablero.setGanador(jugador2)
                cont +=1
                return True
        if cont == 0:
            return False
    
    def victoria(self, jugador1, jugador2, tablero):
        if self.ganador(jugador1, jugador2, tablero) == True or self.advertencias(jugador1, jugador2, tablero) == True:
            return True
        else:
            return False
    
###########################################################################################################################################################################################################################
    
    ## Sección para cambiamos que necesita la base lógica para adapatarse a la base gráfica
    
    def jugadaGrafCPU(self, jugador1, jugador2, tablero):
        posiciones = tablero.posicionesLibres()
        posRandom = random.choice(posiciones)
        tablero.setPosicion(posRandom[0], posRandom[1], jugador1, jugador2)
        self.imprimirJugada(self.canvas1, posRandom[0], posRandom[1], jugador1)
    
    def definicionesPrevias(self):
        self.tab = Tablero()
        self.jugadores = int(self.dato1.get())
        if self.jugadores == 1:
            self.jugador1 = Jugador(self.dato2.get(), 'X')
            self.jugador2 = Jugador('CPU', 'O')
        elif self.jugadores == 2:
            self.jugador1 = Jugador(self.dato2.get(), 'X')
            self.jugador2 = Jugador(self.dato3.get(), 'O')
            self.juego1v1Graf(self.jugador1, self.jugador2, self.tab)
    
    
    def juego1v1Graf(self, jugador1, jugador2, tablero):
        vict = False
        for i in range(1,5):
            # Realizamos una jugada
            self.jugadaGraf(jugador1, jugador2, tablero)
            # Verificamos si hay un ganador
            vict = self.victoria(jugador1, jugador2, tablero)
            # Imprimimos el tablero
            if vict != False:
                break
            # Realizamos una jugada
            self.jugadaGraf(jugador2, jugador1, tablero)
            vict = self.victoria(jugador1, jugador2, tablero)
            if vict != 0:
                break
        if vict == False:
            self.jugadaGraf(jugador1, jugador2, tablero)
            vict = self.victoria(jugador1, jugador2, tablero)
        self.imprimirGanador(tablero, vict)
    
    
    def jugadaGraf(self, jugador1, jugador2, tablero):
        ## Petición de entrada
        self.label4=ttk.Label(self.marcoJugadas, text="Introduza su jugada {name}".format(name=jugador1.getNombre()))
        self.label4.grid(column=0, row=0, padx=5, pady=5)
        self.caracter=jugador1.getCaracter()
        ## Creación de la entrada
        self.datoJugada=tk.StringVar()
        self.entryJugada=ttk.Entry(self.marcoJugadas, textvariable=self.datoJugada)
        self.entryJugada.grid(column=1, row=0, padx=5, pady=5)
        self.temporal = self.datoJugada.get()
        print(self.datoJugada.get())
        ## Segunda petición
        self.label5=ttk.Label(self.marcoJugadas, text="Introduza su jugada {name}".format(name=jugador2.getNombre()))
        self.label5.grid(column=0, row=2, padx=5, pady=5)
        self.caracter=jugador2.getCaracter()
        ## Creación de la entrada
        self.datoJugada2=tk.StringVar()
        self.entryJugada2=ttk.Entry(self.marcoJugadas, textvariable=self.datoJugada2)
        self.entryJugada2.grid(column=1, row=2, padx=5, pady=5)
        self.temporal2 = self.datoJugada2.get()
        print(self.datoJugada2.get())
        
        ## Asignación de las variables
        self.botonjugada=ttk.Button(self.marcoJugadas, text="Realizar", command=self.dibujarjugadas)
        self.botonjugada.grid(column=0, row=4, columnspan=2, padx=5, pady=5, sticky="we")
        self.entryJugada.focus()
    
    def jugadaGrafRandom(self, jugador, tablero):
        pos = self.tab.posicionesLibres()
        print(pos)
        jugada = random.choice(pos)
        self.tab.getPosiciones()[jugada[0]][jugada[1]]=jugador.getCaracter()
        self.dibujar(jugada[0], jugada[1], jugador.getCaracter())
    
    
    def dibujarjugadas(self):
        temp1 = self.temporal.split(' ')
        print(temp1)
        temp2 = self.temporal2.split(' ')
        print(temp2)
        #self.tab.getPosiciones()[int(temp1[0])][int(temp1[1])] = 'X'
        #self.tab.getPosiciones()[int(temp2[0])][int(temp2[1])] = 'O'
        posiciones = self.tab.getPosiciones()
        for i in range(3):
            for j in range(3):
                if posiciones[i][j] == 'X':
                    self.canvas1.create_line(i*100+160, j*100+160, i*100+240, j*100+240)
                    self.canvas1.create_line(i*100+160, j*100+240, i*100+240, j*100+160)
                elif posiciones[i][j] == 'O':
                    self.canvas1.create_oval(i*100+160, j*100+160, i*100+240, j*100+240)
    
    
app=InterfazTotito()
