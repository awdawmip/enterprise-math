#!/usr/bin/env python3
"""Independent congruence-first 32-bit census for PREFIX-918, Python integers."""
from math import gcd
from json import dump
from pathlib import Path
P=32; N=1<<P; A_MOD=321651; B_MOD=440665

def ones_before(z,j):
    h=1<<j
    q,r=divmod(z,2*h)
    return q*h+max(0,r-h)

def high_prefix(z,hi,lo,u,v,shift):
    h=1<<hi
    q,r=divmod(z,2*h)
    length=min(h,max(0,r-u*h))
    one=ones_before(shift+length,lo)-ones_before(shift,lo)
    return q*(h//2)+(one if v else length-one)

def overlap(lo1,hi1,lo2,hi2):
    return max(0,min(hi1,hi2)-max(lo1,lo2))

def same(i,A,u,v,length):
    h=1<<i; period=h*2; shift=A%period
    def tail(z):
        return sum(overlap(u*h,min((u+1)*h,z),v*h-shift+t*period,(v+1)*h-shift+t*period) for t in (0,1))
    blocks,remaining=divmod(length,period)
    return blocks*tail(period)+tail(remaining)

def multiplicity(A,i,j,eps,eta):
    L=N-A; u=(eps==-1);v=(eta==-1)
    if i>j:return high_prefix(L,i,j,u,v,A)
    if i<j:return high_prefix(N,j,i,v,u,-A)-high_prefix(A,j,i,v,u,-A)
    return same(i,A,u,v,L)

def main():
    assert gcd(A_MOD,B_MOD)==1
    inv=pow(A_MOD,-1,B_MOD)
    max_k=(N-1)//A_MOD
    totals=[0]*4; families=0
    for i in range(P):
        for j in range(P):
            for eps in (-1,1):
                for eta in (-1,1):
                    rhs=eps*(1<<i)-eta*(1<<j)
                    k=(rhs*inv)%B_MOD
                    if k==0 or k>max_k:continue
                    A=k*A_MOD
                    D=A-rhs
                    assert D%B_MOD==0
                    count=multiplicity(A,i,j,eps,eta)
                    if not count:continue
                    families+=1
                    index=0 if (i>j and D>0) else 1 if i>j else 2 if i<j else 3
                    totals[index]+=count
    expected=[196960748158,7516192768,204476940926,13416271437]
    assert totals==expected and families==557,(totals,families)
    result={'schema':'PREFIX918_INDEPENDENT_RESIDUE_CHECK_V1','method':'congruence-first modular-inverse enumeration of k, independent of first-port k scan','p':P,'a':A_MOD,'b':B_MOD,'families_with_positive_multiplicity':families,'categories':totals,'total':sum(totals),'agrees_with_original_32bit_Cpp':True}
    path=Path(__file__).with_name('PREFIX918_R6_INDEPENDENT_RESIDUE_RESULTS.json')
    with path.open('w') as f:dump(result,f,indent=2);f.write('\n')
    print(result)
if __name__=='__main__':main()
