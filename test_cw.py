"""
Tests are a key part of software development. 

The tests provided below are not property-based tests, and their coverage is incomplete.
Thus, passing them does not mean that your code is fully correct.
This test file is a starting point for you to write your own tests.
Pay attention to edge cases (e.g. zero, empty list, empty string, etc).
Your mark will also depend on how you have coded your answers.

Any additional test code you produce will not be marked directly, but it may help give you credit for demonstrating understanding, so it should be included in your fork as part of this test_cw.py file or in a separate file.

To run these tests, type `pytest test_cw.py` within this directory.
"""

import importlib  
py_cw = importlib.import_module("py_cw")


## Q1

def test_q1a():
	s = py_cw.cadd((1, 0), (0, 1))
	p = py_cw.cmult((3, 2), (9, 6))
	assert s == (1, 1) and p == (15, 36)
	
def test_q1a_custom():
	s = py_cw.cadd((6, 9), (9, 6))
	p = py_cw.cmult((86, 7), (9, 32))
	assert s == (15, 15) and p == (550, 2815)
	
def test_q1b():
	assert py_cw.tocomplex(1, 2) == (1 + 2j) and py_cw.fromcomplex(1 + 1j) == (1, 1)
	
def test_q1b_custom():
	assert py_cw.tocomplex(32, 86) == (32 + 86j) and py_cw.fromcomplex(15 + 43j) == (15, 43)


## Q2

def test_q2a():
	assert py_cw.seqandi([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxori([True, False, True, False], [True, True, False, False]) == [False, True, True, False]
	
def test_q2a_custom():
	assert py_cw.seqandi([True, False, True, True], [True, True, False, True]) == [True, False, False, True] and py_cw.seqxori([False, True, False, True], [True, True, False, False]) == [True, False, False, True]

def test_q2b():
	assert py_cw.seqandr([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxorr([True, False, True, False], [True, True, False, False]) == [False, True, True, False]

def test_q2b_custom():
	assert py_cw.seqandr([True, False, True, True], [True, True, False, True]) == [True, False, False, True] and py_cw.seqxorr([False, True, False, True], [True, True, False, False]) == [True, False, False, True]

def test_q2c():
	assert py_cw.seqandlc([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxorlc([True, False, True, False], [True, True, False, False]) == [False, True, True, False]

def test_q2c_custom():
	assert py_cw.seqandlc([True, False, True, True], [True, True, False, True]) == [True, False, False, True] and py_cw.seqxorlc([False, True, False, True], [True, True, False, False]) == [True, False, False, True]

## Q3 

# Code segments are in the py_cw document.

## Q4 

def test_q4_supermap():
    assert py_cw.supermap(lambda a : 2*a, [5, [5]]) == [10, [10]]
    
def test_q4_supermap_custom():
    assert py_cw.supermap(lambda a : 3*a, [6, [6]]) == [18, [18]]

## Q5 

def test_q5_fenc():
	assert py_cw.fenc(4)=='[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]]'


def test_q5_fdec():
	assert py_cw.fdec([[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]])==4

## Q6 

def test_q6_love():
   x = py_cw.love()
   assert next(x) == "I love you"
   assert next(x) == "You love that I love you"
   assert next(x) == "I love that you love that I love you"

## Q7

def test_q7_removeall_oo():
    assert py_cw.removeall_oo(0, [0, 0, 1, 1, 0]) == [1, 1]
    
def test_q7_removeall_oo_custom():
    assert py_cw.removeall_oo(0, [0, 0, 1, 1, 0, 2]) == [1, 1, 2]  

def test_q7_removeall_ft():
    assert py_cw.removeall_ft(0, [0, 0, 1, 1, 0]) == [1, 1]
    
def test_q7_removeall_ft_custom():
    assert py_cw.removeall_ft(0, [0, 0, 1, 1, 0, 2]) == [1, 1, 2]

def test_q7_removeall_rd():
    assert py_cw.removeall_rd(0, [0, 0, 1, 1, 0]) == [1, 1]
    
def test_q7_removeall_rd_custom():
    assert py_cw.removeall_rd(0, [0, 0, 1, 1, 0, 2]) == [1, 1, 2]

## Q8

def test_q8_sudan():
    assert py_cw.sudan(0,0,0) == 0 and py_cw.sudan(2,2,1) == 27
    
def test_q8_sudan_custom():
    assert py_cw.sudan(1,2,0) == 2 and py_cw.sudan(2,3,1) == 74

## Q9

## Q10

## Q11

def test_q11_iint():
	assert py_cw.iint(21) == [1, 2] and py_cw.iint(0) == []

def test_q11_pint():
	assert py_cw.pint([1, 2]) == 21 and py_cw.pint([]) == 0

def test_q11_iadd():
	assert py_cw.iadd([1], [2]) == [3] and py_cw.iadd([8], [9]) == [7, 1]

def test_q11_imult():
	assert py_cw.imult([1], [2]) == [2] and py_cw.imult([8], [9]) == [2, 7]

def test_q11_ipow():
	assert py_cw.ipow([1], [2]) == [1] and py_cw.ipow([8], [9]) == [8, 2, 7, 7, 1, 2, 4, 3, 1]

## Q12

def test_q12_abstractsize():
	assert py_cw.abstractsize([[5], [], 4]) == 5 and py_cw.abstractsize([5, [], 4, 1]) == 5

def test_q12_compress():
	assert py_cw.compress([[5], [], 4]) == [5, 4] and py_cw.compress([5, [], 4, 1]) == [5, 4, 1]

## Q13

def test_q13_equals23():
    assert py_cw.equals23(23) == True

