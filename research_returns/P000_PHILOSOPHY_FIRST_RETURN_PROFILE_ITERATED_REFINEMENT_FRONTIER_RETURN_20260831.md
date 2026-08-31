# P000 Philosophy-First Q22 — Return Profile Iterated Refinement Stable Frontier Return

Task: `RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-ITERATED-REFINEMENT-FRONTIER`  
Publication: `TP2-FB7F3C4C97CC74A3CA25`  
Researcher: `EM-PQ22-E21EA3`  
Claim: `chatgpt-p000q22-20260831-1343-e21ea3`  
Execution branch: `research/p000-phil-q22-return-profile-iterated-refinement-em-pq22-e21ea3`  
Hard target: `P000_RETURN_PROFILE_ITERATED_REFINEMENT_STABLE_FRONTIER_EXACTLY_CLASSIFIED`

## Terminal verdict

`SUCCESS / ITERATED_REFINEMENT_INJECTIVE_AND_REPRESENTABLE_ON_EXACT_DECLARED_PREFIX`

Freeze the Q19 family

\[
\mathcal U_{BR}(n)
\]

as finite connected simple native-Cell adjacency graphs on exactly `n` Cells, every Cell of degree `2` or `3`, with at least one degree-`3` Cell, modulo Cell relabeling / graph isomorphism.

Freeze the Q16/Q19 primitive-return multiplicity profile

\[
c_0(x)=m_X(x),
\]

and define natively, before any classical terminology is imported,

\[
c_{t+1}(x)=\Bigl(c_t(x),\ \multiset_{y\sim x}c_t(y)\Bigr).
\]

Let `R_t(X)` be the anonymous multiset of root colors.  The exact result established here is:

1. every `R_t`, and hence the stabilized semantic packet `R_inf`, is invariant under Cell relabeling;
2. the induced root partition refines monotonically and stabilizes after at most `n-1` strict refinement steps (sharpened to `n-|c_0(X)|` strict splits for a fixed object);
3. the frozen Q19 nine-Cell collision is separated already by `R_1`;
4. exact degree-normalized exhaustive enumeration proves the stable semantic packet injective on every `U_BR(n)` for `4 <= n <= 9`;
5. the exact representability image sizes on that prefix are

   `2, 3, 10, 20, 59, 147`;

6. the exact search covers `566,557` degree-normalized connected realizations and `241` graph-isomorphism types / stable packets;
7. every one of the `241` exact image elements has a frozen ordered metadata row recording degree sector, minimum stabilization index, and stable color-class count, while the full per-size canonical image is pinned by a whole-image SHA256;
8. the largest stabilization index on the exact prefix is `3`;
9. only `30/241` exact image elements have a discrete stable root partition, while `211/241` remain non-discrete, so the local refinement does **not** collapse to full vertex-by-vertex canonical encoding on this prefix;
10. after the native recurrence was frozen, prior-art deduplication identifies it exactly as ordinary one-dimensional Weisfeiler-Leman / color refinement applied with the project-specific initial coloring `m_X(x)`.  No novelty is claimed for the refinement algorithm itself.

No collision-free or completeness claim is made for `n >= 10`.

## 1. Relabeling invariance

Let `f:X -> Y` be a Cell relabeling / graph isomorphism.

Q16/Q19 already freezes `m_X(x)` as the vector of primitive simple-cycle multiplicities through root `x`.  Isomorphism bijects simple native cycles and preserves their lengths, hence

\[
c_0^Y(f(x))=m_Y(f(x))=m_X(x)=c_0^X(x).
\]

Assume inductively that

\[
c_t^Y(f(x))=c_t^X(x)
\]

for every root.  Since `f` bijects the native neighbors of `x` with the native neighbors of `f(x)`,

\[
\multiset_{z\sim f(x)}c_t^Y(z)
=
\multiset_{y\sim x}c_t^X(y).
\]

Therefore

\[
c_{t+1}^Y(f(x))=c_{t+1}^X(x).
\]

By induction, every `c_t` is equivariant and every anonymous multiset `R_t` is relabeling-invariant.  Any deterministic stable normal form obtained from these semantic colors is therefore also relabeling-invariant.

The checker uses a finite canonical DAG compression of these recursively nested colors: raw `c_0` profiles are sorted into a legend, and at each later round the exact pair `(prior-color-id, sorted neighbor-color-ids)` is sorted into the next legend.  The legends plus final multiset are a lossless abbreviation of the semantic nested colors; no hash is used to decide color equality.

## 2. Finite stabilization bound

Let `Pi_t` be the partition of `Cell(X)` induced by equality of `c_t`.

Because `c_{t+1}(x)` contains `c_t(x)` as its first component,

\[
\Pi_{t+1}\preceq \Pi_t,
\]

so refinement never merges two previous color classes.  If the refinement is strict, the number of classes increases by at least one.  Starting from `k_0=|Pi_0|` classes and ending with at most `n` classes, there can be at most

\[
n-k_0
\]

strict refinement steps, and in particular at most `n-1`.

Once `Pi_{t+1}=Pi_t`, every root in one `Pi_t` class has the same multiset of `Pi_t` neighbor classes; applying the same update again cannot split that class.  Thus the partition remains stable thereafter.

This is a structural proof; the finite enumeration below is not used for the general stabilization bound.

## 3. `R_1` strictly contains the Q19 edge-profile packet

This gives a useful exact relation between Q19 and Q22.

Write the Q19 root profile as `P=m_X(x)`.  From `R_1` we see, for every anonymous root,

\[
\bigl(P,\ N(x)\bigr),
\qquad
N(x)=\multiset_{y\sim x}m_X(y).
\]

The Q19 root multiplicity packet `M(X)` is recovered simply by forgetting `N(x)`.

For distinct profile classes `P != Q`, the Q19 class-edge count is recovered by

\[
E_X(P,Q)
=
\sum_{x:m_X(x)=P}\operatorname{mult}_{Q}N(x).
\]

For a diagonal class,

\[
E_X(P,P)
=
\frac12
\sum_{x:m_X(x)=P}\operatorname{mult}_{P}N(x).
\]

Hence the entire Q19 packet

\[
\mathcal C(X)=(\mathcal M(X),E_X)
\]

is a deterministic function of `R_1(X)`.

Consequently every exact separation proved by Q19 through eight Cells is inherited by Q22 before any new exhaustive computation is needed.  The new computation is needed to extend the frontier to nine Cells and to freeze the exact Q22 representability image.

## 4. Mandatory Q19 nine-Cell collision repair

The Q19 equal-`C` pair is reproduced exactly.

`H_9`:

```text
01 02 04 13 15 24 26 37 38 56 78
```

`G_9`:

```text
01 04 05 14 16 23 25 26 37 38 78
```

Their anonymous `c_0` packets agree.  Q19 classified four primitive-return profile classes

\[
A=(5:1,6:1),\quad
B=(3:1),\quad
C=(3:1,6:1),\quad
D=(3:1,5:1,6:1),
\]

with common multiplicities

\[
A^3B^3C^1D^2.
\]

But the first native rootwise neighbor-profile refinement already separates them.  In `H_9`, one `A` root has neighbor-profile multiset `{A,A}`; in `G_9`, no `A` root has that multiset.  Therefore

\[
R_1(H_9)\ne R_1(G_9).
\]

The minimum partition-stabilization indices of the two witnesses are also different:

- `H_9`: `2`;
- `G_9`: `1`.

Thus Q22 performs exactly the lowest-information repair diagnosed by Q19; no two-root tuple, spectrum, zeta function, complete cycle incidence, or canonical graph label is required to repair that witness.

## 5. Exact exhaustive prefix through nine Cells

The enumeration follows the exact Q19 normalization.

If exactly `r` vertices have degree `3`, handshaking forces `r` even.  Every graph in `U_BR(n)` with that `r` admits a labeling in which the degree-`3` vertices are exactly `0,...,r-1`.  The checker exhausts every simple realization of the degree sequence

\[
3^r2^{n-r}
\]

under this normalization, rejects disconnected realizations, computes the semantic stable packet, and checks every equal-packet fiber by exact graph-isomorphism backtracking.

Therefore the normalization removes redundant label permutations but does not omit any isomorphism type.

Exact totals:

| n | degree-normalized connected realizations | isomorphism types | stable representable packets | stable collision? |
|---:|---:|---:|---:|:---|
| 4 | 2 | 2 | 2 | no |
| 5 | 13 | 3 | 3 | no |
| 6 | 178 | 10 | 10 | no |
| 7 | 1,812 | 20 | 20 | no |
| 8 | 39,492 | 59 | 59 | no |
| 9 | 525,060 | 147 | 147 | no |

Combined exact cover:

- degree-normalized connected realizations: `566,557`;
- graph-isomorphism types: `241`;
- stable packet image size: `241`.

Every equal stable-packet fiber encountered in the exact cover contains only one graph-isomorphism type.  Therefore the stable packet is injective on

\[
\mathcal U_{BR}^{\le9}
=
\bigcup_{n=4}^{9}\mathcal U_{BR}(n).
\]

This is the task's accepted terminal class

`ITERATED_REFINEMENT_INJECTIVE_AND_REPRESENTABLE_ON_EXACT_DECLARED_PREFIX`.

It is deliberately **not** upgraded to a universal reconstruction theorem.

## 6. Exact representability image

Machine artifact:

`research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_ITERATED_REFINEMENT_FRONTIER/P000_Q22_RETURN_PROFILE_ITERATED_REFINEMENT_EXACT_PREFIX_V1.json`

The artifact freezes, for every size, the exact canonical image digest and one compact metadata row per image element in the lexicographic order of the complete canonical packet serialization.  The `n` value is the surrounding image key. Each ordered row stores:

- number of degree-`3` Cells;
- minimum stabilization index;
- number of stable root-color classes.

In full mode the checker reconstructs the complete exact image by exhaustive degree-normalized enumeration, verifies its per-size whole-image SHA256, and then compares the per-object metadata row-by-row in the lexicographic order of the **complete canonical packet serialization**.  Thus the certificate includes both exact **separation** and exact **representability**, rather than an injectivity-only census.  SHA256 pins the already constructed whole image; it is never used as the equality test between two packets.

Per-size exact image SHA256:

- `n=4`: `682f52266af9a4d8ee944747c9b4bb4a3494fc4e093890353dba583206ab5efa`
- `n=5`: `c5606b5c5e8f252718e6a602add00a86394bdcab39f4bb7c93b2866929e34cd2`
- `n=6`: `15f5e8bc28cb7264bfca8359dd5cd08b934ffd75177bdb284cead1c748ed07df`
- `n=7`: `f6c9dcf76b9da113b10684f243bfb634355b8541ba6d964ef60ea342797518f7`
- `n=8`: `2dbd311eb413a2dc853c8ea350c0172cb7f5949c01e115f5b582394b92298055`
- `n=9`: `4030985011a7b14a08caa565a44165a7fdbf1a4070b8020557a531142f657844`

Combined exact image SHA256:

`9f95149157883d6253f28ba39663c93fc3aa577f9311639927b0da0862d3e1bc`

## 7. Minimum stabilization rounds for every exact-prefix object

The artifact records the value for all `241` exact image elements.  Aggregated by size, where index `t` means `Pi_t=Pi_{t+1}` for the first time:

| n | stabilization-index census over isomorphism types |
|---:|:---|
| 4 | `0:2` |
| 5 | `0:3` |
| 6 | `0:8, 1:2` |
| 7 | `0:11, 1:8, 2:1` |
| 8 | `0:29, 1:23, 2:7` |
| 9 | `0:49, 1:63, 2:33, 3:2` |

Thus the maximum exact-prefix stabilization index is only `3`, far below the structural general bound `n-1` on this family and size range.

This empirical/exhaustive statement is restricted to `U_BR(n)` for `n<=9`; the general `n-1` bound is the only universal conclusion made here.

## 8. Does the refinement become near-complete object encoding?

The exact prefix gives a useful negative answer to the immediate kill gate.

Stable root-color class counts over the `241` graph types are:

- `n=4`: classes `1:1, 2:1`;
- `n=5`: classes `2:1, 3:2`;
- `n=6`: classes `1:2, 2:4, 3:2, 4:2`;
- `n=7`: classes `3:6, 4:10, 5:3, 7:1`;
- `n=8`: classes `1:2, 2:6, 3:13, 4:9, 5:15, 6:6, 7:3, 8:5`;
- `n=9`: classes `2:3, 3:1, 4:21, 5:38, 6:34, 7:12, 8:14, 9:24`.

Only `30` of `241` stable partitions are discrete.  The other `211` retain genuine anonymous root classes of multiplicity greater than one.

Therefore the added Q22 refinement has not simply become a canonical labeling in disguise on the declared exact prefix.  It remains a local one-root relation refinement of the frozen return profile.  Its graph-level injectivity through nine Cells is a property of this restricted family, not evidence that the packet contains full adjacency in general.

The absolute information content of `c_0` is not re-litigated here: Q22 inherits the primitive-cycle multiplicity profile from Q16/Q19.  The statement is only that **the incremental repair introduced by Q22** remains the task-declared low-order local refinement rather than importing a higher-order relation or a full graph encoding.

## 9. Classical prior-art / duplication audit

This comparison was performed only after the native recurrence above was frozen.

The recurrence

\[
c_{t+1}(x)=\Bigl(c_t(x),\multiset_{y\sim x}c_t(y)\Bigr)
\]

is exactly the standard **color refinement / one-dimensional Weisfeiler-Leman (1-WL)** update on a vertex-colored graph, with the project-specific initial coloring

\[
c_0(x)=m_X(x).
\]

Relevant prior-art references include:

1. Martin Grohe, *Colour Refinement: A Simple Partitioning Algorithm with Applications From Graph Isomorphism Testing to Machine Learning*, FSTTCS 2014, DOI `10.4230/LIPIcs.FSTTCS.2014.31`.
2. Sandra Kiefer and Brendan D. McKay, *The Iteration Number of Colour Refinement*, arXiv:`2005.10182`.  Among other things, it records the general trivial `n-1` stabilization upper bound and shows that this bound is tight on unrestricted graph families.
3. V. Arvind, F. Fuhlbrück, J. Köbler, O. Verbitsky, *On Weisfeiler-Leman Invariance: Subgraph Counts and Related Graph Properties*, arXiv:`1811.04801`, using `1-WL` and classical color refinement as the same one-vertex refinement regime.

Dedup conclusion:

- **not new:** the iterative neighbor-color multiset algorithm;
- **project-specific:** initialization by native primitive-return multiplicity profiles and the exact separation/representability frontier on `U_BR(n)` through nine Cells;
- **no novelty claim:** no claim that Q22 invents 1-WL, color refinement, stable equitable partitions, or their general stabilization theory.

## 10. Enterprise tool-reuse gate

The current toolbox/method surfaces were checked after task semantics and Q19 were understood.

### `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`

Reuse resolution: `REUSE_APPLIED`.

The task already declares the observation.  T4 is used only for the exact fiber language: equal packet fibers, injective prefix, representability image, and first-collision semantics.  Its hard boundary is preserved: it does not choose or strengthen the observation.

### `T7_FINITE_SYMMETRY_EQUIVARIANCE` / `symmetry.finite_group_action`

Reuse resolution: `REUSE_APPLIED`.

It supports the relabeling/orbit viewpoint and the legitimacy of quotienting by Cell relabeling.  No canonical Cell choice, orientation, or extra carrier structure is inferred.

### `T6_OPERATION_SAFE_QUOTIENT` / `quotient.predictive_partition`

Reuse resolution: `NOT_APPLICABLE` to the actual Q22 observable construction.

Q22 fixes the neighbor-multiset recurrence explicitly; the task is not choosing an operation-safe quotient, future observation language, or coarsest predictive repair.  Importing T6 as the defining mechanism would add an abstraction not needed by the task.

### Q19 task-local exact checker frame

Reuse resolution: `REUSE_APPLIED`.

The exact degree-sequence normalization, primitive-cycle profile computation, and profile-aware graph-isomorphism backtracking are carried forward from Q19.  Q22 extends only the task-fixed rootwise iterative refinement and its representability certificate.  No new general-purpose toolbox family is created.

Method-harvest classification: `RESULT_ONLY`.

## 11. Deterministic checker

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_ITERATED_REFINEMENT_FRONTIER_CHECK_20260831.py`

The checker uses only the Python standard library.  It:

1. recomputes primitive simple-cycle multiplicity profiles;
2. computes the native iterative neighbor-profile refinement as a lossless canonical color DAG;
3. verifies the general finite stabilization invariant used by the implementation;
4. reproduces the Q19 nine-Cell pair and verifies `c_0` equality but `R_1` inequality;
5. validates all `241` compact ordered packet-metadata certificates;
6. exhausts the degree-normalized connected realization cover for `n=4..9`;
7. partitions the expensive nine-Cell degree sectors into disjoint deterministic chunks without sampling;
8. verifies every equal-packet fiber by exact graph isomorphism;
9. reconstructs the per-size and combined exact representability images;
10. verifies stabilization-index and stable-class-count censuses.

Quick frozen-certificate run:

```text
PASS P000_Q22_RETURN_PROFILE_REFINEMENT_QUICK; Q19_n9_separated_at_c1; frozen_packet_metadata=241
```

The exhaustive full run is intentionally heavier because it revisits all `566,557` degree-normalized connected realizations.  The research execution independently completed every declared `(n,r)` sector and the frozen image digests above were generated only after all equal-packet fibers had passed exact isomorphism checks.

## 12. Evidence boundary and hard-target disposition

The hard target is satisfied in the taskbook's explicitly allowed bounded-prefix terminal mode:

`P000_RETURN_PROFILE_ITERATED_REFINEMENT_STABLE_FRONTIER_EXACTLY_CLASSIFIED`

with terminal class

`ITERATED_REFINEMENT_INJECTIVE_AND_REPRESENTABLE_ON_EXACT_DECLARED_PREFIX`.

What is proved:

- relabeling invariance for all rounds;
- finite stabilization bound for every finite graph in the declared semantic recurrence;
- Q19 nine-Cell witness repaired at the first rootwise refinement;
- exact stable-packet injectivity and exact representability image on the complete declared prefix `4<=n<=9`;
- exact per-object stabilization data on that prefix;
- no near-complete-encoding kill on that prefix;
- exact prior-art deduplication to 1-WL/color refinement after native freeze.

What is **not** proved:

- no statement that `R_inf` is injective on `U_BR(n)` for `n>=10`;
- no universal graph-reconstruction theorem;
- no higher-order tuple refinement;
- no spectrum, Ihara zeta, complete cycle-incidence, or canonical-label repair;
- no Foundation, Working Truth, or canonical ontology promotion.

The next legitimate research question, if the Driver chooses to continue, is therefore a fresh countermodel-first extension beyond the exact nine-Cell prefix.  It must preserve this Q22 result and must not silently repair a future 1-WL collision inside the same task.
