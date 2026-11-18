"""Independent finite small-state verifier of the PREFIX895 collision existence cascade.
No dependencies. It uses direct full transition hashing for the oracle, and
independent pure-Python modular/bit-state search for the predicate.
"""
from math import gcd

def exact_collision(p,q1,q2):
    N=1<<p
    seen=set()
    for x in range(N):
        for y in [x]+[x^(1<<i) for i in range(p)]:
            key=(x%q1,y%q2)
            if key in seen:
                return True
            seen.add(key)
    return False

def modular_decision(p,q1,q2):
    N=1<<p;K=(N-1)//q1;g=gcd(q1,q2)
    if g==1:
        inv=pow(q1,-1,q2)
        for i in range(p):
            z=(1<<i)*inv%q2
            if z and (z<=K or (q2-z)*q1+(1<<i)<N):
                return True
    if q1//g*q2<N:
        return True
    for h in range(1,p):
        if ((1<<h)-1)%q2==0 or ((1<<h)+1)%q2==0:
            return True
    m=q2//g
    assert m>K
    inv=pow(q1//g,-1,m)
    for i in range(p):
        for j in range(p):
            for s in (-1,1):
                D=(1<<i)-s*(1<<j)
                if D%g: continue
                k=(D//g*inv)%m
                if 1<=k<=K and ((k*q1>>j)&1)==(s<0):
                    return True
    for i in range(p):
        for j in range(p):
            for s1 in (-1,1):
                for s2 in (-1,1):
                    D=s1*(1<<i)-s2*(1<<j)
                    if D%g: continue
                    k=(D//g*inv)%m
                    if not 1<=k<=K: continue
                    a=k*q1
                    for x in range(N-a):
                        if ((x>>i)&1)==(s1<0) and (((x+a)>>j)&1)==(s2<0):
                            return True
    return False

if __name__=="__main__":
    checked=0
    for p in range(2,8):
        qq=range(3,min((1<<p)-1,31)+1,2)
        for q1 in qq:
            for q2 in qq:
                brute=exact_collision(p,q1,q2)
                derived=modular_decision(p,q1,q2)
                assert brute==derived,(p,q1,q2,brute,derived)
                checked+=1
    assert checked==734
    print({"checked":checked,"p_range":[2,7],"q_range":"odd 3..min(2^p-1,31)","result":"PASS"})
