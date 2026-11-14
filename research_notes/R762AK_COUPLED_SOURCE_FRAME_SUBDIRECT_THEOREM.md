# R762AK — Exact coupled source/frame subgroup rigidity and BRC provenance

**Status:** Author-side CONDITIONAL theorem with finite exhaustive verification; NOT_REVIEWED / NOT_NATIVE_ADMITTED.
**Task:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`.
**Frozen scientific pins:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, including `p000_reality_foundation.json`, `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, and `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`.
**Reused results:** R762AG (#2395), R762AI (#2405), R762AJ (#2410), and the prior independent `research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md`. The new result addresses AJ4's coupled-source/frame question without assuming independently selectable primitives.

## 1. Typed finite model and observer

Source placement `s` takes values in `A=C3=A3`, the even three-source permutations, or hypothetically in `A=S3` if an odd source-moving operation is actually enabled. Active frame holonomy `h` takes values in `B=S3`, following the *conditional* V17 three-slot frame carrier. The two fields are separately typed. Permutation multiplication is composition `(pq)(i)=p(q(i))`.

Each declared event `j` has a fixed `g_j=(a_j,b_j) in A x B` and acts by **total state-independent reversible** left multiplication `(s,h)->g_j(s,h)`. The physically paired events need not contain independent source-only or frame-only primitives. Let `H=<g_j>` be their generated subgroup; as a finite group it is exactly the forward-reachable set from `(1,1)` because powers of generators also produce their inverses. The observer reports **both** permutation cycle types `Obs(s,h)=(type(s),type(h))`, with identity `E` distinguished in each component.

**Marginal surjectivity**, whenever used, is an explicit hypothesis: `pr_source(H)=A` and `pr_frame(H)=S3`. P000 and V17 alone do not supply the paired native event alphabet or establish either marginal. If real events have state-dependent enablement, partial actions, noninvertible updates, or changing signed X6 fibers, use the actual typed transition graph instead of this group-action model.

## 2. AK1 — Cyclic source / full frame: compulsory full product

**Theorem.** Any subgroup `H <= C3 x S3` with both marginal projections surjective is the **entire** `C3 x S3`. Consequently exactly **18** joint states and **5 fixed binary bits** are necessary and sufficient for the declared future observer. No independent primitive event types are required.

**Proof.** Put `K={a in C3:(a,1) in H}`. Since `|C3|=3`, either `K=C3` or `K={1}`. In the first case, any `b in S3` has some `(a,b) in H`; multiplying by `(a^-1,1) in H` yields `(1,b) in H`. Thus `H=C3 x S3`. In the second case, the map `H->S3` is injective and surjective, so `H` is the graph of a surjective homomorphism `phi:S3->C3`. Every transposition has order 2 and maps to identity in `C3`; transpositions generate `S3`. Hence `phi` is trivial, contradiction. QED.

**Sharp hypothesis witness:** if the frame projection is only `C3` rather than all `S3`, the diagonal `{(c^r,c^r):r=0,1,2}` has three states and both cyclic marginals. Testing complete odd *frame* holonomy reachability is decisive.

## 3. AK2 — Full S3 source / full S3 frame: exactly three carrier sizes

**Theorem.** For any `H <= S3 x S3` surjective onto *each* factor, precisely one of the following holds:

| Coupling | Joint group | Cardinality | Minimal fixed binary bits |
|---|---|---:|---:|
| Free joint product | `S3 x S3` | 36 | 6 |
| Parity-locked | `{(s,h):sgn(s)=sgn(h)}` | 18 | 5 |
| Automorphism-locked | `{(s,phi(s)):s in S3}` | 6 | 3 |

There are six distinct automorphism-locked graphs, one for each `phi in Aut(S3)`; thus exactly **eight** subdirect subgroups in total.

**Proof.** Define `N1={s:(s,1) in H}`, `N2={h:(1,h) in H}`. Both are normal because both projections are onto. The relation on cosets induced by `(s,h) in H` defines an isomorphism `S3/N1 ≅ S3/N2` (if two pairs have the same first entry, their second entries differ by an element of `N2`, and vice versa). The normal subgroups of `S3` are exactly `{1},A3,S3`, with quotients `S3,C2,{1}` respectively. Hence both kernels are the corresponding unique matching subgroup. The trivial quotient yields the full product; the `C2` quotient is exactly the shared sign character, giving parity-locked pairs; the `S3` quotient gives the graph of an automorphism. Every automorphism sends the three transpositions bijectively to themselves, and all six possibilities are realized by conjugation in `S3`. QED.

In particular, a real source-moving *odd* permutation (different from a passive V17 frame flip), if it exists, forces a new classification question: is the paired state graph a six-state automorphism graph, the 18-state parity fiber, or the full 36-state product?

## 4. AK3 — Future-safe residual despite inseparable coupled events

**Theorem.** For *any* finite generated paired subgroup `H` as above, the observer `Obs=(source cycle type, frame cycle type)` distinguishes **every two different states** by some future word over the coupled event alphabet. Its exact future-safe state cardinality is `|H|`, needing `ceil(log2 |H|)` fixed bits.

**Proof.** Given `x≠y` in `H`, a forward event word represents `x^-1` (finite subgroup). Applied to both states, it produces `(1,1)` and `x^-1 y≠(1,1)`. Only the former has joint cycle-type readout `(E,E)`. Hence no two states may be merged in a quotient safe for *all* permitted future words; storing `x in H` itself is sufficient. QED.

This removes AJ4's independent-future-control hypothesis **for the declared total paired-action model**: even individually entangled source/frame events can produce a fully distinguishing language.

### Positive BRC weighted histories and correlation loss

For an event alphabet `J` with exact nonnegative rational weights `w_j`, the positive BRC group-ring state distribution has

`W_0(1)=1; W_0(x≠1)=0; W_(k+1)(x)=Σ_(j∈J) w_j W_k(g_j^-1 x)`.

Its total mass is exactly `(Σ_j w_j)^k`, with state dimension `|H|`. Marginal source and frame distributions alone need not determine the joint BRC history. The equally weighted joint supports `{(1,1),(c,c)}` and `{(1,c),(c,1)}` have identical marginals but different source/frame correlations; preserve the typed joint direction until an observer- and future-safe quotient certificate exists. Positive BRC mass is not a signed-force cancellation law.

## 5. Exact integer verification

`R762AK_COUPLED_SOURCE_FRAME_VERIFY.py` exhaustively enumerates *all subgroups* by repeated adjoining and closure from the identity subgroup, independent of the proof classification. Its generated JSON reports:

* `C3 x S3`: **14** total subgroups; **one** subdirect of size 18; all **153** unordered distinct reachable-state pairs future distinguishable.
* `S3 x S3`: **60** total subgroups; **eight** subdirects, with orders `6×6, 18×1, 36×1`; all **873** unordered distinct-state pairs across those eight subdirects future distinguishable.
* A nontrivial parity-locked 18-state subgroup generated by three paired events, with weights `2,3,5`: exact positive integer recurrence equals independently enumerated ordered words for `k=0..7`, with total mass `10^k`.
* Two explicit joint distributions with equal individual marginals and distinct joint correlation.

All checker operations are exact integer arithmetic and finite complete enumeration. See adjacent `R762AK_COUPLED_SOURCE_FRAME_EVIDENCE.json`.

## 6. Discriminating next native experiment

For each proposed P000-compatible `TRIADIC_CLOSURE_E` macro-event and its V29 PASS/TRANSFER, V17 frame and V39 return transports, record `{signed_X6_port,source_slot_action,frame_action,enablement,ordered_time,observer,provenance}`. Determine whether actions are actually total, fixed and reversible on one source-typed signed-fiber. If yes, form their paired generators and compute both marginal projection groups. The two theorems then give an exact carrier classification. If the native event system instead has partial enabling, calculate future-observer equivalence on the corresponding labeled transition system.

**Scientific status:** These results are author-checked conditional finite group theorems; no native-force event legitimacy, formal Source Result, independent Driver review or P000 modification is inferred.
