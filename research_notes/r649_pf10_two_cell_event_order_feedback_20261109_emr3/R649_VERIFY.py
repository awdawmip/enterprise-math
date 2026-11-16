#!/usr/bin/env python3
"""R649 exact V29/V27/V17 two-cell eventwise coupling. Python stdlib only."""
import json
from itertools import combinations, product
P=range(4)
B=((0,1),(2,0),(2,3),(3,0))
TRIADS=tuple(combinations(range(6),3))
MATCHINGS=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
NEI={s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
def code(m,s):
    z=set(s)
    if any((a in z)+(b in z)!=1 for a,b in m):return 0
    return 1 if sum(b in z for a,b in m)%2==0 else -1
C={s:tuple(code(m,s) for m in MATCHINGS) for s in TRIADS}
assert len(C)==20 and len(set(C.values()))==20
def fresh(cx,cy):
    def cell(cnt):
        M=[[0]*4 for _ in P]
        for (a,b),n in zip(B,cnt):M[a][b]=n
        return dict(M=M,rin=[0]*4,rout=[0]*4)
    return {'x':cell(cx),'y':cell(cy),'Nxy':[[0]*4 for _ in P]}
def derived(s):
    M=s['M'];ri=s['rin'];ro=s['rout']
    O=[[M[i][j]-M[j][i] for j in P] for i in P]
    u=[sum(M[i])-sum(M[j][i] for j in P)+ri[i]-ro[i] for i in P]
    assert u==[sum(O[i])+ri[i]-ro[i] for i in P]
    return u,O
def score(s,t,u,O):
    return sum(u[i]*C[t][i] for i in P)+sum(C[s][i]*O[i][j]*C[t][j] for i in P for j in P)
def step(s,slots,u,O):
    ranking=sorted(((score(s,t,u,O),t) for t in NEI[s]),reverse=True)
    gap=ranking[0][0]-ranking[1][0]
    if gap<=0:return None
    t=ranking[0][1];same=set(s)&set(t)
    leaving=next(iter(set(s)-same));enter=next(iter(set(t)-same))
    return t,{**{v:slots[v] for v in same},enter:slots[leaving]},gap
def transfer(L,a,b):
    L['x']['rout'][a]+=1;L['y']['rin'][b]+=1;L['Nxy'][a][b]+=1
    assert sum(derived(L['x'])[0])+sum(derived(L['y'])[0])==0
def recover(L):
    N=L['Nxy'];r=L['x']['rout'];c=L['y']['rin']
    R=[[0]*4 for _ in P]
    for i in range(3):
        for j in range(3):R[i][j]=N[i][j]
    for i in range(3):R[i][3]=r[i]-sum(R[i][:3])
    for j in range(3):R[3][j]=c[j]-sum(R[i][j] for i in range(3))
    R[3][3]=r[3]-sum(R[3][:3])
    assert R==N and all(x>=0 for row in N for x in row)
def run(cx,cy,events):
    L=fresh(cx,cy)
    active={c:((0,1,2),{i:i for i in range(3)}) for c in ('x','y')}
    trace=[]
    for a,b in events:
        transfer(L,a,b);line={'event':[a,b]}
        for c in ('x','y'):
            s,slots=active[c]
            u,O=derived(L[c]);got=step(s,slots,u,O)
            if got is None:return None
            t,slots_new,gap=got
            active[c]=(t,slots_new)
            line[c]={'from':list(s),'to':list(t),'gap':gap,'u':u,'slots':[slots_new[k] for k in t]}
        recover(L);trace.append(line)
    return L,{c:{'triad':list(s),'slots':[slots[k] for k in s]} for c,(s,slots) in active.items()},trace
cx=(0,0,0,1);cy=(3,3,3,3);e=(0,0);f=(1,1)
A=run(cx,cy,(e,f));B_=run(cx,cy,(f,e))
assert A is not None and B_ is not None
assert A[0]==B_[0] and A[1]['x']!=B_[1]['x'] and A[1]['y']==B_[1]['y']
assert A[1]['x']=={'triad':[0,1,2],'slots':[0,1,2]}
assert B_[1]['x']=={'triad':[1,3,5],'slots':[1,0,2]}
assert A[1]['y']=={'triad':[1,2,4],'slots':[0,2,1]}
assert A[0]['Nxy']==[[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]]
assert [l['x']['gap'] for l in A[2]]==[1,1]
assert [l['x']['gap'] for l in B_[2]]==[1,1]
assert [l['y']['gap'] for l in A[2]]==[3,1]
assert [l['y']['gap'] for l in B_[2]]==[2,1]
all_cases=strict_cases=different=0
for cnt in product(range(4),repeat=4):
    for a,b in combinations(P,2):
        all_cases+=1
        p=run(cnt,cy,((a,0),(b,1)))
        q=run(cnt,cy,((b,1),(a,0)))
        if p is None or q is None:continue
        strict_cases+=1
        assert p[0]==q[0]
        if p[1]!=q[1]:different+=1
assert (all_cases,strict_cases,different)==(1536,416,30)
print(json.dumps({
 'marker':'R649_TWO_CELL_ORDER_FEEDBACK_COLLISION_PASS',
 'source_pin':'V29/V26/V27/V17@b62110008321d9147212cb89f2627ff613c2550d',
 'science_pin':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'witness':{'A_ef':{'endpoint':A[1],'steps':A[2]},'B_fe':{'endpoint':B_[1],'steps':B_[2]},
            'equal_full_V29_and_N':A[0]==B_[0]},
 'finite_search':{'cases':all_cases,'both_strict':strict_cases,'different_endpoints':different},
 'new_model':'TRANSFER -> V27 strict neighbor -> V17 slot transport, on both Cells',
 'author_side':True,'driver_reviewed':False},ensure_ascii=False,indent=2))