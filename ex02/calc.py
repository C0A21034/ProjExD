import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        e = entry.get()
        ans = eval(e)
        entry.delete(0, tk.END)
        entry.insert(tk.END, ans)

    else:
        #tkm.showinfo("報告", f"[{num}]が押されました")
        entry.insert(tk.END, num)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓君.exe")
    root.geometry("300x600")

    entry = tk.Entry(root,
                    justify="right",
                    width=10,
                    font=("Times New Roman", 40)
                    )
    entry.grid(row=0, column=0, columnspan=3)

    a = 1
    b = 0
    for i, k in enumerate([9,8,7,6,5,4,3,2,1,0,"+","="]):
        btn = tk.Button(root,
                        text=f"{k}",
                        font=("Times New Roman", 30),
                        width=4,
                        height=2)
        btn.grid(row=a, column=b)

        b+=1
        if b == 3:
            a+=1
            b=0
        btn.bind("<1>", button_click)



    root.mainloop()