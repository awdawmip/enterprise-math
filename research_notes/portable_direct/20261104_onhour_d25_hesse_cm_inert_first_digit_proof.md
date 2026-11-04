# D25 — Hesse/CM proof of the original 216 first-digit inert-class criterion

Date: 2026-11-04 (Asia/Hong_Kong). Author-side portable mathematics only. **EXACT CLASSICAL-CM COROLLARY / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`.
Publication: `TP2-B6F4FC938FF94941C1B7`. Frozen scientific source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Research logical lane: `chatgpt-research-onhour-enterprise-math-20260923`. No maintenance-lane claim or act.
Consumes the exact prior Clausen-square theorem in `research_notes/portable_direct/20261104_onhour_d25_dual_clausen_first_digit_cm_observer.md`, and retains the original 216 coefficient source.

## Newly discharged lemma (precise domain)

For every prime `p=6r+1 >= 7`, define

```
a_k = (2k)!(3k)! / ((k!)^5 216^k), 0<=k<p
A_p = sum_{k=0}^{p-1} a_k
M_p = sum_{k=0}^{p-1} k a_k
W_p = A_p + 6 M_p
epsilon = (-6/p) (Legendre symbol).
```

**Theorem:** `A_p = 0 (mod p)` if and only if `epsilon=-1`. Equivalently, among primes `p=1 (mod 6)`, the zero classes are exactly `p=13,19 (mod 24)`. Moreover, in those two classes `M_p=W_p=0 (mod p)`.

This closes the **216-family first-digit CM zero/nonzero selector for p=1 mod 6**, previously supported by finite data only. It does not yet determine the p²/p³ digit defect or the full D25 hard target.

## Exact proof

1. **Clausen square (reused, not reproved).** Over `F_p`, put
   `F_r(x)=sum_{k=0}^r ( (r choose k)(2r choose k) ) x^k` and
   `P_r(x)=sum_{k=0}^{2r} [(1/2)_k(1/3)_k(2/3)_k/(k!)³]x^k`.
   The prior theorem gives `P_r(x)=F_r(x)^2` in `F_p[x]`. The original source is `A_p=P_r(1/2)`, since `v_p(a_k)>=1` for `k>2r`. Thus `A_p=F_r(1/2)^2`; similarly, `M_p=2 F_r(1/2)(theta F_r)(1/2)` with `theta=x d/dx`.

2. **A quadratic change of observer with exact finite truncation.** Set `u²=2` and `z=(2+u)/4`, so `4z(1-z)=1/2`. The classical Gauss quadratic identity
   `2F1(a,b; a+b+1/2; 4z(1-z)) = 2F1(2a,2b; a+b+1/2; z)`
   with `(a,b)=(1/6,1/3)` yields, after legal coefficient reduction below degree `2r<p`,
   ```
   F_r(4z(1-z)) =
   H_r(z) := sum_{k=0}^{2r} ( (2r choose k)(4r choose k) ) z^k   (mod p).
   ```
   Indeed `1/6=-r`, `1/3=-2r`, `2/3=-4r (mod p)`; the first series stops at k=r and the second at k=2r. No division by p occurs at these degrees. Therefore `F_r(1/2)=H_r(z)`.

3. **Hesse curve and its genuine Hasse invariant.** Choose `lambda³=z^(-1)` in an algebraic closure and consider the smooth plane cubic
   `E_lambda: X³+Y³+Z³-3 lambda XYZ=0`.
   Since `z(1-z)=1/8`, the model has good reduction away from 2 and 3. Its Hasse invariant is, up to a nonzero factor, the coefficient of `(XYZ)^{p-1}` in `(X³+Y³+Z³-3lambda XYZ)^{p-1}`:
   ```
   h_p(lambda) = sum_{t=0}^{2r} ((p-1)!/[t!³(p-1-3t)!])(-3lambda)^(p-1-3t).
   ```
   Using Wilson and `(3t)!/(27^t t!³) = (1/3)_t(2/3)_t/(t!)²`,
   `h_p(lambda)=(-3lambda)^(p-1) H_r(z)` in characteristic p.
   The factor is a unit. Hence `H_r(z)=0` exactly when this smooth elliptic curve is supersingular.

4. **One exact CM discriminant, rather than a fitted character.** The Hesse j-function and our parameter give
   ```
   j(E_lambda) = 27(1+8z)^3/[z(1-z)^3]
               = 2417472 + 1707264 sqrt(2).
   ```
   It satisfies the classical Hilbert class polynomial
   `H_{-24}(J)=J²-4834944 J+14670139392`, the CM class polynomial of the maximal order of `Q(sqrt(-6))`, discriminant -24. Thus the characteristic-zero curve has CM by this order. Deuring's good-reduction criterion says precisely that its reduction is supersingular if and only if p is nonsplit in `Q(sqrt(-6))`. As `p>=7`, p is unramified in this quadratic field: nonsplit iff `(-6/p)=-1`.
   Combining steps 1–4 gives the claimed equivalence, and in the inert case also `M_p=W_p=0 (mod p)`.

The proof uses published classical Gauss/Clausen transformations, the Hesse invariant calculation, the Hilbert class polynomial and Deuring's CM reduction theorem. It is a **scoped, source-attributed new corollary/bridge**, not an independent proof of those classical theorems.

## Reproducible finite evidence and observer typing

Executed exact standard-library integer checker: `d25_hesse_cm_inert_first_digit_checker_20261104.py`. Results: **611** primes `7<=p<=10000, p=1 mod6`; **312** inert (all `F=A=M=0`), **299** split (all `F,A !=0`), **22** independent entire-polynomial coefficient comparisons (eligible p<=211), all pass. The checks also verify `4z(1-z)=1/2`, both Hilbert class polynomial and explicit j root in `F_p[u]/(u²-2)`, and the equality of both parameterizations. At p=13,19,373: F=A=M=0; at p=7: (F,A,M)=(2,4,4); at p=97: (2,4,64). Computation is exact mod p and supports the formal steps; the universal classification rests on steps 1–4.

Retain the typed **(original coefficient source, prime, valuation band, A, M, W, Hesse Hasse, field of definition)** observer. CM/Hasse vanishing is an exact **first-digit projection** and does not erase higher digits or independent H0/B0 native evidence. BRC applicability audit: this classical hypergeometric family has no evidenced native BRC carrier or BRC operation under the frozen Task; do not claim a BRC theorem from the observer notation. Actual useful reuse here is source/valuation preservation and exact finite-field mapping.

External source locators:
- Classical Hilbert class polynomial -24: https://numberdb.org/Hilbert_class_polynomials
- Deuring criterion (explicit theorem): https://link.springer.com/article/10.1007/s10231-024-01528-x
- Hesse-pencil context: https://arxiv.org/abs/1606.08352
- Prior D25 Clausen-square author-side proof: `research_notes/portable_direct/20261104_onhour_d25_dual_clausen_first_digit_cm_observer.md`.

## Durable next frontier and actual authority

Mother objective: frozen `Delta_p-R_p=0 mod p` for `p=13,19 mod24`. The original 216/2304 comparison `W_p-V_p=0 mod p³` and fixed p=373 native H0/B0 remain open.

**Next smallest scientific action:** take the exact CM zero `A_p=M_p=0 modp` and construct a **p-adic first nonzero digit/source-moment formula** for `D_p=(A_full-B_full)/p² modp`, preserving both original models' p-valuations and full truncations. First discriminants p=13 (D=7), 19 (D=1), 373 (D=241); derive the signed counterpart of the true moment observer and seek a termwise WZ/Green lift to p³. Do not use the CM first-digit theorem as evidence that the p² defect vanishes.

Native fixed-373 `[X]U mod 139129`, rank, true semilinear Frobenius and independent replay stay on original issue `awdawmip/enterprise-math#1559`; NOT_EXECUTED by this author-side proof.

Native service `em_status` read at 2026-11-04 17h local: version 0.6.11, `research_authority_granted=false`, `source_sync.control.state=CODE_REVIEW_REQUIRED`. Own read-only `continuation` request `onhour-d25-20261104-1702-continuation-read` later returned `FAILED / SOURCE_TREE_SIZE_LIMIT files=20001/20000` at Source SHA `5b05a2828a84b3fb73c6069d9dd0af6fb2a0aa6c`. Preserve that exact request and failure; do not resubmit or infer absent owner. Previous `research-onhour-20261031-0205-dispatch-r15` was `FAILED / UPSTREAM_CODE_REVIEW_REQUIRED` in `kimi-query-bridge#6633`. No new successful CLAiM/open/run/native checkpoint/Result, no maintenance-conversation mutation. Same research lane and old independent staging preserved.

**Artifact class**: `AUTHOR_SIDE_PORTABLE_GITHUB / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`. This GitHub path is an independently discoverable research artifact, not a new Source checkpoint or a substitute native benchmark.
