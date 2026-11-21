# X6 native time / Unit237: signed-axis histogram fiber and sharp BRC order repair

Date: 2026-11-21, Asia/Hong_Kong. Task: RS-X6-NATIVE-TIME-DYNAMICS, publication TP2-91D4A7C2F63805BE21A3.
Research lane: chatgpt-research-onhour-enterprise-math-20260923; existing Researcher EM-X6-FB6990; existing SID MCP-082892eb480e45dea6d4b9fcc0491034.
Status: AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. Conditional on the frozen source-possible two-branch Cell microtrace; no physical branch-selection law asserted.

## Frozen source, scope and question

Scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, notably p000_reality_foundation.json, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md, and the existing VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md and VIETE_NATIVE_HALF_TURN_PRINCIPAL_ROOT_BUNDLE_20260905.md.
Consume, without redoing, the author's Unit234-236 two-branch and bidirectional 36-state exact certificates.
P000 supplies signed primitive steps in the X6 Cell torsor; the centered three-axis slice is a genuine affine sub-torsor, not a claim that X6 has only three spatial axes. BRC source directions and their joint observations are retained.
Question: does a physically tempting aggregate -- the *full signed-axis frequency histogram* of primitive events, not merely the final Cell -- retain enough time information to distinguish the two shortest macro-edge paths, their ordered complete histories, and the frozen principal-root eligibility domain?

## Source-possible oriented two-step paths

Use one chosen chart anchor c_* and signed full-X6 coordinate vectors
 a_0=e_1, a_1=e_2, a_2=e_3, a_3=-e_1, a_4=-e_2, a_5=-e_3,
with indices mod 6 and epsilon in {-1,+1}. For a macro-edge r -> r+epsilon put a=a_r, b=a_(r+epsilon).
Both paths have the same ordered shell endpoints and exactly two native signed-axis steps:
 INNER: (a -> 0 -> b), chronological signed steps (-a, +b);
 OUTER: (a -> a+b -> b), chronological signed steps (+b, -a).
All intermediate and endpoint Cell addresses above are relative to c_*; common translations act on the entire chart.

### Theorem A (a sharp histogram collision)

The two microtraces have the identical signed-axis multiset {-a,+b}, identical displacement b-a, elapsed primitive event count two and macro shell endpoints, but different ordered native words. Their signed-axis histogram is exactly the *abelianization* of the primitive step word; abelianization destroys which of these two orderings occurred.

For any W>=1 complete six-edge shell circuits of a fixed sweep chirality, all 2^(6W) independent INNER/OUTER selections have the same signed-axis histogram and ordered even-time shell list. Joining both chiralities yields exactly 2^(6W+1) distinct complete ordered Cell paths, all sharing the same start and finish a_0, event count 12W, and the same full signed histogram:
 H(+e_i)=H(-e_i)=2W for i=1,2,3; H(+/-e_i)=0 for i=4,5,6.

Proof: over a complete six-edge cycle, the multiset of first/second step *without chronological order* is the union of {a_r:r mod6} and {-a_r:r mod6}. Each set is exactly {+e1,-e1,+e2,-e2,+e3,-e3}. Branch order does not enter this count and the sign of the circuit only permutes its factors. At each macro-edge, the first step differs for INNER versus OUTER because a and b are distinct signed axes. Thus the first differing branch bit produces a different intermediate Cell. Reversing chirality changes the first subsequent shell endpoint a_(epsilon), so also changes the full Cell path. There are 6W binary branch choices in each chirality and two chiralities.

This is a *single observer fiber* of cardinality 2^(6W+1) for the declared fixed-W population. Therefore any injective fixed-length record of the complete ordered time history conditioned on (start, endpoint, event count, full signed histogram) requires at least 6W+1 bits, and the record (epsilon, branch word of length 6W) attains this bound. Even supplying ordered shell positions and the unordered signed-step pair *for each macro-edge* leaves 2^(6W) histories per known chirality and needs 6W branch bits.

### Theorem B (minimal locally measurable repair)

At every macro-edge its actual intermediate native Cell x_mid has
 d6(x_mid,c_*)^2 = 0 for INNER and d6(x_mid,c_*)^2 = 2 for OUTER.
Hence B_r = 1[d6(x_mid,c_*)^2=2] exactly recovers the local branch bit from one intermediate-Cell observation. The readout is invariant under simultaneous chart translation and full S6 positive-axis permutation of the declared chosen three-axis slice. Given the ordered shell sequence (or independently recorded chirality), the full B_0...B_(6W-1) word reconstructs the primitive path with no extra spatial axis.

This is an observer repair, not a physical assertion that an unknown rotation/Port mechanism measures this norm or chooses a branch. The same Cell-count and endpoint data without x_mid do not certify BRC chronology.

### Theorem C (root-domain observer cannot factor through histogram)

The frozen principal dyadic half-turn root section Sigma=3*epsilon has a proven native geometry lease on *oriented all-OUTER half-turn arcs*. On a W-circuit path, define the typed predicate E=1 if every one of its 6W intermediate Cells is an OUTER gate and every corresponding source-qualified OUTER half-turn arc remains available. For fixed W there are exactly two E=1 complete histories, one per chirality. In the same signed-histogram fiber there are 2^(6W+1)-2 ineligible histories.

Thus E is not a function of the signed histogram (nor of the ordered per-edge *unordered* step multisets). A typed C12 readout on this population with values {UNDEFINED,+3,-3} has exactly three distinguishable outcomes (2 fixed bits suffice); at the C6 root level the +/-3 branches alias, leaving {UNDEFINED,3}, two outcomes (one bit). Complete BRC chronology still requires 6W+1 bits. These observer sizes answer different questions; no physical precision-fiber time increment is inferred from static root selection.

## Executed exact certificate

Native test source:
- research_checks/X6_TIME_NATIVE_BRC_SIGNED_HISTOGRAM_FIBER_CHECK_20261121_1600.js
  at db42c81e256e2b4f47e3034e6ee8afdbfa7d9156;
- research_checks/X6_TIME_NATIVE_BRC_SIGNED_HISTOGRAM_FIBER_RESULTS_20261121_1600.json
  at 66bdb7e4abaf26c38157db9c45d14a6dddee3701.

The JS checker was actually executed for every path of W=1 and W=2 across both chiralities: 128 + 8192 paths, 537744 integer assertions, 0 mismatches. Each edge checks signed unit primitiveness, Cell displacement, local midpoint squared norm, branch-independent unordered two-step multiset; each path checks full return, exact signed histogram and uniqueness of ordered words; the global populations check complete cardinality and the typed root-domain labels. The general W formulas are proved symbolically above, not extrapolated from only two finite tests.

## Native objective, custody and next scientific action

This strengthens the parent native-time goal by identifying the precise *physical time datum* missing from signed direction counts: chronological joint relation / intermediate native Cell. It supplies a one-bit-per-macro-step observable test which a future actual Cell/Link/Port selection law can try to realize, instead of treating a direction histogram or simulated phase as proof of a physical branch.

Investigate source-backed rotation/triadic Port transition and evaluate whether it observes B_r or restricts its values; only then restrict the 36-state possibility graph and recompute its true reachable Markov quotient. The frozen Viète root eligibility witness is OUTER-only. No new physical transfer law, independent Driver admission or R063 native benchmark completion is claimed.

Existing exact protected request onhour-20261121-1502-own-time-units233-235-native-progress-v1 was OUTCOME_UNKNOWN then original-ID RECONCILE as of this turn; it must not be replayed. Unit236 semantic PROGRESS remains unsent. Preserve the original Research SID/claim/run and their original Source authorization boundary; a Github research note and Activity are distinct from Native semantic PROGRESS.
