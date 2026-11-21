# PREFIX-982 — Branching signed-source fiber law and a sharp 13-step finite triple

2026-11-21 · Research6 · AUTHOR_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED.

Predecessor: `enterprise-math@b5a6cc19c0bc9c90f105efddef477ebb61048a87:research_notes/portable_direct/2026-11-21_r6_prefix981_singleton_periodic_extinction.md`.
Frozen scientific input: `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json` (P000 V5), unchanged. The ACTIVE worldview and joint-relation preservation rules apply. This is an auxiliary signed-source XOR observer; no typed embedding into native X6 or triadic closure is asserted.

## Exact setting

Fix integer `p>=3`. Distinct named sources are triples `(i,j,s)` satisfying `a=2^i-s*2^j` with `0<=i,j<p`, `s in {+1,-1}`. Restrict parity-preserving feedback to `j>=1` and odd states `x mod 2^p`. A source is enabled precisely when bit `j` of `x` is 0 for positive `s` or 1 for negative `s`; the update is `x -> x XOR 2^j`. Let `B_a(j)` be the set of eligible bit values at a port. For fixed `(a,j,bit)`, the signed source is unique, since `2^i=a+s*2^j` uniquely determines `i`.

The residual word `w=(a_0,...,a_(L-1))` repeats in the specified phase order. Its phase is only an auxiliary schedule index.

## Theorem 982.1 — full branching signed-fiber formula

For a selected port skeleton `J=(j_0,...,j_(n-1))`, let `m_j(t)=#{u<t:j_u=j}`, and define

`I_j(J) = intersection_{t:j_t=j} {b XOR (m_j(t) mod 2):b in B_(a_(t mod L))(j)}`.

An empty intersection is `{0,1}`. The number of odd initial states supporting this complete *named* skeleton is

`N(J;p,w)=product_(j=1 to p-1) |I_j(J)|`.

Summing over permitted port skeletons yields the exact integer history count

`N_n(p,w)=sum_(j_t in T_(a_(t mod L))) product_(j=1 to p-1) |I_j(J)|`. (982.1)

At `n=0`, this is `2^(p-1)`.

**Proof.** Before transition `t\), the current bit at port `j` equals its initial bit XOR the parity of earlier uses of `j`. Source eligibility is exactly the stated condition on that initial bit. Intersecting these requirements over uses of the same port gives `I_j`. Independent initial coordinates multiply, with bit zero fixed to one. For every selected port and initial bit, the source sign and exponent are uniquely determined, so no source multiplicity is lost. Summation over distinct port sequences completes the proof.

**Nonnegative weighted-source variant.** For step/port/current-bit weights `lambda_(t,j,b)>=0`, replace the factor `|I_j|` by
`sum_(b0 in {0,1}) product_(t:j_t=j) [b_t in B_(phase_t)(j)] lambda_(t,j,b_t)`,
where `b_t=b0 XOR (m_j(t) mod 2)`. This is an exact positive-branch path-mass formula when the weights factor over the declared step sources. Path kernels that couple ports, or signed/complex amplitude cancellation, need an explicit joint carrier and are outside this factorization.

## Theorem 982.2 — exact 13-step termination at all p>=5

For every `p>=5`, take the **nonzero branching** residual word `w=(12,4,20)`. Every odd-state signed-source history following this repeated word ends after at most 13 legal transitions, and the upper bound is attained.

For `0<=n<=14`, the exact number of named initial-state/path pairs is

`N_n(p,w)=2^(p-5) * A_n`, with

`(A_0,...,A_14)=(16,24,24,30,40,28,30,36,18,18,20,6,6,6,0)`. (982.2)

At `p=19` there are exactly **98,304** length-13 named histories, and **zero** length-14 histories. Length-6 histories exist, so survival through two complete periods of this three-letter word no longer implies an infinite history once branching is admitted.

**Proof and exact finite certificate.** The complete nonzero-port signed-source dictionary for the three residuals is:

| Residual | Sources `(i,j,s)` and required input bit |
|---|---|
| `12` | `(4,2,+1):0`, `(3,2,-1):1`, `(2,3,-1):1` |
| `4` | `(1,1,-1):1`, `(3,2,+1):0` |
| `20` | `(4,2,-1):1`, `(2,4,-1):1` |

All sources are stable for `p>=5`, and only ports 1,2,3,4 occur. The other `p-5` free input bits neither influence legality nor change, giving the stated factor `2^(p-5)`. The reduced odd five-bit space has only 16 states. Let the initial integer path mass be one at each odd five-bit state, and propagate it through every legal named source in the repeating order, summing masses only on identical full five-bit successor states. Iterating this exact integer recurrence for 14 steps gives the sequence (982.2), with `A_14=0`; this exhausts **all** initial states and branches, hence proves the upper bound at every bitwidth.

Independently, the longest legal future lengths from initial odd states `x=1,3,...,31` at phase zero are respectively

`(1,4,4,7,4,7,7,10,1,7,7,10,7,10,10,13)`.

An attaining 13-step path begins at `x=31` and uses ports

`(2,2,4,2,2,2,3,2,2,2,1,2,2)`,

with successive states

`(31,27,31,15,11,15,11,3,7,3,7,5,1,5)`.

Every transition has a source in the displayed dictionary and the prescribed phase. The finite recurrence, complete source table, and maximal witness yield an independently inspectable finite proof. QED.

## Verification and limits

The accompanying `PREFIX982_R6_BRANCHING_SIGNED_PORT_CHECK.py` computes direct named-source XOR-state integer DP independently of the port-fiber formula (982.1). Both agree in **41,871** test aggregates: all three-phase words over residuals with at least one nonzero source port at `p=3,4`, for `n=0..6`, plus seeded `p=5` (400 cases) and `p=6` (80 cases), with `n=0..8`. The reduced 16-state and free-coordinate 19-bit counts agree for every `n=0..14`. See adjacent `PREFIX982_R6_EXACT_RESULTS.json`.

A separate exploratory exhaustive three-phase **nonzero residual** graph census for `p=3..7` found maximal finite path lengths `6,11,13,13,13`; the tentative all-bitwidth bound of 13 is an **open conjecture**, not asserted as a theorem. The theorem above concerns the fixed word `(12,4,20)` for all `p>=5`. The signed-source observer's mapping to native BRC/X6 remains open. Mother question `B_fix,odd(32) in {19,20}` remains open.

## Provenance and next question

Historical Researcher `EM-DIRECT-FBEA5D`, Activity `RA-3FB2D033BE6048D8712FF056`; no new CLAIM, PROGRESS, reviewer acceptance or P000 update. Publication and Activity association are separate, and any Activity update must pass its own Source CAS and observation requirements.

Next: decide whether every nonzero-residual three-stage word has a phase-aligned 6-step loop or terminates in at most 13 steps, by a proof from power-of-two source incidence or an exact higher-p counterexample. Then connect a correctly typed source/phase carrier to native Cell/Link/Port and TRIADIC_CLOSURE_E, preserving the joint signed-source relation.
