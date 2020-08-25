from tkinter import *
from tkinter import ttk, colorchooser, filedialog
import PIL
from PIL import ImageGrab

class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
    
    def changeW(self,e):
        self.penwidth = e

    def save(self):
        pass

    def clear(self):
        self.c.delete(ALL)

    def change_fg(self):
        pass
    def change_bg(self):
        pass

    def drawWidgets(self):
        self.controls= Frame(self.master, padx=5, pady=5)
        Label(self.controls, text='Pen Width:', font=('Bell MT',15)).grid(row=0, column=0)
        self.slider = ttk.Scale(self.controls, from_=5, to_ = 100, command = self.changeW,orient= HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1,ipadx=30)
        self.controls.pack()

        self.c = Canvas(self.master, width=500, height=400, bg=self.color_bg,)
        self.c.pack(fill=BOTH, expand=True)


        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        filemenu= Menu(menu)
        menu.add_cascade(label='File..', menu=filemenu)
        filemenu.add_command(label='Export..', command=self.save)
        
        colormenu= Menu(menu)
        menu.add_cascade(label='Colors..', menu=colormenu)
        colormenu.add_command(label = 'Brush Color', command = self.change_fg)
        colormenu.add_command(label = 'Background Color', command = self.change_bg)
        
        optionmenu= Menu(menu)
        menu.add_cascade(label='Option..', menu=optionmenu)
        optionmenu.add_command(label = 'Clear Canvas', command = self.clear)
        optionmenu.add_command(label = 'Exit', command = self.master.destroy)

if __name__=='__main__':
    root = Tk()
    main(root)
    root.title("DrawingApp")
    root.mainloop()