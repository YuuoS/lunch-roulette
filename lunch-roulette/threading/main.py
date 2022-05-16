import threading
import time
from tkinter import ttk
import tkinter as tk
import random

import roulette


class GUI(ttk.Frame):
    def __init__(self, root=None, normal_list=None, conf_list=None):
        super().__init__(root)
        self.root = root
        self.root.title("Roulette")
        self.root.geometry("400x350")

        self.normal_list = normal_list
        self.conf_list = conf_list
        self.roulette_list = None
        self.roulette_length = None

        self.text = []
        self.list_len = 5

        self.start_flg = True
        self.index = 0
        self.roulette_speed = 100

        frame1 = ttk.Frame(self.root)
        frame1.pack(padx=20, pady=30)

        self.target_char = tk.StringVar(frame1)
        self.target_char.set('')
        self.text = []

        self.conf_flg = tk.BooleanVar(value=False)
        self.tenho_flg = tk.BooleanVar(value=False)

        for i in range(self.list_len):
            if i == 2:
                font_size = 32
            elif i == 1 or i == 3:
                font_size = 18
            elif i == 0 or i == 4:
                font_size = 8
            self.text.append(tk.StringVar(frame1))
            self.text[i].set('')
            label = ttk.Label(frame1, textvariable=self.text[i],
                              font=("", font_size, "bold"))
            # 各種ウィジェットの設置
            label.grid(row=i, column=1)

        label_left_arrow = ttk.Label(frame1, textvariable=self.target_char, font=("", "20", "bold"))
        label_right_arrow = ttk.Label(frame1, textvariable=self.target_char, font=("", "20", "bold"))
        label_left_arrow.grid(row=2, column=0, sticky=tk.W)
        label_right_arrow.grid(row=2, column=3, sticky=tk.W)

        frame2 = ttk.Frame(self.root)
        frame2.pack(padx=20, pady=10)
        button_start = ttk.Button(frame2, text="start",
                                  command=self.start_roulette,
                                  padding=[5, 10])
        button_stop = ttk.Button(frame2, text="stop",
                                 command=self.stop_roulette,
                                 padding=[5, 10])
        button_start.grid(row=0, column=0, padx=10)
        button_stop.grid(row=0, column=1, padx=10)

        frame3 = ttk.Frame(self.root)
        frame3.pack(padx=20, pady=10)
        check1 = ttk.Checkbutton(frame3, text='会議', variable=self.conf_flg)
        check2 = ttk.Checkbutton(frame3, text='テンホウ', variable=self.tenho_flg)

        check1.grid(row=0, column=0)
        check2.grid(row=0, column=1)

    def start_roulette(self):
        # リスト読み込み
        roulette1 = roulette.Roulette()

        # チェックボックスから分岐
        if self.conf_flg.get():
            roulette1.set_list(self.conf_list)
            roulette1.conf_day()
        elif self.tenho_flg.get():
            roulette1.set_list(self.normal_list)
            roulette1.tuesday()
        else:
            roulette1.set_list(self.normal_list)
            roulette1.normal_day()

        # シャッフル
        roulette1.shuffling_list()
        self.roulette_list = roulette1.shuffled_list
        self.roulette_length = len(self.roulette_list)

        self.start_flg = True
        self.roulette_speed = 50
        self.target_char.set('')
        self.start_event()

    def start_event(self):
        if self.start_flg:
            thread1 = threading.Thread(target=self.update)
            thread1.start()
            self.after(self.roulette_speed, self.start_event)

    def stop_roulette(self):
        thread2 = threading.Thread(target=self.stop_event)
        thread2.start()

    def stop_event(self):
        time.sleep(0.5)
        self.roulette_speed = 200
        time.sleep(1)
        self.roulette_speed = 400
        time.sleep(1)
        self.roulette_speed = 500
        time.sleep(1)
        self.roulette_speed = 700
        self.start_flg = False
        self.target_char.set('✓')

    def update(self):
        roulette_length = self.roulette_length
        roulette_list = self.roulette_list
        i = self.index

        first_num = i % roulette_length
        second_num = (i + 1) % roulette_length
        third_num = (i + 2) % roulette_length
        fourth_num = (i + 3) % roulette_length
        fifth_num = (i + 4) % roulette_length

        show_list = [roulette_list[first_num],
                     roulette_list[second_num],
                     roulette_list[third_num],
                     roulette_list[fourth_num],
                     roulette_list[fifth_num]]

        for j in range(self.list_len):
            self.text[j].set(show_list[j])

        self.index += 1


def main():

    normal_list = ['内山魚店', 'すし友', 'すし友', 'テンホウ', 'はま寿司',
                   'あかいし', '小木曽そば', '刀屋', '檸檬', 'マルコポーロ',
                   '丸源ラーメン', 'マサラキッチン', 'サイゼリヤ', 'ケンタッキー',
                   '西友の弁当', 'ガスト', 'ジャイプール']

    conf_list = ['内山魚店', 'すし友', 'すし友', 'テンホウ', 'はま寿司',
                   'あかいし', '小木曽そば', '刀屋',
                   'マサラキッチン', 'サイゼリヤ', 'ケンタッキー',
                   '西友の弁当', 'ガスト']


    gui = tk.Tk()
    app = GUI(root=gui, normal_list=normal_list, conf_list=conf_list)
    app.mainloop()


if __name__ == '__main__':
    main()
