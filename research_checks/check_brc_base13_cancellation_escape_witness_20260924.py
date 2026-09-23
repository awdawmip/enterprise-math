#!/usr/bin/env python3
"""Regression for the base-13 cancellation escape witness theorem.

Falsification only; proof is in the companion note.
"""
TARGET_RESIDUES=(13,19)

def is_prime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def target_primes(limit):
    return [p for p in range(2,limit+1) if is_prime(p) and p%24 in TARGET_RESIDUES]

def vp(n,p):
    n=abs(n); r=0
    while n and n%p==0:r+=1;n//=p
    return r

def vpfact(n,p):
    r=0
    while n:
        n//=p;r+=n
    return r

def pf(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=1 if d==2 else 2
    if n>1:out.append(n)
    return out

def ord4(p):
    o=p-1
    for r in pf(o):
        while o%r==0 and pow(4,o//r,p)==1:o//=r
    return o

def cancel(p,j):
    if p%24!=13:return (False,0)
    o=ord4(p);s=o//2
    C=j%s==0 and (j//s)%2==1
    return (C, vp(pow(4,s)+1,p) if C else 0)

def endpoint(p,j): return j%((p-1)//2)==0

def defect(p,m):
    out=0
    for j,mult in m.items():
        E=int(endpoint(p,j)); a=vp(j,p); C,c=cancel(p,j)
        out += mult*(E+a-(a+c if C else 0)) + vpfact(mult,p)
    return out

def positive_singleton_criterion(q,j):
    E=endpoint(q,j); a=vp(j,q); C,_=cancel(q,j)
    return E or (a>0 and not C)

def main():
    ps=[p for p in target_primes(5000) if p%24==13 and p>13]
    failures=[]; novel=[]; covered=[]
    for p in ps:
        h=(p-1)//2
        m={3:1,h:1}
        dp=defect(p,m)
        d13=defect(13,m)
        if dp!=1 or d13!=vp(h,13):
            failures.append((p,'identity',dp,d13,vp(h,13)))
            continue
        for q in target_primes(p-1):
            if q==13: continue
            if defect(q,{3:1})!=0:
                failures.append((p,'e3-neutrality',q,defect(q,{3:1})))
                break
            if (defect(q,{h:1})>0) != positive_singleton_criterion(q,h):
                failures.append((p,'singleton-criterion',q,h,defect(q,{h:1})))
                break
        if failures: break
        vals=[(q,defect(q,m)) for q in target_primes(p-1)]
        prev=max([0]+[d for _,d in vals])
        criterion=(vp(h,13)==0 and not any(q!=13 and positive_singleton_criterion(q,h)
                                           for q in target_primes(p-1)))
        actual=dp>prev
        if criterion!=actual:
            failures.append((p,'novelty',h,dp,prev,criterion,vals))
            break
        if actual:
            novel.append((p,h,p+7))
        else:
            src=[(q,d) for q,d in vals if d==prev and d>0]
            covered.append((p,h,prev,src[:6]))
    print({
        'status':'PASS' if not failures else 'FAIL',
        'class13_primes_13_lt_p_lt_5000':len(ps),
        'failures':failures[:3],
        'uniform_novel_mixed_witness_count':len(novel),
        'uniform_novel_mixed_witnesses':novel,
        'covered_count':len(covered),
        'covered_examples':covered[:10],
    })
    if failures: raise SystemExit(1)

if __name__=='__main__': main()
