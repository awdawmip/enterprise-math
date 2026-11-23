# PREFIX-1033 — Global continuous signed density and exact Bernstein detection for the X6 port contrast

Date: 2026-11-23 (Asia/Shanghai)
Status: AUTHOR_ANALYTIC_PROOF / EXACT_SMALL_INTEGER_CROSSCHECK / NOT_REVIEWED
Parent: PREFIX-1032; scientific input is FROZEN P000 V5 at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json.

## Object and frozen scope

Continue the Stage46 candidate signed BRC W=J12-6I12, native Heartbeat World X6, incoming -e1, forbidden bidirectional Link {0,e1}, exactly one outgoing negative step, and the original coherent joint Cell–terminal-port–grade square-mass observer. The auxiliary six-phase Haar/Laurent integral is an exact scalar-observer calculation inherited from PREFIX-1026. It is not an information-lossless replacement for the native BRC state, nor a new native physical computation.

Let mu be the Haar pushforward of Y=|z1+...+z6|², supported on [0,36], and let rho be its density. The inherited distributional functional nu is

5 nu[f] = -4 int H(y) f'(y) mu(dy) -2 int P(y) f(y) mu(dy)
          +12 int (6-t) [int_0^t (11+y) f(y) dy] mu(dt),

H(y)=y²(36-y)², P(y)=y(y-36)(17y-91).

Its integer moments are a_m=nu[y^m]=Q⁺_(m+4,1)-Q⁺_(m+4,2) for m>=1, with the algebraic extension a_0=2412. Define F(y)=int_[y,36](6-t)mu(dt).

The prior PREFIX-1031 proved the only positive critical levels of Y on the 5-phase quotient are 4,16,36, with all 21 points at 4 and 16 nondegenerate; PREFIX-1032 established rho(0)>0, rho(y)=rho(0)+O(sqrt(y)), rho'(y)=O(y^(-1/2)) near 0. At the unique upper maximum, PREFIX-1031 proved rho(36-u)=c u^(3/2)+O(u^(5/2)), with differentiable asymptotic and c>0.

## Theorem A — no hidden delta masses at the Morse levels

Under these exact inherited frozen-observer formulas and verified mathematical premises:

1. rho belongs to C¹((0,36)), including at the interior Morse critical levels 4 and 16, and extends continuously to both endpoints.
2. H rho belongs to C¹([0,36]) and H rho=(H rho)'=0 at y=0 and y=36.
3. nu is integration against one finite signed absolutely continuous measure with a continuous density g on all [0,36]:

   g(y) = [4(H(y)rho(y))' - 2P(y)rho(y) +12(11+y)F(y)]/5,

   g(0)=g(36)=0, int_0^36 g(y)dy=2412, and int_0^36 y^m g(y)dy=a_m for all m>=0.

In particular no atom, derivative-of-delta, or jump-boundary term at 0,4,16,36 is allowed by this representation. This does not assert g>=0.

### Proof

On a compact regular interval avoiding 0,4,16,36, the coarea/submersion theorem already gives a smooth pushforward density.

Fix one of the interior critical values v in {4,16}, and choose a smooth cutoff chi(y) supported in a small interval around v containing no other critical value and equal to 1 near v. The Fourier transform of chi rho is, up to an inessential Fourier sign convention,

I(t) = (2pi)^(-5) int_(T^5) chi(Y(theta)) exp(it Y(theta)) dtheta.

There are finitely many stationary points on this support, all with nondegenerate 5-by-5 Hessians (15 at v=4 and 6 at v=16). A smooth partition of unity and the five-dimensional nondegenerate stationary-phase estimate give O(|t|^(-5/2)) from each critical neighborhood; repeated integration by parts gives O(|t|^(-M)) for any M on the complementary nonstationary support. Hence I(t)=O(|t|^(-5/2)). As int_R (1+|t|)|I(t)|dt is finite, Fourier inversion yields chi rho in C¹. This applies at both critical levels and proves the first assertion on the open band.

At y down to zero, H(y)=1296y²+O(y³), rho(y)=rho(0)+O(sqrt(y)), and rho'(y)=O(y^(-1/2)); thus H rho->0 and (H rho)'=2592rho(0)y+O(y^(3/2))->0. At y=36-u down from above, H(36-u)=1296u²+O(u³) and rho=c u^(3/2)+O(u^(5/2)) with the differentiable expansion, so H rho=O(u^(7/2)) and (H rho)'=O(u^(5/2)), both tending to zero. The density rho is continuous at the endpoints by those expansions. Therefore H rho is C¹ on the closed interval.

F is continuous because mu is absolutely continuous; it satisfies F(36)=0 and F(0)=6-int t mu(dt)=6-A6(1)=0. Since P(0)=P(36)=0, the stated g is continuous and has g(0)=g(36)=0.

For C¹ test f, integration by parts (the H rho boundary terms vanish) gives -4 int H rho f'=4 int (H rho)' f. Fubini, justified by bounded y and finite mu, converts the nested term to 12 int (11+y) F(y) f(y)dy. This proves 5nu[f]=5int f g. Polynomial tests recover all a_m; for m=0 the already proved algebraic extension is 2412. The representation is a signed finite measure since g is continuous on a compact interval. QED.

## Theorem B — exact beta smoothing and a complete counterexample criterion

For integers m,k>=0, put N=m+k and E_(m,k)=nu[y^m(36-y)^k]. Define

D_(m,k)=(N+1) binom(N,m) E_(m,k)/36^(N+1).

Then exactly

D_(m,k) = E[g(36T)]  where T has Beta(m+1,k+1) law.

Consequently for every continuous g above,

lim_(N->infty) max_(0<=m<=N) |D_(m,N-m)-g(36m/N)| =0.

A quantitative version (N>=1) uses M=max_[0,36]|g| and the modulus omega_g(delta)=sup_{|x-y|<=delta}|g(x)-g(y)|:

|D_(m,N-m)-g(36m/N)|
<= omega_g(delta) + 2M min{1, [1296/delta²] [1/(4(N+3))+1/(N+2)²]}

for each delta>0, uniformly in m=0,...,N.

### Proof

The beta probability density of 36T is exactly (N+1)binom(N,m)y^m(36-y)^k/36^(N+1). Inserting Theorem A's g into E yields the identity. With s=m/N, E[T]=(m+1)/(N+2), |E[T]-s|<=1/(N+2), and Var(T)=(m+1)(k+1)/((N+2)^2(N+3))<=1/(4(N+3)). Chebyshev and the modulus of continuity give the displayed bound. Choose delta->0 slower than N^(-1/2) to obtain uniform convergence.

The following statements are now equivalent for this precise frozen observer:

(A) E_(m,k)>=0 for every integer m,k>=0;
(B) g(y)>=0 for every y in [0,36].

(B) trivially implies (A). Conversely, for each 0<y<36, select m_N=floor(Ny/36), k_N=N-m_N. If g(y)<0, the uniform beta convergence produces D_(m_N,k_N)<0 and therefore a finite exact E_(m_N,k_N)<0 for all sufficiently large N. At the endpoints g=0. Thus (A) implies (B).

Moreover, PREFIX-1031/1032 give g>0 on nonempty lower and upper spectral-edge intervals. Hence (B) actually implies strict E_(m,k)>0 for every finite pair and strict positive definiteness of every shifted contrast Hankel matrix:

sum_(a,b=0)^(h-1) c_a c_b a_(n0+a+b)
= int_0^36 y^n0 (sum_a c_a y^a)^2 g(y)dy >0

for any h>=1, n0>=0, and nonzero real vector c. The positive edge interval makes the polynomial integral strictly positive. If (B) fails at any interior y, the beta criterion supplies a falsifying finite E with m/N approximately y/36. QED.

## Exact crosschecks and evidence scope

The deterministic local integer/finite-rational crosscheck used the PREFIX-1016 three-shift formula, multinomial collision moments A6(r), and symbolic expansion of H and P:

H=1296y²-72y³+y⁴; P=3276y-703y²+17y³.
a_0..a_7=[2412,25620,386028,7124592,149251656,3398043852,81969197100,2063490736128].
At N=1, E_(0,1)=61212 and E_(1,0)=25620; at N=2 the values for m=0,1,2 are [1667340,536292,386028].
The lower-end coefficient checks 4*2592 -2*3276 -792=3024; at the upper end -18144+37512-6768=12600, giving inherited g(36-u)~2520c u^(5/2).

These calculations were executed using Python integers, fractions.Fraction and SymPy for polynomial expansions on 2026-11-23. Theorem A's Fourier/stationary-phase implication is an analytic hand proof, not numerically certified and NOT_REVIEWED. No new native BRC propagation or physical interpretation is claimed. The old up-to-N=5000 exact Hausdorff triangle is inherited as published PREFIX-1030 evidence; it has not been recomputed here.

## Consequence, unresolved item, and next unit

The positive-measure problem has been reduced to the pointwise sign of a single continuous, fully explicit g, including the two saddle values. There are no additional singular measure terms to analyze. The remaining decisive task is to certify g>=0 or locate a negative g(y) on one of (0,4), (4,16), (16,36). Rigorous interval bounds for rho,rho',F (with the proved C¹ regularity at 4,16) are one route; a negative sign at a rationally isolated interval would guide a finite exact Bernstein witness via Theorem B. Continue to preserve the full BRC Cell–port–grade observer and all frozen provenance. Mother B_fix,odd(32) in {19,20} remains unresolved.

Historical contributor provenance: EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056 / SID MCP-45ad6d29cd534c1aad25595a72e3c532, as source attribution only. This paper does not claim current ownership, CLAIM, PROGRESS, Result, independent review or Activity association.
