"""Finite checks of the symbolic T_{17,2} refinement induction.
Only the seed has numeric primes. New labels assert Bang existence of an exact
order prime; they are not numeric prime certificates.
"""
from hashlib import sha256
from math import gcd,lcm
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
PATTERNS={'5':[(2,0,2),(3,0,3),(4,1,1),(6,5,11),(12,7,7)],
 '6':[(2,0,2),(3,0,15),(4,1,1),(8,3,11),(12,7,7),(24,23,23)]}

def build(word,seed,H):
 rows=[dict(r) for r in seed];oldorders={r['ord2'] for r in rows};stages=[]
 for level,kind in enumerate(word):
  if level==0:parent=next(r for r in rows if r['q']==37441)
  else:parent=max(rows,key=lambda r:r['period_u'])
  d=parent['period_u'];c=parent['phase_u'];w=parent['private_u'];L=lcm(105,*(r['period_u'] for r in rows))
  assert L==7*d
  pattern=PATTERNS[kind];R=max(m for m,c,v in pattern);assert gcd(7,R)==1
  v0=(w-c)//d;assert (w-c)%d==0
  new=[]
  for m,b,priv in pattern:
   order=2*d*m;assert order>max(oldorders) and order>420 and order>6
   # The comparison is against pre-stage orders; new orders are distinct by m.
   t=((priv-v0)*pow(7,-1,R))%R
   new.append({'q':f'Bang_exact_order_{order}','ord2':order,'period_u':d*m,'phase_u':(c+d*b)%(d*m),'private_u':w+L*t,'primitive_prime_is_symbolic':True})
  assert len({r['ord2'] for r in new})==len(new)
  oldorders.update(r['ord2'] for r in new)
  rows=[r for r in rows if r is not parent]+new
  assert lcm(105,*(r['period_u'] for r in rows))==7*R*d
  for i,r in enumerate(rows):
   u=r['private_u'];assert u%105 in H
   assert [j for j,s in enumerate(rows) if u%s['period_u']==s['phase_u']]==[i]
   assert r['ord2']//gcd(r['ord2'],210)>2
  stages.append({'kind':kind,'parent_period_u':d,'parent_phase_u':c,'parent_private_u':w,'new_max_period_u':R*d,'new_orders':[r['ord2'] for r in new]})
 h=word.count('5');j=word.count('6');assert len(rows)==33+4*h+5*j
 return {'word':word,'h':h,'j':j,'delta_P':33+4*h+5*j,'tau':53+4*h+5*j,'rows':rows,'stages':stages,'private_witnesses_verified':True}

def main():
 raw=(HERE/'m2_extension_certificate.json').read_bytes();cert=json.loads(raw)
 rows=cert['rows'];H=set(cert['H_u']);old=[w for w in cert['private_witnesses'] if w['type']=='old_P']
 for p,pattern in PATTERNS.items():
  R=max(m for m,b,w in pattern)
  assert all(any(n%m==b for m,b,w in pattern) for n in range(R))
  for i,(_,_,w) in enumerate(pattern):assert [j for j,(m,b,_) in enumerate(pattern) if w%m==b]==[i]
 words=['','5','6','55','56','65','66','5566','6655','565656']
 skels=[]
 for word in words:
  skel=build(word,rows,H)
  for w in old:
   assert all((w['n']-2*r['phase_u'])%r['ord2'] for r in skel['rows'])
  skel['all_old_private_odd_witnesses_preserved']=True;skels.append(skel)
 out={'schema':'enterprise-math.riesel-T17m2-refinement.v1','numeric_seed_sha256':sha256(raw).hexdigest(),
 'theorem':'For every h,j>=0 there are infinitely many a in the same P observer class, divisible by T_{17,2}, with delta_P=33+4h+5j and tau=53+4h+5j.',
 'cofinite_delta_threshold':45,'cofinite_total_threshold':65,
 'symbolic_new_primes_source':'Bang primitive prime divisor theorem, t>6; FFK2008 Lemma2',
 'skeletons':skels,'status':'finite checks of a written induction; symbolic prime labels are not numeric primality certificates'}
 (HERE/'m2_refinement_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'seed_delta':33,'seed_tau':53,'cofinite_delta':45,'symbolic_words_checked':words}))
if __name__=='__main__':main()
