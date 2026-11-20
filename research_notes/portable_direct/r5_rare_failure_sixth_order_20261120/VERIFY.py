#!/usr/bin/env python3
"""Exact certificate for R5 N^90: finite moments and predecessor B91 checks.
Usage: python VERIFY.py [--frozen /path/to/EXACT_R5_ALL_101_BUDGETS.json]
No stochastic or floating-point numerical evidence.
"""
import argparse
import hashlib
import json
from math import comb, factorial
from fractions import Fraction as F
A = tuple(range(214, 219))
B = tuple(range(219, 315))
D = tuple(range(222, 315))
J = 219*220*221
FROZEN_SHA256 = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"

def local_moments(prices, m, order):
    state = [[0]*(order+1) for _ in range(m)]
    state[0][0] = 1
    for p in prices:
        nxt = [[0]*(order+1) for _ in range(m)]
        for t in range(m):
            for n in range(m-t):
                w = p*n
                for r in range(order+1):
                    nxt[t+n][r] += sum(comb(r,j)*state[t][j]*w**(r-j) for j in range(r+1))
        state = nxt
    return [sum(state[t][r] for t in range(m)) for r in range(order+1)]

def overlap_grouped(m):
    K = Z = Y = 0
    for a in range(m):
        for b in range(m):
            for c in range(m):
                for d in range(m):
                    r = (a+b+c<m)+(a+c+d<m)+(b+c+d<m)
                    if r < 2:
                        continue
                    t = comb(c+2,2)*comb(d+2,2)
                    w = 214*a+215*b+217*c+220*d
                    K += (r-1)*t
                    Z += (r-1)*t*w
                    Y += (r-1)*(t*w*w+t*F(c*(c+3)+d*(d+3),6))
    assert F(Y).denominator == 1
    return K, Z, int(Y)

def overlap_bruteforce(m):
    K = Z = Y = 0
    def visit(ns):
        nonlocal K,Z,Y
        if len(ns)==8:
            a,b,c,d,e,f,g,h=ns
            r=(a+b+c+d+e<m)+(a+c+d+e+f+g+h<m)+(b+c+d+e+f+g+h<m)
            if r>=2:
                w=sum((214+i)*x for i,x in enumerate(ns))
                K+=r-1
                Z+=(r-1)*w
                Y+=(r-1)*w*w
            return
        for x in range(m):
            visit(ns+[x])
    visit([])
    return K,Z,Y

def laplace(prices, order=5):
    s=sum(prices);q=sum(k*k for k in prices);v=sum(k**4 for k in prices)
    coeff=[
        F(1),
        F(s,2),
        F(s*s,8)-F(q,24),
        F(s*s*s-s*q,48),
        F(s**4,384)-F(s*s*q,192)+F(q*q,1152)+F(v,2880),
        F(s**5,3840)-F(s**3*q,1152)+F(s*q*q,2304)+F(s*v,5760)
    ]
    return coeff[:order+1]

def calculate(m):
    M=local_moments(A,m,5)
    H1=local_moments((214,216,217,218,219,220,221),m,3)
    H2=local_moments((215,216,217,218,219,220,221),m,3)
    K,Z,Y=overlap_grouped(m)
    aB=laplace(B);aD=laplace(D,2)
    def b5(t):
        return sum(F((-1)**r*M[r],factorial(r))*aB[t-r] for r in range(t+1))
    def b7(t):
        h=t-2
        return J*sum(F(1,e)*sum(F((-1)**r*H[r],factorial(r))*laplace(D+(e,),h)[h-r] for r in range(h+1)) for e,H in ((215,H1),(214,H2)))
    def b8(t):
        h=t-3
        moments=(K,Z,Y)
        return -J*sum(F((-1)**r*moments[r],factorial(r))*aD[h-r] for r in range(h+1))
    def frac(x):
        return {"numerator":str(x.numerator),"denominator":str(x.denominator)}
    return {"m":m,"K":K,"Z":Z,"Y":str(Y),
            "B92":frac(b5(3)+b7(3)+b8(3)),
            "B91":frac(b5(4)+b7(4)+b8(4)),
            "B90":frac(b5(5)+b7(5)+b8(5))}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--frozen",help="path to original frozen input bytes; verifies unchanged SHA-256")
    args=parser.parse_args()
    sha_status="not supplied (derived witness sets kept from pinned predecessor)"
    if args.frozen:
        digest=hashlib.sha256(open(args.frozen,"rb").read()).hexdigest()
        assert digest==FROZEN_SHA256, (digest,FROZEN_SHA256)
        sha_status="matched "+digest
    assert (len(A),len(B),len(D),sum(B),sum(k*k for k in B),sum(D),J)==(5,96,93,25584,6891856,24924,10647780)
    for m in (1,2,3):
        assert overlap_grouped(m)==overlap_bruteforce(m)
    values=[calculate(m) for m in (1,2,3,5,8,17)]
    expected={1:"910818345468291342997/828180",2:"574883425643096600713/92020",
              3:"1904222299429571880323/92020",8:"13540123056221986210899/23005",
              17:"805947608855350953261777/92020"}
    for row in values:
        if row["m"] in expected:
            assert F(int(row["B91"]["numerator"]),int(row["B91"]["denominator"]))==F(expected[row["m"]])
    print(json.dumps({"schema":"R5_N90_EXACT_MOMENTS_V1",
        "model":"frozen R5 scalar/nonadaptive/query multiset",
        "frozen_input_sha256":FROZEN_SHA256,
        "frozen_bytes_status":sha_status,
        "checks":{"grouped_vs_independent_bruteforce_m":[1,2,3],
                  "predecessor_B91_matched_m":[1,2,3,8,17],
                  "arithmetic":"integer and fractions only"},
        "values":values},indent=2))

if __name__=="__main__":
    main()
