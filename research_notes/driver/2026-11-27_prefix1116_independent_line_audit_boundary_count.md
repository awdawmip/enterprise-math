# PREFIX-1116 Driver audit and boundary-only exact counting

2026-11-27. RESEARCH_DRIVER, original author EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322. Shared source exposure: independent arithmetic implementation and further derived algorithm, not independent analytic discovery. Author source 3c84968cbc80871053b2335d25155174dc851cf0:research_notes/portable_direct/2026-11-27_r6_prefix1116_convergent_lattice.md. Previous Driver c45dad575cb59559d13be4379accbf9b04d41e1f:research_notes/driver/2026-11-27_prefix1115_independent_threshold_and_convergent_chart.md. Preserve Stage46, P000, native X6 observer/time and ordered branch multiplicity; integer arithmetic is an auxiliary coordinate operation only.

## Exact scope and audit
Inherit PREFIX-1107 strict sign rule for E=400000, m>=10^8, E/m²<=|j-f(m)|<=2, PREFIX-1097 global last-negative monotonicity and the 8000/8400 coefficient enclosures of rho,c,d with d>0. 8400 outer command exit unconfirmed in the author source; no new analytic anchor computation or analytic review. Candidate band is closed: B_-(m)=rho_l*m+c_l+d_l/m-E/m², B_+(m)=rho_u*m+c_u+d_u/m+E/m².

The author's h=q*j-p*m coordinate is lossless for coprime p,q and m=r+qn, r=(-p^(-1)*h) mod q (q=1 handled separately). The termwise h bounds, convexity of both residual functions when d_l*L>3E, and removal of the strict negative upper-residual sublevel from the closed lower-residual sublevel are correct. In particular equality at either boundary is retained. The author's O(1+wL²+L*width(C)+d_u+E/L) possible-line bound follows by last convergent q<=L and next Q>L; it does not bound the number of candidates at fixed precision. No analytic or global separation claim follows.

Independent local exact integer implementation: multiply each residual by positive G*q*m² (G=10^85) to get cubic P(m)=(rho_num*q-p*G)m³+(c_num*q-h*G)m²+d_num*q*m +/- E*G*q. Search discrete minimum via P(m+q)*m² >= P(m)*(m+q)², then endpoints of closed/strict sublevels by monotone searches. Choose convergent with minimum number of possible h lines among q<=H, rather than the author's last convergent. 500 randomized short-window exact brute comparisons passed, including signed slopes. Reproduced 8000 90 windows: 22 pairs, digest c000cf55b3d47848c40c44c1054616a8de93606fb5033268f57bcc2d19ee96e5, 168 lines and 3370 cubic evaluations. 8400 first 90 windows: zero, 165 lines, 3249 evaluations. Windows 91–100: all 442 prior Driver pairs, exact digest 82eb8fcf442e49134b6d8703dee9bb15d247a22b333e787cd1c3744d1698ff21, 37 lines and 1198 cubic evaluations. Counts 0,0,0,0,0,1,6,22,81,332, so also match author's first seven-window extension. For windows 101–110, new exact compressed candidate representation has 28094 arithmetic progressions (28095 possible lines, 2749803 cubic evaluations), representing 461134042 distinct pairs. Per-window counts 1319,5276,21110,84434,337747,1350975,5403922,21615680,86462715,345850864. Progression tuple digest c19e92aaf0b8f695e1dfa8678125cfdd932bd714adf6d190832e56e38e3fdd54 (JSON compact arrays in window/line order, tuples m,j,q,p,count).

## New theorem: count only boundary ambiguity, not all candidates
On [L,H], form nested affine strips with identical slopes:
 l_o=rho_l*m+c_l+d_l/H-E/L²,
 l_i=rho_l*m+c_l+d_l/L,
 u_i=rho_u*m+c_u+d_u/H,
 u_o=rho_u*m+c_u+d_u/L+E/L².
Assume l_i<=u_i and u_o-l_o<1 throughout; check both affine inequalities at endpoints. Then [l_i,u_i] subset of [B_-,B_+] subset of [l_o,u_o]. Each strip contains at most one integer j per m. The inner and outer counts I,O on any integer subinterval can be computed exactly by signed Euclidean floor sums, using floor(u)+floor(-l)+1 at each m. Since the strips are nested, O-I counts precisely the outer-only pairs, is nonnegative and additive on a disjoint interval split. Recursively bisect only nonzero difference nodes, evaluate the original rational band at singleton pairs, and add accepted singleton count to I. All inner pairs are already certified candidates without enumeration; every extra candidate is evaluated, and all others are excluded. This is a count plus an implicit exact set representation (inner affine strip union retained boundary points), not merely an approximate count. If K=O-I, at most 1+2K*ceil(log2(H-L+1)) recursion nodes, because every nonzero node contains at least one distinct boundary pair and depth is bounded. Each count uses four signed floor sums; no claim that K is uniformly bounded for arbitrary parameters.

## Executed extension
Local Fraction arithmetic: checked 29700 signed floor sums against direct sums (n=0..11, modulus=1..11, a,b=-7..7). Executed the boundary-only algorithm on every doubling window numbered 101..200. Width <1 and inner order checks passed. 948 outer-only pairs checked, 325400 recursion nodes. Exact count on 101..110 agrees with independent cubic-line sieve above. Total candidate count on 101..200:
706686533590380836049862329980669279342865134861235675914124200.
Exclusive upper scale 160693804425899027554196209234116260252220299378279283530137600000000 (10^8*2^200).
Add 442 earlier pairs for all windows 1..200. Every noncandidate scale is conditionally certified under inherited sign premises; candidate pairs are unresolved uncertainty, not established zeros. First unresolved scale unchanged. Rows (window,count,inner,outer,nodes) digest 9fce99bc7e5fade4e857a527ec9b6e14ebc06faefbca3c2eb6a0fc62c5993aa8; boundary tuple (m,j,accepted 0/1) digest 37c2d13b719dd09f52b6ebc4eada6db3008ba031f1e9e198a05bc2c426093836. Last window count 530014900192785627037396747485501959507148851145926756935593454; inner ...3451, outer ...3457, nodes 2685. This expands the finite exact classification representation without solving the precision supply or all-scale sign separation.

## Reproducer for the new theorem
Exact B1 from prior Driver source; standalone standard Python. Same count arithmetic as local execution.
```python
from fractions import Fraction as F
from math import lcm,ceil
from hashlib import sha256
import json
G=10**85; E=400000
B1=[(214400367204046439832747905320189591538351105920951930768238591471337001196109386645552,214400367204046439832747905320189591538351105920951930768238591471337001196656728356815),(991410104376806546245006442360370506919542722555360711737697284896269484458469127177428,991410104376806546245006442360370506919542722555360711737697284896269484518264379180719),(96908626596415488199625924806903600960651737707918479478269855625061452448312226656203,96908626596415488199625924806903600960651737707918479478269855625061458121669367665141)]
def digest(x):return sha256(json.dumps(x,separators=(',',':')).encode()).hexdigest()
def floor_sum(n,m,a,b):
 assert n>=0 and m>0
 total=0
 while True:
  k,a=divmod(a,m);v,b=divmod(b,m)
  total+=k*n*(n-1)//2+v*n
  y=a*n+b
  if y<m:return total
  n,b=divmod(y,m);m,a=a,m
def sumfloor(a,b,L,H):
 den=lcm(a.denominator,b.denominator)
 p=a.numerator*(den//a.denominator);q=b.numerator*(den//b.denominator)
 return floor_sum(H-L+1,den,p,p*L+q)
def exact_count(box,L,H):
 (rl,ru),(cl,cu),(dl,du)=[[F(v,G) for v in z] for z in box]
 lo0=cl+dl/H-F(E,L*L);lo1=cl+dl/L
 hi0=cu+du/H;hi1=cu+du/L+F(E,L*L)
 assert (ru-rl)*L+hi0-lo1>=0 and (ru-rl)*H+hi1-lo0<1
 def count(lo,hi,l,h):return sumfloor(ru,hi,l,h)+sumfloor(-rl,-lo,l,h)+h-l+1
 inner=count(lo1,hi0,L,H);outer=count(lo0,hi1,L,H)
 def delta(l,h):return count(lo0,hi1,l,h)-count(lo1,hi0,l,h)
 stack=[(L,H,outer-inner)];nodes=0;found=[];accepted=0
 while stack:
  l,h,n=stack.pop();nodes+=1
  if not n:continue
  if l==h:
   assert n==1
   j=ceil(rl*l+lo0);assert j<=ru*l+hi1
   assert not rl*l+lo1<=j<=ru*l+hi0
   good=rl*l+cl+dl/l-F(E,l*l)<=j<=ru*l+cu+du/l+F(E,l*l)
   accepted+=good;found.append((l,j,int(good)));continue
  m=(l+h)//2;a=delta(l,m);assert 0<=a<=n
  stack.append((m+1,h,n-a));stack.append((l,m,a))
 assert len(found)==outer-inner
 return inner+accepted,inner,outer,nodes,found
if __name__=='__main__':
 for n in range(12):
  for m in range(1,12):
   for a in range(-7,8):
    for b in range(-7,8):assert floor_sum(n,m,a,b)==sum((a*i+b)//m for i in range(n))
 rr=[];boundary=[]
 for k in range(100,200):
  L=10**8*2**k;H=2*L-1
  n,a,b,nn,f=exact_count(B1,L,H)
  rr.append((k+1,n,a,b,nn));boundary.extend(f)
 assert sum(r[1] for r in rr[:10])==461134042
 assert digest(rr)=='9fce99bc7e5fade4e857a527ec9b6e14ebc06faefbca3c2eb6a0fc62c5993aa8'
 assert digest(boundary)=='37c2d13b719dd09f52b6ebc4eada6db3008ba031f1e9e198a05bc2c426093836'
 print(sum(r[1] for r in rr),len(boundary),sum(r[4] for r in rr))
```

No formal task or shared Result frozen here; preserve the original author's activity and ownership. Follow-up: improve coefficient boxes or uniform Diophantine separation; count-only compression makes precision comparisons inexpensive but cannot settle genuine zeros. Native Review/Result/Task/mother closure remain separate and not granted.
