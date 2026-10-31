"""EC49CS formal BRC suffix-observer theorem audit; exact Q arithmetic.
Requires Python 3 stdlib only. This script checks the finite class identities
used in the all-h induction and the resulting recurrence up to horizon 12.
It is an independently runnable author-side checker, not formal project admission.
"""
from fractions import Fraction as Q
from collections import defaultdict

S = {'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),
     'd':(2,1,-2,-1),'e':(3,1,1,-3)}
DELTA={'a':(-2,0),'b':(0,-2),'c':(0,0),'d':(0,0),'e':(2,0)}

def dfa(q, letter):
    qa,qb=divmod(q,3)
    def nxt(state,first,second):
        return 2 if state==2 or (state==1 and letter==second) else int(letter==first)
    return 3*nxt(qa,1,2)+nxt(qb,2,1)

def follow(q,word):
    for letter in word:q=dfa(q,letter)
    return q

def label(q):return 2*(q//3==2)+(q%3==2)
F={op:tuple(follow(q,suf) for q in range(9)) for op,suf in S.items()}

def span(rows):
    basis={}
    for raw in rows:
        v=list(map(Q,raw))
        for k in sorted(basis):
            if v[k]:
                factor=v[k]
                v=[x-factor*y for x,y in zip(v,basis[k])]
        pivot=next((i for i,x in enumerate(v) if x),None)
        if pivot is None:continue
        factor=v[pivot]
        v=[x/factor for x in v]
        for k in basis:
            if basis[k][pivot]:
                factor=basis[k][pivot]
                basis[k]=[x-factor*y for x,y in zip(basis[k],v)]
        basis[pivot]=v
    return tuple(tuple(basis[k]) for k in sorted(basis))

def add(*spaces):return span(row for rows in spaces for row in rows)
def image(op,rows):return span(tuple(row[F[op][q]] for q in range(9)) for row in rows)

U4=span(tuple(int(label(q)==t) for q in range(9)) for t in range(4))
U3=add(image('c',U4),image('d',U4))
K3=image('a',U3)
U5=add(U3,K3)
U6=add(U3,U4)
classes={'U3':U3,'U4':U4,'U5':U5,'U6':U6}
assert {k:len(v) for k,v in classes.items()}=={'U3':3,'U4':4,'U5':5,'U6':6}
assert len(K3)==3 and add(U4,U5)==U6
for name,rows in classes.items():
    assert add(image('c',rows),image('d',rows))==U3,(name,'cd')
    for op in 'abe':
        assert image(op,rows)==(U4 if name in ('U4','U6') else K3),(name,op)
print('PASS finite Q class algebra (all 5 literal native operations)')

prev={(0,0):U4};cum={}
for h in range(1,13):
    curr=defaultdict(list)
    for (u,v),rows in prev.items():
        for op,(dx,dy) in DELTA.items():
            # The full signed prefix target is minus the suffix displacement.
            curr[(u-dx//2,v-dy//2)].extend(image(op,rows))
    curr={xy:span(rows) for xy,rows in curr.items()}
    for xy,rows in curr.items():cum[xy]=add(cum.get(xy,()),rows)
    er=sum(len(rows) for rows in curr.values())
    cr=sum(len(rows) for rows in cum.values())
    want_e=15 if h==1 else (11*h*h+15*h+8)//2
    want_c=15 if h==1 else 6*h*h+8*h+4
    assert (er,cr)==(want_e,want_c),(h,er,cr,want_e,want_c)
    if h==3:assert (er*3,cr*3)==(228,246)
    print('h=',h,'exact-three-channel=',er*3,'cumulative-three-channel=',cr*3)
    prev=curr
print('PASS all h=1..12 exact-Q recurrence; universal claim follows finite identities + induction')
