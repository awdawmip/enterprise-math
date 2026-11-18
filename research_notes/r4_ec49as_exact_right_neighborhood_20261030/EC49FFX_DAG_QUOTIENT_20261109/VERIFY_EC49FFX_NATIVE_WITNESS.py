#!/usr/bin/env python3
"""Independently verify the original signed-native X6 BRC attaining family H2/Hh."""
from collections import Counter
OP='acdefg'
C={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
def check_one(word,h,sig):
 q=0
 for c in word:q=T[q][OP.index(c)]
 assert len(word)==h and SIG[q]==sig
 n=Counter(word);z=n['e'];x=h+1-n['g'];y=h+1-2*z-n['f']
 assert z==n['a']+1 and min(x,y,z)>0 and n['c']+n['d']==x+y-h-1
 steps=tuple(v for c in word for v in C[c]);counts=Counter(steps)
 assert tuple(counts[i]-counts[-i] for i in range(1,7))==(2,0,0,0,0,0)
 assert (counts[1],counts[2],counts[3])==(x,y,z)
 return (x,y,z),steps
def check(h):
 old={1:'de',2:'ed',4:'ce',8:'ec'}
 new={1:'gfe'+'g'*(h-4)+'d',2:'fe'+'g'*(h-3)+'d',4:'fe'+'g'*(h-3)+'c',8:'gfe'+'g'*(h-4)+'c'}
 prefixes=set();keys=set()
 for H,words in ((2,old),(h,new)):
  for sig,word in words.items():
   key,steps=check_one(word,H,sig);keys.add(key)
   for j in range(1,len(steps)+1):prefixes.add(steps[:j])
 assert keys=={(3,1,1),(4,h-2,1)}
 assert len(prefixes)==4*h+42
 print(h,len(prefixes),'PASS')
if __name__=='__main__':
 for h in range(14,31):check(h)