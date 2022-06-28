import tkinter as tk
from turtle import width

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}が押されました")

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20
    else:
        pass
    can.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    tori = tk.PhotoImage(file="fig/3.png")
    cx, cy = 300, 400
    can = tk.Canvas(root, width=1500, height=900, background="black")
    can.create_image(cx, cy, image=tori, tag="tori")
    can.pack()
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()