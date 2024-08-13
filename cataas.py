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
        print(f"Some error have happened: {e}")
        return None


def open_new_window():
    img = load_image(url)

    if img:
        new_window = Toplevel()
        new_window.title("Kitty's image")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img

def exit():
    window.destroy()


window = Tk()
window.title("Cutie patootie")
window.geometry("600x520")

# update_button = Button(text="More cats", command=set_image)
# update_button.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Get photo", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

url = "https://cataas.com/cat"

set_image()

window.mainloop()
