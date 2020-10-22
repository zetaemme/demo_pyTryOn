<<<<<<< HEAD:inference/canvas.py
from tkinter import *
from tkinter import ttk, colorchooser, filedialog
import PIL
from PIL import ImageTk, Image
import os
import glob
from random import sample
import pyscreenshot as ImageGrab


class Main:
    def __init__(self, master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'black'
        
        #Color:
        self.new_color_right_arm = "#BE0182"
        self.new_color_pants = "#3E0100"
        self.new_color_left_arm = "#BD8101"
        self.new_color_face = "#3D007F"
        self.new_color_hair = "#800002"

        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
    
    def paint(self, e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth,
                               fill=self.color_fg, capstyle=ROUND, smooth=True)
        
        self.old_x = e.x
        self.old_y = e.y

    def reset(self):
        self.old_x = None
        self.old_y = None

    def changeW(self, e):
        self.penwidth = e

    def save(self):
        filename = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics', '*png')],
                                            initialfile=self.file[len(self.file)-12:])
        if filename:
            x = self.master.winfo_rootx()+self.c.winfo_x()
            y = self.master.winfo_rooty()+self.c.winfo_y()
            x1 = x + self.c.winfo_width()
            y1 = y + self.c.winfo_height()

            back_to_grayscale(ImageGrab.grab().crop((x + 2, y + 2, x1 - 2, y1 - 2))).save(filename + '.png')

    def importImage(self):
        filename = filedialog.askopenfilename()
        self.filename = filename

        rgb_image = colorize_image(Image.open(self.filename))
        rgb_image.save('./pictures/temp/' + self.filename[len(self.filename) - 12:])

        self.image2 = ImageTk.PhotoImage(file='./pictures/temp/' + self.filename[len(self.filename) - 12:])
        self.c.create_image(96, 130, image=self.image2, anchor=CENTER)

    def clear(self):
        self.c.delete(ALL)

    def change_fg_RA(self):
        self.color_fg = self.new_color_right_arm

    def change_fg_LA(self):
        self.color_fg = self.new_color_left_arm

    def change_fg_P(self):
        self.color_fg = self.new_color_pants

    def change_fg_F(self):
        self.color_fg = self.new_color_face

    def change_fg_H(self):
        self.color_fg = self.new_color_hair

    def change_fg(self):
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1] 

    def change_bg(self):
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    def drawWidgets(self):
        self.controls = Frame(self.master, padx=5, pady=5)
        Label(self.controls, text='Pen Width:', font=('Berlin Sans FB', 15)).grid(row=0, column=0)
        self.slider = ttk.Scale(self.controls, from_=5, to_=100, command=self.changeW, orient=HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1, ipadx=30)
        self.controls.pack()

        # self.image2 = ImageTk.PhotoImage(file = "pictures/000812_0.png")
        # print(type(self.image2))
        self.c = Canvas(self.master, width=192, height=256, bg=self.color_bg,)
        self.c.pack(fill=NONE, expand=False)
        # self.c.create_image(96,130,image = self.image2, anchor=CENTER)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        filemenu = Menu(menu)
        menu.add_cascade(label='File..', menu=filemenu)
        filemenu.add_command(label='Export..', command=self.save)
        filemenu.add_command(label='Import..', command=self.importImage)
        
        colormenu = Menu(menu)
        menu.add_cascade(label='Colors..', menu=colormenu)
        colormenu.add_command(label='Brush Right Arm', command=self.change_fg_RA)
        colormenu.add_command(label='Brush Left Arm', command=self.change_fg_LA)
        colormenu.add_command(label='Brush Pants', command=self.change_fg_P)
        colormenu.add_command(label='Brush Face', command=self.change_fg_F)
        colormenu.add_command(label='Brush Hair', command=self.change_fg_H)
        colormenu.add_command(label='Brush Color', command=self.change_fg)
        colormenu.add_command(label='Background Color', command=self.change_bg)
        
        optionmenu = Menu(menu)
        menu.add_cascade(label='Option..', menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas', command=self.clear)
        optionmenu.add_command(label='Exit', command=self.master.destroy)


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
            #new_color_right_arm = 235, 64, 52
            # Yellow
            #new_color_pants = 252, 186, 3
            # Green
            #new_color_left_arm = 50, 168, 82
            # Blue
            # new_color_shirt = 66, 135, 245
            # Purple
            #new_color_face = 128, 52, 235
            # Cyan
            #new_color_hair = 52, 235, 217

            new_color_right_arm = 190, 1, 130
            new_color_left_arm = 189, 130, 1
            new_color_face = 62, 0 , 127
            new_color_hair = 128, 0, 2
            new_color_pants = 62, 1, 0

            # Cambia colori
            if r == g == b == 13:
                rgb_image.putpixel((x, y), new_color_right_arm)
            elif r == g == b == 8:
                rgb_image.putpixel((x, y), new_color_pants)
            elif r == g == b == 11:
                rgb_image.putpixel((x, y), new_color_left_arm)
            # elif r == g == b == 4:
                # rgb_image.putpixel((x, y), new_color_shirt)
            elif r == g == b == 12:
                rgb_image.putpixel((x, y), new_color_face)
            elif r == g == b == 1:
                rgb_image.putpixel((x, y), new_color_hair)
    
    return rgb_image


def back_to_grayscale(image):
    gs_image = image.convert('L')

    h, w = gs_image.size
    
    for x in range(0, h - 1):
        for y in range(0, w - 1):
            gs = gs_image.getpixel((x, y))
            
            if gs == 72:
                gs_image.putpixel((x, y), 13)
            elif gs == 19:
                gs_image.putpixel((x, y), 8)
            elif gs == 133:
                gs_image.putpixel((x, y), 11)
            # elif gs == 127:
                # gs_image.putpixel((x, y), 4)
            elif gs == 33:
                gs_image.putpixel((x, y), 12)
            elif gs == 38:
                gs_image.putpixel((x, y), 1)
                
    return gs_image


def launch_canvas():
    if not os.path.exists('./pictures/temp'):
        os.mkdir('./pictures/temp')

    for f in glob.glob('./pictures/temp/*'):
        os.remove(f)

    # Vecchio codice per pulizia dataset

    # img_selection = [[str(s) for s in line.split()] for line in open('./Data_preprocessing/demo_dataset.txt').readlines()]
    # img_selection = [str(item)[2:14] for item in img_selection]
    #
    # for filename in os.listdir('./Data_preprocessing/test_label'):
    #     if filename not in img_selection:
    #         os.remove('./Data_preprocessing/test_label/' + filename)
    #
    # img_selection = [item.replace('.png', '.jpg') for item in img_selection]
    #
    # for filename in os.listdir('./Data_preprocessing/test_img'):
    #     if filename not in img_selection:
    #         os.remove('./Data_preprocessing/test_img/' + filename)
    #
    # color_files = [filename for filename in os.listdir('./Data_preprocessing/test_color')]
    #
    # if len(color_files) > 10:
    #     for f in sample(os.listdir('./Data_preprocessing/test_color'), 2022):
    #         os.remove('./Data_preprocessing/test_color/' + f)
    #
    # edge_files = [filename for filename in os.listdir('./Data_preprocessing/test_edge')]
    #
    # for filename in os.listdir('./Data_preprocessing/test_edge'):
    #     if filename not in edge_files:
    #         os.remove('./Data_preprocessing/test_edge' + filename)

    root = Tk()
    Main(root)
    root.title("Canvas: Modify Labels")
    root.mainloop()


if __name__ == '__main__':
=======
from tkinter import *
from tkinter import ttk, colorchooser, filedialog
import PIL
from PIL import ImageTk, Image
import os
import glob
from random import sample
import pyscreenshot as ImageGrab


# Main UI class
class Main:
    def __init__(self, master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'black'
        
        #Color:
        self.new_color_right_arm = "#BE0182"
        self.new_color_pants = "#3E0100"
        self.new_color_left_arm = "#BD8101"
        self.new_color_face = "#3D007F"
        self.new_color_hair = "#800002"

        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
    
    # Creates actual UI response for paint action
    def paint(self, e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth,
                               fill=self.color_fg, capstyle=ROUND, smooth=True)
        
        self.old_x = e.x
        self.old_y = e.y

    # Resets x, y position for the brush
    def reset(self):
        self.old_x = None
        self.old_y = None

    # Cheanges brush width
    def changeW(self, e):
        self.penwidth = e

    # Saves the image on the filesystem
    def save(self):
        filename = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics', '*png')],
                                            initialfile=self.file[len(self.file)-12:])
        if filename:
            x = self.master.winfo_rootx()+self.c.winfo_x()
            y = self.master.winfo_rooty()+self.c.winfo_y()
            x1 = x + self.c.winfo_width()
            y1 = y + self.c.winfo_height()

            back_to_grayscale(ImageGrab.grab().crop((x + 2, y + 2, x1 - 2, y1 - 2))).save(filename + '.png')

    # Opens an image
    def importImage(self):
        filename = filedialog.askopenfilename()
        self.filename = filename

        rgb_image = colorize_image(Image.open(self.filename))
        rgb_image.save('./pictures/temp/' + self.filename[len(self.filename) - 12:])

        self.image2 = ImageTk.PhotoImage(file='./pictures/temp/' + self.filename[len(self.filename) - 12:])
        self.c.create_image(96, 130, image=self.image2, anchor=CENTER)

    # Deletes all on screen
    def clear(self):
        self.c.delete(ALL)

    # Changes the brush color
    def change_fg_RA(self):
        self.color_fg = self.new_color_right_arm

    def change_fg_LA(self):
        self.color_fg = self.new_color_left_arm

    def change_fg_P(self):
        self.color_fg = self.new_color_pants

    def change_fg_F(self):
        self.color_fg = self.new_color_face

    def change_fg_H(self):
        self.color_fg = self.new_color_hair

    def change_fg(self):
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1] 

    def change_bg(self):
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    # Draws the UI
    def drawWidgets(self):
        self.controls = Frame(self.master, padx=5, pady=5)
        Label(self.controls, text='Pen Width:', font=('Berlin Sans FB', 15)).grid(row=0, column=0)
        self.slider = ttk.Scale(self.controls, from_=5, to_=100, command=self.changeW, orient=HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1, ipadx=30)
        self.controls.pack()

        # self.image2 = ImageTk.PhotoImage(file = "pictures/000812_0.png")
        # print(type(self.image2))
        self.c = Canvas(self.master, width=192, height=256, bg=self.color_bg,)
        self.c.pack(fill=NONE, expand=False)
        # self.c.create_image(96,130,image = self.image2, anchor=CENTER)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        filemenu = Menu(menu)
        menu.add_cascade(label='File..', menu=filemenu)
        filemenu.add_command(label='Export..', command=self.save)
        filemenu.add_command(label='Import..', command=self.importImage)
        
        colormenu = Menu(menu)
        menu.add_cascade(label='Colors..', menu=colormenu)
        colormenu.add_command(label='Brush Right Arm', command=self.change_fg_RA)
        colormenu.add_command(label='Brush Left Arm', command=self.change_fg_LA)
        colormenu.add_command(label='Brush Pants', command=self.change_fg_P)
        colormenu.add_command(label='Brush Face', command=self.change_fg_F)
        colormenu.add_command(label='Brush Hair', command=self.change_fg_H)
        colormenu.add_command(label='Brush Color', command=self.change_fg)
        colormenu.add_command(label='Background Color', command=self.change_bg)
        
        optionmenu = Menu(menu)
        menu.add_cascade(label='Option..', menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas', command=self.clear)
        optionmenu.add_command(label='Exit', command=self.master.destroy)

# Turns the label image to RGB, for better interpretation
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

            new_color_right_arm = 190, 1, 130
            new_color_left_arm = 189, 130, 1
            new_color_face = 62, 0 , 127
            new_color_hair = 128, 0, 2
            new_color_pants = 62, 1, 0

            # Cambia colori
            if r == g == b == 13:
                rgb_image.putpixel((x, y), new_color_right_arm)
            elif r == g == b == 8:
                rgb_image.putpixel((x, y), new_color_pants)
            elif r == g == b == 11:
                rgb_image.putpixel((x, y), new_color_left_arm)
            elif r == g == b == 12:
                rgb_image.putpixel((x, y), new_color_face)
            elif r == g == b == 1:
                rgb_image.putpixel((x, y), new_color_hair)
    
    return rgb_image

# Turns the label back to grayscale before saving
def back_to_grayscale(image):
    gs_image = image.convert('L')

    h, w = gs_image.size
    
    for x in range(0, h - 1):
        for y in range(0, w - 1):
            gs = gs_image.getpixel((x, y))
            
            if gs == 72:
                gs_image.putpixel((x, y), 13)
            elif gs == 19:
                gs_image.putpixel((x, y), 8)
            elif gs == 133:
                gs_image.putpixel((x, y), 11)
            elif gs == 33:
                gs_image.putpixel((x, y), 12)
            elif gs == 38:
                gs_image.putpixel((x, y), 1)
                
    return gs_image

# Wrapper for the whole DrawingApp
def launch_canvas():
    if not os.path.exists('./pictures/temp'):
        os.mkdir('./pictures/temp')

    for f in glob.glob('./pictures/temp/*'):
        os.remove(f)

    root = Tk()
    Main(root)
    root.title("Canvas: Modify Labels")
    root.mainloop()


if __name__ == '__main__':
>>>>>>> 93f5be76a2540307ba491d746d6f8988b37dc701:canvas.py
    launch_canvas()