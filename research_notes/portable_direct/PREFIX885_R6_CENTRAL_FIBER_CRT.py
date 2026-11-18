"""PREFIX-885: exact odd-modulus central fiber count for named XOR trajectories.
Finite auxiliary observer only. No physical time evolution is inferred.
"""
from math import gcd
from collections import Counter
import json
import random


def floor_sum(n, m, a, b):
    """Exact sum of floor((a*j+b)/m), j=0..n-1, for n>=0,m>=1,a,b>=0."""
    ans = 0
    while True:
        if a >= m:
            ans += (n-1)*n*(a//m)//2
            a %= m
        if b >= m:
            ans += n*(b//m)
            b %= m
        y = a*n+b
        if y < m:
            return ans
        n = y//m
        b = y % m
        m, a = a, m


def bit_ones_progression(first, step, count, i):
    """Number of entries with bit i=1 in first+j*step, 0<=j<count."""
    return (floor_sum(count, 1 << i, step, first)
            - 2*floor_sum(count, 1 << (i+1), step, first))


def centered_residue(N, q):
    return ((N-1)*pow(2,-1,q)) % q


def central_fiber_count(p, q1, q2, details=False):
    assert p >= 1 and q1 >= 1 and q2 >= 1 and q1%2 == q2%2 == 1
    N = 1 << p
    g = gcd(q1, q2)
    L = q1*(q2//g)
    h = (N-1)//L
    zero = 2*((h+1)//2)
    r1 = centered_residue(N, q1)
    r2 = centered_residue(N, q2)
    plus = minus = 0
    inv = pow(q1//g, -1, q2//g) if q2//g > 1 else None
    for i in range(p):
        for sigma in (1,-1):
            target = (r2-sigma*(1<<i)) % q2
            if (target-r1) % g:
                continue
            t = 0 if q2//g == 1 else (((target-r1)//g)*inv) % (q2//g)
            first = (r1+q1*t) % L
            if first >= N:
                continue
            count = 1+(N-1-first)//L
            ones = bit_ones_progression(first,L,count,i)
            contrib = (count-ones) if sigma==1 else ones
            if sigma == 1:
                plus += contrib
            else:
                minus += contrib
    c = zero+plus+minus
    assert c%2 == 0
    result = {'p':p,'q1':q1,'q2':q2,'gcd':g,'lcm':L,
              'zero_center':zero,'plus_center':plus,'minus_center':minus,
              'c_star':c,'collision_parity':(c//2)%2}
    if g>1:
        assert plus == minus == 0
    return result if details else c


def brute_center(p,q1,q2):
    N=1<<p
    r=centered_residue(N,q1)
    s=centered_residue(N,q2)
    c=0
    for x in range(r,N,q1):
        if x % q2 == s:
            c+=1
        for i in range(p):
            if (x^(1<<i)) % q2 == s:
                c+=1
    return c


def direct_collisions_mod2(p,q1,q2):
    N=1<<p
    counts=Counter()
    for x in range(N):
        for y in [x]+[x^(1<<i) for i in range(p)]:
            counts[(x%q1,y%q2)]+=1
    return sum(v*(v-1)//2 for v in counts.values())%2


def test():
    rr=random.Random(885)
    for _ in range(2000):
        n=rr.randrange(0,201)
        m=rr.randrange(1,301)
        a=rr.randrange(0,501)
        b=rr.randrange(0,501)
        assert floor_sum(n,m,a,b)==sum((a*j+b)//m for j in range(n))
        i=rr.randrange(0,12)
        assert bit_ones_progression(b,a,n,i)==sum(((b+j*a)>>i)&1 for j in range(n))
    center_tests=0
    parity_tests=0
    for p in range(1,9):
        N=1<<p
        for q1 in range(1,min(N,18),2):
            for q2 in range(1,min(N,18),2):
                r=central_fiber_count(p,q1,q2,True)
                assert r['c_star']==brute_center(p,q1,q2),(p,q1,q2,r)
                center_tests+=1
                if p<=6:
                    assert r['collision_parity']==direct_collisions_mod2(p,q1,q2)
                    parity_tests+=1
    pairs=[(524287,524285),(500383,522777),(523001,523003),
           (262143,524287),(524287,524287),(262143,262143),
           (524287,3),(65535,32767),(524287,1)]
    large=[]
    for q1,q2 in pairs:
        r=central_fiber_count(32,q1,q2,True)
        assert r['c_star']==brute_center(32,q1,q2),(q1,q2,r)
        large.append(r)
    return {
        'schema':'PREFIX885_R6_RESULTS_V1',
        'model':'p named binary sources; zero or one XOR source toggle; ordered two-port odd-residue observer',
        'method':'generalized_CRT + exact Euclidean floor_sum bit count',
        'tests':{'floor_sum_bit_progression_random_checks':2000,
                 'small_exhaustive_center_pairs':center_tests,
                 'small_direct_collision_parity_pairs':parity_tests,
                 'large_direct_center_pairs':len(large)},
        'large_examples':large,
        'status':'ALL_EXACT_ASSERTIONS_PASSED',
        'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d'
    }


if __name__=='__main__':
    out=test()
    with open('PREFIX885_R6_CENTRAL_FIBER_RESULTS.json','w',encoding='utf-8') as f:
        json.dump(out,f,ensure_ascii=False,indent=2)
    print(json.dumps(out,indent=2))
