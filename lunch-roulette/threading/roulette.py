import csv
import random


class Roulette:

    def __init__(self):
        self.input_list = None
        self.shuffled_list = []

    def set_list(self, input_list):
        self.input_list = input_list.copy()

    def normal_day(self):
        for row in range(int(len(self.input_list) / 3 * 7)):
            self.input_list.append('学食')

    def conf_day(self):
        for row in range(int(len(self.input_list) / 2 * 8)):
            self.input_list.append('学食')

    def tuesday(self):
        list_len = len(self.input_list)
        for row in range(int(list_len / 3 * 3)):
            self.input_list.append('学食')
        for row in range(int(list_len / 3 * 4)):
            self.input_list.append('テンホウ')

    def shuffling_list(self):
        self.shuffled_list = self.input_list.copy()
        random.shuffle(self.shuffled_list)
        random.shuffle(self.shuffled_list)

