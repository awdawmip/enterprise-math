"""Exact T_{17,2} completion; 33 added primes; exact delta_P=33 and tau=53.
The fixed finite row file is verified; no optimizer status is used as a proof.
Large integers are serialized as hex, and term fingerprints use unsigned big-endian bytes.
"""
from fractions import Fraction
from hashlib import sha1,sha256
from itertools import combinations
from math import gcd,isqrt,lcm,prod
from pathlib import Path
import json,sys,time
HERE=Path(__file__).resolve().parent
BASE_REL=Path('research_notes/portable_direct/riesel_mixed_20261119/certificate.json')
ROOT=next(p for p in HERE.parents if (p/BASE_REL).is_file())
BASE=ROOT/BASE_REL
SRC=next(p for p in (ROOT/'src',ROOT/'vendor_src')
         if (p/'enterprise_math/brc_transport.py').is_file())

def prime(p):return p>=2 and all(p%d for d in range(2,isqrt(p)+1))
def strip(x,ps):
 removed={}
 for p in sorted(ps):
  e=0
  while x%p==0:x//=p;e+=1
  if e:removed[str(p)]=e
 return x,removed
def crt(a,m,b,q):
 assert gcd(m,q)==1
 return a+m*((b-a)*pow(m,-1,q)%q),m*q
def digest(x):
 return {'bit_length':x.bit_length(),'unsigned_big_endian_sha256':sha256(x.to_bytes((x.bit_length()+7)//8,'big')).hexdigest()}
def blob(x):return sha1(b'blob '+str(len(x)).encode()+b'\0'+x).hexdigest()

def main():
 sys.set_int_max_str_digits(0);start=time.time()
 baseraw=BASE.read_bytes();old=json.loads(baseraw);b=old['optimized']
 astar=int(b['a']);oldrows=b['rows'];P=[r['p'] for r in oldrows];M=prod(P)
 source_checks={}
 for name,expected in old['project_source_blobs'].items():
  observed=blob((SRC/'enterprise_math'/name).read_bytes());assert observed==expected
  source_checks[name]={'expected':expected,'observed':observed,'matches':True}
 raw=(HERE/'m2_irredundant_rows.json').read_bytes();seed=json.loads(raw)
 Qrows=seed['rows'];Q=[r['q'] for r in Qrows]
 assert len(Q)==33 and len(set(Q))==33 and not set(Q)&set(P)
 H=[u for u in range(105) if all((astar*astar*pow(2,2*u,p)-1)%p for p in P)]
 assert len(H)==36
 for r in oldrows:
  assert prime(r['p']) and pow(2,r['order'],r['p'])==1
  assert all(pow(2,j,r['p'])!=1 for j in range(1,r['order']))
  assert (astar*astar*pow(2,r['exponent_phase'],r['p'])-1)%r['p']==0
 for r in Qrows:
  q,o,d,c,w=(r[k] for k in ['q','ord2','period_u','phase_u','private_u'])
  assert prime(q) and pow(2,o,q)==1 and all(pow(2,j,q)!=1 for j in range(1,o))
  assert d==o//gcd(o,2)
  r['relative_order_R']=o//gcd(o,210)
  assert q>17 and r['relative_order_R']>2
  assert r['root_mod_q']==pow(pow(2,c,q),-1,q)
  assert w%105 in H and [s['q'] for s in Qrows if w%s['period_u']==s['phase_u']]==[q]
 Lu=lcm(105,*(r['period_u'] for r in Qrows));assert Lu==5040
 assert all(u%105 not in H or any(u%r['period_u']==r['phase_u'] for r in Qrows) for u in range(Lu))
 Ln=lcm(*(r['order'] for r in oldrows),*(r['ord2'] for r in Qrows));assert Ln==20160
 combined=[(r['p'],r['order'],r['exponent_phase']) for r in oldrows]+[(r['q'],r['ord2'],2*r['phase_u']%r['ord2']) for r in Qrows]
 for n in range(Ln):
  assert any(n%o==c for q,o,c in combined)
  oldhole=not any(n%r['order']==r['exponent_phase'] for r in oldrows)
  assert oldhole==(n%2==0 and (n//2)%105 in H)
 oldprivate={p:None for p in P}
 for n in range(1,Ln,2):
  hits=[q for q,o,c in combined if n%o==c]
  if len(hits)==1 and hits[0] in oldprivate and oldprivate[hits[0]] is None:oldprivate[hits[0]]=n
 assert all(n is not None for n in oldprivate.values())
 witnesses=[{'q':p,'n':oldprivate[p],'type':'old_P'} for p in P]+[{'q':r['q'],'n':2*r['private_u'],'type':'new_Q'} for r in Qrows]
 ns=[r['n'] for r in witnesses];assert len(set(ns))==53
 for w in witnesses:assert [q for q,o,c in combined if w['n']%o==c]==[w['q']]
 # T_{17,2} uses lcm(R-1,R^2-1)=R^2-1, retaining every non-P prime power.
 R=1<<210;D2=lcm(R-1,R*R-1);assert D2==(1<<420)-1
 T2,removed_T2=strip(D2,set(P))
 U17=prod(q for q in range(3,18) if prime(q) and q not in P)
 T_Bm=lcm(T2,U17);assert T_Bm==T2
 diffs=sorted({abs(n-n2) for n,n2 in combinations(ns,2)})
 D=lcm(*((1<<d)-1 for d in diffs));E,removed_D=strip(D,set(P)|set(Q));T=lcm(E,T_Bm)
 c=astar;K=2*M
 for r in Qrows:c,K=crt(c,K,r['root_mod_q'],r['q'])
 assert gcd(K,T)==1
 a=T*(c*pow(T,-1,K)%K)
 assert a>max(P+Q) and a%(2*M)==astar and a%T==0 and a%T_Bm==0
 print(json.dumps({'stage':'root_constructed','root_bits':a.bit_length(),'D_bits':D.bit_length(),'private_count':len(ns),'max_n':max(ns),'seconds':time.time()-start}),flush=True)
 # Native single-register positive BRC generates each finite witness term.
 sys.path.insert(0,str(SRC))
 from enterprise_math.brc_transport import Affine,EffectHistogram
 step=EffectHistogram.from_terms(1,[(1,Affine(((2,),),(1,)),1)])
 assert step.then(step).entries==((Fraction(1),Affine(((4,),),(3,)),1),)
 def advance(x):
  (point,weights),=step.evaluate((x,)).items()
  assert weights.entries==((Fraction(1),1),) and point[0].denominator==1
  return int(point[0])
 assert advance(-1)==-1
 vals={};x=a*a-1;nset=set(ns)
 for n in range(1,max(ns)+1):
  x=advance(x)
  if n in nset:assert x==(a*a<<n)-1;vals[n]=x
 print(json.dumps({'stage':'native_terms_generated','seconds':time.time()-start}),flush=True)
 for w in witnesses:
  x=vals[w['n']];assert [q for q in P+Q if x%q==0]==[w['q']]
  assert x>w['q']>1;w.update(digest(x))
 gcdchecks=[]
 for i,j in combinations(ns,2):
  g=gcd(vals[i],vals[j]);assert g==1;gcdchecks.append({'n1':i,'n2':j,'gcd':g})
 for q,o,c0 in combined:assert (a*a*pow(2,c0,q)-1)%q==0
 assert 2*a*a-1>max(P+Q)
 root_digits=len(str(a));square_digits=len(str(a*a))
 cert={'schema':'enterprise-math.riesel-T17m2-finite-cover.v1',
 'researcher_id':'EM-DIRECT-970E1C','research_activity_id':'RA-D2EC212845B63844081F9A14',
 'status':'author derivation and exact finite verification; not independent project Review',
 'base_certificate_sha256':sha256(baseraw).hexdigest(),'row_input_sha256':sha256(raw).hexdigest(),
 'project_source_commit':old['project_source_commit'],'project_source_blob_checks':source_checks,
 'a_star':str(astar),'P':P,'M':str(M),'rows':Qrows,'H_u':H,
 'B':17,'m':2,'full_period_u':Lu,'full_period_n':Ln,'T_Bm':str(T_Bm),'U_B':str(U17),'T2_removed_valuations':removed_T2,
 'private_witnesses':witnesses,'witness_differences':diffs,'all_pairwise_gcd_checks':gcdchecks,
 'D_summary':digest(D),'E_summary':digest(E),'T_summary':digest(T),'D_removed_valuations':removed_D,
 'crt_b':str(c),'crt_K':str(K),'root_a_hex':hex(a),'root_progression_modulus_hex':hex(T*K),
 'root_summary':dict(digest(a),decimal_digits=root_digits),'square_summary':dict(digest(a*a),decimal_digits=square_digits),
 'exact_delta_P':33,'exact_total_tau':53,'native_brc_every_step_through_n':max(ns),
 'native_brc':{'one_step':'x -> 2x+1','even_step':'x -> 4x+3','state_dimension':1,'weight':1,'multiplicity':1},
 'theorem':'Infinitely many a congruent to a_star mod 2M, divisible by T_{17,2}, have delta_P(a)=33 and total tau(a^2)=53.',
 'not_claimed':['smallest finite cover among all roots satisfying T17m2','arbitrary B,m finite-cover existence','arbitrary finite forbidden-set existence','independent project Review']}
 out=HERE/'m2_extension_certificate.json';out.write_text(json.dumps(cert,indent=2)+'\n')
 print(json.dumps({'stage':'complete','root_digits':root_digits,'square_digits':square_digits,'delta_P':33,'tau':53,'gcd_checks':len(gcdchecks),'full_period_n':Ln,'seconds':time.time()-start,'output':str(out)}),flush=True)
if __name__=='__main__':main()
