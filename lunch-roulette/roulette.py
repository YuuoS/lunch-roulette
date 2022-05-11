import csv
import sys
import time
import random
from pynput import keyboard


class Roulette:

    def __init__(self):
        self.input_list = []
        self.roulette_list = []
        self.loop_flg = True

    def create_list(self):
        csv_path = './restaurant.csv'
        with open(csv_path, encoding='utf-8') as f:
            reader = csv.reader(f)

            for row in reader:
                self.input_list.append(str(row[0]))
                if int(row[1]) > 1:
                    for i in range(int(row[1]) - 1):
                        self.input_list.append(str(row[0]))

    def append_gakusyoku(self):
        for row in range(int(len(self.input_list) / 3 * 7)):
            self.input_list.append('学食')

    def append_tenhou(self):
        for row in range(int(len(self.input_list) / 3 * 7 / 2)):
            self.input_list.append('学食')
            self.input_list.append('テンホウ')

    def shuffling_list(self):
        self.roulette_list = self.input_list.copy()
        random.shuffle(self.roulette_list)

    def run_roulette(self):
        roulette_length = len(self.roulette_list)

        i = 0
        while self.loop_flg:
            first_num = i % roulette_length
            second_num = (i + 1) % roulette_length
            third_num = (i + 2) % roulette_length
            fourth_num = (i + 3) % roulette_length
            fifth_num = (i + 4) % roulette_length
            print("\r" + f'{self.roulette_list[first_num]:12s} '
                         f'{self.roulette_list[second_num]:12s} '
                         f'{self.roulette_list[third_num]:12s} '
                         f'{self.roulette_list[fourth_num]:12s} '
                         f'{self.roulette_list[fifth_num]:12s}', end="")
            time.sleep(0.05)
            i += 1

    def press(self, key):
        x = random.randrange(0, 20)
        time.sleep(x / 10)
        print()
        print(' ' * 30 + '↑↑↑↑↑↑↑↑')
        self.loop_flg = False


def main():
    roulette1 = Roulette()
    roulette1.create_list()
    roulette1.append_tenhou()

    # シャッフル
    roulette1.shuffling_list()
    # print(roulette1.roulette_list)

    listener = keyboard.Listener(on_press=roulette1.press)
    listener.start()

    roulette1.run_roulette()


if __name__ == '__main__':
    main()