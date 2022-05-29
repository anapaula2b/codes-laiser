from email.headerregistry import ContentTypeHeader
from multiprocessing.spawn import old_main_modules
from pickle import TRUE
import socket
import keyboard
import threading
import socket
import select
import time
import pyautogui
import tkinter as tk
import pygame, sys, random, pyautogui, keyboard
from pygame.locals import *
from tkinter import LEFT, Button, Entry, Radiobutton, Frame, Label, Tk
import os
# from PIL import Image, ImageSequencea
import keyboard
from pynput.mouse import Controller
from time import sleep
import threading
    
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)









def protecaoDeTela(status): 

    if status == True:    
        pygame.init()
        clok = pygame.time.Clock()
        pygame.display.set_caption('Fireworks')
        largura, altura = pyautogui.size()
        screen = pygame.display.set_mode((400, 400),0,32)

       

        pygame.mouse.set_visible(False)

        screen.fill((00,80,00))
        for event in pygame.event.get():
            if event.type == QUIT:
                pass
        pygame.display.update()

    if status == False: 
        print('Proteção de tela desativada.')
        pygame.quit()
        
    
# def enviaDados(udp_socket, dest_ip, dest_port):
    
#     while True:

#         send_data = input(" please enter a message to send: ")

#         udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recebeDados(udp_socket,): # mostra na tela os dados recebidos
    
    """ receive data """
    recv_data = udp_socket.recvfrom(1024)
    
    dadosRecebidos = recv_data[0].decode("utf-8")

    pygame.init()
    clok = pygame.time.Clock()
    pygame.display.set_caption('Fireworks')
    largura, altura = pyautogui.size()
    screen = pygame.display.set_mode((400, 400),0,32)

    keys = pygame.key.get_pressed()

    

    pygame.mouse.set_visible(False)

    screen.fill((00,80,00))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    gameloop = True

    while gameloop:
        pygame.display.update()

        recv_data = udp_socket.recvfrom(1024)
        
        dadosRecebidos = recv_data[0].decode("utf-8")

        if dadosRecebidos == 'False':
            pygame.quit()

    while True:
        recv_data = udp_socket.recvfrom(1024)
        
        dadosRecebidos = recv_data[0].decode("utf-8")

        print(f'Dados recebidos: {dadosRecebidos}')
  

        if dadosRecebidos == 'True': 
            print(f'Mensagem recebida: {dadosRecebidos}')
            protecaoDeTela(True) #ativa a proteção de tela
            # deixarMouseDoidao(True)

        if dadosRecebidos == 'False':
            print(f'Mensagem recebida: {dadosRecebidos}')
            protecaoDeTela(False) #desativa a proteção de tela
            # deixarMouseDoidao(False)


        if dadosRecebidos == 'des':
            print(f'Mensagem recebida: {dadosRecebidos}')
            os.system("shutdown /s /t 1") #desliga o pc

        if dadosRecebidos == 'rein':
            print(f'Mensagem recebida: {dadosRecebidos}')
            os.system("shutdown /r /t 1") #reinicia o pc

        


def main():
   
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
    udp_socket.bind(("", 7788))

  
    dest_ip = '10.15.130.18'
    dest_port = 7788



    # ts = threading.Thread(target=enviaDados, args=(udp_socket, dest_ip, dest_port))
    tr = threading.Thread(target=recebeDados, args=(udp_socket,))

    # ts.start()
    tr.start()




if __name__ == "__main__":
    main()