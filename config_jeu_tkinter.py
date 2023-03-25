from tkinter import *

def callback(selection):
    return(selection)

def config_jeu_visuel():
    root=Tk()
    root.title('2048')
    choices=['Default', 'Chemistry', 'Alphabet']
    texte1=Label(text="Choose grid size :", bg="white")
    variable=StringVar(root)
    variable.set('Default')
    variable.trace_add('write', lambda *args: print(variable.get()))
    menutaille=Scale(root, orient='horizontal', from_=2, to=10, resolution=1,length=200)
    menutaille.set(4)
    texte2=Label(text="Choose a theme", bg="white")
    menutheme=OptionMenu(root, variable, *choices, command=callback)

    quitbutton=Button(root, text="Quit", command=quit)
    savebutton=Button(root, text="Save")
    playbutton=Button(root, text="Play")
    retourbutton=Button(root, text="Retour")

    texte1.grid(row=0, column=2)
    menutaille.grid(row=1, column=2)
    texte2.grid(row=2, column=2)
    menutheme.grid(row=3, column=2)
    quitbutton.grid(row=5, column=0)
    savebutton.grid(row=5, column=3)
    playbutton.grid(row=5, column=1)
    retourbutton.grid(row=5, column=4)

    # texte1.pack()
    # menutaille.pack()
    # texte2.pack()
    # menutheme.pack()
    # quitbutton.pack()
    # savebutton.pack()
    # playbutton.pack()
    root.mainloop()

config_jeu_visuel()