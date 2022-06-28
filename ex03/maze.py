import tkinter as tk
from tokenize import maybe
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}が押されました")

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up":
        if maze_bg[my-1][mx] == 0:
            my -= 1
    elif key == "Down":
        if maze_bg[my+1][mx] == 0:
            my += 1
    elif key == "Left":
        if maze_bg[my][mx-1] == 0:
            mx -= 1
    elif key == "Right":
        if maze_bg[my][mx+1] == 0:
            mx += 1
    else:
        pass
    cx, cy = mx*100+50, my*100+50
    can.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    tori = tk.PhotoImage(file="fig/3.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    can = tk.Canvas(root, width=1500, height=900, background="black")
    maze_bg = mm.make_maze(15, 9)   #壁と床のリストを作る
    mm.show_maze(can, maze_bg)  #canvasにmaze_bgを書いている
    can.create_image(cx, cy, image=tori, tag="tori")
    can.pack()

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()