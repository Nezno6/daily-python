from tuples import get_hash_from_tuple

# The hash() function can produce different results
# in different Python implementations or even different runs of the same program.
# This is because the hash() function is implementation-specific.
# The hash() function is built into the Python interpreter, and its behavior is determined 
# by the Python implementation.
# This means that the hash() function in PyPy3 is part of the PyPy3 interpreter,
# and it can’t be imported into a different Python interpreter.

# The value for Python is -3550055125485641917 and for Pypy3 3713081631934410656
def test_tuples():
    assert hash(tuple([1,2])) == -3550055125485641917