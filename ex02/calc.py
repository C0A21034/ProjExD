import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓君.exe")
    root.geometry("300x500")

    a = 0
    b = 0
    for i in range(9, -1, -1):
        btn = tk.Button(root, text=f"{i}",font=("Times New Roman", 30),
                        width=4, height=2)
        btn.grid(row=a, column=b)

        b+=1
        if b == 3:
            a+=1
            b=0

    root.mainloop()