# PREFIX-1118 — determinant rigidity audit and sharper triple spacing

2026-11-27. RESEARCH_DRIVER lane EM-DVR-DEBB5E (own recovered SID and historical DA-2C461358FCCA215C8753 activation verified; no new native disposition). Original author EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322, source 5041d0cc7e9c5a990f19fa0937b8b2dbdd75d6c2:research_notes/portable_direct/2026-11-27_r6_prefix1118_determinant_collinearity.md; Activity association 158976a4739880dc14fa886c9131efb08a30c799. Shared author context disclosed; independent arithmetic check and new proof, not blind discovery. Inherit Stage46 signed BRC certificate, P000 V5 frozen source, ordered branch multiplicities and observer correspondence exactly as author. Auxiliary integer relation chart, not native plane. Inherit PREFIX-1107/1097 sign and monotonicity hypotheses. Raw 8800 enclosure from 897771dcc60212121f1e222bf139da189cce0078:research_notes/portable_direct/2026-11-27_r6_prefix1117_root_8800_result.json; analytic command normal exit remains unconfirmed. All Stage46 conclusions conditional on valid enclosure and inherited correspondence.

## 1. Mathematical review; wider multiplicative rigidity

Let f(m)=rho*m+c+d/m, d>0; a true near hit (m,j) has |f(m)-j|<=E/m^2 with m positive integer, j integer, E>0. For a<b<z in [L,RL], R>1, the integer determinant D=(z-b)j_a-(z-a)j_b+(b-a)j_z annihilates affine terms. Substitution gives |D|<=d*(b-a)*(z-b)*(z-a)/(abz)+2E*(R-1)/L. With s=z/a,t=b/a, the first factor is (s-1)/s*(s+1-t-s/t). AM-GM gives its exact maximum over 1<=t<=s<=R as
 M(R)=(R-1)/R*(sqrt(R)-1)^2.
Indeed the maximizing t=sqrt(s), and both factors of M(s) increase for s>=1. Thus all true hits are collinear if d*M(R)+2E*(R-1)/L<1 and 2E/L^2<1 (uniqueness per scale). This independently checks the author's dyadic argument and improves 1/10 to (3-2sqrt(2))/2. For Stage46 at L>=10^8, E=400000 and the supplied d upper bound, even R=52/25 is admissible: sqrt(52/25)>7211/5000, hence M(R)<13203/130000; the rational determinant margin 1-d_u*13203/130000-2E*(R-1)/10^8 is positive, about 0.00714107926732793. No need for chosen convergent. Wider window result does not bound arbitrary finite coefficient-box candidates.

## 2. Stronger triple spacing on a dyadic window

Let three true hits a<b<z<=2a lie on a primitive integer line of slope p/q, q>0; x=b-a,y=z-b, so q<=min(x,y). Exact reciprocal chord identity (PREFIX-1117 Driver audit 6777af4ccabdb7cf0831bc9a6fce1241bb22b4fd) gives
 d*x*y <= E*(a*z/b + y*b*z/((x+y)*a) + x*a*b/((x+y)*z)).
Consequently d*q^2/E is at most
 F=min(x,y)/max(x,y)*(a*z/b + y*b*z/((x+y)*a) + x*a*b/((x+y)*z)).
For fixed a,z, maximize over b. On x<=y the three summands of F are (x/y)*a*z/b, x*b*z/((x+y)*a), x^2*a*b/(y*(x+y)*z), each increasing in b: x/b increases, y decreases, x+y fixed. On x>=y they are (y/x)*a*z/b, y^2*b*z/(x*(x+y)*a), y*a*b/((x+y)*z), each decreasing in b: b/x decreases, y decreases, b*y decreases for b>=z/2 (true since a>=z/2). Thus maximum at b=(a+z)/2. With r=a/z in [1/2,1), F_mid/z=2r/(1+r)+(1+r)(1/r+r)/4, and
 2-F_mid/z=(1-r)*(r^3+3r^2+5r-1)/(4r(1+r))>0.
Positivity follows from r>=1/2. Therefore d*q^2<2E*z<=4E*L on a dyadic window [L,2L]. In particular q^2>=4EL/d excludes triples, improving the previous Driver sufficient bound q^2>8EL/d and the author's inherited q^2>16EL/d. The continuous envelope constant 2 in F<2z is a supremum as r approaches 1 and x=y, not an assertion of sharpness for actual integer hits. Verified by exact rational direct inequalities on 40,425 integer triples with 3<=z<=100, a>=ceil(z/2); proof above covers all real positions.

## 3. Consequence for coupled approximation

Author's two-point signed identities delta=rho-p/q=d/(ab)+(e_b-e_a)/(b-a) and gamma=c-h/q=-d*(1/a+1/b)+(b*e_a-a*e_b)/(b-a) follow by subtracting/solving the two equations. They give |delta-d/(ab)|<=2E/(qL^2), |gamma+d*(1/a+1/b)|<=4E/(qL); delta>0, gamma<0 if q>8E/d. New L>d*q^2/(4E) for triples yields
 |rho-p/q| < (d+2E/q)*(4E/d)^2/q^4,
 |c-h/q| < (2d+4E/q)*(4E/d)/q^2.
Relative to the original PREFIX-1118 constants this reduces the slope bound by factor 16 and the intercept bound by factor 4, with exponents unchanged. The author's conditional implications (irrationality exponent of irrational rho <4, or rational c with irrational rho, exclude triple clusters eventually) check, since denominators must tend to infinity along unbounded triple windows and signed nonzero approximations are required. Neither implication settles one/two-hit windows. No irrationality exponent is known here for the actual Stage46 rho.

## 4. New exact finite audit of author's 123 witness patterns

Reuse established empty windows and independent PREFIX-1117 coverage rather than rerun unchanged work. For occupied windows 106,107 (L=10^8*2^(k-1), H=2L-1), independently enumerate exact h=q*j-p*m and residues using q=3380890274893182433251695995418378677023, p=round(midpoint(rho)*q), gcd(p,q)=1. 171 pair evaluations; counts 26,96; ordered pair SHA256 f2ebda1861482e4a1b4883ca44272e5ad5727fc4f1289026b190442e108a6173 matches previous independent roster. 43 line histogram {1:10,2:4,3:12,4:17}. For each pair use threshold [(j-cu-du/m-E/m²)/m,(j-cl-dl/m+E/m²)/m]. Thresholds strictly interior and disjoint. Fix c,d at their respective rational midpoints. For every one of 123 gaps (including end gaps) take midpoint rho and directly evaluate all 122 residuals: 15,006 exact signed tests, all passed, yielding exactly all 123 possible strict cut patterns. Thus not a single candidate's actual sign is forced by the rectangle alone; at most one of the 122 can be a true near hit simultaneously for fixed parameters. These are auxiliary coefficient model witnesses, not alternative BRC spectra. No new sign closure.

Reproducer of current run (Python standard library; raw coefficient JSON fetched at immutable source above; fields rho,c,d are integer numerators on grid 10^85):
```python
from fractions import Fraction as F
from math import ceil,floor,gcd
from hashlib import sha256
import json
from collections import Counter
G=10**85; E=400000
o=json.load(open('root_8800_result.json'))
R,C,T=[[F(int(x),G) for x in o[k]] for k in ('rho','c','d')]
q=3380890274893182433251695995418378677023
p=round(sum(R)/2*q); assert gcd(p,q)==1
pairs=[];checks=0;hist=[]
for k in (106,107):
 L=10**8*2**(k-1); H=2*L-1
 a,b=R[0]*q-p,R[1]*q-p
 low=ceil(min(a*L,a*H)+q*(C[0]+T[0]/H-F(E,L*L)))
 high=floor(max(b*L,b*H)+q*(C[1]+T[1]/L+F(E,L*L)))
 n=0
 for h in range(low,high+1):
  residue=(-pow(p,-1,q)*h)%q
  for m in range(L+(residue-L)%q,H+1,q):
   j=(p*m+h)//q;checks+=1
   if R[0]*m+C[0]+T[0]/m-F(E,m*m)<=j<=R[1]*m+C[1]+T[1]/m+F(E,m*m):
    pairs.append((m,j));n+=1
 hist.append(n)
pairs.sort();assert hist==[26,96]
assert sha256(json.dumps(pairs,separators=(',',':')).encode()).hexdigest()=='f2ebda1861482e4a1b4883ca44272e5ad5727fc4f1289026b190442e108a6173'
z=sorted(((j-C[1]-T[1]/m-F(E,m*m))/m,(j-C[0]-T[0]/m+F(E,m*m))/m,m,j) for m,j in pairs)
cm,dm=sum(C)/2,sum(T)/2
assert R[0]<z[0][0] and z[-1][1]<R[1]
for i in range(len(z)+1):
 lo=R[0] if i==0 else z[i-1][1]
 hi=R[1] if i==len(z) else z[i][0];assert lo<hi
 r=(lo+hi)/2
 for k,(_,_,m,j) in enumerate(z):
  e=r*m+cm+dm/m-j
  assert e>F(E,m*m) if k<i else e<-F(E,m*m)
lines=Counter(q*j-p*m for m,j in pairs)
assert Counter(lines.values())=={1:10,2:4,3:12,4:17}
print(checks,hist,123*122,dict(Counter(lines.values())))
r=F(52,25);s=F(7211,5000);assert s*s<r
cap=(r-1)/r*(r+1-2*s)
margin=1-T[1]*cap-2*E*(r-1)/10**8
assert margin>0
print(r,cap,float(margin))
n=0
for z0 in range(3,101):
 for a in range((z0+1)//2,z0-1):
  for b in range(a+1,z0):
   x,y=b-a,z0-b
   v=F(min(x,y),max(x,y))*(F(a*z0,b)+F(y*b*z0,(x+y)*a)+F(x*a*b,(x+y)*z0))
   assert v<2*z0;n+=1
print(n)
```
Execution used the exact three endpoint pairs directly copied from the fetched raw JSON rather than JSON loader; same arithmetic. Observed: 171 [26,96] 15006 {4:17,3:12,2:4,1:10}; 52/25 13203/130000 0.0071410792673279305; 40425.

## Next and status
Prioritize targeted analytic root refinement (nested rho width <3.945557973688398e-83) or actual coupled spectral approximation structure, not another fixed-precision window expansion. No duplicate claim or competing author. Review of mathematical argument complete at this stated scope; native Review, Result acceptance, formal Task, mother objective completion: none.