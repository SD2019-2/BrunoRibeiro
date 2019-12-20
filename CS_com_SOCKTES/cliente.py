

import socket, string
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
porta = 12345

server.connect((ip,porta))
print("Conectado! Para sair digite exit")
print ("Digite seu nome")

nome = input()

server.send(nome.encode('utf-8'))

while True:
	mensagem = input()
	
	if(mensagem == 'exit'):
		break

	server.send(mensagem.encode('utf-8'))
	print("Mensagem enviada!")


server.close()
