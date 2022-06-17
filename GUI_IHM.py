#inclusao do modulo tkinter
import tkinter as tk

#inclusao do modulo serial
import serial

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

def decrease_degree_a():
    if int(a_degree_lbl["text"])> 0:
        value = int(a_degree_lbl["text"])
        a_degree_lbl["text"] = f"{value - 1}"

def increase_degree_b():
    if int(b_degree_lbl["text"])>= 0:
        value = int(b_degree_lbl["text"])
        b_degree_lbl["text"] = f"{value + 1}"

def decrease_degree_b():
    if int(b_degree_lbl["text"])> 0:
        value = int(b_degree_lbl["text"])
        b_degree_lbl["text"] = f"{value - 1}"

def increase_degree_c():
    if int(c_degree_lbl["text"])>= 0:
        value = int(c_degree_lbl["text"])
        c_degree_lbl["text"] = f"{value + 1}"

def decrease_degree_c():
    if int(c_degree_lbl["text"])> 0:
        value = int(c_degree_lbl["text"])
        c_degree_lbl["text"] = f"{value - 1}"    

def increase_degree_d():
    if int(d_degree_lbl["text"])>= 0:
        value = int(d_degree_lbl["text"])
        d_degree_lbl["text"] = f"{value + 1}"

def decrease_degree_d():
    if int(d_degree_lbl["text"])> 0:
        value = int(d_degree_lbl["text"])
        d_degree_lbl["text"] = f"{value - 1}"

def increase_degree_e():
    if int(e_degree_lbl["text"])>= 0:
        value = int(e_degree_lbl["text"])
        e_degree_lbl["text"] = f"{value + 1}"

def decrease_degree_e():
    if int(e_degree_lbl["text"])> 0:
        value = int(e_degree_lbl["text"])
        e_degree_lbl["text"] = f"{value - 1}"

def send_string():
    mov_string = string_ent.get()
    ser.write(chr(mov_string).encode())
 
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
home_btn = tk.Button(master=frm_widgets,text="Home")

hold_lbl = tk.Label(master=frm_widgets,text="Hold/Drop")
hold_btn = tk.Button(master=frm_widgets,text="LED ON",command=hold_on_off)

string_lbl = tk.Label(master=frm_widgets,text="String of Movement")
string_ent = tk.Entry(master=frm_widgets,width=20, bg="white", fg="black")
string_send_btn = tk.Button(master=frm_widgets,text="Send",command=send_string)

a_joint_lbl = tk.Label(master=frm_widgets,text="Joint A(°)")
a_plus_btn = tk.Button(master=frm_widgets,text="+",command=increase_degree_a)
a_degree_lbl = tk.Label(master=frm_widgets,width=20, bg="white", fg="black",text="0")
a_minus_btn = tk.Button(master=frm_widgets,text="                 -                 ",command=decrease_degree_a)

b_joint_lbl = tk.Label(master=frm_widgets,text="Joint B(°)")
b_plus_btn = tk.Button(master=frm_widgets,text="+",command=increase_degree_b)
b_degree_lbl = tk.Label(master=frm_widgets,width=20, bg="white", fg="black",text="0")
b_minus_btn = tk.Button(master=frm_widgets,text="-",command=decrease_degree_b)

c_joint_lbl = tk.Label(master=frm_widgets,text="Joint C(°)")
c_plus_btn = tk.Button(master=frm_widgets,text="+",command=increase_degree_c)
c_degree_lbl = tk.Label(master=frm_widgets,width=20, bg="white", fg="black",text="0")
c_minus_btn = tk.Button(master=frm_widgets,text="-",command=decrease_degree_c)

d_joint_lbl = tk.Label(master=frm_widgets,text="Joint D(°)")
d_plus_btn = tk.Button(master=frm_widgets,text="+",command=increase_degree_d)
d_degree_lbl = tk.Label(master=frm_widgets,width=20, bg="white", fg="black",text="0")
d_minus_btn = tk.Button(master=frm_widgets,text="-",command=decrease_degree_d)

e_joint_lbl = tk.Label(master=frm_widgets,text="Joint E(°)")
e_plus_btn = tk.Button(master=frm_widgets,text="+",command=increase_degree_e)
e_degree_lbl = tk.Label(master=frm_widgets,width=20, bg="white", fg="black",text="0")
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
i=3
while i>0: #Loop para a conexão com o Arduino
    try:  #Tenta se conectar, se conseguir, o loop se encerra
        ser = serial.Serial('/dev/ttyUSB0', 9600)    
        break
    except:
        pass
        print('Não foi possível conectar com Arduino UNO')
    i= i -1
    
window.mainloop()
