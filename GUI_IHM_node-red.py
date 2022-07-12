#inclusao do modulo tkinter
import tkinter as tk
from tkinter import messagebox

#inclusao do modulo serial
import serial

import time

#definicao de funcoes
def power_on_off():
    
    if power_btn.config('text')[-1] == 'ON':
        power_btn.config(text='OFF')
    else:
        power_btn.config(text='ON')

def hold_on_off():
    
    if hold_btn.config('text')[-1] == 'LED ON':
        hold_btn.config(text='LED OFF')
    else:
        hold_btn.config(text='LED ON')

def increase_degree_a():
    if int(a_degree_lbl["text"])>= 0:
        value = int(a_degree_lbl["text"])
        a_degree_lbl["text"] = f"{value + 1}"
        mov_string = string_ent.get()
        string_ent_array = list(mov_string)

        #Alterando o ângulo da junta A
        A_string_index = string_ent_array.index("A")
        
        a_degree_string_ent_array = list(string_ent_array)
        if int(a_degree_string_ent_array[A_string_index+1]) < 9 and a_degree_string_ent_array[A_string_index+2] == " ":
            a_degree_string_ent_array[A_string_index+1]=int(a_degree_string_ent_array[A_string_index+1])+1
            a_degree_string_ent_array[A_string_index+1]=str(a_degree_string_ent_array[A_string_index+1])
        elif int(a_degree_string_ent_array[A_string_index+1]) == 9 and a_degree_string_ent_array[A_string_index+2] == " ":
            a_degree_string_ent_array.insert(A_string_index+1, 1)
            a_degree_string_ent_array[A_string_index+1]=str(a_degree_string_ent_array[A_string_index+1])
            a_degree_string_ent_array[A_string_index+2]=int(0)
            a_degree_string_ent_array[A_string_index+2]=str(a_degree_string_ent_array[A_string_index+2])
        elif int(a_degree_string_ent_array[A_string_index+1]) <= 9 and int(a_degree_string_ent_array[A_string_index+2]) < 9 and a_degree_string_ent_array[A_string_index+3] == " ":
            a_degree_string_ent_array[A_string_index+2]=int(a_degree_string_ent_array[A_string_index+2])+1
            a_degree_string_ent_array[A_string_index+2]=str(a_degree_string_ent_array[A_string_index+2])
        elif int(a_degree_string_ent_array[A_string_index+1]) <= 9 and int(a_degree_string_ent_array[A_string_index+2]) == 9 and a_degree_string_ent_array[A_string_index+3] == " ":
            a_degree_string_ent_array[A_string_index+1]=int(a_degree_string_ent_array[A_string_index+1])+1
            a_degree_string_ent_array[A_string_index+1]=str(a_degree_string_ent_array[A_string_index+1])
            a_degree_string_ent_array[A_string_index+2]=0
            a_degree_string_ent_array[A_string_index+2]=str(a_degree_string_ent_array[A_string_index+2])
        elif int(a_degree_string_ent_array[A_string_index+1]) == 9 and int(a_degree_string_ent_array[A_string_index+2]) == 9 and a_degree_string_ent_array[A_string_index+3] == " ":
            a_degree_string_ent_array.insert(A_string_index+1, 1)
            a_degree_string_ent_array[A_string_index+1]=str(a_degree_string_ent_array[A_string_index+1])
            a_degree_string_ent_array[A_string_index+2]=int(0)
            a_degree_string_ent_array[A_string_index+3]=int(0)
            a_degree_string_ent_array[A_string_index+2]=str(a_degree_string_ent_array[A_string_index+2])
            a_degree_string_ent_array[A_string_index+3]=str(a_degree_string_ent_array[A_string_index+3])
        elif int(a_degree_string_ent_array[A_string_index+1]) == 1 and int(a_degree_string_ent_array[A_string_index+2]) < 8 and int(a_degree_string_ent_array[A_string_index+3]) == 9 and a_degree_string_ent_array[A_string_index+4] == " ":
            a_degree_string_ent_array[A_string_index+2]=int(a_degree_string_ent_array[A_string_index+2])+1
            a_degree_string_ent_array[A_string_index+2]=str(a_degree_string_ent_array[A_string_index+2])
            a_degree_string_ent_array[A_string_index+3]=0
            a_degree_string_ent_array[A_string_index+3]=str(a_degree_string_ent_array[A_string_index+3])
        elif int(a_degree_string_ent_array[A_string_index+1]) == 1 and int(a_degree_string_ent_array[A_string_index+2]) < 8 and int(a_degree_string_ent_array[A_string_index+3]) <= 9 and a_degree_string_ent_array[A_string_index+4] == " ":
            a_degree_string_ent_array[A_string_index+3]=int(a_degree_string_ent_array[A_string_index+3])+1
            a_degree_string_ent_array[A_string_index+3]=str(a_degree_string_ent_array[A_string_index+3])
        else:    
            tk.messagebox.showwarning(title="Didatic Robotic Arm (GUI)", message="Ângulo máximo atingido!")
            
    local_string_ent = ""
    for i in a_degree_string_ent_array:
        local_string_ent += i
    string_ent.delete(0, tk.END)
    string_ent.insert(0, local_string_ent)
        
def decrease_degree_a():
    if int(a_degree_lbl["text"])> 0:
        value = int(a_degree_lbl["text"])
        a_degree_lbl["text"] = f"{value - 1}"
        mov_string = string_ent.get()
        string_ent_array = list(mov_string)

        #Alterando o ângulo da junta A
        A_string_index = string_ent_array.index("A")
        
        a_degree_string_ent_array = list(string_ent_array)
        if int(a_degree_string_ent_array[A_string_index+1]) > 0 and a_degree_string_ent_array[A_string_index+2] == " ":
            a_degree_string_ent_array[A_string_index+1]=int(a_degree_string_ent_array[A_string_index+1])-1
            a_degree_string_ent_array[A_string_index+1]=str(a_degree_string_ent_array[A_string_index+1])
        elif int(a_degree_string_ent_array[A_string_index+1]) == 1 and int(a_degree_string_ent_array[A_string_index+2]) == 0 and a_degree_string_ent_array[A_string_index+3] == " ":
            del a_degree_string_ent_array[1]
            a_degree_string_ent_array[A_string_index+1]=int(9)
            a_degree_string_ent_array[A_string_index+1]=str(a_degree_string_ent_array[A_string_index+1])
        elif int(a_degree_string_ent_array[A_string_index+1]) > 0 and int(a_degree_string_ent_array[A_string_index+2]) == 0 and a_degree_string_ent_array[A_string_index+3] == " ":
            a_degree_string_ent_array[A_string_index+1]=int(a_degree_string_ent_array[A_string_index+1])-1
            a_degree_string_ent_array[A_string_index+1]=str(a_degree_string_ent_array[A_string_index+1])
            a_degree_string_ent_array[A_string_index+2]=int(9)
            a_degree_string_ent_array[A_string_index+2]=str(a_degree_string_ent_array[A_string_index+2])
        elif int(a_degree_string_ent_array[A_string_index+1]) > 0 and int(a_degree_string_ent_array[A_string_index+2]) > 0 and a_degree_string_ent_array[A_string_index+3] == " ":
            a_degree_string_ent_array[A_string_index+2]=int(a_degree_string_ent_array[A_string_index+2])-1
            a_degree_string_ent_array[A_string_index+2]=str(a_degree_string_ent_array[A_string_index+2])
        elif int(a_degree_string_ent_array[A_string_index+1]) == 1 and int(a_degree_string_ent_array[A_string_index+2]) == 0 and int(a_degree_string_ent_array[A_string_index+3]) == 0 and a_degree_string_ent_array[A_string_index+4] == " ":
            del a_degree_string_ent_array[A_string_index+1]
            a_degree_string_ent_array[A_string_index+1]=int(9)
            a_degree_string_ent_array[A_string_index+2]=int(9)
            a_degree_string_ent_array[A_string_index+1]=str(a_degree_string_ent_array[A_string_index+1])
            a_degree_string_ent_array[A_string_index+2]=str(a_degree_string_ent_array[A_string_index+2])
        elif int(a_degree_string_ent_array[A_string_index+1]) > 0 and int(a_degree_string_ent_array[A_string_index+2]) == 0 and int(a_degree_string_ent_array[A_string_index+3]) > 0 and a_degree_string_ent_array[A_string_index+4] == " ":
            a_degree_string_ent_array[A_string_index+3]=int(a_degree_string_ent_array[A_string_index+3])-1
            a_degree_string_ent_array[A_string_index+3]=str(a_degree_string_ent_array[A_string_index+3])
        elif int(a_degree_string_ent_array[A_string_index+1]) > 0 and int(a_degree_string_ent_array[A_string_index+2]) > 0 and int(a_degree_string_ent_array[A_string_index+3]) == 0 and a_degree_string_ent_array[A_string_index+4] == " ":
            a_degree_string_ent_array[A_string_index+2]=int(a_degree_string_ent_array[A_string_index+2])-1
            a_degree_string_ent_array[A_string_index+2]=str(a_degree_string_ent_array[A_string_index+2])
            a_degree_string_ent_array[A_string_index+3]=9
            a_degree_string_ent_array[A_string_index+3]=str(a_degree_string_ent_array[A_string_index+3])
        elif int(a_degree_string_ent_array[A_string_index+1]) > 0 and int(a_degree_string_ent_array[A_string_index+2]) > 0 and int(a_degree_string_ent_array[A_string_index+3]) > 0 and a_degree_string_ent_array[A_string_index+4] == " ":
            a_degree_string_ent_array[A_string_index+3]=int(a_degree_string_ent_array[A_string_index+3])-1
            a_degree_string_ent_array[A_string_index+3]=str(a_degree_string_ent_array[A_string_index+3])
        else:    
            tk.messagebox.showwarning(title="Didatic Robotic Arm (GUI)", message="Ângulo mínimo atingido!")

    local_string_ent=""
    for i in a_degree_string_ent_array:
        local_string_ent += i
    string_ent.delete(0, tk.END)
    string_ent.insert(0, local_string_ent)

def increase_degree_b():
    if int(b_degree_lbl["text"])>= 0:
        value = int(b_degree_lbl["text"])
        b_degree_lbl["text"] = f"{value + 1}"

        mov_string = string_ent.get()
        string_ent_array = list(mov_string)

        #Alterando o ângulo da junta B
        B_string_index = string_ent_array.index("B")
        
        b_degree_string_ent_array = list(string_ent_array)
        if int(b_degree_string_ent_array[B_string_index+1]) < 9 and b_degree_string_ent_array[B_string_index+2] == " ":
            b_degree_string_ent_array[B_string_index+1]=int(b_degree_string_ent_array[B_string_index+1])+1
            b_degree_string_ent_array[B_string_index+1]=str(b_degree_string_ent_array[B_string_index+1])
        elif int(b_degree_string_ent_array[B_string_index+1]) == 9 and b_degree_string_ent_array[B_string_index+2] == " ":
            b_degree_string_ent_array.insert(B_string_index+1, 1)
            b_degree_string_ent_array[B_string_index+1]=str(b_degree_string_ent_array[B_string_index+1])
            b_degree_string_ent_array[B_string_index+2]=int(0)
            b_degree_string_ent_array[B_string_index+2]=str(b_degree_string_ent_array[B_string_index+2])
        elif int(b_degree_string_ent_array[B_string_index+1]) <= 9 and int(b_degree_string_ent_array[B_string_index+2]) < 9 and b_degree_string_ent_array[B_string_index+3] == " ":
            b_degree_string_ent_array[B_string_index+2]=int(b_degree_string_ent_array[B_string_index+2])+1
            b_degree_string_ent_array[B_string_index+2]=str(b_degree_string_ent_array[B_string_index+2])
        elif int(b_degree_string_ent_array[B_string_index+1]) <= 9 and int(b_degree_string_ent_array[B_string_index+2]) == 9 and b_degree_string_ent_array[B_string_index+3] == " ":
            b_degree_string_ent_array[B_string_index+1]=int(b_degree_string_ent_array[B_string_index+1])+1
            b_degree_string_ent_array[B_string_index+1]=str(b_degree_string_ent_array[B_string_index+1])
            b_degree_string_ent_array[B_string_index+2]=0
            b_degree_string_ent_array[B_string_index+2]=str(b_degree_string_ent_array[B_string_index+2])
        elif int(b_degree_string_ent_array[B_string_index+1]) == 9 and int(b_degree_string_ent_array[B_string_index+2]) == 9 and b_degree_string_ent_array[B_string_index+3] == " ":
            b_degree_string_ent_array.insert(B_string_index+1, 1)
            b_degree_string_ent_array[B_string_index+1]=str(b_degree_string_ent_array[B_string_index+1])
            b_degree_string_ent_array[B_string_index+2]=int(0)
            b_degree_string_ent_array[B_string_index+3]=int(0)
            b_degree_string_ent_array[B_string_index+2]=str(b_degree_string_ent_array[B_string_index+2])
            b_degree_string_ent_array[B_string_index+3]=str(b_degree_string_ent_array[B_string_index+3])
        elif int(b_degree_string_ent_array[B_string_index+1]) == 1 and int(b_degree_string_ent_array[B_string_index+2]) < 8 and int(b_degree_string_ent_array[B_string_index+3]) == 9 and b_degree_string_ent_array[B_string_index+4] == " ":
            b_degree_string_ent_array[B_string_index+2]=int(b_degree_string_ent_array[B_string_index+2])+1
            b_degree_string_ent_array[B_string_index+2]=str(b_degree_string_ent_array[B_string_index+2])
            b_degree_string_ent_array[B_string_index+3]=0
            b_degree_string_ent_array[B_string_index+3]=str(b_degree_string_ent_array[B_string_index+3])
        elif int(b_degree_string_ent_array[B_string_index+1]) == 1 and int(b_degree_string_ent_array[B_string_index+2]) < 8 and int(b_degree_string_ent_array[B_string_index+3]) <= 9 and b_degree_string_ent_array[B_string_index+4] == " ":
            b_degree_string_ent_array[B_string_index+3]=int(b_degree_string_ent_array[B_string_index+3])+1
            b_degree_string_ent_array[B_string_index+3]=str(b_degree_string_ent_array[B_string_index+3])
        else:    
            tk.messagebox.showwarning(title="Didatic Robotic Arm (GUI)", message="Ângulo máximo atingido!")
            
    local_string_ent = ""
    for i in b_degree_string_ent_array:
        local_string_ent += i
    string_ent.delete(0, tk.END)
    string_ent.insert(0, local_string_ent)

def decrease_degree_b():
    if int(b_degree_lbl["text"])> 0:
        value = int(b_degree_lbl["text"])
        b_degree_lbl["text"] = f"{value - 1}"

        mov_string = string_ent.get()
        string_ent_array = list(mov_string)

        #Alterando o ângulo da junta B
        B_string_index = string_ent_array.index("B")
        
        b_degree_string_ent_array = list(string_ent_array)
        if int(b_degree_string_ent_array[B_string_index+1]) > 0 and b_degree_string_ent_array[B_string_index+2] == " ":
            b_degree_string_ent_array[B_string_index+1]=int(b_degree_string_ent_array[B_string_index+1])-1
            b_degree_string_ent_array[B_string_index+1]=str(b_degree_string_ent_array[B_string_index+1])
        elif int(b_degree_string_ent_array[B_string_index+1]) == 1 and int(b_degree_string_ent_array[B_string_index+2]) == 0 and b_degree_string_ent_array[B_string_index+3] == " ":
            del b_degree_string_ent_array[B_string_index+1]
            b_degree_string_ent_array[B_string_index+1]=int(9)
            b_degree_string_ent_array[B_string_index+1]=str(b_degree_string_ent_array[B_string_index+1])
        elif int(b_degree_string_ent_array[B_string_index+1]) > 0 and int(b_degree_string_ent_array[B_string_index+2]) == 0 and b_degree_string_ent_array[B_string_index+3] == " ":
            b_degree_string_ent_array[B_string_index+1]=int(b_degree_string_ent_array[B_string_index+1])-1
            b_degree_string_ent_array[B_string_index+1]=str(b_degree_string_ent_array[B_string_index+1])
            b_degree_string_ent_array[B_string_index+2]=int(9)
            b_degree_string_ent_array[B_string_index+2]=str(b_degree_string_ent_array[B_string_index+2])
        elif int(b_degree_string_ent_array[B_string_index+1]) > 0 and int(b_degree_string_ent_array[B_string_index+2]) > 0 and b_degree_string_ent_array[B_string_index+3] == " ":
            b_degree_string_ent_array[B_string_index+2]=int(b_degree_string_ent_array[B_string_index+2])-1
            b_degree_string_ent_array[B_string_index+2]=str(b_degree_string_ent_array[B_string_index+2])
        elif int(b_degree_string_ent_array[B_string_index+1]) == 1 and int(b_degree_string_ent_array[B_string_index+2]) == 0 and int(b_degree_string_ent_array[B_string_index+3]) == 0 and b_degree_string_ent_array[B_string_index+4] == " ":
            del b_degree_string_ent_array[B_string_index+1]
            b_degree_string_ent_array[B_string_index+1]=int(9)
            b_degree_string_ent_array[B_string_index+2]=int(9)
            b_degree_string_ent_array[B_string_index+1]=str(b_degree_string_ent_array[B_string_index+1])
            b_degree_string_ent_array[B_string_index+2]=str(b_degree_string_ent_array[B_string_index+2])
        elif int(b_degree_string_ent_array[B_string_index+1]) > 0 and int(b_degree_string_ent_array[B_string_index+2]) == 0 and int(b_degree_string_ent_array[B_string_index+3]) > 0 and b_degree_string_ent_array[B_string_index+4] == " ":
            b_degree_string_ent_array[B_string_index+3]=int(b_degree_string_ent_array[B_string_index+3])-1
            b_degree_string_ent_array[B_string_index+3]=str(b_degree_string_ent_array[B_string_index+3])
        elif int(b_degree_string_ent_array[B_string_index+1]) > 0 and int(b_degree_string_ent_array[B_string_index+2]) > 0 and int(b_degree_string_ent_array[B_string_index+3]) == 0 and b_degree_string_ent_array[B_string_index+4] == " ":
            b_degree_string_ent_array[B_string_index+2]=int(b_degree_string_ent_array[B_string_index+2])-1
            b_degree_string_ent_array[B_string_index+2]=str(b_degree_string_ent_array[B_string_index+2])
            b_degree_string_ent_array[B_string_index+3]=9
            b_degree_string_ent_array[B_string_index+3]=str(b_degree_string_ent_array[B_string_index+3])
        elif int(b_degree_string_ent_array[B_string_index+1]) > 0 and int(b_degree_string_ent_array[B_string_index+2]) > 0 and int(b_degree_string_ent_array[B_string_index+3]) > 0 and b_degree_string_ent_array[B_string_index+4] == " ":
            b_degree_string_ent_array[B_string_index+3]=int(b_degree_string_ent_array[B_string_index+3])-1
            b_degree_string_ent_array[B_string_index+3]=str(b_degree_string_ent_array[B_string_index+3])
        else:    
            tk.messagebox.showwarning(title="Didatic Robotic Arm (GUI)", message="Ângulo mínimo atingido!")

    local_string_ent=""
    for i in b_degree_string_ent_array:
        local_string_ent += i
    string_ent.delete(0, tk.END)
    string_ent.insert(0, local_string_ent)

def increase_degree_c():
    if int(c_degree_lbl["text"])>= 0:
        value = int(c_degree_lbl["text"])
        c_degree_lbl["text"] = f"{value + 1}"

        mov_string = string_ent.get()
        string_ent_array = list(mov_string)

        #Alterando o ângulo da junta C
        C_string_index = string_ent_array.index("C")
        
        c_degree_string_ent_array = list(string_ent_array)
        if int(c_degree_string_ent_array[C_string_index+1]) < 9 and c_degree_string_ent_array[C_string_index+2] == " ":
            c_degree_string_ent_array[C_string_index+1]=int(c_degree_string_ent_array[C_string_index+1])+1
            c_degree_string_ent_array[C_string_index+1]=str(c_degree_string_ent_array[C_string_index+1])
        elif int(c_degree_string_ent_array[C_string_index+1]) == 9 and c_degree_string_ent_array[C_string_index+2] == " ":
            c_degree_string_ent_array.insert(C_string_index+1, 1)
            c_degree_string_ent_array[C_string_index+1]=str(c_degree_string_ent_array[C_string_index+1])
            c_degree_string_ent_array[C_string_index+2]=int(0)
            c_degree_string_ent_array[C_string_index+2]=str(c_degree_string_ent_array[C_string_index+2])
        elif int(c_degree_string_ent_array[C_string_index+1]) <= 9 and int(c_degree_string_ent_array[C_string_index+2]) < 9 and c_degree_string_ent_array[C_string_index+3] == " ":
            c_degree_string_ent_array[C_string_index+2]=int(c_degree_string_ent_array[C_string_index+2])+1
            c_degree_string_ent_array[C_string_index+2]=str(c_degree_string_ent_array[C_string_index+2])
        elif int(c_degree_string_ent_array[C_string_index+1]) <= 9 and int(c_degree_string_ent_array[C_string_index+2]) == 9 and c_degree_string_ent_array[C_string_index+3] == " ":
            c_degree_string_ent_array[C_string_index+1]=int(c_degree_string_ent_array[C_string_index+1])+1
            c_degree_string_ent_array[C_string_index+1]=str(c_degree_string_ent_array[C_string_index+1])
            c_degree_string_ent_array[C_string_index+2]=0
            c_degree_string_ent_array[C_string_index+2]=str(c_degree_string_ent_array[C_string_index+2])
        elif int(c_degree_string_ent_array[C_string_index+1]) == 9 and int(c_degree_string_ent_array[C_string_index+2]) == 9 and c_degree_string_ent_array[C_string_index+3] == " ":
            c_degree_string_ent_array.insert(C_string_index+1, 1)
            c_degree_string_ent_array[C_string_index+1]=str(c_degree_string_ent_array[C_string_index+1])
            c_degree_string_ent_array[C_string_index+2]=int(0)
            c_degree_string_ent_array[C_string_index+3]=int(0)
            c_degree_string_ent_array[C_string_index+2]=str(c_degree_string_ent_array[C_string_index+2])
            c_degree_string_ent_array[C_string_index+3]=str(c_degree_string_ent_array[C_string_index+3])
        elif int(c_degree_string_ent_array[C_string_index+1]) == 1 and int(c_degree_string_ent_array[C_string_index+2]) < 8 and int(c_degree_string_ent_array[C_string_index+3]) == 9 and c_degree_string_ent_array[C_string_index+4] == " ":
            c_degree_string_ent_array[C_string_index+2]=int(c_degree_string_ent_array[C_string_index+2])+1
            c_degree_string_ent_array[C_string_index+2]=str(c_degree_string_ent_array[C_string_index+2])
            c_degree_string_ent_array[C_string_index+3]=0
            c_degree_string_ent_array[C_string_index+3]=str(c_degree_string_ent_array[C_string_index+3])
        elif int(c_degree_string_ent_array[C_string_index+1]) == 1 and int(c_degree_string_ent_array[C_string_index+2]) < 8 and int(c_degree_string_ent_array[C_string_index+3]) <= 9 and c_degree_string_ent_array[C_string_index+4] == " ":
            c_degree_string_ent_array[C_string_index+3]=int(c_degree_string_ent_array[C_string_index+3])+1
            c_degree_string_ent_array[C_string_index+3]=str(c_degree_string_ent_array[C_string_index+3])
        else:    
            tk.messagebox.showwarning(title="Didatic Robotic Arm (GUI)", message="Ângulo máximo atingido!")
            
    local_string_ent = ""
    for i in c_degree_string_ent_array:
        local_string_ent += i
    string_ent.delete(0, tk.END)
    string_ent.insert(0, local_string_ent)

def decrease_degree_c():
    if int(c_degree_lbl["text"])> 0:
        value = int(c_degree_lbl["text"])
        c_degree_lbl["text"] = f"{value - 1}"

        mov_string = string_ent.get()
        string_ent_array = list(mov_string)

        #Alterando o ângulo da junta C
        C_string_index = string_ent_array.index("C")
        
        c_degree_string_ent_array = list(string_ent_array)
        if int(c_degree_string_ent_array[C_string_index+1]) > 0 and c_degree_string_ent_array[C_string_index+2] == " ":
            c_degree_string_ent_array[C_string_index+1]=int(c_degree_string_ent_array[C_string_index+1])-1
            c_degree_string_ent_array[C_string_index+1]=str(c_degree_string_ent_array[C_string_index+1])
        elif int(c_degree_string_ent_array[C_string_index+1]) == 1 and int(c_degree_string_ent_array[C_string_index+2]) == 0 and c_degree_string_ent_array[C_string_index+3] == " ":
            del c_degree_string_ent_array[C_string_index+1]
            c_degree_string_ent_array[C_string_index+1]=int(9)
            c_degree_string_ent_array[C_string_index+1]=str(c_degree_string_ent_array[C_string_index+1])
        elif int(c_degree_string_ent_array[C_string_index+1]) > 0 and int(c_degree_string_ent_array[C_string_index+2]) == 0 and c_degree_string_ent_array[C_string_index+3] == " ":
            c_degree_string_ent_array[C_string_index+1]=int(c_degree_string_ent_array[C_string_index+1])-1
            c_degree_string_ent_array[C_string_index+1]=str(c_degree_string_ent_array[C_string_index+1])
            c_degree_string_ent_array[C_string_index+2]=int(9)
            c_degree_string_ent_array[C_string_index+2]=str(c_degree_string_ent_array[C_string_index+2])
        elif int(c_degree_string_ent_array[C_string_index+1]) > 0 and int(c_degree_string_ent_array[C_string_index+2]) > 0 and c_degree_string_ent_array[C_string_index+3] == " ":
            c_degree_string_ent_array[C_string_index+2]=int(c_degree_string_ent_array[C_string_index+2])-1
            c_degree_string_ent_array[C_string_index+2]=str(c_degree_string_ent_array[C_string_index+2])
        elif int(c_degree_string_ent_array[C_string_index+1]) == 1 and int(c_degree_string_ent_array[C_string_index+2]) == 0 and int(c_degree_string_ent_array[C_string_index+3]) == 0 and c_degree_string_ent_array[C_string_index+4] == " ":
            del c_degree_string_ent_array[C_string_index+1]
            c_degree_string_ent_array[C_string_index+1]=int(9)
            c_degree_string_ent_array[C_string_index+2]=int(9)
            c_degree_string_ent_array[C_string_index+1]=str(c_degree_string_ent_array[C_string_index+1])
            c_degree_string_ent_array[C_string_index+2]=str(c_degree_string_ent_array[C_string_index+2])
        elif int(c_degree_string_ent_array[C_string_index+1]) > 0 and int(c_degree_string_ent_array[C_string_index+2]) == 0 and int(c_degree_string_ent_array[C_string_index+3]) > 0 and c_degree_string_ent_array[C_string_index+4] == " ":
            c_degree_string_ent_array[C_string_index+3]=int(c_degree_string_ent_array[C_string_index+3])-1
            c_degree_string_ent_array[C_string_index+3]=str(c_degree_string_ent_array[C_string_index+3])
        elif int(c_degree_string_ent_array[C_string_index+1]) > 0 and int(c_degree_string_ent_array[C_string_index+2]) > 0 and int(c_degree_string_ent_array[C_string_index+3]) == 0 and c_degree_string_ent_array[C_string_index+4] == " ":
            c_degree_string_ent_array[C_string_index+2]=int(c_degree_string_ent_array[C_string_index+2])-1
            c_degree_string_ent_array[C_string_index+2]=str(c_degree_string_ent_array[C_string_index+2])
            c_degree_string_ent_array[C_string_index+3]=9
            c_degree_string_ent_array[C_string_index+3]=str(c_degree_string_ent_array[C_string_index+3])
        elif int(c_degree_string_ent_array[C_string_index+1]) > 0 and int(c_degree_string_ent_array[C_string_index+2]) > 0 and int(c_degree_string_ent_array[C_string_index+3]) > 0 and c_degree_string_ent_array[C_string_index+4] == " ":
            c_degree_string_ent_array[C_string_index+3]=int(c_degree_string_ent_array[C_string_index+3])-1
            c_degree_string_ent_array[C_string_index+3]=str(c_degree_string_ent_array[C_string_index+3])
        else:    
            tk.messagebox.showwarning(title="Didatic Robotic Arm (GUI)", message="Ângulo mínimo atingido!")

    local_string_ent=""
    for i in c_degree_string_ent_array:
        local_string_ent += i
    string_ent.delete(0, tk.END)
    string_ent.insert(0, local_string_ent)

def increase_degree_d():
    if int(d_degree_lbl["text"])>= 0:
        value = int(d_degree_lbl["text"])
        d_degree_lbl["text"] = f"{value + 1}"

        mov_string = string_ent.get()
        string_ent_array = list(mov_string)

        #Alterando o ângulo da junta D
        D_string_index = string_ent_array.index("D")
        
        d_degree_string_ent_array = list(string_ent_array)
        if int(d_degree_string_ent_array[D_string_index+1]) < 9 and d_degree_string_ent_array[D_string_index+2] == " ":
            d_degree_string_ent_array[D_string_index+1]=int(d_degree_string_ent_array[D_string_index+1])+1
            d_degree_string_ent_array[D_string_index+1]=str(d_degree_string_ent_array[D_string_index+1])
        elif int(d_degree_string_ent_array[D_string_index+1]) == 9 and d_degree_string_ent_array[D_string_index+2] == " ":
            d_degree_string_ent_array.insert(D_string_index+1, 1)
            d_degree_string_ent_array[D_string_index+1]=str(d_degree_string_ent_array[D_string_index+1])
            d_degree_string_ent_array[D_string_index+2]=int(0)
            d_degree_string_ent_array[D_string_index+2]=str(d_degree_string_ent_array[D_string_index+2])
        elif int(d_degree_string_ent_array[D_string_index+1]) <= 9 and int(d_degree_string_ent_array[D_string_index+2]) < 9 and d_degree_string_ent_array[D_string_index+3] == " ":
            d_degree_string_ent_array[D_string_index+2]=int(d_degree_string_ent_array[D_string_index+2])+1
            d_degree_string_ent_array[D_string_index+2]=str(d_degree_string_ent_array[D_string_index+2])
        elif int(d_degree_string_ent_array[D_string_index+1]) <= 9 and int(d_degree_string_ent_array[D_string_index+2]) == 9 and d_degree_string_ent_array[D_string_index+3] == " ":
            d_degree_string_ent_array[D_string_index+1]=int(d_degree_string_ent_array[D_string_index+1])+1
            d_degree_string_ent_array[D_string_index+1]=str(d_degree_string_ent_array[D_string_index+1])
            d_degree_string_ent_array[D_string_index+2]=0
            d_degree_string_ent_array[D_string_index+2]=str(d_degree_string_ent_array[D_string_index+2])
        elif int(d_degree_string_ent_array[D_string_index+1]) == 9 and int(d_degree_string_ent_array[D_string_index+2]) == 9 and d_degree_string_ent_array[D_string_index+3] == " ":
            d_degree_string_ent_array.insert(D_string_index+1, 1)
            d_degree_string_ent_array[D_string_index+1]=str(d_degree_string_ent_array[D_string_index+1])
            d_degree_string_ent_array[D_string_index+2]=int(0)
            d_degree_string_ent_array[D_string_index+3]=int(0)
            d_degree_string_ent_array[D_string_index+2]=str(d_degree_string_ent_array[D_string_index+2])
            d_degree_string_ent_array[D_string_index+3]=str(d_degree_string_ent_array[D_string_index+3])
        elif int(d_degree_string_ent_array[D_string_index+1]) == 1 and int(d_degree_string_ent_array[D_string_index+2]) < 8 and int(d_degree_string_ent_array[D_string_index+3]) == 9 and d_degree_string_ent_array[D_string_index+4] == " ":
            d_degree_string_ent_array[D_string_index+2]=int(d_degree_string_ent_array[D_string_index+2])+1
            d_degree_string_ent_array[D_string_index+2]=str(d_degree_string_ent_array[D_string_index+2])
            d_degree_string_ent_array[D_string_index+3]=0
            d_degree_string_ent_array[D_string_index+3]=str(d_degree_string_ent_array[D_string_index+3])
        elif int(d_degree_string_ent_array[D_string_index+1]) == 1 and int(d_degree_string_ent_array[D_string_index+2]) < 8 and int(d_degree_string_ent_array[D_string_index+3]) <= 9 and d_degree_string_ent_array[D_string_index+4] == " ":
            d_degree_string_ent_array[D_string_index+3]=int(d_degree_string_ent_array[D_string_index+3])+1
            d_degree_string_ent_array[D_string_index+3]=str(d_degree_string_ent_array[D_string_index+3])
        else:    
            tk.messagebox.showwarning(title="Didatic Robotic Arm (GUI)", message="Ângulo máximo atingido!")
            
    local_string_ent = ""
    for i in d_degree_string_ent_array:
        local_string_ent += i
    string_ent.delete(0, tk.END)
    string_ent.insert(0, local_string_ent)

def decrease_degree_d():
    if int(d_degree_lbl["text"])> 0:
        value = int(d_degree_lbl["text"])
        d_degree_lbl["text"] = f"{value - 1}"

        mov_string = string_ent.get()
        string_ent_array = list(mov_string)

        #Alterando o ângulo da junta D
        D_string_index = string_ent_array.index("D")
        
        d_degree_string_ent_array = list(string_ent_array)
        if int(d_degree_string_ent_array[D_string_index+1]) > 0 and d_degree_string_ent_array[D_string_index+2] == " ":
            d_degree_string_ent_array[D_string_index+1]=int(d_degree_string_ent_array[D_string_index+1])-1
            d_degree_string_ent_array[D_string_index+1]=str(d_degree_string_ent_array[D_string_index+1])
        elif int(d_degree_string_ent_array[D_string_index+1]) == 1 and int(d_degree_string_ent_array[D_string_index+2]) == 0 and d_degree_string_ent_array[D_string_index+3] == " ":
            del d_degree_string_ent_array[D_string_index+1]
            d_degree_string_ent_array[D_string_index+1]=int(9)
            d_degree_string_ent_array[D_string_index+1]=str(d_degree_string_ent_array[D_string_index+1])
        elif int(d_degree_string_ent_array[D_string_index+1]) > 0 and int(d_degree_string_ent_array[D_string_index+2]) == 0 and d_degree_string_ent_array[D_string_index+3] == " ":
            d_degree_string_ent_array[D_string_index+1]=int(d_degree_string_ent_array[D_string_index+1])-1
            d_degree_string_ent_array[D_string_index+1]=str(d_degree_string_ent_array[D_string_index+1])
            d_degree_string_ent_array[D_string_index+2]=int(9)
            d_degree_string_ent_array[D_string_index+2]=str(d_degree_string_ent_array[D_string_index+2])
        elif int(d_degree_string_ent_array[D_string_index+1]) > 0 and int(d_degree_string_ent_array[D_string_index+2]) > 0 and d_degree_string_ent_array[D_string_index+3] == " ":
            d_degree_string_ent_array[D_string_index+2]=int(d_degree_string_ent_array[D_string_index+2])-1
            d_degree_string_ent_array[D_string_index+2]=str(d_degree_string_ent_array[D_string_index+2])
        elif int(d_degree_string_ent_array[D_string_index+1]) == 1 and int(d_degree_string_ent_array[D_string_index+2]) == 0 and int(d_degree_string_ent_array[D_string_index+3]) == 0 and d_degree_string_ent_array[D_string_index+4] == " ":
            del d_degree_string_ent_array[D_string_index+1]
            d_degree_string_ent_array[D_string_index+1]=int(9)
            d_degree_string_ent_array[D_string_index+2]=int(9)
            d_degree_string_ent_array[D_string_index+1]=str(d_degree_string_ent_array[D_string_index+1])
            d_degree_string_ent_array[D_string_index+2]=str(d_degree_string_ent_array[D_string_index+2])
        elif int(d_degree_string_ent_array[D_string_index+1]) > 0 and int(d_degree_string_ent_array[D_string_index+2]) == 0 and int(d_degree_string_ent_array[D_string_index+3]) > 0 and d_degree_string_ent_array[D_string_index+4] == " ":
            d_degree_string_ent_array[D_string_index+3]=int(d_degree_string_ent_array[D_string_index+3])-1
            d_degree_string_ent_array[D_string_index+3]=str(d_degree_string_ent_array[D_string_index+3])
        elif int(d_degree_string_ent_array[D_string_index+1]) > 0 and int(d_degree_string_ent_array[D_string_index+2]) > 0 and int(d_degree_string_ent_array[D_string_index+3]) == 0 and d_degree_string_ent_array[D_string_index+4] == " ":
            d_degree_string_ent_array[D_string_index+2]=int(d_degree_string_ent_array[D_string_index+2])-1
            d_degree_string_ent_array[D_string_index+2]=str(d_degree_string_ent_array[D_string_index+2])
            d_degree_string_ent_array[D_string_index+3]=9
            d_degree_string_ent_array[D_string_index+3]=str(d_degree_string_ent_array[D_string_index+3])
        elif int(d_degree_string_ent_array[D_string_index+1]) > 0 and int(d_degree_string_ent_array[D_string_index+2]) > 0 and int(d_degree_string_ent_array[D_string_index+3]) > 0 and d_degree_string_ent_array[D_string_index+4] == " ":
            d_degree_string_ent_array[D_string_index+3]=int(d_degree_string_ent_array[D_string_index+3])-1
            d_degree_string_ent_array[D_string_index+3]=str(d_degree_string_ent_array[D_string_index+3])
        else:    
            tk.messagebox.showwarning(title="Didatic Robotic Arm (GUI)", message="Ângulo mínimo atingido!")

    local_string_ent=""
    for i in d_degree_string_ent_array:
        local_string_ent += i
    string_ent.delete(0, tk.END)
    string_ent.insert(0, local_string_ent)

def increase_degree_e():
    if int(e_degree_lbl["text"])>= 0:
        value = int(e_degree_lbl["text"])
        e_degree_lbl["text"] = f"{value + 1}"

        mov_string = string_ent.get()
        string_ent_array = list(mov_string)

        for i in range(3):
            string_ent_array.append(" ")

        #Alterando o ângulo da junta E
        E_string_index = string_ent_array.index("E")
        
        e_degree_string_ent_array = list(string_ent_array)
        if int(e_degree_string_ent_array[E_string_index+1]) < 9 and e_degree_string_ent_array[E_string_index+2] == " ":
            e_degree_string_ent_array[E_string_index+1]=int(e_degree_string_ent_array[E_string_index+1])+1
            e_degree_string_ent_array[E_string_index+1]=str(e_degree_string_ent_array[E_string_index+1])
        elif int(e_degree_string_ent_array[E_string_index+1]) == 9 and e_degree_string_ent_array[E_string_index+2] == " ":
            e_degree_string_ent_array.insert(E_string_index+1, 1)
            e_degree_string_ent_array[E_string_index+1]=str(e_degree_string_ent_array[E_string_index+1])
            e_degree_string_ent_array[E_string_index+2]=int(0)
            e_degree_string_ent_array[E_string_index+2]=str(e_degree_string_ent_array[E_string_index+2])
        elif int(e_degree_string_ent_array[E_string_index+1]) <= 9 and int(e_degree_string_ent_array[E_string_index+2]) < 9 and e_degree_string_ent_array[E_string_index+3] == " ":
            e_degree_string_ent_array[E_string_index+2]=int(e_degree_string_ent_array[E_string_index+2])+1
            e_degree_string_ent_array[E_string_index+2]=str(e_degree_string_ent_array[E_string_index+2])
        elif int(e_degree_string_ent_array[E_string_index+1]) <= 9 and int(e_degree_string_ent_array[E_string_index+2]) == 9 and e_degree_string_ent_array[E_string_index+3] == " ":
            e_degree_string_ent_array[E_string_index+1]=int(e_degree_string_ent_array[E_string_index+1])+1
            e_degree_string_ent_array[E_string_index+1]=str(e_degree_string_ent_array[E_string_index+1])
            e_degree_string_ent_array[E_string_index+2]=0
            e_degree_string_ent_array[E_string_index+2]=str(e_degree_string_ent_array[E_string_index+2])
        elif int(e_degree_string_ent_array[E_string_index+1]) == 9 and int(e_degree_string_ent_array[E_string_index+2]) == 9 and e_degree_string_ent_array[E_string_index+3] == " ":
            e_degree_string_ent_array.insert(E_string_index+1, 1)
            e_degree_string_ent_array[E_string_index+1]=str(e_degree_string_ent_array[E_string_index+1])
            e_degree_string_ent_array[E_string_index+2]=int(0)
            e_degree_string_ent_array[E_string_index+3]=int(0)
            e_degree_string_ent_array[E_string_index+2]=str(e_degree_string_ent_array[E_string_index+2])
            e_degree_string_ent_array[E_string_index+3]=str(e_degree_string_ent_array[E_string_index+3])
        elif int(e_degree_string_ent_array[E_string_index+1]) == 1 and int(e_degree_string_ent_array[E_string_index+2]) < 8 and int(e_degree_string_ent_array[E_string_index+3]) == 9 and e_degree_string_ent_array[E_string_index+4] == " ":
            e_degree_string_ent_array[E_string_index+2]=int(e_degree_string_ent_array[E_string_index+2])+1
            e_degree_string_ent_array[E_string_index+2]=str(e_degree_string_ent_array[E_string_index+2])
            e_degree_string_ent_array[E_string_index+3]=0
            e_degree_string_ent_array[E_string_index+3]=str(e_degree_string_ent_array[E_string_index+3])
        elif int(e_degree_string_ent_array[E_string_index+1]) == 1 and int(e_degree_string_ent_array[E_string_index+2]) < 8 and int(e_degree_string_ent_array[E_string_index+3]) <= 9 and e_degree_string_ent_array[E_string_index+4] == " ":
            e_degree_string_ent_array[E_string_index+3]=int(e_degree_string_ent_array[E_string_index+3])+1
            e_degree_string_ent_array[E_string_index+3]=str(e_degree_string_ent_array[E_string_index+3])
        else:    
            tk.messagebox.showwarning(title="Didatic Robotic Arm (GUI)", message="Ângulo máximo atingido!")
            
    local_string_ent = ""
    for i in e_degree_string_ent_array:
        local_string_ent += i
    string_ent.delete(0, tk.END)
    string_ent.insert(0, local_string_ent)

def decrease_degree_e():
    if int(e_degree_lbl["text"])> 0:
        value = int(e_degree_lbl["text"])
        e_degree_lbl["text"] = f"{value - 1}"

        mov_string = string_ent.get()
        string_ent_array = list(mov_string)

        for i in range(3):
            string_ent_array.append(" ")

        #Alterando o ângulo da junta E
        E_string_index = string_ent_array.index("E")
        
        e_degree_string_ent_array = list(string_ent_array)
        if int(e_degree_string_ent_array[E_string_index+1]) > 0 and e_degree_string_ent_array[E_string_index+2] == " ":
            e_degree_string_ent_array[E_string_index+1]=int(e_degree_string_ent_array[E_string_index+1])-1
            e_degree_string_ent_array[E_string_index+1]=str(e_degree_string_ent_array[E_string_index+1])
        elif int(e_degree_string_ent_array[E_string_index+1]) == 1 and int(e_degree_string_ent_array[E_string_index+2]) == 0 and e_degree_string_ent_array[E_string_index+3] == " ":
            del e_degree_string_ent_array[E_string_index+1]
            e_degree_string_ent_array[E_string_index+1]=int(9)
            e_degree_string_ent_array[E_string_index+1]=str(e_degree_string_ent_array[E_string_index+1])
        elif int(e_degree_string_ent_array[E_string_index+1]) > 0 and int(e_degree_string_ent_array[E_string_index+2]) == 0 and e_degree_string_ent_array[E_string_index+3] == " ":
            e_degree_string_ent_array[E_string_index+1]=int(e_degree_string_ent_array[E_string_index+1])-1
            e_degree_string_ent_array[E_string_index+1]=str(e_degree_string_ent_array[E_string_index+1])
            e_degree_string_ent_array[E_string_index+2]=int(9)
            e_degree_string_ent_array[E_string_index+2]=str(e_degree_string_ent_array[E_string_index+2])
        elif int(e_degree_string_ent_array[E_string_index+1]) > 0 and int(e_degree_string_ent_array[E_string_index+2]) > 0 and e_degree_string_ent_array[E_string_index+3] == " ":
            e_degree_string_ent_array[E_string_index+2]=int(e_degree_string_ent_array[E_string_index+2])-1
            e_degree_string_ent_array[E_string_index+2]=str(e_degree_string_ent_array[E_string_index+2])
        elif int(e_degree_string_ent_array[E_string_index+1]) == 1 and int(e_degree_string_ent_array[E_string_index+2]) == 0 and int(e_degree_string_ent_array[E_string_index+3]) == 0 and e_degree_string_ent_array[E_string_index+4] == " ":
            del e_degree_string_ent_array[E_string_index+1]
            e_degree_string_ent_array[E_string_index+1]=int(9)
            e_degree_string_ent_array[E_string_index+2]=int(9)
            e_degree_string_ent_array[E_string_index+1]=str(e_degree_string_ent_array[E_string_index+1])
            e_degree_string_ent_array[E_string_index+2]=str(e_degree_string_ent_array[E_string_index+2])
        elif int(e_degree_string_ent_array[E_string_index+1]) > 0 and int(e_degree_string_ent_array[E_string_index+2]) == 0 and int(e_degree_string_ent_array[E_string_index+3]) > 0 and e_degree_string_ent_array[E_string_index+4] == " ":
            e_degree_string_ent_array[E_string_index+3]=int(e_degree_string_ent_array[E_string_index+3])-1
            e_degree_string_ent_array[E_string_index+3]=str(e_degree_string_ent_array[E_string_index+3])
        elif int(e_degree_string_ent_array[E_string_index+1]) > 0 and int(e_degree_string_ent_array[E_string_index+2]) > 0 and int(e_degree_string_ent_array[E_string_index+3]) == 0 and e_degree_string_ent_array[E_string_index+4] == " ":
            e_degree_string_ent_array[E_string_index+2]=int(e_degree_string_ent_array[E_string_index+2])-1
            e_degree_string_ent_array[E_string_index+2]=str(e_degree_string_ent_array[E_string_index+2])
            e_degree_string_ent_array[E_string_index+3]=9
            e_degree_string_ent_array[E_string_index+3]=str(e_degree_string_ent_array[E_string_index+3])
        elif int(d_degree_string_ent_array[E_string_index+1]) > 0 and int(e_degree_string_ent_array[E_string_index+2]) > 0 and int(e_degree_string_ent_array[E_string_index+3]) > 0 and e_degree_string_ent_array[E_string_index+4] == " ":
            e_degree_string_ent_array[E_string_index+3]=int(e_degree_string_ent_array[E_string_index+3])-1
            e_degree_string_ent_array[E_string_index+3]=str(e_degree_string_ent_array[E_string_index+3])
        else:    
            tk.messagebox.showwarning(title="Didatic Robotic Arm (GUI)", message="Ângulo mínimo atingido!")

    local_string_ent=""
    for i in e_degree_string_ent_array:
        local_string_ent += i
    string_ent.delete(0, tk.END)
    string_ent.insert(0, local_string_ent)

def move_home():
    mov_string = home_degree.get()
    #ser.write(str(mov_string).encode())
    update_string_values(mov_string)
    print(mov_string)

def send_string():
    mov_string = string_ent.get()
    #ser.write(str(mov_string).encode())
    update_string_values(mov_string)
    print(mov_string)

def update_string_values(mov_string):

    #Atualizando a caixa com a string
    string_ent.delete(0, tk.END)
    string_ent.insert(0, mov_string)
    
    #Obtendo o valor do ângulo de cada junta
    string_ent_array = list(mov_string)

    #Junta A
    A_string = ""
    a_found = 0
    a_degree_angle_lbl = ""
    for a in string_ent_array:
                if a == "A":
                    a_found=1
                if a_found ==1:
                    if a == " ":
                        break
                    else:
                        A_string+=a
    a_degree_angle = list(A_string)
    del a_degree_angle[0]
    for i in a_degree_angle:
        a_degree_angle_lbl += i
    a_degree_lbl["text"] = a_degree_angle_lbl

    #Junta B
    B_string = ""
    b_found = 0
    b_degree_angle_lbl = ""
    for b in string_ent_array:
                if b == "B":
                    b_found=1
                if b_found ==1:
                    if b == " ":
                        break
                    else:
                        B_string+=b
    b_degree_angle = list(B_string)
    del b_degree_angle[0]
    for i in b_degree_angle:
        b_degree_angle_lbl += i
    b_degree_lbl["text"] = b_degree_angle_lbl

    #Junta C
    C_string = ""
    c_found = 0
    c_degree_angle_lbl = ""
    for c in string_ent_array:
                if c == "C":
                    c_found=1
                if c_found ==1:
                    if c == " ":
                        break
                    else:
                        C_string+=c
    c_degree_angle = list(C_string)
    del c_degree_angle[0]
    for i in c_degree_angle:
        c_degree_angle_lbl += i
    c_degree_lbl["text"] = c_degree_angle_lbl

    #Junta D
    D_string = ""
    d_found = 0
    d_degree_angle_lbl = ""
    for d in string_ent_array:
                if d == "D":
                    d_found=1
                if d_found ==1:
                    if d == " ":
                        break
                    else:
                        D_string+=d
    d_degree_angle = list(D_string)
    del d_degree_angle[0]
    for i in d_degree_angle:
        d_degree_angle_lbl += i
    d_degree_lbl["text"] = d_degree_angle_lbl

    #Junta E       
    E_string = ""
    e_found = 0
    e_degree_angle_lbl = ""
    for e in string_ent_array:
                if e == "E":
                    e_found=1
                if e_found ==1:
                    if e == " ":
                        break
                    else:
                        E_string+=e
    e_degree_angle = list(E_string)
    del e_degree_angle[0]
    for i in e_degree_angle:
        e_degree_angle_lbl += i
    e_degree_lbl["text"] = e_degree_angle_lbl

#def send_string():
#    mov_string = string_ent.get() #captura string de movimento e armazena em var.
#    while ser.is_open: #enquanto serial estiver disponivel
#        ser.write(chr(10).encode()) #envia mensagem para arduino checar o botao
#        send_checked = ser.read(3).decode("ascii","ignore")
#        if chr(20) in send_checked: #checa se msg do arduino =20
#            ser.write(str(mov_string).encode()) #caso seja, envia string de movimento
#            break
 
#instanciacao da janela
window = tk.Tk()
window.title("Didatic Robotic Arm (GUI)")

#configuracao da quantidade de linhas e colunas
window.rowconfigure([0,15],weight=1,minsize=250)
window.columnconfigure([0,3],weight=1,minsize=500)

#instanciacao do frame para widgets
frm_widgets = tk.Frame(master=window,relief=tk.SUNKEN,width=400,height=600,borderwidth=5)

#instanciacao dos buttons e labels
power_lbl = tk.Label(master=frm_widgets,text="Power On/Shutdown")
power_btn = tk.Button(master=frm_widgets,text="ON",command=power_on_off)

reset_lbl = tk.Label(master=frm_widgets,text="Clear Memory")
reset_btn = tk.Button(master=frm_widgets,text="Reset")

home_lbl = tk.Label(master=frm_widgets,text="Initial Position")
home_degree = tk.Entry(master=frm_widgets,width=20, bg="white", fg="black")
home_degree.insert(0, "A90 B50 C82 D90 E90")
home_btn = tk.Button(master=frm_widgets,text="Home",command=move_home)

hold_lbl = tk.Label(master=frm_widgets,text="Hold/Drop")
hold_btn = tk.Button(master=frm_widgets,text="LED ON",command=hold_on_off)

string_lbl = tk.Label(master=frm_widgets,text="String of Movement")
string_ent = tk.Entry(master=frm_widgets,width=20, bg="white", fg="black")
string_ent.insert(0, "A90 B90 C90 D90 E90")
#string_degree_lbl = tk.Label(master=frm_widgets,width=20, bg="white", fg="black",text="A90 B90 C90 D90 E90")
string_send_btn = tk.Button(master=frm_widgets,text="Send",command=send_string)

a_joint_lbl = tk.Label(master=frm_widgets,text="Joint A(°)")
a_plus_btn = tk.Button(master=frm_widgets,text="+",command=increase_degree_a)
a_degree_lbl = tk.Label(master=frm_widgets,width=20, bg="white", fg="black",text="90")
a_minus_btn = tk.Button(master=frm_widgets,text="                 -                 ",command=decrease_degree_a)

b_joint_lbl = tk.Label(master=frm_widgets,text="Joint B(°)")
b_plus_btn = tk.Button(master=frm_widgets,text="+",command=increase_degree_b)
b_degree_lbl = tk.Label(master=frm_widgets,width=20, bg="white", fg="black",text="90")
b_minus_btn = tk.Button(master=frm_widgets,text="-",command=decrease_degree_b)

c_joint_lbl = tk.Label(master=frm_widgets,text="Joint C(°)")
c_plus_btn = tk.Button(master=frm_widgets,text="+",command=increase_degree_c)
c_degree_lbl = tk.Label(master=frm_widgets,width=20, bg="white", fg="black",text="90")
c_minus_btn = tk.Button(master=frm_widgets,text="-",command=decrease_degree_c)

d_joint_lbl = tk.Label(master=frm_widgets,text="Joint D(°)")
d_plus_btn = tk.Button(master=frm_widgets,text="+",command=increase_degree_d)
d_degree_lbl = tk.Label(master=frm_widgets,width=20, bg="white", fg="black",text="90")
d_minus_btn = tk.Button(master=frm_widgets,text="-",command=decrease_degree_d)

e_joint_lbl = tk.Label(master=frm_widgets,text="Joint E(°)")
e_plus_btn = tk.Button(master=frm_widgets,text="+",command=increase_degree_e)
e_degree_lbl = tk.Label(master=frm_widgets,width=20, bg="white", fg="black",text="90")
e_minus_btn = tk.Button(master=frm_widgets,text="-",command=decrease_degree_e)

#geometry managers
frm_widgets.pack()

power_lbl.grid(row=0,column=0,sticky="nsew",padx=5,pady=5)
power_btn.grid(row=0,column=1,sticky="nsew",padx=5,pady=5)

reset_lbl.grid(row=1,column=0,sticky="nsew",padx=5,pady=5)
reset_btn.grid(row=1,column=1,sticky="nsew",padx=5,pady=5)

home_lbl.grid(row=2,column=0,sticky="nsew",padx=5,pady=5)
home_btn.grid(row=2,column=1,sticky="nsew",padx=5,pady=5)

hold_lbl.grid(row=3,column=0,sticky="nsew",padx=5,pady=5)
hold_btn.grid(row=3,column=1,sticky="nsew",padx=5,pady=5)

string_lbl.grid(row=4,column=0,sticky="nsew",padx=5,pady=5)
string_ent.grid(row=4,column=1,sticky="nsew",padx=5,pady=5)
#string_degree_lbl.grid(row=4,column=1,sticky="nsew",padx=5,pady=5)
string_send_btn.grid(row=4,column=2,sticky="nsew",padx=5,pady=5)

a_joint_lbl.grid(row=5,column=0,sticky="nsew",padx=5,pady=5)
a_plus_btn.grid(row=5,column=1,sticky="nsew",padx=5,pady=5)
a_degree_lbl.grid(row=5,column=2,sticky="nsew",padx=5,pady=5)
a_minus_btn.grid(row=5,column=3,sticky="nsew",padx=5,pady=5)

b_joint_lbl.grid(row=6,column=0,sticky="nsew",padx=5,pady=5)
b_plus_btn.grid(row=6,column=1,sticky="nsew",padx=5,pady=5)
b_degree_lbl.grid(row=6,column=2,sticky="nsew",padx=5,pady=5)
b_minus_btn.grid(row=6,column=3,sticky="nsew",padx=5,pady=5)

c_joint_lbl.grid(row=7,column=0,sticky="nsew",padx=5,pady=5)
c_plus_btn.grid(row=7,column=1,sticky="nsew",padx=5,pady=5)
c_degree_lbl.grid(row=7,column=2,sticky="nsew",padx=5,pady=5)
c_minus_btn.grid(row=7,column=3,sticky="nsew",padx=5,pady=5)

d_joint_lbl.grid(row=8,column=0,sticky="nsew",padx=5,pady=5)
d_plus_btn.grid(row=8,column=1,sticky="nsew",padx=5,pady=5)
d_degree_lbl.grid(row=8,column=2,sticky="nsew",padx=5,pady=5)
d_minus_btn.grid(row=8,column=3,sticky="nsew",padx=5,pady=5)

e_joint_lbl.grid(row=9,column=0,sticky="nsew",padx=5,pady=5)
e_plus_btn.grid(row=9,column=1,sticky="nsew",padx=5,pady=5)
e_degree_lbl.grid(row=9,column=2,sticky="nsew",padx=5,pady=5)
e_minus_btn.grid(row=9,column=3,sticky="nsew",padx=5,pady=5)

#comunicacao serial com arduino
'''i=3
while i>0: #Loop para a conexão com o Arduino
    try:  #Tenta se conectar, se conseguir, o loop se encerra

        #Conexão via Linux
        #ser = serial.Serial('/dev/ttyUSB0', 115200)

        #Conexão via Windows
        ser = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
        break
    except:
        pass
        print('Não foi possível conectar com Arduino UNO')
    i= i -1
'''
window.mainloop()
