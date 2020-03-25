from tkinter import *
from time import sleep
from random import random
import math

mutation_cance= float(input('input mutation chance.\n').replace('%',''))

window = Tk()
window.title('cyberlife')
window.geometry('1600x400')

land=[]
for x in range(400):
	land.append([])
for x in range(400):
	for y in range(100):
		land[x].append({'type':0,'color':'#181818'})

life=[]

canvas = Canvas(width=1600,height=400,bg='#181818')
canvas.place(x=0,y=0,relwidth=1,relheight=1)

class tree:
	def __init__(self,spx,spy,par_dna):
		self.start_point=[spx,spy]
		self.energy=100
		self.old=0
		r = random()*100
		self.dna=par_dna
		life.append(self)
		self.structure=[{'x':0,'y':0,'type':1,'gen':0}]
	def update(self):
		for element in self.structure:
			if element['type']==1:
				element['type']=0
				if self.dna[element['gen']][0]!=16:
					self.structure.append({'x':element['x'],'y':element['y']+1,'type':1,'gen':self.dna[element['gen']][0]})
		print(self.dna[0][0])

first_dna=[]
for dna in range(15):
	first_dna.append([])
	for gen in range(3):
		first_dna[dna].append(round(random()*16))
first_life=tree(random()*400,random()*100,first_dna)

def main():
	for tree in life:
		tree.update()
	draw()

def draw():
	for x in range(len(land)):
		for y in range(len(land[x])):
			canvas.create_rectangle((x*4,y*4),(x*4+4,y*4+4),fill=land[x][y]['color'])

window.after(300,main)
window.bind("escape",window.destroy)
window.mainloop()