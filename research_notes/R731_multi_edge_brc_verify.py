#!/usr/bin/env python3
"""R731 1..4 edge exact BRC support/polytope verification; stdlib integer arithmetic."""
from itertools import combinations,product
from functools import lru_cache
from math import factorial
import json

AX=range(6)
OUTER=tuple(range(2,6))
BASE=frozenset(t for t in combinations(AX,3) if not (0 in t and 1 in t))
@lru_cache(None)
def count(a, mask=0):
    if not any(a):return 1
    if sum(a)%3:return 0
    i=next(j for j,v in enumerate(a) if v)
    E=BASE | {(0,1,k) for k in OUTER if mask&(1<<(k-2))}
    result=0
    for t in E:
        if i not in t:continue
        j,k=(p for p in t if p!=i)
        if a[j] and a[k]:
            b=list(a);b[i]-=1;b[j]-=1;b[k]-=1
            result+=a[j]*a[k]*count(tuple(b),mask)
    return result

def coeff(a,mask,s):
    m=sum(a)//3
    chosen=[k for k in OUTER if mask&(1<<(k-2))]
    q=sum(s)
    if q>min(a[0],a[1],m):return 0
    if q<max(0,a[0]+a[1]-m):return 0
    b=list(a);b[0]-=q;b[1]-=q
    for k,x in zip(chosen,s):
        if x>a[k]:return 0
        b[k]-=x
    if any(x>m-q for x in (b[0]+b[1],b[2],b[3],b[4],b[5])):return 0
    factor=(factorial(a[0])//factorial(a[0]-q))*(factorial(a[1])//factorial(a[1]-q))
    divisor=1
    for k,x in zip(chosen,s):
        factor*=factorial(a[k])//factorial(a[k]-x)
        divisor*=factorial(x)
    assert factor%divisor==0
    val=factor//divisor*count(tuple(b),0)
    assert val>0,(a,mask,s,b)
    return val

def poly(a,mask):
    chosen=[k for k in OUTER if mask&(1<<(k-2))]
    return {s:v for s in product(*(range(a[k]+1) for k in chosen)) if (v:=coeff(a,mask,s))}

def vectors(total,n=6):
    if n==1:yield(total,);return
    for x in range(total+1):
        for y in vectors(total-x,n-1):yield(x,)+y

def main():
    stats={}
    for m in range(0,4):
        st={'vectors':0,'subset_tests':0,'positive_tests':0,'max_support_points':0}
        for a in vectors(3*m):
            st['vectors']+=1
            for mask in range(1,16):
                P=poly(a,mask)
                assert sum(P.values())==count(a,mask),(m,a,mask)
                st['subset_tests']+=1
                if P:st['positive_tests']+=1;st['max_support_points']=max(st['max_support_points'],len(P))
        stats[str(m)]=st
    family=0
    for d in (2,3,4):
        for m in range(d,9):
            for s in product(range(1,m+1),repeat=d):
                if sum(s)!=m:continue
                a=(m,m,*s,*(0 for _ in range(4-d)))
                mask=(1<<d)-1
                P=poly(a,mask)
                assert P=={tuple(s):factorial(m)**2},(m,d,s,P)
                for missing in range(d):
                    assert count(a,mask^(1<<missing))==0,(m,d,s,missing)
                family+=1
    stats['strict_cooperation_family']={'configurations_tested':family,'d_values':[2,3,4],'m_up_to':8,'m8_count':factorial(8)**2}
    with open('R731_multi_edge_brc_results.json','w') as f:json.dump({'marker':'R731_MULTI_EDGE_LATTICE_POLYTOPE_EXACT_PASS','stats':stats,'model':'six-axes candidate H; no native event verified'},f,ensure_ascii=False,indent=2)
    print(json.dumps(stats,indent=2))
    print('R731_MULTI_EDGE_LATTICE_POLYTOPE_EXACT_PASS')
if __name__=='__main__':main()
