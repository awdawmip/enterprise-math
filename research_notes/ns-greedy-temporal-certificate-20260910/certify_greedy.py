#!/usr/bin/env python3
"""Full-output greedy causal NS certificate, no PDE time/space sampling.
Uses unchanged canonical packet backend through the preceding research package.
Floating point proposes indices/coefficients only; all acceptance is rational.
"""
from pathlib import Path
import sys,json,pickle,hashlib,math,time
from fractions import Fraction as F
from collections import defaultdict
from types import SimpleNamespace
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parent
# The exact packet algebra is reused unchanged, either from the package or its canonical repo path.
backend_candidates=[ROOT/'exact_packets.py',ROOT.parent/'ns-inexact-newton-error-ledger-20260909'/'exact_packets.py',ROOT/'parent'/'current'/'exact_packets.py']
backend=next((p for p in backend_candidates if p.is_file()),None)
if backend is None: raise FileNotFoundError('canonical exact_packets.py is required')
assert hashlib.sha256(backend.read_bytes()).hexdigest()=='0ffab938427c4827700876fbd9f9c371a59d07aa89edefd5a6447071ec48d25d'
sys.path.insert(0,str(backend.parent))
import exact_packets as E

def root_bounds(x,digits=22):
 x=F(x)
 if x<0: raise ValueError('negative square root')
 scale=10**digits;n=math.isqrt(x.numerator*scale*scale//x.denominator)
 lo,hi=F(n,scale),F(n+1,scale)
 assert lo*lo<=x<hi*hi
 return lo,hi

def exp_bounds(x,degree=70):
 x=F(x)
 if x<0 or x>=degree+2:raise ValueError('Taylor remainder range')
 lo=sum((x**j/F(math.factorial(j)) for j in range(degree+1)),F())
 rem=x**(degree+1)/F(math.factorial(degree+1))/(1-x/F(degree+2))
 return lo,lo+rem

def radical_bounds(expr):
 lo=hi=F()
 for term in s.Add.make_args(s.expand(expr)):
  c,rest=term.as_coeff_Mul();cc=F(int(s.numer(c)),int(s.denom(c)))
  if rest==1:a=b=F(1)
  elif rest.is_Pow and rest.exp==s.Rational(1,2) and rest.base.is_Rational:
   a,b=root_bounds(F(int(s.numer(rest.base)),int(s.denom(rest.base))))
  else:raise ValueError(f'unsupported radical {rest}')
  lo+=cc*(a if cc>=0 else b);hi+=cc*(b if cc>=0 else a)
 return lo,hi

def real_inner(aa,bb):
 a=b=F()
 for x,y in zip(aa,bb):
  rr=E.prod(x[:2],y[:2]);ii=E.prod(x[2:],y[2:]);a+=rr[0]+ii[0];b+=rr[1]+ii[1]
 return a,b

def plus(*arrays):
 out={}
 for h in arrays:out=E.plus(out,h)
 return out

def exact_linear(v,h):
 return plus(E.heat_derivative(h),E.scale(E.ntime(v,h),F(-1)),E.scale(E.ntime(h,v),F(-1)))

def score(G,b,R,coeff):
 x=s.Matrix([s.Rational(q.numerator,q.denominator)for q in coeff])
 return s.expand(R-2*(x.T*b)[0]+(x.T*G*x)[0])

# Same declared interfaces as the parent; no Fourier operator is reimplemented.
P=SimpleNamespace(root_bounds=root_bounds,radical_bounds=radical_bounds,real_inner=real_inner,parent=SimpleNamespace(exp_bounds=exp_bounds))
A=SimpleNamespace(linear=exact_linear,plus=plus,pair=E.gram_expr,score=score)

def build_parent_directions():
 ks=[(1,1,0),(1,0,1),(0,1,1),(2,-2,0)];modes={}
 assert s.Matrix(ks).rank()==3
 for k in ks:
  kk=s.Matrix(k);ee=s.zeros(3,1);ee[list(k).index(0)]=1
  h=s.simplify((ee+s.I*kk.cross(ee)/s.sqrt(E.sq(k)))/s.sqrt(2))
  assert s.simplify(s.I*kk.cross(h)-s.sqrt(E.sq(k))*h)==s.zeros(3,1)
  modes[k]=h;modes[tuple(-q for q in k)]=s.conjugate(h)
 unit=E.import_packets({(k,E.sq(k),0):h for k,h in modes.items()})
 v=E.scale(unit,F(1,10));g=E.ntime(v,v)
 p1=E.solve_heat(g);n3=plus(E.ntime(v,p1),E.ntime(p1,v));p2=E.solve_heat(n3)
 assert E.heat_derivative(p1)==g and E.heat_derivative(p2)==n3
 assert not E.initial(p1) and not E.initial(p2)
 return {'v':v,'g':g,'psi':[p1,p2]}
OUT=ROOT/'output';OUT.mkdir(exist_ok=True)
if not __debug__: raise RuntimeError('verification requires assertions')
SCALE=10**35
class I:
 def __init__(self,a,b=None):
  aa=F(a);bb=F(a if b is None else b)
  assert aa<=bb
  self.a=F((aa*SCALE).__floor__(),SCALE)
  self.b=F((bb*SCALE).__ceil__(),SCALE)
 def __add__(self,o):
  o=iv(o);return I(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return I(-self.b,-self.a)
 def __sub__(self,o):return self+-iv(o)
 def __rsub__(self,o):return iv(o)+-self
 def __mul__(self,o):
  o=iv(o);vals=[self.a*o.a,self.a*o.b,self.b*o.a,self.b*o.b];return I(min(vals),max(vals))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=iv(o);assert not o.a<=0<=o.b
  return self*I(1/o.b,1/o.a)
 def square(self):
  return I(0 if self.a<=0<=self.b else min(self.a*self.a,self.b*self.b),max(self.a*self.a,self.b*self.b))
 def maxabs(self):return max(abs(self.a),abs(self.b))
def iv(x):return x if isinstance(x,I) else I(x)
def ri(x):return I(*P.radical_bounds(s.expand(x)))
def expiv(x):
 x=iv(x)
 def one(q):
  if q>=0:return P.parent.exp_bounds(q,max(70,int(q)+20))
  lo,hi=P.parent.exp_bounds(-q,max(70,int(-q)+20));return 1/hi,1/lo
 return I(one(x.a)[0],one(x.b)[1])
def rootiv(x):
 x=iv(x);assert x.a>=0
 return I(P.root_bounds(x.a,34)[0],P.root_bounds(x.b,34)[1])
def linear(v,h):return A.linear(v,h)
def ldl_solve(mat,vec):
 n=len(vec);l=[[I(0)for _ in range(n)]for _ in range(n)];d=[]
 for i in range(n):
  l[i][i]=I(1)
  di=mat[i][i]-sum((l[i][k].square()*d[k]for k in range(i)),I(0));assert di.a>0;d.append(di)
  for j in range(i+1,n):l[j][i]=(mat[j][i]-sum((l[j][k]*l[i][k]*d[k]for k in range(i)),I(0)))/di
 y=[]
 for i in range(n):y.append(vec[i]-sum((l[i][k]*y[k]for k in range(i)),I(0)))
 x=[I(0)for _ in range(n)]
 for i in reversed(range(n)):x[i]=y[i]/d[i]-sum((l[k][i]*x[k]for k in range(i+1,n)),I(0))
 return x

def phi(lam,sig,t):
 t=iv(t)
 if lam==sig:return t*expiv(-lam*t)
 return (expiv(-sig*t)-expiv(-lam*t))/I(lam-sig)
def intphi2(lam,sig,t):
 t=iv(t)
 if lam==sig:
  x=2*lam*t
  return (1-expiv(-x)*(1+x+x.square()/2))/(4*lam**3)
 return ((1-expiv(-2*sig*t))/(2*sig)-2*(1-expiv(-(lam+sig)*t))/(lam+sig)+(1-expiv(-2*lam*t))/(2*lam))/(lam-sig)**2

def temporal_certificate(unitg):
 # Unique maxima of phi^2+c*lambda*integral phi^2 occur in these rational brackets.
 brackets={6:(F(1814842508,10**10),F(1814842509,10**10)),10:(F(4,25),F(4,25)),14:(F(1527272705,10**10),F(1527272706,10**10))}
 mags=defaultdict(lambda:s.S.Zero)
 for (k,rate,m),vec in unitg.items():
  assert rate==10 and m==0
  aa,bb=P.real_inner(vec,vec)
  mags[E.sq(k)]+=s.Rational(aa.numerator,aa.denominator)+s.Rational(bb.numerator,bb.denominator)*s.sqrt(2)
 total=I(0);rows=[]
 for lam in sorted(mags):
  lo,hi=brackets[lam];c=F(3,4)
  # E'=phi*[2 exp(-sigma*t)-(2-c)*lambda*phi].
  if lam!=10:
   def derivsign(t):return 2*expiv(-10*iv(t))-(2-c)*lam*phi(lam,10,t)
   assert derivsign(lo).a>0 and derivsign(hi).b<0
  else: assert lo==1/(F(lam)*(1-c/2))
  val=phi(lam,10,I(lo,hi)).square()+c*lam*intphi2(lam,10,hi)
  contrib=rootiv(lam)*ri(mags[lam])*val
  total+=contrib
  rows.append({'lambda':lam,'source_squared':str(mags[lam]),'maximum_time_bracket':[str(lo),str(hi)],'running_energy_upper':str(contrib.b)})
 bound=F(3271,10000)
 assert total.b<bound**2
 return {'status':'PASS','unit_first_response_norm_upper':str(bound),'norm_readout_upper':float(rootiv(total).b),'modes':rows,'method':'analytic unique-maximum proof + rational exponential enclosures; sum of modal suprema'},bound

def inverse_certificate(a):
 rt=rootiv(2)
 ma=6*rt*(F(1,2)+rootiv(1+rt));mb=4*rt*(F(1,2)+rootiv(1+2*rt))
 # b(t)=(a(ma exp(-2t)+mb exp(-8t))-1/4)_+.
 # Bracket the unique time zero by dyadic rational bisection.
 lo,hi=F(0),F(4)
 def val(t):return a*(ma*expiv(-2*iv(t))+mb*expiv(-8*iv(t)))-F(1,4)
 assert val(lo).a>0 and val(hi).b<0
 for _ in range(38):
  mid=(lo+hi)/2;v=val(mid)
  if v.a>0:lo=mid
  elif v.b<0:hi=mid
  else:break
 assert val(lo).a>0 and val(hi).b<0
 # integrate M to hi, subtract at least lo/4; valid upper for int b.
 Bhi=(a*(ma*(1-expiv(-2*iv(hi)))/2+mb*(1-expiv(-8*iv(hi)))/8)-lo/4).b
 L=(expiv(I(0,Bhi))/rootiv(F(3,4))).b
 Cb=(I(F(9503,1000))/rootiv(F(3,2))).b
 return {'growth_zero_bracket':[str(lo),str(hi)],'growth_integral_upper':str(Bhi),'inverse_upper_exact':str(L),'inverse_upper_readout':float(L),'alpha_upper_readout':float(L*Cb)},L,Cb

def scalar_checks():
 t=s.symbols('t',nonnegative=True);la,si=s.symbols('la si',positive=True)
 ph=(s.exp(-si*t)-s.exp(-la*t))/(la-si)
 pp=((1-s.exp(-2*si*t))/(2*si)-2*(1-s.exp(-(la+si)*t))/(la+si)+(1-s.exp(-2*la*t))/(2*la))/(la-si)**2
 assert s.simplify(s.diff(pp,t)-ph**2)==0
 assert s.simplify(s.diff(ph,t)+la*ph-s.exp(-si*t))==0
 aa,bb,cc,dd,ee=s.symbols('aa bb cc dd ee',real=True)
 change=(cc*dd**2-2*bb*dd*ee+aa*ee**2)/(aa*cc-bb**2)-dd**2/aa
 gain=(ee-bb*dd/aa)**2/(cc-bb**2/aa)
 assert s.factor(change-gain)==0
 return {'heat_response_and_integral':True,'Schur_gain_identity':True}

def main():
 t=time.monotonic();scalar=scalar_checks()
 # Deterministic construction; no untrusted serialized objects are loaded.
 data=build_parent_directions()
 unitg=E.scale(data['g'],F(100));temporal,H1=temporal_certificate(unitg)
 a=F(3,20);q=a/F(1,10)
 v=E.scale(data['v'],q);g=E.scale(data['g'],q*q)
 h1=E.scale(data['psi'][0],q*q);h2=E.scale(data['psi'][1],q**3)
 by=defaultdict(dict)
 for key,val in h2.items():by[E.sq(key[0])][key]=val
 labels=['all-first-response']+sorted(by)
 psi=[h1]+[by[n]for n in sorted(by)]
 images=[linear(v,h)for h in psi]
 for h in psi:assert not E.initial(h)
 # Splitting one exponential out of a heat response generally changes the initial datum.
 split_key=next(key for key in h1 if key[2]==0)
 assert E.initial({split_key:h1[split_key]})
 n=len(psi); G=s.zeros(n);bb=s.zeros(n,1);R=A.pair(g,g)
 for i in range(n):
  bb[i]=A.pair(images[i],g)
  for j in range(i+1):G[i,j]=G[j,i]=A.pair(images[i],images[j])
 print('Full all-output Gram complete',n,'directions',round(time.monotonic()-t,2),flush=True)
 inv,Lexact,Cb=inverse_certificate(a)
 Lup=F(73,20);alpha=F(57,2)
 assert Lexact<Lup and Lup*Cb<alpha
 GI=[[ri(G[i,j])for j in range(n)]for i in range(n)];bi=[ri(bb[i])for i in range(n)]
 selected=[0];rows=[];mp.mp.dps=80
 while True:
  GG=mp.matrix([[mp.mpf(str(G[i,j].evalf(85)))for j in selected]for i in selected]);bv=mp.matrix([mp.mpf(str(bb[i].evalf(85)))for i in selected])
  raw=mp.lu_solve(GG,bv);coeff=[F(int(mp.nint(x*10**12)),10**12)for x in raw]
  ss=G.extract(selected,selected);bv_s=bb.extract(selected,[0]);r2=A.score(ss,bv_s,R,coeff);r_iv=ri(r2);assert r_iv.a>0
  d=A.plus(*[E.scale(psi[i],c)for i,c in zip(selected,coeff)])
  rest=A.plus(*[E.scale(psi[i],c)for i,c in zip(selected,coeff)if i!=0])
  rhs=E.heat_derivative(rest);rest2=A.pair(rhs,rhs)if rhs else s.S.Zero
  eta=abs(coeff[0])*a*a*H1+rootiv(ri(rest2)).b+Lup*rootiv(r_iv).b
  eta_round=F(math.ceil(eta*10**8),10**8)
  # An accepted nonlinear radius, not selected by floating point proof.
  radius=F(3,200) # .015
  margin=radius-eta_round-alpha*radius**2
  row={'selected_labels':[labels[i]for i in selected],'coefficients':[str(x)for x in coeff],
       'correction_packets':len(d),'full_residual_norm_upper':str(rootiv(r_iv).b),
       'relative_residual_upper':str(rootiv(r_iv/ri(R)).b),
       'eta_upper':str(eta_round),'q_upper':str(4*alpha*eta_round),
       'nonlinear_radius':str(radius),'ball_margin':str(margin),'nonlinear_pass':margin>0 and 2*alpha*radius<1}
  print('stage',len(selected),'labels',row['selected_labels'],'eta',float(eta_round),'q',float(4*alpha*eta_round),'pass',row['nonlinear_pass'],flush=True)
  # Compute all available Schur gains using outward rational LDL solves.
  mat=[[GI[i][j]for j in selected]for i in selected]
  xx=ldl_solve(mat,[bi[i]for i in selected]);gains=[]
  station=[sum((mat[i][j]*coeff[j]for j in range(len(selected))),I(0))-bi[selected[i]]for i in range(len(selected))]
  inv_station=ldl_solve(mat,station)
  loss=sum(si.maxabs()*wi.maxabs()for si,wi in zip(station,inv_station))
  assert loss<r_iv.a/F(10**6)
  row['coefficient_suboptimality_upper']=str(loss)
  if rows:
   assert r_iv.b<F(rows[-1]['residual_norm_squared_lower'])
  row['residual_norm_squared_lower']=str(r_iv.a)
  row['residual_norm_squared_upper']=str(r_iv.b)
  for j in range(n):
   if j in selected:continue
   hh=[GI[i][j]for i in selected];yy=ldl_solve(mat,hh)
   den=GI[j][j]-sum((hh[i]*yy[i]for i in range(len(selected))),I(0));assert den.a>0
   num=bi[j]-sum((hh[i]*xx[i]for i in range(len(selected))),I(0))
   gain=num.square()/den
   gains.append((j,gain))
  if gains:
   pick=max(gains,key=lambda x:x[1].a)
   # weak greedy guarantee accounts for interval ties; not a claim of global sparsest set.
   assert pick[1].a>max(h.b for _,h in gains)/2
   row['all_candidate_gains']=[{'label':labels[j],'lower':str(gi.a),'upper':str(gi.b),'packets':len(psi[j])}for j,gi in gains]
   row['next_selected_label']=labels[pick[0]];row['weak_greedy_factor']='1/2'
  rows.append(row)
  if row['nonlinear_pass']:
   error=A.plus(linear(v,d),E.scale(g,F(-1)))
   assert s.expand(A.pair(error,error)-r2)==0
   assert margin>0 and 2*alpha*radius<1
   row['full_residual_packets']=len(error)
   row['full_residual_modes']=len({key[0]for key in error})
   row['max_residual_squared_radius']=max(E.sq(key[0])for key in error)
   for h in [d,error]:
    for (k,rate,m),vec in h.items():
     assert E.dotk(vec,k)==E.Z
     conj=tuple((aa,bb,-cc,-dd)for aa,bb,cc,dd in vec)
     assert h[(tuple(-q for q in k),rate,m)]==conj
   # Bounds from old norm-only h1 trial at the same amplitude are not small enough.
   break
  if not gains:raise AssertionError('tested dictionary failed the nonlinear target')
  selected.append(pick[0])
  if len(selected)>8:raise AssertionError('bounded search exceeded')
 out={'status':'PASS','date':'2026-09-10','amplitude':str(a),'nu':1,'initial_rank':3,'initial_modes':8,
 'scalar_checks':scalar,'all_trial_initial_traces_zero':True,'single_heat_packet_unsafe_split_witness':True,'dictionary_size':n,'dictionary':'global first heat response plus 11 radius-coherent groups of its next causal response',
 'temporal_certificate':temporal,'inverse_certificate':inv,'inverse_upper':'73/20','alpha_upper':'57/2',
 'stages':rows,'certified_radius':str(radius),'contraction_factor':str(2*alpha*radius),
 'all_selected_residuals_include_out_of_core_outputs':True,'final_residual_independently_recomputed':True,
 'elapsed_seconds_readout':time.monotonic()-t,
 'limits':['specific normalized periodic A3 datum; no arbitrary-data theorem','greedy relative to the tested finite dictionary only','parent all-mode inverse and C*=9.503 remain analytic dependencies','ordinary proofs and rational certificates, not independent peer review']}
 (OUT/'greedy_verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 (OUT/'greedy_gram.json').write_text(json.dumps({'labels':labels,'G':[[str(G[i,j])for j in range(n)]for i in range(n)],'b':[str(x)for x in bb],'R':str(R)},ensure_ascii=False)+'\n')
 print('PASS',round(time.monotonic()-t,2),flush=True)
if __name__=='__main__':main()
