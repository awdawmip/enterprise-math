# D25/LIFT — exact p-local product and the next-digit Jacobi endpoint anomaly

Date: 2026-10-25. Scope: mathematical continuation **of the existing portable Jacobi second-jet endpoint lemma**, not a new native CM/Frobenius experiment. Author derivation; exact author verification only; **UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / NO_NEW_NATIVE_CHECKPOINT**.

Parent Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, immutable publication `TP2-B6F4FC938FF94941C1B7`; parent Objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Original frozen scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (not changed). The source is the original truncated Jacobi hypergeometric coefficient family, **not** authenticated original-class CM data.

## Smallest new question

The previous portable proof [universal second-jet forcing](20261025_hourly_d25_terminal_jacobi_jet_universal_forcing.md) determined the endpoint coefficient `-40 m² w_{p-1} ≡ -4 (mod p)` and its observer at `z=1/2` as `-2 (mod p)`. Can one preserve its next digit **without** treating the `-4` as an all-precision constant, losing endpoint provenance, or replaying the first-digit UR theorem?

## Theorem (exact complement product, all finite p-adic precisions)

For every prime `p=6m+1 ≥ 7`, put `N=p-1`, and use the same finite Jacobi family

\[
b_n(x)=\frac{(-x)_n(-2x)_n}{(n!)^2},\qquad
w_N=\frac12\,b_N''(m).
\]

Define the p-unit products and observer

\[
P_k=\prod_{j=1}^{k}\left(1-\frac pj\right),\quad
K_p=-40m^2w_N,\quad E_p=K_p2^{-p}.
\]

The following are **exact rational identities** (in particular, valid at arbitrary finite p-adic precision):

\[
\boxed{\displaystyle
w_N=\frac{2}{(m+1)(2m+1)P_{m+1}P_{2m+1}},}
\]

\[
\boxed{\displaystyle
K_p=-4\frac{(1-p)^2}{(1+p/5)(1+p/2)P_{m+1}P_{2m+1}},}
\]

\[
\boxed{\displaystyle
E_p=-2\frac{(1-p)^2}
{(1+p/5)(1+p/2)2^{p-1}P_{m+1}P_{2m+1}}.}
\]

All factors inverted here are p-units. The full endpoint observer is therefore retained as a **finite, source-marked, invertible product**; it cannot be replaced by its mod-p reduction before a higher-precision operation.

## The next two digits

Write

\[
H_1=\sum_{j=1}^{m+1}\frac1j+\sum_{j=1}^{2m+1}\frac1j,\qquad
H_2=\sum_{j=1}^{m+1}\frac1{j^2}+\sum_{j=1}^{2m+1}\frac1{j^2},
\]

and let `q_p(2)=(2^{p-1}-1)/p` (the integer Fermat quotient). Set

\[
a=H_1-\frac{27}{10},\qquad
b=\frac{H_1^2+H_2}{2}-\frac{27}{10}H_1+\frac{279}{100}.
\]

Then

\[
\boxed{\ K_p\equiv-4(1+pa+p^2b)\pmod{p^3},\ }
\]

\[
\boxed{\ E_p\equiv-2\{1+p(a-q_p(2))
+p^2[b-aq_p(2)+q_p(2)^2]\}\pmod{p^3}.\ }
\]

In particular, the **next-digit correction at the original observer** is

\[
\boxed{\displaystyle
E_p\equiv-2\left[1+p\left(
H_{m+1}+H_{2m+1}-\frac{27}{10}-q_p(2)
\right)\right]\pmod{p^2}.}
\]

Here `H_k=Σ_{j=1}^k 1/j`. Consequently the formerly universal `-2 mod p` anomaly is **not** an all-precision constant. Its second digit depends on a sourced harmonic correction and the evaluation-point Fermat quotient. This is an exact conditional-input formula, not a new axiom, numerical fit, or proof of LIFT.

## Proof

The prior exact factorial differentiation gives

\[
w_N=
\frac{2(-1)^m m!(2m)!(5m-1)!(4m-1)!}{((p-1)!)^2}.
\]

For `0≤k≤p-1` the complementary factorial identity is exact:

\[
k!(p-1-k)!
=\frac{(-1)^k(p-1)!}{P_k},
\]

because `(p-1)!/(p-1-k)!=∏_{j=1}^k(p-j)=(-1)^k k!P_k`.
Use `k=m+1` and `k=2m+1`, cancel the two copies of `(p-1)!`, and track both signs. This yields the exact formula for `w_N`. Substituting `m=(p-1)/6` yields the exact formula for `K_p`; multiplying by `2^{-p}` gives `E_p`.

Since `j<p`, p-adic geometric expansion is legitimate for each `(1-p/j)^{-1}`. Multiplication of the finitely many factors gives

\[
(P_{m+1}P_{2m+1})^{-1}
\equiv 1+pH_1+\frac{p^2}{2}(H_1^2+H_2)\pmod{p^3}.
\]

Direct multiplication also gives

\[
\frac{(1-p)^2}{(1+p/5)(1+p/2)}
\equiv 1-\frac{27}{10}p+\frac{279}{100}p^2\pmod{p^3}.
\]

Finally `2^{p-1}=1+pq_p(2)`, and its inverse is `1-pq_p(2)+p²q_p(2)² mod p³`. Combining these expansions proves both congruences. Every denominator is invertible because `p≥7` and `j<p`. The exact product formula, unlike a truncated power series, may be used at **any** later precision.

## Exact certificates and validation scope

At the original field observer `z=1/2`:

| p | `w_{p-1} mod p²` | `K_p mod p²` | `E_p mod p²` | `H_1 mod p` | `q_p(2) mod p` |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 7 | 19 | 24 | 40 | 1 | 2 |
| 13 | 79 | 35 | 11 | 0 | 3 |
| 19 | 224 | 224 | 226 | 13 | 3 |
| 373 | 106607 | 8202 | 17156 | 221 | 204 |

In particular, `E_7=40 mod 49` and `E_13=11 mod 169`; neither is `-2` at that precision. Both remain `-2 mod p`, exactly as in the previous theorem.

The adjacent Python standard-library verifier [`20261025_hourly_d25_jacobi_endpoint_padic_product_check.py`](20261025_hourly_d25_jacobi_endpoint_padic_product_check.py) checks the factorial route, complementary product, harmonic second-order expansion, and the evaluation-point Fermat quotient formula **modulo p³** for the 35 primes `7≤p≤373, p≡1 (mod 6)` plus `p=1327,19963`: **37 author-checked cases, all PASS**. Direct `Fraction` equality of the rational product holds for `p=7,13,19`. No floating-point arithmetic is used. These cases check the proof, not prove its universal quantifier; universal validity follows from the rational identities and p-local expansions.

## Source typing, BRC use, limitations, continuation

- Provenance: original finite-rank Jacobi Pochhammer data and its terminal second parameter derivative; observer `z=1/2`; signed boundary `-40m²w_N z^p`; exact p-adic factorial/product/harmonic/Fermat quotient operations. BRC relevance is **source-preserving observer/residual composition**; this is **not** an executed native BRC/CM or divided-power Frobenius experiment.
- Do not redo: accepted first-digit UR/JT0; prior `-4 mod p` endpoint proof; already-verified portable terminal bridge. Their published identities are inputs, not newly completed predecessor Source units.
- Open D25/LIFT/JT2 question remains the signed, **all-target-prime** identity `B_{01,p}+A_2H_0/72-T_{jet,p}=0 mod p`. The exact `E_p` product shows the second digit that would have to be respected when lifting a telescoper to higher precision, but it **does not** itself close the mod-p target. Keep the nonzero forcing term in the finite differential equation.
- Missing native evidence: current exact winning Researcher claim/open/run and checkpoint authorization; same original CM class `H_0/B_0`, `[X]U mod p²`, Frobenius rank/normalization, and the verified kappa map. Source-independent review and formal checker evidence have **not** been obtained.
- Next smallest action: seek a signed telescope of the already-established Jacobi reduction and the reflected Clausen corner **at the required mod-p precision**, explicitly retaining the terminal port. If that cannot be closed, classify the smallest obstruction and only then exploit this all-precision endpoint product for an elevated observer.
