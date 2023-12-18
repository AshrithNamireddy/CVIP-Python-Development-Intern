from essential_generators import DocumentGenerator
import random
import tkinter as tk
import time
import threading
from itertools import zip_longest
#from itertools import zip

gen = DocumentGenerator()
class speedtyping:
    
    def __init__(self):
        global gen
        self.root = tk.Tk()
        self.root.title("Typing speed test")
        self.root.geometry("1200x600")
        self.root.configure(bg='#fff8a3')
        self.frame= tk.Frame(self.root,bg='#fff8a3')
        
        self.rantext = gen.sentence()

        self.titl = tk.Label(self.frame,text="TEST YOUR TYPING SKILLS",bg='#fff8a3',font=("Arial bold",36))
        self.titl.grid(row=0,column=0,columnspan=2,padx=5,pady=(10,100))
        
        self.sample = tk.Label(self.frame,text=self.rantext,bg='black',fg='yellow',font=("Italics bold",18))
        self.sample.grid(row=1,column=0,columnspan=2,padx=5,pady=50)
        
        self.inputs = tk.Entry(self.frame,width=40,font=("Helvetica",24))
        self.inputs.grid(row=2,column=0,columnspan=2,padx=5,pady=5)
        self.inputs.bind("<KeyPress>",self.run)
        self.inputs.config(highlightbackground="black",highlightthickness=3)
        
        self.outputs = tk.Label(self.frame,text="Speed(Words/Minute): 0.00\n Speed(Words/second): 0.00\nAccuracy: 0.00", bg="#dfe05c",font=("Italics",18))
        self.outputs.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

        self.resets=tk.Button(self.frame,text="Reset",command=self.reset,font=("Italics",18))
        self.resets.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
        self.resets.configure(foreground="white",background="black")

        self.counter=0
        self.started=False

        self.frame.pack(expand=True)
        self.root.mainloop()

    def run(self,event):
        #print(event.keycode)
        if not self.started:
            if not event.keycode in [16,17,18,13]:
                t=threading.Thread(target=self.times)
                self.started=True
                t.start()
        if event.keycode == 13:
            self.started=False
        if not self.sample.cget('text').startswith(self.inputs.get()):
            self.inputs.config(fg = "red")
        else:
            self.inputs.config(fg = "black")
        if self.sample.cget('text') == self.inputs.get():
            self.started = False
            self.inputs.config(fg="green")
            

    def times(self):
        while self.started:
            time.sleep(0.1)
            self.counter+=0.1
            wps=len(list(map(str,self.rantext.split())))/self.counter
            wpm=wps*60
            m=self.inputs.get()
            k=sum(c1==c2 for c1,c2 in zip(self.rantext[:len(m)],m))
            try:
                acc=(k/len(m))*100
            except:
                acc=0
            self.outputs.config(text=f"Speed(Words/Minute): {wpm:.2f}\n Speed(words/second): {wps:.2f}\nAccuracy: {acc:.2f}%")

    def reset(self):
        self.started = False
        self.counter = 0
        self.outputs.config(text="Speed(Words/Minute): 0.00\n Speed(Words/second): 0.00\nAccuracy: 0.00")
        self.rantext = gen.sentence()
        self.sample.config(text=self.rantext)
        self.inputs.delete(0,tk.END)
        
            
speedtyping()          
        
        
