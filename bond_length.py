# -*- coding: utf-8 -*-
"""
@author: Anneng
bondlength between Si and O atom
"""
import re, os
import matplotlib.pyplot as plt

def plot_bondlength_hist(file): 
	with open(file) as f: #change file name and/or directory if necessary
		data = f.read()
	#print(data)

	data = data.replace(' ', '').replace('\n', '')
	data = data.split('B')[1:]
	#print(data)

	bondlength = []
	for i in data:
		bond_i = i.split(':')
		temp =re.match(r'([0-9\(-]{3,4})(O|Si|H)([0-9\-\,]{3,4})(O|Si|H)', bond_i[0])
		if (temp[2] == 'O' and temp[4] == 'Si') or (temp[2] == 'Si' and temp[4] == 'O'):
			bondlength.append(float(bond_i[1]))
			
	#print(bondlength)
			
	plt.hist(bondlength)
	plt.savefig('%s.png' %file.strip('.txt'), dpi=600)
    print('%s.png has been saved' %file.strip('.txt'))        
        
    
dir_path = os.path.dirname(os.path.realpath(__file__))
files=[]

for file in os.listdir(dir_path):
    if file.endswith(".txt"):
        files.append(file)
        print(os.path.join(dir_path, file))
        
for file in files:
    plot_bondlength_hist(file)