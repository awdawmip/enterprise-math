"""Independent selected exhaustive subset and exact rational rank checks for EC49FAN."""
import json
from itertools import combinations
from fractions import Fraction
import VERIFY_EC49FAN as V

def fraction_rank(sigs):
    A=[]
    for sig in sigs:
        for i in range(5):A.append([Fraction(int(v==i)) for v in sig])
    M=[list(row) for row in zip(*A)] if A else [[] for _ in range(9)]
    r=0
    for col in range(len(A)):
        p=next((i for i in range(r,9) if M[i][col]), None)
        if p is None:continue
        M[r],M[p]=M[p],M[r]
        t=M[r][col]
        M[r]=[x/t for x in M[r]]
        for i in range(r+1,9):
            if M[i][col]:
                t=M[i][col];M[i]=[x-t*y for x,y in zip(M[i],M[r])]
        r+=1
        if r==9:break
    return r

def check():
    base=V.B2+V.B3+sum((V.CASES[1512][h] for h in range(4,8)),[])
    roots=V.CASES[1512][5]
    oldsig=set(V.obs(V.steps(w)) for w in base)
    assert len(oldsig)==6
    checked_masks=0
    sigs=sorted(oldsig)
    for mask in range(64):
        subset=[s for i,s in enumerate(sigs) if mask>>i&1]
        if V.rank(subset)!=fraction_rank(subset):
            raise ValueError('rational rank mismatch')
        checked_masks+=1
    k=(5,5,1,0,0,0)
    a=[(w,V.obs(V.steps(w))) for r in roots for suf in V.suffixes(3) for w in [r+suf] if V.key(V.steps(w))==k and V.obs(V.steps(w)) in oldsig]
    b=[(w,V.obs(V.steps(w))) for r in roots for suf in V.suffixes(4) for w in [r+suf] if V.key(V.steps(w))==k and V.obs(V.steps(w)) in oldsig]
    assert len(a)==12 and len(b)==8
    bp=V.prefixes(base)
    F=bp|V.prefixes([w for w,s in a])
    brute=[]
    for words,ref in ((a,bp),(b,F)):
        wins=[]
        for mask in range(1,1<<len(words)):
            A=[w for i,(w,s) in enumerate(words) if mask>>i&1]
            if V.rank([s for i,(w,s) in enumerate(words) if mask>>i&1])==9:
                wins.append(len(V.prefixes(A)-ref))
        brute.append((min(wins),len(wins)))
    dp8=V.min_rank_cost(a,bp,oldsig)
    dp9=V.min_rank_cost(b,F,oldsig)
    assert dp8==brute[0][0]==16 and dp9==brute[1][0]==6
    # Reproduce parent FAL H6 rooted 3 common-key lower bounds for first schedule.
    h6=V.CASES[1512][6]
    z2=V.suffixes(2);z3=V.suffixes(3)
    parent=[]
    for k in ((5,5,1,0,0,0),(6,4,1,0,0,0),(6,5,1,0,0,0)):
        A=[(w,V.obs(V.steps(w))) for r in h6 for suf in z2 for w in [r+suf] if V.key(V.steps(w))==k and V.obs(V.steps(w)) in oldsig]
        B=[(w,V.obs(V.steps(w))) for r in h6 for suf in z3 for w in [r+suf] if V.key(V.steps(w))==k and V.obs(V.steps(w)) in oldsig]
        d8=V.min_rank_cost(A,bp,oldsig)
        d9=V.min_rank_cost(B,bp|V.prefixes([w for w,s in A]),oldsig)
        parent.append((list(k)[:3],len(A),len(B),d8,d9,72+d8+d9))
    assert [e[3] for e in parent]==[16,20,30]
    return {'rational_vs_modular_masks':checked_masks,'brute_force_H8':brute[0],'brute_force_H9':brute[1], 'dp_results':[dp8,dp9], 'parent_H6_classes':parent,'result':'PASS'}

if __name__=='__main__':print(json.dumps(check(),indent=2))
