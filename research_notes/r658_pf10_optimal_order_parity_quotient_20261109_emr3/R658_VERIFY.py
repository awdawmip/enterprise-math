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

# R658: exact parity quotient and strict positive-cost nonunique optimal repair
from functools import lru_cache
SEED_X=(0,1,3,0);SEED_Y=(3,3,3,3)
SEND=(1,1,1,0);OLD=(0,1,1,1)
H={0:(0,1),1:(1,),2:(2,),3:()}
K={(i,i):0 for i in range(4)}; K[(3,0)]=K[(3,1)]=1

def qstep(L,s,p):
    z=step(L,s,{a:i for i,a in enumerate(s)})
    if z is None:return None
    t,slots,gap,bit=z
    return (t,p^bit,gap)

def qrun(cx,cy,events):
    L={'x':fresh(cx),'y':fresh(cy)}
    state={'x':((0,1,2),0),'y':((0,1,2),0)}
    gaps=[]
    for a,j in events:
        L['x']['rout'][a]+=1;L['y']['rin'][j]+=1
        out={c:qstep(L[c],*state[c]) for c in ('x','y')}
        if any(v is None for v in out.values()):return None
        gaps.append((out['x'][2],out['y'][2]))
        state={c:(out[c][0],out[c][1]) for c in ('x','y')}
    return (*state['x'],*state['y'],tuple(gaps))

def plans():
    for old in permutations((1,2,3)):
        for recv0 in H[0]:
            actual=(recv0,1,2)
            if all((i,j) in K for i,j in zip(old,actual)):
                p=tuple((a,i,j) for a,(i,j) in enumerate(zip(old,actual)))
                yield (p,sum(K[i,j] for i,j in zip(old,actual)))

def compare_full(cx,cy,events):
    full=run(cx,cy,events);q=qrun(cx,cy,events)
    assert (full is None)==(q is None)
    if q is not None:
        assert (full[2]['x'][0],parity(full[2]['x'][1]),
                full[2]['y'][0],parity(full[2]['y'][1]))==q[:4]
    return q

PLANS=list(plans());assert len(PLANS)==3
assert set(c for p,c in PLANS)=={1}
assert len(set(tuple((a,j) for a,i,j in p) for p,c in PLANS))==2
strict=[]
for p,cost in PLANS:
    for w in permutations(p):
        actual=tuple((a,j) for a,i,j in w)
        q=compare_full(SEED_X,SEED_Y,actual)
        if q is not None:
            strict.append({'plan':p,'word':w,'cost':cost,'end':q[:4],'gaps':q[4]})
assert len(strict)==12
ENDS={((0,3,4),0,(0,1,2),1),((0,3,4),1,(0,1,2),1)}
assert set(z['end'] for z in strict)==ENDS
assert len(set(z['plan'] for z in strict))==3

def incr(v,i):
    z=list(v);z[i]+=1;return tuple(z)
def decr(v,i):
    z=list(v);z[i]-=1;return tuple(z)
def with_io(seed,rin,rout):
    L=fresh(seed);L['rin']=list(rin);L['rout']=list(rout);return L

@lru_cache(None)
def dp(sr,tr,ro,ri,sx,px,sy,py):
    if not any(sr):
        return (0,frozenset({(sx,px,sy,py)})) if not any(tr) else None
    best=None;ends=set()
    for a in range(4):
        if not sr[a]:continue
        for i in range(4):
            if not tr[i]:continue
            for j in H[a]:
                if (i,j) not in K:continue
                n_ro=incr(ro,a);n_ri=incr(ri,j)
                vx=qstep(with_io(SEED_X,(0,0,0,0),n_ro),sx,px)
                vy=qstep(with_io(SEED_Y,n_ri,(0,0,0,0)),sy,py)
                if vx is None or vy is None:continue
                tail=dp(decr(sr,a),decr(tr,i),n_ro,n_ri,
                        vx[0],vx[1],vy[0],vy[1])
                if tail is None:continue
                cand=K[(i,j)]+tail[0]
                if best is None or cand<best:
                    best=cand;ends=set(tail[1])
                elif cand==best:ends.update(tail[1])
    return (best,frozenset(ends)) if best is not None else None

result=dp(SEND,OLD,(0,0,0,0),(0,0,0,0),(0,1,2),0,(0,1,2),0)
assert result==(1,frozenset(ENDS))
n=valid=0
for seed in product(range(4),repeat=4):
    for recv0 in H[0]:
        for word in permutations(((0,recv0),(1,1),(2,2))):
            n+=1
            if compare_full(seed,SEED_Y,word) is not None:valid+=1
assert (n,valid)==(3072,1072)
p=run(SEED_X,SEED_Y,((0,0),(1,1),(2,2)))
q=run(SEED_X,SEED_Y,((1,1),(0,0),(2,2)))
assert p is not None and q is not None and p[:2]==q[:2]
assert p[2]['x'][0]==q[2]['x'][0]
assert parity(p[2]['x'][1])!=parity(q[2]['x'][1])
evidence={
  'marker':'R658_OPTIMAL_HOLONOMY_PARITY_QUOTIENT_EXACT_PASS',
  'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
  'typed_source':'V23/V27/V17/V29@b62110008321d9147212cb89f2627ff613c2550d',
  'model':'two X6 Cells / signed BRC / event-first strict V27 followed by V17',
  'positive_cost_example':{'x_pass_seed':SEED_X,'y_pass_seed':SEED_Y,
    'sender_quotas':SEND,'old_target_quotas':OLD,
    'H':H,'K':'identity cost0; 3->0 and 3->1 each cost1',
    'distinct_detailed_plans':len(PLANS),'distinct_actual_pair_matrices':2,
    'allowed_candidate_event_words':18,'strict_words':len(strict),
    'minimum_strict_cost':result[0],'optimal_parity_terminal_set':sorted(ENDS),
    'exact_strict_words':strict},
  'parity_quotient_regression':{'candidate_words':n,'all_steps_strict':valid},
  'exact_bellman_states':dp.cache_info().currsize,
  'scope':'author-side precise finite witness and universal model-conditional lemma; not native law',
  'driver_review':'UNREVIEWED'}
Path(__file__).with_name('R658_EVIDENCE.json').write_text(
    json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(evidence['marker'])
print('plans',len(PLANS),'strict',len(strict),'optimal cost',result[0],
      'endpoints',sorted(ENDS),'regression',n,valid,'states',dp.cache_info().currsize)
