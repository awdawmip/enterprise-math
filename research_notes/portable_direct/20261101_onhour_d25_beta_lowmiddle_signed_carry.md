# D25 SECOND-DIGIT-LIFT: exact low/middle clipped beta carry; LL is the residual proof obligation

2026-11-01 Asia/Hong_Kong · **TASK_RESEARCH / AUTHOR-SIDE ELEMENTARY THEOREM / EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN**.

Mother: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Ordinary Research logical lane chatgpt-research-onhour-enterprise-math-20260923 (distinct from the maintenance lane). This unit **consumes**, without recredit, the original high/low theorem e5f31baf and the preceding middle/middle moment theorem 3cc0aede.

## One genuinely new first-carry port

For primes p≥13, p≡5 mod8, define a=(5p−1)/8, b=(7p−3)/8, and beta_k=((1/8)_k(3/8)_k)/(9^k(k!)²) in p-local integers. The first coefficient bands are L=[0,a], M=[a+1,b], H=[b+1,p−1] with valuations 0,1,2. Let

\[
\ell_i=\binom ai\binom bi9^{-i}\pmod p
\quad(0\le i\le a), \qquad
s_j=\beta_j/p\pmod p
\quad(a<j\le b).
\]

The previously proved middle seed/recurrence supplies all s_j using only p-unit denominators. Define original-index **suffix moments** (zero beyond M):

\[
U_k=\sum_{\substack{j\in M\\j\ge k}}s_j,\qquad
V_k=\sum_{\substack{j\in M\\j\ge k}}j\,s_j\pmod p.
\]

Denote by T^{LM} **both ordered orientations**, exactly as in the original signed clipped double sum:

\[
T^{LM}_{\beta,p}=
2\sum_{\substack{0\le i\le a,\ a<j\le b\\i+j\ge p}}
(8(i+j)+1)\beta_i\beta_j.
\]

**Theorem (all p≡5 mod8, original signed low/middle first carry).**

\[
\boxed{\quad
T^{LM}_{\beta,p}\equiv p\,C^{LM}_p\pmod{p^2}, \qquad
C^{LM}_p=
2\sum_{i=p-b}^{a}\ell_i\bigl((8i+1)U_{p-i}+8V_{p-i}\bigr)
\pmod p.\quad}
\]

**Proof.** The clipping condition for j≤b forces i≥p−b, and for a fixed low i requires middle j≥p−i. Middle beta_j=p s_j (modp²), low beta_i=ell_i (modp). After division by p, the original signed weight splits into (8i+1)+8j; the sum of these two moments over the eligible middle suffix is precisely the displayed bracket. Count the opposite orientation once again, yielding the factor 2. Since every denominator in ell_i and the s_j recurrence is a unit modp, the formula is defined for every stated prime. Nothing has been replaced by an unsigned, un-clipped or single-orientation observer. QED.

This is an O(p) suffix-moment evaluation of the **entire valuation-one** LM port; it is not merely another example of the already-completed high/low port.

## Exact remaining obstruction for the p≡13 mod24 target

For p≡13 mod24, reuse the **previously proved mod-p CM selection** G_p≡0 (modp), the original identity B_p=G_p H_p−T_beta, the previous unit property H_p∈Z_(p)^× and the published 2304 theorem B_p≡pχ_(−3)(p) (modp³). The four-port decomposition of the preceding unit then implies:

- LL is itself divisible by p: modulo p, G_pH_p and B_p vanish and every non-LL source has positive valuation.
- The p13 second-digit statement is **equivalent** to the following one remaining signed-low-source statement:

\[
\boxed{\quad
G_p\equiv0\pmod{p^2}
\iff
\frac{T^{LL}_{\beta,p}}p+C^{LM}_p
\equiv-\chi_{-3}(p)\pmod p.
\quad}
\]

The right-hand congruence is **NOT established for every p13 prime**. It is a sharpened, source-preserving proof target; the LL carry still needs a genuine all-prime argument. The already-proved LH and MM ports are order p² and therefore vanish only in the indicated mod-p² test. The original 216-model Δ_p−R_p remains separate and unresolved.

## Exact computation and a necessary non-dropping observation

Executable: research_notes/portable_direct/d25_beta_lowmiddle_signed_carry_20261101.py, importing the immediately preceding reusable arithmetic certificate d25_beta_middle_moment_fourport_20261101.py. Local Python standard-library integer arithmetic completed: **109/109 p≡5 mod8 primes p≤3000**, including **53 p≡13 mod24**. The checker uses the new suffix formula and performs a separate original signed **double-index LM summation** for every p≤700 in scope; for 13,29,37,53,61,109,373 it also compares the LM contribution to the existing independent four-source calculator. All assertions passed.

| p | C_LM=LM/p modp | LL/p modp | (LL+LM)/p modp |
|--:|--:|--:|--:|
| 13 | 3 | 9 | 12 |
| 29 | 0 | 1 | 1 |
| 37 | 6 | 30 | 36 |
| 53 | 12 | 42 | 1 |
| 61 | 0 | 60 | 60 |
| 109 | 36 | 72 | 108 |
| 373 | 203 | 169 | 372 |

In the actual p13 target cases 13,37,109,373, the last column is −1 modulo p, as required by the still-conjectural cancellation; **LM is nonzero in all four** and **cannot be dropped** in a proof or native observer. For p29/53 ordinary non-target class, the sign differs as expected; these finite values are not universal proof.

## BRC, next and native boundary

BRC COMPOSE_APPLIED: retained original ordered pair indices, clipping cut, (0,1) valuations, signed weight, normalizations, operator scope and both source identities. The new suffix projection is proved valid for this one modular scalar observer; it does not permit source erasure before native H0/B0 semilinear Frobenius or derivative operations.

**Next smallest mathematical unit:** prove/refute, for all p≡13 mod24, the remaining LL/p low/low signed carry equation with the **now explicit, already completed C_LM**, then return to the original 216 Δ−R. No more recycling already-completed source terminal seeds.

The original-class p=373 native H0/B0 divided-power [X]U mod139129, rank, actual semilinear Frobenius/eta, signed odd Green/Hesse, κ and independent reproduction remain **NOT_RUN/PENDING_OWNER** under existing issue #1559. Responsible path: an authorized Source Task owner/native evaluator or implementation maintainer; acceptance requires original raw evidence and independent validation. This beta calculation cannot satisfy that benchmark.

Gateway 0.6.11 already read on this turn: Research authority false, executor binding false, subject native-job quota full. Old target_request_id research-onhour-20261031-0205-dispatch-r15 receipt query returned scoped CONTROL_REQUEST_NOT_FOUND, not evidence of global disappearance. No current own winning CLAIM, open run, formal Source checkpoint, freeze or Result admission established; no request replay/maintenance impersonation. Three old staging sources remain independent. P000, ACTIVE worldview, scientific source pin, schedule and notifications unchanged.
