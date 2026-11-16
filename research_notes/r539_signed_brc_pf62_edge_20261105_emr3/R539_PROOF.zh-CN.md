# R539 | signed BRC Toeplitz order 62: exact all-positive-integer sign classification

Date: 2026-11-05. Frozen source: R462 @ `18783e01e3646c72b7aab3b16d3f565e83e6446f`. Predecessor: R538 @ `a72f6010e6f2e46026c0baea32bd8b81ac3bf146`. **Author-side exact computer-assisted CONDITIONAL theorem, not independently admitted.**

## Statement

For integer k≥1, let r=2k+1 and C_k=binom(2k,k)/(k+1)>0. Set, for 2≤t≤r,
H_k(t)=binom(r+t,2t)[x^r](1-x)(1+x)^(2t)(1+x²)^(r-t)
and H_k(t)=0 otherwise. Frozen R462 signed ballot–Catalan form:
B_k(t)=binom(r+t,2t) Σ_{q=0}^{min(floor((t-1)/2),k)} binom(t-1,2q)4^q C_(k-q)
for 2≤t≤r, and zero otherwise.

**Shared precise hypothesis:** for all positive integer k and relevant t, H_k(t)=B_k(t), with the R536 derived fixed-t polynomiality p_t(k)=H_k(t)/C_k ∈ Q[k], deg p_t≤2t. The H=B identity has been checked on an extensive finite grid but remains the frozen conditional premise.

Let D_m(k)=det(H_k(3+i-j))_(0≤i,j<m). Then for m=62 and every integer k≥1,

**D_62(k)>0 iff 1≤k≤6 or 12≤k≤73; D_62(k)<0 iff 7≤k≤11 or k≥74.**

Thus D_62 never vanishes on the positive integer domain. For odd r=2k+1, the infinite negative tail begins at r=149. Combining the R538 61st-order classification yields D_61(7)>0>D_62(7), D_61(k)<0<D_62(k) for 12≤k≤15, and D_61(k)>0>D_62(k) for every k≥74.

## Exact polynomial certificate and infinite tail proof

Define normalized f_n(k)=D_n(k)/C_k^n. The Toeplitz–Hessenberg determinant identity gives
f_0=1; f_n(k)=Σ_(a=1)^n (-1)^(a-1) p_(a+2)(k) p_2(k)^(a-1) f_(n-a)(k).
Induction with deg(p_t)≤2t gives deg(f_n)≤6n, hence deg f_62≤372.

Define G(k)=[k(k+1)(2k+1)(2k+3)]^62(k+2), with degree 249 and G(k)>0 for k≥1. Compute D_62(k)/(C_k^62 G(k)) exactly for k=1,...,124, take L>0 the least common multiple of their reduced denominators, and let δ_j (0≤j≤123) be the forward differences of the resulting integer values L D_62(k)/(C_k^62 G(k)) at k=1. Set S(k)=Σ_(j=0)^123 δ_j binom(k-1,j); deg S≤123. All exact δ_j and L are written in R539_EVIDENCE.json, and the regenerating program is R539_VERIFY.js.

The program verifies the exact identity
**L D_62(k)=C_k^62 G(k) S(k)** at all 373 distinct positive integers k=1,...,373. After division by C_k^62, both f_62(k) and G(k)S(k)/L are rational polynomials of degree at most 372. Therefore 373 exact evaluation equalities establish equality for all integer k≥1.

The exact certificate has S(k)>0 at k=1,...,6, S(k)<0 at k=7,...,11, S(k)>0 at k=12,...,73. Let ε_j=Δ^j S(74) for j=0,...,123. **Every one of the 124 exact ε_j is STRICTLY NEGATIVE**, checked and recorded in R539_EVIDENCE.json. For each u≥0 integer,
S(74+u)=Σ_(j=0)^123 ε_j binom(u,j)<0.
Since L,C_k,G(k)>0 for all positive integers k, the theorem follows.

## Reproduction and scoped verification

Run `node R539_VERIFY.js > R539_EVIDENCE.json`, then check the integer data, all 373 polynomial identity points, 20 raw 62×62 Bareiss determinants of matrices built from original H formula, 1240 direct H=B checks and 23499 full interpolation-grid H=B checks. All values use JavaScript arbitrary-precision BigInt.

A separate Python/SymPy Berkowitz check (R539_INDEPENDENT.py and R539_INDEPENDENT_EVIDENCE.json) verifies 4 original 62×62 determinants at k=6,7,11,12, 15 direct-H recurrence / integer-certificate points including k=73,74, 945 H=B coefficient pairs, and the 124 negative shifted forward differences. The cross-language code and tests were actually run.

All these are AUTHOR-SIDE exact verifications. Their infinite-tail conclusion uses the explicit H=B shared premise and R536 fixed-t consequence. Independent Driver review/CLAIM/Result not represented by these GitHub files. This auxiliary Toeplitz sign theorem does not assert a physical X6/BRC dynamical interpretation; P000 and the ACTIVE worldview remain unchanged.

## Open question

Next m=63; compare newly emerging sign windows with fixed-k generating-function poles. Separately, seek a direct proof of frozen H=B to discharge the common conditional hypothesis.
