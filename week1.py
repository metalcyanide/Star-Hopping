#to move the image using buttons
import tkinter as tk
import random

# --- globals ---

drops_background = None
drops = None

# --- functions ---

def rain():
    global drops_background
    global drops

    filename = "Intro.png"

    drops = tk.PhotoImage(file=filename) # there is some error in PhotoImage - it have to be assigned to global variable

    drops_background = canvas.create_image(100, 100, image=drops)



def left():
    global drops_background

    canvas.move(image, 10, 0)

def right():
    global drops_background

    canvas.move(image, -10, 0)
    
def up():
    global drops_background

    canvas.move(image, 0, 10)

def down():
    global drops_background

    canvas.move(image, 0, -10)
    
    
root = tk.Tk()

#Create the canvas
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

frame = tk.Frame(root)


rain()

buttonl = tk.Button(frame, 
                   text="Left", 
                   fg="red",
                   command=left)
buttonl.pack(side=tk.LEFT)

buttonr = tk.Button(frame, 
                   text="Right", 
                   fg="red",
                   command=right)
buttonr.pack(side=tk.RIGHT)

buttonu = tk.Button(frame, 
                   text="Up", 
                   fg="red",
                   command=up)
buttonu.pack(side=tk.TOP)

buttond = tk.Button(frame, 
                   text="Down", 
                   fg="red",
                   command=down)
buttond.pack(side=tk.BOTTOM)
frame.pack()

root.mainloop()

# to let the user change the color of a pixel
import tkinter as tk
from PIL import Image, ImageTk

img = Image.new( 'RGB', (500,500), "white") # create a new white image

window = tk.Tk()
canvas = tk.Canvas(window, width=img.size[0], height=img.size[1])
canvas.pack()
image_tk = ImageTk.PhotoImage(img)
canvas.create_image(img.size[0]//2, img.size[1]//2, image=image_tk)

def mouseClick( event):
    x, y = event.x, event.y

    result = askcolor(title = "Colour Chooser") 

    canvas.create_oval(x, y, x, y, fill = result[1])

canvas.bind("<Button-1>", mouseClick)

window.mainloop()