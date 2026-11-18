# EC49FAH — Exact 76-edge optimum in the frozen H8/M5 signed-X6 observer model

Date: 2026-11-04. Status: **AUTHOR_FINITE_PROOF / EXACT_EXECUTED_CERTIFICATE / TWO_CHECKER_AUDIT / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED**.

Continuation: EC49FAG, immutable parent author commit `0a4b9d7af79241581500a955967ef56e42074cf8`, Draft PR #1730. Scientific input remains frozen at Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; current behavioral policy was read separately. P000 and ACTIVE worldview unchanged.

## Mother question and exact scope

The previously defined H8/M5/S<=6 *finite* problem selects legal ordered native signed-six-axis primitive-step words for windows h=2,...,8, realizes the complete six-axis positive-step BRC cache keys (five distinct keys), and realizes at most six distinct nine-history observer matrices with the required T2 or T4 signatures. Cost E counts all distinct **nonempty ordered signed primitive-step prefixes** in the chosen paths. The finite operations in this problem use the first three coordinates of a declared native X6 chart; the result does not assert optimality for unrestricted six-axis dynamics, other horizons, physical Heartbeat evolution, or arbitrary observer signatures.

The preceding author-side exhaustive classification partitioned all 1,989,509 legal cache schedules into triple-collision schedules (already certified E>=80), double-collision schedules eliminated at E<80, and the **12,356 double-collision schedules** in the immutable EC49EXY candidate TSV. Four explicit signed-X6 word selections published in EC49FAB achieve E=76.

### Theorem EC49FAH-1 — exact local-observer-demand prefix bound

Fix one of these schedules and one of its five complete-key fibers `i`. Let `H_i` be its assigned horizons, and for each horizon let the required observation colors be its complete frozen T2/T4 signature set. At depth d, let `U_i(p,d)` be the set of those horizon-tagged signatures for which **some actual observer-admissible signed primitive operation word** has the depth-d prefix p. Set `q_i(d)=0` when the fiber has no required depth-d words, and otherwise define the *exact finite set-cover number*

`q_i(d) = min {|S| : S consists of signed depth-d prefixes and union_{p in S} U_i(p,d) covers all required horizon-tagged signatures in fiber i}`.

Every legal global construction must realize at least `q_i(d)` distinct depth-d prefixes within fiber i. This follows by taking the depth-d prefixes of the actual words chosen for each required signature: their union is one admissible cover in the stated finite set-cover problem. No earlier-depth `q_i=1` simplification is needed.

Let `C_ij` be the exact largest possible signed primitive-step common-prefix length between *any* admissible words in fibers i and j, as computed from the unchanged pinned EC49EXJ native generator and stored in the EC49EXY exact capacities table. At depth d form the incompatibility graph `G_d` on live fibers with edge `ij` whenever `C_ij<d`. Distinct fibers joined by an edge have disjoint possible depth-d prefixes; therefore, for every clique J of `G_d`, physical total distinct depth-d prefixes `N_d >= sum_{i in J}q_i(d)`. Hence

`B_local(S) := sum_{d=1}^{Lmax} max_{J clique of G_d} sum_{i in J} q_i(d) <= E(S)`,

for every fixed schedule S, with empty depths contributing zero. This is a mathematical necessary bound; its exact local set-cover numbers and finite clique maxima are computable with integer masks alone.

### Theorem EC49FAH-2 — complete finite catalogue closes the bound at 76

The executed checker `VERIFY_EC49FAH_COMPACT.py` independently regenerates every admissible signed native path using the pinned source, maps all actual ordered signed prefixes to IDs, computes all local `q_i(d)` exactly by bitmask set cover, and computes all five-fiber clique weights at each active depth. The complete frozen TSV census has **12,356 schedules and zero rows with `B_local<76`**. In fact the minimum is 76, attained by 66 rows in the lower-bound relaxation.

Inputs and coverage:
- EC49EXY `EC49EXY_DOUBLE_CANDIDATES.tsv`: 12,356 data rows, SHA256 `1e5f75bdc2491f355db6e2632fb6789a55397f7943c77c6ebf249807ee20712a`.
- Unchanged native generator `EC49EXJ_H8_M4_S6_GLOBAL_EXACT/SCREEN_H5_EC49EXJ.py`, Git blob `0e83eac43199e5854d462d1928aba6a146db5261`; 137 distinct observer-admissible word families actually used.
- EC49EXY exact cross-family capacities `EC49EXY_CAPS_TABLE.txt`, 164 families (existing published table); 448,120 signed nonroot prefix-trie nodes.
- 219 distinct complete-key groups and **3,964 (group,depth) exact local signature-cover computations**.

Two additional separately executed author-side audits:
1. `AUDIT_EC49FAH.py`: independent breadth-first search in color-mask state space confirms all **3,964** local q values; all **9,316** unordered native family-pair capacities among the 137 actually used families are checked against signed-prefix existence at C and absence at C+1; all four existing explicit witness sets are rechecked as cost 76 with required observation signatures and per-depth q bounds.
2. `AUDIT_EC49FAH_PAIRWISE_CENSUS.py`: an independently coded complete 12,356-schedule direct subset enumeration confirms `min B_local=76`, exactly 66 cases of equality, and zero <76 cases.

The original EC49FAG three-way prefix obstructions were also tested: **2,520** live three-fiber events; adding their immediate counting inequality increases the numerical depth lower bound in **18 schedules**, by a combined **34 edges** across those schedules. They are structurally informative but are **not needed** for the exact 76 threshold: the exact local observer demands and existing pairwise signed-prefix capacities already close it. Thus no full five-fiber integer multicover optimizer is needed for this theorem.

### Corollary EC49FAH-3 — exact finite optimum

In the frozen H8/M5/S<=6 signed-X6 observer model, assuming the published upstream complete 1,989,509-schedule classification and the already published explicit 76-edge legal signed-word constructions,

`E* >= 76` (all schedules by the complete old classification plus EC49FAH-2),

`E* <= 76` (the four published legal witnesses),

so **`E* = 76`** in this *precisely declared finite model*.

The upstream enumeration and 76-edge witness dependencies must be verified by an independent Driver before Source-native admission. This author-side theorem has been locally executed and independently cross-checked at the algorithm level, not reviewed as a canonical Enterprise Math Result.

## Reproduction and artifacts

From the sibling research-notes directory, run:

```sh
python3 EC49FAH_H8_M5_EXACT_76_OPTIMUM/VERIFY_EC49FAH_COMPACT.py > EC49FAH_COMPACT_REPORT.json
```

This program reads only the existing pinned native generator, unchanged EXY candidate TSV and EXY exact capacities table. Its exact executed output is stored as `EC49FAH_COMPACT_REPORT.json`. The two independent audit reports are stored as `EC49FAH_INDEPENDENT_AUDIT_COMPACT.json` and `EC49FAH_INDEPENDENT_PAIRWISE_CENSUS_COMPACT.json`, and their executed source is `AUDIT_EC49FAH.py` and `AUDIT_EC49FAH_PAIRWISE_CENSUS.py`. These audit scripts reuse the primary source's trie, then independently recompute its key local and global claims; they are not independent Driver reviews.

Witness dataset: `../EC49FAB_H8_M5_FOUR_EXPLICIT_76_WITNESSES/EC49FAB_EXPLICIT_76_WITNESSES.json`. The four examples have original ranking identifiers 1512, 1513, 2200, 2203 (unranked TSV rows 592,782,3307,3954). Their exact selected paths and observer signatures are in that earlier immutable file, not replaced here.

## Status and next discriminating question

This is a **finite exact optimization theorem**, a useful closed subproblem of Enterprise Math. The cross-horizon q construction suggests a reusable BRC observer sufficiency invariant: how do the local prefix-cover numbers behave under a new horizon, signature family or native axis support? Next EC49FAI should first obtain independent Driver review of the finite 76 certificate, then derive a reusable parametric inequality or a minimal counterexample to its persistence at H9/M5. Source-native authority and active Owner remained unavailable to this author session on 2026-11-04; native CLAIM, Result, Driver admission and promotion have not occurred.
