#!/usr/bin/env python3
"""Self-contained exact certificate; Python standard library, no RH input.
Run normally (not python -O). Numerical candidate discovery is not trusted.
"""
from fractions import Fraction as F
from math import lcm, isqrt
import json

C10 = [90, 88, 17, 70, -42, 58, 5, 15, -13]
C60 = [947037, 939064, 93988, 825999, -671899, 743961, -2769, 34987, -585464, 641943, -99488, 602255, -492787, -545756, 56124, 483936, -76918, 529253, -13983, -530443, -380417, 500849, 41296, -32524, -378353, -4767, -77213, 379564, 385032, 287517, -63006, -305881, -273756, -296539, 122647, 350741, -356973, -321441, -49222, 296274, 409265, 214853, -56797, 13314, -387718, 231483, -58522, 21532, 86970, -221497, 7245, 335936, 51079, -265405, 48611, -257917, -276699, 228233, 135449]
C100 = [953242, 947220, 80975, 847190, -713773, 772198, 12049, 11446, -616736, 666048, -69749, 665911, -584332, -585285, 33272, 558778, -44127, 551085, -31634, -507511, -462135, 498985, 24268, 53, -483141, 30790, -57986, 442147, 416031, 501488, -77677, -519075, -277149, -433946, 104784, 473980, -360051, -498577, -72502, 367228, 381007, 406564, -56773, -37747, -237360, 355845, -102218, -41184, -91752, -229095, 43219, 306310, 43164, -268300, 40822, -226618, -289143, 184103, 26111, 251902, -413288, 49686, 75087, -299868, 419625, 165302, -79040, -227496, 383564, 165336, -186296, 229240, -337065, 67233, 35570, -243274, 390866, 214786, -20762, -43655, -238979, 295033, 80278, -286955, -269420, -152256, -4468, 199313, 144623, -207651, -136154, -272355, -285807, -222920, 172830, 272495, 108428, 93713, 332376]
V = [10617923707994172031523024625, 2899221059906375468780691555, -1479892602581880989762169645, -1079961614376633156375396783, -4650413705203479130957955547, 3435807875539571241921890535, -746473105267256846126946420, -633930763215506592131540270, -897745028243747770258900939, 1093274073715256187770513079, -1094901540431987050955618525, 892880375588103047200746305, -940476352647732579527804055, -182394006334897686850478505, 547670594943400967916619800, 469119197536272577388334015, -437988181988836984705953810, 437988181988836984705953810, -528661555211286511603604136, 394784929349060877828456, 220165038935096725897574715, 308101731346840724828200965, -301290686135155604027483665, 195839805303600787777145143, -629685671401904822990223, 11545653930405338756364455, -35779085358831054077860235, 130313997931382436394824525, -271507813131073298509931940, 271507813131073298509931940]

def r(n, m):
    return F(m % n, n)

def prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))

def norm_bounds(nums, D, M):
    ns = list(range(2, len(nums) + 2))
    P = lcm(*ns)
    Q = D * P
    slope = sum(a * (P // n) for n, a in zip(ns, nums))
    increments = [-slope] * (M + 1)
    for n, a in zip(ns, nums):
        for m in range(n, M + 1, n):
            increments[m] += a * P
    S = 10**16
    E = Q
    K = 0
    for m in range(1, M + 1):
        E += increments[m]
        if m <= 200:
            assert E == Q - sum(a * (P // n) * (m % n) for n, a in zip(ns, nums))
        K += E * E * S // (Q * Q * m * (m + 1))
    pos = sum((F(a*(n-1), D*n) for n,a in zip(ns,nums) if a > 0), F(0))
    neg = sum((F(-a*(n-1), D*n) for n,a in zip(ns,nums) if a < 0), F(0))
    B = max(abs(1-pos), 1+neg)
    return F(K,S), F(K+M,S) + B*B/F(M+1)

def main():
    # All primes >30 are annihilated by the linear column m.
    assert len(V) == 30
    assert sum(m*v for m,v in enumerate(V,1)) == 0
    for p in range(2,31):
        if prime(p):
            assert sum(v*(m%p) for m,v in enumerate(V,1)) == 0
    lower = F(sum(V)**2, sum(m*(m+1)*v*v for m,v in enumerate(V,1)))
    assert lower == F(549980544461335314637000615,22936449866115041739513080208)
    assert lower > F(239,10000)
    v6 = [8,2,-3,-2,-5,5]
    assert sum(m*v for m,v in enumerate(v6,1)) == 0
    assert all(sum(v*r(p,m) for m,v in enumerate(v6,1)) == 0 for p in [2,3,5])
    assert F(sum(v6)**2,sum(m*(m+1)*v*v for m,v in enumerate(v6,1))) == F(5,428)
    a6 = [2,0,-1,0,-1,1]
    assert sum(a6) == 1 and sum(m*(m+1)*v*v for m,v in enumerate(a6,1)) == 92
    mu = [0]*121
    mu[1] = 1
    for d in range(1,121):
        for n in range(2*d,121,d):
            mu[n] -= mu[d]
    for n in range(2,121):
        for k in range(2,121):
            value = sum(mu[n//d]*(r(k,d)-r(k,d-1)) for d in range(1,n+1) if n%d == 0)
            assert value == (-1 if n == k else 0)
    for m in range(60):
        z = r(2,m)+2*r(3,m)
        assert r(6,m) == z - z.numerator//z.denominator
    assert r(6,1)-r(6,3)-r(6,4)+r(6,0) == -1
    assert 1%6 == 7%6 and r(5,1) != r(5,7)
    c = {2:F(1),3:F(1),5:F(1),6:F(-1),7:F(14,15)}
    assert all(sum(a*r(n,m) for n,a in c.items()) == 1 for m in range(1,7))
    output = {'prime_only_lower_squared':str(lower),'candidate_intervals':{}}
    for nums,D,M,barrier in [(C10,100,1000000,F(239,10000)),
                             (C60,1000000,1000000,F(5,428)),
                             (C100,1000000,2000000,F(1,92))]:
        lo,hi = norm_bounds(nums,D,M)
        assert hi < barrier
        output['candidate_intervals'][str(len(nums)+1)] = [str(lo),str(hi)]
    output['status'] = 'EXACT_CHECK_PASS'
    print(json.dumps(output,indent=2))

if __name__ == '__main__':
    main()
