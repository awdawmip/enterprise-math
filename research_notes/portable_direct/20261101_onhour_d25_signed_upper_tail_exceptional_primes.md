# D25: two exceptional zeroes of the signed fourth-order upper-tail observer

2026-11-01. **AUTHOR-SIDE / FINITE EXACT CERTIFICATE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_RUN.**

Mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; task publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin stays c47e13e4aba0e006366f989d6334d443f6333ae3.** Ordinary Research conversation: chatgpt-research-onhour-enterprise-math-20260923; it does not use the maintenance conversation identity chatgpt-hourly-enterprise-math-20260921.

## Original objects, source-preserving statement

In Z_(p), p>3, preserve the two different original unweighted coefficients

\[
a_k=\binom{2k}{k}^2\binom{3k}{k}/216^k,\qquad
b_k=\binom{4k}{2k}\binom{2k}{k}^2/2304^k.
\]

On I_5={0<=k<p:4k>=3p}, separately sum S_A=sum (6k+1)a_k, S_B=sum (8k+1)b_k, then apply the signed observer D_5=S_A-2S_B. The existing **author-proved, not Source-admitted** all-prime reflection theorem (project commit abca20f33ef41943d70135000f27a7af3ed802e0, original note 20261031_onhour_d25_affine_p4_six_ports_upper_reflection.md) proves D_5=p^3 U_p modulo p^4, with m=floor(p/4),

\[
P_0=Q_0=1,\quad
P_{j+1}=P_j\frac{36(j+1)^3}{(2j+3)(3j+4)(3j+5)},\quad
Q_{j+1}=Q_j\frac{288(j+1)^3}{(2j+3)(4j+5)(4j+7)},
\]
\[
U_p=\sum_{j=0}^{m-1}((5+6j)P_j-2(7+8j)Q_j)\pmod p.
\]

## NEW exact finite result and negative witness

A *complete*, exact finite sieve and modular evaluation of all **2,260 primes 5<=p<=20,000** finds **exactly two** zeroes U_p=0 mod p:

| prime | p mod 24 | S_A / p^3 mod p | S_B / p^3 mod p | U_p |
|---:|---:|---:|---:|---:|
| 1019 | 11 | 826 | 413 | 0 |
| 17231 | 23 | 14762 | 7381 | 0 |

Both model-specific tails are nonzero modulo p^4, but their signed difference vanishes. The previous theorem's terminal k=p-1 contributes -9 modulo p for **every prime p>3**, so the *remaining indices* contribute +9 at each exceptional prime: the cancellation is within the genuine highest band, not deletion of an individual zero term. This is an exact counterexample to the unqualified statement **U_p is nonzero for every prime**.

Control values for the actual D25 target class:

| p | S_A/p^3 | S_B/p^3 | U_p | D_5 mod p^4 |
|---:|---:|---:|---:|---:|
| 13 | 3 | 6 | 4 | 8788 |
| 19 | 9 | 16 | 15 | 102885 |
| 373 | 90 | 119 | 225 | 11676401325 |

Both exceptional primes are **outside** the D25 p≡13,19 (mod24) target. No statement about nonvanishing for all target primes or beyond p=20,000 is proved.

## Certificate, its domain and independence

The exact, executed Python standard-library source is research_notes/portable_direct/d25_signed_upper_tail_compact_20261101.py. It verifies all 2,260 primes using the already-proved reflected U recurrence and asserts the exhaustive zero list. Separately it compares the **original weighted A/B tails** at p=13,19,373,1019,17231 by TWO independent arithmetic routes: a forward rational hypergeometric coefficient recurrence and a p-stripped unit-factorial implementation of the original **integer binomial** formulas, with modular p-valuation reinstated. For all five primes both tails agree, and D_5=p^3 U_p modulo p^4. Exact arithmetic only, no floating point or tolerance. All assertions PASS. The two exceptional **fixed-prime congruences** and exhaustive **finite range** are reproducible arithmetic certificates; no infinite-prime statement or formal checker verification is inferred.

BRC and observer-safety application: the retained carrier is (p, I_5, the individual k-labelled original model A/B weighted terms, their p-adic valuations, signed provenance). The readout map (S_A,S_B) -> S_A-2S_B has a nontrivial zero fiber at both witness primes. A zero coupled scalar DOES NOT mean the independent components or their internal signs have vanished; one cannot drop them under a future model-specific observer without a factorization/fiber-constancy certificate. The external p-adic polynomial model is not a native X6 plane or H0/B0 result.

## Exact continuation and authority boundary

Frozen mother LIFT/JT2 remains Delta_p-R_p≡(A_p-p)/p^2≡0 (mod p) for all p≡13,19 (mod24). The affine A_p-2B_p+pχ_{-3}(p)≡0 (mod p^4) remains a conjecture. Do not redo prior UR/CM0, six-port theorem, p19 reflection, or original p13 Jacobi first-jet theorem; the last author's smaller exact pending p13 proof is the Jacobi two-shift congruence from project commit ac48238d40c28c9ad139faa5b0e11cb7defdd8f9. This new certificate *only* rules out a blanket nonvanishing shortcut in the broader fourth-order proof.

The **original same-class fixed p=373 native H0/B0 divided-power experiment** is a distinct unmet scientific obligation: actual [X]U mod 139129, module rank, operator's semilinear Frobenius type and normalization eta, signed odd Green/Hesse and κ, original Delta-R and independent replay. Support issue awdawmip/enterprise-math#1559 was OPEN without an assignee at this run's read; no different scalar surrogate passes that gate. Original p=373 scalar Delta=R=196 mod373 is already known, not a native result.

Gateway em_status v0.6.11 at 2026-11-01: research_authority_granted=false, executor_binding_configured=false; original own-lane request research-onhour-20261031-0205-dispatch-r15 returned CONTROL_REQUEST_NOT_FOUND in this client's scope. The reported recovery_status is not exposed as a callable tool, and a historical missing request is not Source ownership. No valid current session, CLAIM/open/run, native Source checkpoint, Result, review or acceptance was created; the three earlier staging artifacts remain independent; user schedule/notification and P000/ACTIVE worldview are unchanged.

**Next:** consume this published author-side exceptional-zero certificate, continue exact p13 Jacobi first-jet proof or counterexample and prioritize a genuinely authorized same-original-class H0/B0 p373 executor. Use Source-native continuation/claim/review only after current authority is verified.

## Second exact unit: both exceptional primes satisfy the full original affine relation

We additionally ran the **same original integer-binomial code with lower endpoint 0**, hence full weighted A_p and B_p rather than only their highest ports. The two chosen least nonnegative residues modulo p^4 are

| p | A_p mod p^4 | B_p mod p^4 | integer A_p-2B_p-p on these representatives |
|---:|---:|---:|---:|
| 1019 | 287800440629 | 143900219805 | 0 |
| 17231 | 48238865242842508 | 68196423129404799 | -88153981015984321 = -(17231)^4 |

For both primes p≡2 (mod3), χ_{-3}(p)=-1. Thus **A_p-2B_p+pχ_{-3}(p)≡0 mod p^4** is verified independently by original integer-binomial evaluation; A_p≡B_p≡-p mod p^3 also holds at both exact inputs. Combined with D_5=0 mod p^4, the **lower five** original signed ports by themselves satisfy the full affine scalar congruence at these two inputs. The calculation neither proves the conjectural all-prime affine relation nor makes the port lossless for a future model-specific observer.

The repository verifier now runs both this full original evaluation and the earlier 2260-prime finite upper-reflection scan; raw integer equalities above are standalone cross-checkable witnesses.
