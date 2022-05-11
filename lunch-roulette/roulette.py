import csv
import time
import random
from pynput import keyboard


class Roulette:

    def __init__(self):
        self.input_list = []
        self.roulette_list = []
        self.loop_flg = True
        self.app1 = None

    def create_list(self):
        """
        リスト作成
        """
        csv_path = './restaurant.csv'
        with open(csv_path, encoding='utf-8') as f:
            reader = csv.reader(f)

            for row in reader:
                self.input_list.append(str(row[0]))
                if int(row[1]) > 1:
                    for i in range(int(row[1]) - 1):
                        self.input_list.append(str(row[0]))

    def append_gakusyoku(self):
        """
        学食大量追加
        """
        for row in range(int(len(self.input_list) / 3 * 7)):
            self.input_list.append('学食')

    def append_tenhou(self):
        """
        学食，テンホウ大量追加
        :return:
        """
        for row in range(int(len(self.input_list) / 3 * 7 / 2)):
            self.input_list.append('学食')
            self.input_list.append('テンホウ')

    def shuffling_list(self):
        """
        リストをシャッフル
        :return:
        """
        self.roulette_list = self.input_list.copy()
        random.shuffle(self.roulette_list)

    def run_roulette(self):
        """
        ルーレットスタート
        :return:
        """
        roulette_length = len(self.roulette_list)

        print('-' * 40)
        print('|')



        i = 0
        while 1:
            if not self.loop_flg:
                break

            first_num = i % roulette_length
            second_num = (i + 1) % roulette_length
            third_num = (i + 2) % roulette_length
            fourth_num = (i + 3) % roulette_length
            fifth_num = (i + 4) % roulette_length

            show_list = [self.roulette_list[first_num],
                         self.roulette_list[second_num],
                         self.roulette_list[third_num],
                         self.roulette_list[fourth_num],
                         self.roulette_list[fifth_num]]

            space1 = '|' + ' ' * 9
            space2 = '|   ' + '⇨ ⇨' + '   '

            if i >= 1:
                print('\033[5A', end='')

            print('-' + ' ' * 40 + '\n', end='')
            print('-' + ' ' * 40 + '\n', end='')
            print('-' + ' ' * 40 + '\n', end='')
            print('-' + ' ' * 40 + '\n', end='')
            print('-' + ' ' * 40 + '\n', end='')
            print('\033[5A', end='')

            print(space1 + show_list[0] + '\n'
                  + space1 + show_list[1] + '\n'
                  + space2 + show_list[2] + '   ⇦ ⇦' + '\n'
                  + space1 + show_list[3] + '\n'
                  + space1 + show_list[4] + '\n', end='')

            time.sleep(0.1)
            i += 1


    def press(self, key):
        x = random.randrange(10, 15)
        time.sleep(x / 10)
        self.loop_flg = False


def main():
    roulette1 = Roulette()
    roulette1.create_list()

    # 曜日で判定 まとめて追加
    roulette1.append_tenhou()

    # シャッフル
    roulette1.shuffling_list()


    # リスナーオン
    listener = keyboard.Listener(on_press=roulette1.press)
    listener.start()

    # ルーレットスタート
    roulette1.run_roulette()

    print('|')
    print('-' * 40)


if __name__ == '__main__':
    main()
