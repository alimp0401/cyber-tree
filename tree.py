import tkinter
import random

world_setting={'width':1,'height':1,'gravity':True,'mutation_chance':0,'circle_world':False}
world_setting['width']=int(input('set world width.'))
world_setting['height']=int(input('set world height'))
world_setting['gravity']=bool(input('will world have gravity(0-off,1-on)'))
world_setting['mutatin_cance']=float(input('set mutation chance in world').replace('%',''))
world_setting['circle_world']=False

class tree:
	def __init__(self,sp,parrents_dna):
		self.start_poin = sp
		self.struct = [[0,0,1,0,10]]
		self.old = 1
		self.max_old = 90
	def grow(self):
		new_struct = []
		old_struct = self.struct
		for cell in old_struct:
			if cell[3]==2:
				new_struct.append(cell)
			else:
				if 