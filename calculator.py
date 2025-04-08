import tkinter as tk

def click(event):
    current = entry.get()
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 18", width=5)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()
