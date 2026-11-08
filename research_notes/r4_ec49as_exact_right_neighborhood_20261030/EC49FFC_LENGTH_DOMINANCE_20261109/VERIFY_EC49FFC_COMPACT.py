"""EC49FFC standalone exact original-BRC-X6 / nine-state / profile audit."""
from itertools import combinations, product
from collections import Counter
from math import factorial
import json

A='acdefg'
STEP=[(-1,-1),(1,2,-1,-2),(2,1,-2,-1),(3,1,1,-3),(1,-1),(2,-2)]
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
OBS=(0,0,4,1,16,32,8,2,0)
W94={2:['de','ed','ce','ec'],3:['feg','gef'],4:['fegg','gefg'],
 5:['feggd','feggc','gefgd','gefgc'],6:['fegggf','gefggf'],
 7:['fegggfg','gefggfg'],8:['fegggfgd','fegggfgc','gefggfgd','gefggfgc'],
 9:['fegggfggf','gefggfggf']}

def keypairs(h):
 for z in range(1,(h+1)//2+1):
  for cd in range(h+2-2*z):
   for f in range(h+2-2*z-cd):
    g=h+1-2*z-cd-f
    yield (cd+2*z+f,cd+g,z),(z-1,cd,z,f,g)

def native(word):
 steps=tuple(v for ch in word for v in STEP[A.index(ch)])
 p=[0]*6
 for v in steps:p[abs(v)-1]+=1 if v>0 else -1
 return steps,tuple(p)

def scan(h,k,counts):
 a,cd,e,f,g=counts;found=Counter();x,y,z=k
 assert a==z-1 and cd==x+y-h-1
 for c in range(cd+1):
  rem=[a,c,cd-c,e,f,g];w=[]
  def dfs(q):
   if not any(rem):
    label=OBS[q]
    if label:
     steps,endpoint=native(w)
     assert len(w)==h and len(steps)==2*(x+y+z-1)
     assert endpoint==(2,0,0,0,0,0)
     found[label]+=1
    return
   for j in range(6):
    if rem[j]:
     rem[j]-=1;w.append(A[j]);dfs(T[q][j]);w.pop();rem[j]+=1
  dfs(0)
 return found

def audit_94():
 pref=set();keys=set();support={}
 for h,ws in W94.items():
  support[h]=set()
  for w in ws:
   n=Counter(w);z=n['e'];cd=n['c']+n['d']
   assert n['a']==z-1
   k=(cd+2*z+n['f'],cd+n['g'],z);keys.add(k)
   st=0
   for ch in w: st=T[st][A.index(ch)]
   support[h].add(OBS[st])
   steps,endpoint=native(w);assert endpoint==(2,0,0,0,0,0)
   assert len(steps)==2*(sum(k)-1)
   for j in range(1,len(steps)+1):pref.add(steps[:j])
 assert len(pref)==94 and len(keys)==5 and sum(map(len,W94.values()))==22
 assert {1,2,4,8}<=support[2] and {16,32}<=support[3]
 for h in range(4,10):
  assert ({16,32} if h in (4,6,7,9) else {1,2,4,8})<=support[h]
 return len(pref)

def audit_boolean():
 n=0
 for s in product(range(4),repeat=6):
  criterion=(all(s) and sum(bool(v&1) for v in s)>=4 and
             sum(bool(v&2) for v in s)>=2)
  exhaustive=any(all(s[i]&1 for i in H) and
                 all(s[i]&2 for i in range(6) if i not in H)
                 for H in combinations(range(6),4))
  assert criterion==exhaustive
  n+=criterion
 direct=sum(factorial(6)//(factorial(b)*factorial(l)*factorial(6-b-l))
            for b in range(7) for l in range(7-b)
            if b+(6-b-l)>=4 and l+(6-b-l)>=2)
 assert n==direct==483
 return n

def run():
 by_h={};K=set();KS=set();strictwords=0;allwords=0;allpairs=0;strictpairs=0
 for h in range(2,10):
  stats=Counter();nonzero=0
  for k,counts in keypairs(h):
   allpairs+=1;K.add(k)
   found=scan(h,k,counts)
   stats.update(found)
   nonzero+=bool(found)
   if min(k)>0:
    strictpairs+=1;KS.add(k);strictwords+=sum(found.values())
  by_h[str(h)]={'words':sum(stats.values()),'nonzero_keys':nonzero}
  allwords+=sum(stats.values())
 assert [by_h[str(h)]['words'] for h in range(2,10)]==[6,38,206,1062,5352,26644,131686,647930]
 assert [by_h[str(h)]['nonzero_keys'] for h in range(2,10)]==[3,6,13,21,34,49,70,94]
 assert (allpairs,len(K),allwords,strictpairs,len(KS),strictwords)==(294,164,812924,270,140,811355)
 assert audit_94()==94
 return {'frozen_science':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
         'all_count_admissible_pairs':allpairs,'all_keys':len(K),'all_labelled_words':allwords,
         'strict_positive_xyz_pairs':strictpairs,'strict_positive_xyz_keys':len(KS),
         'strict_positive_xyz_words':strictwords,'native_length_endpoint':'EXACT_PASS',
         'boolean_profiles_total':4096,'dominated_boolean_profiles':audit_boolean(),
         'prior_witness_native_edges':94,'horizon_details':by_h}
if __name__=='__main__':print(json.dumps(run(),indent=2))
