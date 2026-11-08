#!/usr/bin/env python3
"""Exact finite BRC signed-X6 prefix-packing sieve for H8 mixed family.
Uses frozen scientific source fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import functools,itertools, collections, argparse, time, json
LETTERS='acdefg'
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
NEXT=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
OBS=(0,0,4,1,16,32,8,2,0)
COUNT=0

def counts(h,k):
 x,y,z=k
 return z-1,x+y-h-1,h+1-y-2*z,h+1-x

@functools.lru_cache(None)
def words(h,k):
 a,cd,f,g=counts(h,k)
 if min(a,cd,f,g)<0:return ()
 result=set()
 for c in range(cd+1):
  left=[a,c,cd-c,k[2],f,g]
  def rec(q,path):
   if not any(left):
    if OBS[q]:result.add((OBS[q],path))
    return
   for j in range(6):
    if left[j]:
     left[j]-=1;rec(NEXT[q][j],path+LETTERS[j]);left[j]+=1
  rec(0,'')
 return tuple(sorted(result))

def eligible(h,required):
 found=set()
 for z in range(1,(h+1)//2+1):
  for cd in range(h-2*z+2):
   for f in range(h-2*z+2-cd):
    g=h+1-2*z-cd-f
    k=(cd+2*z+f,cd+g,z)
    if set(required).issubset({s for s,_ in words(h,k)}):
     assert k[0]+k[1]==h+1
     found.add(k)
 return sorted(found)

def signed_steps(w):return tuple(s for ch in w for s in STEPS[ch])

@functools.lru_cache(None)
def prefixes(h,k,sig):
 W={w for s,w in words(h,k) if s==sig}
 D=collections.defaultdict(set)
 for w in W:
  path=()
  for idx,s in enumerate(signed_steps(w),1):
   path=path+(s,)
   D[idx].add(path)
 return {idx:frozenset(v) for idx,v in D.items()}

def all_groups(mixed,late):
 H={3}|set(late)
 return [(h,s) for h in range(2,10) for s in ((1,8,16) if h==mixed else ((16,32) if h in H else (1,2,4,8)))]

def build_inventories(mixed,late):
 H={3}|set(late)
 high_options=[eligible(h,(16,) if h==mixed else (16,32)) for h in sorted(H-{3})]
 output=[];seen=set();status=collections.Counter()
 for tup in itertools.product(*high_options):
  keys=frozenset([(3,1,1),*tup])
  if len(keys)!=5:continue
  key=tuple(sorted(keys))
  if key in seen:continue
  seen.add(key)
  good=True
  for h,s in all_groups(mixed,late):
   if not any(any(label==s for label,_ in words(h,k)) for k in keys):good=False;break
  status['feasible' if good else 'infeasible']+=1
  if good: output.append(key)
 return output,status,high_options

def greedy_independent(adj,n):
 """Return certified independent vertex selection using multiple deterministic greedy orders."""
 best=()
 if n==0:return best
 degrees=[x.bit_count() for x in adj]
 orders=[sorted(range(n),key=lambda j:(degrees[j],j)),
         sorted(range(n),key=lambda j:(degrees[j],-j)),
         list(range(n)),list(range(n-1,-1,-1))]
 for offset in range(0,n,3):
  orders.append(sorted(range(n),key=lambda j:((degrees[j]+offset+j)%max(n,1),degrees[j],j)))
 for order in orders:
  sel=[];mask=0
  for j in order:
   if adj[j]&mask==0:
    sel.append(j);mask|=1<<j
  if len(sel)>len(best):best=tuple(sorted(sel))
 assert all(not (adj[i]&(1<<j)) for ii,i in enumerate(best) for j in best[ii+1:])
 return best

def sieve(mixed,late,limit=0,start=0):
 beginning=time.time()
 invs,stat,options=build_inventories(mixed,late)
 print('inventories',late,len(invs),stat,'key-options',[(len(x),x[:3]) for x in options],flush=True)
 groups=all_groups(mixed,late); assert len(groups)==23
 all_keys=sorted(set(itertools.chain.from_iterable(invs)))
 word_prefixes={}
 for h,s in groups:
  for k in all_keys:
   if any(label==s for label,_ in words(h,k)):
    word_prefixes[(h,s,k)] = prefixes(h,k,s)
 print('cached nonempty',(len(word_prefixes)),'elapsed',round(time.time()-beginning,2),flush=True)
 out=[]
 for count,keys in enumerate(invs):
  if count<start: continue
  if limit and count>=limit: break
  by_group=[]; min_lengths=[]
  for h,s in groups:
   U=collections.defaultdict(set); lens=[]
   for k in keys:
    dic=word_prefixes.get((h,s,k))
    if dic:
     lens.append(max(dic))
     for d,p in dic.items():U[d].update(p)
   assert lens
   min_lengths.append(min(lens))
   by_group.append(U)
  layers=[];layer_witness=[]
  for d in range(1,21):
   adj=[0]*len(groups)
   for i in range(len(groups)):
    ai=by_group[i].get(d)
    if not ai:continue
    for j in range(i+1,len(groups)):
     aj=by_group[j].get(d)
     if aj and not ai.isdisjoint(aj):adj[i]|=1<<j;adj[j]|=1<<i
   active=[i for i in range(len(groups)) if d<=min_lengths[i]]
   adj2=[sum(1<<z for z,j in enumerate(active) if adj[i]&(1<<j)) for i in active]
   chosen=greedy_independent(adj2,len(active))
   witness=[active[i] for i in chosen]
   layers.append(len(witness));layer_witness.append(witness)
  lower=sum(layers)
  out.append((lower,keys,layers,layer_witness))
  if count%100==0:print('progress',count,'lb',lower,'elapsed',round(time.time()-beginning,2),flush=True)
 print('classified',len(out),'bounds',collections.Counter(x[0] for x in out),'elapsed',round(time.time()-beginning,2),flush=True)
 return out,stat
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('late');ap.add_argument('--limit',type=int,default=0);ap.add_argument('--start',type=int,default=0);args=ap.parse_args()
 out,stat=sieve(8,tuple(map(int,args.late)),args.limit,args.start)
 data={'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','late':args.late,'limit':args.limit,'start':args.start,'status':dict(stat),'counts':dict(collections.Counter(str(row[0]) for row in out)),'sample': [{'lower_bound':a,'keys':k,'layers':v} for a,k,v,_ in out[:10]]}
 with open('SIEVE_'+args.late+'_'+str(args.limit)+'.json','w') as f:json.dump(data,f,indent=2)
 if True:
  with open('WITNESSES_'+args.late+'_'+str(args.start)+'_'+str(args.limit)+'.jsonl','w') as f:
   for lb,keys,layers,witness in out:
    f.write(json.dumps({'keys':keys,'lower_bound':lb,'D':witness},separators=(',',':'))+'\n')
