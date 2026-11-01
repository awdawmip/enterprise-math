#!/usr/bin/env python3
"""PREFIX-355: exact 10^-12 brackets for two guaranteed physical-source singular parameters.

The rational Gaussian centers in CENTERS_PREFIX355_PROPOSALS.json are only
proposals. Every theorem-bearing assertion is recomputed with exact Gaussian
rational arithmetic (SymPy QQ(i), Rational and integer combinatorics).
This verifies endpoint counts, not uniqueness, earliest occurrence, or fold type.
"""
import json
from pathlib import Path
from math import comb
import sympy as sp

R=sp.Rational
I=sp.I
u,v=sp.symbols('u v')
A=sp.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
q0=[R(2125,3721),R(200,3721),R(29125,29768),R(5825,7442),R(31525,59536)]
qp=[R(4),R(1),R(1),R(1),R(1)]
assert A[:3,:].det()!=0
B=sp.simplify(A[3:,:]*A[:3,:].inv())
assert B==sp.Matrix([[R(5,2)+R(9,2)*I,R(3,2)+R(7,2)*I,4*I],
                     [R(11,4)+R(15,8)*I,R(11,4)+R(15,8)*I,R(5,4)+R(9,4)*I]])
CENTERS=json.loads(Path(__file__).with_name('CENTERS_PREFIX355_PROPOSALS.json').read_text(encoding='utf-8'))
PARAMS=['0.014024659632','0.014024659633','0.066934102180','0.066934102181']
EXPECTED=[6,4,4,2]
assert sorted(CENTERS)==sorted(PARAMS)
SCALE=10**18
RAD=R(1,10**14)

def l1(z):return abs(sp.re(z))+abs(sp.im(z))
def lbi(z):return max(abs(sp.re(z)),abs(sp.im(z)))

def check_endpoint(t_str, centres, expected):
 t=R(t_str)
 q=[(1-t)*a+t*b for a,b in zip(q0,qp)]
 assert all(x>0 for x in q)
 rr=[sp.cancel(qj/q[0]) for qj in q]
 Fs=[]
 for j in range(2):
  row=list(B.row(j))
  h=row[0]+row[1]*u+row[2]*v
  hc=sp.conjugate(row[0])+sp.conjugate(row[1])*rr[1]/u+sp.conjugate(row[2])*rr[2]/v
  Fs.append(sp.Poly(sp.cancel(u*v*(h*hc-rr[j+3])),u,v,extension=I).as_expr())
 F4,F5=Fs
 raw=sp.resultant(F4,F5,v)
 P=sp.Poly(sp.cancel(raw/u),u,extension=I)
 assert P.degree()==6 and P.eval(0)!=0
 coeff=list(reversed(P.all_coeffs()))
 assert len(coeff)==7
 assert sp.gcd(P,P.diff()).degree()==0
 # Exact coefficient identity for the anti-holomorphic inversion J(u)=R2/conj(u).
 C=sp.cancel(coeff[6]/sp.conjugate(coeff[0]))
 for k in range(7):
  assert sp.cancel(coeff[k]-C*rr[1]**(6-k)*sp.conjugate(coeff[6-k]))==0, (t_str,k)
 # Each nonzero P root uniquely lifts to one nonzero v solving both F4=F5=0.
 f4,f5=[sp.Poly(f,v) for f in Fs]
 a4,b4,c4=f4.all_coeffs(); a5,b5,c5=f5.all_coeffs()
 D=sp.expand(a5*b4-a4*b5)
 E=sp.expand(a5*c4-a4*c5)
 for pol in [D,E,a4,a5]:
  assert sp.gcd(P,sp.Poly(pol,u,extension=I)).degree()==0
 e4=sp.Poly(sp.expand(a4*E**2-b4*D*E+c4*D**2),u,extension=I)
 e5=sp.Poly(sp.expand(a5*E**2-b5*D*E+c5*D**2),u,extension=I)
 Q4,rem4=sp.div(e4,P)
 Q5,rem5=sp.div(e5,P)
 assert rem4.is_zero and rem5.is_zero
 assert sp.gcd(P,Q4).degree()==0
 # Strict Gaussian-rational Rouché tests independently contain all six simple roots.
 assert len(centres)==6
 disks=[];zlist=[]
 for j,(xr,xi) in enumerate(centres):
  assert type(xr) is int and type(xi) is int
  z=R(xr,SCALE)+I*R(xi,SCALE)
  zlist.append(z)
  d=[sp.expand(sum(coeff[k]*comb(k,l)*z**(k-l) for k in range(l,7))) for l in range(7)]
  lhs=l1(d[0])+sum(l1(d[l])*RAD**l for l in range(2,7))
  rhs=lbi(d[1])*RAD
  assert 100*lhs<rhs,(t_str,'ROUCHE',j)
  x,y=abs(sp.re(z)),abs(sp.im(z))
  modulus_lower=(max(R(0),x-RAD))**2+(max(R(0),y-RAD))**2
  modulus_upper=(x+RAD)**2+(y+RAD)**2
  cls='INSIDE' if modulus_upper<rr[1] else 'OUTSIDE' if modulus_lower>rr[1] else 'ON_CIRCLE_BY_INVOLUTION'
  disks.append({'centre_numerators':[xr,xi],'class':cls})
 for i in range(6):
  for j in range(i+1,6):
   dz=zlist[i]-zlist[j]
   assert abs(sp.re(dz))>2*RAD or abs(sp.im(dz))>2*RAD,(t_str,'DISJOINT',i,j)
 # The involution preserves the ray, thus a root whose angle-sector is
 # unique among all six discs is fixed. Check strict determinant bounds
 # against every other disc to certify unique ray for each candidate.
 for i,z in enumerate(zlist):
  if disks[i]['class']!='ON_CIRCLE_BY_INVOLUTION':continue
  xi,yi=sp.re(z),sp.im(z)
  for j,w in enumerate(zlist):
   if i==j:continue
   xj,yj=sp.re(w),sp.im(w)
   det=abs(xi*yj-yi*xj)
   err=RAD*(abs(xi)+abs(yi)+abs(xj)+abs(yj))+2*RAD**2
   assert det>err,(t_str,'ANGLE',i,j)
 # Once u is J-fixed, the unique v lift must be inversion fixed as well,
 # since the original pair of complexified equations is conjugation invariant.
 nphys=sum(d['class']=='ON_CIRCLE_BY_INVOLUTION' for d in disks)
 assert nphys==expected,(t_str,'COUNT',nphys,expected)
 print('VERIFIED',t_str,'exact physical=',nphys,'algebraic roots=6','classifications=',','.join(d['class'] for d in disks),flush=True)
 return {'t':t_str,'q':[str(x) for x in q],'r2':str(rr[1]),
         'complex_algebraic_roots':6,'physical_source_count':nphys,
         'centre_scale':str(SCALE),'disk_radius':'1/100000000000000',
         'disks':disks,'certificates':{
             'rouche':'100*L1(P(c)+higher Taylor remainder)<Linfty(Pprime(c))*r, six disjoint discs',
             'simple_roots':'gcd(P,Pprime)=1',
             'reciprocal':'all 7 coefficients satisfy exact J self-inversive identity',
             'unique_lift':'gcd(P,D*E*a4*a5)=1 and both eliminated identities divisible by P',
             'physical':'circle box exclusion or unique-angle inversion fixed point',
             'regularity':'simple P roots with unique regular v lift imply nonzero physical angular Jacobian'
             }}

results=[]
for t,c in zip(PARAMS,EXPECTED): results.append(check_endpoint(t,CENTERS[t],c))
assert [x['physical_source_count'] for x in results]==[6,4,4,2]
assert R(PARAMS[1])-R(PARAMS[0])==R(1,10**12)
assert R(PARAMS[3])-R(PARAMS[2])==R(1,10**12)
output={
 'schema':'ENTERPRISE_MATH_PREFIX355_TWO_EXACT_MICROBRACKETS_V1',
 'claim':'Two disjoint OPEN intervals each contain at least one physical-source Jacobian-singular t',
 'mathematics':'Static auxiliary complex 3-to-5 measurement phase retrieval, all five exact intensities, sources modulo global U(1)',
 'scientific_status':'AUTHOR_EXACT_CERTIFICATE_UNREVIEWED_NOT_ADMITTED',
 'fixed_input':{'A_gaussian_integer':[[str(x) for x in A.row(i)] for i in range(5)],'q0':[str(x) for x in q0],'qplus':[str(x) for x in qp]},
 'endpoint_certificates':results,
 'guaranteed_singular_parameter_intervals':[
    {'open_interval':[PARAMS[0],PARAMS[1]],'width':'1/1000000000000','endpoint_counts':[6,4]},
    {'open_interval':[PARAMS[2],PARAMS[3]],'width':'1/1000000000000','endpoint_counts':[4,2]}],
 'logic':'The physical solution set is compact over each parameter interval because q1..q3 are positive and fix two phases. If all physical angular Jacobians were nonsingular, local implicit continuation plus compactness would make fibre cardinality constant. Endpoint counts differ, hence at least one singular point in each disjoint open interval.',
 'limitations':{'first_guaranteed_singularity_is_earliest_from_t0':False,'unique_singularity_in_each_bracket':False,'fold_type':False,'native_X6_or_timing_transfer':False},
 'next':'Derive a parameter-uniform discriminant/square-free certificate and prove exclusion of all earlier/extra physical Jacobian singularities, then certify fold transversality.'
}
path=Path(__file__).with_name('RESULTS_PREFIX355.json')
path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS_PREFIX355_EXACT_TWO_1E12_SINGULAR_BRACKETS')
