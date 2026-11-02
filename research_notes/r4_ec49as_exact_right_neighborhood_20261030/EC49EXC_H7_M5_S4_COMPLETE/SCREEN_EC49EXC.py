#!/usr/bin/env python3
"""EC49EXC preliminary exact H5-prefix screen for H7 M5 S4 late-repeat.
Self-contained relative to pinned previous VERIFY_EC49ER.py, no new assumptions.
"""
from VERIFY_EC49ER import *
from collections import defaultdict, Counter
from itertools import product
import json, time

def screen():
 start=time.time();fs=fibers()
 t4=frozenset(signature(w) for w in BASE)
 P={h:tuple(sorted(p for p,words in fs[h].items() if essential(words)==t4)) for h in range(2,7)}
 # seven-letter enumeration for H7 only
 tab=defaultdict(set);counts7=0
 for tup in product(OPS,repeat=7):
  word=''.join(tup)
  if displacement(word)!=(2,0,0,0,0,0):continue
  counts7+=1
  s=signature(word)
  if s in t4:tab[poscount(word)].add(s)
 P[7]=tuple(sorted(p for p,ss in tab.items() if ss==t4))
 print('Pcounts', {h:len(p) for h,p in P.items()},'returning7',counts7,'s',round(time.time()-start,1),flush=True)
 # Only 3 distinct p at H5 horizon? full 7*13*22=2002 exact
 # For h2..h5, calculate exact min E for relevant H7 late repeat H5 prefix keys.
 p0=P[2][0]
 P5_inter=set(P[7]) & set(P[5]);P6_inter=set(P[7])&set(P[6])
 late=[]
 for p3,p4,p5,p6 in product(P[3],P[4],P[5],P[6]):
  seq=(p0,p3,p4,p5,p6)
  if len(set(seq))!=5:continue
  if p5 in P5_inter:late.append((3,(p3,p4,p5,p6),p5))
  if p6 in P6_inter:late.append((4,(p3,p4,p5,p6),p6))
 assert len(late)==4454,len(late)
 print('late cases',len(late),Counter(x[0] for x in late),'s',round(time.time()-start,1),flush=True)
 relevant=sorted({entry[1][:3] for entry in late})
 print('distinct H5 prefixes',len(relevant),flush=True)
 values={}
 for i,k in enumerate(relevant):
  values[k]=exact_trie_opt(fs,{3:k[0],4:k[1],5:k[2]})['E']
  if (i+1)%100==0:print('H5',i+1,'/',len(relevant),'elapsed',round(time.time()-start,1),flush=True)
 bins=Counter(values[entry[1][:3]] for entry in late)
 cut=Counter('certified_E>=80' if values[x[1][:3]]>=64 else 'requires_more' for x in late)
 report={'unit':'EC49EXC','method':'exact minimum E for each realized H5 key prefix; any H7 S4 terminal requires >=8 new native edges at h6 and h7','scope':'H7 M5 S4 schedules with one late-repeat pair h5,h7 or h6,h7','word_count_h7':counts7,'eligible_keys_by_h':{h:len(P[h]) for h in P},'late_pair_counts':dict(Counter(f'{x[0]+2},7' for x in late)), 'distinct_H5_key_prefixes':len(relevant),'H5_E_histogram_by_H7_schedule':dict(sorted(bins.items())),'H5_prefix_lower_bound_screen':dict(cut),'unresolved':[{'pair':(int(q[0]+2),7),'h3to6':[list(p) for p in q[1]],'p7':list(q[2]),'H5_exact_E':values[q[1][:3]]} for q in late if values[q[1][:3]]<64], 'executed_seconds':round(time.time()-start,2)}
 with open('EC49EXC_SCREENED.json','w') as out:json.dump(report,out,indent=2)
 print('SCREEN_REPORT',json.dumps({k:v for k,v in report.items() if k not in ('unresolved',)},ensure_ascii=False),flush=True)
 return report
if __name__=='__main__':screen()
