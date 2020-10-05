from tkinter import *
from PIL import ImageTk, Image
from shutil import copyfile
import os
import sys
from canvas import launch_canvas
from test import launch_acgpn


# Dresses drop-down menu choices
OptionDresses = [
    "000192_1.jpg",
    "000445_1.jpg",
    "001301_1.jpg",
    "001879_1.jpg",
    "002337_1.jpg"
]

# Models drop-down menu choices
OptionModels = [
    "000812_0.jpg",
    "000988_0.jpg",
    "000001_0.jpg",
    "000174_0.jpg",
    "002474_0.jpg"
]

# Clean-up routine for the dataset target locations
for filename in os.listdir('../Data_preprocessing/test_color'):
    os.remove('../Data_preprocessing/test_color/' + filename)

for filename in os.listdir('../Data_preprocessing/test_img'):
    os.remove('../Data_preprocessing/test_img/' + filename)

for filename in os.listdir('../Data_preprocessing/test_label'):
    os.remove('../Data_preprocessing/test_label/' + filename)

root = Tk()
root.title("Demo PyTryOn")

# Models UI images
img1 = ImageTk.PhotoImage(Image.open('pictures/Models/000812_0.jpg'))
img_1 = Label(root, image=img1)
img_1.grid(row=0, column=0)

img2 = ImageTk.PhotoImage(Image.open('pictures/Models/000988_0.jpg'))
img_2 = Label(root, image=img2)
img_2.grid(row=0, column=1)

img3 = ImageTk.PhotoImage(Image.open('pictures/Models/000001_0.jpg'))
img_3 = Label(root, image=img3)
img_3.grid(row=0, column=2)

img4 = ImageTk.PhotoImage(Image.open('pictures/Models/000174_0.jpg'))
img_4 = Label(root, image=img4)
img_4.grid(row=0, column=3)

img5 = ImageTk.PhotoImage(Image.open('pictures/Models/002474_0.jpg'))
img_5 = Label(root, image=img5)
img_5.grid(row=0, column=4)


# Models names
img_lbl_1 = Label(root, text="000812_0.jpg")
img_lbl_2 = Label(root, text="000988_0.jpg")
img_lbl_3 = Label(root, text="000001_0.jpg")
img_lbl_4 = Label(root, text="000174_0.jpg")
img_lbl_5 = Label(root, text="002474_0.jpg")

img_lbl_1.grid(row=1, column=0)
img_lbl_2.grid(row=1, column=1)
img_lbl_3.grid(row=1, column=2)
img_lbl_4.grid(row=1, column=3)
img_lbl_5.grid(row=1, column=4)

# Dresses UI images
dress1 = ImageTk.PhotoImage(Image.open('pictures/dresses/000192_1.jpg'))
dress_1 = Label(root, image=dress1)
dress_1.grid(row=2, column=0)

dress2 = ImageTk.PhotoImage(Image.open('pictures/dresses/000445_1.jpg'))
dress_2 = Label(root, image=dress2)
dress_2.grid(row=2, column=1)

dress3 = ImageTk.PhotoImage(Image.open('pictures/dresses/001301_1.jpg'))
dress_3 = Label(root, image=dress3)
dress_3.grid(row=2, column=2)

dress4 = ImageTk.PhotoImage(Image.open('pictures/dresses/001879_1.jpg'))
dress_4 = Label(root, image=dress4)
dress_4.grid(row=2, column=3)

dress5 = ImageTk.PhotoImage(Image.open('pictures/dresses/002337_1.jpg'))
dress_5 = Label(root, image=dress5)
dress_5.grid(row=2, column=4)

# Dresses names
dress_lbl_1 = Label(root, text="000192_1.jpg")
dress_lbl_2 = Label(root, text="000445_1.jpg")
dress_lbl_3 = Label(root, text="001301_1.jpg")
dress_lbl_4 = Label(root, text="001879_1.jpg")
dress_lbl_5 = Label(root, text="002337_1.jpg")

dress_lbl_1.grid(row=3, column=0)
dress_lbl_2.grid(row=3, column=1)
dress_lbl_3.grid(row=3, column=2)
dress_lbl_4.grid(row=3, column=3)
dress_lbl_5.grid(row=3, column=4)

# Drop-down menues
variableDresses = StringVar(root)
variableModels = StringVar(root)

variableDresses.set("Choose dress")
variableModels.set("Choose Model")

menuDresses = OptionMenu(root, variableDresses, *OptionDresses)
menuModels = OptionMenu(root, variableModels, *OptionModels)

menuModels.grid(row=0, column=5)
menuDresses.grid(row=2, column=5)

# Wapper for the launch of ACGPN
def wrapper_acgpn():
    for filename in os.listdir('../Data_preprocessing/test_label'):
        if filename != variableModels.get()[:8] + '.png':
            os.remove(filename[:8] + '.png')

    if len(os.listdir('../Data_preprocessing/test_label')) == 0:
        copyfile('./pictures/Label/' + variableModels.get()[:8] + '.png',
                 '../Data_preprocessing/test_label/' + variableModels.get()[:8] + '.png')

    copyfile('./pictures/Models/' + variableModels.get(), '../Data_preprocessing/test_img/' + variableModels.get())
    copyfile('./pictures/dresses/' + variableDresses.get(), '../Data_preprocessing/test_color/' + variableDresses.get())

    launch_acgpn()

    preproc_img = Image.open('./sample/' + variableModels.get())
    w, h = preproc_img.size

    Image._show(preproc_img.crop((384, 0, w, h)))

# Launch buttons
btn = Button(root, text="Modify ColorMap", command=launch_canvas)
btn.grid(row=0, column=6)

btn = Button(root, text="LAUNCH ACGPN", command=wrapper_acgpn)
btn.grid(row=2, column=6)

root.mainloop()
