'''
mod docstring
'''


import pytest
import bloomdata.bloomdata2 as bd


def test_increment_int():
    '''
    function docstring
    '''
    assert bd.increment(3) == 4
    assert bd.increment(-2) == -1


def test_increment_float():
    '''
    function docstring
    '''
    assert bd.increment(1.5) == 2.5
    assert bd.increment(-2.5) == -1.5


def test_increment_int_return_type():
    '''
    function docstring
    '''
    assert isinstance(bd.increment(3), int)
