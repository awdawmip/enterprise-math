"""R183 exact diagonal reset affine representation and restricted optimality.
Run: python R183_quadratic_reset_affine_check.py
"""
from itertools import permutations, combinations
from fractions import Fraction
from collections import defaultdict
from math import factorial
import json


def states(k):
    return [()] + [p for r in range(1, k+1) for p in permutations(range(k), r)]


def star(a,b):
    block = set(b)
    return tuple(i for i in a if i not in block) + b


def features(k):
    return [(i,) for i in range(k)] + list(combinations(range(k), 2))


def action(k, state):
    """The tuple (diagonal, translation) of the k(k+1)/2-affine map."""
    fs = features(k)
    A, b = [], []
    for U in fs:
        last = next((i for i in reversed(state) if i in U), None)
        A.append(int(last is None))
        b.append((last+1) if last is not None else 0)
    return tuple(A), tuple(b)


def then(f,g):
    a,b=f
    c,d=g
    return tuple(c[i]*a[i] for i in range(len(a))), tuple(c[i]*b[i]+d[i] for i in range(len(a)))


def packet(terms):
    d=defaultdict(int)
    for w,s,n in terms:
        w=Fraction(w)
        assert w>0 and isinstance(n,int) and n>0
        d[(w,tuple(s))]+=n
    return tuple(sorted((w,s,n) for (w,s),n in d.items()))


def serial(p,q):
    return packet((w*v,star(s,t),n*m) for w,s,n in p for v,t,m in q)


def as_affine(p,k):
    d=defaultdict(int)
    for w,s,n in p:
        d[(Fraction(w),action(k,s))]+=n
    return tuple(sorted((w,a,n) for (w,a),n in d.items()))


def run():
    checks=dict(semigroup_pairs=0,faithful_state_pairs=0,coordinate_minimality_witnesses=0,
                positive_packet_pairs=0)
    stats=[]
    for k in range(1,6):
        S=states(k)
        dim=k*(k+1)//2
        expected=sum(factorial(k)//factorial(k-r) for r in range(k+1))
        assert len(S)==expected
        act={s:action(k,s) for s in S}
        assert len(set(act.values()))==expected
        for i,a in enumerate(S):
            for b in S:
                assert then(act[a],act[b])==act[star(a,b)]
                checks['semigroup_pairs']+=1
            checks['faithful_state_pairs']+=len(S)-i-1
        # Every singleton feature is forced by i+R versus R, and every pair
        # by i j R versus j i R, where R contains all other targets.
        fs=features(k)
        allsets=[frozenset(i for i in range(k) if (mask>>i)&1) for mask in range(1,1<<k)]
        for U in fs:
            R=tuple(i for i in range(k) if i not in U)
            if len(U)==1:
                i=U[0]; u=(i,)+R; v=R
            else:
                i,j=U; u=(i,j)+R; v=(j,i)+R
            assert star((),u)!=star((),v)
            distinguishing=[]
            for V in allsets:
                def scalar(word):
                    last=next((x for x in reversed(word) if x in V),None)
                    return 0 if last is None else last+1
                if scalar(u)!=scalar(v):
                    distinguishing.append(V)
            assert distinguishing==[frozenset(U)], (k,U,distinguishing)
            checks['coordinate_minimality_witnesses']+=1
        stats.append(dict(k=k,states=len(S),simplex_dim=len(S)-1,reset_dim=dim,
                          faithful=True,restricted_coordinate_reset_optimal=True))
    weights=[Fraction(1,2),Fraction(2,3),Fraction(5,4)]
    base=[(weights[i%3],(i%5,(i+1)%5,i%5),i%4+1) for i in range(40)]
    for shift in range(80):
        p=base[shift%20:shift%20+8]
        q=base[(shift+7)%20:(shift+7)%20+7]
        left=as_affine(serial(p,q),3)
        grouped=defaultdict(int)
        for w,a,n in as_affine(p,3):
            for v,b,m in as_affine(q,3):
                grouped[(w*v,then(a,b))]+=n*m
        right=tuple(sorted((w,a,n) for (w,a),n in grouped.items()))
        assert left==right
        checks['positive_packet_pairs']+=1
    return {"status":"R183_EXACT_QUADRATIC_RESET_PASS",
            "scientific_pin":"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
            "stats":stats,"checks":checks,
            "scope":"All states and ordered pairs k=1..5; exact positive rational packet reference; universal lower bound only within coordinatewise reset/identity class."}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
