from tkinter import *
from tkinter import ttk, colorchooser, filedialog
import PIL
from PIL import ImageGrab, ImageTk, Image, ImageDraw

class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'black'
        
        #Color:
        self.new_color_right_arm = "#EB4034"
        self.new_color_pants ="#FCBA03"
        self.new_color_left_arm = "#32A852"
        self.new_color_shirt = "#4287F5"
        self.new_color_face = "#8034EB"
        self.new_color_hair = "#34EBD9"

        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)
    
    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)
        
        self.old_x = e.x
        self.old_y = e.y

    def reset(self,e):
        self.old_x = None
        self.old_y = None

    def changeW(self,e):
        self.penwidth = e

    def save(self):
        file = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*png')])
        if file:
            x= self.master.winfo_rootx()+self.c.winfo_x()
            y=self.master.winfo_rooty()+self.c.winfo_y()
            x1= x + self.c.winfo_width()
            y1= y + self.c.winfo_height()

            PIL.ImageGrab.grab().crop((x+2,y+2,x1-2,y1-2)).save(file+'.png')

    def clear(self):
        self.c.delete(ALL)

    def change_fg_RA(self):
        self.color_fg = self.new_color_right_arm
    def change_fg_LA(self):
        self.color_fg = self.new_color_left_arm    
    def change_fg_S(self):
        self.color_fg = self.new_color_shirt
    def change_fg_P(self):
        self.color_fg = self.new_color_pants
    def change_fg_F(self):
        self.color_fg = self.new_color_face
    def change_fg_H(self):
        self.color_fg =  self.new_color_hair

    def change_fg(self):
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1] 

    def change_bg(self):
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg']=self.color_bg

    def drawWidgets(self):

        self.controls= Frame(self.master, padx=5, pady=5)
        Label(self.controls, text='Pen Width:', font=('Berlin Sans FB',15)).grid(row=0, column=0)
        self.slider = ttk.Scale(self.controls, from_=5, to_ = 100, command = self.changeW,orient= HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1,ipadx=30)
        self.controls.pack()

       

        self.image2 = ImageTk.PhotoImage(file = "pictures/000001_0.png")
        self.c = Canvas(self.master, width=192, height=256, bg=self.color_bg,)
        self.c.pack(fill=NONE, expand=False)
        self.c.create_image(96,128,image = self.image2, anchor=CENTER)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        filemenu= Menu(menu)
        menu.add_cascade(label='File..', menu=filemenu)
        filemenu.add_command(label='Export..', command=self.save)
        
        colormenu= Menu(menu)
        menu.add_cascade(label='Colors..', menu=colormenu)
        colormenu.add_command(label = 'Brush Right Arm', command = self.change_fg_RA)
        colormenu.add_command(label = 'Brush Left Arm', command = self.change_fg_LA)
        colormenu.add_command(label = 'Brush Pants', command = self.change_fg_P)
        colormenu.add_command(label = 'Brush Shirt', command = self.change_fg_S)
        colormenu.add_command(label = 'Brush Face', command = self.change_fg_F)
        colormenu.add_command(label = 'Brush Hair', command = self.change_fg_H)
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