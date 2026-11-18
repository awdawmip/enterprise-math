# EC49FCN — Complete 720-group early3 + H7pair finite minimum

## Statement

Scientific input frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Preserve the original nine-state observer `T`, 24 signed primitive-step witness paths, path order, observer signatures and full cache keys L=(4,2,1), M=(7,3,2). H2/H3 witness paths remain fixed. Among ten H4–H6 observed slots choose exactly three; among four H7 slots choose exactly two. For each of the C(10,3) C(4,2)=720 five-slot subsets, replace all five paths with *any* legal frozen-model candidate preserving each original slot's signature and cache key; the remaining nineteen paths stay fixed.

**The exact minimal number of distinct nonempty signed, ordered, primitive-step prefixes is 158 for every one of the 720 subsets.**

## Exact finite certificate argument

For selected slot set U, let F_U be the union of nineteen fixed paths' ordered signed prefix sets. For each replaced slot i and candidate path w, define R_i(w)=prefixes(w) minus F_U. Then total cost equals |F_U|+|union_i R_i(w_i)|. The fixed original 158-edge witness provides an admissible upper bound in each family. Put b=158-|F_U|.

To rule out a strict improvement, keep only candidate residuals of size <b and dynamic-program their unions. After every newly selected slot, discard unions of size >=b. If A is included in B, then for every later residual T, A union T is included in B union T. Therefore an inclusion-minimal antichain retains the existence or nonexistence of a strictly better completion *exactly*; no statistical sampling or approximate arithmetic is used. Start with {empty set}, add all legal residuals for each of the five slots, and prune to the inclusion-minimal antichain each time.

In the executed literal-prefix-set solver all 720 groups, indices 0 through 719, have empty final strict-improvement antichains. Consequently every allowed substitution has cost >=158; since the frozen construction attains 158, its optimum is exactly 158. The largest intermediate antichain has 2,196 states; the nineteen fixed-word costs range from 115 to 149. The total Cartesian candidate count, before lossless pruning, is 1,869,832,512,000 across the 720 groups.

## Executed checks and reproducibility

The source-controlled verifier `VERIFY_EC49FCN.py` and `frozen_model.py` reproduce all 720 groups in Python 3 standard library. The verifier's mathematical operations match the executed local script `VERIFY_EC49FCN_PUBLISHED.py`; execution was split into the three exact ranges 0–119, 120–239, and 240–719, and its 720 per-group results, fixed counts and all intermediate antichain cardinalities were compared to a second locally executed literal-source implementation. An independently represented integer-bitset dynamic program was executed on groups 0–77 and 90–119 (108 distinct groups); fixed-word counts and exact minima match. These methods share the frozen observer and candidate-generation semantics, so crosschecks cover optimization representation rather than independent physical/model interpretation.

Reproduce by running `python VERIFY_EC49FCN.py --start 0 --stop 720 --output EC49FCN_RECOMPUTED.json` alongside the frozen model. The generated JSON contains each group, fixed-prefix count, stage cardinalities and exact minimum. Local raw 720-group certificate SHA-256: `106dad58a04b6d857f928fa561e6ace849d72e30c7c6e3554bd578ea2dda9231`. The complete raw execution and independent-bitset evidence bundle accompanies the author handoff.

Status: author-side exact finite theorem and reproducible code, not Source-native Result or independent Driver mathematical admission. Current live owner is not confirmed. Extension to larger replacement sets, other five-slot families and changed legal cache keys remains open.

## Next

EC49FCO: exhaust all 720 early3 + H8pair replacements, using antichains and independently represented bitsets for challenging cases. Either return an explicit <=157 legal witness or a full exact 158 certificate. Preserve the full nine-window 93-edge mother objective.
