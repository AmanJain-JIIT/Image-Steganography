#importing required libraries
from tkinter import *
from tkinter import filedialog
from turtle import bgcolor
from PIL import Image, ImageTk
from stegano import exifHeader as stg

#encode function
def encode():

    #defining image open function
    def open():
        fileopen = filedialog.askopenfilename(initialdir="/desktop", title="Select Image", filetypes=(("jpeg file", "*jpg"),))
        
        #encryption function
        stg.hide(fileopen, imageentry.get() + ".jpg", textentry.get())

    #open new window
    newwindow = Toplevel(root)
    newwindow.title("ENCODE")
    newwindow.state("zoomed")

    #defining a frame in new window
    newframe = LabelFrame(newwindow, padx = 200, pady = 200, borderwidth=10, bg = "black")
    newframe.pack(padx = 100, pady = 100)

    #defining text labels in frame
    textlabel = Label(newframe, text = "Enter Text To Be Encrypted : ", padx = 10, pady = 10, fg="white", bg="black")
    textlabel.configure(font = ('Times',20, "bold"))
    textlabel.grid(row = 0, column=0, padx = 20, pady = 20)

    imagelabel = Label(newframe, text = "Enter Name Of Encrypted Image : ", padx = 10, pady = 10, fg="white", bg="black")
    imagelabel.configure(font = ('Times',20, "bold"))
    imagelabel.grid(row = 1, column=0, padx = 20, pady = 20)

    #defining entry boxes in labels
    textentry = Entry(newframe, width = 30, borderwidth=5)
    textentry.configure(font = ('Times',20, "bold"))
    textentry.grid(row = 0, column=1, padx = 20, pady = 20)

    imageentry = Entry(newframe, width =30, borderwidth=5)
    imageentry.configure(font = ('Times',20, "bold"))
    imageentry.grid(row = 1, column=1, padx = 20, pady = 20)

    #defining image select button
    select = Button(newframe, text = "Select Image To Encrypt On", width=25, height=1, padx=20, pady=20, borderwidth=5, command=open)
    select.grid(row=2, column=0, columnspan=2, padx=20, pady=20, ipadx=100)

#defining decode function
def decode():
    fileopen = filedialog.askopenfilename(initialdir="/desktop", title="Select Image", filetypes=(("jpeg file", "*jpg"),))
    
    #decryption function
    dtext = stg.reveal(fileopen)

    #open new window
    newwindow = Toplevel(root)
    newwindow.title("ENCODE")
    newwindow.state("zoomed")

    #defining a frame in new window
    newframe = LabelFrame(newwindow, padx = 200, pady = 200, borderwidth=10, bg = "black")
    newframe.pack(padx = 100, pady = 100)

    #defining text labels in frame
    textlabel = Label(newframe, text = "Decrypted Text Is : ", padx = 10, pady = 10, fg="white", bg="black")
    textlabel.configure(font = ('Times',20, "bold"))
    textlabel.grid(row = 0, column=0, padx = 20, pady = 20)

    decryptlabel = Label(newframe, text = dtext, padx = 10, pady = 10, fg="white", bg="black")
    decryptlabel.configure(font = ('Times',20, "bold"))
    decryptlabel.grid(row = 1, column=0, padx = 20, pady = 20)




#defining main window
root = Tk()
root.title("Image Steganography")
root.state("zoomed")

#defining a frame in main window
frame = LabelFrame(root, padx = 200, pady = 200, borderwidth=10, bg = "black")
frame.pack(padx = 100, pady = 100)

#defining buttons for encode/decode
encodeB = Button(frame, text = "ENCODE", width=25, height=1, padx=20, pady=20, borderwidth=5, command=encode)
encodeB.grid(row=0, column=0, padx=20, pady=20, ipadx=100)
decodeB = Button(frame, text = "DECODE", width=25, height=1, padx=20, pady=20, borderwidth=5, command = decode)
decodeB.grid(row=1, column=0, padx=20, pady=20, ipadx=100)

root.mainloop()
