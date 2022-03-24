from cProfile import label
from cgitb import reset
from operator import truediv
from tkinter import*
from tkinter import messagebox
from tkinter import font
from turtle import color #paziņojumi, ieteikumi
mansLogs=Tk()
mansLogs.title("TicTacToe")
speletajsX=True #kuram speletejam karta spelet, liks krustinu
count=0 #aizpildito rutinu skaits


def disableButtons():
    btn1.config(state=DISABLED)#disable poga nestrada
    btn2.config(state=DISABLED)#normal poga strada
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
    return
def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""

    global uzvaretajs,count, speletajsX
    uzvaretajs=False
    count=0
    speletajsX=True
    return 0
def infoLogs():
    jaunsLogs=Toplevel()
    jaunsLogs.title("Info par spēli")
    jaunsLogs.geometry("380x300")
    apraksts=Label(jaunsLogs,text="Spēle tiek spēlēta katru reizi mainoties.\n Sāk spēlētājs, kurš ir X.\n Spēles mērķis ir dabūt trīs vienādus simbolus virknē vai pa diagonāli.")
    apraksts.grid(row=0,column=0)
    return 0    
def btnClick(button):#pados tukšu pogu
    global speletajsX,count # kādi mainīgie tiks lietoti
    if button["text"]=="" and speletajsX==True: #spele x speletajs
        button["text"]="X"#maina uz X
        button["fg"]="purple"
        speletajsX=False
        count+=1
        parbUzvar()
    elif button["text"]=="" and speletajsX==False:
        button["text"]="O"
        button["fg"]="black"
        speletajsX=True
        count+=1
        parbUzvar()
    else:
        messagebox.showerror("TicTacToe", "Šeit jau ir simbols")
    return  
def parbUzvar():
    global uzvaretajs
    if(btn1["text"]=="X" and btn2["text"]=="X"and btn3["text"]=="X" or
        btn1["text"]=="X" and btn4["text"]=="X"and btn7["text"]=="X" or
        btn1["text"]=="X" and btn5["text"]=="X"and btn9["text"]=="X" or
        btn3["text"]=="X" and btn6["text"]=="X"and btn9["text"]=="X" or
        btn7["text"]=="X" and btn8["text"]=="X"and btn9["text"]=="X" or
        btn2["text"]=="X" and btn5["text"]=="X"and btn8["text"]=="X" or
        btn7["text"]=="X" and btn5["text"]=="X"and btn3["text"]=="X" or
        btn4["text"]=="X" and btn5["text"]=="X"and btn6["text"]=="X"):
    
        uzvaretajs=True
        disableButtons()
        messagebox.showinfo("TicTacToe", "Speletajs X ir uzvarētājs")
    elif(btn1["text"]=="O" and btn2["text"]=="O"and btn3["text"]=="O"
        or btn1["text"]=="O" and btn4["text"]=="O"and btn7["text"]=="O"
        or btn1["text"]=="O" and btn5["text"]=="O"and btn9["text"]=="O"
        or btn3["text"]=="O" and btn6["text"]=="O"and btn9["text"]=="O"
        or btn7["text"]=="O" and btn8["text"]=="O"and btn9["text"]=="O"
        or btn2["text"]=="O" and btn5["text"]=="O"and btn8["text"]=="O"
        or btn4["text"]=="O" and btn5["text"]=="O"and btn6["text"]=="O"
        or btn7["text"]=="O" and btn5["text"]=="O"and btn3["text"]=="O"):
        uzvaretajs=True
        disableButtons()
        messagebox.showinfo("TicTacToe", "Speletajs O ir uzvarētājs")
    elif count==9:
        
        uzvaretajs=False
        disableButtons()
        messagebox.showinfo("TicTacToe", "Spēle ir neizšķirta" )
        return    

btn1=Button(mansLogs, bd=20,bg="lightgreen",text="",width=6,height=3,font=("Arial Black",20), command = lambda:btnClick(btn1))
btn2=Button(mansLogs, bd=20,bg="lightgreen",text="",width=6,height=3,font=("Arial Black",20), command = lambda:btnClick(btn2))
btn3=Button(mansLogs, bd=20,bg="lightgreen",text="",width=6,height=3,font=("Arial Black",20), command = lambda:btnClick(btn3))
btn4=Button(mansLogs, bd=20,bg="lightgreen",text="",width=6,height=3,font=("Arial Black",20), command = lambda:btnClick(btn4))
btn5=Button(mansLogs, bd=20,bg="lightgreen",text="",width=6,height=3,font=("Arial Black",20), command = lambda:btnClick(btn5))
btn6=Button(mansLogs, bd=20,bg="lightgreen",text="",width=6,height=3,font=("Arial Black",20), command = lambda:btnClick(btn6))
btn7=Button(mansLogs, bd=20,bg="lightgreen",text="",width=6,height=3,font=("Arial Black",20), command = lambda:btnClick(btn7))
btn8=Button(mansLogs, bd=20,bg="lightgreen",text="",width=6,height=3,font=("Arial Black",20), command = lambda:btnClick(btn8))
btn9=Button(mansLogs, bd=20,bg="lightgreen",text="",width=6,height=3,font=("Arial Black",20), command = lambda:btnClick(btn9))
btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
galvenaIzvelne=Menu(mansLogs)#iveido galveno izvēlni
mansLogs.config(menu=galvenaIzvelne)#pievieno galvenajam logam
opcijas=Menu(galvenaIzvelne,tearoff=False)#mazā izvēlne
galvenaIzvelne.add_cascade(label="Opcijas",menu=opcijas)#lejupkritošs saraksts
opcijas.add_command(label="Jauna spēle", command=reset)
opcijas.add_command(label="Iziet",command=mansLogs.quit)
galvenaIzvelne.add_cascade(label="Info",command=infoLogs)#pieveino mazajai izvēlnei
mansLogs.mainloop()