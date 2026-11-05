# EC49FBI — H5 high-key mixing cannot improve the 112-edge native-X6 nine-window construction

Date: 2026-11-05. Mode: TASK_RESEARCH / exposed directed context. Author-side finite 0-1 MILP optimum with independently verified integer witnesses; not independently Driver-admitted. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Target and genuinely new coverage

Retain original H2 = {fe,ge}, H3 = {feg,gef}. These use 16 native signed primitive-prefix edges and three six-component positive cache keys. Fix the remaining two keys
`L=(4,2,1,0,0,0)` and `M=(6,4,1,0,0,0)`.
Allow unrestricted legal operation words with **L at H4, L or M in any mixture at H5, M at H6,H7,H8,H9**. Across all H2–H9 require the original endpoint (2,0,0,0,0,0), all horizon-specific observation matrices of rational rank nine, at most five full positive BRC cache keys. The objective E counts distinct signed primitive-step prefixes.

Complete 0-1 integer optimization reports:
- **E*=112 edges** over this entire specified mixed-H5 family.
- **E*=128 edges** if at least one M-key H5 word is selected.
The first optimum is attained without any M-key H5 word; the second is attained with `ceccc` (M-key) at H5. These are scoped finite computational optima with exact model-to-ILP equivalence and HiGHS 0.0 reported MIP gaps, plus independently checked explicit upper-bound witnesses. An independent exact-integer dynamic-programming lower-bound certificate is a possible follow-up, not claimed here.

This extends EC49FAZ (fixed L at H4/H5, M at H6–H9), and shows that **premature use of the H9-compatible M key at H5 cannot reduce this selected key schedule's nine-window prefix cost.** In particular the existing 70-edge H2–H6 local winner belongs to a complete schedule whose global best is 112; the mother question's unrelated 94-edge construction remains intact.

## Exact native operation model and analytic structural lemma

Original operations: `a=(-1,-1)`, `b=(-2,-2)`, `c=(+1,+2,-1,-2)`, `d=(+2,+1,-2,-1)`, `e=(+3,+1,+1,-3)`, `f=(+1,-1)`, `g=(+2,-2)`. In this frozen terminal family b is excluded by the earlier endpoint-count identity. Every selected word expands into its original ordered signed-six-axis primitive steps. BRC key counts positive signed-axis occurrences. Nine-state DFA and signature/rank test are unchanged from EC49FAX/FAR.

**Same-key terminal-depth lemma.** Suppose a native path ends at displacement (+2,0,0,0,0,0) and its complete positive key is K=(x,y,z,0,0,0). Total positive primitive steps = x+y+z. The six signed displacement equations give a total of x+y+z−2 negative primitive steps. Hence its native primitive length is precisely
[
  \ell(K)=2(x+y+z)-2.
]
Thus every L-key terminal lies at depth 12, and every M-key terminal lies at depth 20 of the signed-prefix trie, even when their operation-word lengths (horizons) differ. The six used operation codewords are primitive-prefix-free (first two primitive signed steps distinguish them), hence different complete operation words are different native terminal leaves. This establishes an exact finite two-depth terminal geometry and permits a single trie to retain every cross-horizon shared prefix.

For any horizon h with key (x,y,z), original count conservation gives
`#a=z-1; #e=z; #c+#d=x+y-h-1; #f=h+1-y-2z; #g=h+1-x`.
The required nonnegativity forces L only at H4 and H5, M first at H5, and M for H6–H9. Candidate words are **every** multiset permutation with all assignments of c/d; the nine-state DFA plus signed endpoint filters them.

## Exhaustive candidate census

| Horizon | Keys | Raw word candidates | Endpoint and allowed-signature candidates |
|---|---|---:|---:|
| H4 | L | 48 | 48 |
| H5 | L and M | 110 = 30+80 | 34 = 24+10 |
| H6 | M | 960 | 240 |
| H7 | M | 2,520 | 1,260 |
| H8 | M | 2,240 | 2,240 |
| H9 | M | 630 | 560 |

The union of all eligible words plus fixed early words forms a native signed-prefix trie of **26,742 non-root edges**; 16 are fixed/prepaid from H2/H3. The four-clause observer test per horizon H4–H8 is (E∨F)∧(C∨F)∧(D∨G)∧(J∨G), and H9 (M key) requires F and G, for **22 exact coverage inequalities**.

## Integer-program equivalence and results

Set one binary variable `t_v` for each non-root native trie edge leading to v. For each non-root parent p require `t_v ≤ t_p`. Set all fixed early `t_v=1`, with objective coefficient zero. Each of 22 coverage clauses requires `Σ_{v terminal satisfying clause} t_v ≥ 1`. Minimize `Σ_{v not prepaid} t_v + 16`. For the forced-H5-M variant, also require `Σ_{v H5-M terminal} t_v ≥ 1`.

Forward direction: from any legal word selection, take its union of primitive prefixes; these variables satisfy every constraint and the objective equals the exact union cost. Reverse direction: from any feasible binary assignment, choose its terminal words that satisfy the clauses; parent closure ensures every required prefix is present, so the resulting union cost is **no larger** than the model objective. Every optimum therefore has exactly the mathematically defined prefix-union minimum. This is a model equivalence for the stated finite family, not a general numerical equivalence claim.

Python 3.13.5 / SciPy 1.17.0 / HiGHS, 0-1 integrality, 26,742 variables. Unforced model: 26,761 linear rows, 57,884 nonzeros, status=0 Optimal, base objective 96, explicit union 112, `mip_gap=0`. Forced H5-M: 26,762 rows, 57,894 nonzeros, status=0 Optimal, base objective 112, explicit union 128, `mip_gap=0`. Reported solver lower bounds equal the respective integer optimum objectives (forced bound 112.00000000000001 before integer rounding).

Separate standard-library witness checker recomputes native signed displacement, positive complete keys, DFA signatures and rank clauses for H2–H9, distinct prefix counts and the forced-H5-M condition. It obtains exact union counts 112 and 128, with five distinct keys in each witness. Lower-bound evidence is the finite ILP plus HiGHS solver status; explicit witness truth is independently checked by integer Python.

Reproduction (run in an environment with SciPy): `python VERIFY_EC49FBI.py 35` for unforced; `python VERIFY_EC49FBI_FORCE_H5M.py 30` for forced. Run `python CROSSCHECK_EC49FBI.py` after producing the JSON reports. Executed local code artifacts and output reports are provided in this directory.

## Next scientific unit

Apply the same rooted signed-X6 leaf-level ILP to selected **other** among EC49FBH's 124 feasible L/M pairs, starting with M choices having small high-horizon operation-word counts. Track explicit witness cost and solver dual bound; test whether a higher H2–H6 cost buys enough late prefix sharing for a whole nine-window improvement. For large candidate trees, derive an exact integer OR/min-plus cutset certificate or scoped admissible lower bound. Eventually vary the fixed H2/H3 root and seek E≤93. Keep distinct author computation, solver evidence, independent integer proof and formal Driver acceptance.

## Provenance

Prior exactly pinned source: EC49FBH `26d3b584ca34ff7439ba0c5879f93a1cc40ee29a` and original frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. P000 and protected ACTIVE worldview unchanged. No CLAIM, Result or independent Driver admission asserted.
