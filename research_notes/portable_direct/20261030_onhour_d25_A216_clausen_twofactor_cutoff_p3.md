# D25 / SECOND-DIGIT-LIFT — two-factor Clausen lifting with the exact p² cutoff port

Date: 2026-10-30 (Asia/Hong_Kong). Logical Research lane: `chatgpt-research-onhour-enterprise-math-20260923` (separate from maintenance). Mother objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` remains unchanged.

**Classification:** AUTHOR-SIDE / PROVED COEFFICIENTWISE p³ REDUCTION / EXECUTED ORIGINAL-BINOMIAL EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING. This is a new source-preserving paired reduction of the actual LIFT, not a proof of the final all-prime congruence or a native H0/B0 calculation.

## Original object and the reduced Gauss carrier

For every prime `p=6m+1>=7`, put
[
 A_p=sum_{n=0}^{p-1}(6n+1)rac{inom{2n}{n}^{2}inom{3n}{n}}{216^n},
 qquad g_k=rac{(1/6)_k(1/3)_k}{(k!)^2},
 qquad G_p(z)=sum_{k=0}^{p-1}g_kz^k.
]
All rational expressions are in `Z_(p)` for `0<=k<p`. Let `x=G_p(1/2)`, `y=G_p'(1/2)`.

The already-published 2026-10-26 Clausen derivative source-port note (commit `2d7bdfd7821d3afac8eaefb4b88bfedca8ff46be`) established the exact truncated convolution `W=M(M+12N)-Q` and original `Q/p²=R_p`. Below is an independent explicit factorial formula for `Q/p²`, plus exact p³ regression; it is **not** a new discovery of the preexisting convolution or original LIFT equivalence.

The classical Clausen identity, as an exact formal-power-series identity over Q, states
[
 left({}_2F_1(1/6,1/3;1;z)ight)^2
 ={}_3F_2(1/2,1/3,2/3;1,1;z).
]
For every coefficient `n<p`, the corresponding term on the right is exactly `a_n z^n 2^n`, where `a_n=\binom{2n}{n}^2\binom{3n}{n}/216^n`. Therefore the following equality holds **exactly** in Q, with the native original `6n+1` weight and cutoff retained:
[
 A_p=x^2+6xy-E_p,qquad
 E_p=sum_{\substack{0\le i,j<p\\i+j\ge p}}
 [6(i+j)+1],g_i g_j,2^{-(i+j)}. \tag{1}
]
Explanation: `1+6\theta` acting on `G_p(z)^2` gives `G_p(z)^2+12zG_p(z)G_p'(z)`; at `z=1/2` this is `x^2+6xy`. Coefficients with `n<p` are precisely the original `A_p`; (1) subtracts the convolution indices `n>=p`. The expression is an exact arithmetic identity, not an informal replacement by an infinite hypergeometric series.

## Theorem: universal explicit two-index boundary modulo p³

The coefficient `g_k` has exact p-adic valuations
[
 v_p(g_k)=
 \begin{cases}
 0,&0\le k\le m,\\
 1,&m<k\le2m,\\
 2,&2m<k<p.
 \end{cases} \tag{2}
]
Indeed, `(1/6)_k` first contains `p/6` at index `m`, and `(1/3)_k` first contains `p/3` at index `2m`; denominators `k!` are p-units.

Define for `2m<k<p`
[
 c_k=\frac{(-1)^m m!(2m)!(k-m-1)!(k-2m-1)!}{18(k!)^2}\pmod p, \tag{3}
]
and `P_i=\binom mi\binom{2m}i` for `0<=i<=m`. All factorials in (3) are of arguments less than p; in particular the denominators are invertible mod p. By isolating the unique p-factor in each of the two numerator Pochhammer symbols, `g_k/p²≡c_k (mod p)` and `g_i≡P_i (mod p)` in the low zone.

For `i+j>=p` and `0<=i,j<p`, every pair other than the two orientations
[
 1\le i\le m,\quad p-i\le j\le p-1
]
has `v_p(g_i g_j)>=3`: two middle indices cannot sum to p; a middle/high pair has valuation >=3; two high indices have >=4. Thus (1) gives the **all-prime formula**
[
 \boxed{A_p\equiv x^2+6xy-p^2\tau_p\pmod{p^3}},\tag{4}
]
where the explicit signed, source-labeled cutoff is
[
 \boxed{\tau_p=
 2\sum_{i=1}^{m}\sum_{k=p-i}^{p-1}
 (6(i+k)+1)\binom mi\binom{2m}i\,
 \frac{(-1)^m m!(2m)!(k-m-1)!(k-2m-1)!}{18(k!)^2}
 2^{-(i+k)}\pmod p.}\tag{5}
]
All exponent and operation order data remain explicit. The cutoff has a triangular index domain; no normalization to an unsigned count or replacement by a native operator is asserted.

## Corollary: exact target-classes second-digit criterion

Reuse the previously derived target-class CM/Hasse zero `P_m(1/2)=0 (mod p)`, where `P_m(z)=\sum_{i=0}^m\binom mi\binom{2m}i z^i`, and the coefficientwise congruence `G_p(z)≡P_m(z) (mod p)`. Consequently `p|x` for `p≡13,19 (mod24)`. Set `h=x/p∈Z_(p)`. Equation (4) becomes
[
 \boxed{A_p\equiv 6p h y+p^2(h^2-\tau_p)\pmod{p^3}}.\tag{6}
]
The frozen arithmetic LIFT is therefore equivalent to **one exact two-factor Gauss derivative condition**:
[
 \boxed{6h y+p(h^2-\tau_p)\equiv1\pmod{p^2},
 \qquad p\equiv13,19\pmod{24}.}\tag{7}
]
Under accepted D24 first-digit `A_p≡p (mod p²)`, the quotient `(6hy-1)/p` is integral and (7) is equivalently
[
 \boxed{(6hy-1)/p+h^2-\tau_p\equiv0\pmod p.}\tag{8}
]
Equations (7)–(8) are an **equivalent remaining proof obligation**, not a completed LIFT proof. They are materially different from the old same-kernel single-term Gosper search: the true two-factor product and the nonvanishing cutoff are retained.

## Executed exact evidence and genuine source arithmetic

Executed Python 3 standard-library integer checker:
`research_notes/portable_direct/d25_a216_twofactor_clausen_boundary_20261030.py`.

For all **45** primes `7<=p<500, p≡1 (mod6)`, including **23** in the frozen two residue classes, the checker independently evaluates the original `(6n+1)binom(2n,n)^2 binom(3n,n)/216^n` modulo `p³`; computes `G_p`, its derivative, the boundary (5), and verifies (4). It verifies each high-zone factorial coefficient via `g_k/p²` and checks (6)–(7) on the target class. Additional direct fixed-prime re-evaluation at `p=373` passed. The range is finite exact evidence, not the proof of (7) for all primes.

| p | m | G_p(1/2) mod p³ | G_p'(1/2) mod p² | τ_p mod p | A_p mod p³ |
|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 988 | 1 | 0 | 13 |
| 19 | 3 | 1596 | 344 | 12 | 19 |
| 373 | 62 | 24495656 | 78545 | **196** | 373 |

**Nonzero boundary and exact reconciliation to the frozen port:** at p=19 and p=373, dropping `p²τ_p` changes the original p³ arithmetic. The previously published author-side source alignment [2026-10-26](../portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md) already proved `Q/p² ≡ R_p (mod p)` for the original reflected scalar `R_p`, using the original `B_k=((1/6)_k(1/3)_k)/(2^k(k!)²)` and the same signed cutoff `Q`. The current `B_k=g_k2^{-k}` and `Q=E_p` are **definitionally identical** to those sources. There is also a direct all-target-primes index reconciliation: reindex the high index in (5) by `a=p-k`, so that `1<=a<=i<=m`; then `6(i+k)+1≡6(i-a)+1 (mod p)`, `B_i≡2^{-i}binom(m,i)binom(2m,i)`, and `B_{p-a}/p²≡2^{-(p-a)}c_{p-a}`. The prior independently proved equality `B_{p-a}/p²≡C_a` then yields
[
\tau_p\equiv 2\sum_{i=1}^{m}B_i\sum_{a=1}^{i}(1+6(i-a))C_a\equiv R_p\pmod p.
]
Thus the `196` at p=373 is an **actual source-aligned equality**, not merely a matching numeric residue. The new contribution of this note is the explicit factorial triangular representation (3)–(5), its direct valuation proof, and an independent original-binomial p³ checker; the underlying Clausen cutoff identity, Source R alignment, and equivalence to LIFT were **already obtained** in the 2026-10-26 author note and are consumed rather than claimed anew. The original CM class, source labels and signed observer remain unchanged.

## BRC and next exact obligation

BRC resolution: **COMPOSE_APPLIED**, using signed two-source convolution with port labels `(i,k)`, valuation strata `(0,1,2)`, exact integer factorial carrier and the declared `(1+6θ)` observation. This is a calculation in external hypergeometric scalar arithmetic, not an implementation of native `X6/H0/B0`. The preserved residual `τ_p` is essential to the original mod-`p³` output.

**Smallest unfinished mathematical step:** prove (or refute with exact original-number counterexample) (7) uniformly on the frozen target classes. A productive starting sublemma is to compute the p-adic Gauss value `h=G_p(1/2)/p` and derivative `y` jointly through the CM parameter lift, **with** the explicit (5) cutoff, rather than using a homogeneous truncated Clausen square. The existing low-two-zone `T²` jet and signed regular middle source may be used to cross-check the identity but are not recredited.

**Separate native benchmark remains mandatory:** `awdawmip/enterprise-math#1559` requires fixed `p=373` original H0/B0 divided-power, `[X]U (mod 139129)`, actual semilinear Frobenius and basis/eta, module rank, signed Green/Hesse and κ with independent replication. The external scalar theorem (4) does not execute this object.

**Operational state at source read 2026-10-30:** EM Site reports `research_authority_granted=false`, `write_relay_enabled=false`, control Source sync `CODE_REVIEW_REQUIRED`, native compute unavailable in this client, and own checkpoint-list read `ACCESS_DENIED`. No successful Source recovery_status/own CLAIM/open/run/Result receipt has been established here. No new control request was issued, and old unknown request IDs were not replayed. Existing author-side repository persistence does not imply Source registration, checkpoint or admission. Research and maintenance logical identities remain separate.
