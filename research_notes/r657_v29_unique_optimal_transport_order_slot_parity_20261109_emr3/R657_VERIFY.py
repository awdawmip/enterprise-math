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
n2=strict2=diff2=same2=0
for cx in product(range(4),repeat=4):
 for a,b in combinations(range(4),2):
  n2+=1;e=((a,0),(b,1));p=run(cx,(3,3,3,3),e);q=run(cx,(3,3,3,3),e[::-1])
  if p is None or q is None:continue
  strict2+=1;assert p[:2]==q[:2]
  if p[2]!=q[2]:
   diff2+=1
   if all(p[2][c][0]==q[2][c][0] for c in ('x','y')):same2+=1
assert (n2,strict2,diff2,same2)==(1536,416,30,0)
n3=strict3=all6=pairs=0;first=None
for cx in product(range(4),repeat=4):
 for senders in combinations(range(4),3):
  n3+=1;valid=[]
  for word in permutations(tuple(zip(senders,(0,1,2)))):
   z=run(cx,(3,3,3,3),word)
   if z is not None:valid.append((word,z))
  strict3+=len(valid)
  if len(valid)==6:all6+=1
  for (wa,za),(wb,zb) in combinations(valid,2):
   if za[2]!=zb[2] and all(za[2][c][0]==zb[2][c][0] for c in ('x','y')):
    pairs+=1
    if first is None:first=(cx,wa,wb)
assert (n3,strict3,all6,pairs)==(1024,1911,127,60)
A=((0,0),(1,1),(2,2));D=((1,1),(0,0),(2,2))
cx=(0,1,3,0);cy=(3,3,3,3)
p=run(cx,cy,A);q=run(cx,cy,D)
assert p is not None and q is not None and p[:2]==q[:2]
assert p[2]['x']==((0,3,4),(1,2,0)) and q[2]['x']==((0,3,4),(0,2,1))
assert p[2]['y']==q[2]['y']==((0,1,2),(1,0,2))
assert (parity(p[2]['x'][1]),parity(q[2]['x'][1]))==(0,1)
assert [[r[c]['gap'] for r in z[3]] for z,c in ((p,'x'),(q,'x'),(p,'y'),(q,'y'))]==[[1,1,1],[1,2,1],[3,1,8],[2,1,8]]
assert [r['x']['bit'] for r in p[3]]==[0,0,0] and [r['x']['bit'] for r in q[3]]==[0,0,1]
K={(i,i):0 for i in range(4)};K[3,0]=1
edits=[(old,sum(K[i,j] for i,j in zip(old,(0,1,2)))) for old in permutations((1,2,3)) if all((i,j) in K for i,j in zip(old,(0,1,2)))]
assert edits==[((3,1,2),1)] and first[0]==cx
result={'marker':'R657_OPTIMAL_SCHEDULE_SAME_TRIAD_DIFFERENT_SLOT_PARITY_PASS',
        'science_pin':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
        'source_pin':'V29/V27/V17@b62110008321d9147212cb89f2627ff613c2550d',
        'search':{'two_cases':n2,'two_both_strict':strict2,'two_diff':diff2,'two_same_tri_diff_slots':same2,
                  'three_configs':n3,'three_words':6*n3,'three_strict':strict3,'three_six_strict_configs':all6,'three_same_tri_diff_slots_pairs':pairs},
        'witness':{'seed_x':cx,'seed_y':cy,'A':A,'B':D,'end_A':p[2],'end_B':q[2],
                   'trace_A':p[3],'trace_B':q[3],'full_ledgers_N_equal':p[:2]==q[:2],
                   'optimal_cost_identity':0,'optimal_cost_edited':edits[0][1]},
        'arithmetic':'exact integers only','status':'author-side; independent Driver pending'}
Path(__file__).with_name('R657_EVIDENCE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(result['marker'],result['search'])