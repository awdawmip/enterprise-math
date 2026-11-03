#!/usr/bin/env python3
"""Exact finite consistency certificate for PREFIX-477, Python stdlib only."""
from math import comb

LETTERS = 'aAbBcCdDeE'
GATES = ('aab', 'ababa', 'aAa')
MAX_N = 9

def kmp_update(w, q, c):
    t = w[:q] + c
    return max(j for j in range(len(w)+1) if t.endswith(w[:j]))

def observed(counts):
    s = counts[0]
    plusminus = [(counts[1+2*i], counts[2+2*i]) for i in range(5)]
    y = tuple(p-m for p,m in plusminus)
    p = [min(a,b) for a,b in plusminus]
    return (s,) + y + (p[1]+2*p[3]+p[4], p[2]+p[4])

def coeff(n,k):
    def b(q): return comb(q+7, 7) if q>=0 else 0
    t = [0]*(n+1)
    for d,v in ((0,1),(2,2)):
      for e,v2 in ((0,1),(1,2),(2,1)):
        for f,v3 in ((0,1),(1,1),(k+1,-1)):
          if d+e+f<=n: t[d+e+f]+=v*v2*v3
    return sum(t[d]*b(n-d-(k+1)*j) for d in range(n+1) for j in range((n-d)//(k+1)+1))

def run(w):
    k=len(w)
    upd={(q,c):kmp_update(w,q,c) for q in range(k+1) for c in LETTERS}
    states={((0,)*11,0)}
    rows=[]
    for n in range(MAX_N+1):
        byq=[set() for _ in range(k+1)]
        for counts,q in states:
            byq[q].add(observed(counts))
        base=set().union(*byq)
        B=len(base); F=sum(map(len,byq))
        assert B==coeff(n,k), (w,n,B,coeff(n,k))
        deficits=[]
        for j in range(k):
            prior=(B if j==0 else rows[n-j]['B']) if n>=j else 0
            delta=prior-len(byq[j])
            assert 0<=delta<=2*k**9,(w,n,j,delta)
            deficits.append(delta)
        full=rows[n-k]['B'] if n>=k else 0
        assert len(byq[k])==full,(w,n,'full')
        D=sum(deficits)
        assert sum(((B if j==0 else rows[n-j]['B']) if n>=j else 0) for j in range(k+1))-F==D
        assert D<=2*k**10
        row={'n':n,'B':B,'F':F,'holes':B-len(byq[0]),'D':D,'history':[len(x) for x in byq]}
        rows.append(row)
        if n in (0,1,2,3,4,7,8,9):
            print(f"word={w} n={n} B={B} F={F} h={row['holes']} D={D} history={row['history']} count_states={len(states)}")
        if n==MAX_N:break
        new=set()
        for counts,q in states:
            for i,c in enumerate(LETTERS):
                v=list(counts); v[i+1]+=1
                new.add((tuple(v),upd[q,c]))
            if n==0 or q==k:
                v=list(counts); v[0]+=1
                new.add((tuple(v),0))
        states=new
    return rows

if __name__=='__main__':
    for w in GATES:
        run(w)
    print('ALL_EXACT_CHECKS_PASS')
