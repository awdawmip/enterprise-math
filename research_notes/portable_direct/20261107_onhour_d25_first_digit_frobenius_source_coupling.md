# D25 — First-digit Frobenius source coupling at the frozen 216/2304 fibers

Date: 2026-11-07. TASK_RESEARCH author-side continuation, **proof of a conditional identity + exact finite certificates; UNREVIEWED / NOT_ADMITTED**. Logical lane: `chatgpt-research-onhour-enterprise-math-20260923`; maintenance conversation excluded. Mother task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Inputs: three-stratum finite Gauss/Clausen-Euler decomposition and signed four-port theorem at `21006d033963b83a33767ae7d058ba3924db8da1`. No repinning.

## Selected unfinished unit and exact definitions

Work on the lowest p-adic digit of the original signed four-port transmission (not another high-tail calculation). Let prime `p ≡ 13 or 19 (mod 24)`; all rational calculations take place in `Z_(p)`.

* A (216): `m=(p-1)/6`, `u=m,v=2m,c1=1/6,c2=1/3`, `x=1/2`, `epsilon=0`, `lambda=6`.
* B (2304): for `p≡19 mod24` take `p=8k+3`; for `p≡13 mod24` take `p=8k+5`. In both cases `u=k,v=3k+1,c1=1/8,c2=3/8,x=1/9,lambda=8`. Set `epsilon=0` or `1` respectively. The B Gauss parameters are `(1/8,3/8)` in the first class and Euler-transformed `(5/8,7/8)` in the second.

For each model define
```
Q(z) = sum_{i=0}^{u} binom(u,i) binom(v,i) z^i
G_p(z) = sum_{n=0}^{p-1} ((-u+c1*p)_n (-v+c2*p)_n)/(n!)^2 z^n
J = (z*dQ/dz)(x).
```
Keep A and B separate as signed source/provenance ports; `W_p` and `V_p` remain the original weighted integer-binomial sums.

## Theorem: exact conditional first-digit product law

Assume `Q(x) ≡ 0 (mod p)` for the chosen model and prime. Put `g=G_p(x)/p mod p` (well-defined under this hypothesis). Then
```
 W_p/p ≡ 12 J_A g_A                                      (mod p)
 V_p/p ≡ 16 J_B g_B,                   p ≡ 19 (mod 24)    (mod p)
 V_p/p ≡ (128/9) J_B g_B,              p ≡ 13 (mod 24)    (mod p).
```
These are **identities modulo p for every p in the stated class satisfying the explicitly stated Hasse-zero hypothesis**, not an unconditional assertion that every target prime has Hasse zero or that the mother supercongruence has been proved.

**Proof.** The already proved projected Clausen/Euler fold gives, modulo `p^2`, the corresponding weighted readout of `C(z)(Q(z)+pF_1(z))^2` with `C=1-epsilon*z`. The four-port support theorem shows there is no above-cutoff contribution at order `p`. Write `U=Q+pF_1`. Under the hypothesis, `U(x)=p g mod p^2` and `(z*dU/dz)(x)=J mod p`. The A observer `1+6D` produces `U^2+12 U DU`, proving the first identity after division by `p`. For B, `(1+8D)((1-z)U^2)=(1-9z)U^2+16(1-z)U DU`; at `z=1/9` the first summand vanishes **exactly** and `16(1-1/9)=128/9`. Without Euler (`epsilon=0`) the B readout is `U^2+16U DU`. This proves all three identities. QED.

A finer **BRC/provenance split** follows by writing `q=Q(x)/p mod p` and `f=F_1(x) mod p`. Since `g=q+f mod p`, the first digit is exactly the signed sum of a zeroth-coefficient lift `c J q` and a first perturbation `c J f`. Only their sum is the observer output; discarding either coordinate generally changes it.

The target first-digit normalization `W_p≡V_p≡p (mod p^2)` is thus reduced, under the Hasse-zero hypothesis, to explicit unit equations `12 J_Ag_A=1` and `c_BJ_Bg_B=1` in `F_p`. The latter equalities are now precise Frobenius/Wronskian proof targets.

## Exact finite evidence (not a universal Hasse-zero proof)

`d25_first_digit_source_coupling_20261107.py` evaluates the native A/B Gauss recurrences modulo `p^2` separately from the original weighted 3F2 integer-binomial recurrences. It checks every target prime `p <= 2000`: **77 primes, 154 independent model/weighted pairs, all PASS**, with Hasse zeros `Q_A(x)=Q_B(x)=0 mod p` and both unit equations `=1 mod p`. These are exact modular integers, no floats. Witnesses below are in the displayed `F_p`; columns denote `(q,J,f,g; cJq,cJf)` and the final two columns sum to 1 modulo p.

| p | A: (q,J,f,g; low,first) | B: (q,J,f,g; low,first) |
| --- | --- | --- |
| 13 | (7,7,4,11; 3,11) | (3,12,8,11; 5,9) |
| 19 | (6,1,2,8; 15,5) | (10,7,18,9; 18,2) |
| 43 | (4,20,27,31; 14,30) | (34,34,29,20; 6,38) |
| 67 | (16,40,45,61; 42,26) | (11,35,3,14; 63,5) |
| 373 | (340,294,57,24; 325,49) | (326,41,33,359; 30,344) |

In particular `325+49=374≡1 mod373` on A and `30+344=374≡1 mod373` on B, while their port components differ. This is an exact signed observer example: the p-adic quotient `g` is sufficient for the first-digit observer under the theorem, but `(q,f)` must be retained if the next operation needs source attribution or higher digits. BRC resolution: `COMPOSE_APPLIED` (signed two-source Gauss lift with derivative observer), not positive-weight BRC collapse.

## Next real scientific action

1. Establish the target-class Hasse zero uniformly by a sourced CM/Cartier or explicit finite-field hypergeometric identity (candidate CM discriminant -8; **not asserted as proved**). Maintain separate A/B Euler branches.
2. Prove `12J_Ag_A=1` and `c_BJ_Bg_B=1` by a common Frobenius/Wronskian normalization. Then lift the same source-preserving ports through order `p^3` using the previously derived `F_2`, self-composition, and nonzero high-tail boundary; the existing mother theorem is still open.
3. Preserve original-class p373 H0/B0, divided-power, Frobenius, Hesse/Green κ and independent replication as **native** evidence under #1559. The checks here are distinct portable integer arithmetic, not that native experiment.

Original native `target_request_id=onhour11-20261106-1400-exact-research-lane-continuation` retained; last live status query 2026-11-07 UTC 14:31 reports `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE / operation_sent=false`; Site `CONFIGURED_NOT_LIVE_VERIFIED`, no verified Researcher session/claim/run. No new native mutation, review, Result or acceptance is asserted.
