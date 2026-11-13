# R5 — An explicit rational statistical marginal pair requiring exactly 15 Blackwell edges

Date: 2026-11-10 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING**.

## Exact question and provenance

Does the enlarged seven-likelihood-ratio `nu_4=0` statistical face contain an **individual exact rational pair** for which no <=14-edge nonnegative martingale/Blackwell coupling exists? Yes. This is a new static statistical witness; the original **physically lawful `g=b` and matched stopping-times** 14-versus-15 question remains open.

Frozen scientific input pins (unchanged): GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Exact predecessor: PR #1894 / `b4d0594d3f9705dbe403b607741871ec9ff97842` (lawful seedless-F `mu_1>0` point, all-30-positive coupling); mathematical correction: PR #1896 / `1ad4649af24cbd5c3a4527ecdd226b721c49aac9` (martingale-compatible marginal affine dimension 10, not 14). Earlier PR #1894 generic-15 assertion for **all** marginals is refuted by PR #1896 and is **not** reinstated here.

These seven labels are likelihood-ratio branch labels and NOT the six native spatial axes in locked P000. The method is exact, positive rational P/Q-BRC branch-mass transport, preserving the full labelled coupling rather than collapsing it into total mass. It does not claim native Heartbeat dynamics, source-time evolution, or a physical calibration.

Define `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. A coupling `E_ij>=0` has row masses `mu_i=sum_j E_ij`, column masses `nu_j=sum_i E_ij`, and conditional-moment constraints `sum_i (r_i-r_j) E_ij=0`. Impose `nu_4=0`, so the allowed support is the 30-edge carrier
`D={(0,0),(6,6)} union {(i,j):i=0..6, j in {1,2,3,5}}`.
Write `A` for the 21x30 augmented matrix mapping `E` to `(mu,nu,(r_j nu_j)_j)`; `rank(A)=15` with an exact `-299/1600` minor (PR #1894).

## Theorem 1 — Exact individual rational 15-edge necessity witness

There is an **explicitly specified rational** normalized `(mu*,nu*)` with `nu*_4=0`, `mu*_j<nu*_j` for **each** `j=1,2,3,5`, and a 30-strictly-positive exact coupling `E*` to it, such that **every** nonnegative coupling to `(mu*,nu*)` uses at least **15** positive edges. A 15-edge coupling also exists by the rank-15 vertex argument. Thus its exact minimum support equals **15**.

### Finite exact construction

`VERIFY.py` is the defining deterministic rational algorithm for this explicit witness; no existence search is left unspecified.

1. Form the physically lawful `X,Y` of PR #1894 from the exact `X0,Y0,H,DY` tuples in the verifier and their exact mass map. The original 30-positive rational coupling `E0` is reconstructed by the published fixed 15x15 basis solve with background `tau=10^-7`. Check all 21 equations, `min(E0)=10^-7`, and the four strict deficits `mu_j<nu_j`.
2. Let `L` be the 5x30 matrix consisting of the four independent column-moment-defect rows `H_1,H_2,H_3,H_5` and total-mass row `1`. Extract its canonical left-to-right exact rational RREF nullspace basis. Greedily retain the first ten vectors `Z_1,...,Z_10` whose `AZ_k` images are linearly independent. The verifier checks `rank(L)=5` and `rank(AZ_1,...,AZ_10)=10`. These ten images span the normalized 10D marginal tangent space.
3. Let `ZMAX=max_{k,e}|(Z_k)_e|` and `alpha=min(E0)/(100(1+ZMAX))`. Set
   `E(t)=E0+alpha*sum_{k=1}^{10} t^k Z_k`.
   On `0<=t<=1`, positivity and all four strict deficits persist: the verifier checks `10 alpha ZMAX < min(E0)/2` and `600 alpha ZMAX < min_j(nu_j-mu_j)`. Every `E(t)` preserves martingale identities and total mass.
4. Select 15 independent augmented observation rows
   `I=(0,1,2,3,4,5,7,9,10,12,15,16,17,19,20)`.
   Multiply each moment row by 20 to form integral 15x30 matrix `C` with entries of modulus <=38 and `rank(C)=15`. Let `w_0=CE0` and `w_k=alpha*C Z_k`. Let `D0` be the positive least common multiple of their coordinate denominators, and `T=max_{k,i}|D0*w_(k,i)|`. All are deterministically computed exact integers. Set
   `M=15*14!*38^14*T`, `N=M+1`, `t*=1/N`, `E*=E(t*)`.
   The actual verifier yields
   `M=4724241976759335031810975442395896247757045760000000000`,
   hence **`N=4724241976759335031810975442395896247757045760000000001`**.
   These definitions are a finite explicit rational recipe for `mu*,nu*`.

### Proof that no 14-edge coupling exists (all supports at once)

For any coupling `F` to `(mu*,nu*)`, the four strict inequalities `mu*_j<nu*_j` imply that source columns `j=1,2,3,5` each contain a positive off-diagonal edge: an all-diagonal column would contribute `nu*_j` to target row `j`, contradicting `mu*_j<nu*_j`. Therefore on its support `S`, the four disjoint source-column defect rows are independent. The total-mass row is independent of these four rows because its evaluation on `F` is 1 whereas all four defects evaluate to 0. Consequently the normalized compatible marginal image of an arbitrary `k`-edge support `S` has dimension at most **`k-5`**.

Suppose `k<=14`. Extend a maximal independent subset of the `A`-columns in `S` to a 14-column linearly independent set `S'` within the full rank-15 carrier. The extension retains the four defect rows and the independent total-mass row, so the corresponding compatible tangent space has dimension <=9. However, `AZ_1,...,AZ_10` have **rank 10**. They cannot all belong to `span(A_(S'))`.

The 15x14 integer matrix `C_(S')` has rank 14. Choose a nonzero integral left annihilator `n` by its signed 14x14 cofactors. Each coordinate obeys
`|n_i| <=14!*38^14`.
The polynomial
`P(t)=n . [D0*C*E(t)]=sum_(k=0)^10 c_k t^k`
has **integer** coefficients, at least one nonzero coefficient (by the independent tangent-image argument), and each `|c_k|<=M`.

If `P(1/N)=0` and `d` is its highest nonzero degree, multiplication by `N^d` and reduction modulo `N` force `c_d ≡ 0 (mod N)`. Since `0<|c_d|<=M<N`, this is impossible. Therefore `C E(t*)` does not belong to the span of any <=14-edge support and **no** such coupling exists.

The feasible nonnegative fiber is a nonempty bounded polytope. Every vertex has <=rank(A)=15 strictly positive edges by linear independence of positive support columns. Combining both directions gives **exact minimum 15**. QED.

## Theorem 2 — Correct local genericity statement

Consider the relatively open subset of the normalized, martingale-compatible `nu_4=0` marginal face where all four strict deficits `mu_j<nu_j` hold and where a 30-strictly-positive coupling exists. It is **nonempty**, as certified by `E0`, and full-dimensional (dimension 10). For each support of <=14 edges, the compatible marginal image has dimension <=9 by the same rank-five argument. A finite union of these lower-dimensional charts has relative 10D Lebesgue measure zero. Rank(A)=15 supplies a <=15-edge vertex for every feasible marginal pair. Hence **almost every** pair in this particular nonempty open region has exact minimum support **15**.

This **conditional open-region** genericity coexists with PR #1896's full-dimensional 12-edge region elsewhere; it makes no global almost-everywhere 15 claim on the entire `nu_4=0` face.

## Reproduction, limits, next discriminating unit

Run `python VERIFY.py` with CPython standard library; `EXACT_OUTPUT.txt` records the actually executed Fraction checks for the deterministic witness, row ranks, positivity, deficits, integer-bound and number size. The cofactor/digit-separation argument establishes the all-support universal claim mathematically; no 145-million-support enumeration is needed. Executing assertions alone is not an independent mathematical review.

**Unresolved physically lawful question:** For the *unperturbed* matched-time `g=b` source / seedless-F target from PR #1894, either find a <=14-edge exact coupling or give a genuine all-support obstruction. The new rational statistical witness perturbs marginals in ten directions and is not claimed to preserve lawful physical strategy coordinates. Research next: compute the actual physical affine tangent image and test whether a digit-separated direction exists outside every 14-edge chart; use exact support/dual certificates before asserting a physical 15-edge necessity result.

No P000/worldview change, formal Result/Review or shared Owner/CLAIM alteration is part of this author-side report.