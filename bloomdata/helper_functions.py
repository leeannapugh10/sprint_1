'''
Mod docstring
'''
import random

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent']
nouns = ['food', 'house', 'tree', 'bicycle', 'phone']


def random_phrase(list1, list2):
    '''
    function docstring
    '''
    item1 = random.choice(list1)
    item2 = random.choice(list2)

    return str(item1) + ' ' + str(item2)


if __name__ == '__main__':
    pass
    # print(random_phrase(adjectives, nouns))
