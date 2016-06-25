# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from array import array
from enum import Enum
from random import seed, sample

seed()

class InputKind(Enum):
    BEST, AVERAGE, WORST = 'best', 'average', 'worst'

    def __str__(self):
        return self.value

def _gen_input_from(xs):
    return array('l', xs)

def gen_input_for_sorting(n, case=InputKind.AVERAGE):
    if n < 0:
        raise ValueError('input length must not be a negative number')
    if case is InputKind.BEST:
        return _gen_input_from(range(n))
    elif case is InputKind.AVERAGE:
        return _gen_input_from(sample(range(n), n))
    elif case is InputKind.WORST:
        return _gen_input_from(range(n - 1, -1, -1))
    else:
        raise NotImplementedError('invalid input kind: ' + str(case))