#!/usr/bin/env python3
"""Stage315-B: exact positive rational source/observer finite tests.

This is a REPRODUCTION CHECK, not a proof by finite sampling. Universal
8-to-4 reduction and moment obstruction are established in PROOF_STAGE315B.md.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product

SOURCE_MASSES = ((63, 1), (21, 3), (21, 3), (7, 9),
                 (9, 7), (3, 21), (3, 21), (1, 63))
P = (Q(1, 4), Q(3, 4))
MAP = tuple(P[0] if a > b else P[1] for a, b in SOURCE_MASSES)
CENTRAL = (1, 2, 5, 6)  # G=(W,Y)=(0,1) or (1,0)


def tv_errors(rates, n):
    """Source-tagged and public total variations for n ordered F bits."""
    public = defaultdict(Q)
    tagged_l1 = Q(0)
    positive_atoms = 0
    for h, (a, b) in enumerate(SOURCE_MASSES):
        for s, mass in enumerate((a, b)):
            for word in product((0, 1), repeat=n):
                k = sum(word)
                true = Q(mass, 256) * P[s]**k * (1-P[s])**(n-k)
                represented = Q(mass, 256)*rates[h]**k*(1-rates[h])**(n-k)
                assert true > 0
                positive_atoms += 1
                residual = represented - true
                public[(h % 4, word)] += residual
                tagged_l1 += abs(residual)
    return sum(map(abs, public.values()))/2, tagged_l1/2, positive_atoms


def raw_moments_of_rate(weighted_rates):
    assert sum(w for w, _ in weighted_rates) == 1
    return tuple(sum(w * t**j for w, t in weighted_rates) for j in (1, 2, 3))


def invariant(m):
    m1, m2, m3 = m
    var = m2 - m1*m1
    centered_3 = m3 - 3*m1*m2 + 2*m1**3
    return centered_3**2 - Q(9,4)*var**3, var, centered_3


def reset_central(rates):
    tmp = list(rates)
    for h in CENTRAL:
        tmp[h] = MAP[h]
    return tuple(tmp)


def main():
    assert sum(sum(ab) for ab in SOURCE_MASSES) == 256
    assert MAP == (Q(1,4),Q(1,4),Q(1,4),Q(3,4),
                   Q(1,4),Q(3,4),Q(3,4),Q(3,4))
    assert tv_errors(MAP,3) == (Q(11,256),Q(77,1024),128)
    # The model is exact for the two central public groups, for any horizon.
    for n in (1,2,3,4):
        base_pub,base_tag,atom_count = tv_errors(MAP,n)
        assert atom_count == 16*2**n
        # Outer rates are unchanged while central rates are moved off MAP.
        for v in (Q(0), Q(1,8), Q(1,3), Q(1,2), Q(2,3), Q(7,8), Q(1)):
            z=list(MAP)
            z[1]=v;z[2]=1-v;z[5]=v;z[6]=1-v
            public,tagged,_=tv_errors(tuple(z),n)
            restored=reset_central(z)
            rp,rt,_=tv_errors(restored,n)
            assert public >= rp and tagged > rt
            assert rp == base_pub and rt == base_tag
    # Exact target-vs-model 2-point mixing invariant for each outer G group.
    target_00 = ((Q(9,10),Q(1,4)),(Q(1,10),Q(3,4)))
    target_11 = ((Q(1,10),Q(1,4)),(Q(9,10),Q(3,4)))
    ht,v,c=invariant(raw_moments_of_rate(target_00))
    assert v == Q(9,400) and c == Q(9,1000)
    assert ht == Q(567,10240000)
    assert invariant(raw_moments_of_rate(target_11))[0] == ht
    for x in (Q(0),Q(1,5),Q(9,40),Q(1,2),Q(3,4),Q(1)):
        for y in (Q(0),Q(1,4),Q(3,5),Q(1)):
            model=((Q(4,5),x),(Q(1,5),y))
            assert invariant(raw_moments_of_rate(model))[0] == 0
    conditional_floor = ht / Q(1745,64)
    public_floor = Q(5,8)*conditional_floor
    assert conditional_floor == Q(567,279200000)
    assert public_floor == Q(567,446720000)
    # One explicit locked-port representation exactly reproduces every
    # 1- and 2-visit *public* trace but cannot reproduce all 3-bit traces.
    exact_two=list(MAP)
    exact_two[0],exact_two[4] = Q(9,40),Q(3,5)
    exact_two[3],exact_two[7] = Q(2,5),Q(31,40)
    assert raw_moments_of_rate(((Q(4,5),exact_two[0]),
                                (Q(1,5),exact_two[4])))[:2] == \
           raw_moments_of_rate(target_00)[:2]
    r1=tv_errors(exact_two,1)
    r2=tv_errors(exact_two,2)
    r3=tv_errors(exact_two,3)
    assert r1[0] == r2[0] == 0
    assert r3 == (Q(63,6400),Q(861051,8192000),128)
    assert r3[0] > public_floor
    print('SOURCE_ATOMS_N3=128; OUTER_GROUP_MASS=5/16; CENTRAL=(001,010,101,110)')
    print('MAP_N3_PUBLIC=11/256; MAP_N3_TAGGED=77/1024')
    print(f'MOMENT_INVARIANT_TRUE={ht}; CONDITIONAL_TV_FLOOR={conditional_floor}')
    print(f'ALL_EIGHT_RATE_PUBLIC_TV_FLOOR_N_GE_3={public_floor}')
    print(f'TWO_VISIT_EXACT_PUBLIC_N1={r1[0]}; N2={r2[0]}')
    print(f'TWO_VISIT_EXACT_PUBLIC_N3={r3[0]}; N3_TAGGED={r3[1]}')
    print('STAGE315B_UNIVERSAL_FOUR_FIBER_AND_MOMENT_OBSTRUCTION_EXACT_PASS')


if __name__ == '__main__':
    main()
