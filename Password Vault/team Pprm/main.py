import tkinter as tk  # python 3
from handlers.login_handler import LoginHandler
from app_database import database as db
from PIL import ImageTk, Image

class PPRM(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.minsize(self, 750, 600)

        self.title("TEAM PPRM")
        self.wm_iconbitmap("Image\\cloud-computing.ico")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        LoginHandler(parent=container, controller=self)
        db()


def app_window():
    app = PPRM()
    app.mainloop()


if __name__ == "__main__":
    splash = tk.Tk()
    splash.geometry("500x500+350+150")
    splash.resizable(width=False, height=False)
    splash.overrideredirect(True)
    my_canvas = tk.Canvas(splash)
    my_canvas.pack(fill='both', expand='true')


    def resizer(e):
        global splash_img, resize_image, new_bg
        splash_img = Image.open("E:\\team Pprm\Image\splash.png")
        resize_image = splash_img.resize((e.width, e.height), Image.ANTIALIAS)
        new_bg = ImageTk.PhotoImage(resize_image)
        my_canvas.create_image(0, 0, image=new_bg, anchor='nw')


    splash.bind("<Configure>", resizer)
    splash.after(3000, splash.destroy)
    splash.mainloop()
    app_window()
