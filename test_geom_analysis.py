"""
Test for geom_analysis.py
"""

import geom_analysis as ga
import pytest


def test_calc_distance():
    coord1=[0,0,2]
    coord2=[0,0,0]
    observed = ga.calc_distance(coord1,coord2)

    assert observed == 2

def test_bond_check_false():
    bond_len = 1.2
    min = 0
    max = 1.0
    observed = ga.bond_check(bond_len,min,max)

    assert observed == False

def test_bond_check_true():
    bond_len = 1.2
    observed = ga.bond_check(bond_len)

    assert observed == True

def test_bond_check_error():
    bond_length='a'

    with pytest.raises(TypeError):
            observed=ga.bond_check(bond_length)
