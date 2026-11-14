#!/usr/bin/env python3
"""R154C: exact finite checks of the proved infinite true-word alias family."""
import json
from fractions import Fraction


def bounds_and_cuts(w):
    m=len(w)
    p=[0]
    for x in w:p.append(p[-1]+x)
    al,be=Fraction(0),Fraction(1)
    for q in range(1,m+1):
        minones=m+1
        maxones=-1
        for i in range(m-q+1):
            k=p[i+q]-p[i]
            if k<minones:minones=k
            if k>maxones:maxones=k
        al=max(al,Fraction(maxones-1,q))
        be=min(be,Fraction(minones+1,q))
    if al>=be:return None
    a,b=al.numerator,al.denominator
    c,d=be.numerator,be.denominator
    U=min(b*(p[j]+1)-a*j for j in range(m+1))
    V=max(d*p[j]-c*j for j in range(m+1))
    return a,b,c,d,U,V


def ceildiv(x,y):return -((-x)//y)

def count(L,a,b,c,d,U,V):
    return ceildiv(c*L-V,d)-(a*L-U)//b-1


def run(max_r=50):
    cases=0
    L_checks=0
    rows=[]
    for r in range(1,max_r+1):
        w=(0,)+(1,)*r+(0,)+(1,)*(r+1)+(0,)
        v=(0,)+(1,)*(r+1)+(0,)+(1,)*r+(0,)
        assert w!=v
        t=(r,r+1,r+1,r+2,1,0)
        assert bounds_and_cuts(w)==t and bounds_and_cuts(v)==t,(r,bounds_and_cuts(w),bounds_and_cuts(v),t)
        P=(r+1)*(r+2)
        for L in range(1,2*P+2):
            observed=count(L,*t)
            formula=ceildiv(L+1,r+1)-L//(r+2)-1
            assert observed==formula and observed>=0,(r,L,observed,formula)
            L_checks+=1
        cases+=1
        if r<=4 or r in (10,25,50):
            rows.append({'r':r,'m':len(w),'a':r,'b':r+1,'c':r+1,'d':r+2,'U':1,'V':0,'P':P})
    return {'result':'R154C_INFINITE_GENUINE_UNEQUAL_DENOMINATOR_ALIASES_PASS',
            'integer_family_range':[1,max_r],
            'distinct_word_pairs':cases,
            'verified_count_values':L_checks,
            'arithmetic':'exact integers and fractions.Fraction',
            'sample_rows':rows}


if __name__=='__main__':
    res=run()
    with open('R154C_verification.json','w',encoding='utf-8') as f:
        json.dump(res,f,ensure_ascii=False,indent=2)
    print(json.dumps(res,ensure_ascii=False,indent=2))
