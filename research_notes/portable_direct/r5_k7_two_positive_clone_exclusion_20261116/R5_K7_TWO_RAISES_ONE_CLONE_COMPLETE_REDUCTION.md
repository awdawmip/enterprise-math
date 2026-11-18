# R5 seven-cycle: unrestricted 18-state one-step controllers — complete one-clone reduction and MILP exclusions

Date: 2026-11-16. Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Status: AUTHOR_PROVED finite reduction / exact 19-state upper from prior source / NUMERICAL_MILP_EXCLUSION for lower / NOT_REVIEWED.
Scope: auxiliary genuine-source seven-cycle, slack s=2, ONLY positive named actions Set_0(1) and Set_1(1). This does not assert native X6 dynamics, P000 promotion or formal task/CLAIM.

## 1. The declared model and the unresolved question

Raw masks u are 0..127. Set q(u)=sum_{i modulo 7} u_i*u_{i+1}; a source centre r supports u precisely when

    G(r,u) : (u & ~r)==0 and 0 <= q(r)-q(u) <= 2.

Let F(r)={u:G(r,u)}. The raw actions are U_a(u)=u|(1<<a), a=0,1.
A deterministic Moore state s has one output centre c(s); its transitions f_0(s),f_1(s) need not commute or be idempotent; each raw u may choose an initialization s. Horizon-one correctness means G(c(s),u) and G(c(f_a(s)), U_a(u)) for both a; all-horizon correctness means the same after every finite action word.

Prior exact set-cover proof establishes M_stat(7,2)=17 (the 299,008-memo-state exhaustive integer recurrence; see the frozen seven-cycle exact 17 theorem). Prior fully integer-checked witness gives an all-horizon controller with 19 states. Prior 0–1 MILP reported infeasible for horizon one with <=18 distinct inclusion-nondominated source labels. The remaining issue was repeated outputs.

## 2. Proven reduction: only one duplicate output is relevant

**Lemma (source-dominance normalization).** If F(r) is included in F(t), replacing an internal state's source output r with t, keeping its transitions and initializations unchanged, cannot destroy correctness at any future word: every requirement involving that state is a membership test in F(c(s)). Every state may therefore be assigned an inclusion-maximal mask without increasing the state count. The inclusion-maximal masks in this model are exactly 57 distinct centres; the adjacent reproduction program computes them from all 128 raw masks.

Any controller with m states yields a static cover of all raw masks by its distinct output labels. The exact static lower bound 17 forces at least 17 distinct source labels. For m<=18 there are only the distinct-label case or m=18 with exactly 17 distinct labels and two states carrying the same output. A 17-state controller is already included in the at-most-18 distinct-label test; equivalently it can be padded with an unreachable duplicate state.

**Reflection symmetry.** Let theta permute the seven bits by i -> 1-i (mod 7). Since theta is a cycle automorphism, q(theta u)=q(u) and G(theta r,theta u)=G(r,u). It swaps U_0 and U_1, so a one-clone controller with duplicated centre d exists iff one with duplicated centre theta(d) exists. The 57 nondominated centres form 32 theta-orbits (7 fixed points and 25 size-two orbits). It suffices to check 32 duplicate centres.

The orbit representatives, exhaustively generated from the source masks, are:

    23,27,29,31,39,43,45,46,47,53,54,55,57,59,61,62,
    63,77,78,79,85,87,92,93,94,95,108,109,111,124,125,127.

## 3. Exact Boolean formulation of each clone case

Fix the duplicate centre d. Create 58 *potential* internal state slots: one for each nondominated centre and a second slot labelled d. Use binary variables x_s (active state), y_{s,a,t} (the unique action-a transition from active s to active t), and z_{u,s} (u may initialize s). Set the clone active, force its primary d-slot active, and require exactly 18 active states. All labels and costs are explicit.

Impose these constraints:

    sum_s x_s = 18, x_clone=1, x_clone<=x_primary(d)
    sum_t y_{s,a,t}=x_s, and y_{s,a,t}<=x_t
    z_{u,s}=0 if u is outside F(label(s))
    z_{u,s}<=x_s, and sum_{s:u in F(label(s))} z_{u,s}>=1
    z_{u,s}<=sum_{t:U_a(u) in F(label(t))} y_{s,a,t}, for both actions
    all variables binary.

**Equivalence proof.** Every actual 18-state controller with this duplicated label yields a solution by making its used slots active, recording its deterministic transitions, and choosing one legal initialization per raw mask. Conversely a feasible binary solution has exactly one selected successor for each active state/action and at least one legal initialization for each raw mask. The last inequality guarantees both one-step observations. This argument relies on no internal reset identities. It handles overlapping beliefs and repeated output labels without a hidden distinctness assumption.

The script REPRODUCE_R5_K7_ONE_CLONE_MILP.py constructs this model directly with integer 0/1 coefficient matrices and SciPy 1.17.0 / HiGHS. For each tested d, its reported model has 7,614–7,623 binary variables, 9,459–9,486 rows and 35,484–36,151 nonzero coefficients. Numerical solving is separated from the exact combinatorial equivalence proof.

## 4. Computational result and exact scope

All 32 orbit representatives were submitted to HiGHS. Each returned scipy status=2 / HiGHS model_status=Infeasible, with no solution or optimality gap. Two first-pass trials (d=63 and d=94) reached their 30-second limit without a verdict; the same fully specified model was actually rerun at a 39-second cap and returned INFEASIBLE (observed 29.656s and 27.771s respectively). These definitive receipts replace the two initial incomplete trials. The original numeric outputs, matrix sizes and per-instance elapsed times are recorded in RESULTS_R5_K7_ONE_CLONE_MILP.json.

Combining this orbit-complete one-clone computation with the prior distinct-label MILP result excludes all <=18-state horizon-one controllers *conditional on the soundness of the reported HiGHS infeasibility decisions*. The exact constructive 19-state witness survives every finite word by a separately checked greatest-forward-invariant relation. Consequently, under that explicit solver-evidence condition,

    N_0(7,{Set_0(1),Set_1(1)},2)=17,
    N_H(7,{Set_0(1),Set_1(1)},2)=19 for every H>=1.

N_0=17 has a separate solver-independent exact set-cover certificate. The 19-state upper is solver-independent. The >=19 lower is at present a fully enumerated family of *numerical integer-program infeasibility reports*, not a separately checked formal UNSAT/branch-and-bound proof certificate. It must not be labelled independent EXACT_FINITE_EXHAUSTIVE until that proof object is supplied and checked.

## 5. Verifier commands and next step

    python REPRODUCE_R5_K7_ONE_CLONE_MILP.py --duplicate 63 --time 40
    python REPRODUCE_R5_K7_ONE_CLONE_MILP.py --all-orbits --time 40

The prior distinct-centre numerical test resides in r5_k7_two_positive_horizon_20261116/REPRODUCE_R5_K7_ONE_STEP_DISTINCT_MILP.py and the exact 19-state controller in VERIFY_R5_K7_TWO_POSITIVE_UPPER.py, under the immutable branch SHA 40ac9d8702762e7153f9e8edbc03ac7d6ffa6696. The exact static 17 lower is in r5_k7_single_control_exact_20261116/R5_K7_SINGLE_CONTROL_EXACT_SEVENTEEN_THEOREM.md at bffcb11580db5949f44bf888e8b821a52e766550.

Next: extract a small solver-independent exact UNSAT certificate for the 18-distinct model plus the 32 clone representatives; alternatively seek a compact groupwise forbidden-initialization theorem which avoids 32 numerical MILPs. Only then upgrade the >=19 result to an unconditional mathematical lower bound. This auxiliary model's observer, source provenance and update semantics remain separate from native six-axis claims.

Publication: independent author-side R5 scientific evidence. Current task execution CLAIM and protected Activity/Result/Review authority are separate.
