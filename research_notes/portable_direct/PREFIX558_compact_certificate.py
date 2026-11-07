"""PREFIX-558 compact certificate; needs published PREFIX550_shared_gauge_compact_certificate.py.
Frozen X6-BRC pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import Counter,deque
import json
import PREFIX550_shared_gauge_compact_certificate as X
ROOTS=(X.ZERO_ROOT,)+X.ROOTS
PRIME=1000000007
Q=(2,3,5,7,11,13)

def edges(root):
    no=[[] for _ in range(96)];g=[[] for _ in range(96)]
    for i in range(96):
        for a in X.A:
            j,m=X.edge(i,a,root)
            (g if m[6] else no)[i].append((j,m[:6]))
    return no,g

def wait_times(no):
    rev=[[] for _ in range(96)]
    for i,row in enumerate(no):
        for j,m in row: rev[j].append(i)
    d={i:0 for i in (7,29,31)}
    q=deque(d)
    while q:
        j=q.popleft()
        for i in rev[j]:
            if i not in d: d[i]=d[j]+1;q.append(i)
    assert len(d)==96
    return [d[i]+1 for i in range(96)]

def step_poly(no,v):
    z=[Counter() for _ in range(96)]
    for i,row in enumerate(no):
        for j,w in row:
            for m,n in v[j].items():
                z[i][tuple(a+b for a,b in zip(m,w))]+=n
    return z

def kappa(root,limit=5):
    no,g=edges(root)
    v=[Counter({m:1 for j,m in row}) for row in g];out=[]
    for s in range(limit+1):
        out.append(dict(v[9]))
        if s<limit:v=step_poly(no,v)
    return out

def finite_field_check(wait,beta):
    tests=0
    evalq=lambda m: __import__('math').prod(pow(q,e,PRIME) for q,e in zip(Q,m))%PRIME
    for root in ROOTS:
        no,g=edges(root)
        W=[[(j,evalq(m)) for j,m in row] for row in no]
        u=[sum(evalq(m) for j,m in row)%PRIME for row in g]
        step=lambda v:[sum(w*v[j] for j,w in row)%PRIME for row in W]
        F=[[[1]*96]+[[0]*96 for _ in range(3)]]
        for d in range(1,14):
            old=F[-1];nxt=[]
            for k in range(4):
                a=step(old[k]);nxt.append([(a[i]+(u[i]*old[k-1][9] if k else 0))%PRIME for i in range(96)])
            F.append(nxt)
        v=u[:];first={}
        for d in range(1,6):
            first[d]=v[:];v=step(v)
        b=sum(n*evalq(m) for m,n in beta.items())%PRIME
        for i,delta in enumerate(wait):
            for k in (1,2,3):
                t=delta+4*(k-1)
                assert F[t][k][i]==first[delta][i]*pow(b,k-1,PRIME)%PRIME
                assert all(F[d][k][i]==0 for d in range(t))
                tests+=t+1
    return tests

def main():
    no,g=edges(X.ZERO_ROOT)
    assert sum(map(len,no))==573 and sum(map(len,g))==3
    assert [(i,j) for i,row in enumerate(g) for j,m in row]==[(7,9),(29,9),(31,9)]
    wait=wait_times(no)
    assert Counter(wait)==Counter({1:3,2:18,3:36,4:30,5:9}) and wait[9]==4
    K=kappa(X.ZERO_ROOT)
    assert all(K==kappa(r) for r in X.ROOTS)
    assert not any(K[s] for s in (0,1,2,4))
    beta={(1,0,1,1,0,1):4,(1,0,1,1,1,0):4,
          (1,1,1,0,0,1):4,(1,1,1,0,1,0):4,(1,1,1,1,0,0):4}
    assert K[3]==beta
    count=finite_field_check(wait,beta)
    return {'status':'ALL_CHECKS_PASS','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'roots_checked':len(ROOTS),'kappa_s_checked_inclusive':5,
        'port_first_gate_wait_distribution':dict(Counter(wait)),
        'first_four_step_return_words':sum(beta.values()),
        'first_return_monomials':len(beta),'finite_field_checks':count,
        'prime':PRIME,'q_values':list(Q)}

if __name__=='__main__':print(json.dumps(main(),sort_keys=True,ensure_ascii=False))
