from tkinter import *  
from tkinter import messagebox  
from math import sqrt  
import re  

def cleaner(): #Función que limpia los cuadros de entrada
	volt.set("")
	corriente.set("")
	resistencia.set("")
	potencia.set("")

def scien(num):

	try:

		patron = r'[+-]?\d*\.?\d+'
		num = str(num)	
		if 'K' in num or 'k' in num:	
			num = re.findall(patron, num)
			num = float(num[0])*1E3
		elif 'M' in num:
			num = re.findall(patron, num)
			num = float(num[0])*1E6
		elif 'G' in num:
			num = re.findall(patron, num)	
			num = float(num[0])*1E9
		elif 'm' in num:	
			num = re.findall(patron, num)	
			num = float(num[0])*1E-3
		elif 'u' in num or 'µ' in num:	
			num = re.findall(patron, num)	
			num = float(num[0])*1E-6
		elif 'n' in num:	
			num = re.findall(patron, num)	
			num = float(num[0])*1E-9
		elif 'p' in num:	
			num = re.findall(patron, num)	
			num = float(num[0])*1E-12
		else:
			num = float(num)

		return num

	except ValueError:		
		return str(num)

def notacion(val,opc): #Función que da la magnitud y notación científica de la magnitud
	change = False
	val = scien(val)
	if val < 0:
		val *= -1

	if opc == 1:
		fisc = "V"
	elif opc == 2:
		fisc = "A"
	elif opc == 3:
		fisc = " Ω"
	elif opc == 4:
		fisc = "W"

	if val < 1:
		change = True
		if val >= 1E-3:
			val = val*1000	
			if (val % 10) == 0 or val == 1:
				enot = str("  " + str(int(val)))
				enot += " m"
			else:	
				enot = str("  " + str(round(val,3)))
				enot += " m"
		elif val >= 1E-6:
			val = val*1000000	
			if (val % 10) == 0 or val == 1:
				enot = str("  " + str(int(val)))
				enot += " µ"
			else:	
				enot = str("  " + str(round(val,3)))
				enot += " µ"
		elif val >= 1E-9:
			val = val*1000000000	
			if (val % 10) == 0 or val == 1:
				enot = str("  " + str(int(val)))
				enot += " n"
			else:	
				enot = str("  " + str(round(val,3)))
				enot += " n"
		elif val >= 1E-12:
			val = val*1000000000000	
			if (val % 10) == 0 or val == 1:
				enot = str("  " + str(int(val)))
				enot += " p"
			else:	
				enot = str("  " + str(round(val,3)))
				enot += " p"

	if val >= 1000 and not(change):
		change = True
		if val >= 1000 and val < 1000000:
			val = val/1000	
			if (val % 10) == 0 or val == 1:
				enot = str("  " + str(int(val)))
				enot += " k"
			else:	
				enot = str("  " + str(round(val,3)))
				enot += " k"
		elif val >= 100000 and val < 1000000000:
			val = val/1000000
			if (val % 10) == 0 or val == 1:
				enot = str("  " + str(int(val)))
				enot += " M"
			else:
				enot = str("  " + str(round(val,3)))
				enot += " M"
		elif val >= 1000000000 and val < 1000000000000:
			val = val/1000000
			if (val % 10) == 0 or val == 1:
				enot = str("  " + str(int(val)))
				enot += " G"
			else:
				enot = str("  " + str(round(val,3)))
				enot += " G"
	
	if val >= 1 and val < 1000 and not(change):
		if (val % 10) == 0 or val == 1:
			val = int(val) 
			enot = str(val)  + " " 
		else:
			val = round(val,3) 
			enot = str(val) + " "
	
	enot += fisc
	return enot


def leyohm(v,i,r,p): #Cálculos de la ley de Ohm
	if "-" in v or "-"in i or "-" in r or "-" in p: #Si hay un menos manda una advertencia
		messagebox.showwarning(message="¡Error De Entrada!\nNo hay valores negativos, por lo tanto serán absolutos.",title="Precaución")

	if (len(v) == 0) and (len(i) == 0) and (len(r) == 0) and (len(p) == 0): #Identifica si todo slos valores están vacíos
		messagebox.showwarning(message="¡Error De Entrada!\nTodos los valores están vacíos.",title="Precaución")
	elif (len(v) != 0) and (len(i) != 0) and (len(r) != 0) and (len(p) != 0):
		messagebox.showwarning(message="¡Error De Entrada!\nTodos los valores están llenos.",title="Precaución") #Identifica si todos los valores están llenos
	#Se evalúa si es potencia la que se desea calcular
	elif (len(p) == 0):
		if (len(v) == 0):
			#Cambiar float(x) por scien(r)
			r = scien(r)
			i = scien(i)
			try:
				potencia.set(notacion((i*i)*r,4))
				volt.set(notacion(i*r,1))
				resistencia.set(notacion(r,3))
				corriente.set(notacion(i,2))
			except:
				messagebox.showerror(message="¡Error De Entrada!\nIngrese un número válido.",title="Error")
		elif (len(i) == 0):
			r = scien(r)
			v = scien(v)
			try:
				potencia.set(notacion((v*v)/r,4))
				corriente.set(notacion(v/r,2))
				volt.set(notacion(v,1))
				resistencia.set(notacion(r,3))
			except:
				messagebox.showerror(message="¡Error De Entrada!\nIngrese un número válido.",title="Error")
		elif (len(r) == 0):
			v = scien(v)
			i = scien(i)
			try:
				potencia.set(notacion(v*i,4))
				resistencia.set(notacion(v/i,3))
				volt.set(notacion(v,1))
				corriente.set(notacion(i,2))
			except:
				messagebox.showerror(message="¡Error De Entrada!\nIngrese un número válido.",title="Error")
	elif (len(p) != 0):
		#P & R
		if (len(v) == 0) and (len(i) == 0):
			r = scien(r)
			p = scien(p)
			try:
				volt.set(notacion(sqrt(p*r),1))
				corriente.set(notacion(sqrt(p/r),2))
				resistencia.set(notacion(r,3))
				potencia.set(notacion(p,4))
			except:
				messagebox.showerror(message="¡Error De Entrada!\nIngrese un número válido.",title="Error")
		#P & I
		elif (len(v) == 0) and (len(r) == 0):
			i = scien(i)
			p = scien(p)
			try:
				volt.set(notacion(p/i,1))
				resistencia.set(notacion(p/(i*i),3))
				corriente.set(notacion(i,2))
				potencia.set(notacion(p,4))
			except:
				messagebox.showerror(message="¡Error De Entrada!\nIngrese un número válido.",title="Error")
		#P & V
		elif (len(i) == 0) and (len(r) == 0):
			v = scien(v)
			p = scien(p)
			try:
				corriente.set(notacion(p/v,2))
				resistencia.set(notacion((v*v)/p,3))
				volt.set(notacion(v,1))
				potencia.set(notacion(p,4))
			except:
				messagebox.showerror(message="¡Error De Entrada!\nIngrese un número válido.",title="Error")
		else:
			messagebox.showwarning(message="¡Faltan Datos!",title="Precaución")




root = Tk()
root.title('Ley De Ohm')
root.iconbitmap('LDO.ico')
root.configure(background='#DDD') 
root.geometry('950x500')

canvas = Canvas(root,width=505,height=300)
canvas.pack(expand=NO, fill=BOTH)
canvas.place(x=200,y=85)
#Fuente +
canvas.create_line(10,110, 70,110, width=5)
#Línea vertical
canvas.create_line(40,110, 40,40, width=5)
#Línea horizontal
canvas.create_line(38,40, 490,40, width=5)
#Corriente (Tríangulo)
canvas.create_polygon(230,40, 230,20, 250,40, 230,60, width=5)
#Línea vertical
canvas.create_line(487,40, 487,250, width=5)
#Línea horizontal
canvas.create_line(490,250, 359,250, width=5)
#Resistencia
canvas.create_line(133,250, 153,230, width=5)
canvas.create_line(151,230, 191,270, width=5)
canvas.create_line(188,270, 228,230,width=5)
canvas.create_line(226,230, 266,270,width=5)
canvas.create_line(264,270, 304,230,width=5)
canvas.create_line(302,230, 342,270,width=5)
canvas.create_line(340,270, 360,250,width=5)
#Línea horizontal
canvas.create_line(135,250, 40,250, width=5)
#Línea vertical
canvas.create_line(40,253, 40,140, width=5)
#Fuente -
canvas.create_line(25,140, 57,140, width=5)
#Símbolo +
canvas.create_line(19,80, 19,100, width=3,fill='red')
canvas.create_line(10,90, 30,90, width=3,fill='red')
#Símbolo -
canvas.create_line(15,155, 25,155, width=3,fill='blue')
#Tríangulo
canvas.create_line(245,110, 175,180, width=3,fill='orange')
canvas.create_line(245,110, 315,180, width=3,fill='orange')
canvas.create_line(175,180, 315,180, width=3,fill='orange')
canvas.create_line(175,180, 315,180, width=3,fill='orange')
canvas.create_line(204,150, 286,150, width=3,fill='orange')
canvas.create_line(245,150, 245,180, width=3,fill='orange')

l0 = Label(text='Ley De Ohm ',fg='#000',bg='#F0F0F0',font=('Arial', 18, 'bold'))
l0.place(x=390,y=150)
l1 = Label(text='Voltaje (En volts):',fg='#000',bg='#DDD',font=('Arial', 12, 'bold'))
l1.place(x=50,y=170)
volt = StringVar()
volt1 = Entry(textvar=volt)
volt1.place(x=115,y=200,width=60,height=27)
l2 = Label(text='Corriente (En Ampers):',fg='#000',bg='#DDD',font=('Arial', 12, 'bold'))
l2.place(x=350,y=10)
corriente = StringVar()
corriente1 = Entry(textvar=corriente)
corriente1.place(x=400,y=35,width=85,height=27)
l3 = Label(text='Resistencia (En Ohms Ω):',fg='#000',bg='#DDD',font=('Arial', 12, 'bold'))
l3.place(x=350,y=400)
resistencia = StringVar()
resistencia1 = Entry(textvar=resistencia)
resistencia1.place(x=405,y=425,width=95,height=27)
l4 = Label(text='Potencia (En Watts):',fg='#000',bg='#DDD',font=('Arial', 12, 'bold'))
l4.place(x=720,y=170)
potencia = StringVar()
potencia1 = Entry(textvar=potencia)
potencia1.place(x=720,y=200,width=80,height=27)
btn = Button(root,text='Calcular',fg='#000',bg='#FE9727',font=('Helvetica', 10, 'bold'),command=lambda: leyohm(volt1.get(),corriente1.get(),resistencia1.get(),potencia1.get()))
btn.place(x=620,y=350)
btn = Button(root,text='Limpiar',fg='#000',bg='#32BC40',font=('Helvetica', 10, 'bold'),command=cleaner)
btn.place(x=250,y=350)
l5 = Label(text='V',fg='#000',font=('Arial', 11, 'bold'))
l5.place(x=438,y=205)
l6 = Label(text='I',fg='#000',font=('Arial', 11, 'bold'))
l6.place(x=415,y=240)
l7 = Label(text='R',fg='#000',font=('Arial', 11, 'bold'))
l7.place(x=460,y=240)

root.mainloop()
