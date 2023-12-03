import tkinter as tk

calci=""
def add_to_calci(par1):
    global calci
    calci+=str(par1)
    result_bar.delete(1.0,"end")
    result_bar.insert(1.0,calci)

def eval_calci():
    global calci
    try:
        result=str(eval(calci))
        calci=""
        result_bar.delete(1.0,"end")
        result_bar.insert(1.0,result)
    except:
        clear()
        result_bar.insert(1.0,"Error")

def clear():
    global calci
    calci=""
    result_bar.delete(1.0,"end")

def bspace():
    global calci
    if len(calci)<2:
        calci=""
    calci=calci[:len(calci)-1]
    result_bar.delete(1.0,"end")
    result_bar.insert(1.0,calci)

root=tk.Tk()
root.title("Calculator")
root.geometry("480x380")

result_bar=tk.Text(root,height=2, width=26, font=("Italic",24))
result_bar.grid(columnspan=5)

bt1=tk.Button(root,text="1",command=lambda: add_to_calci(1),width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
bt1.grid(row=5,column=1)
bt2=tk.Button(root,text="2",command=lambda: add_to_calci(2),width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
bt2.grid(row=5,column=2)
bt3=tk.Button(root,text="3",command=lambda: add_to_calci(3),width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
bt3.grid(row=5,column=3)
bt4=tk.Button(root,text="4",command=lambda: add_to_calci(4),width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
bt4.grid(row=4,column=1)
bt5=tk.Button(root,text="5",command=lambda: add_to_calci(5),width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
bt5.grid(row=4,column=2)
bt6=tk.Button(root,text="6",command=lambda: add_to_calci(6),width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
bt6.grid(row=4,column=3)
bt7=tk.Button(root,text="7",command=lambda: add_to_calci(7),width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
bt7.grid(row=3,column=1)
bt8=tk.Button(root,text="8",command=lambda: add_to_calci(8),width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
bt8.grid(row=3,column=2)
bt9=tk.Button(root,text="9",command=lambda: add_to_calci(9),width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
bt9.grid(row=3,column=3)
bt0=tk.Button(root,text="0",command=lambda: add_to_calci(0),width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
bt0.grid(row=6,column=1)
btclc=tk.Button(root,text="AC",command=clear,width=6,bg='#008080',fg='#00FFFF',font=("Italic",20))
btclc.grid(row=2,column=1)
btpr1=tk.Button(root,text="(",command=lambda: add_to_calci("("),width=6,bg="#A4B9A7",fg='#D6EBD1',font=("Italic",20))
btpr1.grid(row=2,column=2)
btpr2=tk.Button(root,text=")",command=lambda: add_to_calci(")"),width=6,bg="#A4B9A7",fg='#D6EBD1',font=("Italic",20))
btpr2.grid(row=2,column=3)
btdiv=tk.Button(root,text="/",command=lambda: add_to_calci("/"),width=6,bg="#A4B9A7",fg='#D6EBD1',font=("Italic",20))
btdiv.grid(row=2,column=4)
btmul=tk.Button(root,text="X",command=lambda: add_to_calci("*"),width=6,bg="#A4B9A7",fg='#D6EBD1',font=("Italic",20))
btmul.grid(row=3,column=4)
btminus=tk.Button(root,text="-",command=lambda: add_to_calci("-"),width=6,bg="#A4B9A7",fg='#D6EBD1',font=("Italic",20))
btminus.grid(row=4,column=4)
btplus=tk.Button(root,text="+",command=lambda: add_to_calci("+"),width=6,bg="#A4B9A7",fg='#D6EBD1',font=("Italic",20))
btplus.grid(row=5,column=4)
bteq=tk.Button(root,text="=",command=eval_calci,width=6,bg="#5C8B5C",fg='#D6EBD1',font=("Italic",20))
bteq.grid(row=6,column=4)
btclr=tk.Button(root,text="DEL",command=bspace,width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
btclr.grid(row=6,column=3)
btdot=tk.Button(root,text=".",command=lambda: add_to_calci("."),width=6,bg='#E4E8DA',fg='black',font=("Italic",20))
btdot.grid(row=6,column=2)

root.mainloop()
