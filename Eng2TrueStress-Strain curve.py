from tkinter import *
from tkinter.filedialog import *
import pandas as pd
from matplotlib import pyplot as plt
from math import log as ln

Eng_Strain=[]
Eng_Stress=[]
True_Strain=[]
True_Stress=[]

def import_data():
    filename=askopenfilename(filetypes=[('CSV files', '.csv'),
                                        ('All files','*')])
    sample_data=pd.read_csv(filename)
    for row in sample_data.Strain:
        Eng_Strain.append(row)
    for row in sample_data.Stress:
        Eng_Stress.append(row)
    for i in range (len(Eng_Strain)):
        True_Strain.append((ln(1+Eng_Strain[i]))*100)
    for j in range(len(Eng_Stress)):
        True_Stress.append(Eng_Stress[j]*(1+Eng_Strain[j]))
    
def plot_graph():
    plt.plot(True_Strain,True_Stress)
    plt.title('True stress-strain curve')
    plt.xlabel('True Strain, %')
    plt.ylabel('True Stress, MPa')
    plt.show()

def print_points():
    print('True strain points (x axis): ', True_Strain)
    print('True stress points (y axis): ', True_Stress)
    
root=Tk()

root.title('Stress-Strain curve converter')
import_label=Label(text='Import .csv file for your material and calculate true stress-strain points:', font=('Verdana', 8))
import_button=Button(text='Import and calculate', font=('Verdana', 10), command=import_data)
plot_label=Label(text='Plot true stress-strain curve: ', font=('Verdana', 8))
plot_button=Button(text='Plot graph', font=('Verdana', 10), command=plot_graph)
print_label=Label(text='Print true stress-strain curve points: ', font=('Verdana', 8))
print_button=Button(text='Print points', font=('Verdana', 10), command=print_points)
import_label.grid(row=0, column=0, columnspan=2)
import_button.grid(row=1, column=0, columnspan=2)
plot_label.grid(row=3, column=0)
plot_button.grid(row=3, column=1)
print_label.grid(row=4, column=0)
print_button.grid(row=4, column=1)

mainloop()
