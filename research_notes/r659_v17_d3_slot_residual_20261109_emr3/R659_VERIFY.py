#!/usr/bin/env python3
"""R657 exact frozen signed V23/V27/V29/V17 event-order verifier."""
from itertools import combinations, permutations, product
import json
from pathlib import Path
B=((0,1),(2,0),(2,3),(3,0))
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
V=tuple(combinations(range(6),3))
NEI={s:tuple(t for t in V if len(set(s)&set(t))==2) for s in V}
def code(s):
 z=set(s)
 return tuple(0 if any(((a in z)+(b in z))!=1 for a,b in m) else (1 if sum(b in z for a,b in m)%2==0 else -1) for m in MATCH)
C={s:code(s) for s in V}
assert len(set(C.values()))==20
def fresh(counts):
 M=[[0]*4 for _ in range(4)]
 for (a,b),n in zip(B,counts): M[a][b]+=n
 return {'M':M,'rin':[0]*4,'rout':[0]*4}
def score(L,s,t):
 M=L['M']; O=[[M[i][j]-M[j][i] for j in range(4)] for i in range(4)]
 u=[sum(O[i])+L['rin'][i]-L['rout'][i] for i in range(4)]
 return sum(u[i]*C[t][i] for i in range(4))+sum(C[s][i]*O[i][j]*C[t][j] for i in range(4) for j in range(4))
def step(L,s,slots):
 ranked=sorted(((score(L,s,t),t) for t in NEI[s]),reverse=True)
 gap=ranked[0][0]-ranked[1][0]
 if gap<=0:return None
 t=ranked[0][1];same=set(s)&set(t)
 leave=next(iter(set(s)-same));enter=next(iter(set(t)-same))
 out={a:slots[a] for a in same};out[enter]=slots[leave]
 return t,out,gap,(s.index(leave)+t.index(enter))%2
def run(cx,cy,events):
 L={c:fresh(seed) for c,seed in (('x',cx),('y',cy))}
 active={c:((0,1,2),{0:0,1:1,2:2}) for c in ('x','y')}
 N=[[0]*4 for _ in range(4)]; trace=[]
 for a,b in events:
  L['x']['rout'][a]+=1;L['y']['rin'][b]+=1;N[a][b]+=1;row={'event':(a,b)}
  for c in ('x','y'):
   s,slots=active[c];ret=step(L[c],s,slots)
   if ret is None:return None
   t,new,gap,bit=ret;active[c]=(t,new)
   row[c]={'triad':t,'slots':tuple(new[i] for i in t),'gap':gap,'bit':bit}
  trace.append(row)
 end={c:(s,tuple(slots[i] for i in s)) for c,(s,slots) in active.items()}
 return L,N,end,trace
def parity(p):return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2

# R659: S3 = Z3 rtimes Z2 full-slot closure and same-parity collision
ID=(0,1,2);RHO=(1,2,0);TAU=(1,0,2)
def compose(a,b):return tuple(a[b[k]] for k in range(3))
def power(a,n):
    v=ID
    for _ in range(n):v=compose(v,a)
    return v
def decode(r,p):return compose(power(RHO,r),power(TAU,p))
ENC={decode(r,p):(r,p) for r in range(3) for p in range(2)}
assert len(ENC)==6
assert all(parity(s)==p for s,(r,p) in ENC.items())
def gamma(i,j):
    a=[0,1,2];v=a.pop(i);a.insert(j,v);return tuple(a)
for sigma in permutations(ID):
    r,p=ENC[sigma]
    for i in range(3):
        for j in range(3):
            g=gamma(i,j);s,q=ENC[g]
            updated=tuple(sigma[g[k]] for k in range(3))
            assert ENC[updated]==((r+(-1 if p else 1)*s)%3,p^q)
for A in permutations(ID):
    for B in permutations(ID):
        r,p=ENC[A];s,q=ENC[B]
        assert ENC[compose(A,B)]==((r+(-1 if p else 1)*s)%3,p^q)
cy=(3,3,3,3);events=((0,0),(1,1),(2,2),(3,3))
words=strict=maxfiber=0;first=None
for cx in product(range(4),repeat=4):
    groups={}
    for seq in permutations(events):
        words+=1
        data=run(cx,cy,seq)
        if data is None:continue
        strict+=1
        L,N,end,trace=data
        key=tuple((end[c][0],parity(end[c][1])) for c in ('x','y'))
        group=groups.setdefault(key,{})
        slots=tuple(end[c][1] for c in ('x','y'))
        group.setdefault(slots,(seq,data))
        maxfiber=max(maxfiber,len(group))
        if first is None and len(group)>1:
            first=(cx,key,list(group.values())[:2])
assert (words,strict,maxfiber)==(6144,1161,2)
assert first is not None
cx,key,items=first;(A,ra),(B,rb)=items
assert cx==(2,0,0,0)
assert A==((2,2),(0,0),(3,3),(1,1))
assert B==((3,3),(0,0),(2,2),(1,1))
assert ra[:2]==rb[:2]
assert ra[2]['x']==((2,4,5),(0,2,1))
assert rb[2]['x']==((2,4,5),(1,0,2))
assert ra[2]['y']==rb[2]['y']==((0,2,4),(1,2,0))
assert ENC[ra[2]['x'][1]]==(2,1) and ENC[rb[2]['x'][1]]==(0,1)
evidence={
 'marker':'R659_SAME_PARITY_DIFFERENT_D3_RESIDUE_PASS',
 'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'source':'V23/V27/V17/V29@b62110008321d9147212cb89f2627ff613c2550d',
 'model':'two X6 Cells; auxiliary event-first strict signed V27 followed by V17',
 'D3_group_law':'(r,p)*(s,q)=(r+(-1)^p*s mod3,p xor q)',
 'permutation_product_checks':36,'edge_reindexing_checks':54,
 'bounded_search':{'x_seeds':256,'four_event_words':words,'strict_words':strict,
                   'maximum_same_triad_parity_full_slot_fiber':maxfiber},
 'witness':{'x_pass_seed':cx,'y_pass_seed':cy,'events':events,
            'word_A':A,'word_B':B,'same_full_ledgers_and_pair_histogram':True,
            'A':{'end':ra[2],'x_d3':ENC[ra[2]['x'][1]],'trace':ra[3]},
            'B':{'end':rb[2],'x_d3':ENC[rb[2]['x'][1]],'trace':rb[3]}},
 'scope':'model-internal exact counterexample; no native V28/V30 law claim',
 'driver_review':'UNREVIEWED'}
Path(__file__).with_name('R659_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(evidence['marker'],'words',words,'strict',strict,'maxfiber',maxfiber,
      'x-D3-A',ENC[ra[2]['x'][1]],'x-D3-B',ENC[rb[2]['x'][1]])
