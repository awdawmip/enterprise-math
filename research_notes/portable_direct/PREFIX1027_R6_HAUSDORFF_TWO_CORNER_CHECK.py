#!/usr/bin/env python3
"""PREFIX-1027: exact Stage46 signed-BRC/Laurent contrast finite Hausdorff witness triangle.
Uses the published PREFIX-1016 three-shift formula and PREFIX-1018 A6 recurrence.
All operations are exact integers/Fraction; no native-heartbeat or physical claim.
"""
from fractions import Fraction
from hashlib import sha256
from json import dump
from pathlib import Path
from sys import argv

def collision(n):
    a = [1, 6, 66]
    for r in range(2, n + 3):
        num = (2 * (2*r+1) * (14*r**4+28*r**3+28*r**2+14*r+3) * a[r]
               - 4*r**3 * (196*r**2+59) * a[r-1]
               + 1152*(2*r-1)*r*r*(r-1)**2 * a[r-2])
        den = (r+1)**5
        assert num % den == 0
        a.append(num // den)
    assert a[:8] == [1, 6, 66, 996, 18306, 384156, 8848236, 218040696]
    return a

def contrast(m, a):
    q = (Fraction(-72*(72*m*m+163*m+80), 5*(m+1)) * a[m+1]
         + Fraction(2*(144*m**3+1135*m*m+2367*m+1310), 5*(m+1)*(m+2)) * a[m+2]
         - Fraction(2*(m+8)*(2*m+5), 5*(m+2)) * a[m+3])
    assert q.denominator == 1
    return q.numerator

def audit(n):
    a = collision(n)
    row = [contrast(m,a) for m in range(1,n+1)]
    assert row[:9] == [25620,386028,7124592,149251656,3398043852,
                       81969197100,2063490736128,53703289713528,
                       1436011181064216]
    h = sha256()
    for k in range(n):
        for m,value in enumerate(row,1):
            assert value > 0, (m,k,value)
            h.update(f"{m},{k},{value}\n".encode("ascii"))
        row = [36*row[i]-row[i+1] for i in range(len(row)-1)]
    return n*(n+1)//2, h.hexdigest()

def main():
    n = int(argv[1]) if len(argv)>1 else 1200
    assert n >= 240
    cnt240,d240 = audit(240)
    assert cnt240 == 28920
    assert d240 == "ba12049d9510eabf3abef8326249de88d7edcfdf88f1d990d2539a51bae8afc8"
    cnt,d = audit(n)
    if n == 1200:
        assert (cnt,d) == (720600,"b626fc2e4e12db5ce219ab6f5e69f0c0344f38d6fe63d189a768a935d888439e")
    report = {"schema":"PREFIX1027_R6_EXACT_HAUSDORFF_TRIANGLE_V1",
              "scientific_pin":"enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
              "model":"Stage46 signed BRC W=J12-6I; X6 Link {0,e1}; k=1; joint coherent Cell-port masses",
              "arithmetic":"unbounded integers and Fraction; original exact A6 recurrence and contrast",
              "m_plus_k_max":n,"positive_witnesses":cnt,"all_strict_positive":True,
              "witness_stream":"ASCII m,k,E newline, ascending k then m",
              "witness_sha256":d,"prior_240_sha256":d240,
              "review":"NOT_REVIEWED"}
    if len(argv)>2:
        with open(argv[2],"w",encoding="utf-8") as f:
            dump(report,f,indent=2,ensure_ascii=False)
            f.write("\n")
    print("PASS:",cnt,"strictly positive integer Hausdorff witnesses")
    print("SHA-256:",d)
    print("PREFIX1026/240:",d240)

if __name__ == "__main__":
    main()
