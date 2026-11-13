#!/usr/bin/env python3
"""R129.4 exact gcd-period and interval endpoint checks."""
from fractions import Fraction as F
from math import gcd
from random import Random
from pathlib import Path
import json
from check_r129 import exact_signatures, rotated, totient

r=Random(129220261113)
passes=0;probes=0;long_matches=0
for z in range(160):
    A,d,E=[r.randint(-8,8) for i in range(3)]
    g=gcd(gcd(abs(A),abs(d)),abs(E))
    if g==0: continue
    m=r.randint(2,9)
    x=F(r.randint(-9,9),r.randint(1,7))
    P=F(1,g)
    canonical=exact_signatures(x,A,d,E,m,F(0),P)[0]
    U=set(canonical)|{rotated(x,A,d,E,m,F(0))}
    B=(abs(E)+sum(abs(A+i*d)+abs(A+i*d-E) for i in range(m)))//g
    assert len(U)<=max(1,2*B)
    for t in (F(0),F(1,17),F(-11,9),F(17,10),F(r.randint(-80,80),r.randint(1,51))):
        assert rotated(x,A,d,E,m,t)==rotated(x,A,d,E,m,t+P)
        probes+=1
    l=F(r.randint(-8,8),r.randint(1,8))
    delta=F(r.randint(1,5),r.randint(2,9))
    h=l+P+delta
    long=set(exact_signatures(x,A,d,E,m,l,h)[0])
    assert long==U
    long_matches+=1;passes+=1
sharp=[]
for m in range(2,33):
    open_one=set(exact_signatures(F(0),0,1,1,m,F(0),F(1))[0])
    open_more=set(exact_signatures(F(0),0,1,1,m,F(0),F(11,10))[0])
    H=1+sum(totient(q) for q in range(2,m))
    assert len(open_one)==H and len(open_more)==H+1
    assert (0,)*m not in open_one and (0,)*m in open_more
    sharp.append({"m":m,"open_exactly_one_period":H,"open_more_than_one_period":H+1})
output={"status":"R129_PERIOD_QUOTIENT_PASS","seed":129220261113,
        "valid_random_nonzero_gcd_instances":passes,"periodicity_exact_probes":probes,
        "long_interval_set_equal_full_period":long_matches,
        "sharp_family_period_endpoint_checks":len(sharp),
        "sharp_family_final":sharp[-1],
        "coverage":"finite Fraction checks; periodicity and quotient bound proved separately"}
Path(__file__).with_name("verification_r129_period.json").write_text(json.dumps(output,indent=2,ensure_ascii=False,sort_keys=True)+"\n")
print(output)
