# EC49FCS — exact 256-group H4/H5 + H7/H8/H9 signed-prefix rigidity

2026-11-06. Author-side finite exhaustive theorem; independent Driver review and Source-native Result are pending.

## Fixed mathematical input and problem

Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Preserve the 24 distinct witness slots, the nine-state observer, signed ordered primitive-step expansion, and cache key multisets `L=(4,2,1)` for H2–H5 and `M=(7,3,2)` for H6–H9. The machine-defining transition table, signatures, permitted word multiset enumeration, and original 24-slot words are in `frozen_model.py` (same exact byte content as the executed local model Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`). The original witness has 158 distinct nonempty ordered signed primitive-step prefixes.

Select exactly one slot of H4 (four observer signatures), one of H5 (two), one of H7 (four), one of H8 (four), and one of H9 (two). Keep the other 19 witness slots fixed. Each selected slot may be replaced by *any* word in the frozen generator's complete allowed pool for the same signature/key multiset.

**Finite theorem.** Every one of the `4*2*4*4*2=256` slot groups has exact optimum **158 distinct signed ordered primitive prefixes**. No five-word replacement in these specific finite candidate pools gives 157 or fewer prefixes.

## Proof and executable certificate construction

For a selected group `S`, let `P(w)` be the set of nonempty signed primitive-step prefixes of `w`, and let `F = union(P(w): w belongs to one of 19 fixed slots)`. For each variable slot `i`, its residual option is `R_i(w)=P(w) \ F`. Let `c=158-|F|`. Any strict improvement exists precisely when some legal choice has `|R_1(w_1) union ... union R_5(w_5)| < c`. The retained witness itself gives an upper bound of 158.

Generate all candidate words with the frozen integer multiset and finite observer transition table. For each slot, retain only inclusion-minimal residual options with size `<c`: if `A subset B`, replacing B by A does not increase the union with any later choice. For the suffix starting after stage `i`, let `I_j` be the intersection of the remaining slot `j`'s inclusion-minimal options, and put `M_i=union(I_j: j>i)`. Every completion using these reduced options contains `M_i`, so a partial residual union `A` with `|A union M_i| >= c` cannot improve the witness and may be discarded. Continue antichain union DP in H4,H5,H7,H8,H9 order. Union and cardinality are exact integer-bitset operations.

The executed program `VERIFY_EC49FCS_EARLY2_H7H8H9.py` performs this exhaustive recurrence for all 256 groups, with `--early4h5 --start 0 --stop 256 --literal 256`. An independent *literal string-prefix frozenset* recurrence, without the suffix lower-bound pruning, agrees group-by-group on fixed counts, thresholds, all five stage-antichain sizes, and absence of strict improvements. Thus all final antichains are empty. The 158-edge witness supplies equality.

## Actual calculation and checks

- 256/256 distinct groups, all optimum 158; independently literal-crosschecked 256/256.
- Total unpruned word-tuple Cartesian products (not actual enumerated tuples): `98,322,481,152,000`.
- Actual tested partial union pairs in bitset recurrence: `456,672`.
- Maximum stored stage antichain: `32`.
- Executed local model generated 16,156 distinct words and 109,972 distinct signed prefixes; 24-slot witness union asserted exactly 158.
- The full 256-row uncompressed JSON SHA-256 is `a602174fda207c69dc45abe8db4020e8dceb451c2e3f31f338705a2778851c26` (65,111 bytes). It is supplied losslessly as `EC49FCS_ALL256.json.gz.b64` (base64(gzip(UTF-8 JSON))). The program source SHA-256 is `687895e8b3c9a13baee8727a51af53b11d8d71d320198d27b95369f66a8c0d8a`.
- The final full run returned wall time 21.49 seconds in this local execution environment; this is a provenance observation, not an asymptotic-performance claim.

To reproduce with Python 3.10+ in this directory: `python VERIFY_EC49FCS_EARLY2_H7H8H9.py --early4h5 --start 0 --stop 256 --literal 256 --output CHECK.json`; compare SHA-256 with the value above. Decode the stored certificate by standard base64+gzip; verify the decoded JSON digest and all 256 rows. No floating-point arithmetic enters the mathematical test; timing uses a monotonic clock for logging only.

## Status and next work

This theorem extends the distinct earlier H7-triple early-two subfamily (EC49FCQ/R, 180 groups) to the mixed late triplet class H7+H8+H9 in the precise H4/H5 early-pair slice (256 new groups). Previous reported disjoint five-path coverage was 7,932; with these 256 distinct groups the reported total becomes 8,188, subject to the previously published certificate ledger. The full 1,440-group early-two plus H7/H8/H9 family still contains 1,184 cases outside this H4/H5 slice.

Scientific source pins remain distinct from current rules: Global Knowledge canonical main `031f4413719ac124984919acec0a55a3b7ac61d2`, Enterprise Math main `ed6e5d3c30c81ee18eb8b115d8294bc73274cdc7`, frozen science pin above. P000 and ACTIVE worldview unchanged. This is an auxiliary finite local-exchange result, not the nine-window 93-edge mother target or global native X6 optimum. The independent Driver mathematical review and Source-native CLAIM/Result remain pending. Next exact scoped action: `NEXT_EC49FCT.md`.
