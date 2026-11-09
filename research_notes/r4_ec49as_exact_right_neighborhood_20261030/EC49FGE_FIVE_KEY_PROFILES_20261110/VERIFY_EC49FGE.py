#!/usr/bin/env python3
"""Independent standard-library exhaustive full-key cover and native witness audit."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
import json
OPS = 'acdefg'
T = ((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG = (0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
BUCKET={1:(2,3,2,3,3,2,4,3,4),2:(2,2,2,3,3,2,2,3,4),4:(1,1,4,1,3,4,4,3,4),8:(1,1,1,1,1,4,4,3,4),16:(0,0,2,1,3,2,2,3,4),32:(0,1,0,1,1,2,4,3,4)}
NEED={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
LABELS=[(h,s) for h in NEED for s in NEED[h]]
W={2:{16:'fe',32:'ge'},3:{16:'feg',32:'gef'},4:{1:'gefd',2:'fegd',4:'fegc',8:'gefc'},5:{16:'feggf',32:'geffg'},6:{1:'gefddd',2:'fegddd',4:'fegccc',8:'gefccc'},7:{1:'gefddgf',2:'fegddgf',4:'fegccfg',8:'gefccfg'},8:{1:'geffgfgd',2:'feggffgd',4:'feggffgc',8:'geffgfgc'},9:{16:'feggffgfg',32:'geffgfggf'}}
EXPECTED_FIVE={(3,0,1),(2,1,1),(3,1,1),(4,2,1),(6,4,1)}

def obs(w):
 q=0
 for c in w:q=T[q][OPS.index(c)]
 return SIG[q]
def native(w):return tuple(x for c in w for x in STEPS[c])
def full_key(w):
 p=native(w);return tuple(p.count(x) for x in (1,2,3))
def exact_rank(M):
 A=[[Fraction(x) for x in r] for r in M];m=len(A);n=len(A[0]);r=0
 for j in range(n):
  ip=next((i for i in range(r,m) if A[i][j]!=0),None)
  if ip is None:continue
  A[r],A[ip]=A[ip],A[r];d=A[r][j]
  for col in range(j,n):A[r][col]/=d
  for i in range(r+1,m):
   if A[i][j]:
    f=A[i][j]
    for col in range(j,n):A[i][col]-=f*A[r][col]
  r+=1
  if r==m:break
 return r

def exhaustive_key_cover():
 covers={};accepted=0
 for h in NEED:
  def go(n,q,x,y,z,e,a):
   nonlocal accepted
   if q==8:return
   if n==h:
    sig=SIG[q]
    if e==a+1 and sig in NEED[h]:
     k=(x,y,z); bit=1<<LABELS.index((h,sig));covers[k]=covers.get(k,0)|bit;accepted+=1
    return
   for i in range(6):
    c=OPS[i];p=STEPS[c]
    go(n+1,T[q][i],x+p.count(1),y+p.count(2),z+p.count(3),e+(c=='e'),a+(c=='a'))
  go(0,0,0,0,0,0,0)
 allmask=(1<<len(LABELS))-1
 forced=[k for k in covers if (covers[k] & 3)]
 assert set(forced)=={(3,0,1),(2,1,1)} and len(forced)==2
 base=covers[forced[0]]|covers[forced[1]]
 rest=[k for k in covers if k not in forced]
 for i,j in combinations(rest,2):assert (base|covers[i]|covers[j])!=allmask
 five=[tuple(sorted((*forced,*tri))) for tri in combinations(rest,3) if (base|covers[tri[0]]|covers[tri[1]]|covers[tri[2]])==allmask]
 assert len(five)==16,(len(five),five)
 assert tuple(sorted(EXPECTED_FIVE)) in five
 A={(3,3,1),(4,2,1),(5,1,1),(5,1,2)}
 B={(5,5,1),(6,4,1),(7,3,1),(7,3,2)}
 basekeys={(3,0,1),(2,1,1),(3,1,1)}
 assert {frozenset(t) for t in five}=={frozenset(basekeys|{a,b}) for a in A for b in B}
 return {'keys_examined':len(covers),'valid_words_examined':accepted,'demand_count':len(LABELS),'min_raw_complete_keys':5,'exact_five_key_profiles':len(five),'five_key_profiles':[list(map(list,t)) for t in sorted(five)]}

def witness_audit():
 prefixes=set();ks=set()
 for h,d in W.items():
  assert set(d)==set(NEED[h]);labs=NEED[h]
  A=[[int(BUCKET[s][i]==b) for s in labs for b in range(5)] for i in range(9)]
  assert exact_rank(A)==9,(h,'rank')
  for sig,w in d.items():
   assert len(w)==h and obs(w)==sig,(h,sig,w)
   assert w.count('e')==w.count('a')+1
   steps=native(w)
   assert tuple(steps.count(j)-steps.count(-j) for j in (1,2,3))==(2,0,0)
   ks.add(full_key(w))
   prefixes.update(steps[:j] for j in range(1,len(steps)+1))
 assert ks==EXPECTED_FIVE,(ks,EXPECTED_FIVE)
 assert len(prefixes)==112,len(prefixes)
 return {'full_keys':sorted(map(list,ks)),'word_count':sum(map(len,W.values())),'native_edges':len(prefixes),'rational_rank_each_window':9,'witness':{f'{h}:{s}':w for h,d in W.items() for s,w in d.items()}}

if __name__=='__main__':
 result={'model':'FROZEN_ORIGINAL_H2_H9_24_SIGNATURES','frozen_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','cover':exhaustive_key_cover(),'witness':witness_audit()}
 with open('EXACT_REPORT_EC49FGE.json','w') as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
 print('EC49FGE_EXACT_ENUMERATION_PASS keys',result['cover']['keys_examined'],'profiles',result['cover']['exact_five_key_profiles'],'min_keys',result['cover']['min_raw_complete_keys'],'witness_native_edges',result['witness']['native_edges'])
