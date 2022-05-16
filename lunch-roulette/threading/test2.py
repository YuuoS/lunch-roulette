import tkinter as tk
from tkinter import ttk
import threading


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x300")
        self.master.title("Test")

        self.text = []
        self.list_len = 0
        self.count = 0

        view_list = ["1", "2", "3", "4", "5"]
        self.list_len = len(view_list)

        frame1 = ttk.Frame(self.master)
        frame1.pack(padx=20, pady=10)

        self.text = []
        for i in range(len(view_list)):
            self.text.append(tk.StringVar(frame1))
            self.text[i].set(view_list[i])
            label = ttk.Label(frame1, textvariable=self.text[i])
            label.grid(row=i, column=0)

        frame2 = ttk.Frame(self.master)
        frame2.pack(padx=20, pady=30)
        button_start = ttk.Button(frame2, text="start")
        button_stop = ttk.Button(frame2, text="stop")
        button_change = ttk.Button(frame2, text="change")
        button_start.grid(row=0, column=0)
        button_stop.grid(row=0, column=1)
        button_change.grid(row=1, column=0, columnspan=2)

        self.timeEvent()

    # タイマー起動用関数
    def timeEvent(self):
        th = threading.Thread(target=self.update)
        th.start()
        self.after(100, self.timeEvent)

    # スレッド処理実体
    def update(self):
        self.count += 1
        print(self.count)
        for i in range(self.list_len):
            self.text[i].set(int(self.text[i].get()) + 1)


if __name__ == "__main__":
    gui = tk.Tk()
    app = GUI(master=gui)
    app.mainloop()
