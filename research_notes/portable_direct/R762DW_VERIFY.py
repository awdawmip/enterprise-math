#!/usr/bin/env python3
"""R762DW: exact ternary subgroup-layer checks; Python standard library only."""
import json
from collections import Counter

SHIFTS=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))

def index(q,i,j,k): return (i*q+j)*q+k

def transition_map(q):
    out=[]
    for i in range(q):
        for j in range(q):
            for k in range(q):
                out.append(tuple(index(q,(i+a)%q,(j+b)%q,(k+c)%q) for a,b,c in SHIFTS))
    return out

def powers(q,end,mod):
    tr=transition_map(q)
    a=[0]*(q**3)
    a[0]=1
    out={0:a}
    for n in range(1,end+1):
        b=[0]*len(a)
        for i, v in enumerate(a):
            if v:
                for j in tr[i]: b[j]+=v
        a=[x%mod for x in b]
        out[n]=a
    return out

def mul9(a,b):
    out=[0]*729
    aa=[(divmod(i//9,9)[0],(i//9)%9,i%9,x) for i,x in enumerate(a) if x]
    bb=[(divmod(i//9,9)[0],(i//9)%9,i%9,x) for i,x in enumerate(b) if x]
    for i,j,k,x in aa:
        for di,dj,dk,y in bb:
            out[index(9,(i+di)%9,(j+dj)%9,(k+dk)%9)] += x*y
    return out

def kernel():
    p3=powers(9,3,100000000)[3]
    A=[0]*729
    for i,j,k in SHIFTS: A[index(9,3*i,3*j,3*k)] += 1
    A2=mul9(A,A)
    A3=mul9(A2,A)
    assert all(x%3==0 for x in A3)
    extra=mul9(A2,[p3[i]-A[i] for i in range(729)])
    K=[(A3[i]//3+extra[i])%9 for i in range(729)]
    direct=powers(9,9,27)[9]
    assert all(x%3==0 for x in direct)
    assert K==[(x//3)%9 for x in direct]
    return K

def run():
    K=kernel()
    hist=dict(sorted(Counter(K).items()))
    assert hist=={0:198,2:21,3:276,5:6,6:228},hist
    strata=[]
    checked=0
    for q in (9,27):
        b=q//9
        ps=powers(q,q+b-1,27)
        small=powers(b,b-1,9)
        for r in range(b):
            arr=ps[q+r]
            low=small[r]
            n1=n2=0
            for i in range(q):
                for j in range(q):
                    for k in range(q):
                        pos=index(q,i,j,k)
                        h=index(9,i//b,j//b,k//b)
                        e=index(b,i%b,j%b,k%b)
                        val=low[e]
                        expected=(K[h]*val)%9
                        z=arr[pos]
                        assert z%3==0
                        assert z//3==expected, (q,r,i,j,k,z,expected)
                        n1+=(z%9!=0)
                        n2+=(z%9==0 and z%27!=0)
                        checked+=1
            s=sum(v%3!=0 for v in low)
            t=sum(v%3==0 and v%9!=0 for v in low)
            assert n1==27*s and n2==504*s+27*t,(q,r,n1,n2,s,t)
            strata.append(dict(q=q,r=r,nonzero_mod3_small=s,valuation_one_small=t,
                               val1=n1,val2=n2,at_least3=q**3-n1-n2))
    evidence={"theorem_id":"R762DW","representation":"positive six-branch full-three-coordinate endpoint BRC", "modulus":"q=3^a, a>=2", "verified_q":[9,27],
              "kernel_histogram_mod9":hist,"H3_kernel_counts":{"2":21,"5":6},"off_H3_kernel_counts":{"0":198,"3":276,"6":228},
              "exact_coefficient_checks":checked,"strata":strata,
              "method":"full cyclic six-shift mod-27 recurrence versus independent polynomial group-ring kernel formula; integer only", "author_result":"PASS", "independent_review":"NOT_REVIEWED", "open":"higher quotient layers and actual native TRIADIC_CLOSURE_E signed event licensing"}
    print(json.dumps(evidence,sort_keys=True,ensure_ascii=False,indent=2))
    return evidence
if __name__=='__main__': run()
