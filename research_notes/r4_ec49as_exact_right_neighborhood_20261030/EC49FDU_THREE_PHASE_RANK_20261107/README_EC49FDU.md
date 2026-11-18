# EC49FDU — Rank-nine three-key temporal gluing and three-phase compression

Date: 2026-11-07. Role: TASK_RESEARCH, author-side finite theorem; independent Source Driver review pending. Parent EC49FDT: `7ca6e255a07f27b26971d9918f520c9851d35de3`. Immutable science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. P000 and ACTIVE worldview unchanged.

## Claim and scope

For the exact signed-X6 operators, nine-state observer, six allowed observer signatures and four rank-nine clauses `(18,20,33,40)` of EC49FDT, there are 155 late positive complete BRC keys and 6734 triples that attain rank nine at all H4–H9 but no member pair does so globally.

**New theorem (finite, exact).** In **6730 of those 6734 triples**, every H4–H9 horizon has at least one **single** key from the triple that independently supplies rank nine. There exists a schedule comprising exactly **three contiguous nonempty horizon blocks**, one key per block, with exactly two key switches, using all three keys. There are **14628** such valid ordered three-block schedules across the 6730 triples (counting all legal orders and two switch positions); per triple the count is 1, 2, 3, 4 or 6, with multiplicities 2000, 2982, 792, 724 and 232 respectively.

Exactly **four** triples require **two keys simultaneously at H4**, while H5–H9 are each independently supported by the third key `(6,4,1)`:

- `[(2,3,1),(5,0,1),(6,4,1)]`
- `[(2,3,1),(5,0,2),(6,4,1)]`
- `[(4,1,2),(5,0,1),(6,4,1)]`
- `[(4,1,2),(5,0,2),(6,4,1)]`

For those four triples, the H4 signature masks are exactly `(32,16,0)` in listed key order; `32|16=48` hits all four clauses. Neither of the first two keys is individually rank-nine at any H4–H9 horizon; the third is individually rank-nine at H5–H9. **For every one of the 6734 triples and every horizon, some pair of keys attains rank nine**, so all three are needed only as a *cross-horizon compatibility* phenomenon, never simultaneously within a single horizon.

## Proof outline

The program exhaustively forms all positive-complete-key signature masks by an integer dynamic program on six operation counts and nine DFA states (no floating point), matching the parent counts at H2–H9. For a signature union mask `m`, rank nine is equivalent in this fixed observer model to `all(m & c for c in (18,20,33,40))`. All `C(155,3)=608685` triples are examined, reproducing parent counts `23728` fully rank-feasible triples, `16994` containing a globally feasible pair and `6734` genuine three-key triples.

Across all 155 keys, exact enumeration finds that the horizons at which an individual key supplies rank nine form an interval (possibly empty). Interval-length counts for lengths `0,1,2,3,4,5` are `36,38,47,24,9,1`, respectively. Of the 6734 triples, 6730 cover all six horizons with the union of their three singleton-rank intervals; the above four are the complete exceptions.

**Interval-cover lemma.** If three intervals on a finite ordered horizon chain cover it, but no two cover it, then there exists a three-block schedule with each block covered by one interval, with exactly two switches. Greedily choose an interval covering the leftmost uncovered horizon and extending farthest right. It covers the chain in at most three choices. No two suffice, hence the greedy cover uses exactly three. Blocks are consecutive from each leftmost uncovered horizon to its chosen interval endpoint; intersections do not affect rank feasibility. This yields the three-block result from the exact interval and coverage census. A separate 60-schedule enumeration per triple proves the 14628 count and emits canonical explicit schedules.

## Verification and limits

Run `python EC49FDU_THREE_PHASE_RANK.py` (standard library), generating `EC49FDU_THREE_PHASE_RANK_RESULT.json` plus `EC49FDU_THREE_PHASE_RANK_CERTIFICATE.json` with a rank-supporting schedule for all 6734 triples. Then run `python VERIFY_EC49FDU.py`: all 6734 certificates were checked, with 6730 schedules having exactly two switches and the four H4 exceptions verified separately. Full certificate SHA-256 from actual local execution: `0ae07590f794d4c6a797ee2e8eedd21d0a8ab54de822a8cbc6ecc1650887ad83`. All integer counts are exactly reproducible.

This theorem classifies **observer-rank support**, not path multiplicity/quota constraints, detailed native-word existence with those quotas, H2–H3 alignment, full five-key usage, or the globally shared signed-primitive-prefix cost. These remain part of the original **≤93-edge** objective, with the known legal 94-edge family as a current comparison. The 6730 simple phase schedules are an effective search-entry family; intra-window mixing and alternative early seeds remain legitimate for optimizing the full problem.

## Next EC49FDV

Use the 6730 certified three-phase schedules to select promising ordered key/switch pairs and jointly optimize H2–H9 path choices and signed-prefix sharing with quotas; route the four H4-mixed exceptions separately. Preserve the original frozen pin, original exact observer and native-X6 semantics, and report exact 93-edge witnesses or exact scoped lower bounds, whichever the next bounded search establishes. Source-native Owner/CLAIM/Result cannot be established when the backend status database is unavailable; retain this as author-side repository evidence pending native intake and independent Driver review.
