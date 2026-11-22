#!/usr/bin/env python3
"""Rooted signed BRC return-loop sums; exact integers, native X6 chart and named port."""
from collections import defaultdict
from fractions import Fraction
import json

D=[(axis,sign) for sign in (1,-1) for axis in range(6)]
ZERO=(0,)*6
E1=(1,0,0,0,0,0)

def crossed(x,d):return (x==ZERO and d==0) or (x==E1 and d==6)
def nxt(x,d):
    a=list(x);axis,sgn=D[d];a[axis]+=sgn
    return tuple(a)
def reverse(d):return (d+6)%12

def returns(kmax=6):
    dp={(ZERO,6):1};rows=[]
    for n in range(2*kmax+1):
        if n%2==0:
            k=n//2
            ports={str(h):dp.get((ZERO,h),0) for h in range(12) if dp.get((ZERO,h),0)}
            count=sum(ports.values())
            s=Fraction(int(k==0))-Fraction(count,6**(2*k+1))
            rows.append({'k':k,'signed_loop_numerator':count,'masked_stable_signed_amplitude':str(s),
                         'return_cell_named_port_numerators':ports})
        if n==2*kmax:break
        out=defaultdict(int)
        for (x,h),val in dp.items():
            for d in range(12):
                if crossed(x,d):continue
                out[(nxt(x,d),reverse(d))]+=val*(-5 if h==d else 1)
        dp={s:v for s,v in out.items() if v}
    return rows

def grade3_direct():
    dp={(ZERO,6,0):1};res=[]
    for n in range(1,9):
        out=defaultdict(int)
        for (x,h,k),val in dp.items():
            for d in range(12):
                kk=k+(d>=6)
                if kk>3 or crossed(x,d):continue
                out[(nxt(x,d),reverse(d),kk)]+=val*(-5 if h==d else 1)
        dp={s:v for s,v in out.items() if v}
        if n>=7:
            total=sum(val for (x,h,k),val in dp.items() if k==3)
            res.append({'n':n,'grade3_numerator_sum':total,'expected':2365*6**(n-7)})
    return res

def main():
    rows=returns()
    assert [r['signed_loop_numerator'] for r in rows]==[1,-25,390,-2365,-49550,1645010,-22026080]
    assert [r['masked_stable_signed_amplitude'] for r in rows]==[
        '5/6','25/216','-65/1296','2365/279936','24775/5038848','-822505/181398528','688315/408146688']
    checks=grade3_direct()
    assert [q['grade3_numerator_sum'] for q in checks]==[2365,14190]
    assert all(q['grade3_numerator_sum']==q['expected'] for q in checks)
    print(json.dumps({'schema':'PREFIX1009_R6_LINK_RENEWAL_V1',
        'science':'Stage46 candidate signed BRC, X6, incoming -e1, closed {0,e1}, integer 1 or -5 weights; charts are relative',
        'theorem':'For all k>=0, n>=2k+1, sum_{Cell,port} Psi^L_(n,k) = [k=0] - L_k/6^(2k+1); L_k is complete signed sum of masked 2k-step loops returning to chosen Cell anchor.',
        'exact_rooted_return_loops':rows,'independent_grade3_full_state_checks':checks,
        'method':'12-port integer dynamic programming without negative count for loop returns; independent negative-graded direct evolution for n=7,8; theorem itself follows from first-hit and BRC orientation-row sum cancellation.',
        'review':'AUTHOR_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED'},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
