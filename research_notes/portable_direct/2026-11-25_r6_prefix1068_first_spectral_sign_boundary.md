# PREFIX-1068 — First spectral sign boundary, existence of the migration limit, and strict upper bound 5/4

2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_INTEGER_SPECIALIZATION_CHECKED / NOT_REVIEWED.
Independent portable continuation of EM-DIRECT-780BBE / TASK_RESEARCH. The own historical session metadata is recovered (MCP-f6d93209fc8e4c5bb2c3b44f69a47174); no current formal CLAIM or execution authorization. Previous owner inventory r6-20261125-0150-owner-read SUCCEEDED, empty LEASED at its dated snapshot; fresh r6-20261125-0250-owner-read RUNNING at readback. No shared task or Result mutation.

Frozen input unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 candidate X6 chart anchor O, incoming -e1, reversal signed -5 (positive phase cover 5q), all other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full six-coordinate joint Cell pairing, ports, grade and phase retained by the source BRC packet. Parents:
- d91f254e8f1fc36e8f974fd5452a91144e46f570:research_notes/portable_direct/2026-11-24_r6_prefix1062_no_finite_shift_complete_monotonicity.md (exact signed BRC numerator and H).
- e22d153b377149d9052d2395e9a4e288a74b8d8c:research_notes/portable_direct/2026-11-24_r6_prefix1065_cubic_observer_slope_bound.md (K4 identically zero).
- 22ba7028ce3bdc225fd64f5d82a01d265401cecd:research_notes/portable_direct/2026-11-25_r6_prefix1067_upper_edge_density_positive_linear_lower.md (upper edge density, small positive linear window).

## Main result

For the inherited D(n,k)=(-1)^k forward_difference^k p_n and k_min(n)=min{k:D(n,k)<0}, the limit exists:
 
    lim_(n->infty) k_min(n)/n = 1/b - 1,   4/9 < b < 1,
    0 < lim_(n->infty) k_min(n)/n < 5/4.

Here b is the largest sign boundary of the exact effective scalar density in the upper regular interval (4/9,1), defined as sup{x in (4/9,1): g_eff(x)<0}. This gives a strict improvement of 81/19, proves convergence, and refutes the previously proposed asymptotic 3/2 for the frozen candidate. No numerical value of b is asserted. The finite computed ratios near 1.49 from PREFIX-1066 remain historical finite observations.

## 1. Exact observer and critical values

Use the previously justified CT character representation only for the declared paired scalar observer; it is not a new native spatial coordinate, physical evolution, or classical comparison. Set S=sum z_i, x=SS*/36, E=x d/dx. The parent's Laurent coefficients K_a=4J_a are those of H_1(n,z) H_1(n,z)* - H_2(n,z) H_2(n,z)*, with terminal monomials canceled only after full paired contraction. The star reverses displacements. K4=0. For m=n-8,

    D(n,k)=L(x^m(1-x)^k),
    L(f)=(4*36^8)^(-1) sum_(a=0)^3 CT[K_a (E+8)^a f(x)].

By the parent's discrete operator bound, L extends continuously to C^3([0,1]); its norm is bounded by a constant times the maximum of the first four ordinary derivative sup norms (or the corresponding Euler derivative norms). Work on the five-dimensional compact character quotient by the common diagonal character, justified by every Laurent monomial of K_a and Y having zero total displacement.

At any critical point with S nonzero, vanishing of the derivatives of SS* with respect to each independent phase means z_i S* is real for every i. Thus after a common rotation each z_i is +1 or -1. For r negative signs, x=(6-2r)^2/36. The nonzero critical values are exactly 1, 4/9, 1/9; points with S=0 have x=0. In particular (4/9,1) is regular. The level 4/9 has six critical points in the quotient, each given by exactly one negative sign (complements represent the same quotient points).

Let w_a be the pushforward of K_a times normalized Haar measure under x. On any regular open band, w_a has a real analytic density: on a compact neighborhood of a regular level, flow along the real analytic vector field grad(x)/||grad(x)||^2 for the flat invariant auxiliary character metric. Its analytic flow identifies nearby compact level sets, and the induced analytic density factor has a uniform local radius of analyticity on the compact reference level (finite chart cover). Integrating over that fixed level gives analyticity. This is a proof of properties of the exact CT observer. Integration by parts against smooth localized tests yields

    g_eff(x)=(4*36^8)^(-1) sum_(a=0)^3 (7-x d/dx)^a w_a(x).

By PREFIX-1067 g_eff is strictly positive sufficiently close to 1, and the formula extends to tests supported near 1 because the stated edge vanishing kills endpoint boundary terms.

## 2. Exact saddle values from the frozen signed BRC packet

For one negative sign, z_i=+/-1 and z_i*=z_i, so H_j(n,z) is a real polynomial in n with coefficients h_(j,0),h_(j,1),h_(j,2). The exact specialization map commutes with sums and products of the parent's Laurent polynomial algebra. In particular at these characters K_a are the coefficients of H_1^2-H_2^2. Do not replace the labeled z_i by absolute-displacement classes: the distinguished incoming axis and port make such a shortcut unsafe at an individual critical point.

Actual exact BigInt results (negative coordinate label, K3):
 1: -9830400000
 2:  3538944000
 3,4,5,6: 0 each
 sum: -6291456000.

All five coefficient sums over the six critical points:
 K0=3406147092480; K1=-1349265653760; K2=167824588800; K3=-6291456000; K4=0.
At all positive signs both H_j=[-28080,0,0], agreeing with PREFIX-1067.
At the 15 two-negative-sign representatives (x=1/9) the five sums are
 [232642117632,-132916445184,25341984768,-1610612736,0].
The second band is not needed in the theorem.

## 3. Sign-sensitive singularity at x0=4/9

Fix one negative coordinate at -1 and use local additive character coordinates theta_i on the five positive coordinates. Differentiation of characters gives S=4+i sum theta_i - (1/2) sum theta_i^2 + higher order terms. Therefore

    36(x-x0)=(sum theta_i)^2-4 sum theta_i^2+O(||theta||^3).

The Hessian has one positive and four negative directions (quadratic eigenvalues +1 and -4), so the real analytic Morse lemma yields local auxiliary coordinates (u,v) in R x R^4 such that x-x0=u^2-|v|^2. The normalized measure has a positive analytic Jacobian. The Jacobian at zero, and hence the common constant below, is the same at all six critical points by axis permutation symmetry of x and Haar measure, irrespective of the different K_a values.

For clarity the one-sided singularity can be derived directly, without any external model computation. Let s=x-x0. Localize by a smooth cutoff in u supported in |u|<epsilon, equal to 1 near zero, and a radial v cutoff equal to 1 for |v|<2epsilon and supported in the Morse chart. For small |s| the v cutoff is identically 1 on the radii reached for this u support. Integrate out |v| using r^2=u^2-s. The radial measure r^3 dr contributes a positive constant times (u^2-s). Averaging the analytic weight K_a times Jacobian over the v sphere and symmetrizing u produces an analytic function B_a(u^2,r^2), whose value at the origin is the positive common Jacobian times K_a at the critical point (the sphere area and radial factor may be absorbed into a common constant). The local density has the form

    const * integral_{u^2>=s} eta(u)(u^2-s) B_a(u^2,u^2-s) du.

For positive s this is the integral over the full fixed u support with analytic continuation of the B_a factor, minus the interval [-sqrt(s),sqrt(s)]. The former is analytic near s=0; the removed integral has leading factor

    integral_{-sqrt(s)}^{sqrt(s)} (u^2-s) du = -(4/3) s^(3/2).

After the substitution u=sqrt(s)t, its remainder is s^(5/2) times an analytic function of s. The rest of the level away from the six saddle neighborhoods is a regular smooth pushforward (smooth partition and local submersion), with bounded derivatives through order three. Summing the six saddle contributions, for s>0 sufficiently small,

    w_a(x0+s)=A_a(s)+C_* sum_crit K_a(z) s^(3/2) + s^(5/2) R_a(s),

with A_a smooth, R_a analytic near zero, C_*>0 common to all a and all saddles. The displayed remainder admits termwise derivatives through order three with the corresponding order. No value of an external trigonometric function or pi is evaluated; these are analytic identities used for the already defined exact BRC scalar pairing.

Only the a=3, third derivative term in the effective density contributes s^(-3/2). Since d^3/ds^3 s^(3/2)=-(3/8)s^(-3/2), its coefficient is

    g_eff(x0+s) =
       (4*36^8)^(-1) (3/8) x0^3 C_* (-6291456000) s^(-3/2)
       + O(s^(-1/2)).

All lower a and lower derivatives are O(s^(-1/2)) or bounded. The leading coefficient is strictly negative. Hence g_eff(x)<0 for x>x0 sufficiently close to x0. This is an ordinary density statement strictly inside the regular band; the distribution may be singular at x0 and no integrability or sign assertion across that critical value is needed.

Together with the positive upper edge this proves b in (4/9,1). On (b,1), g_eff is nonnegative, real analytic and not identically zero. It is strictly positive off isolated zeros. In particular every open subinterval of (b,1) has positive density somewhere.

## 4. Proof of the slope limit, including isolated zero issues

Write f_(m,k)=x^m(1-x)^k. For k/m -> rho>0 the normalized exponent has unique maximum at x_rho=1/(1+rho). More precisely the phase is phi_rho(x)=log x+rho log(1-x) with strict maximum there. On any fixed closed set away from x_rho the supremum is strictly smaller than its peak, with endpoints interpreted by the powers. The same exponential gap holds for the first three Euler derivatives: product rule yields a polynomial factor O((m+k+1)^3) times x^m(1-x)^(k-3) for k>=3. On compact ratio intervals away from zero, replacing k by k-3 preserves the strict gap for sufficiently large m; for a sequence with k/m tending to rho the same statement follows by strict concavity and uniformity away from endpoints. Multiplication by a fixed smooth cutoff adds only bounded coefficients. Thus any part of L outside a neighborhood of x_rho is exponentially smaller than a fixed interior test interval with phase above that outside maximum. This bound uses the inherited C^3/Euler norm, so it includes possible singular distributions at lower critical values.

Upper bound: if g_eff(x_rho)<0 in (4/9,1), choose a smooth cutoff chi supported within a negative regular neighborhood and equal to one on a smaller neighborhood of x_rho. For k=floor(rho m), L(f chi) is a negative integral and its magnitude has an exponential lower bound from a fixed subinterval near x_rho. L(f(1-chi)) is exponentially smaller by the gap above. Hence D(m+8,k)<0 for all sufficiently large m. Apply to negative points approaching b from below, so limsup k_min(n)/n <= 1/b-1.

Lower bound: choose any 0<rho0<1/b-1. Suppose there are infinitely many n with some k<=rho0 n and D(n,k)<0. Pass to a subsequence with k/(n-8)->rho in [0,rho0]. If rho=0, PREFIX-1067's uniform small positive linear window already contradicts this. If rho>0, x_rho>b. Use a nonnegative smooth cutoff supported in a small regular interval inside (b,1), equal to one on a neighborhood of x_rho. The localized integral is nonnegative, and even if g_eff vanishes at x_rho its isolated zeros allow a fixed subinterval arbitrarily close to x_rho with strictly positive minimum and phase strictly above the outside maximum. This positive contribution dominates the norm bound for the complement. Contradiction. Hence liminf k_min(n)/n >= 1/b-1. Combining both gives the asserted limit. The offset n=m+8 is asymptotically irrelevant. This argument is not a fit to the historical finite triangle.

## 5. Reproduction (actually executed exact specialization; no fresh path enumeration)

The following JS uses the frozen PREFIX-1062 numerator with each labeled z_i specialized to +/-1. Variable t is retained as a formal polynomial. The incoming, reversal and boundary factors are unchanged; at these values z_i^-1=z_i. H coefficients implement the exact same d-dependent formula as the parent's H routine. This is an algebra homomorphism of the actual typed BRC packet for the stated scalar pairing, not a new propagation implementation or arbitrary numerical model.

~~~js
const add=(...ps)=>{let q=[];for(let p of ps)for(let i=0;i<p.length;i++)q[i]=(q[i]||0n)+p[i];return q};
const sc=(p,c)=>p.map(a=>a*c);
const mul=(...ps)=>ps.reduce((a,b)=>{let q=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)q[i+j]+=a[i]*b[j];return q},[1n]);
function run(z){
 let S=z.reduce((a,b)=>a+b,0n),R=[1n,-S],t=[0n,1n],L=z.map(a=>S-6n*a),A=z.map((_,i)=>add(sc(R,i===0?-5n:1n),sc(t,L[i])));
 const C=(i,j)=>add(sc(R,i===j?-5n:1n),sc(t,L[i]));
 const B=(i,h)=>add(sc(mul(t,R),S-6n*(z[i]+z[h])+(i===h?36n*z[i]:0n)),sc(mul(t,t),L[i]*L[h]));
 let H=[0,1].map(j=>{
  let u=[0n],v=[0n];
  for(let i=0;i<6;i++){v=add(v,sc(mul(A[i],C(i,j)),z[i]));for(let h=0;h<6;h++)u=add(u,sc(mul(A[i],C(h,j),add(R,B(i,h))),z[i]*z[h]))}
  let N=add(mul([1n,-z[0]],u),sc(mul(t,t,R,v),25n*z[0]),sc(mul(t,t,R,R,C(0,j)),-10n),sc(mul(t,t,t,R,R),-390n*z[0]),j===0?sc(mul(t,t,R,R,R),-390n):[0n]);
  let h=[0n,0n,0n];
  for(let d=0;d<N.length;d++){if(N[d]===0n)continue;if(d>5)throw Error("degree");let w=N[d]*S**BigInt(5-d),b=BigInt(d);h[0]+=w*(b+1n)*(b+2n);h[1]-=w*(2n*b+3n);h[2]+=w}
  return h
 });
 return {H,K:add(mul(H[0],H[0]),sc(mul(H[1],H[1]),-1n))}
}
for(let r of [0,1,2]){
 let sum=Array(5).fill(0n),rows=[];
 for(let mask=0;mask<64;mask++){
  let z=Array.from({length:6},(_,i)=>(mask>>i)&1?-1n:1n);
  if(z.filter(x=>x===-1n).length!==r)continue;
  let {H,K}=run(z);sum=add(sum,K);
  rows.push({mask,H:H.map(h=>h.map(String)),K:K.map(String)})
 }
 console.log(JSON.stringify({r,sum:sum.map(String),rows}));
}
~~~

Actual execution output, one-negative representatives:
 mask 1 H1=[2419520,-592000,32000], H2=[1382720,-438400,32000], K=[3942162432000,-1652342784000,224624640000,-9830400000,0].
 mask 2 H1=[442048,-176000,19200], H2=[855232,-268160,19200], K=[-536015339520,303077130240,-56800051200,3538944000,0].
 masks 4,8,16,32: H1=H2=[442048,-176000,19200], K all zero.
 r=0,1,2 aggregate values are as recorded in section 2. Total specialized quotient representatives checked 22; all arithmetic BigInt. No evaluation of classical trig or pi, no new native canonical kernel execution, no independent review.

## 6. Next

The earlier numerical suggestion 3/2 is incompatible with this proof for the same frozen packet; investigate the long finite-scale delay from a singular distribution at 4/9. The next concrete scientific question is to bracket b strictly inside (4/9,1) using sign-sensitive analytic continuation or exact localized BRC observer tests, and obtain a quantitative onset estimate for the eventual slope. Preserve the existing permanent obstruction and fixed-k asymptotics. Mother problem remains open; no canonical theorem admission or native physical attribution.
