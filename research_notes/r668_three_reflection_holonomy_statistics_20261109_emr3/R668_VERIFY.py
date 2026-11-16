#!/usr/bin/env python3
"""R668 exact counts of V17 three-reflection holonomy, integer-only."""
import itertools
import json
from math import factorial, comb
from pathlib import Path

A=(0,2,1); B=(2,1,0); C=(1,0,2)
GEN=(A,B,C); E=(0,1,2); R=(2,0,1)

def mul(p,q):
    return tuple(p[q[i]] for i in range(3))

def parity_bins(n):
    N=sum(n); o=(N+1)//2; e=N//2
    totals=n[1]+2*n[2]
    out=[0,0,0]
    for ka in range(n[0]+1):
        for kb in range(n[1]+1):
            kc=o-ka-kb
            if not 0<=kc<=n[2]: continue
            k=(ka,kb,kc)
            d=(2*(kb+2*kc)-totals)%3
            den=1
            for i in range(3):
                den*=factorial(k[i])*factorial(n[i]-k[i])
            num=factorial(o)*factorial(e)
            assert num%den==0
            out[d]+=num//den
    return tuple(out)

def group_dp(n):
    states={(0,0,0,E):1}
    for _ in range(sum(n)):
        nxt={}
        for (a,b,c,g),ways in states.items():
            used=(a,b,c)
            for j in range(3):
                if used[j]<n[j]:
                    k=list(used);k[j]+=1
                    z=(*k,mul(g,GEN[j]))
                    nxt[z]=nxt.get(z,0)+ways
        states=nxt
    R2=mul(R,R)
    finals=[E,R,R2]
    if sum(n)%2: finals=[mul(g,A) for g in finals]
    out=[0,0,0]
    for (_,_,_,g),ways in states.items():
        out[finals.index(g)]+=ways
    return tuple(out)

def all_words(n):
    N=sum(n);R2=mul(R,R)
    finals=[E,R,R2] if N%2==0 else [mul(g,A) for g in (E,R,R2)]
    out=[0,0,0]
    for w in itertools.product(range(3),repeat=N):
        if tuple(w.count(j) for j in range(3))!=n: continue
        g=E
        for j in w: g=mul(g,GEN[j])
        out[finals.index(g)]+=1
    return tuple(out)

def balanced(m):
    T=factorial(3*m)//factorial(m)**3
    if m%2:
        assert T%3==0
        return (T//3,)*3
    half=3*m//2
    C0=comb(3*m,half);D=comb(m,m//2)
    Q=factorial(half)**2;den=3*factorial(m)**3
    assert Q*(C0+2*D)%den==0 and Q*(C0-D)%den==0
    return (Q*(C0+2*D)//den,Q*(C0-D)//den,Q*(C0-D)//den)

def main():
    assert mul(R,A)==B and mul(mul(R,R),A)==C
    count=0
    for n in itertools.product(range(7),repeat=3):
        a=parity_bins(n);b=group_dp(n)
        assert a==b,(n,a,b)
        assert sum(a)==factorial(sum(n))//(factorial(n[0])*factorial(n[1])*factorial(n[2]))
        count+=1
    brute_count=0
    for N in range(10):
        for a in range(N+1):
            for b in range(N-a+1):
                n=(a,b,N-a-b)
                assert all_words(n)==parity_bins(n),n
                brute_count+=1
    examples={}
    for m in range(1,9):
        assert balanced(m)==parity_bins((m,m,m)),m
        z=balanced(m)
        examples[str(m)]={"total":sum(z),"residues":list(z)}
    ev={
      "marker":"R668_ALTERNATING_PARITY_BIN_HOLONOMY_STATISTICS_EXACT_PASS",
      "frozen_science":"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",
      "source":"R667@06c496b74ae5027967f52b8f0119274e4be084b2",
      "group_dp_vectors":count,"brute_vectors":brute_count,
      "brute_total_free_words":sum(3**j for j in range(10)),
      "balanced_m_1_to_8":examples,
      "model":"V17 base-012 reflection loops A,B,C; arbitrary fixed-multiplicity block order",
      "review":"AUTHOR_SIDE_UNREVIEWED"
    }
    Path(__file__).with_name("R668_EVIDENCE.json").write_text(json.dumps(ev,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(ev["marker"],"dp=",count,"brute_vectors=",brute_count,"word_space=",ev["brute_total_free_words"])

if __name__=="__main__":
    main()
