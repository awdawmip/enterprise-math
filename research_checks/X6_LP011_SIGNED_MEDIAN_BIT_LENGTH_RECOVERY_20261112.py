#!/usr/bin/env python3
"""X6 selected signed 3-axis: exact rho + L1 + median-sign repair.
This is a finite regression for an independently proved infinite-domain theorem.
"""
from itertools import product
from math import factorial

def normalize(d):
    h = min(d)
    return tuple(x-h for x in d)

def length(d):
    return sum(abs(x) for x in d)

def brc(d):
    n = length(d)
    return factorial(n) // (factorial(abs(d[0]))*factorial(abs(d[1]))*factorial(abs(d[2])))

def median(a):
    return sorted(a)[1]

def branch_sign(d,a):
    z = min(d) + median(a)
    return -1 if z<0 else (1 if z>0 else 0)

def recover_depth(a,n,s):
    """Return exact signed depth h or None on unachievable (a,n,s)."""
    assert len(a)==3 and min(a)==0 and all(isinstance(x,int) and x>=0 for x in a)
    b, m = sorted(a)[1:]
    if n < m or s not in (-1,0,1): return None
    if s==0:
        h = -b
        return h if n==m else None
    if s < 0:
        if n <= 2*m - b:
            h = m-b-n
        else:
            u=n+b+m
            if u%3: return None
            h=-u//3
    else:
        if n <= m+b:
            h=n-b-m
        else:
            u=n-b-m
            if u%3: return None
            h=u//3
    if h+b==0 or ((h+b>0)-(h+b<0))!=s: return None
    d=tuple(h+x for x in a)
    return h if length(d)==n and normalize(d)==a else None

def main():
    tested=0
    signatures={}
    collisions=[]
    for d in product(range(-9,10),repeat=3):
        a=normalize(d); n=length(d); s=branch_sign(d,a)
        h=recover_depth(a,n,s)
        assert h==min(d),(d,a,n,s,h)
        tested+=1
        signatures.setdefault((a,n),set()).add(h)
    assert max(map(len,signatures.values()))==2
    for (a,n), depths in signatures.items():
        assert len(depths)<=2
        if len(depths)==2:
            signs={(-1 if h+median(a)<0 else (1 if h+median(a)>0 else 0)) for h in depths}
            assert signs=={-1,1},(a,n,depths,signs)
            collisions.append((a,n,sorted(depths)))
    a=(0,1,4); d1=(-2,-1,2); d2=(0,1,4)
    assert normalize(d1)==normalize(d2)==a
    assert length(d1)==length(d2)==5
    assert brc(d1)==30 and brc(d2)==5
    assert branch_sign(d1,a)==-1 and branch_sign(d2,a)==1
    # verify piecewise forward length slopes and inversion for independent residuals
    n_pieces=0
    for x in range(0,9):
      for y in range(0,9):
       for z in range(0,9):
        a=(x,y,z)
        if min(a)!=0: continue
        b,M=sorted(a)[1:]
        for h in range(-16,17):
          n = length(tuple(h+t for t in a))
          if h<=-M: expect=-3*h-b-M
          elif h<=-b: expect=M-b-h
          elif h<=0: expect=M+b+h
          else: expect=3*h+b+M
          assert n==expect,(a,h,n,expect)
          n_pieces+=1
    print(f'PASS selected_X6_signed_L1_median_bit: signed_points={tested} length_signatures={len(signatures)} double_fibres={len(collisions)} piecewise_cases={n_pieces} witness_BRC=30_vs_5')
if __name__=='__main__':main()
