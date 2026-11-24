# R5 continuation: future-language residual quotient and two-cut ordered recourse certificates

Date: 2026-11-15. Provenance: frozen scientific input `435e77af0d180eac32bd1f9c4c464bc4010b7551`, R5 independent author-side Draft PR #2427 head `f397ff3067c5857e374fd82547379373a6aa9c79`. Scope: the prior 954-event strictly increasing integer-coordinate, radius-two, event-indexed-center **derived observer**; the first theorem is more general finite layered-DAG mathematics. It asserts no native X6 equivalence.

Research status: AUTHOR_PROVED / FINITE_EXACT_TOY_CHECKED / EXACT_PREVIOUS_TABLE_DERIVATION / NOT_INDEPENDENTLY_REVIEWED. No formal Task, CLAIM, Result or review status is inferred.

## 1. Future-language residual is a sufficient old-frontier observer

Consider two finite center-path languages N (new) and O (old), each from a fixed start to a fixed end. Every center-path vertex is labeled by an integer original event index; edges increase that index, and the overlap score is the number of **shared labeled center indices**, excluding any agreed unweighted endpoints. Fix a new-language node at cutoff j and a new prefix ending there. For each live, rank-labeled old frontier vertex t, let `v_t` be the maximum overlap with this new prefix among old prefixes ending at t. A nonreachable t has score `-infinity`.

Let `L_t(j)` be the complete set of old labeled suffix sequences *strictly beyond cutoff j* available from t to the common terminal. Every complete old path crosses the cut at one live tail t. For a possible continuation Q of the new path beyond j, define

```
F_t(Q) = max_{T in L_t(j)} |set(Q) intersect set(T)|,
Phi_v(Q) = max_t (v_t + F_t(Q)).
```

The maximum over an empty or unreachable set is minus infinity. Each old full path splits at its unique crossing tail; its processed-prefix score is at most `v_t`, and one old prefix realizing `v_t` can concatenate with any old suffix in `L_t(j)`. Hence `Phi_v(Q)` is **exactly** the old player's maximum final overlap for that completed new suffix. This is the load-bearing frontier decomposition premise of the existing offline R5 Pareto algorithm.

### Theorem 1a: lossless future-language quotient

Define `t ~ s` when `L_t(j)=L_s(j)` as *labeled* suffix languages, retaining event identities and multiplicity semantics when present. For every equivalence class C, replace the scores of all its states by the single value `M_C=max_{t in C} v_t`. Then for every possible new suffix Q,

```
Phi_v(Q) = max_C (M_C + F_C(Q)).
```

**Proof.** Each t in C has the same F function because it has the same set of labeled old future paths. Distributivity of max over addition gives `max_{t in C}(v_t+F_C(Q))=M_C+F_C(Q)`; taking max over classes yields the identity. This holds for all new continuations Q, so no future overlap observer can distinguish vectors with the same class maxima.

If an old frontier has w rank-labeled states but only s distinct nonempty future languages, the **representation of the response as an abstract sufficient observer** needs at most s score coordinates, rather than w. With h processed weighted new centers, each coordinate is one of `{-infinity,0,...,h}`. Under componentwise Pareto deletion at a fixed new node, the number of retained *quotient* score vectors is bounded by

```
A_suffix(j,h) <= (h+2)^(s-1)  (s >= 1).
```

This follows by projecting a componentwise antichain to any s-1 coordinates. It refines the previously proved `(h+2)^(w-1)` **for an implementation that actually maintains valid quotient transitions**. An existing w-coordinate implementation is unchanged by this theorem; naively dropping coordinates without implementing the induced transitions is not licensed.

### Theorem 1b: inclusion-based dominance strictly strengthens Pareto

At the same new-language node, let u and v be two old-frontier score vectors. Suppose that for every t with finite `u_t`, there exists some old frontier state q such that

```
u_t <= v_q  and  L_t(j) subseteq L_q(j).
```

Then `Phi_u(Q)<=Phi_v(Q)` for **every** possible future new suffix Q. Thus the new minimizer may discard v, even when u and v are incomparable componentwise.

**Proof.** Labeled-language inclusion implies `F_t(Q)<=F_q(Q)`. The displayed score inequality gives `u_t+F_t(Q)<=v_q+F_q(Q)<=Phi_v(Q)`. Maximize over t. A finite scorer with no reachable old path is handled by minus infinity.

The ordinary coordinatewise rule is recovered by choosing q=t for every t; language inclusion can therefore yield strictly stronger exact pruning. It is a sufficient, not a claimed necessary, language-order test.

**Concrete witnesses.** For two old states with identical future language `{{1},{2}}`, the vectors `(1,0)` and `(0,1)` are coordinatewise incomparable but induce the same future response for every new suffix. For a strict inclusion witness, take `L_a={{1}}`, `L_b={{1},{2}}`, `u=(1,0)`, `v=(0,1)`. The inclusion certificate holds; for Q={2}, `Phi_u(Q)=1 < 2=Phi_v(Q)`, yet neither vector is coordinatewise <= the other.

**Validation.** `VERIFY_FUTURE_LANGUAGE_RESIDUAL.py` runs 3,000 deterministic finite path-language/vector trials over all 16 new suffix subsets of a four-symbol universe: 48,000 exact quotient equalities and 8,112 certified inclusion-response inequalities. It also checks both strict witnesses. Result: `PASS_FUTURE_LANGUAGE_RESIDUAL_OBSERVER`. These are toy and generic finite-language checks, **not** a rerun of all 256 frozen R5 optimizer instances. Proof above establishes the universal finite statement; project-specific computational savings remain open.

## 2. R5 cuts 8 and 9: exact ordering-dependent two-step **bounds**

For nonempty families A,C of K-element labeled center sets, let
`H(C,A)=max_{S in C} min_{T in A}|S\T|`. This is a directed Hausdorff distance for the equal-cardinality set-replacement metric, and satisfies the triangle inequality. Write `O_B=Opt_B(K)` for the prior exact optimizer family.

For K=214..221, the previously proved constant optimal cost and family-expansion theorem give `O_B subseteq O_{B+i}` after closing cut i. Fix a background B missing cuts 8,9, and define `D_89=H(O_{B+8+9},O_B)`. The following are **certified interval bounds**:

```
L = max(r_8(K,B), r_9(K,B))
U_8then9 = r_8(K,B) + r_9(K,B+8)
U_9then8 = r_9(K,B) + r_8(K,B+9)
L <= D_89 <= min(U_8then9,U_9then8).
```

The lower inequality follows because both single-closed optimizer families are subsets of the joint-closed family. The upper inequalities follow by taking the intermediate family along either route and applying the directed Hausdorff triangle inequality. This statement preserves the old-target/min then new-source/max quantifier order.

Reuse the existing 256 exact author-side single-cut distances in `EXACT_R5_OFFLINE_MAXMIN_ALL_BACKGROUND_VALUES.json`, whose original full-calculation SHA-256 is `e8157e196f3d8408a11bf5f67935d4e083578844d6461433f209fed63f4e04ed`. The previously established effective cut set is {3,8,9,10,27} at these budgets; thus there are exactly 8 relevant backgrounds B over {3,10,27}, for each of 8 K values = **64** two-cut cases. The table below gives `(U_8then9,U_9then8)`; bits 3 and 27 have no effect on these particular values.

| K | Cut 10 open | Cut 10 closed |
|---:|---:|---:|
|214|(12,10)|(12,14)|
|215|(11,9)|(11,12)|
|216|(11,9)|(10,10)|
|217–220|(10,8)|(10,10)|
|221|(10,8)|(10,8)|

Out of 64 exact upper-certificate comparisons, **9-then-8 yields the tighter bound in 36 cases; 8-then-9 in 8 cases; the bounds tie in 20 cases**. After choosing the better route, the interval upper-minus-lower gaps are exactly 3 in 36 cases and 5 in 28 cases. Therefore the already-known single-cut table alone does **not** determine the joint-closure distance; it does determine an exact family of two-step upper/lower certificates and their order dependence.

`VERIFY_R5_TWO_CUT_ORDER_CERTIFICATES.py` reads the **committed compact table**, checks all 256 input entries (16 masks × 2 cuts × 8 budgets), computes the 64 certificates and the summary above, and returns `PASS_R5_TWO_CUT_ORDERED_CERTIFICATES`. This is a deterministic integer consequence of the previously saved author data; it is not an independent rebuild of those old optimal-path DP values.

## 3. Unfinished scientific obligations

1. On the actual R5 old optimal rank-labeled DAGs, compute labeled future-language equivalence and inclusion classes at the relevant cuts. Measure the reduced width s against the previously observed w<=19 and compare a correctly implemented quotient DP with the unchanged 256-case baseline before claiming runtime improvements.
2. Independently audit the existing common-anchor factorization and exact old max-plus frontier recurrence against full optimizer languages.
3. For simultaneous closure of cuts 8,9, run a genuine direct max-new/min-old joint-language calculation to replace the interval certificates by exact D_89; keep all frozen science inputs and case labels unchanged.

Source and interpretation: `research_notes/portable_direct/r5_low_budget_unit_recourse_20261115/OFFLINE_MAXMIN_EXACT_RECOURSE_THEOREM.md`, `PARETO_FRONTIER_PARAMETRIC_BOUND_AND_BACKGROUND_REVERSALS.md`, and `research_notes/portable_direct/r5_frontier_spatial_support_20261115/BUDGET_EXCESS_FRONTIER_WIDTH_BOUND.md` at prior Draft branch `f397ff3067c5857e374fd82547379373a6aa9c79`. Existing author-source evidence is reused under its exact declaration; native X6/P000 premises are preserved without promotion of this auxiliary 1D observer. No independent mathematical review or formal result admission has been performed.
