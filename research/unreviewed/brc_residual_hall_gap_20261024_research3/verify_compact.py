#!/usr/bin/env python3
"""Finite exact certificate for the BRC residual-freezing gap (unreviewed)."""
from functools import lru_cache
from fractions import Fraction
import json
Q=((1,665,1,333),(333,333,1,333),(1,1,1,997))
E=((0,1),(1,2),(1,3),(2,3)); DEG=(1,3,2,2)
T=((690,684,676,661,635,588,503,354,111),
(682,670,649,613,546,427,226,0,0),(661,632,580,486,323,61,0,0,0),
(608,534,403,185,0,0,0,0,0),(467,289,8,0,0,0,0,0,0),
(140,0,0,0,0,0,0,0,0)) + ((1,0,0,0,0,0,0,0,0),)*10
BE=tuple(tuple(q[i]+q[j] for i,j in E) for q in Q)
PE=tuple(tuple(tuple(b**n for n in range(692)) for b in v) for v in BE)
PV=tuple(tuple(tuple(b**n for n in range(692)) for b in v) for v in Q)
def inc(c,k):
 v=list(c);v[k]+=1;return tuple(v)
@lru_cache(None)
def num(c):
 return sum(PE[0][j][c[0]]*PE[1][j][c[1]]*PE[2][j][c[2]] for j in range(4))-sum(DEG[i]*PV[0][i][c[0]]*PV[1][i][c[1]]*PV[2][i][c[2]] for i in range(4))
def delta(c):return Fraction(0) if sum(c)<2 else Fraction(num(c),1000**sum(c))
@lru_cache(None)
def sign(c,k):
 z=num(inc(c,k))-1000*num(c);return (z>0)-(z<0)
def cuts(c):
 v=[PV[0][i][c[0]]*PV[1][i][c[1]]*PV[2][i][c[2]] for i in range(4)]
 e=[PE[0][j][c[0]]*PE[1][j][c[1]]*PE[2][j][c[2]] for j in range(4)]
 for k,q in enumerate(Q):
  d=[DEG[i]*(1000-q[i])*v[i] for i in range(4)]
  cap=[(1000-q[i]-q[j])*e[t] for t,(i,j) in enumerate(E)]
  for mask in range(1,16):
   yield k,mask,sum(cap[t] for t,(i,j) in enumerate(E) if mask&((1<<i)|(1<<j)))-sum(d[i] for i in range(4) if mask&(1<<i))
@lru_cache(None)
def H(c):return all(x>=0 for _,_,x in cuts(c))
assert sum(map(sum,T))==14102
for a in range(16):
 for b in range(9):
  t=T[a][b];assert H((a,b,t))
  if t:assert not H((a,b,t-1))
assert all(H(c) for c in ((16,0,0),(0,9,0),(0,0,690)))
F0={(a,b,k) for a in range(16) for b in range(9) for k in range(T[a][b])}
F={c for c in F0 if sum(c)>=2};assert len(F)==14098
maxima=sorted(c for c in F if all(inc(c,k) not in F0 for k in range(3)))
assert len(maxima)==31 and all(any(sign(c,k)>0 for k in range(3)) for c in maxima)
# Reachability of an internal negative edge; order by decreasing total length.
unsafe={}
for c in sorted(F,key=lambda c:(sum(c),c),reverse=True):
 unsafe[c]=any(inc(c,k) in F and (sign(c,k)<0 or unsafe[inc(c,k)]) for k in range(3))
assert sum(unsafe.values())==14067
assert sorted(c for c in F if not unsafe[c])==maxima
# Minimum attainable prefix maximum, among every ordered history with counts c.
peak={}
for c in sorted(F,key=lambda c:(sum(c),c)):
 predecessors=[]
 for k in range(3):
  if c[k]:
   p=list(c);p[k]-=1;predecessors.append(peak.get(tuple(p),Fraction(0)))
 peak[c]=max(delta(c),min(predecessors))
special=sorted(c for c in maxima if peak[c]==delta(c))
assert special==[(4,0,466),(4,1,288),(4,2,7),(5,0,139)]
word='3333333220000';c=(0,0,0);vals=[];masks=[1]+[0]*15
for ch in word:
 k=(0,2,3).index(int(ch));c=inc(c,k);vals.append(delta(c))
 nxt=[0]*16
 for mask,m in enumerate(masks):
  for i in range(4):nxt[mask|(1<<i)]+=m*Q[k][i]
 masks=nxt
 assert Fraction(sum(masks[(1<<i)|(1<<j)] for i,j in E),sum(masks))==vals[-1]
assert c==(4,2,7) and vals[-1]>max(vals[:-1])
assert not H(c) and all(H(inc(c,k)) for k in range(3))
assert [sign(c,k) for k in range(3)]==[1,-1,-1]
neg=[(k,m,x) for k,m,x in cuts(c) if x<0]
assert any((k,m,x)==(0,8,-1575304155146108101612691573430824142) for k,m,x in neg)
mins=[min(x for _,_,x in cuts(inc(c,k))) for k in range(3)]
assert mins==[2484711903995635042822401,2484711903995598264489549,7461597309296090884353]
print(json.dumps({'result':'PASS','hall_threshold_columns':144,'hall_fail_counts_n_ge_2':len(F),'maximal_fail_states':len(maxima),'nonmax_negative_reachable':sum(unsafe.values()),'special_record_states':[list(x) for x in special],'shortest_witness':word,'shortest_length':len(word),'witness_terminal_delta_numerator':str(num(c)),'witness_terminal_delta_denominator':'1'+'0'*(3*len(word)),'witness_neg_cut_action0_subset8':str(neg[0][2]),'successor_min_hall_margins':[str(x) for x in mins]},ensure_ascii=False,sort_keys=True))
