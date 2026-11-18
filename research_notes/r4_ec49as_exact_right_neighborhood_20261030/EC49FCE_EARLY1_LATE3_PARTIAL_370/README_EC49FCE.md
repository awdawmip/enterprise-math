# EC49FCE — Exact four-slot rigidity in 370 early-one/late-three positions

Date: 2026-11-06. Author-side research. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Theorem (finite, fixed-cache schedule)

Take the native signed-X6 nine-state BRC model and the 24-word 158-primitive-prefix witness EC49FBU at immutable `b3b43ef6abe2fd816d979792d18a67ee5d0aad50`. Hold H2/H3 fixed, use L=(4,2,1) for H4/H5, M=(7,3,2) for H6–H9, and preserve the required four observer signatures in their respective windows. Among alternative legal operation words at exactly four chosen H4–H9 signature slots, the minimum number of distinct ordered signed native primitive-prefix edges equals 158 for every slot set in the following disjoint families:

- One of 10 early H4–H6 slots and three of four H7 slots: 10*C(4,3)=**40** groups, complete.
- One early slot, two of four H7 slots and one of two H9 slots: 10*C(4,2)*2=**120** groups, complete.
- One early slot, two H7 slots and one H8 slot: **first 210 of the 240** groups in the deterministic enumeration (early ordered by H4,H5,H6, H7 two-combinations and H8 signature order). All 210 checked; the final 30 remain.

Thus **370 distinct four-slot groups** have exact optimum 158. Together with preceding disjoint four-slot work EC49FBZ/FCA/FCB/FCC/FCD, the coverage is **4,015 / 4,845** position sets. Of the remaining 830, 30 are the last H7/H7/H8 groups and 800 have other late-triple types. This is a local theorem about the declared fixed schedule and observer, not an optimization over alternative schedules.

## Exact exhaustive proof

The frozen candidate generator is `EC49FBY_COMPLETE_TRIPLE_RIGIDITY/VERIFY_EC49FBY.py` at immutable commit `5b10f1c296cb8826d4b69f6fd83dba89d765df1c`. Each legal operation word expands to the complete ordered signed primitive-step list. Let P(w) denote its set of nonempty signed-native primitive prefixes, and let F be the union of P(w) for the 20 unchanged witness paths. For any legal replacement at each of four slots S, the objective is
`| F union P(w1) union P(w2) union P(w3) union P(w4) |`.

Set `c=158-|F|`; each candidate residual `R(w)=P(w)\F` with `|R(w)|>=c` can be discarded for the search for any cost <158. Exact residual deduplication is safe because the objective depends on each replacement only through its set of prefixes beyond F. For each four-slot group, enumerate every residual tuple surviving individual rejection, sorted by pool cardinality. Discard a pair (resp. triple) only when its residual union is already >=c: adding sets cannot decrease cardinality. Compute the fourth union for every remaining tuple; every group gives cost >=158. The unchanged original 24-word witness attains 158 for each group. Therefore each tested group has exact minimum **158**.

The Python implementation uses arbitrary-precision integers as lossless bitsets over **109,972 distinct native signed primitive-prefix strings**, preserving order, signs, multiplicity of candidate paths through their distinct slot assignment, and all window signatures. It enumerates the frozen legal words (16,152 H4–H9 candidates), not generic unrestricted words. BRC positive cache keys and native X6 step provenance are retained.

## Executed calculation

| Group family | Checked | Raw quartets | Pair pruned | Triple pruned | Fourth union checks | Minimum |
|---|---:|---:|---:|---:|---:|---:|
| H7/H7/H7 | 40 | 188,116,992,000 | 88,324 | 256,804 | 131,592 | 158 |
| H7/H7/H9 | 120 | 1,525,837,824,000 | 202,052 | 572,020 | 538,800 | 158 |
| H7/H7/H8 first 210 | 210 | 3,666,321,792,000 | 352,384 | 1,093,949 | 1,909,746 | 158 |
| **Total** | **370** | **5,380,276,608,000** | **642,760** | **1,922,773** | **2,580,138** | **158** |

Local Python 3 exact runs on 2026-11-06 produced exhaustive per-group JSON for all 370 rows. The H7/H7/H8 program was interrupted while processing index 210 (zero-based), after writing/validating indices 0–209; those 210 verified rows, not the uncompleted remaining family, are the claimed result.

Independent signed integer-tuple prefix-union checker reproduced the exact minimum and fourth-union count in nine representative slot sets: H7^3 indices 0,16,32; H7/H7/H9 indices 0,60,100; H7/H7/H8 indices 0,100,200. This independent checker differs in its prefix representation; candidate enumeration is shared from the frozen generator. The compact JSON summary is stored alongside this proof; the adjacent verifier regenerates the complete 370-row certificate.

## Next research

Resume H7/H7/H8 at indices 210–239 using a more efficient prefix-union lower-bound cache or exact pair-union optimization, then handle the remaining 800 early-one/late-three configurations. Search in parallel for 157-edge explicit constructions in five-or-more-slot neighborhoods or different L/M cache schedules. Full global schedule optimization remains separate. The result is `AUTHOR_EXACT_FINITE_CHECK / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`: no current native CLAIM/Source Result or independent Driver decision is asserted.
