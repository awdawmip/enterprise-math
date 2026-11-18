#!/usr/bin/env python3
"""Exact parameter-pair union of known axis and zero-flip witnesses in three slices."""
import json, math
from pathlib import Path

def axis(p,q):
    return any((pow(2,h,q)==1 or pow(2,h,q)==q-1) for h in range(1,p))

def zero_flip_present(p,q1,q2):
    if math.gcd(q1,q2)!=1: return False
    n=1<<p; K=(n-1)//q1; inv=pow(q1,-1,q2)
    for i in range(p):
        v=((1<<i)*inv)%q2
        for bit, rem in [(1,v),(0,(-v)%q2)]:
            k=rem or q2
            while k<=K:
                a=k*q1
                block=1<<(i+1); half=1<<i
                ones_below=(a//block)*half + max(0,a%block-half)
                ones=n//2-ones_below
                count=ones if bit else (n-a-ones)
                if count>0: return True
                k+=q2
    return False

p=32
qs=range(262145,524288,2)
axis_q={q for q in qs if axis(p,q)}
assert len(axis_q)==24, len(axis_q)
fixed=(262145,500383,524287)
rows=[]
for q1 in fixed:
    a1=axis(p,q1)
    counts={k:0 for k in ('neither','axis_only','zero_flip_only','both')}
    for q2 in qs:
        a=a1 or q2 in axis_q
        z=zero_flip_present(p,q1,q2)
        counts['both' if a and z else 'axis_only' if a else 'zero_flip_only' if z else 'neither']+=1
    rows.append({'q1':q1,'axis_q1':a1,**counts,'axis_union':counts['axis_only']+counts['both'],'ZF_total':counts['zero_flip_only']+counts['both'],'union':131072-counts['neither']})
assert [r['ZF_total'] for r in rows]==[57485,66613,48723],rows
print(json.dumps({'schema':'PREFIX891_R6_AXIS_ZF_THREE_SLICES_V1','frozen_scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','p':p,'q1_slices':list(fixed),'q2_domain':'all odd q2 in [262145,524287]','axis_q_count':len(axis_q),'axis_q_list':sorted(axis_q),'rows':rows,'totals':{k:sum(r[k] for r in rows) for k in ('neither','axis_only','zero_flip_only','both','axis_union','ZF_total','union')},'coverage':'exact exhaustive 393216 ordered modulus pairs; every pair classified into exactly one of four cases','math_status':'AUTHOR_EXACT_FINITE_CHECKED_NOT_INDEPENDENTLY_REVIEWED'},indent=2,ensure_ascii=False))
