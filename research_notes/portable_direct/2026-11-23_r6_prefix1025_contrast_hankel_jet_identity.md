# PREFIX-1025 — Positive-port contrast: eventual strict Hankel positivity and exact signed jet identity

Date: 2026-11-23 Asia/Shanghai. Status: AUTHOR_EXACT_PROOF_WITH_INHERITED_ASYMPTOTIC_INPUT / EXACT_INTEGER_CHECKED / NOT_REVIEWED.
Scientific parent: PREFIX-1024, PREFIX-1023, PREFIX-1017, PREFIX-1014. This is a new contrast-observer statement and a new all-order algebraic identity, not a replacement or review of any parent.

## Frozen scientific scope

P000 V5 pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`. Stage46 candidate signed 12-direction BRC kernel `W=J_12-6I_12`; chosen X6 Cell anchor; incoming `-e1`; bidirectionally blocked Link `{0,e1}`; exactly one negative outgoing direction (grade k=1). The observed integer masses are coherent squares after **signed amplitudes are combined within the same Cell–terminal-port–grade fibre**. Normalized probability denominator is `36^n`. No primitive axis, origin, branch or observer is silently erased.

Let `R=Z[z_1^{±1},...,z_6^{±1}]`, `S=sum_i z_i`, `S*=sum_i z_i^-1`, `L=SS*`; `CT` denotes the Laurent constant term. Let `m=n-4>=1`, and `Q_{m+4,j}^+=CT[S^m B_{m,j}(S^m B_{m,j})*]`, with
```text
T = S-z1
E_j = 72-6 S (z1^-1+z_j^-1)
P_j = z_j T (L-36)
R_j = z_j [ T (3(L-36)+E_j) + z1 (L-36) +25 z1 ]
B_{m,j} = m P_j + R_j.
```
These are exactly the fixed PREFIX-1014/1023 packets rearranged, with `R_j` a Laurent polynomial and no approximation. On the 5-relative-phase torus, `L=|S|^2` and `Q=∫ L^m |mP_j+R_j|^2 dμ`, where `dμ` is normalized Haar measure. This torus integral is an exact Fourier/Parseval observer of native BRC Laurent coefficients, not a new native transition rule.

## Theorem A — exact finite-order jet/Gram identity (new)

For any integer `m>=1`, any fixed positive port `j=1,...,6`, any `h>=1`, and all **real** `c_0,...,c_{h-1}`, put `p(x)=Σ_{i=0}^{h-1}c_i x^i` and `D=x d/dx`. Then, exactly,
```text
Σ_{i,k=0}^{h-1} c_i c_k Q^+_{m+4+i+k,j}
 = ∫ L^m {
      | [(mP_j+R_j) p(L) + 2 P_j (Dp)(L)] |^2
      + 2 |P_j|^2 [p(L)(D²p)(L) - ((Dp)(L))²]
   } dμ.
```
The first term is nonnegative; the second is a **signed jet-curvature residual** and may be negative for a real-coefficient `p`. Thus a positive square-mass sequence need not have a positive-semidefinite Hankel matrix. For the linear test `p=a+bx`, the residual is exactly `2ab L|P_j|²`, exhibiting the role of coefficient sign. The retained joint Laurent representation preserves the signed interference before any square-mass observation.

**Proof.** For `x=L`, `A=mP_j+R_j` and `p=Σ c_i x^i`, use
`Σ_{i,k}c_i c_k x^{i+k}=p²`,
`Σ_{i,k}(i+k)c_i c_k x^{i+k}=2pDp`,
`Σ_{i,k}(i+k)^2 c_i c_k x^{i+k}=2pD²p+2(Dp)^2`.
Expand `|(m+i+k)P_j+R_j|²`, substitute these three identities and complete the square. No limiting argument is used. □

This identity is a fixed-future-horizon quadratic **observer representation**; it does not certify that a scalar Hankel readout replaces the full Cell–port–grade state under arbitrary future native BRC updates.

## Theorem B — eventual strict Hankel positivity of the positive-port contrast (new observer)

Set `Δ^+_{m+4}=Q^+_{m+4,1}-Q^+_{m+4,2}`; symmetry makes `j=2,...,6` interchangeable. For any **fixed integer h>=1**, there exists `N_h` such that
```text
[ Δ^+_{n0+a+b} ]_(0<=a,b<h) ≻ 0   for all integer n0>=N_h.
```
Moreover, with `m=n0-4`, `α=7/2`, `CΔ=1530900 / π^(5/2)`, one has
```text
det[Δ^+_{n0+a+b}]_(a,b<h)
 ~ CΔ^h * 36^(h*m+h*(h-1))
   * m^(-α*h-h*(h-1))
   * ∏_(k=0)^(h-1) k! (α)_k ,
```
where `(α)_k` is the rising factorial. The asymptotic constant is strictly positive. This new theorem upgrades the positive-port *contrast* from its known strict pointwise sign and non-C-finiteness to an eventual **fixed-order moment-Gram signature**. It does not assert a uniform `N` valid simultaneously for unbounded `h`.

**Proof.** PREFIX-1023/1024 derives an all-orders descending-integer-power asymptotic expansion for each `Q^+_{m+4,j}/36^m` by an exact torus Parseval packet followed by analytic Laplace observation. Their common leading term cancels in `Δ`. PREFIX-1017 (three-A6-shift asymptotic), as re-used and quantified in PREFIX-1023, identifies the first nonzero coefficient:
`Δ^+_{m+4}/36^m ~ CΔ m^-7/2`, with `CΔ>0`.
The subtraction therefore admits the full expansion
`Δ^+_{m+4}/36^m=CΔ m^-α[1+Σ_{r=1}^K d_r/m^r+O_K(m^-K-1)]`
at every fixed order `K`. For each fixed `s`, finite differences yield
`D_forward^s (Δ_{m+4}/36^m)=(-1)^s CΔ (α)_s m^-α-s[1+O_s(1/m)]`.
Here `D_forward` denotes the unit forward difference, not the `x d/dx` used above. The unimodular binomial transform on the Hankel rows and columns converts the determinant into that of these differences. After extracting powers of `36`, `CΔ` and `m`, the limiting matrix is `[(-1)^(a+b)(α)_(a+b)]`. Removing matching row/column signs, its determinant equals `∏k!(α)_k>0` by the rising-factorial Vandermonde identity (equivalently Gamma moment positivity). Every fixed leading principal minor has the same positive asymptotic, so Sylvester's criterion proves strict positive definiteness eventually. □

The `π` expression above is reused as a **symbolic asymptotic coefficient from PREFIX-1023**, not numerically evaluated or used to generate a BRC native input, state update or residual claim. All finite checks below are signed BRC-packet **exact integer** Laurent operations.

## Exact finite contrast evidence

The independent Laurent packet was recomputed in this run at `n=5,...,11`, with exactly the signed Stage46 packet above. The seven outputs matched PREFIX-1024's immutable integer table. Independently, the full published PREFIX-1024 exact integer table `n=5,...,18` was consumed, its axis1/axis2 differences formed using exact integers, and all contiguous contrast Hankel determinants of orders `1,...,6` that fit in that table were recomputed by **Bareiss fraction-free elimination**; none was zero or negative. The derived JSON `PREFIX1025_R6_CONTRAST_HANKEL_CERT.json` stores the full exact contrast series and *every* computed determinant, not just a sign count.

Finite evidence is:
```text
h=1: n0=5..18 all >0
h=2: n0=5..16 all >0
h=3: n0=5..14 all >0
h=4: n0=5..12 all >0
h=5: n0=5..10 all >0
h=6: n0=5..8  all >0
```
In particular, for `n0=5`, the first three determinants are
```text
det_h=1 = 25620
det_h=2 = 33514430256
det_h=3 = 2499254569446762816
det_h=4 = 13727712579539428981488102912.
```
The finite calculation locates strong *observed* positive contrast minors through h=6, while Theorem B proves only an order-dependent asymptotic onset.

## Sign-sensitive comparison and next scientific questions

PREFIX-1023/1024 proved that one ordinary other-axis positive-port Hankel matrix has early negative minors and becomes positive at each fixed order eventually. The **axis1-minus-other signed contrast** has a different, stronger finite sign profile, yet its all-order simultaneous positivity remains open.

Next valuable questions: (1) is `[Δ^+_{n0+a+b}]` strictly positive definite for **every** `n0>=5` and **every** order h, i.e. does a genuine positive spectral measure exist for the contrast? A proof needs an exact positivity/measure certificate, not finite minors. (2) Can the signed curvature term in Theorem A be transformed via native BRC/Parseval identities into an exact positive or controlled-remainder jet at a declared future horizon? (3) Obtain explicit effective `N_h` from finite error bounds, not an assumed universal threshold.

Mother question `B_fix,odd(32) ∈ {19,20}` remains open. Attribution retains historical `EM-DIRECT-FBEA5D`, `RA-3FB2D033BE6048D8712FF056`, original SID `MCP-45ad6d29cd534c1aad25595a72e3c532`; these public Source IDs are provenance only. No formal CLAIM/PROGRESS, independent review or theorem admission is claimed.

Proof and exact integer reproduction sources:
- `research_notes/portable_direct/2026-11-23_r6_prefix1023_positive_port_hankel_asymptotic.md`
- `research_notes/portable_direct/2026-11-23_r6_prefix1024_eventual_positive_port_hankel.md`
- `research_notes/portable_direct/PREFIX1024_R6_EXACT_INTEGER_RESULTS.json` at immutable GitHub commit `c4439e36faa633b0d674e8fc225a2000950a97f1`.
- This note and `PREFIX1025_R6_CONTRAST_HANKEL_CERT.json`.
