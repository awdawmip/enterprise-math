# D25/LIFT — exact finite signed-boundary adjoint and telescope

2026-10-31. Author-side portable TASK_RESEARCH result; mathematical admission and native Source CLAIM/OPEN/checkpoint pending. Research logical conversation: chatgpt-research-hourly-enterprise-math-20260923. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3; P000 remains ACTIVE. This is external finite rational / p-adic auxiliary mathematics, not a native X6 result.

## Exact inherited inputs

The original weighted 216 target A_p = p (mod p^3) for p mod24 in {13,19} remains OPEN. Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Consume the other on-hour lane's original Clausen/Green signed-R derivation (20261031_onhour_d25_clausen_jet_unique_overdegree_R.md; 20261031_onhour_d25_first_jet_only_finite_green_signed_R_reduction.md), and this hourly lane's exact signed coefficient and finite holonomic inverse (20261031_hourly_d25_signed_R_holonomic_coefficient_bridge.md; 20261031_hourly_d25_finite_holonomic_green_inverse.md). Their prior proofs remain assigned to their actual authors.

Fix any integer ell >= 1, work over Q, and put

$$g_i={\ell\choose i}{2\ell\choose i}2^{-i}, \quad 0\le i\le\ell; \qquad c_1=1/10,\quad c_{a+1}/c_a=36a^2/((6a+5)(3a+2)).$$

The previously source-identified original signed boundary is

$$\mathscr R_\ell=2\sum_{i=1}^{\ell}g_i\sum_{a=1}^{i}(1+6(i-a))c_a,\quad R_p=\mathscr R_\ell\bmod p,\quad p=6\ell+1\ {\rm prime}.$$

The previously proved finite holonomic source is

$$f(z)=10\sum_{a=1}^\ell c_a z^{a-1},\quad
\mathcal L f=-20\ell^3c_\ell z^\ell,\quad
\mathcal L=\theta(\theta+5/6)(\theta+2/3)-2z(\theta+1)^3,\quad\theta=z\,d/dz.$$

## New theorem 1 — an explicit finite adjoint / WZ-type telescope

Define reverse Gauss tails S_j=sum_{i=j}^\ell g_i, T_j=sum_{i=j}^\ell i g_i, with tails zero after ell, and for k<ell let

$$w_k=\frac{6T_{k+1}-(6k+5)S_{k+1}}5
=\frac15\sum_{i=k+1}^{\ell}(1+6(i-k-1))g_i,\quad w_\ell=w_{\ell+1}=0.$$

Then for 0 <= k < ell the reverse discrete Green forcing is exact:

$$\boxed{w_k-2w_{k+1}+w_{k+2}=(g_{k+1}+5g_{k+2})/5},\quad g_{\ell+1}=0.$$

Put d_n=n(n+5/6)(n+2/3), d_0=0, lambda_0=0, and

$$\boxed{\lambda_{k+1}=(d_k\lambda_k-w_k)/(2(k+1)^3)},\quad 0\le k<\ell.$$

For every polynomial h=sum_{k=0}^{ell-1}h_k z^k, h_ell=0, with y=mathcal L h=sum_{n=1}^\ell y_nz^n, define B_n=d_n lambda_n h_n. The exact coefficientwise identity is

$$\boxed{\lambda_n y_n-w_{n-1}h_{n-1}=B_n-B_{n-1}},\quad 1\le n\le\ell.$$

Both endpoint terms B_0=B_ell=0. Thus

$$\boxed{\sum_{k=0}^{\ell-1}w_k h_k=\sum_{n=1}^{\ell}\lambda_n y_n}.$$

In the ACTUAL source family, swapping finite sums gives mathscr R_ell=sum w_k f_k and y_ell=-20 ell^3 c_ell with all other y_n=0, so

$$\boxed{\mathscr R_\ell=-20\ell^3c_\ell\lambda_\ell}.$$

Explicit expanded finite kernel:

$$\boxed{\lambda_\ell=-\sum_{k=0}^{\ell-1}\frac{w_k}{2(k+1)^3}
\prod_{j=k+1}^{\ell-1}\frac{d_j}{2(j+1)^3}}.$$

Proof: swapping the original signed double sum gives the displayed w_k. One reverse difference equals (g_{k+1}+6S_{k+2})/5, and a second yields the reverse forcing. Coefficient extraction gives y_n=d_n h_n-2n^3 h_{n-1}; the lambda recurrence gives w_{n-1}=d_{n-1}lambda_{n-1}-2n^3lambda_n. Subtraction is exactly B_n-B_{n-1}; the boundary vanishes. The actual source is terminal, proving the scalar identity. Unrolling lambda yields the product. These are rational identities for every ell, not guesses from modular samples. For p=6ell+1>=7 all denominator factors are p-units, so reduction into F_p is legitimate.

## New theorem 2 — exact observer quotient and p=13 vanishing witness

For arbitrary source perturbations delta y within the same finite operator and signed readout, the change is exactly

$$\boxed{\delta\mathscr R_\ell=\sum_{n=1}^\ell\lambda_n\delta y_n}.$$

Consequently dropping lower source coordinates is safe for this readout ONLY on a declared source family with corresponding lambda-orthogonality, such as the actual single-terminal-source family. This is a BRC typed observer condition, not a whole-state quotient.

For ell=2 one obtains exactly

$$g=(1,4,3/2),\quad w=(29/10,3/10),\quad
(\lambda_1,\lambda_2)=(-29/20,-1703/5760),$$

$$c_2=18/275,\quad y_2=-576/55,\quad
\mathscr R_2=1703/550,\quad1703=13\cdot131.$$

At target prime p=13 the actual signed observer R_13=0, but y_2 mod13=3 (a unit), lambda_2 mod13=0, lambda_1 mod13=7. Thus non-erasure of a terminal forcing does not forbid a scalar cancellation, and this R is sensitive to nonterminal perturbations. Neither R nor its adjoint is the distinct finite Green E_p.

## Composed remaining second-digit interface (conditional on inherited proven inputs)

For target p mod24 in {13,19}, the existing first-jet-only finite Green formula implies

$$(A_p-p)/p^2 \equiv (L_0N_0-1)/p+L_0N_1-12\cdot2^{-3\ell}E_p+20\ell^3c_\ell\lambda_\ell\pmod p.$$

This substitutes the ORIGINAL signed R with its finite adjoint source. It is a new source-preserving representation of the remaining obligation, NOT a proof that the right side vanishes for all target primes. In particular E_p and lambda_ell carry different source/provenance. At p=19,67,373 the independently checked signed triples (R, source, lambda_ell) are (12,11,8), (21,48,13), (196,259,31) modulo their primes; the inherited lower-jet rows are respectively (16,4,11), (41,20,27), (81,103,12). These satisfy the combined check but have no all-prime joint-cancellation proof.

## Executed evidence and exact frontier

The accompanying executable Python program checks the original rational double sum independently of the adjoint, Gauss-tail forcing, each coefficient telescope, arbitrary nonterminal input, the terminal identity, and the expanded kernel on small degrees. Rational Fraction ell=1..9 passes; all 330 primes p=6ell+1 in [7,5000] pass for original and independent mixed forcing. Anchor triples (p,R,source,lambda_ell): (7,3,5,2), (13,0,3,0), (19,12,11,8), (37,11,28,7), (67,21,48,13), (373,196,259,31). Marker PASS_D25_SIGNED_R_EXACT_FINITE_ADJOINT_TELESCOPE. Exact computation is verification of implementation, not a universal proof or a native p=373 benchmark.

Next precise step: derive a second source-aware adjoint for E_p's existing finite first-jet binomial transform and construct a JOINT finite telescoping certificate including its E_p readout, the integer carry, L_0N_1, and the distinct original signed terminal port. Preserve the p=19,67,373 nonzero cases. Other unfinished original-class p=373 H0/B0 divided-power and semilinear Frobenius work remains with enterprise-math#1559. Current gateway 0.6.11 read in this research run: research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED; exact continuation call returned CONTROL_QUOTA. Existing issue enterprise-math#1558 remains the control owner path. No session reset, CLAIM, OPEN, native checkpoint, Result or review is inferred from this author-side artifact.