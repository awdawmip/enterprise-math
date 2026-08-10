# R004 precision genesis — Supplement 14: mixed typed fixed-point dispatcher and generator descent

Status: `PROVED_WIP + EXECUTABLE_CHECKED + CORRECTION + PRIOR_ART_SPECIALIZATION + P023/A3/A4_BOUNDARY`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_13.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 13 correctly established quotient-relative relation stabilization, semantic factor order and relation activation cascades, but its comparison sentence about total operations was too broad. The valid raw-meet statement is scoped to **one fixed operation family while observations vary**. Distinct operation families can activate one another and can require arbitrarily many alternating repairs. This supplement records that correction and replaces the operation/relation dichotomy by one mixed typed fixed-point interface.

## 1. R004-COMP-CORR-01 — fixed algebra meet law, not universal operation meet law

Fix one total finitary algebra `A` on `X`. For an observation partition `P`, let `C_A(P)` be the coarsest `A`-congruence refining `P`.

For any observation partitions `P,Q`,

`C_A(P meet_raw Q) = C_A(P) meet_raw C_A(Q)`.

Proof: both `C_A(P)` and `C_A(Q)` are congruences for the **same** algebra, so their intersection is again an `A`-congruence refining `P intersect Q`. Conversely any `A`-congruence refining `P intersect Q` refines both largest compatible congruences.

Independent finite checking covered every unary operation and every partition pair for carriers of size `2,3,4`: **58,291** cases, zero violations.

This theorem does **not** say that quotients compiled for different operation languages may be raw-intersected once and declared jointly stable.

## 2. R004-COMP-CE13 — different total operations cross-activate

On `X={0,1,2,3}`, let

`f=(0,0,0,1)`, `g=(0,0,3,0)`

and initial partition

`P_0={{0,2,3},{1}}`.

Compiling `f` alone gives

`P_f={{0,2},{1},{3}}`.

Compiling `g` alone leaves `P_0` unchanged. Their raw common refinement is therefore `P_f`.

But `P_f` is not `g`-stable: `0` and `2` are still together while `g(0)=0` and `g(2)=3` now lie in different target blocks. The joint compiler must split again and reaches the discrete partition.

Exhaustive search over all unary-total-operation pairs and all initial partitions for `|X|<=3` checked **3,677** cases and found no such failure, so four states are minimal in that bounded class.

## 3. R004-COMP-T15 — arbitrary-length operation ping-pong

The previous counterexample is not an isolated finite accident.

For every `n>=3`, take

`X_n={0,1,...,n-1}`,

`P_0={{0},{1,...,n-1}}`.

Define two unary total operations by

`f(0)=g(0)=0`,

`f(k)=k-1` for odd `k`, otherwise `f(k)=k`,

`g(k)=k-1` for positive even `k`, otherwise `g(k)=k`.

Starting from `P_0`, exact closure under `f` isolates state `1`; exact closure under `g` then isolates `2`; the next `f` closure isolates `3`; and so on. After `t` strict activations the partition is

`{{0},{1},...,{t},{t+1,...,n-1}}`.

Hence exactly

`n-2 = |X|-|P_0|`

strict cross-language refinements are required before the discrete partition is reached.

Therefore no state-size-independent rule such as “compile each operation language once” or “two passes suffice” can replace a common fixed point. The elementary block-count termination bound is sharp.

## 4. R004-COMP-T16 — unified mixed typed signature

Generic finitary operation-to-unary-context compilation already belongs upstream to A2/P023. R004 therefore consumes finite unary context families rather than duplicating that theorem.

For a current partition `P`, a mixed typed language may contain:

1. total unary contexts `f:X->X`;
2. partial unary contexts `g:D_g subset X -> X`, with enabledness part of the future semantics;
3. quotient-relative relation channels `c` with commutative-monoid block aggregation.

Define the state signature

`S_P(x) = ([x]_P, ([f(x)]_P)_f, (tag_g(x))_g, (Sigma_(c,P)(x,B))_(c,B in P))`,

where

`tag_g(x)=disabled` if `x` is outside the partial domain, and

`tag_g(x)=(enabled,[g(x)]_P)` otherwise.

One mixed refinement step is simply

`P^+ = ker S_P`.

The current-class component guarantees that `P^+` only refines `P`.

## 5. R004-COMP-T17 — unique coarsest mixed fixed point

Iterate

`P_(r+1)=ker S_(P_r)`

from an initial observation partition `P_0`.

Every strict step increases the block count, hence termination occurs after at most

`|X|-|P_0|`

strict steps.

The terminal partition `P_*` is exactly the **unique coarsest refinement of `P_0` satisfying all declared typed obligations simultaneously**.

Proof. Let `Q` be any jointly stable refinement of `P_0`. Inductively suppose `Q` refines `P_r`.

- total-operation stability in `Q` implies equal `Q` output classes, hence equal coarser `P_r` output classes;
- partial-operation stability gives equal enabledness and, when enabled, equal `Q` output classes;
- every `P_r` target block is a disjoint union of `Q` target blocks, so equality of monoid aggregates on all `Q` blocks implies equality on each `P_r` block.

Thus any two states identified by `Q` have identical `S_(P_r)` signatures and remain identified by `P_(r+1)`. Therefore `Q` refines every `P_r` and hence refines `P_*`.

This is the mixed semantic form of the coarsest-safe-refinement principle. The generic fixed-point/partition-refinement mathematics is prior art; the project value is the typed P023/A3/A4 interface and its exact finite specializations.

## 6. R004-COMP-T18 — modular closure/worklist theorem

Let each typed sublanguage `L_i` expose its own coarsest-refinement closure operator `C_i` on finite partitions. Each `C_i` is refinement-extensive, monotone and idempotent.

Any fair iteration

`P <- C_i(P)`

that keeps re-queueing semantic domains after a strict refinement reaches the same least common fixed point, independent of fair scheduling.

Reason: the partition chain can strictly refine only finitely many times. At termination of a fair schedule every `C_i` fixes the result. Conversely the least common fixed point bounds every intermediate iterate by monotonicity, so the terminal common fixed point is the coarsest one above the initial observation.

For the full three-state family combining one total unary operation, one partial unary operation and one COUNT relation channel, all six cyclic domain orders were compared with the simultaneous compiler on **552,960** cases; all agreed.

This theorem justifies a modular dispatcher that reuses owner compilers instead of constructing one monolithic P023/A3/A4 engine.

## 7. R004-COMP-T19 — partial legality totalization

For a partial unary operation `g`, adjoin one distinguished state `bottom` and define

`g_hat(x)=bottom` when `g(x)` is undefined, otherwise `g_hat(x)=g(x)`,

with `g_hat(bottom)=bottom`.

Lift any partition `P` by keeping `bottom` in its own class.

Then `P` has representative-independent partial-operation enabledness and enabled output classes iff the lifted partition is compatible with `g_hat`.

Thus legality is not a second independent precision primitive: at the quotient-compatibility layer it is a tagged deterministic output.

This totalization is used only as a compatibility device. It does **not** claim that arbitrary algebraic identities of a partial algebra are preserved by one-point extension.

All **320** partial-unary/partition cases on three states were checked exhaustively.

## 8. R004-COMP-T20 — stable semiring relations form a subsemiring

Suppose relation weights lie in a semiring `K`. A matrix `R in K^(X x X)` is `P`-stable when for every source block `A`, target block `B`,

`sum_(y in B) R(x,y)`

depends only on `A=[x]_P`. Write the well-defined quotient matrix as `R_bar`.

Then the set of all `P`-stable matrices contains `0` and `I`, is closed under `+` and matrix multiplication, and

`R -> R_bar`

is a semiring homomorphism:

`overline(R+S)=R_bar+S_bar`,

`overline(RS)=R_bar S_bar`.

For multiplication,

`sum_(z in C) (RS)(x,z)`

`= sum_B (sum_(y in B) R(x,y)) S_bar(B,C)`

`= sum_B R_bar(A,B) S_bar(B,C)`.

Consequently the compiler needs to stabilize relation **generators**, not every finite path expression generated from them.

Three-state `N_0` path-count matrices supplied **4,964** stable matrix-pair checks of product closure and quotient multiplication, all exact.

## 9. R004-COMP-T21 — MAY path lifting and finite reachability

The Boolean semiring specializes the previous theorem to MAY semantics.

If relation generators are block-MAY stable, every finite relation composition descends exactly. In particular, for stable `S`,

`overline(R ; S) = R_bar ; S_bar`

whenever `R` is also represented on the quotient; more generally a coarse path can be lifted one intermediate block at a time because every member of a stable intermediate block has the same outgoing block-support word.

Without stability, fake witness stitching occurs. On two states in one coarse block, let `R` have only `0->0` and `S` only `1->1`. Both coarse relations are nonempty, so coarse composition claims a path, but the fine composition is empty.

Exhaustive three-state checks:

- all two-step cases with the required downstream MAY stability: **8,960**, zero failures;
- all three-step cases with stable downstream generators: **361,472**, zero failures;
- all stable Boolean one-relation cases for reflexive-transitive reachability: **140**, zero failures.

Thus one-step stabilization can certify an unbounded finite reachability syntax in the Boolean finite-state setting.

## 10. R004-COMP-T22 — finite typed generator basis

The mixed compiler can now separate **carrier synthesis** from **future syntax closure**.

For a finite declared generator basis:

- compatible total operation generators imply all ordinary algebraic terms descend;
- compatible partial-operation generators imply definedness/value descent inductively for generated partial terms;
- stable semiring relation generators imply every finite semiring polynomial in those matrices descends through the quotient homomorphism.

Therefore an infinite family of future expressions need not be enumerated if it is generated algebraically by a finite typed basis and the compiler emits the relevant homomorphism/descent certificate.

This is the strongest current form of the R004 Representation Compiler contract:

`Exact Carrier + Typed Generator Basis + Initial Observation`

`-> least common safe fixed point`

`-> descended generator tables / quotient matrices`

`-> algebraic closure certificates for the requested future syntax`.

## 11. Validation

Independent research enumeration, separate from the committed direct regression file, checked the mixed fixed-point theorem on every three-state combination of:

- one total unary operation;
- one partial unary operation;
- one loopless binary relation;
- every initial partition.

For each of COUNT, MAY and MUST relation aggregation there were **552,960** cases and zero coarsest-partition oracle mismatches.

Additional exact checks are listed above: 58,291 fixed-operation observation-meet cases; 3,677 small different-operation raw-meet searches; 320 partial-totalization cases; 4,964 semiring-product cases; 8,960 two-step MAY path cases; 361,472 three-step MAY path cases; and 140 Boolean reachability cases.

The candidate `precision_mixed_typed_dispatcher.py` direct regression file has seven `unittest` tests and passes in the available private Python environment. No fresh full-repository CI or canonical-main status is claimed.

## 12. Prior-art and ownership boundary

Generic fixed-point iteration, congruence closure, partial-algebra congruence, equitable/balanced partitions, weighted/semiring transition systems, weighted bisimulation, quotient matrices, coalgebraic partition refinement and modular combinations of transition types are prior mathematics.

In particular, existing coalgebraic partition-refinement work already covers weighted systems and modular combinations of system types; R004 must not claim a generic mixed partition-refinement algorithm as a new invention.

The R004 addition remains a project-local synthesis:

1. correct the over-broad operation/relation dichotomy by an explicit different-operation activation family;
2. express P023/A3/A4 obligations through one finite typed-signature fixed point without seizing mother ownership;
3. make legality and relation composition explicit typed descent certificates;
4. separate finite generator compilation from potentially infinite future syntax;
5. preserve an integer/fractionless internal representation throughout these finite compilers.

Historical novelty of this packaging remains `NOVELTY_UNVERIFIED`.

## 13. Next frontier

The next unresolved object is not another refinement engine. It is **minimal typed generator synthesis**:

> Given a large declared future language, which finite subset of operation contexts, legality probes, relation channels and witness semantics is sufficient to generate exactly the same safe carrier and descended future algebra?

Semantic factor maps can already delete some dominated channels (COUNT or LABEL-SET can dominate MAY), but a complete minimal-basis compiler must also recognize algebraic generation and cross-domain redundancy without solving a harder problem than the future language itself.

That question belongs at the P023/A3/A4 interface; R004 should continue supplying finite theorems, no-go examples and executable reductions.
