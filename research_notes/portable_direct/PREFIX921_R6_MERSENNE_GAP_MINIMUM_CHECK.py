#!/usr/bin/env python3
"""PREFIX-921 exact Mersenne modular obstruction, standard library only."""
from math import gcd
import json

N=1<<32
B=(1<<19)-1
powers={pow(2,i,B) for i in range(32)}
single={s*x%B for x in powers for s in (-1,1)}
double={(s*x+t*y)%B for x in powers for y in powers for s in (-1,1) for t in (-1,1)}
S=single|double|{0}
assert len(powers)==19 and len(single)==38 and len(double)==647 and len(S)==647
assert {2*x%B for x in S}==S and gcd(94,B)==1
inv=pow(-94,-1,B)
first=min(r*inv%B for r in S if r)
assert first==8369
assert all((-94*k)%B not in S for k in range(1,8369))
family=[]
for t in range(12):
    a=B-94*(1<<t)
    assert 262145<=a<=524287 and a%2 and gcd(a,B)==1
    K=(N-1)//a
    family.append({"t":t,"a":a,"max_k":K,"modular_obstruction":K<first})
    assert (t<=6)==(K<first)
mins=sorted(z["a"] for z in family if z["modular_obstruction"])
assert mins==[518271,521279,522783,523535,523911,524099,524193]
mass=13*(N//2)
assert mass==27917287424
a7=B-94*(1<<7); y=8369*a7
assert a7==512255 and y<N and ((y>>15)&1)==0 and ((y^(1<<15))-64)%B==0
print(json.dumps({"schema":"PREFIX921_R6_MERSENNE_MINIMUM_CERT_V1","b":B,
"number_of_residues":len(S),"minimum_k":first,"family":family,
"seven_minimizers":mins,"minimum_total_collision_mass":mass,
"t7_witness":{"a":a7,"k":8369,"x":0,"y":y,"i":6,"j":15,
"first_end":64,"second_end":y^(1<<15)}},indent=2))
