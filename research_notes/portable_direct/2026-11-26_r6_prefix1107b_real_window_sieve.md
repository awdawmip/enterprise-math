# PREFIX-1107b -- Two real Stage46 dyadic windows have no integer-edge candidates

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_COMPUTATION / NOT_REVIEWED. Same R6 own Activity and owner snapshot as PREFIX-1107, no new claim or shared state transition. Same frozen Stage46 signed BRC joint observer and P000 pin; exact auxiliary integer-edge calculation, not a native propagation run.

Parents: 7e95625df3a8c21b6d370246065d51469afa6345:research_notes/portable_direct/2026-11-26_r6_prefix1107_signed_density_jet.md; f6903fef5f9c2eae033eb4524c62bc67b437e3d5:research_notes/portable_direct/2026-11-26_r6_prefix1107_signed_density_jet.py; 3dbbec783d4eb0f6ae1ca4909f7b535c6f0e8cf5:research_notes/portable_direct/2026-11-26_r6_prefix1099_reanchored_large_scale_sign.md (actual certified 25-decimal anchor intervals); 0919218e87c1f6a094123bb19ff315c17846b778:research_notes/portable_direct/2026-11-26_r6_prefix1096_second_order_last_negative_edge.md (exact rho,c,d formulas); acd24d8499f11d2b8faa6cd0fd8567735f295333:research_notes/portable_direct/2026-11-26_r6_prefix1104_compressed_exception_sieve.md.

## Result

The actual Stage46 parameter windows [100000000,200000000) and [1000000000,2000000000) contain zero points in the conservative integer-edge outer strips. Thus every one of the 1100000000 integer m in these two DISJOINT windows has an exact global last-negative integer given by the single rational floor formula

  K_last(m) = floor((42880073440809287966549749811773*m + 198282020875361309249001917399666 + 19381725319283097639924876692052/m)/(2*10^30)).

No high-cost CT sign fallback or fast sign oracle call is needed for these windows. This is a compressed certificate of all rows in the two windows, not a claim that individual rows were generated or that the intervening gap was certified. Inherit the exact BRC radial observer correspondence and PREFIX-1107 monotonicity/sign-band assumptions.

## Proof and actual calculation

Re-use the already certified 1099 25-decimal anchor boxes, and reconstruct the same signed numerator center with n<=80 and differentiated geometric tails to order 4, paying the parameter radii after signed assembly. Shift the polynomial to the midpoint of the inherited root enclosure before exact interval evaluation. Round each shifted coefficient downward on the grid 10^-60, pay its actual weighted residual (including derivatives). Calculated total F derivative errors j=0..4: [8.459310044342007e-12,3.421266224268369e-11,1.2705231765099551e-10,4.423184256728191e-10,1.511219560949264e-09], display only. For the certified simple root t*, use the mean-value identity t*=mid-F(mid)/F'(xi) with xi in the current interval; F' strictly negative on each enclosure. Intersect the interval quotient with the inherited enclosure, outward rounding on 10^-40. Four contractions were actually executed; widths [8.442014820675609e-21,1.7680224764319804e-21,1.7680224764319804e-21,1.7680224764319804e-21]. Use exact x-jet coefficients through degree 4, with F0=0 only at the actual root, to compute r2,r3,r4 and the 1096 formulas.

Outward enclosures for (rho,c,d), integer endpoints divided by 10^30:
rho [21440036720404643983243551290966,21440036720404643983306198520807]
c [99141010437680654620437916203756,99141010437680654628564001195910]
d [9690862659641548432988461360525,9690862659641549206936415331527].
Their midpoint rational function fhat(m)=rhohat*m+chat+dhat/m is exactly the expression in the displayed floor formula. Let eps_r,eps_c,eps_d be the half widths of these outward enclosures. For all M<=m<2M,

  m^2|f(m)-fhat(m)| <= eps_r*(2M)^3+eps_c*(2M)^2+eps_d*2M.

This pays the true coefficient uncertainty without pretending to meet the narrower sufficient precision rule of 1104. Use A=400000+ceil(the RHS), and apply the 1104 rational strip geometry directly; its proof only needs A<M and 9<dhat<10. For each of four consecutive integer subblocks [l,h], construct secant H(m)=(rhohat-dhat/(l*h))*m+chat+dhat*(l+h)/(l*h). It obeys H-fhat=dhat*(m-l)*(h-m)/(l*h*m). The strip
  H(m)-dhat*(h-l)^2/(4*M^3)-A/M^2 <= j <= H(m)+A/M^2
contains every point |j-fhat(m)|<=A/m^2. Width <1 and determinant bound <1 are checked exactly. Count all lattice points by the exact signed Euclidean floor-sum recurrence of 1104. Actual counts:
M=10^8, A=650590: [0,0,0,0] on the four subblocks.
M=10^9, A=250988936: [0,0,0,0] on the four subblocks.
Hence no integer in either window is within A/m^2 of fhat. Both floor(fhat) and its successor are strictly beyond C/m^2 on the respective sides of f(m); they are within |e|<=2 (A<M and fhat-f bounded above). PREFIX-1107 strict signs plus PREFIX-1097 infinite-tail monotonicity imply the exact floor formula. This directly certifies the integer endpoint without even the fast oracle. The finite exact calculation used Fraction and integer floor division; no floating decision, no scanning of 1.1 billion scales.

## Reproduction extension

Append the following code to the immutable PREFIX-1107 companion. The local calculation executed these equivalent cells after its reconstruction. The concatenated file has not been rerun as one standalone script.

```python
anchors25=[[1684139808832244674612244,1684139808832244674612245],[403144180414993614805275,403144180414993614805276],[-109220034251684978380170,-109220034251684978380169],[-1,1],[336827961766448934922448,336827961766448934922449],[28068996813870744576870,28068996813870744576871]]
c25=[F(l+u,2*10**25) for l,u in anchors25]; r25=[F(u-l,2*10**25) for l,u in anchors25]
assert all(c-r>=l-r0 and c+r<=l+r0 for c,r,l,r0 in zip(c25,r25,centers,rad))
cut2=80; degree2=2*(cut2+2+10); polys2=[]
for a,z,h,T in basis:
 pol=[F(0)]*(degree2+1); off=int(2*a)
 for n in range(cut2+1):
  for i,cc0 in enumerate(z[n]+[h[0][n],h[1][n]]):
   for k,w in enumerate(nums[i]): pol[off+2*(n+k)]+=cc0*w
 polys2.append(pol)
for j in range(2):
 pol=[F(0)]*(degree2+1)
 for k,w in enumerate(nums[7+j]): pol[2*(k+j)]=F(w)
 polys2.append(pol)
center2=[sum(c*p[i] for c,p in zip(c25,polys2)) for i in range(degree2+1)]
t02=(lo+hi)/2; D0=10**60
sh2=[sum(center2[k]*comb(k,j)*t02**(k-j) for k in range(j,len(center2))) for j in range(len(center2))]
rounded2=[F((a*D0).numerator//(a*D0).denominator,D0) for a in sh2]
rerr=[a-b for a,b in zip(sh2,rounded2)]
terr2=[]
for a,z,h,T in basis:
 off=int(2*a); J=N+1; out=[]
 for j in range(5):
  e=sum(max(abs(v) for v in z[n]+[h[0][n],h[1][n]])*falling(off+2*n,j)*tmax**(off+2*n-j) for n in range(cut2+1,N+1)); p=off+2*J; ratio=tmax*tmax/2*F(p+2-j+1,p-j+1)**j; assert ratio<1
  e+=64*T*F(1,2)**J*falling(p,j)*tmax**(p-j)/(1-ratio);out.append(e)
 terr2.append(out)
terr2.extend([[F(0)]*5]*2)
errors2=[]
for j in range(5):
 pe=sum(r*abs_poly_bound(p,j) for r,p in zip(r25,polys2)); se=sum((abs(c)+r)*sum(comb(j,k)*rowbounds[k]*tr[j-k] for k in range(j+1)) for c,r,tr in zip(c25,r25,terr2))
 re=sum(abs(v)*((hi-lo)/2)**k for k,v in enumerate(deriv(rerr,j)))
 errors2.append(pe+se+re)
def gridiv(v,D=10**40):
 a=v.a*D;b=v.b*D
 return IV(F(a.numerator//a.denominator,D),F(-((-b.numerator)//b.denominator),D))
def jet2(t,j):
 return gridiv(evalp(deriv(rounded2,j),t-t02)+IV(-errors2[j],errors2[j]))
ti=IV(lo,hi)
for _ in range(4):
 mid0=(ti.a+ti.b)/2
 fv=jet2(IV(mid0),0); df=jet2(ti,1); assert df.b<0
 new=gridiv(mid0-fv/df)
 ti=IV(max(ti.a,new.a),min(ti.b,new.b))
 print("root width",float(ti.b-ti.a))
oldjets=jets
def jets(t): return [jet2(t,j) for j in range(5)]+[IV(0),IV(0)]
jr2=density_jet(ti,True)
jets=oldjets
assert jr2[1].b<0
r2,r3,r4=[jr2[i]/jr2[1]*factorial(i) for i in range(2,5)]
bi=ti*ti/36; vi=bi*(1-bi); Li=1-2*bi; Ai=-vi*r2/2
ci=(1-Ai)/bi-2
di=-(ci+2)*Ai+r2/2*(Ai*Li-(ci+3)*vi+Ai*Ai)+r3/6*vi*(2*Li+3*Ai)+r4/8*vi*vi
ri=1/bi-1
from math import lcm
C=400000
rv,cv,dv=[gridiv(a,10**30) for a in (ri,ci,di)]
mid=[(a.a+a.b)/2 for a in (rv,cv,dv)]
radius=[(a.b-a.a)/2 for a in (rv,cv,dv)]
assert [int(x*2*10**30) for x in mid]==[42880073440809287966549749811773,198282020875361309249001917399666,19381725319283097639924876692052]
def floor_sum(n,m,a,b):
 q,a=divmod(a,m); ans=q*n*(n-1)//2
 q,b=divmod(b,m); ans+=q*n
 while True:
  if a>=m:
   q,a=divmod(a,m); ans+=q*n*(n-1)//2
  if b>=m:
   q,b=divmod(b,m);ans+=q*n
  y=a*n+b
  if y<m:return ans
  n,b=divmod(y,m); m,a=a,m
def floorq(x):return x.numerator//x.denominator
def ceilq(x):return -floorq(-x)
def strip_count(l,h,slope,low,high):
 w=lcm(slope.denominator,low.denominator,high.denominator)
 u=int(slope*w); vl=int(low*w);vu=int(high*w)
 n=h-l+1
 return floor_sum(n,w,u,u*l+vu)+floor_sum(n,w,-u,-u*l-vl)+n
for M,expected in [(10**8,650590),(10**9,250988936)]:
 rho,c,d=mid
 A=C+ceilq(radius[0]*(2*M)**3+radius[1]*(2*M)**2+radius[2]*2*M)
 assert M>A and 9<d<10 and A==expected
 counts=[]
 for i in range(4):
  l=M+i*M//4; h=M+(i+1)*M//4-1
  slope=rho-d/(l*h); intercept=c+d*(l+h)/(l*h)
  low=intercept-d*(h-l)**2/(4*M**3)-F(A,M**2)
  high=intercept+F(A,M**2)
  assert high-low<1 and (h-l)*(high-low)<1
  counts.append(strip_count(l,h,slope,low,high))
 assert counts==[0,0,0,0]
 print(M,A,counts)
```

## Next

Use adaptive anchor precision to certify additional windows, paying actual coefficient errors rather than forcing all three coefficients to unnecessary fixed accuracy. The interval between these two windows is not yet covered; additional windows must be separately certified. No independent review or formal result promotion. Exact zero, uniform Diophantine separation, remaining spectral zeros, c2=0, and mother B_fix,odd(32) remain open.
