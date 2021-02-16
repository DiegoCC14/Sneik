from pynput import keyboard as kb
import os , time , random

class MatrizNew():
		def __init__(self,filas,columnas):
				self.matriz = []
				for i in range(filas):
						self.matriz.append(['[ ]']*columnas)

		def mostrarMatriz(self):
				for x in range(len(self.matriz)):
					print("-",end="")
				print("")
				for x in range(len(self.matriz)-1,-1,-1):
						for i in range(len(self.matriz[0])):
								print(self.matriz[x][i],end=" ")
						print("")
				for x in range(len(self.matriz)):
					print("-",end="")
				print("")

class Tablero_Juego(MatrizNew):
	
	def __init__(self):
		MatrizNew.__init__(self,15,15) 
		self.vibora = Vibora() 
		self.comida = None
		self.Definiendo_Comida()

	def Movimiento_Usuario(self):
		#Movemos la cabeza hacia la derecha, las posiciones anteriores toman el de adelante de la lista

		print(self.vibora.direccion + '--- Puntos: ', self.vibora.puntuacion)
		if self.vibora.direccion == 'Derecha':
			self.Vivora_Moviendose(0,1)
		elif self.vibora.direccion == 'Izquerda':
			self.Vivora_Moviendose(0,-1)
		elif self.vibora.direccion == 'Norte':
			self.Vivora_Moviendose(1,0)
		else: 
			self.Vivora_Moviendose(-1,0)

	def Definiendo_Comida(self):
		x = random.randint(0,14)
		y = random.randint(0,14)
		while self.matriz[x][y] != '[ ]': #Creamos nueva comida
			x = random.randint(0,14)
			y = random.randint(0,14)
		self.comida = (x,y)

	def Vivora_Moviendose(self,filas,columnas): #FILAS indica que mueva en fila, DERECHA en derecha y solo eso

		#Verificamos que no exista colicion o fuera del tablero
			#Verificamos si comio algo
			#Pintamos el movimiento

		long_vibora = len(self.vibora.cuerpo_vibora)

		cola_vibora = self.vibora.cuerpo_vibora[long_vibora-1]
		
		self.vibora.posicion_cabeza = (self.vibora.posicion_cabeza[0]+filas,self.vibora.posicion_cabeza[1]+columnas)
		
		if self.vibora.posicion_cabeza[0] < 0 or self.vibora.posicion_cabeza[0] > 15 or self.vibora.posicion_cabeza[1] < 0 or self.vibora.posicion_cabeza[1] > 15:
			int('error aproposito')
		elif self.matriz[self.vibora.posicion_cabeza[0]][self.vibora.posicion_cabeza[1]] == '[▅]':
			int('error aproposito')
		elif self.vibora.posicion_cabeza == self.comida:

			self.vibora.cuerpo_vibora.append(self.comida)
			self.vibora.puntuacion += 1
			self.Definiendo_Comida()

		for x in range(long_vibora-1,0,-1):
			self.vibora.cuerpo_vibora[x] = self.vibora.cuerpo_vibora[x-1]
		
		self.vibora.cuerpo_vibora[0] = self.vibora.posicion_cabeza #Ponemos la posicion a la cabeza
		
		self.Dibijando_vibora_tablero(cola_vibora)


	def Dibijando_vibora_tablero(self,cola_vibora):
		if self.matriz[self.comida[0]][self.comida[1]] != '[C]': 
			self.matriz[self.comida[0]][self.comida[1]] = '[C]' #Dibuja Comida
		
		for part in self.vibora.cuerpo_vibora:
			self.matriz[part[0]][part[1]] = '[▅]'
		
		self.matriz[cola_vibora[0]][cola_vibora[1]] = '[ ]'
		
class Vibora():
	def __init__(self):
		self.posicion_cabeza = (7,7) #Tupla que indica la posicion de la cabeza
		self.cuerpo_vibora = [self.posicion_cabeza] 
		#Cuando coma la lista crece y solo contiene posciones del cuerpo de la vibora
		self.puntuacion = 1
		self.direccion = 'Derecha' #Camina hacia la derecha

	def cambio_direccion(self,direccion): #Cambiamos la direccion de la vibora
		
		direccion = str(direccion)

		if direccion == 'Key.left' and self.direccion != 'Derecha': 
			self.direccion = 'Izquerda'
		elif direccion == 'Key.up' and self.direccion != 'Sur':
			self.direccion = 'Norte'
		elif direccion == 'Key.right' and self.direccion != 'Izquerda':
			self.direccion = 'Derecha'
		elif direccion == 'Key.down' and self.direccion != 'Norte':
			self.direccion = 'Sur'
		



try:

	Juego_Terminado = True
	Tablero_Juego = Tablero_Juego() #Generamos el tablero y introducimos la vibora en el tablero

	with kb.Listener(Tablero_Juego.vibora.cambio_direccion) as keyboart:
		
		while Juego_Terminado:

			Tablero_Juego.mostrarMatriz() # Mostramos la matriz
			Tablero_Juego.Movimiento_Usuario()

			time.sleep(0.3)
			
			if os.name=='posix': #Borramos la terminal o consola 
		 		os.system('clear')
			else: #Window
				os.system('cls')
			
except :
	print('===============')
	print('Juego Terminado')
	print('Puntuacion Final: ', Tablero_Juego.vibora.puntuacion)
	print('===============')

