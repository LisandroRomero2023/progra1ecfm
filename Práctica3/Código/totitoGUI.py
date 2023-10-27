import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from totitoJugador import Jugador
from totitoTablero import Tablero

#####################################################################################################################################################################################################################################################################33


class InterfazTotito():
    def __init__(self):
        self.ventanaInit = tk.Tk()
        self.canvas1=tk.Canvas(self.ventanaInit, width = 400, height=400, bg="gray")
        self.canvas1.grid(column=0, row=1)
        self.entradadatos()
        self.entrada1= None
        self.posicion1=None
        self.entrada2= None
        self.posicion2=None
        self.vict = False
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
    
    def deshabilitar(self, objeto):
        try:
            objeto.config(state='disable')
        except AttributeError:
            pass
    
    def habilitar(self, objeto):
        objeto.config(state='able')
    
    def validacionJuego(self):
        try:
            self.jugadores = int(self.dato1.get())
            if self.jugadores == 1:
                self.deshabilitar(self.entry1)
                self.deshabilitar(self.boton1)
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
                self.deshabilitar(self.entry1)
                self.deshabilitar(self.boton1)
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
                self.entry3.focus()
            
        except ValueError:
            self.dato1.set("Introduzca un valor entero")
    
    def tablero(self):
        self.canvas1.create_rectangle(50,50,350,350)
        self.canvas1.create_line(150,50,150,350)
        self.canvas1.create_line(250,50,250,350)
        self.canvas1.create_line(50,150,350,150)
        self.canvas1.create_line(50,250,350,250)
        self.definicionesPrevias()
    
    def posicion1(self):
        return print(self.jugadaJg1.get())
    
    def posicion2(self):
        return print(self.jugadaJg2.get())
    
    def preparacionEntradas(self, jugador1, jugador2):
        self.frameJg1 = ttk.LabelFrame(self.ventanaInit, text="Jugadas de {name}".format(name=self.jugador1.getNombre()))
        self.frameJg1.grid(column=1, row=0, padx=5, pady=5)
        self.peticionJg1 = ttk.Label(self.frameJg1, text="Formato columna fila separados por un espacio")
        self.peticionJg1.grid(column=0, row=0, padx=5, pady=5)
        
        self.jugadaJg1 = tk.StringVar()
        self.entradaJg1 = ttk.Entry(self.frameJg1, textvariable=self.jugadaJg1)
        self.entradaJg1.grid(column=0, row=1, padx=5, pady=5)
        
        self.botonJg1 = ttk.Button(self.frameJg1, text="Realizado", command=self.capturar1)
        self.botonJg1.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
        self.entradaJg1.focus()
        
        self.frameJg2 = ttk.LabelFrame(self.ventanaInit, text="Jugadas de {name}".format(name=self.jugador2.getNombre()))
        self.frameJg2.grid(column=1, row=1, padx=5, pady=5)
        self.peticionJg2 = ttk.Label(self.frameJg2, text="Formato columna fila separados por un espacio")
        self.peticionJg2.grid(column=0, row=0, padx=5, pady=5)
        
        self.jugadaJg2 = tk.StringVar()
        self.entradaJg2 = ttk.Entry(self.frameJg2, textvariable=self.jugadaJg2)
        self.entradaJg2.grid(column=0, row=1, padx=5, pady=5)
        
        self.botonJg2 = ttk.Button(self.frameJg2, text="Realizado", command=self.capturar2)
        self.botonJg2.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
        self.entradaJg2.focus()
        
        self.habilitar(self.entradaJg1)
        self.deshabilitar(self.entradaJg2)
        
    def preparacionEntradasCPU(self, jugador1, jugador2):
        self.frameJg1 = ttk.LabelFrame(self.ventanaInit, text="Jugadas de {name}".format(name=self.jugador1.getNombre()))
        self.frameJg1.grid(column=1, row=0, padx=5, pady=5)
        self.peticionJg1 = ttk.Label(self.frameJg1, text="Formato columna fila separados por un espacio")
        self.peticionJg1.grid(column=0, row=0, padx=5, pady=5)
        
        self.jugadaJg1 = tk.StringVar()
        self.entradaJg1 = ttk.Entry(self.frameJg1, textvariable=self.jugadaJg1)
        self.entradaJg1.grid(column=0, row=1, padx=5, pady=5)
        
        self.botonJg1 = ttk.Button(self.frameJg1, text="Realizado", command=self.capturar1)
        self.botonJg1.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
        self.entradaJg1.focus()
        
        self.frameJg2 = ttk.LabelFrame(self.ventanaInit, text="Jugadas de {name}".format(name=self.jugador2.getNombre()))
        self.frameJg2.grid(column=1, row=1, padx=5, pady=5)
        self.peticionJg2 = ttk.Label(self.frameJg2, text="Formato columna fila separados por un espacio")
        self.peticionJg2.grid(column=0, row=0, padx=5, pady=5)
        
        self.jugadaJg2 = tk.StringVar()
        self.entradaJg2 = ttk.Entry(self.frameJg2, textvariable=self.jugadaJg2)
        self.entradaJg2.grid(column=0, row=1, padx=5, pady=5)
        
        self.botonJg2 = ttk.Button(self.frameJg2, text="Realizado", command=self.capturarCPU)
        self.botonJg2.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
        self.entradaJg2.focus()
        
        self.habilitar(self.entradaJg1)
        self.deshabilitar(self.entradaJg2)
    
    def dibujarjugada(self, i, j, jugador):
        if self.vict == True or len(self.tab.posicionesLibres())==0:
            self.deshabilitar(self.entradaJg1)
            self.deshabilitar(self.entradaJg2)
        else:
            if jugador.getCaracter() == 'X':
                self.canvas1.create_line(i*100+60, j*100+60, i*100+140, j*100+140)
                self.canvas1.create_line(i*100+60, j*100+140, i*100+140, j*100+60)
                self.deshabilitar(self.entradaJg1)
                if self.jugador2.getNombre() == 'CPU':
                    self.deshabilitar(self.entradaJg2)
                else:
                    self.habilitar(self.entradaJg2)
            elif jugador.getCaracter() == 'O':
                self.canvas1.create_oval(i*100+60, j*100+60, i*100+140, j*100+140)
                self.habilitar(self.entradaJg1)
                self.deshabilitar(self.entradaJg2)
    
    
    def mostrarGanador(self):
        self.frameGanador = ttk.LabelFrame(self.ventanaInit, text="Victoria")
        self.frameGanador.grid(column=0, row=2, padx=5, pady=5)
        self.JugadorGanador = ttk.Label(self.frameGanador, text="")
        self.JugadorGanador.grid(column=0, row=0, padx=5, pady=5)
        if self.vict == False and len(self.tab.posicionesLibres()) == 0:
            self.JugadorGanador.config(text="Empate")
        elif self.vict==True:
            self.JugadorGanador.config(text="El ganador es {name}".format(name=self.tab.getGanador().getNombre()))
    
    def capturar1(self):
        self.vict = self.tab.victoria(self.jugador1, self.jugador2)
        self.mostrarGanador()
        if self.vict==True:
            self.deshabilitar(self.jugadaJg1)
        self.entrada1 = self.jugadaJg1.get().split(' ')
        self.posicion1 = [int(self.entrada1[0]), int(self.entrada1[1])]
        if self.tab.getPosiciones()[self.posicion1[0]-1][self.posicion1[1]-1] == ' ':
            self.tab.setPosicion(self.posicion1[0], self.posicion1[1], self.jugador1, self.jugador2)
            self.dibujarjugada(self.posicion1[0]-1, self.posicion1[1]-1, self.jugador1)
            self.vict = self.tab.victoria(self.jugador1, self.jugador2)
            self.mostrarGanador()
        else:
            self.jugadaJg1.set("Elija una posicion vacía.")
            self.jugador1.setAdvertencias(1)
    
    def capturar2(self):
        self.vict = self.tab.victoria(self.jugador1, self.jugador2)
        self.mostrarGanador()
        self.entrada2 = self.jugadaJg2.get().split(' ')
        self.posicion2 = [int(self.entrada2[0]), int(self.entrada2[1])]
        if self.tab.getPosiciones()[self.posicion2[0]-1][self.posicion2[1]-1] == ' ':
            self.tab.setPosicion(self.posicion2[0], self.posicion2[1], self.jugador2, self.jugador1)
            self.dibujarjugada(self.posicion2[0]-1, self.posicion2[1]-1, self.jugador2)
            self.vict = self.tab.victoria(self.jugador1, self.jugador2)
            self.mostrarGanador()
        else:
            self.jugadaJg2.set("Elija una posicion vacía.")
            self.jugador2.setAdvertencias(1)
        
    def capturarCPU(self):
        self.vict = self.tab.victoria(self.jugador1, self.jugador2)
        self.mostrarGanador()
        self.posiciones = self.tab.posicionesLibres()
        movRan = random.choice(self.posiciones)
        self.jugadaJg2.set('{p1} {p2}'.format(p1=movRan[0]+1, p2=movRan[1]+1))
        self.posicion2 = [movRan[0], movRan[1]]
        if self.tab.getPosiciones()[self.posicion2[0]][self.posicion2[1]] == ' ':
            self.tab.setPosicionCPU(self.posicion2[0], self.posicion2[1], self.jugador2)
            self.dibujarjugada(self.posicion2[0], self.posicion2[1], self.jugador2)
            self.vict = self.tab.victoria(self.jugador1, self.jugador2)
            self.mostrarGanador()
        else:
            self.jugadaJg2.set("Elija una posicion vacía.")
            self.jugador2.setAdvertencias(1)
    
    def definicionesPrevias(self):
        self.tab = Tablero()
        self.jugadores = int(self.dato1.get())
        if self.jugadores == 1:
            self.jugador1 = Jugador(self.dato2.get(), 'X')
            self.jugador2 = Jugador('CPU', 'O')
            self.preparacionEntradasCPU(self.jugador1, self.jugador2)
        elif self.jugadores == 2:
            self.jugador1 = Jugador(self.dato2.get(), 'X')
            self.jugador2 = Jugador(self.dato3.get(), 'O')
            self.preparacionEntradas(self.jugador1, self.jugador2)
    
    
    
    
    
    
app=InterfazTotito()
