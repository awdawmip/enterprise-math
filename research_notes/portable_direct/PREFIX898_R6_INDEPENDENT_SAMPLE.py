#!/usr/bin/env python3
"""Independent Python checks for PREFIX-898. Exact integers, stdlib only."""
import json, math
from pathlib import Path
N=1<<32; T=33*N; LO=262145; HI=524287
S={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285}
def in_U(q):
    return q in S or 400011<=q<=400521 or 480011<=q<=480521 or any((2**h-1)%q==0 or (2**h+1)%q==0 for h in range(1,32))
def old(q1,q2):
    if q1*q2<T or in_U(q1) or in_U(q2):return True
    if q1*q2//math.gcd(q1,q2)<N:return True
    return 33*((N+q1-1)//q1)>q2 or 33*((N+q2-1)//q2)>q1
def zf(q1,q2):
    if math.gcd(q1,q2)>1:return False
    inv=pow(q1,-1,q2)
    for i in range(32):
        r=(pow(2,i,q2)*inv)%q2
        if r*q1<N or (q2-r)*q1+(1<<i)<N:return True
    return False
report=json.loads(Path('PREFIX898_R6_EXACT_ZF_OVERLAP_PANEL_RESULTS.json').read_text())
checks=[]
for a,uncovered,positive in report['rows'][::8]:
    n=c=0
    for b in range(LO,HI+1,2):
        if not old(a,b):
            n+=1
            if zf(a,b):c+=1
    checks.append([a,n,c])
    assert [a,n,c] in report['rows'], (a,n,c)
w=report['first_witness'];a=w['q1'];b=w['q2'];x=w['zero_x'];u=w['flip_start'];i=w['flip_source_bit']
assert x%a==u%a and x%b==(u^(1<<i))%b and 0<=x,u<N
print(json.dumps({'independent_python_full_row_crosschecks':checks,'checked_rows':len(checks),'mismatch':0,'first_witness_directly_verified':True},ensure_ascii=False,indent=2))
