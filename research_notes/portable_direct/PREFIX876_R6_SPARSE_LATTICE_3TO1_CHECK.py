#!/usr/bin/env python3
"""PREFIX-876: complete integer count and constructive witness tests for p=32 B=19."""
import json
from collections import Counter

B=19; P=32; Q=(1<<B)-1; N=1<<P
D={}
for i in range(1,B): D[1<<i]=('one',i,None)
for i in range(2,B):
    for j in range(1,i): D[(1<<i)+(1<<j)]=('sum',i,j)
for i in range(2,B+1):
    for j in range(1,i): D.setdefault((1<<i)-(1<<j),('diff',i,j))
assert len(D)==307 and sum(D)==24903696
DP=dict(D)
for i in (B,B+1): DP[1<<i]=('one',i,None)
assert len(DP)==309

def ceildiv(a,b): return -(-a//b)
def odds(lo,hi):
    lo+=(lo%2==0)
    return max(0,1+(hi-lo)//2)
def bounds(d):
    return max(1,ceildiv(d+1,3)),min(Q,(Q+d)//3)
def valid(x,y):
    return 1<=x<=Q and x%2==1 and 1<=y<=Q and y%2==1
def witness(x,y,rep):
    typ,i,j=rep
    z=1<<i
    a=3*x; b=y
    assert a-b==(z if typ=='one' else z+(1<<j) if typ=='sum' else z-(1<<j))
    if typ=='one':
        u=0 if a&z else z
        A=(u,u); C=(u+a,u+b)
    elif typ=='sum':
        t=1<<j
        u=0 if a&z else z
        A=(u,u+t); C=(u+a,u+b+t)
    else:
        t=1<<j
        u=t if (a+t)&z else t+z
        A=(u,u-t); C=(u+a,u+b-t)
    assert A!=C and all(0<=v<N for v in A+C)
    assert (A[0]^A[1]).bit_count()<=1
    assert (C[0]^C[1]).bit_count()<=1
    assert A[0]%x==C[0]%x and A[1]%y==C[1]%y
    return [list(A),list(C)]

total=0; diag=0
types=Counter()
for d,rep in DP.items():
    lo,hi=bounds(d)
    total+=odds(lo,hi)
    types[rep[0]]+=odds(lo,hi)
    if d%4==2 and valid(d//2,d//2):diag+=1
    first=lo+(lo%2==0)
    if first<=hi:
        last=hi-(hi%2==0)
        middle=min(last,max(first,(first+last)//4*2+1))
        for x in {first,middle,last}:
            y=3*x-d
            assert valid(x,y)
            witness(x,y,rep)

intersection=0
for d in DP:
    lo,hi=bounds(d)
    for h in D:
        for sign in (-1,1):
            num=d+sign*h
            if num%2:continue
            x=num//2; y=x+sign*h
            if lo<=x<=hi and valid(x,y):
                assert abs(x-y)==h
                intersection+=1
old=0;old_intersection=0
for i in range(1,21):
    d=1<<i
    lo,hi=bounds(d)
    old+=odds(lo,hi)
    if d%4==2 and valid(d//2,d//2):old-=1
    for h in D:
        for sign in (-1,1):
            num=d+sign*h
            if num%2:continue
            x=num//2;y=x+sign*h
            if lo<=x<=hi and valid(x,y):old_intersection+=1
old_outside=old-old_intersection
non_diagonal=total-diag
new_outside=non_diagonal-intersection
assert (total,diag,intersection,old,old_outside,new_outside)==(
    27000811,34,25427,1747629,1746491,26975350)
for b in range(3,7):
    q=(1<<b)-1
    small={1<<i for i in range(1,b)}
    small|={(1<<i)+(1<<j) for i in range(2,b) for j in range(1,i)}
    small|={(1<<i)-(1<<j) for i in range(2,b+1) for j in range(1,i)}
    allsmall=small|{1<<b,1<<(b+1)}
    formula=sum(odds(max(1,ceildiv(d+1,3)),min(q,(q+d)//3)) for d in allsmall)
    explicit=sum(3*x-y in allsmall for x in range(1,q+1,2) for y in range(1,q+1,2))
    assert formula==explicit

result={
  "status":"ALL_EXACT_ASSERTIONS_PASSED",
  "p":P,"B":B,"Q":Q,"N":N,
  "D_size":len(D),"D_extended_size":len(DP),
  "three_to_one_including_diagonal":total,
  "diagonal":diag,
  "three_to_one_non_diagonal":non_diagonal,
  "intersection_with_PREFIX874":intersection,
  "new_beyond_PREFIX874":new_outside,
  "old_PREFIX875_non_diagonal":old,
  "old_PREFIX875_new_beyond_PREFIX874":old_outside,
  "strict_increment_over_PREFIX874_875":new_outside-old_outside,
  "confirmed_union_PREFIX874_875_876":136052720+new_outside,
  "counts_by_representation":dict(types),
  "sample_d6_x160001":witness(160001,479997,DP[6]),
  "coverage":"309 difference interval counts; 309x307x2 intersection candidates; low/mid/high witness per difference; small B=3..6 independent double loops"
}
assert result["confirmed_union_PREFIX874_875_876"]==163028070
print(json.dumps(result,indent=2))
