#!/usr/bin/env python3
"""Minimax over fixed phase translates only; not a global optimal field theorem."""
from pathlib import Path
import hashlib,importlib.util,sys,time,json
from itertools import product,combinations
from collections import deque,Counter
import numpy as np
root=Path(__file__).resolve().parent
import argparse
parser=argparse.ArgumentParser(description='Exact finite atlas minima and translated-chart minimax certificates')
parser.add_argument('--output',type=Path,default=root/'results')
OUT=parser.parse_args().output;OUT.mkdir(parents=True,exist_ok=True)
path=next((p for p in [root/'prior/nollm_two_inert_511/experiment.py',root/'nollm_two_inert_511_20260909_c6c82.py'] if p.exists()),None)
if path is None:raise FileNotFoundError('hash-pinned two-inert predecessor required')
assert hashlib.sha256(path.read_bytes()).hexdigest()=='db00742a81241d10883299253307fb1ee7831b7703bf710f88288606998f53b4'
s=importlib.util.spec_from_file_location('inert_parent',path);f=importlib.util.module_from_spec(s);sys.modules['inert_parent']=f;s.loader.exec_module(f)
m=f.m

def cycle(p,l):
    ans=[]
    while l not in ans:ans.append(l);l=f.act(f.ES[7],l,p,True)
    assert l==ans[0]
    return ans
c5=cycle(5,3);c11=cycle(11,8)
print('cycles',c5,c11,flush=True)
for p in [7,13,19]:
 a=c5.index(f.act(f.ES[p],c5[0],5,True));b=c11.index(f.act(f.ES[p],c11[0],11,True))
 print('shift',p,a,b)
 assert all(f.act(f.ES[p],c5[i],5,True)==c5[(i+a)%6] for i in range(6))
 assert all(f.act(f.ES[p],c11[i],11,True)==c11[(i+b)%12] for i in range(12))
print('setup',len(f.KEYS),flush=True)

def delta(C):
 a,b,c,d=map(int,C.ravel());u=-(b+c);v=a+c-d
 return u*u+u*v+v*v

def ratio(D,n):
 return (np.sqrt(3*n+D)+np.sqrt(D))/(np.sqrt(3*n+D)-np.sqrt(D))

# Exact minimization uses finite ellipsoid supersets based on candidate trace.
def minimum(H):
 n=m.old.det(H)
 seeds=[]
 for a,b,c,d in product(range(-2,3),repeat=4):
  if a*d-b*c==1:seeds.append(H@np.array([[a,b],[c,d]],dtype=np.int64))
 best=min(seeds,key=delta);bestd=delta(best)
 # Any improving matrix has each Euclidean column squared length <= its trace.
 cap=(6*n+4*bestd)//3  # floor(trace), safe for Q integer
 # enumerate vectors directly in ambient coords, then membership
 R=__import__('math').isqrt(4*cap//3)+1
 cand=np.array([(q,r) for q,r in product(range(-R,R+1),repeat=2) if (q or r) and f.Q((q,r))<=cap],dtype=np.int64)
 cand=cand[np.all((cand@m.old.adj(H).T)%n==0,axis=1)]
 for x in cand:
  dt=x[0]*cand[:,1]-x[1]*cand[:,0]
  for y in cand[dt==n]:
   C=np.array([x,y],dtype=np.int64).T;D=delta(C)
   if D<bestd:bestd=D;best=C.copy()
 return dict(det=n,delta=bestd,K=float(ratio(bestd,n)),matrix=best.tolist(),cap=cap,vectors=len(cand))

regular=minimum(f.I)
assert regular['delta']==0
(OUT/'regular.json').write_text(json.dumps(regular,indent=2))
costs=np.empty((6,12),dtype=np.int64);records=[]
for i,j in product(range(6),range(12)):
 rec=minimum(f.H(1,1,c5[i],c11[j]));rec.update(i=i,j=j,line5=c5[i],line11=c11[j]);records.append(rec);costs[i,j]=rec['delta']
print('costdist',Counter(costs.ravel()),flush=True)
np.save(OUT/'costs.npy',costs);(OUT/'minima.json').write_text(json.dumps(records,indent=2))
print('max',max(r['K'] for r in records),'min',min(r['K'] for r in records),flush=True)
# Translate extra representations, measure worst best over phase choices.
best={}
for a,b in product(range(6),range(12)):
 shifted=np.roll(costs,(-a,-b),(0,1));worst=int(np.minimum(costs,shifted).max())
 best[(a,b)]=worst
val=min(best.values());print('two_best_delta',val,'K',ratio(val,55),'offsets',[list(s) for s,v in best.items() if v==val],flush=True)
(OUT/'two_options.json').write_text(json.dumps([dict(offset=k,delta=v,K=float(ratio(v,55))) for k,v in best.items()],indent=2))
# Triple all possible offsets incl zero; labels A and B symmetric.
translations=[np.roll(costs,(-a,-b),(0,1)) for a,b in product(range(6),range(12))]
b3=10**8;w3=[]
for a,b in combinations(range(1,72),2):
 v=int(np.minimum(np.minimum(costs,translations[a]),translations[b]).max())
 if v<b3:b3=v;w3=[(a,b)]
 elif v==b3:w3.append((a,b))
print('three_best',b3,ratio(b3,55),[(divmod(a,12),divmod(b,12)) for a,b in w3[:20]],'count',len(w3),flush=True)
(OUT/'three_best.json').write_text(json.dumps(dict(delta=b3,K=float(ratio(b3,55)),offset_pairs=[(divmod(a,12),divmod(b,12)) for a,b in w3]),indent=2))
singles5=[minimum(f.H(1,0,l,-1)) for l in c5]
singles11=[minimum(f.H(0,1,-1,k)) for k in c11]
print('single5',[(a['delta'],a['K']) for a in singles5]);print('single11',[(a['delta'],a['K']) for a in singles11])
# rank comparisons using Delta/n; common denominator 55 makes all exact ints.
allcost=np.empty((4,6,12),dtype=np.int64);allcost[0]=0
allcost[1]=np.array([r['delta']*11 for r in singles5])[:,None]
allcost[2]=np.array([r['delta']*5 for r in singles11])[None,:]
allcost[3]=costs
pair=[]
for a,b in product(range(6),range(12)):
 worst=int(np.minimum(allcost,np.roll(allcost,(-a,-b),(1,2))).max())
 pair.append(dict(offset=[a,b],score=worst,K=float(ratio(worst,55))))
v=min(r['score'] for r in pair);print('all_parity_two',v,ratio(v,55),'offsets',[r['offset'] for r in pair if r['score']==v])
(OUT/'all_parity_pairs.json').write_text(json.dumps(pair,indent=2))
np.save(OUT/'allcost.npy',allcost)
(OUT/'singles.json').write_text(json.dumps(dict(p5=singles5,p11=singles11),indent=2))
sh=[np.roll(allcost,(-a,-b),(1,2)) for a,b in product(range(6),range(12))]
b3=10**8;w3=[]
for a,b in combinations(range(1,72),2):
 val=int(np.minimum(np.minimum(allcost,sh[a]),sh[b]).max())
 if val<b3:b3=val;w3=[(a,b)]
 elif val==b3:w3.append((a,b))
print('all_parity_three',b3,ratio(b3,55),[(divmod(a,12),divmod(b,12)) for a,b in w3[:10]],'count',len(w3))
(OUT/'all_parity_triples.json').write_text(json.dumps(dict(score=b3,K=float(ratio(b3,55)),offset_pairs=[(divmod(a,12),divmod(b,12)) for a,b in w3]),indent=2))
