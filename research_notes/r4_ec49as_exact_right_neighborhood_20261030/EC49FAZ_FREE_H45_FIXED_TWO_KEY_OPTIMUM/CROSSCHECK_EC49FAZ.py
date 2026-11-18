"""Independent exact H4/H5 candidate and native signed witness crosscheck."""
import collections, itertools, json
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=[(1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8)]
S={0:0,1:0,2:4,3:1,4:16,5:32,6:8,7:2,8:0}
letters='acdefg'
witness={2:['fe','ge'],3:['feg','gef'],4:['fegc','fegd','gefc','gefd'],5:['feggf','gefgf'],6:['fegccc','fegddd','gefccc','gefddd'],7:['fegccfg','fegddgf','gefccfg','gefddgf'],8:['feggfgfc','feggfgfd','gefgfgfc','gefgfgfd'],9:['feggfgfgf','gefgfgfgf']}
def primitive(w):return tuple(q for c in w for q in OPS[c])
def signature(w):
 s=0
 for c in w:s=T[s][letters.index(c)]
 return S[s]
def cache(w):
 p=primitive(w);return [sum(x==i for x in p) for i in range(1,7)],[sum((x==i)-(x==-i) for x in p) for i in range(1,7)]
def distinct_prefixes(ws):return set(p[:n] for w in ws for p in [primitive(w)] for n in range(1,len(p)+1))
def count_candidates(h,K):
 x,y,z=K;r=x+y-h-1;f=h+1-y-2*z;g=h+1-x
 counts=collections.Counter()
 for numc in range(r+1):
  bag='a'*(z-1)+'e'*z+'c'*numc+'d'*(r-numc)+'f'*f+'g'*g
  for seq in set(itertools.permutations(bag)):
   s=signature(seq)
   if s:counts[s]+=1
 return dict(sorted(counts.items()))
res={}
for h in (4,5):
 counts=count_candidates(h,(4,2,1));res[h]=counts
 assert counts==({1:12,2:12,4:12,8:12} if h==4 else {16:12,32:12})
seen=[];stages={};keys=set()
for h in range(2,10):
 sig=0
 for w in witness[h]:
  k,d=cache(w);assert d==[2,0,0,0,0,0],(h,w,d)
  assert k[3:]==[0,0,0]
  assert (h==2 and tuple(k[:3]) in {(2,1,1),(3,0,1)}) or (h==3 and tuple(k[:3])==(3,1,1)) or (h in (4,5) and tuple(k[:3])==(4,2,1)) or (h>=6 and tuple(k[:3])==(6,4,1))
  sig|=signature(w);keys.add(tuple(k))
 assert (sig&18)and(sig&20)and(sig&33)and(sig&40)
 seen+=witness[h];stages[h]=len(distinct_prefixes(seen))
assert stages=={2:12,3:16,4:32,5:38,6:70,7:82,8:106,9:112}
assert len(keys)==5
print(json.dumps({'schema':'EC49FAZ_INDEPENDENT_PYTHON_CHECK','h45_signature_counts':res,'witness_stage_edges':stages,'witness_unique_cache_keys':len(keys),'status':'PASS'},indent=2,ensure_ascii=False))
