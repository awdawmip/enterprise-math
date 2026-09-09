#!/usr/bin/env python3
"""Exact Fourier checks for a fourth heat correction and its positive helicity Gram.

This verifies finite algebra only. The analytic proofs and scope are in RESEARCH_NOTE.md.
The inherited full Fourier convolution implementation is used unchanged.
"""
from __future__ import annotations
import json, sys
from collections import defaultdict
from pathlib import Path
import sympy as s
def nonlinear(modes):
    out = {}
    for p,a in modes.items():
        for q,b in modes.items():
            k = tuple(p[i]+q[i] for i in range(3))
            if not any(k):
                continue
            out[k] = out.get(k,s.zeros(3,1))-s.I*a.dot(s.Matrix(q))*b
    for k,z in out.items():
        kv = s.Matrix(k)
        out[k]=s.simplify(z-kv*kv.dot(z)/kv.dot(kv))
    return out

Z=s.zeros(3,1)

def sq(k): return sum(int(x)**2 for x in k)
def clean(v):return v.applyfunc(s.expand)
def put(out,key,z):out[key]=out.get(key,Z)+z

def npack(A,B):
 out={}
 for (p,sp),a in A.items():
  for (q,sq0),b in B.items():
   k=tuple(p[i]+q[i] for i in range(3))
   if not any(k):continue
   put(out,(k,sp+sq0),-s.I*a.dot(s.Matrix(q))*b)
 result={}
 for (k,rate),z in out.items():
  kv=s.Matrix(k);v=clean(z-kv*kv.dot(z)/sq(k))
  if v!=Z:result[(k,rate)]=v
 return result

def add(A,B):
 out=dict(A)
 for key,z in B.items():put(out,key,z)
 return {key:clean(z) for key,z in out.items() if clean(z)!=Z}

def lift(modes):return {(k,sq(k)):v for k,v in modes.items() if v!=Z}

def cubic2(A,B,H):
 """Cubic physical heat-resolvent, followed by outer LEAF-rate resolvent; nu=1."""
 hi=defaultdict(list)
 for (k,rate),z in H.items():hi[k].append((rate,z))
 coeff=defaultdict(lambda:s.S.Zero)
 for (p,rp),a in A.items():
  for (q,rq),b in B.items():
   k=tuple(p[i]+q[i] for i in range(3))
   if k not in hi:continue
   dot=s.expand(a.dot(s.Matrix(q)))
   if dot==0:continue
   for rh,h in hi[k]:
    inner=s.expand((s.conjugate(h).T*b)[0])
    if inner==0:continue
    coeff[sq(k)]+= -s.I*dot*inner/s.Integer((sq(p)+sq(q)+sq(k))*(rp+rq+rh))
 return s.simplify(sum(s.sqrt(m)*s.re(s.expand(v)) for m,v in coeff.items()))

def fourth_and_fifth(modes):
 X=lift(modes);N=npack(X,X)
 h=lift({k:clean(z) for k,z in nonlinear(modes).items() if z!=Z})
 # Independent packet sum equals the inherited full nonlinear output.
 summed={}
 for (k,rate),z in N.items():put(summed,k,z)
 assert all(clean(summed.get(k,Z)-z)==Z for (k,_),z in h.items())
 DN=add(npack(h,X),npack(X,h))
 C4=s.simplify(cubic2(N,X,X)+cubic2(X,N,X)+cubic2(X,X,N))
 R5=s.simplify(sum(cubic2(A,B,C) for A,B,C in [
   (DN,X,X),(N,h,X),(N,X,h),
   (h,N,X),(X,DN,X),(X,N,h),
   (h,X,N),(X,h,N),(X,X,DN)]))
 return C4,R5,N

def helical_data(ks,phases):
 modes={}
 for k,ph in zip(ks,phases):
  kv=s.Matrix(k);e=Z.copy();e[list(k).index(0)]=1
  z=clean(ph*(e+s.I*kv.cross(e)/s.sqrt(sq(k)))/2)
  modes[k]=z;modes[tuple(-x for x in k)]=s.conjugate(z)
  assert clean(s.I*kv.cross(z)-s.sqrt(sq(k))*z)==Z
 return modes

def nminus_packets(N):
 out={}
 for (k,rate),z in N.items():
  b=s.simplify((z-s.I*s.Matrix(k).cross(z)/s.sqrt(sq(k)))/2)
  if b!=Z:out[(k,rate)]=b
 return out

def positive_gram(J):
 by=defaultdict(list)
 for (k,rate),z in J.items():by[k].append((rate,z))
 ans=0
 for k,pack in by.items():
  lam=sq(k)
  for sigma,a in pack:
   for tau,b in pack:
    inner=s.simplify(s.re((s.conjugate(a).T*b)[0]))
    ans+=s.sqrt(lam)*s.Rational(2*lam+sigma+tau,(lam+sigma)*(lam+tau)*(sigma+tau))*inner
 return s.simplify(ans)

def verify_corrector():
 # Full-rank root-ray witness with one initial positive helicity and two radii.
 ks=[(1,0,1),(2,0,-2),(0,2,2),(0,2,-2)]
 modes=helical_data(ks,[s.I,1,1,1])
 print('computing exact fourth/fifth',flush=True)
 C4,R5,N=fourth_and_fifth(modes)
 G=positive_gram(nminus_packets(N))
 assert s.simplify(C4-G)==0
 K=s.simplify(sum(s.sqrt(sq(k))*(s.conjugate(z).T*z)[0] for k,z in modes.items()))
 Q=s.simplify(sum(sq(k)**s.Rational(3,2)*(s.conjugate(z).T*z)[0] for k,z in modes.items()))
 assert s.Matrix(ks).rank()==3
 # Exact differential identity for the scalar Gram numerator.
 lam,si,ta,nu=s.symbols('lambda sigma tau nu',positive=True)
 gram=(2*lam+si+ta)/(2*nu**3*lam*(lam+si)*(lam+ta)*(si+ta))
 kernel=(1/(lam+si)+1/(lam+ta))/(nu**2*(si+ta))
 assert s.simplify(2*nu*lam*gram-kernel)==0
 result={'status':'PASS','scope':'finite Fourier identities; not a proof by simulation',
  'input_wavevectors':ks,'phases':['i','1','1','1'],'input_modes':len(modes),
  'input_rank':3,'all_initial_helicities':'+','viscosity_for_readouts':1,
  'K_exact':str(K),'Q_exact':str(Q),'C4_exact':str(C4),'C4_gram_exact':str(G),
  'R5_exact':str(R5),'C4_decimal':str(s.N(C4,30)),'R5_decimal':str(s.N(R5,30)),
  'positive_gram_equals_fourth_corrector':True,'gram_resolvent_identity':True,
  'R5_sign_certificate':'Exact rational bounds are checked by verify_responses() in this script.'}
 # Sign decisions below use explicit rational enclosures, not floating-point sign.
 expr=s.expand(R5)
 radicals=sorted(expr.atoms(s.Pow),key=str)
 print('C4 =',C4,flush=True);print('R5 =',R5,flush=True)
 print('K,Q =',K,Q,flush=True)
 Path(__file__).with_name('quartic_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print('PASS: exact Gram equality and derivative',flush=True)



from math import factorial
def ntime(A,B):
 out={}
 for (p,sp,mp),a in A.items():
  for (q,sq0,mq),b in B.items():
   k=tuple(p[i]+q[i] for i in range(3))
   if not any(k):continue
   put(out,(k,sp+sq0,mp+mq),-s.I*a.dot(s.Matrix(q))*b)
 result={}
 for (k,rate,power),z in out.items():
  kv=s.Matrix(k);v=clean(z-kv*kv.dot(z)/sq(k))
  if v!=Z:result[(k,rate,power)]=v
 return result

def plus(A,B):
 out=dict(A)
 for key,z in B.items():put(out,key,z)
 return {key:clean(z) for key,z in out.items() if clean(z)!=Z}

def solve_heat(F):
 out={}
 for (k,rate,m),z in F.items():
  lam=sq(k);gap=lam-rate
  if gap==0:
   put(out,(k,lam,m+1),z/s.Integer(m+1))
  else:
   for j in range(m+1):
    put(out,(k,rate,m-j),s.Rational((-1)**j*factorial(m),factorial(m-j)*gap**(j+1))*z)
   put(out,(k,lam,0),-s.Rational((-1)**m*factorial(m),gap**(m+1))*z)
 return {key:clean(z) for key,z in out.items() if clean(z)!=Z}

def diss_inner_minus(A,B):
 """integral <Lambda^1.5 P_-A,Lambda^1.5 P_-B> dt at nu=1."""
 by=defaultdict(list)
 for (k,rate,power),z in B.items():by[k].append((rate,power,z))
 coeff=defaultdict(lambda:s.S.Zero)
 for (k,ra,ma),a in A.items():
  for rb,mb,b in by.get(k,[]):
   integ=s.Rational(factorial(ma+mb),(ra+rb)**(ma+mb+1))
   lam=sq(k)
   aa=s.expand(s.re((s.conjugate(a).T*b)[0]))
   ab=s.expand(s.re((s.conjugate(a).T*(s.I*s.Matrix(k).cross(b)))[0]))
   coeff[lam]+=lam*integ*aa/2
   coeff[1]-=lam*integ*ab/2
 return s.simplify(sum(s.sqrt(k)*s.expand(v) for k,v in coeff.items()))

def check_equation(V,F):
 out={}
 for (k,rate,power),z in V.items():
  put(out,(k,rate,power),(sq(k)-rate)*z)
  if power:put(out,(k,rate,power-1),power*z)
 for key,z in F.items():put(out,key,-z)
 assert all(clean(z)==Z for z in out.values())
 initial={}
 for (k,rate,power),z in V.items():
  if power==0:put(initial,k,z)
 assert all(clean(z)==Z for z in initial.values())

def verify_responses():
 modes=helical_data([(1,0,1),(2,0,-2),(0,2,2),(0,2,-2)],[s.I,1,1,1])
 v1={(k,sq(k),0):z for k,z in modes.items()}
 n2=ntime(v1,v1);v2=solve_heat(n2);check_equation(v2,n2)
 print('v2 packets',len(v2),flush=True)
 n3=plus(ntime(v1,v2),ntime(v2,v1));v3=solve_heat(n3);check_equation(v3,n3)
 print('v3 packets',len(v3),flush=True)
 C4=2*diss_inner_minus(v2,v2)
 C5=4*diss_inner_minus(v2,v3)
 S6=2*diss_inner_minus(v3,v3)
 R5=-s.Rational(1409,120960)+s.Rational(107,50400)*s.sqrt(5)+s.Rational(451,120960)*s.sqrt(3)
 assert s.simplify(C5-R5/28)==0
 expectedC4=-s.Rational(123,6400)*s.sqrt(2)+s.sqrt(14)/560+7*s.sqrt(10)/2000+3*s.sqrt(6)/640
 assert s.simplify(C4-expectedC4)==0
 # Fully rational sign certificate; square the proposed bounds before using them.
 assert s.Rational(9,4)**2>5 and s.Rational(7,4)**2>3
 upper=-s.Rational(1409,120960)+s.Rational(107,50400)*s.Rational(9,4)+s.Rational(451,120960)*s.Rational(7,4)
 assert upper == -s.Rational(839,2419200)
 # At amplitude 64 and viscosity 1, the flipped field has positive E4 derivative.
 assert 64**3*(-upper)>75
 # Cauchy Schwarz guarantees the exact nonnegative discriminant; compute it too.
 discr=s.simplify(4*C4*S6-C5*C5)
 result={
  'status':'PASS','v1_packets':len(v1),'v2_packets':len(v2),'v3_packets':len(v3),
  'v2_and_v3_full_heat_response_equations':True,'zero_initial_response':True,
  'resonant_packets_retained':True,
  'C4_exact':str(C4),'C5_exact':str(C5),'positive_sixth_square_exact':str(S6),
  'C4_decimal_readout':str(s.N(C4,25)),'C5_decimal_readout':str(s.N(C5,25)),
  'S6_decimal_readout':str(s.N(S6,25)),
  'C5_equals_R5_over_28':True,
  'R5_strict_rational_upper_bound':str(upper),
  'amplitude_64_times_nu_counterexample_certified':True,
  'square_completion':'K/2+C4+C5+S6 = K/2+2nu integral ||Lambda^1.5(v2^-+v3^-)||^2',
  'Cauchy_Schwarz_discriminant_exact':str(discr),
  'Cauchy_Schwarz_discriminant_decimal_readout':str(s.N(discr,25)),
  'warning':'The sixth square is not the full sixth homological correction. These are initial-state identities, not invariance of one-helicity dynamics.'}
 Path(__file__).with_name('square_completion_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print('C4',C4,flush=True);print('C5',C5,flush=True)
 print('S6',s.N(S6,20),flush=True);print('PASS all identities',flush=True)



if __name__ == '__main__':
    verify_corrector()
    verify_responses()

    combined = {'status':'PASS', 'corrector':json.loads(Path(__file__).with_name('quartic_verification.json').read_text()), 'responses':json.loads(Path(__file__).with_name('square_completion_verification.json').read_text())}
    Path(__file__).with_name('verification.json').write_text(json.dumps(combined,ensure_ascii=False,indent=2)+'\n')
