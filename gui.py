import tkinter as tk
import tkinter.scrolledtext as tks
import subprocess
import typeNwriteMain as tNw

spacing = tNw.spacing

def get_copy():
    global e1,e2
    txt = e1.get('1.0', tk.END)
    pf = e2.get()
    tNw.createfile(txt,pf)
    # subprocess.call(['python3','typeNwriteMain.py',txt,pf])


root = tk.Tk()
root.title = 'TypeNwrite'
sWidth = root.winfo_screenwidth()
sHeight = root.winfo_screenheight()


canvas=tk.Canvas(root,bg="#000000",height=sHeight,width=sWidth)

canvas.pack()

frame = tk.Frame(canvas,bg="#000000",height=sHeight,width=sWidth)
frame.pack(side='top')

l1 = tk.Label(frame,bg='#000000',fg='#ffffff',text="Input")
l1.grid(row=0,column=0,pady=2)

e1 = tks.ScrolledText(frame,bg='#000000',fg='#ffffff',highlightcolor="#00ff00",width=40,height=8)
e1.grid(row=1,column=0,pady=2)

l2 = tk.Label(frame,bg='#000000',fg='#ffffff',text="Profile")
l2.grid(row=2,column=0,pady=2)

e2 = tk.Entry(frame,bg='#000000',fg='#ffffff',highlightcolor="#00ff00")
e2.grid(row=3,column=0,pady=2)

b1 = tk.Button(frame,activeforeground='#ffffff',activebackground='#323232',bg="#000000",fg="#ffffff",text='get copy',command=get_copy)
b1.grid(row=4,column=0,pady=2)
root.mainloop()
