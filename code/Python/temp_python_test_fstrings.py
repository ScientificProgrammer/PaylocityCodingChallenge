"""
    Just testing Python.

    See https://stackoverflow.com/questions/54823506/\
    mixing-normal-string-with-f-string-in-line-continuation
    for more details.
"""

import timeit

my_format = (
    """
def my_format(name, age):
    return (
        f'He said his name is '
        f'{name} and he is '
        f'{age} years old.'
    )
""",
    """
def my_format(name, age):
    return (
        'He said his name is '
        f'{name} and he is '
        f'{age} years old.'
    )
""",
)

test = """
def test():
    for name in ('Fred', 'Barney', 'Gary', 'Rock', 'Perry', 'Jackie'):
        for age in range (20, 200):
            my_format(name, age)
"""

for fmt in my_format:
    print(timeit.timeit("test()", fmt + test, number=10000))

MY_STRING = """
[out]:
  3.4188902939995387
  3.3931472289996236\n
"""

print(MY_STRING)
