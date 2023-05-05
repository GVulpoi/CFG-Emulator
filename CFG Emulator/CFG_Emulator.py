import sys
from tkinter.tix import COLUMN, ROW
import tkinter as tk
from tkinter.ttk import Style
from turtle import width
import random

def progr(fisier="BD.txt"):

	def _var_list(fisier):
		f = open(fisier , "r")
		bd_mult={}
		var_list=[]
		sigma_list=[]
		rules_list=[]

		init = f.readline().strip()

		if init == "[Vars]":
			init = f.readline().strip()

			while init != "[Sigma]":
				var_list.append(init)
				init = f.readline().strip()

			init=f.readline().strip()

			while init != "[Rules]":
				sigma_list.append(init)
				init = f.readline().strip()

			init = f.readline().strip()
			while init != "":
				init = init.split("->")
				init[1].split(",")
				rules_list.append(init)
				init = f.readline().strip()

		bd_mult["[Var]"]=var_list
		bd_mult["[Sigma]"]=sigma_list

		return bd_mult

	def _rules_list(fisier):
		f = open(fisier , "r")
		init = f.readline().strip()
		rules_list={}

		while init != "[Rules]":
			init = f.readline().strip()

		init = f.readline().strip()
		while init != "":
			init = init.split("->")
			aux = init[1].split(",")
			if init[0] not in rules_list:
				rules_list[init[0]]=aux
			else:
				for i in aux:
					if i not in rules_list[init[0]]:
						rules_list[init[0]].append(i)
			init = f.readline().strip()

		return rules_list


	rules_list = _rules_list(fisier)
	var_list = _var_list(fisier)
	solution_list=[]

	def _CFG_generator(rules_list , gen , var_list):

		if (gen[len(gen)-1] in var_list["[Sigma]"] or gen[len(gen)-1] not in rules_list):
			
			solution_list.append(gen)

		else:

			for i in rules_list[gen[len(gen)-1]]:
				gen += [i]
				_CFG_generator(rules_list , gen , var_list)
				gen = gen[0:len(gen)-1]


	for i in rules_list['S']:
		gen = [i]
		_CFG_generator(rules_list , gen , var_list)

	return solution_list

win=tk.Tk()
win.title("Context Free Grammar Emulator")
win.configure(width=500 , height=300)
win.minsize(width=850 , height=400)
win.configure(bg='#333333')




#run button
run_button=tk.Button(
	win,
	text="Start",
	font='Calibri',
	bg='#333333',
	fg='white',
	border=0,
	command=lambda: afis()
).grid(
	column=0,
	row=0,
	padx=5,
	pady=5
)
#############


#linia de outuput , box+label+functia de afisare folosita la butonul de start
output_label = tk.Label(win , text="Output : " , bg='#333333' , font='Calibri' , fg='White')
output_label.grid(column=1 , row=1 , sticky=tk.W , padx=5 , pady=5)

afis_label= tk.Text(win , bg='#333333' , fg='White' , border=0 ,height=20 , width=40 )
afis_label.grid(row=2 , column=1 , padx=5 , pady=5 )

def afis():
	afis_label.delete(1.0,tk.END)
	aux = progr("BD.txt")

	for i in range(len(aux)-1 , -1 , -1):

		for j in range(len(aux[i])-1 , -1 , -1):
			afis_label.insert(1.0 , aux[i][j])
			afis_label.insert(1.0 , " ")

		afis_label.insert(1.0 ,"\n")
#############


#exit button
exit_button=tk.Button(
	win,
	text="Exit",
	font='Calibri',
	bg='#333333',
	fg='white',
	border=0,
	command= lambda : win_exit()
).grid(
	row=3,
	column=0,
	sticky=tk.SW
	)
#############


#afisare si modificare de fisier cu text box
file_show= tk.Text(win , bg='#686868' , width=40 , height=20)

file_show.grid(
	row=2,
	column=3,
	sticky = tk.N,
	padx = 5,
	pady = 5
)

file_label = tk.Label(win , text="Date.in" , bg='#333333' , fg='White' , font='Calibri')
file_label.grid(
	row=0,
	column=3,
	sticky=tk.S
)

def afis_fisier(fisier="BD.txt"):
	f=open(fisier , 'r')
	s=f.readline()
	lista=[]
	while s:
		file_show.insert(tk.END , s)
		s=f.readline()
afis_fisier()


bd_button = tk.Button(
	win,
	text="Modify",
	font='Calibri',
	bg='#333333',
	fg='white',
	border=0,
	command=lambda : bd_change()
).grid(
	padx=5,
	pady=5,
	row=1,
	column=3,
	sticky=tk.N
)

def bd_change(fisier="BD.txt"):
	f=open(fisier , "w")
	linie=file_show.get(1.0 , tk.END)
	f.write(linie)

bd_change()
#############

def win_exit():
	sys.exit()

win.after(1)
win.mainloop()