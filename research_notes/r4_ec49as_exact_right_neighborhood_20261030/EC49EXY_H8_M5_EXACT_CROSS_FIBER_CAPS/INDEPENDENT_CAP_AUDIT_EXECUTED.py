#!/usr/bin/env python3
"""Independent exact cap recomputation by lexicographic two-set merge, no prefix trie."""
import sys,json,hashlib,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49EXJ_H8_M4_S6_GLOBAL_EXACT'))
from SCREEN_H5_EC49EXJ import words
src=json.loads((HERE/'EC49EXY_EXACT_CAPS.json').read_text())
F=src['family']; n=len(F)
S=[sorted(set(st for st,sig,operation in words(f['h'],tuple(f['key']),f['type']))) for f in F]
assert sum(len(x) for x in S)==163888

def lc(a,b):
 i=0
 for x,y in zip(a,b):
  if x!=y: break
  i+=1
 return i

def cap(A,B):
 i=j=0;best=0
 while i<len(A) and j<len(B):
  a=A[i];b=B[j]
  now=lc(a,b)
  if now>best:best=now
  if a<b:i+=1
  elif b<a:j+=1
  else:
   i+=1;j+=1
 return best
count=0;exceptions=[];t0=time.monotonic()
for i in range(n):
 for j in range(i+1,n):
  v=cap(S[i],S[j]);want=src['max_lcp_primitive_steps'][i][j]
  if v!=want:exceptions.append((i,j,v,want))
  count+=1
assert not exceptions,exceptions[:10]
out={'status':'PASS','algorithm':'independent_sorted_fiber_two_pointer_merge','compared_fiber_pairs':count,'frozen_eligible_words':sum(len(x) for x in S),'full_cap_matrix_match':True,'original_native_cap_table_sha256':hashlib.sha256((HERE/'EC49EXY_CAPS_TABLE.txt').read_bytes()).hexdigest(),'elapsed_seconds':round(time.monotonic()-t0,2)}
(HERE/'EC49EXY_INDEPENDENT_CAP_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
