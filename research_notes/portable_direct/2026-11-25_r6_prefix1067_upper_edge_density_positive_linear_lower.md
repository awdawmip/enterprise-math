# PREFIX-1067 — Upper-edge cubic observer density and a positive linear lower bound

2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_INTEGER_CONTRACTION_CHECKED / NOT_REVIEWED. Independent portable continuation of the prior EM-DIRECT-780BBE line. Current formal execution authority is not established; no CLAIM, task or Result mutation. Prior owner request r6-20261125-0050-owner-read read back SUCCEEDED with empty LEASED list at its dated snapshot; fresh r6-20261125-0150-owner-read pending when checked. Native recovery lookup of r6-20261125-0050-own-recovery returned CONTROL_REQUEST_NOT_FOUND; no new identity asserted.

Frozen science unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 candidate X6 chart anchor O, incoming -e1, reversal -5 (phase cover 5q), all other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization; exactly two negative steps. Parents:
- d91f254e8f1fc36e8f974fd5452a91144e46f570:research_notes/portable_direct/2026-11-24_r6_prefix1062_no_finite_shift_complete_monotonicity.md (exact BRC polynomial checker).
- e22d153b377149d9052d2395e9a4e288a74b8d8c:research_notes/portable_direct/2026-11-24_r6_prefix1065_cubic_observer_slope_bound.md.
- 96fbfae0c536e454e833e6eba2f903dace1fb27e:research_notes/portable_direct/2026-11-25_r6_prefix1066_monotone_envelope_slope.md.

## Theorems

For the inherited p_n and D(n,k)=(-1)^k forward_difference^k p_n, there exists c0>0 such that for all sufficiently large n, D(n,k)>0 for every integer 0<=k<=c0 n. In particular combined with PREFIX-1066,
 
    0 < liminf k_min(n)/n <= limsup k_min(n)/n <= 81/19.

For each fixed integer k>=0, with m=n-8,

    D(n,k) ~ A B(m+1,k+7/2), A>0.

A is specified below in terms of the common free pair edge-density normalization. This is an upper-edge result for the exact paired scalar observer; the full candidate BRC state is not quotiented. The actual slope limit and explicit numerical positive lower bound remain open.

## Exact algebra and order of cancellation

Use the exact parent's N_j(t,z), S=sum z_i, R=1-tS, L_i=S-6z_i. Expand N_j in R after t=(1-R)/S:
N_j=N_(j,0)+R N_(j,1)+R^2 N_(j,2)+... . In a neighborhood of the all-equal character, write ell for the degree of deviation from it, with O(ell^d) denoting vanishing to order d. The parent's polynomial H is twice the coefficient packet, H_j(n)=h_(j,0)+n h_(j,1)+n^2 h_(j,2), with
 h_(j,2)=S^5 N_(j,0);
 h_(j,1)=S^5(-3 N_(j,0)+2 N_(j,1));
 h_(j,0)=S^5(2 N_(j,0)-4 N_(j,1)+2 N_(j,2)).
These identities follow by substituting q=tS and applying n^2-(2d+3)n+(d+1)(d+2) to each q^d coefficient at q=1.

For N_(j,0), both A_i and C_(i,j) reduce to L_i/S, while R+B_(i,h) reduces to L_i L_h/S^2. Thus N_(j,0) is independent of j and O(ell^4). In N_(j,1), differentiating the middle R+B factor can leave two L factors, so N_(j,1)=O(ell^2). The j-dependent difference in N_(j,1) must differentiate C, leaving at least three L factors; the term 25 z_1 t^2 R v has j-independent coefficient of R, all other correction terms start at R^2 or higher. Hence N_(1,1)-N_(2,1)=O(ell^3). At z_i=1, A and C are multiples of R, R+B is divisible by R; the only contribution at R^2 in N is the common -390 z_1 t^3 R^2, giving N_(j,2)(1)=-390/216. Therefore h_(j,0)(1)=-28080, identical for both ports.

Let K_a=4J_a, the exact Laurent coefficients of H_1 H_1^* - H_2 H_2^* in n. The star reverses all displacements. Terminal z_j cancels with its paired star. K_a are inversion-even and every monomial displacement v has sum v_i=0. From h_2 common O(ell^4), h_1 common to order 2 with difference O(ell^3), h_0 common at degree 0 with difference O(ell), obtain:
 K_0=O(ell^2), K_1=O(ell^4), K_2=O(ell^6), K_3=O(ell^8), K_4=0.
For K_1 the possible degree-3 difference vanishes by inversion; K_2 starts at least degree 5 before inversion; K_3 starts at least degree 7. These are pointwise order statements, stronger than cancellation of one radial sum.

## Upper-edge density of the exact scalar pair contraction

Use the compact character group of the discrete translation algebra only as a proof representation of CT: the normalized Haar integral of z^v equals the discrete delta v=0. It is not an external physical model, state update, classical trigonometric calculation or reference experiment. All numerical coefficients below come from the parent's exact signed BRC polynomial contractions. Diagonal quotient is legitimate here because every monomial in K_a and Y=SS* has total displacement zero; no full Cell/port/branch information is discarded in the original packet. It is only the declared paired scalar observer, including all polynomial test functions and their derivatives.

Put x=Y/36. Its maximum 1 occurs only at the common character (triangle equality), one point in the quotient. Near this point take local additive coordinates theta in the five-dimensional real hyperplane sum theta_i=0. Such coordinates can be defined by the local additive group differential dz_i/(i z_i); they are auxiliary character coordinates, not native spatial axes. The leading homogeneous derivative of a character is obtained by repeated differentiation, yielding (i v dot theta)^r/r!. Inversion is theta -> -theta. By the quadratic product expansion and sum theta_i=0,
 
    s=1-x=||theta||^2/6 + O(||theta||^4).

No value of pi or classical trigonometric function is evaluated. The normalized Haar density is positive and constant in these additive coordinates. Write theta=r omega, with omega a unit vector in this five-dimensional hyperplane. The radial map s=r^2(1/6+O(r^2)) is analytically invertible in r^2 near zero, uniformly in omega. Thus CT[K_a h(x)] has, for x close to 1, a density w_a(x) analytic after factoring s^(a+5/2); this follows from r^4 dr and the even homogeneous expansion of K_a of degree at least 2(a+1). There are no other preimages near the maximum by compactness. Let C>0 denote the common leading unweighted density normalization, so CT[h(x)] has density C s^(3/2)(1+O(s)). Then, for r=a+1,

    w_a(1-s)=C b_a s^(a+5/2)+O(s^(a+7/2)),
    b_a=(-1)^r 3^r M_a / (r! * product_{j=0}^{r-1}(5+2j)),
    M_a=sum_v [z^v]K_a * (sum_i v_i^2)^r.

For clarity, the isotropic angular average of (v dot omega)^(2r) is (2r-1)!! ||v||^(2r)/(5*7*...*(5+2r-2)); this follows by the rotationally invariant moment tensor or integration of powers of one coordinate on the unit sphere, and is a rational identity. Since all lower degree terms vanish pointwise, higher-order corrections of the radial map and Haar density cannot change the displayed leading coefficient. Analytic remainders have the corresponding differentiated order through the required three derivatives. The grouped absolute displacement classes in PREFIX-1062 preserve these exact squared norms irrespective of the balanced sign partition, so computing M_a after the existing paired contraction is exact.

The paired observer is L(F)=(4*36^8)^(-1) sum_(a=0)^3 CT[K_a (E+8)^a F], E=x d/dx. On the upper-edge open interval, its density is
    g_eff(x)=(4*36^8)^(-1) sum_(a=0)^3 (7-x d/dx)^a w_a(x).
This is integration by parts, E*=-1-x d/dx, valid for smooth localized tests. At x=1 all boundary terms through derivative order 2 vanish because w_a vanishes to order a+5/2; cutoffs make the other boundary terms vanish. In s coordinates the adjoint is 7+(1-s)d/ds. The leading coefficient of g_eff is therefore
    A=C/(4*36^8) * sum_(a=0)^3 b_a (a+5/2)_(a),
where the subscript is the falling factorial. Cancellation of factors gives the simpler exact sum
    A=C/(4*36^8) * sum_(a=0)^3 (-1)^(a+1) 3^(a+1) M_a / ((a+1)! * 5 * 2^a).

## Executed exact coefficient calculation

Reused PREFIX-1062's JS code from its fixed parent above through the line "for(const [k,v] of J)if(v.every(x=>!x))J.delete(k)" (remove opening function check(){ if executing as a standalone script), retaining the exact numerator, H support and six-axis pair contraction. Here its map J stores K_a=4J_a. Appended:

```js
let sums=Array.from({length:5},(_,i)=>Array.from({length:5},(_,r)=>[...J].reduce((s,[k,v])=>s+v[i]*BigInt(vec(k).reduce((a,b)=>a+b*b,0))**BigInt(r),0n).toString()));
text({H:hs.map(h=>h.length),J:J.size,sums,hsum:hs.map(h=>[0,1,2].map(i=>h.reduce((s,[v,a])=>s+a[i],0n).toString()))})
```

Actual output: H=[2072,2072], J=121, hsum=[[-28080,0,0],[-28080,0,0]].
Rows of sums for a=0,...,4, columns r=0,...,4:
 0, -1128074895360, -11719652769792, -337791219646464, -16029027936239616
 0, 0, -4371838894080, 4353564672000, 5789307093516288
 0, 0, 0, -21332466892800, -1303097368117248
 0, 0, 0, 0, 0
 0, 0, 0, 0, 0

A separate exact BigInt computation of the four rational contributions gives 676844937216, -1967327502336, 4799805050880, 0. Their sum is 3509322485760 >0. Thus
    g_eff(1-s) = [C*3509322485760/(4*36^8)] s^(5/2) + O(s^(7/2)).
This establishes positivity on an open upper-edge interval. The third-order contribution vanishes at leading order even though K_3 need not be zero. This is a sign-sensitive cancellation, not a global absolute-value estimate.

## Uniform linear window

Choose 0<delta<1/2 sufficiently small that g_eff(x)>0 on (1-delta,1). Pick a smooth 0<=chi<=1 supported in that interval relative to [0,1], equal to 1 for x>=1-delta/2. For f=x^m(1-x)^k, L(f chi)=integral f chi g_eff>0. On I=[1-delta/4,1-delta/8], the density has a positive minimum and chi=1, so L(f chi)>=c1(1-delta/4)^m (delta/8)^k for a constant c1>0 independent of m,k. On the complementary term use the inherited cubic sup norm of L and the product rule. All derivatives (E+8)^i[f(1-chi)] (i<=3) vanish for x>1-delta/2, and are bounded by C2(1+m+k)^3(1-delta/2)^m, since the differentiated powers of (1-x) with nonzero falling factorials have nonnegative exponent and powers of x from Euler derivatives are nonnegative. Therefore choose any gamma>0 small enough that
    (1-delta/4)(delta/8)^gamma > 1-delta/2.
For every 0<=k<=gamma m the positive contribution dominates the complementary error exponentially, uniformly in k. For n sufficiently large, k<=gamma n/2 implies k<=gamma(n-8). This proves the positive linear lower bound (non-explicit c0=gamma/2).

For fixed k, integration against g_eff in the near-edge interval gives A B(m+1,k+7/2)(1+O(1/m)), by the leading density and the beta integral; the distant term is exponentially small. The exact fixed-k power is m^(-k-7/2) times a positive k-dependent constant. In particular every fixed order is eventually strictly positive despite permanent negative differences at moving orders.

## Scope and next question

The calculation uses the signed BRC-derived rational packets, all six Cell coordinates and both paired terminal ports before the observer contraction. The local compact-character construction and radial integration are proof identities for that already verified discrete CT algebra, not a new classical reference run or native physical attribution. No independent review or canonical native kernel rerun. The positive linear lower bound and fixed-k asymptotic are analytic proofs conditional on the inherited candidate packet; the coefficient sums alone are exact executed checks, not a numerical density computation. No explicit delta computed. Next: extend sign-sensitive density continuation from x=1 toward the first zero or singularity, certify explicit delta and lower slope, then determine whether the observed ~1.5 is an actual limit. Preserve the parent upper bound 81/19 and the permanent-obstruction theorem.
