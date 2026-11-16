# PREFIX-840 — One-frame exact recovery of named source assignments from a tagged one-deletion BRC channel

Date: 2026-11-16. Status: AUTHOR_PROVED / EXACT_BIGINT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Scope and provenance

Scientific-input pin: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\` (unchanged). Predecessor: PREFIX-839 at \`b2e5888d1730114497caf5f10cfb086d80162751:research_notes/portable_direct/2026-11-16_r6_prefix839_two_adjacent_Q_histograms_reconstruct_source_multiset.md\`.

The positive-integer, named-source BRC Q-only auxiliary model is used. Formal iteration index \`t\` is not a native X6 heartbeat duration. Name provenance and positive counting mass are distinct from signed/phase amplitudes; no native Cell/Link/Port permission or physical correspondence is asserted.

## Model and observer

Fix \`p=q>=1\`. Initially all \`p\` distinct unmarked names \`1,...,p\` are present with positive integer removal weights \`w_1,...,w_p\`. One separately marked source is absent, has addition weight \`a>0\` and removal weight \`b>0\`. Occupancy never exceeds \`p\`. Each \`Q=R+A\` step sums all legal removal alternatives (weight \`w_j\` for present unmarked name \`j\`, weight \`b\` for the marked source) and any legal addition of the absent marked source (weight \`a\`). All histories have their weighted masses summed only at observation.

For \`t>=1\`, put \`c_t = a^floor(t/2) b^floor((t-1)/2)\`. Define \`G(t)\` as the weighted mass of histories whose terminal state contains **exactly p-1 unmarked names**, and whose marked bit is 0 for odd t or 1 for even t. Its occupancy is p-1 (odd t) or p (even t). Define \`G_i(t)\` as the mass in the same channel for which name i remains present. These are joint/tagged observations of the same Q evolution, not a changed transition law.

## Theorem 840.1 — Exact one-frame labeled inverse

For every p>=1, arbitrary positive integer w_i,a,b and t>=1,

\`\`\`
G(t)   = c_t * (w_1 + ... + w_p),
G_i(t) = c_t * (sum_{j!=i} w_j),
c_t    = a^floor(t/2) * b^floor((t-1)/2) > 0.
\`\`\`

A single global scalar G(t), and p-1 named survival scalars G_i(t) for any fixed p-1 names, determine every named weight exactly:

\`\`\`
w_i = (G(t)-G_i(t)) / c_t              (for observed names i),
w_j = G(t)/c_t - sum_{i observed} w_i  (last unobserved name j).
\`\`\`

Each division is exactly integral; for p=1 the global scalar alone suffices.

**Proof.** Every terminal state counted by G has exactly one initially present unmarked name j missing; no operation ever adds an unmarked name. The initial state is full, with the marked source absent, hence the first step must remove j, contributing w_j. Any later removal of a different unmarked name would irreversibly exceed one missing name, so every later removal must remove the marked source. The unique remaining admissible sequence is therefore alternating marked addition (factor a) and marked removal (factor b), ending with the specified parity bit. For each j there is exactly one history in this channel, of mass c_t w_j. Summing over all j proves G; restricting to j!=i proves G_i. Subtraction yields the inverse. QED.

## Theorem 840.2 — Exact worst-case labeled-probe lower bound

In the measurement family consisting of any/all untagged Q occupancy histograms, G(t), and individually requested **one-name-at-a-time** tagged survival probes G_i(t) at fixed t>=1, **p-1 tagged probes are necessary and sufficient** to reconstruct every labeled assignment uniformly over pairwise-distinct positive integer source weights, for p>=2. This also holds for adaptive name selection.

**Proof.** Sufficiency is Theorem 840.1. With at most p-2 distinct queried names, two unqueried names u,v remain. Swap their different weights. Untagged Q counts at every time remain equal by the symmetric permutation invariance established in PREFIX-839; G stays the same, and each previously queried name i retains its original w_i and thus the same G_i=c_t(e_1-w_i). Hence the same adaptive query transcript can arise from two different named assignments. At least p-1 names must be probed in the worst case. QED.

Minimality is scoped to **the stated one-name-per-query interface**. A coded joint readout with more information per scalar has another resource analysis. Repeated source weights may reduce actual probe requirements.

## Connection with provenance-fidelity and PREFIX-839

PREFIX-839 recovers the unordered multiset from two adjacent late occupancy histograms but exhibits a label-permutation fiber. PREFIX-840 introduces a precisely typed one-deletion provenance observer and gives a one-time inverse. It does not alter Q itself. The named field should only be discarded when the declared downstream observer and its future operations are invariant under name permutations; the current count-only quotient is not a certificate for arbitrary name/port-specific updates.

The raw observation is the **unnormalized positive weighted mass of all histories**, not a sample trajectory. For large t, c_t and the emitted integers grow; no bit-complexity or speedup result is asserted here.

## Independently implemented finite check

The accompanying Node.js BigInt program enumerates every named unmarked subset and marked bit, and applies the Q operation by direct legal-state transitions. For each configuration it checks all G and G_i formulas, integral divisions and complete named-weight recovery.

Complete finite domain: p=1..5; **all ordered assignments** w in {1,2,3}^p; a,b independently in {1,2,3}; t=1..9. This is 3267 configurations, 29403 time frames, 162324 scalar formula assertions, 132921 exact reconstruction assertions. Result: ALL_EXACT_ASSERTIONS_PASSED.

Example: p=3, w=(1,2,3), a=2, b=3, t=6 gives c_t=72, G=432 and (G_1,G_2,G_3)=(360,288,216); these values recover (1,2,3). The general theorem relies on the combinatorial proof; the regression separately checks the independent named-state implementation in its enumerated finite domain.

## Next discriminating units

1. Analyze a jointly coded name observer with fewer separate fields, including full integer bit costs of encoding, reading and recovery.
2. Seek an actual source/target-admitted Cell/Link/Port event observer that realizes the tagged one-deletion readout with permitted source provenance; establish the native-to-BRC map before any transfer.
3. Compare bit costs with PREFIX-839 late two-frame symmetric recovery and retain the open q>=5 nonnegative Q carrier and uniform even-time recollision bounds.

Activity/CLAIM status: independent auxiliary research material; no shared task CLAIM/Result/Review is asserted. Scientific proof and admission remain separate.
