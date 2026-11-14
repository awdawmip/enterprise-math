"""EC49FFP: independently runnable one-key adjacent-horizon census.
Frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Original X6/DFA model Git blob 6350340fbe869f17b5a50bd1ba30640db44a3a99.
"""
from collections import Counter
import json
A='acdefg'; S=(0,0,4,1,16,32,8,2,0)
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}

def original_words(h,k):
 x,y,z=k;total=x+y-h-1
 for c in range(total+1):
  ct=[z-1,c,total-c,z,h+1-y-2*z,h+1-x]
  def rec(t,s):
   if not any(ct):
    if S[s] in (1,2,4,8): yield t,S[s]
    return
   for i in range(6):
    if ct[i]:
     ct[i]-=1
     yield from rec(t+A[i],T[s][i])
     ct[i]+=1
  yield from rec('',0)

def solve(horizons,k):
 need=tuple((h,s) for h in horizons for s in (1,2,4,8))
 trie=[{}];term=[0];cnt=Counter()
 for h in horizons:
  for word,sig in original_words(h,k):
   ct=Counter(x for op in word for x in OPS[op])
   assert tuple(ct[i]-ct[-i] for i in range(1,7))==(2,0,0,0,0,0)
   assert tuple(ct[i] for i in (1,2,3))==k
   cnt[h]+=1;p=0
   for x in (v for op in word for v in OPS[op]):
    if x not in trie[p]:
     trie[p][x]=len(trie);trie.append({});term.append(0)
    p=trie[p][x]
   term[p]|=1<<need.index((h,sig))
 dp=[None]*len(trie)
 for p in range(len(trie)-1,-1,-1):
  d={0:0};mask=term[p];sub=mask
  while sub:d[sub]=0;sub=(sub-1)&mask
  for child in trie[p].values():
   e=dp[child];f=d.copy()
   for a,va in d.items():
    for b,vb in e.items():
     if not a&b:
      i=a|b;v=va+vb+(b!=0)
      if v<f.get(i,10**9):f[i]=v
   d=f
  dp[p]=d
 return dp[0][255],len(trie),dict(cnt)


def keys(h):
 for z in range(1,(h+1)//2+1):
  for x in range(2*z,h+2):
   for y in range(h+2-2*z):
    if x+y>=h+2: yield (x,y,z)

def signature(word):
 st=0
 for c in word: st=T[st][A.index(c)]
 return S[st]

def native(word): return tuple(step for c in word for step in OPS[c])

def family(h):
 assert h>=5
 q=h-4
 ww={
  (h,1):'g'*q+'efdd', (h,2):'f'+'g'*q+'edd',
  (h,4):'f'+'g'*q+'ecc', (h,8):'g'*q+'efcc',
  (h+1,1):'g'*q+'efdgf', (h+1,2):'f'+'g'*q+'edgf',
  (h+1,4):'f'+'g'*q+'ecfg', (h+1,8):'g'*q+'efcfg'}
 key=(5,h-2,1); prefixes=set()
 for (window,sig),word in ww.items():
  assert signature(word)==sig,(window,sig,word)
  ct=Counter(word)
  assert ct['a']==0 and ct['e']==1
  assert ct['c']+ct['d']==sum(key[:2])-window-1
  assert ct['f']==window+1-key[1]-2*key[2]
  assert ct['g']==window+1-key[0]
  path=native(word)
  assert len(path)==2*(sum(key)-1)
  sc=Counter(path)
  assert tuple(sc[i] for i in (1,2,3))==key
  assert tuple(sc[i]-sc[-i] for i in range(1,7))==(2,0,0,0,0,0)
  prefixes.update(path[:j] for j in range(1,len(path)+1))
 profile=Counter(map(len,prefixes));L=2*h+6
 assert all(profile[j]==2 for j in range(1,2*h-1))
 assert all(profile[j]==4 for j in range(2*h-1,2*h+4))
 assert all(profile[j]==8 for j in range(2*h+4,L+1))
 assert len(prefixes)==4*h+40

def main():
 rows=[]
 for h in (5,6,7,8):
  kk=sorted(set(keys(h))&set(keys(h+1)))
  assert len(kk)=={5:7,6:13,7:22,8:34}[h]
  records=[]
  for k in kk:
   value,nodes,counts=solve((h,h+1),k)
   records.append({'key':list(k),'cost':value,'trie_nodes':nodes,
                   'eligible_words':{str(a):b for a,b in counts.items()}})
  best=min(r['cost'] for r in records)
  assert best=={5:60,6:64,7:68,8:72}[h]
  minimizers=[r['key'] for r in records if r['cost']==best]
  assert minimizers==[[x,h+3-x,1] for x in range(5,h+1)]
  rows.append({'horizons':[h,h+1],'complete_keys':len(kk),
               'global_minimum':best,'minimizers':minimizers,'rows':records})
 for h in range(5,65): family(h)
 report={'schema':'EC49FFQ_ADJACENT_ONE_KEY_EXACT_V1',
         'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
         'native_model_git_blob_sha1':'6350340fbe869f17b5a50bd1ba30640db44a3a99',
         'status':'EXACT_INTEGER_TRIE_DP_PASS; UNIVERSAL_UPPER_AUDITED; DRIVER_PENDING',
         'finite_exact_range':'H5/H6 through H8/H9',
         'complete_key_cases':sum(x['complete_keys'] for x in rows),
         'universal_upper':'C_native<=4h+40 for every integer h>=5',
         'upper_construct_audit_h':[5,64], 'rows':rows}
 print(json.dumps(report,indent=2))

if __name__=='__main__': main()
