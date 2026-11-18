#!/usr/bin/env python3
"""Exact per-positive-cache-key signature counts in the frozen native BRC DFA.
Independently cross-check with quota-aware backward suffix DP in VERIFY_EC49FFW.py.
This certifies operation-word counts only, not signed X6 minimum prefix cost.
"""
from math import factorial,comb
from VERIFY_EC49FFW import suffix,LOW
def per_key(h,z,m,f,g):
    a=z-1;e=z
    assert 2*z-1+m+f+g==h and z>=1 and min(m,f,g)>=0 and m+g>0
    key=(h+1-g,m+g,z)
    if not m:return key,{str(s):0 for s in LOW}
    P=factorial(h)//(factorial(a)*factorial(e)*factorial(m)*factorial(f)*factorial(g))
    ans={'1':P*(m+g)//h, '2':P*(a+e+f)//h,
         '4':P*(m+f)//h, '8':P*(a+e+g)//h}
    assert sum(ans.values())==2*P
    return key,ans
def check(h):
    actual={'1':0,'2':0,'4':0,'8':0}
    positive_keys=0;low_keys=0;quota_splits=0
    for z in range(1,(h+1)//2+1):
        remaining=h-2*z+1
        for m in range(remaining+1):
            for f in range(remaining-m+1):
                g=remaining-m-f
                if m+g==0:continue
                positive_keys+=1
                quota_splits+=m+1
                key,calc=per_key(h,z,m,f,g)
                if m:
                    low_keys+=1
                    a=z-1;e=z
                    _,cc,_,_=suffix((a,m,0,e,f,g),0)
                    _,dd,_,_=suffix((a,0,m,e,f,g),0)
                    from_dfa={str(s):cc[i]+dd[i] for i,s in enumerate(LOW)}
                    assert calc==from_dfa,(h,key,calc,from_dfa)
                for s in actual:actual[s]+=calc[s]
    assert low_keys==sum(comb(h-2*z+2,2) for z in range(1,h//2+1))
    assert positive_keys==sum(comb(h-2*z+3,2)-1 for z in range(1,(h+1)//2+1))
    return h,positive_keys,quota_splits,low_keys,actual
if __name__=='__main__':
    for h in range(3,15):
        row=check(h)
        print('H%d total_positive_keys=%d all_splits=%d low_keys=%d low_splits=%d signature_counts=%s'
              %(row[0],row[1],row[2],row[3],2*row[3],row[4]))
    print('EC49FFW_PER_KEY_EXACT_CROSSCHECK_PASS_H3_H14')
