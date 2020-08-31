from tkinter import *
from tkinter import ttk, colorchooser, filedialog
import PIL
from PIL import ImageGrab, ImageTk, Image, ImageDraw
import numpy as np
import os
import glob


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
        file = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*png')], initialfile=self.file[len(self.file)-12:])
        if file:
            x= self.master.winfo_rootx()+self.c.winfo_x()
            y=self.master.winfo_rooty()+self.c.winfo_y()
            x1= x + self.c.winfo_width()
            y1= y + self.c.winfo_height()

            back_to_garyscale(PIL.ImageGrab.grab().crop((x+2,y+2,x1-2,y1-2))).save(file+'.png')
          

            files = glob.glob('pictures/temp/*')
            for f in files:
                os.remove(f)

            

    def importImage(self):
        file=filedialog.askopenfilename()
        self.file=file
        rgb_image=colorize_image(Image.open(self.file))
        rgb_image.save('pictures/temp/'+self.file[len(self.file)-12:])
        self.image2 = ImageTk.PhotoImage(file = 'pictures/temp/'+self.file[len(self.file)-12:])
        print(type(self.image2))
        self.c.create_image(96,130,image = self.image2, anchor=CENTER)
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

       

        #self.image2 = ImageTk.PhotoImage(file = "pictures/000812_0.png")
        #print(type(self.image2))
        self.c = Canvas(self.master, width=192, height=256, bg=self.color_bg,)
        self.c.pack(fill=NONE, expand=False)
        #self.c.create_image(96,130,image = self.image2, anchor=CENTER)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        filemenu= Menu(menu)
        menu.add_cascade(label='File..', menu=filemenu)
        filemenu.add_command(label='Export..', command=self.save)
        filemenu.add_command(label='Import..', command=self.importImage)
        
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


def colorize_image(image):
	# Converte l'immagine da GRAYSCALE a RGB mantenendo la size
	rgb_image = Image.new('RGB', image.size)
	rgb_image.paste(image)

	w, h = rgb_image.size

	# Itera sui pixel dell'immagine per cambio colore
	for x in range(0, w - 1):
		for y in range(0, h - 1):
			# Acquisisce il valore RGB del pixel
			r, g, b = rgb_image.getpixel((x, y))

			# Definizione dei colori
			# Red
			new_color_right_arm = 235, 64, 52
			# Yellow
			new_color_pants = 252, 186, 3
			# Green
			new_color_left_arm = 50, 168, 82
			# Blue
			new_color_shirt = 66, 135, 245
			# Purple
			new_color_face = 128, 52, 235
			# Cyan
			new_color_hair = 52, 235, 217

			# Cambia colori
			if r == g == b == 13:
				rgb_image.putpixel((x, y), new_color_right_arm)
			elif r == g == b == 8:
				rgb_image.putpixel((x, y), new_color_pants)
			elif r == g == b == 11:
				rgb_image.putpixel((x, y), new_color_left_arm)
			elif r == g == b == 4:
				rgb_image.putpixel((x, y), new_color_shirt)
			elif r == g == b == 12:
				rgb_image.putpixel((x, y), new_color_face)
			elif r == g == b == 1:
				rgb_image.putpixel((x, y), new_color_hair)

	return rgb_image


def back_to_garyscale(image):
	gs_image = image.convert('L')

	h, w = gs_image.size

	for x in range(0, h - 1):
		for y in range(0 , w -1):
			gs = gs_image.getpixel((x, y))

			if gs == 114:
				gs_image.putpixel((x, y), 13)
			elif gs == 185:
				gs_image.putpixel((x, y), 8)
			elif gs == 123:
				gs_image.putpixel((x, y), 11)
			elif gs == 127:
				gs_image.putpixel((x, y), 4)
			elif gs == 96:
				gs_image.putpixel((x, y), 12)
			elif gs == 178:
				gs_image.putpixel((x, y), 1)

	return gs_image


if __name__=='__main__':
    root = Tk()
    main(root)
    root.title("DrawingApp")
    root.mainloop()