#!/usr/bin/env python3
"""PREFIX-920: exact dyadic-residue hit criterion and exhaustive strict-19-bit row.

Pure Python 3, arbitrary-precision integers, no external dependencies.
Run: python3 PREFIX920_R6_BINARY_ORBIT_ROW_CHECK.py
"""
import hashlib
import json
from collections import defaultdict
from math import gcd, lcm

P = 32
N = 1 << P
FIRST = (1 << 18) + 1
LAST = (1 << 19) - 1
B_FIXED = 440665


def tau(A, h):
    r = A % (2 * h)
    return min(r, 2 * h - r)


def orbit_mass(p, a, b):
    """32-step doubling recurrence, counts all named zero-flip collisions."""
    n = 1 << p
    if gcd(a, b) != 1:
        return 0, 0, 0, 0, 0
    K = (n - 1) // a
    q = pow(a, -1, b)
    total = plus_count = minus_count = plus_mass = minus_mass = 0
    for i in range(p):
        h = 1 << i
        for minus_k in range(q, K+1, b):
            A = minus_k * a
            w = n - A + tau(A, h)
            assert w > 0 and w % 2 == 0
            total += w
            minus_mass += w
            minus_count += 1
        # Strict bound: at A+h=n or above the plus mass is zero.
        for plus_k in range(b-q, (n - 1 - h)//a+1, b):
            A = plus_k * a
            w = n - A - tau(A, h)
            assert w > 0 and w % 2 == 0
            total += w
            plus_mass += w
            plus_count += 1
        q = (2 * q) % b
    return total, plus_count, minus_count, plus_mass, minus_mass


def independent_residue_mass(p,a,b):
    """Independent i-indexed modular inverse with binary bit-population weights.

    Does not call the orbit recurrence or tau() helper.
    """
    n=1<<p
    if gcd(a,b)>1:
        return 0
    inv=pow(a,-1,b)
    cap=(n-1)//a
    total=0
    for i in range(p):
        H=1<<i
        residue=(pow(2,i,b)*inv)%b
        # b odd and gcd(a,b)=1 makes residue nonzero.
        assert 0<residue<b
        for k in range(residue,cap+1,b):
            A=k*a
            ones=(A//(2*H))*H+max(0,(A%(2*H))-H)
            total += n-2*ones
        for k in range(b-residue,(n-1-H)//a+1,b):
            A=k*a
            ones=(A//(2*H))*H+max(0,(A%(2*H))-H)
            total += n-2*(A-ones)
    return total


def direct_mass(p, a, b):
    """Independent direct ka congruence scan; designed for selective checks."""
    n = 1 << p
    total = 0
    for k in range(1, (n - 1)//a + 1):
        A=k*a
        for i in range(p):
            h=1<<i
            t=tau(A,h)
            if (A+h) % b == 0:
                total += n-A-t
            if (A-h) % b == 0:
                total += n-A+t
    return total


def brute(p,a,b):
    from collections import defaultdict
    n=1<<p
    bins=defaultdict(lambda:[0,0])
    for x in range(n):
        bins[(x%a,x%b)][0]+=1
        for i in range(p):
            bins[(x%a,(x^(1<<i))%b)][1]+=1
    return sum(z*f for z,f in bins.values())


def check_small():
    cases=0
    for p in range(2,9):
        for a in range(3,min(15,(1<<p)-1)+1,2):
            for b in range(3,min(15,(1<<p)-1)+1,2):
                m=orbit_mass(p,a,b)[0]
                assert m == brute(p,a,b), (p,a,b,'brute')
                assert m == direct_mass(p,a,b), (p,a,b,'direct')
                assert m == independent_residue_mass(p,a,b), (p,a,b,'independent residues')
                assert m == orbit_mass(p,b,a)[0], (p,a,b,'time reversal')
                cases+=1
    return cases


def main():
    cases=check_small()
    counts=defaultdict(int)
    sum_mass=sum_plus_mass=sum_minus_mass=0
    examples={}
    row_hash=hashlib.sha256()
    maximum=(-1,None)
    for a in range(FIRST,LAST+1,2):
        m,nplus,nminus,mp,mm = orbit_mass(P,a,B_FIXED)
        assert m==mp+mm
        # Independent swapped-port implementation for every row entry.
        swapped=orbit_mass(P,B_FIXED,a)[0]
        independent=independent_residue_mass(P,a,B_FIXED)
        assert m==swapped==independent,(a,B_FIXED,m,swapped,independent)
        assert m % 2 == 0
        if gcd(a,B_FIXED)>1:
            counts['noncoprime']+=1
            assert m==0
        else:
            counts['coprime']+=1
            if m==0:
                counts['coprime_zero']+=1
                examples.setdefault('coprime_zero',{'a':a,'b':B_FIXED})
            elif nplus and nminus:
                counts['coprime_both_signs']+=1
                examples.setdefault('both_signs',{'a':a,'b':B_FIXED,'mass':m,'plus_fibers':nplus,'minus_fibers':nminus})
            elif nplus:
                counts['coprime_plus_only']+=1
                examples.setdefault('plus_only',{'a':a,'b':B_FIXED,'mass':m,'plus_fibers':nplus})
            elif nminus:
                counts['coprime_minus_only']+=1
                examples.setdefault('minus_only',{'a':a,'b':B_FIXED,'mass':m,'minus_fibers':nminus})
            else:
                raise AssertionError('positive mass without fiber')
            if nplus: counts['coprime_plus_any']+=1
            if nminus: counts['coprime_minus_any']+=1
        sum_mass+=m
        sum_plus_mass+=mp
        sum_minus_mass+=mm
        if m>maximum[0]:maximum=(m,a)
        row_hash.update(f'{a},{B_FIXED},{m},{nplus},{nminus},{mp},{mm}\n'.encode('ascii'))
    assert sum(counts[k] for k in ('noncoprime','coprime')) == (LAST-FIRST)//2+1
    assert sum(counts[k] for k in ('coprime_zero','coprime_plus_only','coprime_minus_only','coprime_both_signs')) == counts['coprime']
    assert sum_mass == sum_plus_mass+sum_minus_mass
    anchor=orbit_mass(P,321651,B_FIXED)
    assert anchor[0]==59007025662 and anchor[1]+anchor[2]==17
    for label,x in examples.items():
        assert direct_mass(P,x['a'],x['b']) == orbit_mass(P,x['a'],x['b'])[0],label
    results = {
        'schema':'PREFIX920_BINARY_RESIDUE_ORBIT_ROW_V1',
        'scientific_input_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'model': {'p':P, 'N':N,'odd_a_inclusive':[FIRST,LAST],'b_fixed':B_FIXED,
                  'trajectory_labels':'Z_x, F_x^i retaining named source bit'},
        'small_full_bruteforce_cases':cases,
        'exact_row_entries':(LAST-FIRST)//2+1,
        'counts':dict(sorted(counts.items())),
        'sum_mixed_mass_all_row':sum_mass,
        'sum_plus_mass_all_row':sum_plus_mass,
        'sum_minus_mass_all_row':sum_minus_mass,
        'maximum_row_mass': {'a':maximum[1],'b':B_FIXED,'mass':maximum[0]},
        'examples':examples,
        'anchor_prefix919': {'a':321651,'b':B_FIXED,'total':anchor[0],
                             'plus_fibers':anchor[1],'minus_fibers':anchor[2]},
        'full_row_digest':{'format':'ASCII lines: a,b,mass,plus_fibers,minus_fibers,plus_mass,minus_mass\\n; a ascending','sha256':row_hash.hexdigest()},
        'independent_checks': ['swapped-port orbit for all row entries','independent i-indexed modular residue/bit-population recount for all row entries','direct ka scan for all first examples',
                               'complete trajectory fiber brute force p=2..8 for all odd moduli <=15',
                               'PREFIX919 frozen anchor regression']
    }
    print(json.dumps(results,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
