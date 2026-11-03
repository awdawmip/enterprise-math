# Stage398-B — Exact recursive future quotient for bounded BRC terminal-pair cancellation

Date: 2026-11-03. Proven author-side result, not canonically admitted. Parent: Stage397-B, PR #1736, immutable commit `997e5fb93ee08310e14fce12ee5a7cc6823b1751`. Frozen scientific inputs: Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; GLOBAL science `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current normative rules read separately from main.

## Carrier, observer and future language

Let A be the 12 signed native X6 directions `±E_i`, i=1,...,6. A history w is a finite ordered word over A, with six-component endpoint z=sum(w). Fix a source label, positive rational endpoint BRC step weights p_d, and independent nonzero rational individual trace factors omega_d. Current observation O_J(w) contains the source, length m, complete 20 three-component relative X6 readouts plus the common depth, exact native unweighted full-length BRC endpoint N_m(z), positive weighted full-length endpoint W_m^p(z), signed individual product Omega(w), and the full 12x12 **ordered** adjacent-pair histogram J_w(d,e). The turn count tau is reconstructed from J. Observations include definedness of each operation and every intermediate readout.

Future operations: APPEND(d) for every d in A, and CANCEL deleting the last two labels only if they are an inverse pair (d,-d). Each future uses at most C CANCEL operations, with arbitrary finite APPEND horizon; no separate POP. This is an exact **path-formal** extension of the existing native BRC endpoint kernel; no physical reversal dynamics are asserted.

Define future indistinguishability on any complete current observer fiber F_o: w~_C v iff every allowed common finite operation sequence has identical enabledness and identical intermediate observations (the first mismatched enabledness already distinguishes).

## Theorem 398.1 — a recursively computed *exact* quotient for every C >= 0

For a word w let pred(w) delete its last letter when nonempty. Write inv(w) iff |w|>=2 and the last two letters are mutually inverse. Define nested signatures:
- S_0(w) = last(w), or EMPTY when w is empty.
- For c>=1 and nonempty w,
  S_c(w) = ( S_{c-1}(w), S_{c-1}(pred(w)),
             S_{c-1}(pred(pred(w))) if inv(w), else ABSENT ).
  For the empty word the second and third entries are ABSENT.

**For any C>=0 and w,v in the same complete O_J-fiber, w~_C v iff S_C(w)=S_C(v).** Consequently the exact minimum number of deterministic additional memory symbols in a finite fiber is
`q_C(o) = | { S_C(w): w in F_o } |`,
and the minimum fixed-length binary memory is `ceil(log2 q_C(o))`. This includes C=2; C=1 specializes to Stage397-B's last-two/conditional-last-three kappa. The theorem's quantification covers arbitrary finite APPEND horizons and all twelve directions.

**Proof, sufficiency by induction on c and operation length.** For c=0, last(w) determines every next joint-histogram increment under APPEND(d), while all other observer components update deterministically using the same current observation and appended direction. For c>0, equality of S_c implies equality of S_{c-1}(w), the predecessor signatures and inverse-pair flags. Under APPEND(d), S_{c-1}(w d) is determined by S_{c-1}(w) and d by the induction-on-c append congruence. Also pred(w d)=w and, if inv(w d), pred²(w d)=pred(w), both whose S_{c-1} signatures are stored in S_c(w). Thus APPEND preserves equality of S_c and O_J. If CANCEL is enabled, both terminal pairs are inverse, and its successor is pred²(w); the third component of S_c provides equal S_{c-1} for the two successors. Both successors have equal O_J because deleting the same last two labels and their previous directed edge changes J equally; endpoint, signed individual product and BRC masses update from the same current data. A CANCEL consumes one unit of budget. Iterate on any finite future action sequence.

**Proof, necessity with explicit distinguishing continuations, by induction on c.** If S_{c-1}(w) differs, its induction witness already distinguishes using <=c-1 CANCELs. Otherwise the last labels coincide. If S_{c-1}(pred(w)) differs, APPEND(the inverse of the shared last label), then CANCEL: both become their predecessors and an induction witness distinguishes using <=c CANCELs total. If the predecessor signatures match but the inverse flags differ, then the previous labels differ and are already detected by the preceding cases. In the remaining case a difference in the conditional third entry requires both original final pairs to be inverse. CANCEL immediately, then apply the induction witness to the two twice-shortened histories. The base case c=0 with distinct last letters is distinguished by any APPEND(d), since J gains different directed edges. All cases terminate, so distinct S_C always have a finite witness. QED.

The stored signature depends only on the original last min(m,2C+1) letters. Its shared-subexpression DAG has O((C+1)^2) nodes and can be updated through the above recurrence, rather than materializing all future words; the count of distinct signatures in a given fiber is the exact quotient size, not merely the uniform suffix upper bound. This is a representation bound, not a polynomial-time enumeration of an unbounded fiber.

## Theorem 398.2 — complete eight-step native BRC fiber, 5 -> 3 states

Set n=8, source fixed, and let w_r for r=2,...,7 be the word with one -E1 in position r and +E1 in the other seven positions. They are **exactly** one complete O_J-fiber: length and endpoint force 7 positive and 1 negative E1; support of J forces only E1 directions; J(+,+)=5, J(+,-)=J(-,+)=1 forces the negative to be interior. All 20 triple readouts, common depth, source, signed Omega and positive BRC endpoint mass therefore match.

For the native full-length twelve-direction BRC kernel, directly by its signed-axis recurrence,
`N_n((n-2)E1) = n + 5n(n-1) = n(5n-4)`, hence `N_8(6E1)=288`.
For weights p_(+E1)=2, p_(-E1)=3, all other ten p_d=1:
`W_n^p((n-2)E1) = 3n2^(n-1) + 5n(n-1)2^(n-2)`, so `W_8=20992`.
These are positive rational BRC endpoint masses; the individual signed Omega is separately fixed by the multiset.

With C=2, the uniform Stage396-B suffix of length 2C+1=5 distinguishes five signatures: one common earlier class and four late positions. The exact S_2 partitions the **whole** fiber into three classes:
`{w_2,w_3,w_4,w_5}`, `{w_6}`, `{w_7}`.
The last is immediately distinguished by enabling CANCEL (inverse final pair). For w_6 versus w_2..w_5, APPEND(-E1), CANCEL exposes an inverse terminal pair only in w_6; a second CANCEL distinguishes. S_2 proves all other words are future-equivalent. Thus **five uniform states (3 bits) compress to exactly three states (2 bits)** without future readout loss.

## Executed evidence, scope and next question

The exact independent Python/Fraction reproduction for this run executed twice and returned byte-identical 1483-byte JSON certificate (SHA256 `99d6f1f7b94611819046a0741f0258a6d49010e13e622b51d8f0d5886b6d24b4`). An independent JS/BigInt checker in this directory re-executed 12-direction native weighted/unweighted BRC recurrences, all 2,040 pairs in identical current-observer fibers over alphabet ±E1,±E2 and lengths 0..6, with all c=0,1,2; it checked 36,660 exact successor congruence or explicit distinguishing-witness cases, max witness length 5. This finite check complements the all-horizon induction. The JS stdout is stored in this directory.

This research result is an author-side mathematical theorem for the stated observer/operations, with native BRC arithmetic for its endpoint checks. It does not change P000, or grant SOURCE CLAIM, Result/Review, physical dynamics, or independent admission. Parent objective: minimal residual-faithful representation for native six-axis histories with future operations. Next Stage399-B: symbolic generation of signatures under an infinite/mutable O_J-fiber, exact counting of quotient classes without enumerating histories, multi-source joint histograms, and concrete cost accounting for maintaining 144 ordered-pair counts.
