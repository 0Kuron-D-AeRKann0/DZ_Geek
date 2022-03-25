

print('Задание 1')

user_numbers = {
             'zero': 'ноль',
             'one': 'один',
             'two': 'два',
             'three': 'три',
             'four': 'четире',
             'five': 'пять',
             'six': 'шесть',
             'seven': 'семь',
             'eight': 'восемь',
             'nine': 'девять',}


def num_translate(num_word):
    return user_numbers.get(num_word)

print(num_translate('one'))

print('Задание 2')

def num_translate_adv(num_word):
    key = user_numbers.get(num_word.lower())

    if key:
        return key.capitalize() if num_word[0].isupper() else key

print(num_translate_adv('one'))
print(num_translate_adv('One'))

print('Задание 3')

def thesaurus(*args):
    out_dict = {}

    for name in args:

        if out_dict.get(name[0]):
            out_dict[name[0]].append(name)
        else:
            out_dict[name[0]] = [name]

    return out_dict

print(thesaurus('Ильяс'))

print('Задание 4')

def thesaurus_adv(*args):

    out_dict = {}

    for elem in args:
        name, second_name = elem.split()
        if not out_dict.get(second_name[0]):
            out_dict[second_name[0]] = { name[0] : [elem] }
        elif not out_dict[second_name[0]].get(name[0]):
            (out_dict[second_name[0]])[name[0]] = [elem]
        else:
            (out_dict[second_name[0]])[name[0]].append(elem)

    return out_dict

print(thesaurus_adv('Абдусаламов    Ильяс'))

print('Задание 5')

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def gen(from_, used_, unique):
    while True:
        n_nouns = choice(from_)

        if not (unique and n_nouns in used_):
            used_.append(n_nouns)
            break

    return (n_nouns, used_)

def get_jokes(count, unique=False):
    used = []
    answer = []

    if unique and count < len([*nouns, *adverbs, *adjectives]):
        return []
    for _ in range(count):
        nons, used_ = gen(nouns, used, unique)
        used.append(used_)

        adv, used_ = gen(adverbs, used, unique)
        used.append(used_)

        adj, used_ = gen(adjectives, used, unique)
        used.append(used_)

        answer.append(f"{nons} {adv} {adj}")

    return answer

print(get_jokes(5))