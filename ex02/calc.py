import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo("報告", f"[{num}]が押されました")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓君.exe")
    root.geometry("300x500")

    #entry = tk.Entry(root, justify="right", width=10, font=(Times New Roman, 40))
    #entry.grid(row=0, column=0, columnspan=3)

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
        btn.bind("<1>", button_click)



    root.mainloop()