# R80 — Exact GCD-period quotient for latest-source circular observers

Author-side mathematical continuation of R79, 2026-11-11. R79 source: `3aff181168131fd82c8fcd4183971f2879a9c27d`. Frozen S23/AV input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34` (unchanged). This is an **auxiliary rational circular-source model**. It is not a native X6/BRC theorem, Task CLAIM, Result, independent Review or Foundation change.

## Domain and observer

Finite distinct identities `E={(t,branch)}`, integer time `t`, integer observer `j`, integer original labels `a,b`, rational constant phase `x`, and rational closed query interval `I=[L,U]`. Set `A(theta)={a theta}`, `B(theta)={b theta}`, `S_e(theta)={x+(t-j)theta}`. The R77 directed half-open circular arc from A to B is `[A,B)` if A<B, `[A,1)∪[0,B)` if A>B, and EMPTY if A=B. The latest-source readout `W(theta)` is the lexicographically maximal qualifying `(t,branch)`, else NONE. Original source identities, multiplicities and branch distinctions remain material for updates.

## Theorem R80-A: exact quotient by common phase period

Define
`g=gcd(|a|,|b|,|t-j| for all (t,branch) in E)`.
If `g>0`, write `a'=a/g`, `b'=b/g`, `s'_e=(t-j)/g` and `y=g theta`. Then identically for every real theta,

`{a theta}={a'y},  {b theta}={b'y},  {x+(t-j)theta}={x+s'_e y}.`

The identity map `(t,branch) ↔ (s'_e,branch)` is injective and preserves lexicographic winner order because `t=j+g s'_e` and g>0. Therefore `W(theta)` is the inverse-image winner of the reduced observer `W'(g theta)`. For any integer k, every reduced affine phase changes by an integer under `y→y+k`, and their fractional parts remain equal. Hence

`W(theta)=W'(g theta)=W'(g theta+k)`, and `W(theta+1/g)=W(theta)`.

Proof: the three displayed fractional identities preserve, pointwise, the ordered original-label arc and every source membership Boolean. The injective order-preserving label map commutes with taking the maximal qualifying identity. Integer translation of y preserves all reduced fractional phases because x is constant and every normalized slope is integer. No continuity argument is needed; this also covers wrap points, coincident boundaries and ties. QED.

## Theorem R80-B: full-interval exact trichotomy in at most one period

For g>0 set `l=gL` and `h=min(gU,l+1)`. If `g(U-L)>=1`, periodicity proves that `[l,l+1]` contains a representative of every reduced phase appearing in `[gL,gU]`; if the width is smaller, `[l,h]` is the complete image. Split `[l,h]` at its integer points; as its width is ≤1, it has at most two nonempty open segments. For each segment, translate by an integer m so that `[u-m,v-m]⊂[0,1]`, then apply any complete exact latest-source interval oracle (e.g. R79; the executed checker uses the R77 six-critical-family oracle) to the **reduced** slopes and unchanged x. Evaluate integer-seam singleton points separately, preserving 0≡1 phase equality. Map every rational witness z in a segment back to `theta=(m+z)/g`, and map normalized source identity `(s'_e,branch)` to `(j+g s'_e,branch)`.

The union of complete segment answers gives exactly one of `STABLE_NONE`, `STABLE(identity)`, or `CHANGES(theta1,theta2)` with two rational witnesses whose original winners differ, for **all real theta in I**. Degeneracies: if a=b the declared arc is empty; if E is empty there is no winner. If g=0 all phase slopes are constant; in this model a=b=0 so the target is empty.

Proof: if the original interval covers at least one period, every normalized phase class occurs in the retained one-period interval; otherwise no part was removed. In every reduced segment the finite complete oracle decides all reals, including half-open boundaries by singleton checks. The inverse rational scaling keeps reconstructed witnesses inside I, preserves original membership by Theorem A and preserves winner ordering. The segments and their seam points partition the retained interval. QED.

## Cost and strict local improvement

GCD reduction costs exact integer arithmetic polynomial in the binary input lengths. In one normalized period, a complete R77 critical-strata oracle enumerates at most
`O(1+|a'|+|b'|+|a'-b'|+Σ_e(|s'_e|+|s'_e-a'|+|s'_e-b'|))`
candidate roots, then sorts and evaluates them. Using R79's complete original-label-cut oracle instead, the root count involves only `a',b',a'-b'`, with at most `O(n(1+|a'|+|b'|+|a'-b'|))` exact source examinations after sorting. In either variant the **numeric magnitude of the common factor g does not appear** in the candidate-count bound; integer bit lengths and rational denominator costs still count. If g=1, this quotient need not yield any reduction.

Infinite family: `j=x=0`, `E={(4g,1)}`, `a=g,b=2g,I=[0,1]`, any positive integer g. The direct original-label cut family `a theta in Z` contains g+1 points; the reduced model `(4,1,2)` is constant-size. Explicit exact witnesses `theta_yes=7/(20g)` and `theta_no=1/(4g)` show CHANGES: the source phase at yes is 2/5 inside `[7/20,7/10)`, while at no it is 0 outside `[1/4,1/2)`. This proves a strict local input-family improvement, not a universal complexity breakthrough.

## Executed exact validation

Full executed local `check_r80.py`, fixed seed 80261111 and Python `Fraction`, compared 260 random finite models to an independent original-interval R77 six-family full-stratum reference: **176,130 exact reference strata** and 1,300 additional direct periodicity point checks, all passed. Outcomes: 70 STABLE_NONE, 2 STABLE, 188 CHANGES; each generated change witness was verified by direct original-model winner evaluation. Family g=1,2,8,32,128,512,1024 required respectively 13,25,97,385,1537,6145,12289 direct full-reference strata, versus 6 reduced point evaluations to exhibit a change, with 7 reduced critical cuts on the evaluated segment. Huge exact factors `g=2^k+3` for k=32,128,512,1024,2048,4096 were also tested; every case returned directly validated changing witnesses. The full local checker and complete large-number witness data remain in the supplied R80 research bundle; `check_r80_min.py` is a separately executed smaller GitHub reproduction.

The all-real claim follows from the two exact proofs and the complete suboracle, not from random sampling. No native BRC transfer or independent semantic review is asserted.

## R81 continuation

Attach the gcd quotient to R76 persistent winner-index versions while preserving original identity provenance; study how a branch insert/delete changes g and cache validity, and compare R75 heap versus R76 maintained maximum with matched full integer-bit and allocated-node costs. Explore piecewise-affine observer phase x(theta) and exact seam semantics without assuming a single period across slope changes.
