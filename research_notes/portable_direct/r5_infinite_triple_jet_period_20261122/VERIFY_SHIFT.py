"""Check arithmetic behind the R5 infinite triple-contraction progression theorem.
Exact modular nonzero witnesses originate in pinned VERIFY_EXTENDED.cpp / EXTENDED_OUTPUT.csv.
This checker validates their parameter ring assumptions and congruence/LCM arithmetic.
"""
import math

WITNESSES = {
    7:(10039,5580), 9:(10009,5783), 11:(10099,792),
    13:(10037,5992), 16:(10177,1750), 17:(10099,4343),
    19:(10223,2301), 23:(10259,4778), 25:(10151,7216),
    27:(10099,2017), 31:(10169,1836), 37:(10139,1802),
}
INITIAL = (2492,2493,2494,4988,6144,8638,8639,8640,
           11132,11133,11134,11135,11136,13628,13629,
           13630,16124,17280,19774,19775,19776)
Z29={0,54,55,56,57}
Z32={0,60,61,62,63}
Z43={0,37,38,39,40,41,42}
EXPECTED_T=59480643762644357887172046372434619641494875163251806048583266045383868826530935839210034044868800
def isprime(n):
    return n>=2 and all(n%k for k in range(2,math.isqrt(n)+1))
for d,(p,w) in WITNESSES.items():
    assert p>69 and isprime(p) and (p-1)%d==0
    assert pow(w,d,p)==1
    assert all(pow(w,k,p)!=1 for k in range(1,d) if d%k==0)
assert tuple(m for m in range(1,20000) if
    m%58 in Z29 and m%64 in Z32 and m%43 in Z43)==INITIAL
assert sum(r%58 in Z29 and r%64 in Z32 and r%43 in Z43
           for r in range(79808))==91
T=math.lcm(79808,*(2*d*p*p for d,(p,_) in WITNESSES.items()))
assert T==EXPECTED_T and len(str(T))==98
assert 229746052653717600//(29*2*43)==92119507880400
assert math.lcm(*WITNESSES.keys())==92119507880400
print("ALL CHECKS PASS")
print("T=",T)
