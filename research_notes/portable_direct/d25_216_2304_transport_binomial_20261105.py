#!/usr/bin/env python3
"""Independent integer-binomial exact audit of 216/2304 cross-model data."""
import csv
from math import comb
from pathlib import Path
rows={int(r['p']):r for r in csv.DictReader((Path(__file__).with_name('cross_model_results.csv')).open())}
count=0
for p,r in sorted(rows.items()):
    if p>997:continue
    m=p**4
    x=pow(216,-1,m);y=pow(2304,-1,m)
    pwx=pwy=1
    w=v=1
    for k in range(1,p):
        pwx=(pwx*x)%m
        pwy=(pwy*y)%m
        wa=(6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pwx%m
        va=(8*k+1)*comb(2*k,k)**2*comb(4*k,2*k)*pwy%m
        w=(w+wa)%m
        v=(v+va)%m
    assert w==int(r['w4']),(p,'w',w,r['w4'])
    assert v==int(r['v4']),(p,'v',v,r['v4'])
    assert (w-v)%m==int(r['difference_p4']),(p,'difference')
    count+=1
print('CROSS_MODEL_INDEPENDENT_BINOMIAL_PASS',count)
