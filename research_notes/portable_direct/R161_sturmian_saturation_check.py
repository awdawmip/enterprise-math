#!/usr/bin/env python3
"""R161 exact checks: exhaustive m=5..8, Farey lemma m=9..100, extremes m=5..160.
Run: python R161_sturmian_saturation_check.py
Uses only Python integers and fractions.Fraction.
"""
from fractions import Fraction as Q
import json

def signature(word):
    m=len(word)
    p=[0]
    for bit in word:
        p.append(p[-1]+int(bit))
    alpha,beta=Q(0),Q(1)
    for i in range(m):
        for j in range(i+1,m+1):
            k=j-i
            ones=p[j]-p[i]
            alpha=max(alpha,Q(ones-1,k))
            beta=min(beta,Q(ones+1,k))
    if alpha>=beta:
        return None
    A=min(Q(p[j])-j*alpha for j in range(m+1))
    B=max(Q(p[j])-j*beta for j in range(m+1))
    W=(B-A)/(beta-alpha)
    return alpha,beta,A,B,W

def count(L,s):
    alpha,beta,A,B,_=s
    lo=L*alpha-(1+A)
    hi=L*beta-B
    ceil=lambda z: -((-z.numerator)//z.denominator)
    return ceil(hi)-(lo.numerator//lo.denominator)-1

def last_missing(s):
    alpha,beta,A,B,W=s
    a,b=alpha.numerator,alpha.denominator
    c,d=beta.numerator,beta.denominator
    U=int(b*(1+A))
    V=int(d*B)
    D=b*c-a*d
    assert D>0 and Q(U,b)==1+A and Q(V,d)==B
    last=0
    for t in range(1,b+1):
        r=(a*t-U)%b
        J=(b*d+b*V-d*(U+r)-D*t)//(D*b)
        if J>=0:
            last=max(last,t+b*J)
    direct=max((L for L in range(1,int(W)+1) if count(L,s)<=0),default=0)
    assert last==direct,(last,direct)
    return last

def check_farey(m):
    fractions=sorted({Q(a,b) for b in range(1,m+1) for a in range(b+1)})
    bound=Q(2,(m-1)*(m-3))
    tiny=[(fractions[i],fractions[i+1],fractions[i+2])
          for i in range(len(fractions)-2)
          if fractions[i+2]-fractions[i]<bound]
    expected=[
       (Q(1,m),Q(1,m-1),Q(1,m-2)),
       (1-Q(1,m-2),1-Q(1,m-1),1-Q(1,m))]
    assert sorted(tiny)==sorted(expected),(m,tiny)
    return len(fractions),len(tiny)

def main():
    out={"scope":"external tied-phase finite Sturmian scalar; science pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34",
         "small_exhaustive":[],"farey_checks":{},"extremal_check":{"range_m":[5,160]}}
    for m in range(5,9):
        observed=[]
        for number in range(1<<m):
            word=format(number,f"0{m}b")
            s=signature(word)
            if s is None:
                continue
            observed.append((word,s[-1],last_missing(s)))
        E=m*(m-3)//2
        M=(m-2)*((m-1)//2)-1
        Ewords={w for w,W,L in observed if W==E}
        Mwords={w for w,W,L in observed if L==M}
        expected={"0"+"1"*(m-2)+"0","1"+"0"*(m-2)+"1"}
        assert max(W for _,W,_ in observed)==E
        assert max(L for _,_,L in observed)==M
        assert Ewords==Mwords==expected
        out["small_exhaustive"].append({
          "m":m,"binary_candidates":1<<m,"admitted":len(observed),
          "max_W":str(E),"max_last_missing_L":M,"exact_T":M+2,
          "T_maximizers":sorted(Mwords),"W_maximizers":sorted(Ewords)})
    for m in range(9,101):
        n,e=check_farey(m)
        if m in (9,10,12,16,24,32,64,100):
            out["farey_checks"][str(m)]={"farey_fraction_count":n,"sub_bound_triplets":e}
    checked=0
    for m in range(5,161):
        n=m-2
        predicted=n*((n+1)//2)-1
        for w in ("0"+"1"*n+"0","1"+"0"*n+"1"):
            s=signature(w)
            assert s is not None
            assert s[-1]==Q(m*(m-3),2)
            assert last_missing(s)==predicted
            checked+=1
    out["extremal_check"]["words_checked"]=checked
    out["extremal_check"]["formula"]="last_missing_L=(m-2)*ceil((m-2)/2)-1; W=m(m-3)/2"
    out["status"]="R161_EXACT_CHECKS_PASS"
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
