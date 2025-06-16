import tkinter as tk
from tkinter import messagebox
from train import train_agent
from play import play_and_record

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LunarLander AI Trainer")
        self.geometry("400x300")

        tk.Label(self, text="Training Parameters").pack(pady=10)

        tk.Label(self, text="Total Timesteps:").pack()
        self.timesteps_entry = tk.Entry(self)
        self.timesteps_entry.insert(0, "500000")
        self.timesteps_entry.pack()

        tk.Button(self, text="Start Training", command=self.start_training).pack(pady=10)
        tk.Button(self, text="Play & Record", command=self.play_agent).pack(pady=10)

    def start_training(self):
        try:
            ts = int(self.timesteps_entry.get())
            train_agent(total_timesteps=ts)
            messagebox.showinfo("Training", "Training completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def play_agent(self):
        try:
            play_and_record()
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = App()
    app.mainloop()