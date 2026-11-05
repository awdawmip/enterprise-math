# D25 — exact CM j-locus, inert second jet and canonical period obstruction
2026-11-05. TASK_RESEARCH. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; TP2-B6F4FC938FF94941C1B7; frozen science c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical conversation chatgpt-research-onhour-enterprise-math-20260923. AUTHOR-PROVED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.

## Frozen objective, models and mathematical question
For all primes p≡13,19(mod24), prove/refute original Delta_p-R_p≡0(mod p), source-aligned to original W_p−V_p≡0(mod p³). Original terms are a_k=(2k)!(3k)!/[216^k (k!)^5], b_k=(4k)!/[2304^k (k!)^4], W_p=Σ_(k=0)^(p−1)(6k+1)a_k and V_p=Σ_(k=0)^(p−1)(8k+1)b_k. Exact preceding rational-tail certificates suggest the *infinite* period candidates |8A∞²−9B∞²|<10^−145 and |2P∞−3Q∞|<10^−145, but do not prove equality. Here the new discriminating question is which exact parameter-level CM correspondence exists and whether it maps the canonical positive hypergeometric periods.

Define z0=1/2,t0=1/9,T=√2, u(z)=(1−√(1−z))/2, v(t)=(1−√(1−t))/2, u0=1/2−T/4, v0=1/2−T/3. The signature Gauss solutions F_A(z)=₂F₁(1/6,1/3;1;z) and F_B(t)=₂F₁(1/8,3/8;1;t) are quadratic pullbacks of the (1/3,2/3) and (1/4,3/4) signature solutions; their squares generate original 216/2304 unweighted ₃F₂ families by Clausen.

## Theorem A: exact same CM rational j and algebraic second jet
Let
J3(u)=27(1+8u)^3/[u(1−u)^3],
J4(v)=64(1+3v)^3/[v(1−v)^2].
Exact substitution in Q(T), T²=2, gives
**J3(u0)=J4(v0)=2417472−1707264T=:J0**,
**J0²−4834944J0+14670139392=0**, and (1+8u0)/(1+3v0)=2.
Keep both the chosen T-positive branch and its Galois conjugate as source labels; the polynomial alone loses the branch. These formulas match the inherited discriminant −24 CM polynomial, but equal j does not select elliptic period cycles or Frobenius.

On the *specific local algebraic graph* J3(u(z))=J4(v(t(z))), t(z0)=t0, implicit differentiation yields
dv/du|0=−2T/9; d²v/du²|0=(40+56T)/27.
As z=4u(1−u) and t=4v(1−v):
**t'(1/2)=−8T/27**,
**t''(1/2)=(104+16T)/81**,
so
**t(1/2+h)=1/9−(8T/27)h+((52+8T)/81)h²+O(h³).**
Exact J4'(v0)=172005120−121678848T has norm −2^16 3^10 17²·23; the u/v denominators and complementary factors are 2/3-units. Thus the local j-graph and its unique second jet lift by the implicit function theorem/Hensel to (Z/p^r)[T]/(T²−2) for every target prime p≡13,19(mod24), every r≥1. In terms of the previously explored Frobenius-odd candidate s=3T/4, **t'(1/2)/s=−32/81** exactly. Both the even 52/81 and odd 8T/81 second-order components must be retained until the declared observer readout.

## Theorem B: branch-specific obstruction to naive operator/positive-period transport
On this exact j-level t(z) branch, no nowhere-zero gauge M(z) can both (i) transform *every solution* f of the Gauss equation for F_B(t) into a solution M(z)f(t(z)) of the equation for F_A(z), and (ii) identify the canonical positive solutions via F_A(z)=M(z)F_B(t(z)) near z=1/2.

Proof: both Gauss equations have first-derivative coefficient P(x)=(1−3x/2)/(x(1−x)). The coefficient of f_t in the pulled-back differential operator forces
M'/M = [P(t)t'−t''/t'−P(z)]/2.
The exact second jet gives **(M'/M)(1/2)=−(1+T)/6<0**. But F_A,F_B and their first derivatives are strictly positive at z=1/2,t=1/9, since their defining power-series coefficients are positive for 0<x<1; t'(1/2)<0. Differentiating the putative ratio M=F_A/F_B(t(z)) therefore gives
M'/M=F_A'/F_A−(F_B'/F_B)t' >0.
Contradiction. This rejects the conjunction (i)+(ii) on the *specified branch*, not other cycles, twists, isogeny correspondences or p-dependent finite transformations. The exact algebraic CM j-matching remains useful; it cannot alone supply the scalar p-adic transport.

## Checker, evidence and provenance
The executable exact symbolic+quadratic-integer checker d25_exact_cm_j_locus_second_jet_check_20261105.py asserts the algebraic identities, J4' norm, first/second implicit jet, tangent ratio and forced gauge sign. It also independently computes in R3=(Z/p³)[T]/(T²−2), verifies J3 and J4 agree under second-order perturbations z0+p·h for h=1,2,3 for all **312** primes p<10000, p≡13,19(mod24); failures **0**. Representative (p,t'_T mod p, h² scalar mod p, h² T mod p) are (13,5,0,7), (19,18,18,13), (139,10,71,43), (373,276,148,281). Exact arithmetic only, no floating-point validity claim.

BRC observer retains original 216 vs 2304 source label, signed difference, T/conjugate, valuation and integer ring, even/odd first/second jet coordinates, and the original weighted operator and unequal half/full cutoff. Previous accepted CM0/SIMPLE/UR and earlier signed upper-shell and carry certificates are consumed, not re-proved. The mother W_p−V_p≡0(modp³) remains open; true original-class fixed-373 divided-power H0/B0 [X]U mod139129, rank, semilinear Frobenius direction, eta, kappa, odd Green/Hesse and independent replication remain NOT_EXECUTED / PENDING_OWNER in Issue #1559.

Own Source continuation request onhour11-20261105-1900-d25-read-source SUCCEEDED (Source 445807d13e58615fed7931d7423282b067ff9ab1; observed 2026-11-05T11:02:29Z) but execution_authorized=false. No own claim/run/source checkpoint/Result is inferred from this author-side GitHub record.

**Next exact action:** Find or exclude a specific period-cycle-compatible branch, twist or isogeny transport for the canonical positive pair; on viable branch derive a *p-parametric terminating* original 216→2304 transformation, retaining the signed p² half-endpoint carry and both different upper-shell cutoffs, test p=13 and p=19, then seek uniform proof. Native p373 H0/B0 must be independently executed through the existing support route #1559; ordinary parameter algebra does not satisfy that benchmark.
