from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)  # кладем в переменную полученную картинку
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS) # адаптируем размер картинки под экран
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Some error have happened!")
        return None


def set_image():
    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img


window = Tk()
window.title("Cutie patootie")
window.geometry("600x520")

label = Label()
label.pack()

update_button = Button(text="Get a new one", command=set_image)
update_button.pack()

url = "https://cataas.com/cat"

set_image()

window.mainloop()
