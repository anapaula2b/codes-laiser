from tkinter import *   
from tkinter import LEFT, Button, Label, Radiobutton, Frame, Entry, Tk
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import socket
#importar as libs
from multiprocessing.sharedctypes import Value
import socket
import threading
from distutils.cmd import Command
import socket
import _thread
import time
from turtle import width
import winsound
from tkinter import *   
from tkinter import LEFT, Button, Label, Radiobutton, Frame, Entry, Tk
from idlelib.tooltip import Hovertip 
import tkinter as tk
from tkinter import ttk
from datetime import datetime

from datetime import datetime



contador = 0
contador2 = 0
contador3 = 0

contador4 = 0
contador5 = 0
contador6 = 0

tempoH = 0
tempoM = [0,0,0,0,0,0]

#declarar as listas 

ip = ['']
pessoa = ['', '']
namePC1 = ['PC1']
IPs = ['']

# ---- Cronometro -----------
contar = ['False', 'False']
Tminutos = [0, 0]


def send_msg(udp_socket, dest_ip1, dest_ip2, dest_port):
    """ send a message """
    #  gets the content to send
    while True:
        send_data = input("please enter a message to send：")
        if send_data == 'Tempo':
            tempo = input("Tempo：")
            udp_socket.sendto(tempo.encode("utf-8"), (dest_ip1, dest_port))
            udp_socket.sendto(tempo.encode("utf-8"), (dest_ip2, dest_port))
    
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip1, dest_port))
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip2, dest_port))


def recv_msg(udp_socket,):
    """ receive data """
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print("\n got the message %s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main():
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. bind the native ip and port : if the first parameter is null, the local ip will be bound by default, and the second parameter is the port number 
	udp_socket.bind(("", 7788))
	# 3. specify the ip of the other party 
	dest_ip = '10.15.2.43'
	dest_port = 7788

	# 4. create a thread and run it ：args you need a tuple parameter 
	tk = threading.Thread(target=send_msg, args=(udp_socket, '10.15.2.43','10.15.2.96', dest_port))
	# ts = threading.Thread(target=send_msg, args=(udp_socket, , dest_port))
	tr = threading.Thread(target=recv_msg, args=(udp_socket,))
	tk.start()
	# ts.start()
	tr.start()
# funçao do cronometro
def iniciarCronometroPC(contador, minutos, pc, nome, comando):

	cont = [contador]
	mins = [minutos]
	pcs = [pc]
	name = [nome]
	def contaTempo():
		
		temporizador = '00:00'
		if contar[comando] == 'True':

			tempoTela2 = str(temporizador)
			m,s = map(int,tempoTela2.split(':'))
			
			m = int(mins[0])
			tempoM[comando] = mins[0]
			print(tempoM[comando])
			s = int(cont[0])

	

			if s == 00:
				mins[0] -= 1
				cont[0] = 59

			segundo = str(0) + str(s)
			minuto = str(0) + str(m)
		

			tempoTela2 = str(minuto[-2:]) + ':' + str(segundo[-2:])

			
			
			pcs[0]['text'] = f'{name[0]} \n {tempoTela2}'
			pcs[0].after(1000,contaTempo)
			
			if tempoTela2 == '00:00':
				
				msg = 'True'
				udp_socket.sendto(msg.encode("utf-8"), (ip[0], 7788)),
				contar[comando] = 'False'

			cont[0] -= 1

	contaTempo()

def pausarCronometroPC():
	if ip[0] == '10.15.2.96':
		contar[0] = 'False'
		
		

	if ip[0] == '10.15.2.43':
		contar[1] = 'False'

def continuarCronometroPC():
	
	global contador
	if ip[0] == '10.15.2.96':
		contar[0] = 'True'
		msg = "False"
		udp_socket.sendto(msg.encode("utf-8"), (ip[0], 7788))
		iniciarCronometroPC(contador, tempoM[0], pc1, pessoa[0], 0)
	
	if ip[0] == '10.15.2.43':
		contar[1] = 'True'
		msg = "False"
		udp_socket.sendto(msg.encode("utf-8"), (ip[0], 7788))
		iniciarCronometroPC(contador, tempoM[1], pc2, pessoa[1], 1)

def iniciarTempo():
	global contador
	def contagemTempo():
		print(ip[0])
		if ip[0] == '10.15.2.96':

			tempo1 = comboExample.get()
			print(tempo1)
			if tempo1 == '30 min':			
				Tminutos[0] = 1
			if tempo1 == '1h': 
				Tminutos[0] = 60
			if tempo1 == '1h 30 min': 
				Tminutos[0] = 90
			if tempo1 == '2h': 
				Tminutos[0] = 120
			
			msg = 'False'
			udp_socket.sendto(msg.encode("utf-8"), (ip[0], 7788))
			contar[0] = 'True'		
			iniciarCronometroPC(contador, Tminutos[0], pc1, pessoa[0], 0)
			
		
		if ip[0] == '10.15.2.43':


			Tminutos[1] = 0
			tempo2 = comboExample.get()
			print(tempo2)
			if tempo2 == '30 min': 
				Tminutos[1] = 30
			if tempo2 == '1h': 
				Tminutos[1] = 60
			if tempo2 == '1h 30 min': 
				Tminutos[1] = 90
			if tempo2 == '2h': 
				Tminutos[1] = 120

			msg = 'False'
			udp_socket.sendto(msg.encode("utf-8"), (ip[0], 7788))
				
			contar[1] = 'True'
			iniciarCronometroPC(contador, Tminutos[1], pc2, pessoa[1], 1)

	class Application:
		def __init__(self, master=None):
			self.fontePadrao = ("Arial", "10")
			self.primeiroContainer = Frame(master)
			self.primeiroContainer["pady"] = 10
			self.primeiroContainer.pack()

			self.segundoContainer = Frame(master)
			self.segundoContainer["padx"] = 20
			self.segundoContainer.pack()

			self.terceiroContainer = Frame(master)
			self.terceiroContainer["padx"] = 20
			self.terceiroContainer.pack()

			self.quartoContainer = Frame(master)
			self.quartoContainer["pady"] = 20
			self.quartoContainer.pack()

			self.titulo = Label(self.primeiroContainer, text="Registrar Matricula")
			self.titulo["font"] = ("Arial", "10", "bold")
			self.titulo.pack()

	#------------ Entrada do nome d@ alun@ ---------------------------------------------

			self.nomeLabel = Label(self.segundoContainer, text="Nome do Alun@", font=self.fontePadrao)
			self.nomeLabel.pack(side=LEFT)

			self.nome = Entry(self.segundoContainer)
			self.nome["width"] = 30
			self.nome["font"] = self.fontePadrao
			self.nome.pack(side=LEFT)

	#------------ Entrada da matricúla d@ alun@ -----------------------------------------

			self.matriculaLabel = Label(self.terceiroContainer, text="Matricula", font=self.fontePadrao)
			self.matriculaLabel.pack(side=LEFT)

			self.matricula = Entry(self.terceiroContainer)
			self.matricula["width"] = 30
			self.matricula["font"] = self.fontePadrao
			self.matricula.pack(side=LEFT)

			

			self.autenticar = Button(self.quartoContainer)
			self.autenticar["text"] = "Liberar"
			self.autenticar["font"] = ("Calibri", "8")
			self.autenticar["width"] = 12
			self.autenticar["command"] = self.verificaMatricula
			self.autenticar.pack()

			self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
			self.mensagem.pack()

		#Método verificar matricula
		def verificaMatricula(self):
			
			nome = self.nome.get()
			if ip[0] == '10.15.2.96':
				pessoa[0] = nome
			if ip[0] == '10.15.2.43':
				pessoa[1] = nome
			matricula = self.matricula.get()
			print(matricula)
			now = datetime.now()
			
			with open('registro.txt', 'a') as r:
				r.write(nome)
				r.write(f'\n')
				r.write(matricula)
				r.write(f'\n')
				r.write(str(now))
				r.write(f'\n')
				r.write(ip[0])
				r.write(f'\n')
				r.write(f'\n')
		
			contagemTempo()
			root.destroy()

	root = Tk()
	Application(root)
	root.mainloop()

def botaoPCprecionado():
	print(ident.get())
	if ident.get() ==  'pc1':
		ip[0] ='10.15.2.96'
	
	if ident.get() ==  'pc2':
		ip[0] ='10.15.2.43'
	
	print(ip[0])

app = tk.Tk()
app.geometry('600x400')

primeiroContainer = Frame()
primeiroContainer["pady"] = 10
primeiroContainer.pack()

segundoContainer = Frame()
segundoContainer["pady"] = 30
segundoContainer.pack()

terceiroContainer = Frame()
terceiroContainer["pady"] = 30
terceiroContainer.pack()

quartoContainer = Frame()
quartoContainer["pady"] = 30
quartoContainer.pack()
# radioValue = tk.IntVar()

comboExample = ttk.Combobox(primeiroContainer,values=[ "30 min", "1h", "1h 30 min","2h",], width=3)
comboExample.pack(ipadx=20, ipady=5, padx=5, pady=5,side=LEFT)

comboExample.current(1)

ident = StringVar()

pc1 = Radiobutton(segundoContainer, background='#d3d3d3', text='namePC1[0]', command=botaoPCprecionado, variable=ident, value='pc1', height=6,width=9, padx=20, indicatoron=0)
pc1.pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT)

pc2 = Radiobutton(segundoContainer, background='#d3d3d3', text=f'PC{2}', command=botaoPCprecionado, variable=ident, value='pc2', height=6,width=9, padx=20, indicatoron=0)
pc2.pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT)

pc3 = Radiobutton(segundoContainer, background='#d3d3d3', text=f'PC{3}', value={3}, height=6,width=9, padx=20, indicatoron=0)
pc3.pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT)

pc4 = Radiobutton(terceiroContainer,background='#d3d3d3',text=f'PC{5}', value={5}, height=6,width=9, padx=20, indicatoron=0)
pc4.pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT)

pc5 = Radiobutton(terceiroContainer,background='#d3d3d3',text=f'PC{6}', value={6}, height=6,width=9, padx=20, indicatoron=0)
pc5.pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT)

pc6 = Radiobutton(terceiroContainer,background='#d3d3d3',text=f'PC{7}', value={7}, height=6,width=9, padx=20, indicatoron=0)
pc6.pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT)


Button(primeiroContainer,text='Iniciar Tempo', command=iniciarTempo).pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT)
Button(primeiroContainer,text='Pausar', command=pausarCronometroPC).pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT )
Button(primeiroContainer,text='Continuar', command=continuarCronometroPC).pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT )
Button(primeiroContainer,text='Desbloquear').pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT)
Button(primeiroContainer,text='Bloquear').pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT )



# Button(primeiroContainer,text ='Adicionar Tempo').pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT)

# Button(primeiroContainer,text='Desligar', command=desligar).pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT)
# Button(primeiroContainer,text='Reiniciar',command=reiniciar).pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT) 



# teste = Label(terceiroContainer, text='0').pack(ipadx=20, ipady=5, padx=5, pady=5, side=LEFT)

app.mainloop()