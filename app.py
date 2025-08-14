import tkinter as tk
from tkinter import filedialog, messagebox
from analysis import load_data, plot_unemployment_rate

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filepath:
        try:
            df = load_data(filepath)
            plot_unemployment_rate(df)
        except Exception as e:
            messagebox.showerror("Error", f"Could not process file:\n{e}")

root = tk.Tk()
root.title("Unemployment Analysis Tool")
root.geometry("400x200")

tk.Label(root, text="Unemployment Analysis", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="Open Dataset", command=open_file, width=20, height=2).pack(pady=20)

root.mainloop()
