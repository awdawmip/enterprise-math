#!/usr/bin/env python3
"""EC49DO native signed-X6 finite rational rank: exhaustive sufficient-state DP.
Run: python VERIFY_EC49DO_PORTABLE.py (standard library only).
"""
from itertools import product
from fractions import Fraction
import json

OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3)}
WEIGHTS={
 'unequal_first_two':((2,3,1,2,3,4),(5,7,3,5,7,9)),
 'equal_first_two_nonconstant':((2,2,5,2,2,2),(5,5,11,5,5,5)),
 'all_equal':((2,)*6,(5,)*6),
}

def compositions(total,k):
 if k==1:yield (total,)
 else:
  for j in range(total+1):
   for tail in compositions(total-j,k-1):yield (j,)+tail

def label_update(A,B,last,s):
 return (int(A or (last==1 and s==2)),int(B or (last==2 and s==1)),
         1 if s==1 else (2 if s==2 else 0))

def compressed_prefixes(n):
 assert n>=2 and n%2==0
 out={};m=(n-2)//2
 for pos in compositions(m,6):
  neg=list(pos);neg[0]+=2;neg=tuple(neg)
  frontier={(pos,neg,0,0,0)}
  for _ in range(n):
   nextstates=set()
   for (pr,nr,A,B,last) in frontier:
    for i in range(6):
     if pr[i]:
      cp=list(pr);cp[i]-=1
      x,y,L=label_update(A,B,last,i+1)
      nextstates.add((tuple(cp),nr,x,y,L))
     if nr[i]:
      cn=list(nr);cn[i]-=1
      x,y,L=label_update(A,B,last,-i-1)
      nextstates.add((pr,tuple(cn),x,y,L))
   frontier=nextstates
  for pr,nr,A,B,last in frontier:
   assert not any(pr) and not any(nr)
   
   out[(pos,A,B,last)]=True
 return out

def rank_over_Q(rows):
 basis={}
 for row in rows:
  v=list(map(Fraction,row))
  for p,b in sorted(basis.items()):
   q=v[p]
   if q:v=[z-q*t for z,t in zip(v,b)]
  p=next((j for j,z in enumerate(v) if z),None)
  if p is not None:
   q=v[p];basis[p]=[z/q for z in v]
 return len(basis)

def history_coords(A,B,last,case):
 pa=int(not A and last==1);pb=int(not B and last==2)
 if case=='h2':return (1,A,B,pa,pb)
 return (int(not A and not B),int(not A and B),int(A and not B),int(A and B),pa,pb)

def label_signature(A,B,last,word):
 for op in word:
  for s in OPS[op]:A,B,last=label_update(A,B,last,s)
 return (A,B)

def future_words(h):
 result=[]
 for w in product(OPS,repeat=h):
  a=sum(w.count(k)*v for k,v in (('e',2),('a',-2)))
  b=-2*w.count('b')
  if (a,b)==(2,0):result.append(w)
 return result

def check_future_basis():
 states=list(product((0,1),(0,1),(0,1,2)))
 for case,hs,r in [('h2',[2],5),('h3',[3],6),('cum1_2',[1,2],6)]:
  words=[w for h in hs for w in future_words(h)]
  assert len(words)==({'h2':4,'h3':15,'cum1_2':5}[case])
  sig=[]
  for A,B,L in states:
   sig.append([int(label_signature(A,B,L,w)==state)
               for w in words for state in ((0,0),(0,1),(1,0),(1,1))])
  assert rank_over_Q(sig)==r
  # Equivalence to the five/six canonical history features used below.
  features=[history_coords(A,B,L,case) for A,B,L in states]
  assert rank_over_Q(features)==r
  assert rank_over_Q([s+list(f) for s,f in zip(sig,features)])==r


def main():
 check_future_basis()
 summary={};ranktables={}
 for n in (2,4,6,8,10,12):
  states=compressed_prefixes(n)
  summary[str(n)]=len(states)
  for key,(x,y) in WEIGHTS.items():
   table={}
   for case in ('h2','h3','cum1_2'):
    rows=[]
    for pos,A,B,last in states:
     wx=wy=1
     for i,e in enumerate(pos):wx*=x[i]**e;wy*=y[i]**e
     z=history_coords(A,B,last,case)
     rows.append(tuple(wx*q for q in z)+tuple(wy*q for q in z)+z)
    table[case]=rank_over_Q(rows)
   ranktables[f'{key}_n{n}']=table
  print('n=',n,'compressed states=',len(states),flush=True)
 wanted={
 'unequal_first_two':[(1,1,1),(4,4,4),(9,9,9),(13,15,15),(15,18,18),(15,18,18)],
 'equal_first_two_nonconstant':[(1,1,1),(4,4,4),(9,9,9),(13,14,14),(15,17,17),(15,18,18)],
 'all_equal':[(1,1,1),(3,3,3),(5,5,5),(5,6,6),(5,6,6),(5,6,6)],
 }
 for family,expected in wanted.items():
  for i,n in enumerate((2,4,6,8,10,12)):
   got=tuple(ranktables[f'{family}_n{n}'][k] for k in ('h2','h3','cum1_2'))
   assert got==expected[i],(family,n,got,expected[i])
 print(json.dumps({'status':'PASS','compressed_count':summary,'ranks':ranktables},ensure_ascii=False,sort_keys=True))

if __name__=='__main__':main()
