"""PREFIX-513: native signed-step exact DP versus negative-b W-prefix formula."""
import json
from collections import defaultdict

COLORS = (0,4,1,2,3,3,4,4,4,4)  # a,A,b,B,c,C,d,D,e,E
GATES = {'aab': (0,0,1), 'aba': (0,1,0)}
RULES = {
 'aab': ((0,'B',0,0,0),(1,'B',1,0,0),(2,'B',2,0,0),(3,'B',2,1,0),
         (0,'C',0,0,1),(1,'C',1,0,1),(2,'C',2,0,1),(3,'C',2,1,1)),
 'aba': ((0,'B',0,0,0),(1,'B',1,0,0),(2,'B',1,1,0),(3,'B',2,1,0),
         (0,'C',0,0,1),(1,'C',1,0,1),(2,'C',1,1,1),(3,'C',2,1,1)),
}

def pref(m,A,beta,C,j):
    J=max(0,min(j,m-A-beta+1)-C)
    return J*(2*m-2*A-2*beta-C+1)-J*(2*C+J-1)//2

def fiber_row(m,gate,W):
    return {(V,q,t) for q,t,A,beta,C in RULES[gate]
            if C<=W<=m-A-beta
            for V in range(beta,2*m-2*A-beta-C-W+1)}

def native(n,gate):
    pattern=GATES[gate]
    def step(q,c):
        word=pattern[:q]+(c,)
        return next((r for r in (3,2,1) if len(word)>=r and word[-r:]==pattern[:r]),0)
    goal=(0,-1,0,0,0)
    states={((0,0,0,0,0),0,0,0,0)}
    for k in range(n):
        nxt=set(); rem=n-k-1
        for y,V,W,q,t in states:
            for axis in range(5):
                for sign in (1,-1):
                    z=list(y); old=z[axis];z[axis]+=sign
                    d=sum(abs(z[i]-goal[i]) for i in range(5))
                    if d>rem or (rem-d)%2: continue
                    cancel=(old*sign<0)
                    v=V+cancel*{1:1,3:2,4:1}.get(axis,0)
                    w=W+cancel*(axis in (2,4))
                    source=t or (1 if axis==1 else 2 if axis==2 else 0)
                    c=COLORS[2*axis+(sign<0)]
                    nxt.add((tuple(z),v,w,step(q,c),source))
        states=nxt
    rows=defaultdict(set)
    for y,V,W,q,t in states:
        assert y==goal
        rows[W].add((V,q,'B' if t==1 else 'C' if t==2 else 'N'))
    return rows

def run():
    out={'status':'ALL_CHECKS_PASS','frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
         'family':'n=2m+1, y=(0,-1,0,0,0)','rows_checked':0,'states_checked':0,
         'prefix_checks':0,'algebra_checks':0,'results':{}}
    for gate in GATES:
        totals=[]
        for n in (1,3,5,7,9):
            m=(n-1)//2;rows=native(n,gate)
            for W in range(m+1):
                assert rows[W]==fiber_row(m,gate,W),(gate,n,W)
                out['rows_checked']+=1;out['states_checked']+=len(rows[W])
            for j in range(-1,m+4):
                actual=sum(len(r) for W,r in rows.items() if W<j)
                formula=sum(pref(m,A,b,C,j) for q,t,A,b,C in RULES[gate])
                assert actual==formula,(gate,n,j)
                out['prefix_checks']+=1
            totals.append((n,sum(map(len,rows.values()))))
        for m in range(61):
            running=[0]
            for W in range(m+1):running.append(running[-1]+len(fiber_row(m,gate,W)))
            for j in range(-1,m+4):
                got=running[max(0,min(j,m+1))]
                want=sum(pref(m,A,b,C,j) for q,t,A,b,C in RULES[gate])
                assert got==want,(gate,m,j)
                out['algebra_checks']+=1
        out['results'][gate]=totals
    return out

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
