from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image():
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content) # кладем в переменную полученную картинку
        img = Image.open(Image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Some mistakes have happened!")
        return None


window = Tk()
window.title("Cutie patootie")
window.geometry("600x400")

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()















