import tkinter as tk
import tkinter.messagebox as tkm
import tkinter.scrolledtext as tks
import typeNwriteMain as tNw
import text_extract as txte
from functools import partial

spacing = tNw.spacing

def get_copy():
    global e1,e2
    txt = e1.get('1.0', tk.END)
    pf = e2.get()
    tNw.createfile(txt,pf)

def extract_letters():
    global e3,e4,win
    # print()
    txte.make_pf(e4.get(),e3.get())
    tkm.showinfo("Done","Profile has been created successfully!")
    win.destroy()
# source,target

def make_profile():
    global e3,e4,win
    win = tk.Tk()
    sframe = tk.Frame(win,bg="#000000",height=sHeight//4,width=sWidth//4)
    sframe.pack(side='left')
    l3 = tk.Label(sframe,bg='#000000',fg='#ffffff',text="Profile Name")
    l3.grid(row=0,column=0,pady=2,padx=2)

    e3 = tk.Entry(sframe,bg='#000000',fg='#ffffff',highlightcolor="#66ffcc")
    e3.grid(row=0,column=1,pady=2,padx=2)

    l4 = tk.Label(sframe,bg='#000000',fg='#ffffff',text="Folder")
    l4.grid(row=1,column=0,pady=2,padx=2)

    e4 = tk.Entry(sframe,bg='#000000',fg='#ffffff',highlightcolor="#66ffcc")
    e4.grid(row=1,column=1,pady=2,padx=2)
    
    b2 = tk.Button(sframe,activeforeground='#ffffff',activebackground='#323232',bg="#000000",fg="#ffffff",text='Create',command=extract_letters)#,command=partial(extract_letters,e3.get(),e4.get())
    b2.grid(row=2,column=1,pady=2,padx=2)


root = tk.Tk()
root.title = 'TypeNwrite'
sWidth = root.winfo_screenwidth()
sHeight = root.winfo_screenheight()

menu = tk.Menu(root,title="Menu",activebackground="#323232",activeforeground="#ffffff",bg="#000000",fg="#ffffff")
root.config(menu=menu)

mmenu=tk.Menu(menu,activebackground="#323232",activeforeground="#ffffff",bg="#000000",fg="#ffffff")
menu.add_cascade(label = "Menu",menu = mmenu)
mmenu.add_command(label="Create new profile",command=make_profile)
mmenu.add_command(label="Help")

canvas=tk.Canvas(root,bg="#000000",height=sHeight,width=sWidth)

canvas.pack()

frame = tk.Frame(canvas,bg="#000000",height=sHeight,width=sWidth)
frame.pack(side='left')

l1 = tk.Label(frame,bg='#000000',fg='#ffffff',text="Input")
l1.grid(row=0,column=0,pady=2,padx=2)

e1 = tks.ScrolledText(frame,bg='#000000',fg='#ffffff',highlightcolor="#66ffcc",width=40,height=8)
e1.grid(row=0,column=1,pady=2,padx=2)

l2 = tk.Label(frame,bg='#000000',fg='#ffffff',text="Profile")
l2.grid(row=1,column=0,pady=2,padx=2)

e2 = tk.Entry(frame,bg='#000000',fg='#ffffff',width=40,highlightcolor="#66ffcc")
e2.grid(row=1,column=1,pady=2)

b1 = tk.Button(frame,activeforeground='#ffffff',activebackground='#323232',bg="#000000",fg="#ffffff",text='get copy',command=get_copy)
b1.grid(row=2,column=1,pady=2,padx=2)


root.mainloop()
