#!/usr/bin/env python3
"""PREFIX-514. Exact signed-native path and closed W-prefix checks, Python 3."""
import json
from collections import defaultdict
from itertools import combinations_with_replacement

COLORS = (0, 4, 1, 2, 3, 3, 4, 4, 4, 4)  # a,A,b,B,c,C,d,D,e,E
GATES = {'aab': (0, 0, 1), 'aba': (0, 1, 0)}
# (q,first_source,required_pair_a,required_pair_b). Extra c step guarantees C source.
THRESHOLDS = {
    'aab': ((0,'B',0,1),(1,'B',1,1),(2,'B',2,1),(3,'B',2,1),
            (0,'C',0,0),(1,'C',1,0),(2,'C',2,0),(3,'C',2,1)),
    'aba': ((0,'B',0,1),(1,'B',1,1),(2,'B',1,1),(3,'B',2,1),
            (0,'C',0,0),(1,'C',1,0),(2,'C',1,1),(3,'C',2,1))
}

def prefix(m, A, B, j):
    J = max(0, min(j, m-A-B+1))
    return J*(2*m-2*A-2*B+1)-J*(J-1)//2

def predicted_row(m, gate, W):
    return {(V,q,t) for q,t,A,B in THRESHOLDS[gate]
            if 0 <= W <= m-A-B
            for V in range(B, 2*m-2*A-B-W+1)}

def predicted_prefix(m, gate, j):
    return sum(prefix(m,A,B,j) for _,_,A,B in THRESHOLDS[gate])

def phi(h):
    return (h+1)*(3*h+2)//2 if h >= 0 else 0

def predicted_total(m,gate):
    return (phi(m)+2*phi(m-1)+2*phi(m-2)+3*phi(m-3) if gate=='aab'
            else phi(m)+2*phi(m-1)+3*phi(m-2)+2*phi(m-3))

def native(n,gate,c_sign):
    pattern=GATES[gate]
    def step(q,c):
        word=pattern[:q]+(c,)
        return next((r for r in (3,2,1) if len(word)>=r and word[-r:]==pattern[:r]),0)
    goal=(0,0,c_sign,0,0)
    states={((0,0,0,0,0),0,0,0,0)}
    for k in range(n):
        nxt=set(); remaining=n-k-1
        for y,V,W,q,t in states:
            for axis in range(5):
                for sign in (1,-1):
                    z=list(y); old=z[axis];z[axis]+=sign
                    dist=sum(abs(z[i]-goal[i]) for i in range(5))
                    if dist>remaining or (remaining-dist)%2: continue
                    cancelling=(old*sign<0)
                    v=V+cancelling*{1:1,3:2,4:1}.get(axis,0)
                    w=W+cancelling*(axis in (2,4))
                    source=t or (1 if axis==1 else 2 if axis==2 else 0)
                    c=COLORS[2*axis+(sign<0)]
                    nxt.add((tuple(z),v,w,step(q,c),source))
        states=nxt
    rows=defaultdict(set)
    for y,V,W,q,t in states:
        assert y==goal and t in (1,2)
        rows[W].add((V,q,'B' if t==1 else 'C'))
    return rows

def compositions(m):
    for a in range(m+1):
      for b in range(m-a+1):
       for c in range(m-a-b+1):
        for d in range(m-a-b-c+1):
         e=m-a-b-c-d
         yield a,b,c,d,e

def run():
    out={'status':'ALL_CHECKS_PASS','scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
         'family':'native restricted X6: n=2m+1, y=(0,0,+/-1,0,0)',
         'native_lengths':[1,3,5,7,9,11,13],
         'native_rows_checked':0,'native_joint_state_memberships':0,
         'native_prefix_equalities':0,'native_sign_reflection_equalities':0,
         'occupancy_composition_checks':0,'long_range_formula_checks':0,'results':{}}
    for gate in GATES:
        totals=[]
        for n in out['native_lengths']:
            m=(n-1)//2
            plus=native(n,gate,+1)
            minus=native(n,gate,-1)
            assert plus==minus,(gate,n,'sign-reflection')
            out['native_sign_reflection_equalities']+=1
            for cs,rows in ((1,plus),(-1,minus)):
                assert set(rows)==set(range(m+1)),(gate,n,cs,'W-range')
                for W in range(m+1):
                    assert rows[W]==predicted_row(m,gate,W),(gate,n,cs,W,rows[W]^predicted_row(m,gate,W))
                    out['native_rows_checked']+=1
                    out['native_joint_state_memberships']+=len(rows[W])
                for j in range(-2,m+4):
                    actual=sum(len(row) for W,row in rows.items() if W<j)
                    assert actual==predicted_prefix(m,gate,j),(gate,n,cs,j)
                    out['native_prefix_equalities']+=1
                assert sum(map(len,rows.values()))==predicted_total(m,gate)
            totals.append({'n':n,'each_c_sign':sum(map(len,plus.values()))})
        out['results'][gate]=totals
        # Independent five-occupation enumeration: explicitly check each
        # Cartesian (W,V) fiber with thresholds, without applying prefix formula.
        for m in range(0,13):
            ps=list(compositions(m))
            for q,t,A,B in THRESHOLDS[gate]:
                actual={(c+e,b+2*d+e) for a,b,c,d,e in ps if a>=A and b>=B}
                expected={(W,V) for W in range(m+1) for V,qq,tt in predicted_row(m,gate,W)
                          if qq==q and tt==t}
                assert actual==expected,(gate,m,q,t,A,B)
                out['occupancy_composition_checks']+=1
        for m in range(0,101):
            running=0
            for j in range(-2,m+4):
                direct=sum(len(predicted_row(m,gate,W)) for W in range(max(0,min(j,m+1))))
                assert direct==predicted_prefix(m,gate,j),(gate,m,j)
                out['long_range_formula_checks']+=1
            assert predicted_total(m,gate)==predicted_prefix(m,gate,m+3)
    return out

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
