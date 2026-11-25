# PREFIX-1090 — Matching the radial zero-edge order removes the asymptotic outer-envelope obstruction

2026-11-26 (Asia/Shanghai). AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_COMPUTATION / NOT_REVIEWED. Independent R6 continuation. Original own registration r6-20261123-2358-session-start-own-v1 recovered SUCCEEDED, EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322; current owner request r6-20261126-0050-owner-read SUCCEEDED, LEASED empty at 2026-11-25T16:51:38.865014Z, source 4472cd8be587a1532fa8fb80a7d134cf9b7d2708. No new CLAIM or shared task mutation.

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Same Stage46 X6 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both directions of Link {O,e1} blocked without renormalization, exactly two negative steps. Retain complete signed phase-paired Cell/port/ordered multiplicity carrier. Auxiliary radial weight changes only the certificate, not D or native dynamics. Native-to-CT correspondence inherited, not independently reverified.

Parents:
- 4c7f400d0557b5ec344b7297b5354f49bfa1fc81:research_notes/portable_direct/2026-11-25_r6_prefix1089_signed_block_floor_certificate.md
- 508dd49782d0203dbcf0e7891fa01484da5be5ef:research_notes/portable_direct/2026-11-25_r6_prefix1085_quadratic_orbit_tail_certificate.md
- 2f3bf251ebcd76aa5cbcae50f47c9fe3a861d010:research_notes/portable_direct/2026-11-25_r6_prefix1087_divergence_completeness_and_envelope_floor.md
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md
- cc1fa4471149037fc07977d0cc27e532e75a5f61:research_notes/portable_direct/2026-11-25_r6_prefix1073_zero_edge_sharp_positive_tail.md
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md

## 1. A different positive reference measure

Use fixed m>=0,r>=1,k>=3, M=m+r, U>=7, Q=k+u, c_u=binom(u+r-1,r-1), x=SB/36, y=1-x, w_Q=x^(M+2)y^(Q-3), c=1/(8*36^6), D_m(k)>0. Let f_u=c_u D_M(Q)/D_m(k), A_true(U)=sum_(u>=U)|f_u|, S(U)=sum f_u. Define for j=0,1

 b_u^(j)=c_u CT[x^j w_Q], B_j(U)=sum_(u>=U)b_u^(j),
 F_j(U)^2=B_j(U) sum_(u>=U) f_u^2/b_u^(j).

F_j denotes the ideal bin-mean envelope, not an executed optimized Gram certificate. Parent 1089 gives its lower block certificates. The original j=0 uses one power of x too few relative to the signed density at zero. Choose j=1 instead. In the original Newton expansion D_M(Q)=c CT[w_Q F_Q], use new measure x w_Q and carrier F_Q/x on x>0 (define arbitrarily on its measure-zero zero set). All bin signed values and multiplicities remain exactly unchanged. More generally replace F by its orbit average or any previously certified null-controlled G before dividing by x. Every such reweighting must keep the original unweighted carrier available.

## 2. New asymptotic theorem: old relative floor is nonzero, shifted floor is asymptotically exact

For fixed m,r,k above and any 0<alpha<1, conditional on PREFIX-1073/1075 density and derivative results, set eta=alpha/2. Then

 F_0(U)/A_true(U) -> (m+4)/sqrt((m+3)(m+5)) > 1,
 F_1(U)/A_true(U) = 1+O_(m,r,k,alpha)(U^(-alpha)).

Proof. Unweighted radial density h(x)=h(0)+O(x^eta), h(0)>0 (1075 section 2 and constant radial Jacobian). Effective signed density on the lower regular band is g(x)=h(0)gamma0*x^3+O(x^(3+eta)), gamma0=F_pol(4)/(4*36^5)>0 with F_pol(4)=4283136/5. Choose a fixed smooth cutoff inside that band; the complement in the signed observer is exponentially small for fixed M by its C^3 norm (1075 section 4), and the radial complement likewise. For any fixed a>=0, integration against x^a y^Q gives the leading factor Gamma(a+1) Q^(-a-1) with relative error O(Q^-eta), by the beta integral and the bound on the density error. Replacing Q by Q-3 in radial moments has relative error O(1/Q). Therefore, writing b_j=b_u^(j),

 b_j = beta_j u^(-m-4-j)(1+O(u^-eta)),
 f_u = phi u^(-m-5)(1+O(u^-eta)),
 beta_j=h(0)Gamma(M+3+j)/(r-1)!,
 phi=h(0)gamma0 Gamma(M+4)/((r-1)! D_m(k)).

The last formula uses Q=k+u and the fixed-r binomial multiplicity. Eventual positivity follows here from phi>0. For j=0, power-tail summation gives
 B_0~beta_0 U^(-m-3)/(m+3),
 sum f_u^2/b_0~(phi^2/beta_0) U^(-m-5)/(m+5),
 A_true~phi U^(-m-4)/(m+4).
Their ratio yields the claimed constant. In particular even perfect internal cancellation cannot remove this relative gap in the original fixed measure.

For j=1, mu_u=f_u/b_1=gamma0/D_m(k)+O(u^-eta), with a strictly positive limit. On u>=U sufficiently large this error is uniformly O(U^-eta); hence under probability weights b_1/B_1 the variance of |mu| is O(U^-2eta), while its mean tends to the positive limit. The exact floor identity F_1^2/A_true^2=1+Var(|mu|)/(E|mu|)^2 (1087) proves the stated rate. The constants are not yet explicit. This is a statement about the mathematical ideal envelope for the specified fixed inputs, not a uniform large-m bound or a guarantee about finite low-order Gram performance.

## 3. Complementary finite upper certificate for either ideal floor

For V>U define C_j(V)=sum_(u>=V)c_u CT[x^(-j) w_Q F_Q^2]. For j=0 this is 1085; for j=1 the integrand is a polynomial after combining powers of x (w exponent M+1). The previous finite L formula applies with its argument i reduced by j, so i-h>=2-j>=1 in every summand. All exponents remain nonnegative. In particular this is exact rational calculation; no singular Laurent evaluation is required. Orbit average may replace F, or use a certified null-controlled G with integrable shifted square. The parent P_d=O(x) estimate gives C_j(V)=O(V^(-m-5+j)) by termwise bounds as in 1085.

By Cauchy-Schwarz at each bin in the shifted positive measure,
 sum_(u>=V) f_u^2/b_j <= (c/D_m(k))^2 C_j(V).
The complementary bracket is thus

 B_j(U)[sum_(U<=u<V) f_u^2/b_j + S(V)^2/B_j(V)]
 <= F_j(U)^2 <=
 B_j(U)[sum_(U<=u<V) f_u^2/b_j +(c/D_m(k))^2 C_j(V)].

Both endpoints are rational and converge to F_j(U)^2 at fixed U, with absolute width O(V^(-m-5+j)). The left endpoint uses the exact signed tail, the right uses the new finite shifted second moment. This is a genuine upper certificate of the ideal floor, distinct from an executed finite-control upper bound for A_true. For actual negative-tail bound, use c sqrt(B_j C_j)/D and (A-S)/2, or the appropriate blockwise sum. A numerical shifted C_j run is still outstanding; no numeric upper for F_j is asserted here.

## 4. Executed exact finite lower-floor comparison

Fixed (m,r,k)=(0,1,115), V=400. Reused exact 66-term BRC paired CT reduction, eight displacement classes and integer difference recurrence from 1082. No classical reference or native re-enumeration. B_j(t)=CT[x^(2+j)y^(112+t)], b_j(u)=CT[x^(3+j)y^(112+u)], S(t)=D_0(115+t)/D_0(115), f=D_1(115+u)/D_0(115). First eight A values match parent. All 393 signed differences and 786 positive radial differences (two weights) were checked exactly. Four cutoff pairs completed exact rational lower-floor calculations; decimals below rounded. The run was terminated by tool timeout after U=200 outputs; U=300 and final digest did not complete and are not claimed. The parent original-weight numbers agree in the displayed precision.

U | S(U) | L0 | L1 | (L0-S)/2 | (L1-S)/2
7 | 1.07326231356434854 | 1.19100077716796300 | 1.32049972413492749 | 0.05886923180180723 | 0.123618705285289475
20 | 0.991984088376968450 | 1.01413200833023813 | 1.07586425815856266 | 0.011073959976634840 | 0.041940084890797105
120 | 0.204628340692588379 | 0.207704998061857445 | 0.205620754949585763 | 0.001538328684634533 | 0.000496207128498692
200 | 0.0727977900795234721 | 0.0740887204741242851 | 0.0729504388439801642 | 0.0006454651973004065 | 0.00007632438222834605

At U=120 and 200 the lower-floor diagnostic for the shifted weight is respectively about 3.1x and 8.5x smaller in negative-envelope units; at U=7 and 20 it is larger. These compare lower bounds, not proved reductions of actual optimal floors or achievable negative-mass upper bounds. Finite lower values may be smaller simply because the gap to the true ideal floor is different. The asymptotic theorem is the rigorous improvement; these finite examples guide testing.

## 5. Reproduction suffix

Run PREFIX-1082 section 4 through A and tables, with Nmax=520,Jmax=Nmax+12, zero shift included; then use the parent 1089 rows/D/b/s/f definitions with rows retaining first six columns (rather than four). Run:
```python
from fractions import Fraction as Fr
from decimal import Decimal,localcontext
def bt(u,j):return b(2+j,k+u-3)
def mass(u,j):return b(3+j,k+u-3)
V=400
for u in range(7,V):
    assert s(u)-s(u+1)==f(u)
    for j in (0,1):assert bt(u,j)-bt(u+1,j)==mass(u,j)>0
for U in (7,20,120,200):
    vals=[f(u) for u in range(U,V)]
    abs_lower=sum(map(abs,vals),Fr(0))+abs(s(V))
    for j in (0,1):
        floor2=bt(U,j)*(sum(f(u)**2/mass(u,j) for u in range(U,V))
                           +s(V)**2/bt(V,j))
        assert floor2>=abs_lower**2
        with localcontext() as ctx:
            ctx.prec=18
            dec=lambda x:Decimal(x.numerator)/Decimal(x.denominator)
            L=dec(floor2).sqrt()
            print(U,j,dec(s(U)),L,(L-dec(s(U)))/2,flush=True)
```
No independent review, formal checker, new native correspondence or speed improvement claimed.

## 6. Next

Compute the exact shifted C_1(V) and compare the two-sided brackets, then a switched outer scheme that uses the unshifted weight in the pre-asymptotic blocks and shifted measure in the final tail. Use the parent exact signed-block data, and test a small number of cutpoints before adding more Gram modes. Explicit uniform positivity constant, p and d, and mother objective B_fix,odd(32) remain open.
