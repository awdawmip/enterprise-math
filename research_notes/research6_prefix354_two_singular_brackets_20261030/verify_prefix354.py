#!/usr/bin/env python3
"""PREFIX-354: five fully exact endpoint fibre counts, two certified singular intervals.

Numerical root finding is NOT run here. Fixed rational Gaussian centres are proposals;
all mathematical decisions use exact SymPy QQ(i) and rational inequalities.
"""
import json
from pathlib import Path
from math import comb
import sympy as sp

R=sp.Rational; I=sp.I; u,v=sp.symbols('u v')
A=sp.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B=sp.simplify(A[3:,:]*A[:3,:].inv())
assert B==sp.Matrix([[R(5,2)+R(9,2)*I,R(3,2)+R(7,2)*I,4*I],[R(11,4)+R(15,8)*I,R(11,4)+R(15,8)*I,R(5,4)+R(9,4)*I]])
q0=[R(2125,3721),R(200,3721),R(29125,29768),R(5825,7442),R(31525,59536)]
qp=[R(4),R(1),R(1),R(1),R(1)]

# These rational Gaussian disk centres are NOT certified roots by assumption.
# The six roots must instead be justified from exact Rouché inequalities below.
CENTERS={
 "0": [
 [-275856876340,134240943213],[-268853606484,-147768011895],
 [-268275513555,-148814971981],[258823529412,-164705882353],
 [266677982345,-151659159933],[284239753519,115435737873]],
 "1753/125000": [
 [-311107296706,107016972019],[-292025460110,-151530567910],
 [-282720676808,-168253978464],[223968437332,-240994857711],
 [224361175359,-240629269531],[225346042223,239707203934]],
 "561/40000": [
 [-311109487737,107014942081],[-292027013259,-151530639526],
 [-282721695996,-168255026081],[224031110524,-240675375263],
 [224293729207,-240957505052],[225341837434,239713094115]],
 "33467/500000": [
 [-373194112799,-83511857711],[-373089692106,-83977126950],
 [-357261387913,-136427185387],[36861762263,380643253834],
 [89160178829,-237206057941],[203056147643,-540220409555]],
 "13387/200000": [
 [-373832853539,-83899794626],[-372453689423,-83590267025],
 [-357262354194,-136426691084],[36858825759,380644267956],
 [89159070638,-237205619525],[203055677699,-540224875404]]
}
EXPECTED={"0":6,"1753/125000":6,"561/40000":4,"33467/500000":4,"13387/200000":2}
SCALE=10**12; RAD=R(1,10**9)

def lc(z): return abs(sp.re(z))+abs(sp.im(z))
def lower(z): return max(abs(sp.re(z)),abs(sp.im(z)))

def checked_fibre(tkey,centers):
 t=R(tkey)
 q=[(1-t)*a+t*b for a,b in zip(q0,qp)]
 assert all(qj>0 for qj in q)
 rr=[sp.cancel(qj/q[0]) for qj in q]
 Fs=[]
 for k in range(2):
  c=list(B.row(k));h=c[0]+c[1]*u+c[2]*v
  hc=sp.conjugate(c[0])+sp.conjugate(c[1])*rr[1]/u+sp.conjugate(c[2])*rr[2]/v
  Fs.append(sp.Poly(sp.cancel(u*v*(h*hc-rr[k+3])),u,v,extension=I).as_expr())
 F4,F5=Fs
 resultant=sp.resultant(F4,F5,v)
 p=sp.Poly(sp.cancel(resultant/u),u,extension=I)
 assert p.degree()==6 and p.eval(0)!=0
 coeff=list(reversed(p.all_coeffs()))
 assert len(coeff)==7
 assert sp.gcd(p,p.diff()).degree()==0
 r2=rr[1]
 C=sp.cancel(coeff[6]/sp.conjugate(coeff[0]))
 for k in range(7):
  assert sp.cancel(coeff[k]-C*r2**(6-k)*sp.conjugate(coeff[6-k]))==0,(tkey,'selfinverse',k)
 # For every P root the two original complexified equations have exactly one v,
 # excluding spurious resultant factors, v=0, and singular complex points.
 f4,f5=[sp.Poly(f,v) for f in Fs]
 a4,b4,c4=f4.all_coeffs();a5,b5,c5=f5.all_coeffs()
 D=sp.expand(a5*b4-a4*b5);E=sp.expand(a5*c4-a4*c5)
 for w in [D,E,a4,a5]:
  assert sp.gcd(p,sp.Poly(w,u,extension=I)).degree()==0,(tkey,'gcd')
 e4=sp.Poly(sp.expand(a4*E**2-b4*D*E+c4*D**2),u,extension=I)
 e5=sp.Poly(sp.expand(a5*E**2-b5*D*E+c5*D**2),u,extension=I)
 Q4, rem4=sp.div(e4,p);Q5,rem5=sp.div(e5,p)
 assert rem4.is_zero and rem5.is_zero
 assert sp.gcd(p,Q4).degree()==0
 # Strict rational Rouché disk checks, six distinct disks exhaust degree 6.
 zlist=[R(x,SCALE)+I*R(y,SCALE) for x,y in centers]
 disks=[]
 for i,z in enumerate(zlist):
  ds=[sp.expand(sum(coeff[j]*comb(j,k)*z**(j-k) for j in range(k,7))) for k in range(7)]
  lhs=lc(ds[0])+sum(lc(ds[k])*RAD**k for k in range(2,7))
  rhs=lower(ds[1])*RAD
  assert 100*lhs<rhs,(tkey,'Rouche',i)
  x=abs(sp.re(z));y=abs(sp.im(z))
  low=(max(R(0),x-RAD))**2+(max(R(0),y-RAD))**2
  high=(x+RAD)**2+(y+RAD)**2
  classif='inside' if high<r2 else 'outside' if low>r2 else 'candidate'
  disks.append({'center':list(centers[i]),'class':classif})
 for i,z in enumerate(zlist):
  for j,w in enumerate(zlist):
   if i>=j:continue
   assert abs(sp.re(z-w))>2*RAD or abs(sp.im(z-w))>2*RAD,(tkey,'overlap',i,j)
 # If candidate's angle cannot equal any other disk's angle,
 # the anti-holomorphic radial involution must fix its unique root.
 # Determinant bound is rigorous for all points in the two radius-RAD disks.
 for i,z in enumerate(zlist):
  if disks[i]['class']!='candidate':continue
  xi,yi=sp.re(z),sp.im(z)
  for j,w in enumerate(zlist):
   if j==i:continue
   xj,yj=sp.re(w),sp.im(w)
   determinant=abs(xi*yj-yi*xj)
   error=RAD*(abs(xi)+abs(yi)+abs(xj)+abs(yj))+2*RAD**2
   assert determinant>error,(tkey,'angle not isolated',i,j)
 nphysical=sum(d['class']=='candidate' for d in disks)
 assert nphysical==EXPECTED[tkey],(tkey,nphysical)
 print('VERIFIED',tkey,'physical=',nphysical,'complexified=6','classifications=',','.join(d['class'] for d in disks),flush=True)
 return {'t':tkey,'q':[str(x) for x in q],'r2':str(r2),'physical_source_count':nphysical,
         'complex_algebraic_source_count':6,'disk_radius':'1/1000000000','center_scale':SCALE,
         'disk_classifications':disks,
         'certificate':{'rouche':'100*LHS<RHS in each of six disks',
            'radial_exclusion':'entire candidate disks rigorously off/on circle',
            'fixedpoint':'self-inversive sextic plus isolated angular sectors',
            'v_recovery':'exact polynomial divisibility and coprimality',
            'jacobian':'simple P roots and nonzero reduced complex Jacobian'}}

results=[checked_fibre(k,CENTERS[k]) for k in EXPECTED]
assert [x['physical_source_count'] for x in results]==[6,6,4,4,2]
output={
 'schema':'ENTERPRISE_MATH_PREFIX354_TWO_SINGULAR_BRACKETS_V1',
 'mathematics':'auxiliary static C^3 five-Port full exact-intensity source fibres modulo U(1)',
 'research_status':'AUTHOR_EXACT_CERTIFICATE_UNREVIEWED_NOT_ADMITTED',
 'point_certificates':results,
 'existence_of_distinct_real_jacobian_singular_parameters':{
  'first_guaranteed_interval':['1753/125000','561/40000'],
  'second_guaranteed_interval':['33467/500000','13387/200000'],
  'proof':'different nonsingular full-source fibre counts at interval endpoints plus properness and implicit function theorem',
  'first_true_critical_parameter_isolated':False,
  'unique_critical_parameter_per_bracket':False,
  'fold_local_type_proved':False,
 },
 'model_limits':'No original X6 time evolution, no native slice/third-coordinate transfer and no mathematical admission.',
 'next':'Prove absence of earlier or additional Jacobian critical points with a complete real discriminant or interval-continuation proof; classify each guaranteed collision.'
}
path=Path(__file__).with_name('RESULTS_PREFIX354.json')
path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS_PREFIX354_EXACT_TWO_DISJOINT_SINGULAR_PARAMETER_BRACKETS')
