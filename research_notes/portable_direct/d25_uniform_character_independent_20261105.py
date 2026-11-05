#!/usr/bin/env python3
"""Independent original-binomial audit against the hypergeometric recurrence scan."""
import csv
from math import comb
from pathlib import Path
p=Path(__file__).with_name('uniform_character_results.csv')
rows={int(r['p']):r for r in csv.DictReader(p.open())}
checked=0
for prime,r in rows.items():
    if prime>1000:
        continue
    modulus=prime**4
    inv216=pow(216,-1,modulus)
    power=1
    value=0
    half=0
    for k in range(prime):
        term=(6*k+1)*comb(2*k,k)**2*comb(3*k,k)*power%modulus
        value=(value+term)%modulus
        if k<=(prime-1)//2:half=(half+term)%modulus
        power=power*inv216%modulus
    assert value==int(r['full_p4']),(prime,value,r['full_p4'])
    assert half%prime**3==int(r['half_p3']),(prime,half,r['half_p3'])
    checked+=1
print(f'INDEPENDENT_ORIGINAL_BINOMIAL_CHECK_PASS: {checked} primes <=1000')
