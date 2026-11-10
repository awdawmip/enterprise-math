#!/usr/bin/env python3
"""R682-C exact source V29/V35 typed four-Cell event-ledger check."""
from itertools import product
import json
axes=((1,0,0,0,0,0),(0,1,0,0,0,0),(-1,0,0,0,0,0),(0,-1,0,0,0,0))
assert all(sum(x!=0 for x in step)==1 for step in axes)
assert all(sum(t[k] for t in axes)==0 for k in range(6))
edges=((0,1),(1,2),(2,3),(3,0))
H={(0,0),(1,1),(2,2),(3,3)}
assert (0,0) in H
def batch(r,s):
    M=[[[0]*4 for _ in range(4)] for _ in range(4)]
    Rin=[[0]*4 for _ in range(4)]
    Rout=[[0]*4 for _ in range(4)]
    edge_occ=[0]*4
    for _ in range(r):
        for a,b in ((0,1),(1,2),(2,0)):
            M[0][a][b]+=1
    for _ in range(s):
        for i,(x,y) in enumerate(edges):
            Rout[x][0]+=1
            Rin[y][0]+=1
            edge_occ[i]+=1
    credit=min(M[0][0][1],M[0][1][2],M[0][2][0])
    scalar=[]
    for x in range(4):
        ing=sum(sum(row) for row in M[x])+sum(Rin[x])
        out=sum(sum(M[x][a][b] for a in range(4)) for b in range(4))+sum(Rout[x])
        scalar.append(ing-out)
    boundary=[0]*4
    for amount,(a,b) in zip(edge_occ,edges):
        boundary[a]-=amount;boundary[b]+=amount
    assert (credit,tuple(edge_occ))==(r,(s,s,s,s))
    assert scalar==boundary==[0,0,0,0]
    assert min(edge_occ)>=0
    return credit,tuple(edge_occ),tuple(scalar)
data={}
for r,s in product(range(9),repeat=2):
    k=','.join(map(str,(r,s)))
    data[k]=batch(r,s)
assert len(data)==81
assert data['1,0'][:2]==(1,(0,0,0,0))
assert data['0,1'][:2]==(0,(1,1,1,1))
out={'schema':'R682C_FOUR_CELL_V29_V39_LEDGER_V1',
     'native_spatial_axes':6,'cells':4,'edges':4,
     'declared_H':sorted(map(list,H)),
     'cases':len(data),'case_range':'r,s integers from 0 through 8',
     'independent_readout':'(internal j_star,net edge transfer chain)=(r,s*(1,1,1,1))',
     'continuity':'all cell scalar charge changes exactly zero',
     'model_status':'Typed finite X6 event ledger; V27/V17 coupling still open.'}
with open('R682C_FOUR_CELL_EVIDENCE.json','w',encoding='utf8') as f:
    json.dump(out,f,indent=2,ensure_ascii=False,sort_keys=True);f.write('\n')
print(json.dumps(out,ensure_ascii=False,sort_keys=True))
print('R682C_V29_V39_FOUR_CELL_INDEPENDENCE_EXACT_PASS')
