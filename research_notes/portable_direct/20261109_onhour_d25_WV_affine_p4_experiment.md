# D25 — a direct fourth-digit W216/V2304 affine-transfer conjecture

2026-11-09 (Asia/Hong_Kong). TASK_RESEARCH; **EXACT_FINITE_EXPERIMENT / NEW_PROJECT_CANDIDATE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.
Frozen Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance).

## Original mathematical objects

For each prime p>3 retain **exactly the frozen complete cutoffs**:
\[
 W_p=\sum_{n=0}^{p-1}(6n+1)\binom{2n}{n}^{2}\binom{3n}{n}/216^n,
 \qquad
 V_p=\sum_{n=0}^{p-1}(8n+1)\binom{4n}{2n}\binom{2n}{n}^{2}/2304^n.
\]
Let `chi_p=(-3/p)` (equivalently `+1` for p=1 mod3, `-1` for p=2 mod3). The current frozen parent objective for p=13,19 mod24 is `W_p-V_p=0 mod p^3`, in the earlier established source crosswalk to `Delta_p-R_p=0 mod p`.

## New candidate: one higher p-adic digit

**Conjecture (not proved):** for every prime p>3,
\[
 \boxed{W_p-2V_p+p\chi_p\equiv0\pmod{p^4}.}\tag{AF4}
\]
This is a *source-preserving signed additive* relation directly between the complete original series, not between Hesse surrogate products. In combination with the published V2304 supercongruence `V_p=chi_p*p mod p^3`, (AF4) would imply `W_p=chi_p*p mod p^3`, hence the target `W_p-V_p=0 mod p^3`, including both frozen classes. This is a **conditional proof route**, not a proof of the conjecture or parent target.

## Actual computation and rigorous finite counterexample

A modular term-recurrence program checked every prime `5<=p<1000` (166 primes) and the 8 further primes `1009,1013,1031,1091,1201,1237,2003,2011`: **174/174 exact (AF4) residues zero**. Every original W and V truncated sum also matched `chi_p*p mod p^3` in this finite sample. An independent original-integer-binomial implementation reproduced *both* sums modulo p^5 for 13 named witness primes, including 13, 19, 373 and 997. No floating-point evaluations.

At p=373, p^3=51,895,117 and p^4=19,356,878,641, direct integers give:
\[
 W_{373}=11,832,087,049,quad V_{373}=5,916,043,711\pmod{p^4};
\]
thus **`W_373=2*V_373-373 mod p^4`**. Moreover
\[
 (W_{373}-V_{373})/373^3=114\pmod{373},
\]
and
\[
 (W_{373}-2V_{373}+373)/373^4=174\pmod{373}.
\]
Therefore the stronger universal statement `W_p=V_p mod p^4` is **rigorously false**, witnessed already at p=13:
\[
 W_{13}=19786,quad V_{13}=24180\pmod{13^4=28561},
 \quad (W_{13}-V_{13})/13^3=11\pmod{13}.
\]
The relation (AF4), if proved, would itself have optimal general p-adic order 4, since p=13 and 373 exhibit nonzero fifth-digit defects. These are exact **finite counterexamples**, independent of whether the all-prime (AF4) conjecture is eventually proved.

## Reproduction and limits

The independent recurrence rests on *exact rational identities* for coefficients A_n and C_n:
\[
 A_{n+1}/A_n=
 \frac{(2n+1)(2n+2)(3n+1)(3n+2)(3n+3)}{216(n+1)^5},
\quad
 C_{n+1}/C_n=
 \frac{\prod_{a=1}^{4}(4n+a)}{2304(n+1)^4}.
\]
For `0<=n<p-1`, all denominators are p-adic units. Thus the executable calculation in `Z/p^5` computes the **original truncated rational sums**, not a surrogate. Direct binomial summation is a separate arithmetic implementation. Exact finite coverage proves (AF4) only for the enumerated 174 primes, not for all primes.

Program: `research_notes/portable_direct/d25_WV_p4_affine_transfer_20261109.py`.
Compact finite certificates: `research_notes/portable_direct/d25_WV_p4_affine_compact_results_20261109.json`. Their p^4 quotient column records the fifth-digit defect; a nonzero entry is **expected and not a (AF4) failure**. The first 166 primes are exhaustive only below 1000.

## Research significance and next exact action

Earlier graded calculations at p=373 gave the nonzero 3-source cancellation `190+290+266=0 mod373`. The new exact full-sum experiment finds the sharper relation `W-2V+chi*p=0 mod p^4` on a much broader sample; this points to a *combined signed transformation*, not grade-by-grade cancellation. Next: formulate a candidate hypergeometric/Fricke or creative-telescoping identity whose **complete original p-1 truncation** yields (AF4); start by testing its p^3 coefficient at p=13 and 373 and the existing BRC four-boundary first jet, then attempt proof for the two frozen classes. Reuse old grade and first-jet certificates rather than recount them.

**Native parallel frontier unchanged:** #1559 remains an open capability intake without verified executor. It still needs the fixed original-class H0/B0 divided-power `[X]U mod139129`, native rank, semilinear orientation/eta, signed Green/Hesse κ, `Delta-R`, independent reproducer. The p-adic AF4 experiment is portable science, not that native run. Historical session `MCP-ecbfd1c046864bb3bff1a2e04c87d207` / `EM-ENTERPRISE-4DEB43` has a successful *historical* registration receipt; this turn's `recovery_status` returned `SESSION_CAPABILITY_REQUIRED`. No winning CLAIM, run, formal Source checkpoint or review was asserted.
