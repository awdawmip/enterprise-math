#!/usr/bin/env python3
"""Exact stdlib verification of EC49FEZ pooled BRC / signed X6 prefix certificate."""
import json,sys,itertools
from functools import lru_cache
LETTERS='acdefg'
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
NEXT=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
OBS=(0,0,4,1,16,32,8,2,0)

def counts(h,k):
 x,y,z=k
 return z-1,x+y-h-1,h+1-y-2*z,h+1-x

@lru_cache(None)
def words(h,k):
 a,cd,f,g=counts(h,k)
 if min(a,cd,f,g)<0:return ()
 result=set()
 for c in range(cd+1):
  left=[a,c,cd-c,k[2],f,g]
  def recur(q,path):
   if not any(left):
    if OBS[q]:result.add((OBS[q],path))
    return
   for j,n in enumerate(left):
    if n:
     left[j]-=1;recur(NEXT[q][j],path+LETTERS[j]);left[j]+=1
  recur(0,'')
 return tuple(sorted(result))

def eligible(h,required):
 found=set()
 for z in range(1,(h+1)//2+1):
  for cd in range(h-2*z+2):
   for f in range(h-2*z+2-cd):
    g=h+1-2*z-cd-f
    key=(cd+2*z+f,cd+g,z)
    labels={sig for sig,_ in words(h,key)}
    if set(required).issubset(labels):
     assert key[0]+key[1]==h+1
     found.add(key)
 return found

def signed_steps(w):
 return tuple(step for letter in w for step in STEPS[letter])

def verify(path):
 cert=json.load(open(path,encoding='utf8'))
 assert cert['schema']=='EC49FEZ_DEPTHWISE_DISJOINT_GROUP_CERT_V1'
 assert cert['science_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
 assert cert['mixed']==8 and cert['late_high_set']=='4789'
 high={3,4,7,8,9}; pool={(3,1,1)}
 for h in (4,7,8,9):pool.update(eligible(h,(16,) if h==8 else (16,32)))
 assert len(pool)==44
 G=[]; valid_words=0; endpoint_checks=0
 for h in range(2,10):
  required=(1,8,16) if h==8 else ((16,32) if h in high else (1,2,4,8))
  for sig in required:
   available=set()
   for key in pool:
    for label,w in words(h,key):
     if label!=sig:continue
     assert len(w)==h
     assert counts(h,key)[0]==w.count('a')
     assert counts(h,key)[1]==w.count('c')+w.count('d')
     assert key[2]==w.count('e')
     assert counts(h,key)[2]==w.count('f') and counts(h,key)[3]==w.count('g')
     displacement=[0]*6
     for step in signed_steps(w):displacement[abs(step)-1]+=1 if step>0 else -1
     assert displacement==[2,0,0,0,0,0]
     available.add(w);endpoint_checks+=1
   assert available, (h,sig)
   G.append((h,sig,available))
 assert len(G)==len(cert['groups'])==23
 for i,(h,sig,W) in enumerate(G):
  assert cert['groups'][i]=={'h':h,'signature':sig}
  valid_words+=len(W)
 total=0; checked=0
 assert len(cert['proof'])==20
 for d,record in enumerate(cert['proof'],1):
  selected=record['group_indices']
  assert record['depth']==d and len(selected)==len(set(selected))
  seen={}
  for index in selected:
   assert isinstance(index,int) and 0<=index<23
   for w in G[index][2]:
    s=signed_steps(w)
    assert len(s)>=d
    p=s[:d]
    assert p not in seen or seen[p]==index,(d,index,seen.get(p),p)
    seen[p]=index;checked+=1
  total+=len(selected)
 assert cert['lower_bound']==total==94
 return {'status':'EXACT_INTEGER_PASS','native_cost_lower_bound':94,'pool_keys':len(pool),
         'groups':len(G),'pooled_group_words':valid_words,'endpoint_checks':endpoint_checks,
         'layers':len(cert['proof']),'selected_group_word_prefix_checks':checked}
if __name__=='__main__':
 print(json.dumps(verify(sys.argv[1] if len(sys.argv)>1 else 'EXACT_DISJOINT_H8_4789.json'),indent=2))
