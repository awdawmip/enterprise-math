# EC49FEL — exact exclusion of ≤93 native-prefix edges for the H3,H4,H5,H7,H9-high family

**2026-11-08 · author-side finite mathematical result · frozen science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`**

## Precise theorem

In the unmodified EC49FEJ signed-X6 native path / full positive-BRC-key / nine-state DFA model, take horizons H2–H9 with endpoint `(+2,0,0,0,0,0)`. Require one path for each signature `(16,32)` at **H3,H4,H5,H7,H9**, and one path for each `(1,2,4,8)` at **H2,H6,H8**. There are exactly 22 selected native paths. Permit arbitrary mixing of eligible full positive-BRC keys within an individual horizon, with **at most five distinct full keys** overall.

**Theorem (finite exact):** Every such valid 22-word system has at least **94 distinct nonempty ordered signed-native-step prefixes**. Therefore none meets the mother target `C_native ≤93` in this particular quota family.

## Exhaustive domain

H2's four required low-signature words force the full key `(3,1,1)`. With five high horizons and only five keys, H3 is high and uses precisely this key. For each other high horizon h, an eligible high key `(x,y,z)` satisfies `x+y=h+1`; keys at different high horizons cannot coincide. Exact primitive enumeration returns the option counts H4=2, H5=4, H7=9, H9=16. This produces **2×4×9×16=1152** distinct and exhaustive inventories (including all legal within-horizon mixing). All **1152** have the required signature pools for H2–H9 and a verified explicit lexicographic 22-word witness.

## Lower-bound proof

There are four legal early H2–H3 variants. Each contributes exactly 42 distinct nonempty native prefixes. Their union U has 54 distinct prefixes. Give the entire U to *every* later configuration for free. For each horizon/signature requirement among H4–H9, enumerate all eligible ordered primitive words from that inventory and retain their **full signed-native-step** expansion. At native depth d, retain a requirement G only when every eligible candidate for G has length at least d. Every chosen word in G necessarily then contributes a prefix at depth d. Each depth-d prefix p covers G if some candidate for G starts with p. Give away all groups covered by U at that depth; solve the remaining exact finite minimum set-cover using integer bitmasks, obtaining m_d(K). Since the chosen actual native prefix set covers every still-mandatory group at every retained depth, every valid system W with that inventory K satisfies

`C_native(W) ≥ 42 + Σ_{d≥1} m_d(K)`.

Independent set cover at each depth and free U both relax, rather than strengthen, the original problem. Stopping when the partial sum reaches 94 is sound because each m_d(K) is a nonnegative integer. The exhaustive integer computation did so for **1152/1152** inventories. Truncated lower-bound values (at stopping depth) range from **94 to 104**. The value is a certified lower bound, not a reported exact optimum of each inventory.

## Actual executed evidence

The executed program `EC49FEL_CENSUS.py` reads the unchanged EC49FEJ/FEK primitive modules. Three uninterrupted, disjoint *result ranges* cover indices `[0,144)`, `[144,936)`, `[936,1152)`; one long process was interrupted after its latest complete result checkpoint `[144,936)` and the continuation resumes exactly at 936. Every stored row has `status=excluded93`. All **1152/1152** lexicographic witnesses are valid with exactly five full keys and 22 words, a total of **25,344 verified original signed-X6 paths**. Witness costs are **114–290** edges; these are construction costs rather than optima. An independently coded SciPy/HiGHS 0–1 MILP implementation agrees for **40 depth-subproblems across 10 sampled inventories**, while completeness rests on the integer-DP census and mathematical covering reduction.

`EC49FEL_WITNESS_REPORT.json`, `EC49FEL_MILP_AUDIT.json`, all three census JSON files and their actual executors are in the full local evidence archive delivered with this study. The repository's readable proof and self-contained study replay script can regenerate all 1152 cases from the pinned EC49FEJ primitive source; the previously submitted FEK reproduction implementation already contains the same exact bitmask covering algorithm.

## Frontier and next discriminating question

The previous author-side enumeration excluded ≤93 for three other distinct minimal 22-word quota families: 1728 inventories (high H3,H4,H6,H7,H9), 2304 (high H3,H4,H6,H8,H9) and 768 (high H3,H4,H5,H6,H9, of which 336 quota-infeasible). The new family adds 1152 **feasible** inventories, raising the enumerated family-specific total to **5952** inventories: **5616** quota-feasible (all excluded for ≤93) and **336** infeasible. This sums *disjoint high-horizon families* and does not assert a global 22-word or unrestricted optimum.

**EC49FEM:** analyze a new high-horizon family outside these four, especially configurations where H9 is low and its four different observer signatures may share earlier native prefixes. For a family whose exact depthwise lower bound remains ≤93, use joint prefix-aware integer optimization or build an explicit ≤93 witness. Keep full key, signed-X6 and DFA semantics. The known global 94-edge construction remains the incumbent upper bound for the original mother target.

## Publication and authority

The 1152-case proof is an **author-side exact finite computation**. The native gateway's current Site-scoped `research_authority_granted=false`; no native CLAIM, Result/Review or independent Driver admission is asserted. The historical research author line is `PR #1730`; this contribution is appended to that existing branch. P000 and the ACTIVE worldview are unchanged. Sources: EC49FEJ, EC49FEK and their exact prior commits; current global governance and Source normative context read independently on 2026-11-08.