from fractions import Fraction as F
from itertools import product
from math import gcd
import json

def prefixes(w):
    s=[0]
    for b in w: s.append(s[-1]+b)
    return s

def support(s):
    m=len(s)-1
    alpha,beta=F(0),F(1)
    for i in range(m):
        for j in range(i+1,m+1):
            h=j-i; d=s[j]-s[i]
            alpha=max(alpha,F(d-1,h))
            beta=min(beta,F(d+1,h))
    return alpha,beta

def pair_bounds(s,L):
    m=len(s)-1
    lo,hi=0,L-1
    for i in range(m):
        for j in range(i+1,m+1):
            h=j-i; d=s[j]-s[i]
            B=L*(d-1)+i*s[j]-j*(s[i]+1)
            A=L*(d+1)+i*(s[j]+1)-j*s[i]
            lo=max(lo,B//h+1)
            hi=min(hi,-(-A//h)-1)
    return lo,hi

def totients(n):
    p=list(range(n+1))
    for i in range(2,n+1):
        if p[i]==i:
            for j in range(i,n+1,i):p[j]-=p[j]//i
    return p

def event_fractions(L,m):
    pts=set()
    for d in range(L,L+m+1):
        for p in range(1,d):
            pts.add(F(p,d))
    return sorted(pts)

def pair_at(theta,L,m):
    floors=[(L+i)*theta.numerator//theta.denominator for i in range(m+1)]
    return (floors[0], tuple(floors[i+1]-floors[i] for i in range(m)))

def finite_sweep():
    stats=[]; total_memberships=0; event_checks=0; width_words=0
    width_candidates=[]
    for m in range(1,11):
        words=[]
        for w in product((0,1), repeat=m):
            s=prefixes(w); a,b=support(s)
            if a<b: words.append((w,s,a,b))
        Wsum=sum((b-a for w,s,a,b in words),F(0))
        assert Wsum==m+1,(m,Wsum)
        width_words+=len(words)
        fs=0
        for q in range(1,m+1):
            phi=totients(q)[q]
            fs+=(m+1-q)*phi
        assert len(words)==fs+1,(m,len(words),fs+1)
        for K in range(2, min(28, 2*m+15)):
            L=K-1; phi=totients(L+m)
            J=sum(phi[q] for q in range(2,L+m+1) if (L+m)//q-(L-1)//q>=1)
            C={}
            for w,s,a,b in words:
                low,high=pair_bounds(s,L)
                c=max(0,high-low+1)
                C[w]=c
                total_memberships+=1
            assert sum(C.values())==J+1,(m,K,sum(C.values()),J+1)
            assert (m+1)*L <= sum(C.values()) <= (m+1)*L+m*(m-1)//2
            if m<=7 and K<=15:
                pts=[F(0)]+event_fractions(L,m)+[F(1)]
                direct={}
                for x,y in zip(pts,pts[1:]):
                    n,w=pair_at((x+y)/2,L,m)
                    direct[w]=direct.get(w,0)+1
                assert direct=={w:c for w,c in C.items() if c},(m,K)
                event_checks+=1
        if m>=5:
            E=(m-2)*((m-1)//2)+1
            L=E-1
            ext=(1,)+(0,)*(m-2)+(1,)
            ext2=tuple(1-i for i in ext)
            width_min=None;bad=[]
            for w,s,a,b in words:
                ua=min(F(s[j]+1)-j*a for j in range(m+1))
                lb=max(F(s[j])-j*b for j in range(m+1))
                width=L*(b-a)+ua-lb
                if w not in (ext,ext2):
                    if width_min is None or width<width_min:width_min=width
                    if width<=1:bad.append((''.join(map(str,w)),str(width)))
            width_candidates.append({'m':m,'min_other_width':str(width_min),'nonextremal_width_le_1':bad[:12], 'number':len(bad)})
        stats.append({'m':m,'words':len(words),'slope_width_sum':str(Wsum),'K_check_count':max(0,min(28,2*m+15)-2)})
    return {'marker':'R145_EXACT_FIBER_MASS_PASS','stats':stats,'word_width_cases':width_words,'C_memberships':total_memberships,'independent_event_checks':event_checks,'width_candidates':width_candidates}

if __name__=='__main__':
    out=finite_sweep()
    with open('verification_r145.json','w') as f:json.dump(out,f,indent=2)
    print(json.dumps(out,ensure_ascii=False))
