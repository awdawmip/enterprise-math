#!/usr/bin/env python3
"""Exact finite-tree observer-stratum checks; author evidence, not native X6 simulation."""
from fractions import Fraction as F
from itertools import product
from math import comb

LEAVES = ("ACl", "ACh", "AL", "BCl", "BCh", "BH")
P0 = tuple(map(F, ("1/24", "1/8", "1/12", "1/32", "7/32", "1/2")))
Q0 = tuple(map(F, ("1/12", "1/12", "1/3", "1/8", "1/8", "1/4")))
LEVELS = (("A", "B"), ("AC", "AL", "BC", "BH"), ("ACl", "ACh", "BCl", "BCh"))
LAMBDA = (F(912), F(456), F(128), F(-194))


def mass(weights, prefix):
    return sum((w for s, w in zip(LEAVES, weights) if s.startswith(prefix)), F(0))


def stratum(p, q):
    assert all(x > 0 for x in p + q)
    assert sum(p) == sum(q) == 1
    delta = F(1)
    equal = []
    smallest = None
    count = 0
    for level in LEVELS:
        for i, h in enumerate(level):
            for g in level[i+1:]:
                ph, qh, pg, qg = mass(p,h), mass(q,h), mass(p,g), mass(q,g)
                det = ph*qg-pg*qh
                delta *= det*det
                count += 1
                if det == 0:
                    equal.append((h,g))
                else:
                    gap = abs(ph/qh-pg/qg)
                    smallest = gap if smallest is None else min(smallest, gap)
    assert count == sum(comb(len(level),2) for level in LEVELS) == 13
    return delta, equal, smallest


def observer(p, q, policy):
    # order: root A, root B; collision actions AC, BC; side AL, BH; four final leaves
    out = [F(0) for _ in range(4)]
    for i, label in enumerate(LEAVES):
        group = 0 if label[0] == 'A' else 1
        root = policy[group]
        if root != 2:
            action, tau = root, 1
        elif label in ('AL','BH'):
            action, tau = policy[4 if group == 0 else 5], 2
        else:
            collision = policy[2 if group == 0 else 3]
            if collision != 2:
                action, tau = collision, 2
            else:
                action, tau = policy[6 + ('ACl','ACh','BCl','BCh').index(label)], 3
        # action 0=declare P, 1=declare Q, 2=continue
        assert action in (0, 1)
        if action == 1:
            out[0] += p[i]
        else:
            out[1] += q[i]
        out[2] += p[i]*tau
        out[3] += q[i]*tau
    return tuple(out)


def policies(collision_merged):
    for a, b in product(range(3),repeat=2):
        for ac, bc in product(range(3), repeat=2):
            if collision_merged and ac != bc:
                continue
            for rest in product(range(2),repeat=6):
                yield (a,b,ac,bc,*rest)


def optimum(p,q,merged):
    best = None
    unique = set()
    count = 0
    for policy in policies(merged):
        outcome = observer(p,q,policy)
        unique.add(outcome)
        val = sum((a*b for a,b in zip(LAMBDA,outcome)),F(0))
        best = val if best is None or val > best else best
        count += 1
    return count, len(unique), best


def main():
    epsilon = F(1, 10000)
    p1 = list(P0)
    p1[0] += epsilon
    p1[2] -= epsilon
    p1 = tuple(p1)
    d0, eq0, gap0 = stratum(P0,Q0)
    d1, eq1, gap1 = stratum(p1,Q0)
    assert eq0 == [('AC', 'BC')] and d0 == 0
    assert eq1 == [] and d1 > 0
    assert gap1 == F(3,5000)
    assert gap0 > 0
    nf, uf, vf = optimum(P0,Q0,False)
    nr, ur, vr = optimum(P0,Q0,True)
    nf1, uf1, vf1 = optimum(p1,Q0,False)
    nr1, ur1, vr1 = optimum(p1,Q0,True)
    assert (nf,nr,nf1,nr1) == (5184,1728,5184,1728)
    assert (vf,vr) == (F(868),F(857))
    assert vf1 == F(868)+F(912)*epsilon
    # Because there is no equality among signatures, the seedless LR policy set
    # has exactly the complete-history 5184 deterministic profiles.
    assert nr1 < nf1 and eq1 == []
    print('levels', [len(x) for x in LEVELS], 'same-level pairs', 13)
    print('original exact collision pairs', eq0, 'D0', d0)
    print('transverse P-only epsilon',epsilon)
    print('perturbed exact collision pairs', eq1)
    print('perturbed minimum signature gap',gap1)
    print('perturbed squared discriminant numerator/denominator bits',d1.numerator.bit_length(),d1.denominator.bit_length())
    print('original enumeration full',nf,'unique',uf,'support',vf)
    print('original enumeration LR',nr,'unique',ur,'support',vr,'gap',vf-vr)
    print('perturbed enumeration full',nf1,'unique',uf1,'support',vf1)
    print('perturbed equal-C restricted subset',nr1,'unique',ur1,'support',vr1, '(not the true perturbed LR class)')
    print('perturbed actual LR descriptors',nf1,'support',vf1,'by injective signature relabeling')
    print('original gap',vf-vr,'perturbed gap',F(0))
    print('ALL EXACT DISCRIMINANT AND SUPPORT CHECKS PASSED')

if __name__ == '__main__':
    main()
