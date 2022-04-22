import random


class Card:
    def __init__(self, title=", rows_amount=3, cols_amount=9, nums_per_row=5, max_num=90):
        self._rows_amount = rows_amount

    self._cols_amount = cols_amount
    self._nums_per_row = nums_per_row
    self._max_num = max_num
    self._title = title
    self._card = [[" for _ in range(self._cols_amount)] for _ in range(self._rows_amount)]
                   self._nums = random.sample(range(1, self._max_num + 1), self._nums_per_row * self._rows_amount)
    self._pixels = self._cols_amount * 3 - 1
    self._nums_for_game = self._nums[:] \
 \
                          @ property

    def nums(self):
        return len(self._nums_for_game)

    def _mapping_card(self):
        for row in self._card:
            while row.count('*') != self._nums_per_row:


row[random.randrange(self._cols_amount)] = '*'


def _filling_card_with_numbers(self):
    for i, row in enumerate(self._card):
        tmp = sorted(self._nums[i * self._nums_per_row:(i + 1) * self._nums_per_row], reverse=True)
        for j, item in enumerate(row):
            self._card[i][j] = tmp.pop() if item else ''


def __str__(self):
    res = ['{:-^{}}'.format(self._title, self._pixels), ]
    for row in self._card:
        res.append(' '.join(['{:<2}'.format(x) for x in row]))
    res.append('-' * self._pixels)
    return '\n'.join(res)


def modify_card(self, num):
    i = int(self._nums.index(num) / self._nums_per_row)
    self._card[i][self._card[i].index(num)] = '-'
    self._nums_for_game.remove(num)


def check_num(self, num):
    return num in self._nums


def create_card(self):
    self._mapping_card()
    self._filling_card_with_numbers()


class Game:
    def __init__(self, max_num=90):
        self._max_num = max_num
        self._unit1 = Card(' Ваша карточка ')
        self._unit2 = Card(' Карточка компьютера ')

    def _get_random_num(self):
        random_numbers = random.sample(range(1, self._max_num + 1), self._max_num)
        for i in random_numbers:
            yield i, self._max_num - random_numbers.index(i) - 1

    def _check_answer(self, unit, num, answer):
        if answer != 'y' and answer != 'n':
            self._check_answer(unit, num, input('Зачеркнуть цифру? (y/n)'))
        elif answer == 'y' and unit.check_num(num):
            unit.modify_card(num)
            return 0
        elif answer == 'n' and not unit.check_num(num):
            return 0
        elif answer == 'y' and not unit.check_num(num):
            print('{} нет на вашей карточке.'.format(num), end=' ')
            return 1
        elif answer == 'n' and unit.check_num(num):
            print('{} на вашей карточке.'.format(num), end=' ')
            return 1

    def lets_play(self):
        self._unit1.create_card()
        self._unit2.create_card()

        num_generator = self._get_random_num()

        while self._unit1.nums and self._unit2.nums:
            num, left = next(num_generator)
            print(self._unit1)
            print(self._unit2)

            print('Новый бочонок: {} (осталось {})'.format(num, left))

            if self._check_answer(self._unit1, num, input('Зачеркнуть цифру? (y/n)')):
                return 'К сожалению, вы проиграли.'
            if self._unit2.check_num(num):
                self._unit2.modify_card(num)

        if not self._unit1.nums and not self._unit2.nums:
            return 'Ничья!'
        elif self._unit2.nums:
            return 'Поздравляем, вы победили!'
        else:
            return 'Компьютер успел первым. Попробуйте еще раз.'


if __name__ == '__main__':
    game = Game()
    print(game.lets_play())