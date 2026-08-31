#!/usr/bin/env python3
import sys,json,time
from pathlib import Path
sys.path.insert(0,'/mnt/data/r055_work/tools');import r055_core as r
D=r.DIRS

def components(R):
 unseen=set(R); comps=[]
 while unseen:
  s=unseen.pop();cc={s};st=[s]
  while st:
   p=st.pop()
   for q in r.neighbors(p):
    if q in unseen:unseen.remove(q);cc.add(q);st.append(q)
  comps.append(cc)
 return comps

def runs(R,v):
 bits=[r.add(v,d) in R for d in D]
 if all(bits):return 1
 return sum(bits[i] and not bits[(i-1)%6] for i in range(6))

def pred(C,u,v):
 R=set(C);R.remove(u); cs=components(R);k=len(cs)
 if k==0:return False
 ids=[]
 for i,cc in enumerate(cs):
  if any(q in cc for q in r.neighbors(v)):ids.append(i)
 conn=len(ids)==k
 return conn and runs(R,v)==k

def main(maxn=8):
 allc=r.enumerate_connected_classes(maxn);out=[];tot=bad=0;t=time.time()
 for N in range(2,maxn+1):
  states=[frozenset(x) for x in allc[N] if r.hole_free(frozenset(x))]
  ncase=nbad=0
  for C in states:
   F=set(r.frontier(C))
   for u in r.boundary(C):
    cand=F|{q for q in r.neighbors(u) if q not in C}
    for v in cand:
     if v==u or v in C:continue
     Cp=frozenset((set(C)-{u})|{v})
     gt=r.connected(Cp) and r.hole_free(Cp)
     pr=pred(C,u,v)
     ncase+=1
     if gt!=pr:
      nbad+=1
      if nbad<=3:print('MISMATCH',N,sorted(C),u,v,gt,pr,file=sys.stderr)
  tot+=ncase;bad+=nbad;out.append({'N':N,'hole_free_state_classes':len(states),'candidate_relocations_checked':ncase,'mismatches':nbad})
  print(N,ncase,nbad,file=sys.stderr,flush=True)
 obj={'schema':'R055_LOCAL_HOLE_CRITERION_EXHAUSTIVE_CHECK_V1','max_N':maxn,'rows':out,'total_candidate_relocations_checked':tot,'total_mismatches':bad,'status':'PASS' if bad==0 else 'FAIL','elapsed_seconds':time.time()-t}
 p=Path('/mnt/data/r055_work/artifacts/R055_LOCAL_HOLE_CRITERION_EXHAUSTIVE_CHECK.json');r.json_dump(p,obj);print(json.dumps(obj,indent=2))
 if bad:raise SystemExit(1)
if __name__=='__main__':main()
