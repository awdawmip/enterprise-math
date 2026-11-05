# EC49FCC — Exact 158-edge rigidity for all 720 H7+H8 four-slot exchanges

Date: 2026-11-06 (Asia/Shanghai). Status: author-side finite computer-assisted theorem, not independently admitted.

Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Research parent: EC49FCB at `242a8dc7caf9dfa8e601cd56bf6cb574566eecd2`.
Frozen 158-edge witness: EC49FBU at `b3b43ef6abe2fd816d979792d18a67ee5d0aad50`.
Generator and full native-prefix model: EC49FBY at `5b10f1c296cb8826d4b69f6fd83dba89d765df1c`.

## Theorem

Keep the 24 frozen words, corresponding to four immutable H2/H3 roots and twenty distinct required observation-signature slots at H4–H9, with exact positive BRC cache keys L=(4,2,1,0,0,0) at H4/H5 and M=(7,3,2,0,0,0) at H6–H9. Retain the nine-state observer and complete ordered signed-X6 native primitive step expansions.

Fix any **two distinct early slots** among the ten H4–H6 slots, **one H7 slot** among four, and **one H8 slot** among four. The other 20 words stay fixed. Each of the four chosen slots may independently take any legal operation word of its **original horizon, complete BRC cache key and terminal observer signature**. For every one of the C(10,2)·4·4 = **720** slot sets, the minimum number of distinct *nonempty ordered native signed-primitive prefixes* is exactly **158**.

The original 158-edge witness attains the minimum for all 720 sets. Full finite exhaustion with exact prefix-set monotonic pruning excludes every strict improvement.

## Proof method / exhaustiveness

For a slot set I let R be the union of all native primitive prefixes from the 20 unchanged words. For each candidate word w let B(w) be its nonempty native signed-step prefix set and D(w)=B(w)\\R. The target strict improvement is exactly
`|D(w1) ∪ D(w2) ∪ D(w3) ∪ D(w4)| < 158-|R|`.
The candidate generator exhausts all operation multiplicity solutions compatible with frozen positive BRC keys and nine-state transition DFA, then separates them by signature. The native primitive encoding uses signs, order and all six axes (the particular witness lives in an X6 subfamily); it never identifies paths by endpoint alone.

Discard a candidate if `|D(w)| >= 158-|R|`. Collapse identical residual sets within each slot. Sort the four candidate pools by remaining size. Reject a pair when `|D(w1) ∪ D(w2)| >= 158-|R|`, and a triple by the analogous inequality. These prunings are mathematically exact because adding further sets only enlarges their union. Enumerate every remaining fourth-set union using unbounded Python integer bitsets representing globally unique primitive prefixes. Each considered fourth union has cost at least 158, and the witness gives equality. This proves the finite proposition for all 720 groups.

## Actually executed enumeration

The 720 groups were processed as eight disjoint, contiguous 96-group chunks (final chunk 48). Each run regenerated the 16,156 distinct baseline and candidate words and 109,972 distinct primitive prefixes. Every group attained 158. A separate audit merged eight local per-group reports, checked 720 distinct groups and all 720 optimum entries, and produced the aggregates below.

| Early slot pair | Groups | Raw four-word combinations | Actual fourth-union evaluations |
| --- | ---: | ---: | ---: |
| H4 + H4 | 96 | 21,946,982,400 | 52,824 |
| H4 + H5 | 128 | 29,262,643,200 | 4,736 |
| H4 + H6 | 256 | 146,313,216,000 | 3,737,268 |
| H5 + H5 | 16 | 3,657,830,400 | 52 |
| H5 + H6 | 128 | 73,156,608,000 | 233,856 |
| H6 + H6 | 96 | 137,168,640,000 | 1,366,848 |
| **Total** | **720** | **411,505,920,000** | **5,395,584** |

After individual strict-improvement filtering and identical-residual collapse, the product of all four residual pool sizes, summed over groups, was 48,517,505,776. Exact bitset pruning excluded 54,820 candidate pairs and 2,904,388 surviving-prefix triples; 5,395,584 final unions were evaluated. All integer sums were audited against 720 per-group rows.

A separate representation built prefixes as tuples of **signed integers**, rather than as alphabet-encoded bitset IDs, and independently reproduced the exact minimum, fixed-prefix count, and final evaluation count in six selected groups (one for each early-window-pair class). This is a six-group crosscheck, while the primary program exhausts all 720.

Source programs: `VERIFY_EC49FCC.py` and `VERIFY_TUPLE_EC49FCC.py`. Aggregate evidence: `SUMMARY_EC49FCC.json`; the complete per-group report can be regenerated with the provided checker. The original locally generated 720-group report is 283,510 UTF-8 bytes, SHA-256 `2e4e3d2fa1e05c14559aadadd662903d4d7783890da3648d026ff1c8fc68c4c8`.

## Frontier

Earlier EC49FBZ/FCA/FCB prove 2,715 other four-slot sets. This work proves another disjoint 720; the cumulative exact local-optimality scope is therefore **3,435 / C(20,4)=4,845** four-slot sets (~70.9%). The remaining 1,410 sets are 1,200 with one early + three late slots and 210 with four late slots. The larger search over different BRC key schedules and five-or-more simultaneous replacements remains open; seek an explicit 157-or-better construction or a global exact lower bound. The 158 result here is the *fixed-schedule, fixed-slot-neighborhood* theorem.

BRC reuse: frozen full positive cache key, nine-state observer, and ordered signed-native X6 prefix objective preserved; EC49FBS lossless primitive-prefix identity underlies the exact optimization objective. No P000, ACTIVE worldview, canonical task Owner, Result or independent Driver acceptance is changed.
