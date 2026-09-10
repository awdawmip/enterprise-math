#!/usr/bin/env python3
"""Goal-oriented NS certificate: exact Fourier Gram + rational primal/dual bounds.
High-precision optimization proposes coefficients only. Acceptance uses intervals.
No PDE time stepping, no frequency-output cutoff, no external pickle inputs.
"""
from pathlib import Path
from fractions import Fraction as F
import sys, json, hashlib, math, time
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parent
parents=[ROOT/'parent',ROOT.parent/'ns-greedy-temporal-certificate-20260910']
PAR=next((p for p in parents if (p/'certify_greedy.py').is_file()),None)
if PAR is None: raise FileNotFoundError('pinned certify_greedy.py dependency required')
expected='b2c662832fccd5749d6f531c17b9bbb7ed9f512c42158271076cd1c2fdfba536'
assert hashlib.sha256((PAR/'certify_greedy.py').read_bytes()).hexdigest()==expected
sys.path.insert(0,str(PAR))
import certify_greedy as P
E=P.E
if not __debug__: raise RuntimeError('Run without -O; assertions are certificate gates')
OUT=ROOT/'output';OUT.mkdir(exist_ok=True)

def qsym(x):
 x=F(x);return s.Rational(x.numerator,x.denominator)
def ceilq(x,n=10**10):return F((F(x)*n).__ceil__(),n)
def floorq(x,n=10**12):return F((F(x)*n).__floor__(),n)
def normi(x):return P.rootiv(x)
def packet_check(h,zero_initial=False):
 if zero_initial: assert not E.initial(h)
 for (k,r,m),v in h.items():
  assert E.dotk(v,k)==E.Z
  assert h[(tuple(-x for x in k),r,m)]==tuple((a,b,-c,-d)for a,b,c,d in v)

def construct():
 data=P.build_parent_directions()
 v=E.scale(data['v'],F(10));g=E.scale(data['g'],F(100))
 psi1=E.scale(data['psi'][0],F(100));psi2=E.scale(data['psi'][1],F(1000))
 labels=['first']+sorted({E.sq(k)for k,_,_ in psi2})
 psi=[psi1]+[{key:vec for key,vec in psi2.items()if E.sq(key[0])==j}for j in labels[1:]]
 for h in psi:packet_check(h,True)
 D=[E.heat_derivative(h)for h in psi]
 K=[P.plus(E.ntime(v,h),E.ntime(h,v))for h in psi]
 n=len(psi);FF=s.zeros(n);FK=s.zeros(n);KK=s.zeros(n);bf=s.zeros(n,1);bk=s.zeros(n,1)
 for i in range(n):
  bf[i]=E.gram_expr(D[i],g);bk[i]=E.gram_expr(K[i],g)
  for j in range(n):
   FK[i,j]=E.gram_expr(D[i],K[j])
   if j<=i:
    FF[i,j]=FF[j,i]=E.gram_expr(D[i],D[j]);KK[i,j]=KK[j,i]=E.gram_expr(K[i],K[j])
 for i in range(1,n):
  assert P.ri(FF[i,i]).a>0
  for j in range(1,n):
   if i!=j:assert FF[i,j]==0
 temporal,w=P.temporal_certificate(g)
 return labels,psi,v,g,FF,FK,KK,bf,bk,E.gram_expr(g,g),w,temporal

def propose(G,b,R,Q,L,w):
 mp.mp.dps=85;n=len(b)
 mm=lambda x:mp.mpf(str(s.N(x,90)))
 gg=mp.matrix([[mm(G[i,j])for j in range(n)]for i in range(n)])
 bb=mp.matrix([mm(x)for x in b]);qq=mp.matrix([[mm(Q[i,j])for j in range(n)]for i in range(n)])
 rr=mm(R);ll=mm(qsym(L));ww=mm(qsym(w));x=mp.lu_solve(gg,bb);ls=x.copy()
 def fun(x):return ww*abs(x[0])+mp.sqrt((x.T*qq*x)[0])+ll*mp.sqrt(rr-2*(bb.T*x)[0]+(x.T*gg*x)[0])
 iterations=0
 for iterations in range(60):
  u=qq*x;y=gg*x-bb;un=mp.sqrt((x.T*u)[0]);rn=mp.sqrt(rr-2*(bb.T*x)[0]+(x.T*gg*x)[0])
  grad=u/un+ll*y/rn;grad[0]+=ww
  if max(abs(z)for z in grad)<mp.mpf('1e-60'):break
  hes=qq/un-u*u.T/un**3+ll*(gg/rn-y*y.T/rn**3)
  step=mp.lu_solve(hes,grad);fac=mp.mpf(1);f0=fun(x)
  for _ in range(120):
   trial=x-fac*step
   if trial[0]>0 and fun(trial)<f0:break
   fac/=2
  else:break
  x=trial
 den=10**12
 rounded=lambda z:[F(int(mp.nint(z[i]*den)),den)for i in range(n)]
 return rounded(x),rounded(ls),iterations

def verify_case(data,amp,chosen,kind):
 labels,psi,vu,gu,FF,FK,KK,bf,bk,R,w,_=data
 inds=[labels.index(j)for j in chosen];a=qsym(amp);n=len(inds)
 sc=s.diag(*([s.S.One]+[a]*(len(labels)-1)))
 # Dividing every image/source by a^2 keeps the finite problem well conditioned.
 G=sc*(FF-a*(FK+FK.T)+a*a*KK)*sc
 b=sc*(bf-a*bk);Q=sc*FF*sc
 for i in range(len(labels)):Q[0,i]=Q[i,0]=0
 G=G.extract(inds,inds).applyfunc(s.expand);b=b.extract(inds,[0]).applyfunc(s.expand);Q=Q.extract(inds,inds).applyfunc(s.expand)
 inv,Lraw,Cb=P.inverse_certificate(amp)
 L=ceilq(Lraw,10**8);alpha=ceilq(L*Cb,10**8)
 if amp==F(3,20):L=F(73,20);alpha=F(57,2)
 assert Lraw<L and L*Cb<alpha
 c,cls,it=propose(G,b,R,Q,L,w);cs=s.Matrix([qsym(x)for x in c])
 r2=s.expand(R-2*(b.T*cs)[0]+(cs.T*G*cs)[0]);rest2=s.expand((cs.T*Q*cs)[0])
 ri=P.ri(r2);qi=P.ri(rest2);assert ri.a>0 and qi.a>0
 eta=P.I(amp**2)*(P.I(w)*abs(c[0])+normi(qi)+L*normi(ri))
 GI=[[P.ri(G[i,j])for j in range(n)]for i in range(n)];bi=[P.ri(b[i])for i in range(n)]
 # The true least-squares solution, not just its rounded proposal.
 ci=P.ldl_solve(GI,bi)
 ls_res=P.ri(R)-sum((bi[i]*ci[i]for i in range(n)),P.I(0));assert ls_res.a>0
 ls_rest=sum((ci[i].square()*P.ri(Q[i,i])for i in range(1,n)),P.I(0))
 assert ci[0].a>0
 ls_eta=P.I(amp**2)*(w*ci[0]+normi(ls_rest)+L*normi(ls_res))
 # Dual y=tau*(g-Ac) in the normalized Y space. Q_rest is diagonal and positive.
 corr=(b-G*cs).applyfunc(s.expand);vi=[P.ri(x)for x in corr]
 dual_rest=sum((vi[i].square()/P.ri(Q[i,i])for i in range(1,n)),P.I(0))
 caps=[L/normi(ri).b,w/vi[0].maxabs(),1/normi(dual_rest).b]
 tau=floorq(min(caps)*(1-F(1,10**12)))
 assert tau>0 and tau*tau*ri.b<=L*L
 assert tau*vi[0].maxabs()<=w and tau*tau*dual_rest.b<=1
 dual=P.I(amp**2*tau)*P.ri(s.expand(R-(b.T*cs)[0]));assert dual.a>0
 assert dual.a<=eta.b
 # Independently form every full output before taking the norm.
 pa=[E.scale(psi[j],amp**(2 if j==0 else 3))for j in inds]
 d=P.plus(*[E.scale(h,x)for h,x in zip(pa,c)])
 v=E.scale(vu,amp);g=E.scale(gu,amp**2)
 e=P.plus(P.linear(v,d),E.scale(g,F(-1)))
 packet_check(d,True);packet_check(e)
 assert s.expand(E.gram_expr(e,e)-a**4*r2)==0
 rest=P.plus(*[E.scale(h,x)for h,x in zip(pa[1:],c[1:])])
 assert s.expand(E.gram_expr(E.heat_derivative(rest),E.heat_derivative(rest))-a**4*rest2)==0
 row={'amplitude':str(amp),'labels':chosen,'inverse_upper':str(L),'alpha_upper':str(alpha),
  'coefficients':[str(x)for x in c], 'iteration_proposal_count':it,
  'eta_interval':[str(eta.a),str(eta.b)],'eta_upper_readout':float(eta.b),
  'dual_tau':str(tau),'dual_lower':str(dual.a),'dual_lower_readout':float(dual.a),
  'primal_dual_gap_upper':str(eta.b-dual.a),
  'least_squares_eta_interval':[str(ls_eta.a),str(ls_eta.b)],
  'least_squares_eta_readout':float(ls_eta.b),
  'optimized_residual_upper':str(amp**2*normi(ri).b),
  'least_squares_residual_upper':str(amp**2*normi(ls_res).b),
  'correction_packets':len(d),'full_defect_packets':len(e),'full_defect_modes':len({k for k,_,_ in e}),
  'max_defect_squared_radius':max(E.sq(k)for k,_,_ in e),
  'exact_all_output_Gram_identity':True,'dual_feasible_by_rational_bounds':True,
  'inverse_certificate':inv,'kind':kind}
 assert amp**2*normi(ri).a>amp**2*normi(ls_res).b
 if kind=='fewer_packets':
  radius=F(3,200);target=radius-alpha*radius**2
  assert ls_eta.a>target>eta.b
 elif kind=='expanded_datum':
  radius=F(17,1000)
  assert 4*alpha*ls_eta.a>1 and 4*alpha*eta.b<1
  assert eta.b+alpha*radius**2<radius and 2*alpha*radius<1
 elif kind=='dictionary_obstruction':
  assert 4*alpha*dual.a>1
  row['barrier_lower_4alpha_eta']=str(4*alpha*dual.a)
  row['scope']='This fixed reference/dictionary/norm-majorant/inverse-bound certificate only; not PDE blow-up.'
 if kind!='dictionary_obstruction':
  etaup=ceilq(eta.b);margin=radius-etaup-alpha*radius**2
  assert margin>0 and 2*alpha*radius<1
  # Arbitrary smooth solenoidal initial perturbations handled without changing v.
  Hgain=normi(P.I(F(3,4))).b*L
  delta=floorq(margin/(2*Hgain))
  assert Hgain*delta<margin and delta>0
  row.update({'eta_rational_upper':str(etaup),'certified_radius':str(radius),
   'inclusion_margin':str(margin),'contraction_upper':str(2*alpha*radius),
   'off_family_initial_perturbation_radius':str(delta)})
 print(kind,amp,'eta',float(eta.b),'dual',float(dual.a),'LS',float(ls_eta.a),'gap',float(eta.b-dual.a),flush=True)
 return row

def main():
 t=time.monotonic();data=construct()
 rows=[verify_case(data,F(3,20),['first',8,6,14],'fewer_packets'),
  verify_case(data,F(19,125),['first',8,6,14,2],'expanded_datum'),
  verify_case(data,F(4,25),data[0],'dictionary_obstruction')]
 out={'status':'PASS','date':'2026-09-10','scope':'fixed-reference convex certificate optimization; specified periodic A3 data only',
  'parent_checker_sha256':expected,'backend_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
  'unit_first_response_norm_upper':str(data[-2]),'cases':rows,
  'all_dual_constraints_verified':True,'no_PDE_sampling':True,'no_frequency_output_cutoff':True,
  'limits':['Not independently reviewed.','No arbitrary-data NS regularity or historical priority claim.',
   'No infeasibility claim outside the stated finite dictionary and chosen norm/inverse majorants.',
   'Numerical optimization proposes coefficients; only rational interval tests certify assertions.'],
  'elapsed_seconds':time.monotonic()-t}
 (OUT/'goal_verification.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
 print('PASS',time.monotonic()-t,flush=True)
if __name__=='__main__':main()
