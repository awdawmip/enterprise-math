#!/usr/bin/env python3
"""Exactly count admissible BRC operation words using arbitrary-precision integers."""
from functools import cache
import json,sys
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
def count(h):
 @cache
 def solve(k,e,a,f,q):
  if 2*e+f>h or abs(e-a-1)>h-k:return 0
  if k==h:return int(e==a+1 and e>=1 and SIG[q] in (1,2,4,8))
  return sum(solve(k+1,e+(j==3),a+(j==0),f+(j==4),T[q][j]) for j in range(6))
 return {'h':h,'admissible_words':str(solve(0,0,0,0,0)),'states':solve.cache_info().currsize}
if __name__=='__main__':
 for h in map(int,sys.argv[1:]):print(json.dumps(count(h)))