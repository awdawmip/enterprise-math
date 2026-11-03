#!/usr/bin/env python3
"""PREFIX-465: exact X6 positive-weight observer certificate (stdlib only)."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
POSITIVE=(6,12,18,24,36)
STEP=[(0,0)] + [(i,sgn) for i in range(5) for sgn in (1,-1)]
COLS=((0,0),(1,0),(0,1),(2,0),(1,1))
def size(p):
    assert p>=0
    return (p+1)*(3*p+2)//2
def offset(p,c):
    return c*(2*p+1)-c*(c-1)//2
def pack(p,A,C):
    assert 0<=C<=p and 0<=A<=2*p-C
    value=offset(p,C)+A
    assert 0<=value<size(p)
    return value
def unpack(p,key):
    assert 0<=key<size(p)
    lo,hi=0,p+1
    while lo+1<hi:
        m=(lo+hi)//2
        if offset(p,m)<=key:lo=m
        else:hi=m
    C=lo; A=key-offset(p,C)
    assert 0<=A<=2*p-C
    return A,C
def q_of(m,s,y):
    v=m-s-sum(abs(z) for z in y)
    assert v>=0 and v%2==0
    return v//2
def weight(m,s,y,A,C):
    p=q_of(m,s,y)
    w=Fraction((6**p)*(2**A)*(3**C),1)
    for idx,z in enumerate(y):
        if z>0: w*=POSITIVE[idx]**z
    return w
def do_step(m,s,y,A,C,bit,step_idx):
    if step_idx==0:
        if m>0 and bit!=1:return None
        return s+1,y,A,C,0
    i,sgn=STEP[step_idx]
    arr=list(y)
    old=arr[i]
    arr[i]+=sgn
    if old*sgn<0:
        da,dc=COLS[i]
        A+=da; C+=dc
    return s,tuple(arr),A,C,int(step_idx==1)
def dense_dp(max_m):
    cur={(0,(0,)*5,0,0):1}
    summaries=[]
    for m in range(max_m+1):
        hist=defaultdict(int)
        for (s,y,packed,bit),count in cur.items():
            p=q_of(m,s,y)
            A,C=unpack(p,packed)
            hist[(s,y,weight(m,s,y,A,C),bit)]+=count
        summaries.append((m,len(cur),sum(cur.values()),dict(hist)))
        if m==max_m:break
        nxt=defaultdict(int)
        for (s,y,packed,bit),count in cur.items():
            p=q_of(m,s,y)
            A,C=unpack(p,packed)
            for step_idx in range(11):
                v=do_step(m,s,y,A,C,bit,step_idx)
                if v is None:continue
                ss,yy,AA,CC,bb=v
                pp=q_of(m+1,ss,yy)
                nxt[(ss,yy,pack(pp,AA,CC),bb)]+=count
        cur=dict(nxt)
    return summaries
def brute(m):
    hist=defaultdict(int)
    for word in product(range(11),repeat=m):
        s=0;y=(0,)*5;A=C=0;bit=0;valid=True
        product_weight=Fraction(1,1)
        for t,k in enumerate(word):
            val=do_step(t,s,y,A,C,bit,k)
            if val is None:
                valid=False;break
            s,y,A,C,bit=val
            if k>0 and k%2==1:
                product_weight*=POSITIVE[(k-1)//2]
        if valid:
            hist[(s,y,product_weight,bit)]+=1
    return dict(hist)
def brute_fiber(p):
    S=set()
    for a in range(p+1):
      for b in range(p-a+1):
       for c in range(p-a-b+1):
        for d in range(p-a-b-c+1):
         S.add((a+2*c+d,b+d))
    return S
def represent(p,A,C):
    d=max(0,A-2*(p-C))
    remain=A-d
    c=remain//2;a=remain%2;b=C-d
    assert min(a,b,c,d)>=0 and a+b+c+d<=p
    assert a+2*c+d==A and b+d==C
    return a,b,c,d
def main():
    for p in range(0,25):
        actual=brute_fiber(p)
        target={(A,C) for C in range(p+1) for A in range(2*p-C+1)}
        assert actual==target and len(actual)==size(p)
        seen=set()
        for (A,C) in target:
            represent(p,A,C)
            code=pack(p,A,C)
            assert unpack(p,code)==(A,C)
            seen.add(code)
        assert seen==set(range(size(p)))
    print('LATTICE_P_0_24_PASS')
    for p in (0,1,2,4,8,16,32,64,128,1024):
        for C in {0,p//2,p}:
            for A in {0,(2*p-C)//2,2*p-C}:
                assert unpack(p,pack(p,A,C))==(A,C)
        mixed=(2*p+1)*(p+1)
        dense=size(p)
        print(f'P={p} SIGNATURES={dense} MIXED_SLOTS={mixed} DENSE_BITS={(dense-1).bit_length()} MIXED_BITS={(mixed-1).bit_length()}')
    assert size(16)==425 and (size(16)-1).bit_length()==9
    assert ((2*16+1)*(16+1)-1).bit_length()==10
    print('FINITE_P16_ONE_BIT_REDUCTION_PASS')
    assert brute(2).get((0,(1,1,0,0,0),Fraction(72),0),0)>0
    assert brute(2).get((0,(1,1,0,0,0),Fraction(72),1),0)>0
    print('ORDER_WITNESS_2_PATHS_EQUAL_ENDPOINT_WEIGHT_DISTINCT_GATE_PASS')
    reports=dense_dp(7)
    for m,states,total,hist in reports:
        if m<=5:
            direct=brute(m)
            assert hist==direct,(m,len(hist),len(direct))
        assert all(v>0 for v in hist.values())
        print(f'M={m} DENSE_STATES={states} HISTOGRAM_ROWS={len(hist)} LEGAL_ORDERED_PATHS={total} DIRECT_BRUTE={m<=5} PASS')
    print('ALL_CHECKS_PASS')
if __name__=='__main__':main()
