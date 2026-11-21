# R5 — New universal residue-class first-jet certificates at primitive 27th and 31st roots

**Date:** 2026-11-22 (Asia/Shanghai). **Status:** AUTHOR_PROOF / FINITE_EXACT_INTEGER_CROSSCHECK / NOT_REVIEWED. **Model:** frozen R5 scalar price-multiplicity observer, no native X6 or BRC identification. The scientific input is inherited from the immutable R5 true-event correction at `75d986aa23b68a7ecf9b29dc1006f0e322b35a15`, and the latest first-jet work at `65d3fa2804a3ae6ebd529d843b419a9a931ba3c7`.

## New theorem

Let `f_m(N)` count nonnegative multiplicities `a_p` of the 101 prices `p=214,...,314`, of total price `N`, satisfying at least one of the *separate* events `E_i={sum_(p in S_i) a_p < m}`, where

- `S0={214,215,216,217,218}`;
- `S1={214,216,217,218,219,220,221}`;
- `S2={215,216,217,218,219,220,221}`;
- `S3={223,...,290}`;
- `S4={296,...,312}`.

Let `F_m(q)=R_m(q)/D(q)`, `D(q)=prod_(p=214)^314(1-q^p)`, and `M_m(O_m(N))` denote the least quasi-polynomial coefficient period modulo an `O_m(N)` remainder, for **fixed positive m**.

**Theorem (new unconditional portion of the O_m(N) period classification):**

1. If `m mod 9 in {1,4}`, then the numerator `R_m` has a *simple zero* at each primitive 27th root. Consequently `27 | M_m(O_m(N))`.
2. If `m mod 31 in {1,...,26}`, then `R_m` has a *simple zero* at each primitive 31st root. Consequently `31 | M_m(O_m(N))`.

At either root `R_m(zeta)=0` for **every m>=1**; the claim of a *simple* zero is made for the explicitly stated residue classes. The remaining classes are open here. This does **not** claim a complete least period at precision `O_m(N)`.

In particular both requirements hold simultaneously for infinitely many m, including m=1 and m=4, so `837=27*31 | M_m(O_m(N))` in those intersections. Combining this with the previously saved author-side all-m `O_m(N^3)` theorem is a **conditional** further least-period lower bound; independent review of that theorem remains pending.

## Proof: genuine 31-mask inclusion-exclusion and cyclotomic valuation

For each nonempty event mask `I subset {0,1,2,3,4}`, let `U_I=union_(i in I) S_i` and `P_(I,m)(q)` be the **finite** generating polynomial over multiplicities on `U_I` satisfying *every* selected original load inequality. Since each variable in `U_I` is in a selected bounded event, this polynomial has integer coefficients. The exact numerator is

`R_m(q)=sum_(I != empty) (-1)^(|I|+1) C_I(q) P_(I,m)(q)`, with `C_I(q)=prod_(p in U_I)(1-q^p)`.

No intersection is replaced by the inequality on a support union.

Fix d=27 or d=31, let `zeta` be primitive of order d and let `pi=1-zeta` in `Z[zeta]`. Write `v=v_pi` normalized by `v(pi)=1`. The prime below pi is respectively 3 or 31. If d is a p-power, `v(p)=phi(d)` and for integer `k` with `d does not divide k`, `v(1-zeta^k)=p^(v_p(k))`.

At d=27, the denominator has precisely four vanishing factors: prices 216,243,270,297. In every support S0,S1,S2 the unique d-multiple is 216; S3 includes two (243 and 270); S4 includes one (297). At d=31 the denominator similarly has 217,248,279,310; the unique d-multiple of S0,S1,S2 is 217, S3 contains two and S4 contains one.

Thus every `C_I(zeta)=0`. A term's first derivative vanishes whenever `U_I` contains at least two d-multiples. This removes every mask involving S3, and every mixed S4/first-three mask. The only surviving first-derivative candidates are the seven nonempty first-three masks and S4 by itself.

For `S0`, the unique divisible price `p0` is 216 (d=27) or 217 (d=31). Differentiation with `D_q=q d/dq` gives

`D_q C_0(zeta)=-p0 * prod_(p in S0, p!=p0)(1-zeta^p)`.

**At d=27:** `v(216)=54`, and the four other S0 prices are coprime to 3, each contributing one unit of pi-valuation, so `v(D_q C_0(zeta))=58`. Each S1 or S2 singleton has valuation 62 (their six non-d-divisible prices have values 1,1,1,3,1,1); intersections among the first three have valuation 63; the S4 singleton has valuation at least 70. Thus every candidate other than E0 has valuation strictly greater than 58.

**At d=31:** `v(217)=30`; the four other S0 prices contribute 4, so `v(D_q C_0(zeta))=34`. E1/E2 singleton contributions have valuation 36, their intersections at least 37, and the S4 singleton at least 46. Again E0 is the unique lowest-valuation candidate.

Since every `P_(I,m)(zeta)` is an algebraic integer, multiplying by any such polynomial cannot *decrease* the valuations. In contrast, modulo pi, `zeta=1`, so the exact E0 threshold polynomial satisfies

`P_(0,m)(zeta) = P_(0,m)(1) mod pi = sum_(n=0)^(m-1) binom(n+4,4) = binom(m+4,5) mod p.`

This is the count of all five-variable assignments with total multiplicity below m. If `binom(m+4,5)` is not divisible by p, the E0 term attains valuation exactly 58 (respectively 34) and all others have strictly greater valuation. Therefore `D_q R_m(zeta) != 0`, despite `R_m(zeta)=0`.

Lucas's theorem now identifies the sufficient residue classes exactly:

- `p=3`: `5=(12)_3`. The last two base-3 digits of `m+4` dominate those of 5 precisely when `(m+4) mod 9 in {5,8}`, i.e. `m mod 9 in {1,4}`.
- `p=31`: `5<31`. The units digit of `m+4` is at least 5 precisely when `m mod 31 in {1,...,26}`.

The denominator has **exactly four** vanishing factors at either primitive root. Hence the nonzero first derivative leaves an **exact third-order pole** for F_m there. A third-order primitive-root pole contributes a nonzero degree-two Fourier/quasipolynomial term. It cannot be dropped within an `O_m(N)` remainder, and it forces d to divide the coefficient period. All Galois conjugates are nonzero as well because R_m is integral.

## Finite validation (supporting the proof, not the infinite-domain reason)

A local exact-integer cyclic-ring implementation independently enumerated the seven simultaneous first-three event masks and the S4 event, preserving all selected loads. For m=1 it also evaluated all 31 original masks directly, with complete cyclotomic-vector equality. Tested m=1,...,5 at both d=27 and d=31. In each of those ten cases the first jet was nonzero; for m=2,3,5 at d=27 this is **finite new evidence outside** the p-adic sufficient class, not an all-m claim.

Selected exact normal-form index-zero coefficients of `D_q R_m(zeta)`:
| d | m=1 | m=2 | m=3 | m=4 | m=5 |
|---|---:|---:|---:|---:|---:|
| 27 | -1323 | -2646 | -5751 | 6021 | 8775 |
| 31 | 1302 | 713 | 93 | 744 | -1984 |

Normal forms are computed in `Z[q]/Phi_27(q)` (degree 18) and `Z[q]/Phi_31(q)` (degree 30). `VERIFY.py` and `CERTIFICATE.json` record exact arithmetic and ten full-vector digest witnesses. This local computation and the p-adic argument are author-side evidence, not an independent reviewer acceptance.

## Scientific continuation

Determine whether the first-jet residue classes not resolved by the leading valuation also have nonzero derivatives, potentially by retaining the next pi-adic term or computing the exact rational threshold generating function. Then classify the other primitive root orders of denominator pole order >=3 at precision O_m(N), assembling the complete period only after all dependencies are checked. The valuation filtration is a typed residual observer: it retains a first nonzero cyclotomic jet when the zero-order root observer vanishes. It is **not** a claim of native X6/BRC coordinate equivalence.

**Control/provenance:** portable author-side result; no new formal shared-task CLAIM, RUN, Result, Review or Working Truth asserted. Current active owner could not be established from the native inventory because its exact request returned `FAILED / SOURCE_TREE_TRUNCATED`. This failure leaves the mathematical source publication path available; do not borrow another Researcher ID. Activity checkpoint and current-session authenticated Source association remain a separate pending operation.
