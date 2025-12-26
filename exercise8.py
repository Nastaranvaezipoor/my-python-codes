#تمرین_شماره_هشتم
import tkinter as tk
from tkinter import messagebox

def calculate_dong():
    try:
        bill = float(e1.get())
        people = int(e2.get())
        
        if people == 0:
            messagebox.showwarning("Error", "People count cannot be zero")
            return
            
        result = bill / people
        messagebox.showinfo("Result", f"Each person: {result} Tomans")
        
    except:
        messagebox.showerror("Error", "Please enter numbers only")

root = tk.Tk()
root.title("Dong Calculator")
root.geometry("900x900")

label1 = tk.Label(root, text="Total Bill Amount:")
label1.pack()
e1 = tk.Entry(root)
e1.pack()

label2 = tk.Label(root, text="Number of People:")
label2.pack()
e2 = tk.Entry(root)
e2.pack()

btn = tk.Button(root, text="Calculate Now", command=calculate_dong)
btn.pack()

root.mainloop()
