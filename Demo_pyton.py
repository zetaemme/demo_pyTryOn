from tkinter import *
from tkinter import messagebox
import PIL
from PIL import ImageGrab, ImageTk, Image, ImageDraw

OptionDresses =  [
    "000192_1.jpg",
    "000445_1.jpg",
    "001301_1.jpg",
    "001879_1.jpg",
    "002337_1.jpg"
]

OptionModels =  [
    "000812_0.png",
    "000988_0.png",
    "000001_0.png",
    "000174_0.png",
    "002474_0.png"
]

root = Tk()
root.title("PYTON")


img1 = ImageTk.PhotoImage(Image.open('./pictures/000812_0.png'))
img_1= Label(root, image=img1)
img_1.grid(row=0, column=0)

img2 = ImageTk.PhotoImage(Image.open('./pictures/000988_0.png'))
img_2= Label(root, image=img2)
img_2.grid(row=0, column=1)

img3 = ImageTk.PhotoImage(Image.open('./pictures/000001_0.png'))
img_3= Label(root, image=img3)
img_3.grid(row=0, column=2)

img4 = ImageTk.PhotoImage(Image.open('./pictures/000174_0.png'))
img_4= Label(root, image=img4)
img_4.grid(row=0, column=3)

img5 = ImageTk.PhotoImage(Image.open('./pictures/002474_0.png'))
img_5= Label(root, image=img5)
img_5.grid(row=0, column=4)


img_lbl_1=Label(root, text="000812_0.png")
img_lbl_2=Label(root, text="000988_0.png")
img_lbl_3=Label(root, text="000001_0.png")
img_lbl_4=Label(root, text="000174_0.png")
img_lbl_5=Label(root, text="002474_0.png")

img_lbl_1.grid(row=1, column=0)
img_lbl_2.grid(row=1, column=1)
img_lbl_3.grid(row=1, column=2)
img_lbl_4.grid(row=1, column=3)
img_lbl_5.grid(row=1, column=4)

dress1 = ImageTk.PhotoImage(Image.open('./pictures/000192_1.jpg'))
dress_1= Label(root, image=dress1)
dress_1.grid(row=2, column=0)

dress2 = ImageTk.PhotoImage(Image.open('./pictures/000445_1.jpg'))
dress_2= Label(root, image=dress2)
dress_2.grid(row=2, column=1)

dress3 = ImageTk.PhotoImage(Image.open('./pictures/001301_1.jpg'))
dress_3= Label(root, image=dress3)
dress_3.grid(row=2, column=2)

dress4 = ImageTk.PhotoImage(Image.open('./pictures/001879_1.jpg'))
dress_4= Label(root, image=dress4)
dress_4.grid(row=2, column=3)

dress5 = ImageTk.PhotoImage(Image.open('./pictures/002337_1.jpg'))
dress_5= Label(root, image=dress5)
dress_5.grid(row=2, column=4)

dress_lbl_1=Label(root, text="000192_1.jpg")
dress_lbl_2=Label(root, text="000445_1.jpg")
dress_lbl_3=Label(root, text="001301_1.jpg")
dress_lbl_4=Label(root, text="001879_1.jpg")
dress_lbl_5=Label(root, text="002337_1.jpg")

dress_lbl_1.grid(row=3, column=0)
dress_lbl_2.grid(row=3, column=1)
dress_lbl_3.grid(row=3, column=2)
dress_lbl_4.grid(row=3, column=3)
dress_lbl_5.grid(row=3, column=4)


variableDresses = StringVar(root)
variableModels = StringVar(root)

variableDresses.set("Choose dress")
variableModels.set("Choose Model")


menuDresses= OptionMenu(root,variableDresses,*OptionDresses)
menuModels= OptionMenu(root,variableModels,*OptionModels)


menuModels.grid(row=0,column=5)
menuDresses.grid(row=2,column=5)

def lauchCanvas():
    messagebox.showinfo('Message', 'You clicked the Submit button!')

btn = Button(root, text = "Modify ColorMap", command=lauchCanvas) 
btn.grid(row = 0, column = 6)

def lauchACGPN():
    messagebox.showinfo('Message', 'You clicked the Submit button!')
    
btn = Button(root, text = "LAUNCH ACGPN", command=lauchACGPN) 
btn.grid(row = 2, column = 6)

root.mainloop()