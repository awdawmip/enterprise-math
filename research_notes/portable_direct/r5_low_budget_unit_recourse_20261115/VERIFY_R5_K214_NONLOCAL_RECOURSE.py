#!/usr/bin/env python3
"""Deterministic discovery and exact certificate for K214 nonlocal R5 recourse.
Uses the independently saved one-swap verifier for the frozen data and path DP.
Standard library only; prints complete new/old 214-center witnesses.
"""
import json,random
from collections import Counter
from VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE import frozen,close,graph,paths_dp,INF

SEED=20261115;SAMPLES=256;K=214

def cost(z,S):
 ds=[min(abs(z[t]-z[j]) for j in S) for t in range(len(z))]
 return max(ds),sum(ds)

def new_optimal_sample(dp,inc,tail,gen):
 out,C,D,J=dp;j=gen.choice([j for j in range(len(tail)) if C[K-1][j]+tail[j]==J[K-1]])
 S=[j]
 for t in range(K-1,0,-1):
  j=gen.choice([i for i,w in inc[j] if C[t-1][i]+w==C[t][j]])
  S.append(j)
 return sorted(S)

def old_best_overlap(S,graph_old,dp_old,reconstruct=False):
 inc,_,pref,tail=graph_old;out,C,D,J=dp_old;best=J[K-1]
 present=set(S);n=len(C[0]);M=[-1]*n;parents=[]
 for j in range(n):
  if C[0][j]<INF and C[0][j]+D[K-1][j]==best:M[j]=int(j in present)
 for t in range(1,K):
  next_M=[-1]*n;parent=[-1]*n
  for j in range(n):
   if C[t][j]+D[K-1-t][j]!=best:continue
   options=[(M[i],i) for i,w in inc[j] if M[i]>=0 and C[t-1][i]+w==C[t][j]]
   if options:
    v,i=max(options);next_M[j]=v+int(j in present);parent[j]=i
  M=next_M
  if reconstruct:parents.append(parent)
 score,j=max((M[j],j) for j in range(n) if M[j]>=0 and C[K-1][j]+tail[j]==best)
 if not reconstruct:return score,None
 T=[j]
 for parent in reversed(parents):
  j=parent[j];assert j>=0;T.append(j)
 return score,sorted(T)

def main():
 x,cuts=frozen();old_graph=graph(x);old_dp=paths_dp(x,K);assert old_dp[-1][K-1]==1064
 gen=random.Random(SEED);rows=[]
 for bit in (3,8,9,10):
  y=close(x,cuts,1<<bit);new_graph=graph(y);dp=paths_dp(y,K)
  assert dp[-1][K-1]==1064
  hist=Counter();winner=(-1,None)
  for _ in range(SAMPLES):
   S=new_optimal_sample(dp,new_graph[0],new_graph[3],gen)
   score,_=old_best_overlap(S,old_graph,old_dp)
   r=K-score;hist[r]+=1
   if r>winner[0]:winner=r,S
  r,S=winner;match,T=old_best_overlap(S,old_graph,old_dp,reconstruct=True)
  assert r==K-match and cost(y,S)==(2,1064) and cost(x,T)==(2,1064)
  assert len(S)==len(T)==K and len(set(S)-set(T))==r
  rows.append({'cut':bit,'cut_start_index':cuts[bit], 'K':K,
               'new_optimal_centers':S,'old_nearest_optimal_centers':T,
               'replace_out':sorted(set(S)-set(T)),
               'replace_in':sorted(set(T)-set(S)),
               'old_max_overlap':match,'exact_min_swaps':r,
               'sample_histogram':{str(v):hist[v] for v in sorted(hist)}})
 assert [row['exact_min_swaps'] for row in rows]==[3,7,7,4]
 print(json.dumps({'status':'PASS_EXACT_R5_K214_NONLOCAL_RECOURSE',
  'scientific_input_commit':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
  'K':K,'J_old_equals_J_new':1064,'seed':SEED,'samples_per_cut':SAMPLES,
  'result_kind':'exact witness-specific minimum and universal lower bound',
  'witnesses':rows,'independent_review':'NOT_REVIEWED'},
  sort_keys=True,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
