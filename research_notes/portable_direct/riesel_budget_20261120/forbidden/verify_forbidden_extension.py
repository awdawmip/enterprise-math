"""Exact certificate: old P observer class, T_{11,1}|a, finite cover, delta_P=11.
Search output is not a proof dependency. Prime and exact-order checks are finite.
"""
from __future__ import annotations
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
from math import gcd,isqrt,lcm,prod
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
BASE_REL=Path('research_notes/portable_direct/riesel_mixed_20261119/certificate.json')
ROOT=next(p for p in HERE.parents if (p/BASE_REL).is_file())
BASE=ROOT/BASE_REL
SOURCEDIR=next(p for p in (ROOT/'src',ROOT/'vendor_src')
              if (p/'enterprise_math/brc_transport.py').is_file())
ROWS=[
 (13,12,6,0,6),(19,18,9,1,10),(73,9,9,7,16),
 (37,36,18,3,3),(109,36,18,15,15),(61,60,30,1,31),
 (433,72,36,9,9),(38737,72,36,27,63),
 (631,45,45,4,49),(23311,45,45,40,85),(181,180,90,76,76)]

def prime(n):
 return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def strip(v,ps):
 removed={}
 for p in sorted(ps):
  k=0
  while v%p==0:v//=p;k+=1
  if k:removed[str(p)]=k
 return v,removed

def blob(data):return sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def crt(a,m,b,q):
 assert gcd(m,q)==1
 return a+m*((b-a)*pow(m,-1,q)%q),m*q

def main():
 sys.set_int_max_str_digits(0)
 raw=BASE.read_bytes(); old=json.loads(raw);base=old['optimized']
 astar=int(base['a']);P=[r['p'] for r in base['rows']];M=prod(P)
 source_checks={}
 for name,expected in old['project_source_blobs'].items():
  observed=blob((SOURCEDIR/'enterprise_math'/name).read_bytes())
  assert observed==expected
  source_checks[name]={'expected':expected,'observed':observed,'match':True}
 rows=[dict(zip(['q','ord2','period_u','phase_u','private_u'],r)) for r in ROWS]
 Q=[r['q'] for r in rows];assert len(set(Q))==11 and not set(P)&set(Q)
 H=[u for u in range(105) if all((astar*astar*pow(2,2*u,p)-1)%p for p in P)]
 assert len(H)==36
 # Revalidate short hole period against the full old residual period.
 oldperiod=lcm(*(r['order'] for r in base['rows']))
 assert oldperiod==6720
 for n in range(oldperiod):
  unhit=all((astar*astar*pow(2,n,p)-1)%p for p in P)
  assert unhit==(n%2==0 and (n//2)%105 in H)
 for r in rows:
  q,o,d,c,w=(r[k] for k in ['q','ord2','period_u','phase_u','private_u'])
  assert prime(q) and pow(2,o,q)==1
  assert all(pow(2,j,q)!=1 for j in range(1,o))
  assert d==o//gcd(o,2)
  r['relative_order_R']=o//gcd(o,210)
  assert r['relative_order_R']>1 and q>11
  r['root_mod_q']=pow(pow(2,c,q),-1,q)
  assert w%105 in H
  assert [s['q'] for s in rows if w%s['period_u']==s['phase_u']]==[q]
 period_u=lcm(105,*(r['period_u'] for r in rows));assert period_u==1260
 assert all(u%105 not in H or any(u%r['period_u']==r['phase_u'] for r in rows) for u in range(period_u))
 # This is the actual v4 T_{11,1}, not merely a squarefree subset.
 T1,removed_T1=strip((1<<210)-1,set(P))
 U=prod(q for q in range(3,12) if prime(q) and q not in P)
 T_Bm=lcm(T1,U)
 assert T_Bm==5*T1
 exponents=[2*r['private_u'] for r in rows]
 diffs=sorted({abs(i-j) for i,j in combinations(exponents,2)})
 D=lcm(*((1<<d)-1 for d in diffs))
 E,removed_D=strip(D,set(P)|set(Q))
 T=lcm(T_Bm,E)
 b=astar;K=2*M
 for r in rows:b,K=crt(b,K,r['root_mod_q'],r['q'])
 assert gcd(T,K)==1
 a=T*(b*pow(T,-1,K)%K)
 while a<=max(P+Q):a+=T*K
 assert a%(2*M)==astar and a%T_Bm==0 and a%T==0
 assert a%3==0 and a%5==0 and a%11==0 and a%2==1
 # Actual project-native scalar positive BRC trajectory.
 sys.path.insert(0,str(SOURCEDIR))
 from enterprise_math.brc_transport import Affine,EffectHistogram
 step=EffectHistogram.from_terms(1,[(1,Affine(((2,),),(1,)),1)])
 twice=step.then(step)
 assert twice.entries==((Fraction(1),Affine(((4,),),(3,)),1),)
 def advance(e,x):
  (point,weights),=e.evaluate((x,)).items()
  assert weights.entries==((Fraction(1),1),)
  assert point[0].denominator==1
  return int(point[0])
 assert advance(step,-1)==-1 and advance(twice,-1)==-1
 native={};x=a*a-1
 for n in range(1,max(exponents)+1):
  x=advance(step,x)
  if n in exponents:
   assert x==(a*a<<n)-1
   native[n]=x
 gcd_checks=[]
 for n1,n2 in combinations(exponents,2):
  g=gcd(native[n1],native[n2]);assert g==1
  gcd_checks.append({'n1':n1,'n2':n2,'gcd':g})
 for r in rows:
  val=native[2*r['private_u']]
  assert all(val%p for p in P)
  assert [q for q in Q if val%q==0]==[r['q']]
 full_period=lcm(oldperiod,*(r['ord2'] for r in rows))
 assert full_period==20160
 for n in range(full_period):
  assert any((a*a*pow(2,n,p)-1)%p==0 for p in P+Q)
 assert 2*a*a-1>max(P+Q)
 cert={
  'schema':'enterprise-math.riesel-finite-forbidden-extension.v1',
  'researcher_id':'EM-DIRECT-970E1C','research_activity_id':'RA-D2EC212845B63844081F9A14',
  'status':'author derivation and exact finite verification; not independent project Review',
  'base_certificate_sha256':sha256(raw).hexdigest(),
  'project_source_commit':old['project_source_commit'],'project_source_blob_checks':source_checks,
  'a_star':str(astar),'P':P,'M':str(M),'rows':rows,'H_u':H,
  'old_full_residual_period':oldperiod,'hole_period_u':105,'cover_period_u':period_u,
  'full_cover_period_n':full_period,'B':11,'m':1,
  'T1':str(T1),'T1_removed_valuations':removed_T1,'U_B':str(U),'T_Bm':str(T_Bm),
  'D':str(D),'E':str(E),'D_removed_valuations':removed_D,'T':str(T),
  'crt_b':str(b),'crt_K':str(K),'root_a':str(a),'root_progression_modulus':str(T*K),
  'root_digits':len(str(a)),'square_digits':len(str(a*a)),
  'private_terms':[{'n':n,'value':str(native[n]),'decimal_sha256':sha256(str(native[n]).encode()).hexdigest()} for n in exponents],
  'pairwise_gcd_checks':gcd_checks,'exact_minimum_P_outside_cover_primes':11,
  'total_cover_size_bound':31,
  'native_brc':{'module':'enterprise_math.brc_transport','one_step':'x -> 2x+1','even_step':'x -> 4x+3','positive_singleton_weight':1,'multiplicity':1},
  'theorem':'Infinitely many a congruent to a_star mod 2M and divisible by T_{11,1} have delta_P(a)=11<infinity.',
  'not_claimed':['arbitrary B,m admits finite cover','arbitrary forbidden finite set admits finite cover','global optimality of the MILP search dictionary','independent project Review']}
 out=HERE/'forbidden_extension_certificate.json';out.write_text(json.dumps(cert,indent=2)+'\n')
 print(json.dumps({'root_digits':len(str(a)),'square_digits':len(str(a*a)),'T_Bm_digits':len(str(T_Bm)),'exact_delta_P':11,'gcd_checks':len(gcd_checks),'full_period_n':full_period,'output':str(out)}))

if __name__=='__main__':main()
