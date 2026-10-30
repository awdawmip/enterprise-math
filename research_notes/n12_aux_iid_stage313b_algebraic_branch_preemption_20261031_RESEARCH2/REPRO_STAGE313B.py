#!/usr/bin/env python3
"""Stage313-B: exact 128-atom TV counterexample and Q(sqrt(13)) certificate.
Self-contained standard-library arithmetic; every assertion is exact.
The proof of universal quantification is in PROOF_STAGE313B.md.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product


@dataclass(frozen=True)
class Q13:
    a: F = F(0)
    b: F = F(0)  # a + b sqrt(13)

    def __init__(self, a=0, b=0):
        object.__setattr__(self, 'a', F(a))
        object.__setattr__(self, 'b', F(b))

    @staticmethod
    def of(x):
        return x if isinstance(x, Q13) else Q13(x)

    def __add__(self, other):
        o = self.of(other)
        return Q13(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Q13(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.of(other))

    def __rsub__(self, other):
        return self.of(other) - self

    def __mul__(self, other):
        o = self.of(other)
        return Q13(self.a * o.a + 13 * self.b * o.b,
                   self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = self.of(other)
        norm = o.a * o.a - 13 * o.b * o.b
        assert norm != 0
        return self * Q13(o.a / norm, -o.b / norm)

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = Q13(1)
        for _ in range(n):
            result *= self
        return result

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if (a > 0) == (b > 0):
            return 1 if a > 0 else -1
        lhs, rhs = a * a, 13 * b * b
        assert lhs != rhs  # sqrt(13) irrational, except zero coefficients
        return ((a > 0) - (a < 0)) if lhs > rhs else ((b > 0) - (b < 0))

    def __abs__(self):
        return self if self.sign() >= 0 else -self

    def __lt__(self, other):
        return (self - self.of(other)).sign() < 0

    def __le__(self, other):
        return (self - self.of(other)).sign() <= 0

    def __eq__(self, other):
        o = self.of(other)
        return self.a == o.a and self.b == o.b

    def __str__(self):
        return str(self.a) if not self.b else f'({self.a})+({self.b})*sqrt(13)'


H = ('000', '001', '010', '011', '100', '101', '110', '111')
AB = ((63, 1), (21, 3), (21, 3), (7, 9),
      (9, 7), (3, 21), (3, 21), (1, 63))
P0_RATE, P1_RATE = Q13(F(1, 4)), Q13(F(3, 4))
MAP = tuple(P0_RATE if a > b else P1_RATE for a, b in AB)
WORDS = tuple(product((0, 1), repeat=3))


def prob_word(rate, word):
    k = sum(word)
    return rate**k * (Q13(1) - rate)**(3-k)


def tv(left, right):
    keys = set(left) | set(right)
    return sum((abs(left.get(k, Q13())-right.get(k, Q13()))
                for k in keys), Q13()) / 2


def risks(t):
    assert len(t) == 8
    tagged_target, tagged_comp = defaultdict(Q13), defaultdict(Q13)
    public_target, public_comp = defaultdict(Q13), defaultdict(Q13)
    for index, history in enumerate(H):
        j, w, y = map(int, history)
        a, b = AB[index]
        for source, mass in ((0, a), (1, b)):
            p = P0_RATE if source == 0 else P1_RATE
            for word in WORDS:
                target = Q13(mass)/256 * prob_word(p, word)
                comp = Q13(mass)/256 * prob_word(t[index], word)
                key_tag = (source, j, w, y, word)
                key_public = (w, y, word)
                tagged_target[key_tag] += target
                tagged_comp[key_tag] += comp
                public_target[key_public] += target
                public_comp[key_public] += comp
    assert sum(tagged_target.values(), Q13()) == Q13(1)
    assert sum(tagged_comp.values(), Q13()) == Q13(1)
    return tv(public_comp, public_target), tv(tagged_comp, tagged_target)


def one_light(u):
    t = list(MAP)
    t[4] = P0_RATE + Q13.of(u)
    return risks(t)


def q(u):
    return Q13(F(9,128))*u + Q13(F(3,32))*u**2 - u**3/8


def g(u):
    return Q13(F(117,4096))*u - Q13(F(123,1024))*u**2 + Q13(F(23,256))*u**3


p_base, t_base = risks(MAP)
assert p_base == Q13(F(11, 256)), p_base
assert t_base == Q13(F(77, 1024)), t_base

small = Q13(F(11,100))
large = Q13(F(87,500))
p_small, t_small = one_light(small)
p_large, t_large = one_light(large)
assert p_small == p_base - q(small)
assert t_small == t_base + g(small)
assert p_large < p_small and t_large < t_small

sqrt13 = Q13(0,1)
u_star = (Q13(5) - sqrt13)/8
t_star = P0_RATE + u_star
p_star, tagged_star = one_light(u_star)
assert p_star == Q13(F(-1,32), F(9,512))
assert tagged_star == Q13(F(319,4096), F(-1,4096))
assert t_star == Q13(F(7,8), F(-1,8))
assert p_star < p_base - q(Q13(F(3,25)))
assert tagged_star < t_small

# The old branch intersects the new algebraic witness between 109/1000 and 11/100.
excess_star = tagged_star - t_base
assert g(Q13(F(109,1000))) < excess_star < g(small)
assert q(Q13(F(109,1000))) < q(small) < q(Q13(F(3,25)))

# Mechanism: B_1(t_star)=B_1(1/4), the exact signed-path kink.
assert prob_word(t_star, (1,0,0)) == prob_word(P0_RATE, (1,0,0))

print('MODEL_MASS:', sum(a+b for a,b in AB), '/256; ATOMS:', len(H)*2*len(WORDS))
print('MAP_PUBLIC:', p_base, 'MAP_TAGGED:', t_base)
print('RATIONAL_SMALL_U:', small, 'PUBLIC:', p_small, 'TAGGED:', t_small)
print('RATIONAL_LARGE_U:', large, 'PUBLIC:', p_large, 'TAGGED:', t_large)
print('STRICT_PUBLIC_ADVANTAGE:', p_small-p_large)
print('STRICT_TAGGED_ADVANTAGE:', t_small-t_large)
print('ALGEBRAIC_KINK_U:', u_star)
print('ALGEBRAIC_PUBLIC:', p_star, 'ALGEBRAIC_TAGGED:', tagged_star)
print('ALGEBRAIC_PUBLIC_GAIN:', p_base-p_star)
print('ALGEBRAIC_TAGGED_EXCESS:', excess_star)
print('ROOT_BRACKET_U:', F(109,1000), F(11,100))
print('ROOT_BRACKET_EPSILON:', q(Q13(F(109,1000))), q(small))
print('STAGE313B_ALGEBRAIC_BRANCH_PREEMPTION_EXACT_PASS')