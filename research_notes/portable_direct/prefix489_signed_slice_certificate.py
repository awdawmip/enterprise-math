#!/usr/bin/env python3
"""PREFIX-489 exact certificate; ordinary native signed X6 with s=0, y_b=y_c=0, q=0.
Counts BRC observation SUPPORT masks, not path multiplicities. Python3 standard library.
"""
from collections import defaultdict, Counter
from itertools import product
from math import comb

AXES='abcde'
ALPHABET='aAbBcCdDeE'
N,B,C=1,2,4


def p_vectors(m):
    for pa in range(m+1):
      for pb in range(m-pa+1):
       for pc in range(m-pa-pb+1):
        for pd in range(m-pa-pb-pc+1):
         yield pa,pb,pc,pd,m-pa-pb-pc-pd


def raw_masks(m, y=(0,0,0)):
    out=defaultdict(int)
    for pa,pb,pc,pd,pe in p_vectors(m):
        v,w=pb+2*pd+pe,pc+pe
        # every vector with m>=1 can end in an uppercase letter, KMP q=0.
        if m==0 and y[0]>0 and y[1]==0 and y[2]==0:
            continue
        if pb==0 and pc==0: out[v,w] |= N
        if pb: out[v,w] |= B
        if pc: out[v,w] |= C
    return dict(out)


def predicted_masks(m,y=(0,0,0)):
    out={}
    if m==0 and y[0]>0 and y[1]==0 and y[2]==0:
        return out
    for w in range(m+1):
        for v in range(2*m-w+1):
            mask=0
            if v>=w and (v-w)%2==0 and v+w<=2*m: mask |= N
            if w<=m-1 and 1<=v<=2*m-w-1: mask |= B
            if 1<=w<=m and v<=2*m-w-1: mask |= C
            assert mask, (m,v,w)
            out[v,w]=mask
    return out


def counts(m):
    if m==0: return {1:1,2:0,4:0,3:0,5:0,6:0,7:0}
    return {1:m+2,2:m,4:2*m-1,3:m-1,5:0,6:(m-1)**2,7:m*(m-1)//2}


def kmp_state(s,w):
    for q in range(len(w),0,-1):
        if s.endswith(w[:q]):return q
    return 0


def brute_upto(nmax,gate):
    obs=defaultdict(int)
    total=0
    for n in range(nmax+1):
        for word in product(ALPHABET,repeat=n):
            s=''.join(word)
            if kmp_state(s,gate)!=0:continue
            cnt=Counter(word)
            if cnt['b']!=cnt['B'] or cnt['c']!=cnt['C']:continue
            ps={a:min(cnt[a],cnt[a.upper()]) for a in AXES}
            yy=tuple(cnt[a]-cnt[a.upper()] for a in 'ade')
            v=ps['b']+2*ps['d']+ps['e']
            ww=ps['c']+ps['e']
            kind=N
            for k in s:
                if k in 'bB':kind=B;break
                if k in 'cC':kind=C;break
            obs[n,yy,v,ww]|=kind
            total+=1
    return obs,total


def theoretical_upto(nmax):
    obs={}
    for n in range(nmax+1):
        for ya in range(-n,n+1):
         for yd in range(-n,n+1):
          for ye in range(-n,n+1):
            rem=n-abs(ya)-abs(yd)-abs(ye)
            if rem<0 or rem%2:continue
            for (v,w),mask in predicted_masks(rem//2,(ya,yd,ye)).items():
                obs[n,(ya,yd,ye),v,w]=mask
    return obs


def coeff_series(nmax):
    # Number of signed displacement triples with length k:
    # ((1+z)/(1-z))^3 = (1+z)^3*(1-z)^-3
    signed=[]
    for k in range(nmax+1):
       signed.append(sum(comb(3,j)*comb(k-j+2,2) for j in range(min(k,3)+1)))
    out=[]
    for n in range(nmax+1):
        total={k:0 for k in (1,2,4,3,5,6,7)}
        for m in range(n//2+1):
            for k,v in counts(m).items():total[k]+=v*signed[n-2*m]
        total[1]-=1 if n>=1 else 0 # correction: one pure a^n per positive length
        out.append(total)
    return out


def main():
    for m in range(31):
        full=raw_masks(m)
        assert full==predicted_masks(m),m
        assert Counter(full.values())==Counter({k:v for k,v in counts(m).items() if v}),m
        assert len(full)==(m+1)*(3*m+2)//2
    print('LATTICE_M0_TO_30_PASS', 'checked_vectors',sum(comb(m+4,4) for m in range(31)))
    for m in (0,1,2,3,5,8):
      for y in product(range(-2,3),repeat=3):
        assert raw_masks(m,y)==predicted_masks(m,y),(m,y)
    print('SIGNED_SHIFT_750_CASES_PASS')
    for gate in ('aab','aba'):
        b,n=brute_upto(5,gate)
        p=theoretical_upto(5)
        assert b==p, (gate,set(b.items())^set(p.items()))
        print('INDEPENDENT_ORDERED_ENUM_PASS',gate,'path_count_examined_in_slice',n,'fibers',len(b))
    # Independent rational-form coefficient arithmetic after canceling the (1+z)^3 factor.
    def binom_shift(n,s,k):
        return comb(n-s+k-1,k-1) if n>=s else 0
    for n, row in enumerate(coeff_series(40)):
        closed={
          N: binom_shift(n,0,5)+binom_shift(n,1,5)+binom_shift(n,2,5)+binom_shift(n,3,5)-binom_shift(n,4,5)-binom_shift(n,5,5)-(1 if n>=1 else 0),
          B: binom_shift(n,2,5)+binom_shift(n,3,5),
          C: binom_shift(n,2,5)+binom_shift(n,3,5)+binom_shift(n,4,5)+binom_shift(n,5,5),
          N|B: binom_shift(n,4,5)+binom_shift(n,5,5),
          N|C: 0,
          B|C: binom_shift(n,4,6)+binom_shift(n,6,6),
          N|B|C: binom_shift(n,4,6)
        }
        assert row==closed,(n,row,closed)
        total=comb(n+5,5)+(2*comb(n+3,5) if n>=2 else 0)-(1 if n>=1 else 0)
        assert sum(row.values())==total,(n,row,total)
    print('RATIONAL_CANCELLATION_AND_TOTAL_FORMULA_0_TO_40_PASS')
    c=coeff_series(12)
    for n in (0,1,2,4,6,8,10,12):
        print('ALL_SIGNED_DISPLACEMENT_LENGTH',n,'N B C NB NC BC NBC', *(c[n][i] for i in (1,2,4,3,5,6,7)))
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
