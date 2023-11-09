'''
mod docstring
'''
import bloomdata.helper_functions as hf

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent']
nouns = ['food', 'house', 'tree', 'bicycle', 'phone']

list1 = [1, 2, 3]
list2 = [4, 5, 6]


def test_random_phrase():
    '''
    function docstring
    '''
    assert type(hf.random_phrase(adjectives, nouns)) == str
    assert type(hf.random_phrase(list1, list2)) == str
    assert hf.random_phrase(['Leeanna'], ['Pugh']) == 'Leeanna Pugh'
    assert hf.random_phrase([3], [4]) == '3 4'
