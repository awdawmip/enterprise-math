"""Exhaust all <=5-prime binary divisibility covers, using the CVE order bound.
Pure integer factorization, exact orders, 32-bit covering masks, and DFS.
No SAT/MILP package, heuristic infeasibility, or probabilistic primality is used.
"""
from collections import Counter
from hashlib import sha256
from math import gcd,isqrt,lcm,prod
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent

def factor_trial(n):
 out={};p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e+=1
  if e:out[p]=e
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out

def order2(q):
 x=1
 for d in range(1,q):
  x=x*2%q
  if x==1:return d
 raise AssertionError('prime order missing')

def main():
 t0=time.time();facts=[];primes=set()
 for d in range(1,17):
  val=(1<<d)-1;f=factor_trial(val);assert prod(p**e for p,e in f.items())==val
  facts.append({'d':d,'value':val,'factorization':{str(p):e for p,e in f.items()}});primes.update(f)
 group={}
 for q in sorted(primes):
  assert q>2 and not any(q%x==0 for x in range(2,isqrt(q)+1))
  d=order2(q);assert d<=16
  group.setdefault(d,[]).append(q)
 ds=sorted(group);caps=[len(group[d]) for d in ds]
 assert ds==[2,3,4,5,7,8,9,10,11,12,13,14,15,16]
 assert all(c==1 if d!=11 else c==2 for d,c in zip(ds,caps))
 N=32;FULL=(1<<N)-1
 masks=[[sum(1<<n for n in range(c,N,d)) for c in range(d)] for d in ds]
 slots0=5;initial_counts=sum(c<<(2*i) for i,c in enumerate(caps))
 stats=Counter();calls_by_depth=[0]*6;witness=None
 def search(covered,counts,left,path):
  nonlocal witness
  stats['calls']+=1
  calls_by_depth[5-left]+=1
  if covered==FULL:witness=list(path);return True
  if left==0:stats['no_slots']+=1;return False
  uncovered=FULL^covered
  first=(uncovered&-uncovered).bit_length()-1
  # In every successful completion, some available class covers `first`.
  # For each available modulus there is exactly one such phase. All are tried.
  # No memoization, density bound, or optimization-based pruning is used.
  for i,d in enumerate(ds):
   if (counts>>(2*i))&3:
    c=first%d;mask=masks[i][c]
    if search(covered|mask,counts-(1<<(2*i)),left-1,path+[(ds[i],c)]):return True
  stats['exhausted_states']+=1
  return False
 found=search(0,initial_counts,slots0,[])
 print(json.dumps({'found':found,'witness':witness,'stats':dict(stats),'calls_by_depth':calls_by_depth,'seconds':time.time()-t0}),flush=True)
 # A six-prime positive witness at k=509203.
 positive=[(3,2,0),(5,4,1),(7,3,2),(13,12,7),(17,8,7),(241,24,3)]
 period=lcm(*(d for q,d,c in positive));k=509203
 for q,d,c in positive:
  assert not any(q%x==0 for x in range(2,isqrt(q)+1))
  assert order2(q)==d and (k*pow(2,c,q)-1)%q==0
 assert period==24 and all(any(n%d==c for q,d,c in positive) for n in range(period))
 assert k%2==1 and 2*k-1>max(q for q,d,c in positive)
 cert={'schema':'enterprise-math.global-minimum-finite-riesel-cover.v1',
 'researcher_id':'EM-DIRECT-970E1C','research_activity_id':'RA-D2EC212845B63844081F9A14',
 'status':'author finite exhaustive verification; not independent project Review',
 'external_theorem':'Any t arithmetic progressions covering 2^t consecutive integers cover all integers (Crittenden-Vanden Eynden).',
 'order_bound_lemma':'In an inclusion-minimal s-prime covering, every base-2 order is at most 2^(s-1).',
 'maximum_cover_size_under_test':5,'maximum_relevant_order':16,'finite_window_length':N,
 'factorizations':facts,'prime_order_dictionary':[{'order':d,'primes':group[d],'capacity':len(group[d])} for d in ds],
 'phase_masks_hex':{str(d):[hex(mask) for mask in masks[i]] for i,d in enumerate(ds)},
 'exhaustive_search':{'found':found,'witness':witness,'stats':dict(stats),'calls_by_depth':calls_by_depth,'method':'unpruned integer first-uncovered-bit DFS with exact order multiplicities; no memoization or coverage-capacity pruning'},
 'six_prime_witness':{'k':k,'rows':[{'q':q,'ord2':d,'phase_n':c} for q,d,c in positive],'full_period':period,'proper_divisors':True},
 'conclusion':('Every finite prime divisibility cover of k*2^n-1 for positive odd k uses at least six primes, and k=509203 attains six.' if not found else 'A <=5 class cover was found; inspect the concrete witness.'),
 'not_claimed':['smallest Riesel coefficient','every Riesel number has a finite prime cover','literature priority','independent project Review']}
 out=HERE/'minimum_six_certificate.json';out.write_text(json.dumps(cert,indent=2)+'\n')
 assert not found,('Unexpected <=5 cover',witness)
 print(json.dumps({'minimum':6,'certificate':str(out),'seconds':time.time()-t0}))
if __name__=='__main__':main()
