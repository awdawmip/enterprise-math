# R004 precision genesis — Supplement 01: exact defects, intervention no-go, hierarchy geometry, and generic adjunction

Status: `PROVED_WIP + EXECUTABLE_CHECKED + COUNTEREXAMPLE + PRIOR_ART + PHYSICAL_HYPOTHESIS`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

This supplement records results obtained after the first R004 report. It does not change any numbered problem status and does not claim `CANONICAL_MAIN`.

## 1. Exact two-mechanism decomposition of history-collision growth

Let `n:X->N_0` be current path-history multiplicities and `R subset X x Y` a finite relation serial on occupied support. Propagate histories state-extensionally:

\[
n'(y)=\sum_{xRy}n(x).
\]

For every `k>=1`, define

\[
W_k(n)=\sum_x {n(x)\choose k}.
\]

The parent report proves `W_k(n')>=W_k(n)`. The increment has the stronger exact decomposition

\[
\boxed{W_k(n')-W_k(n)=B_k+C_k},
\]

where

\[
B_k=\sum_x(\deg_R(x)-1){n(x)\choose k}
\]

and

\[
C_k=\sum_y\left[
{\sum_{xRy}n(x)\choose k}
-\sum_{xRy}{n(x)\choose k}
\right].
\]

Both terms are nonnegative integers. `B_k` is **branch-copy growth**: a k-history bundle already sharing one current endpoint is copied to additional successors. `C_k` is **cross-source growth**: histories arriving from distinct current endpoints create new k-way coincidences at a common successor.

Thus equality is not mysterious: `W_k` is unchanged exactly when both mechanisms vanish. For `k=2`, strict growth occurs whenever an already-collided state branches, or two occupied current states acquire a common successor.

For merge excess

\[
M(n)=\sum_x\max(n(x)-1,0),
\]

there is a parallel decomposition

\[
\boxed{M(n')-M(n)=B_M+C_M},
\]

with

\[
B_M=\sum_x(\deg_R(x)-1)\max(n(x)-1,0)
\]

and

\[
C_M=\sum_y\max(p_y-1,0),
\]

where `p_y` is the number of occupied current source states incident to `y`.

This identifies two distinct finite sources of irreversibility increase rather than hiding them in one scalar.

## 2. Exact path accounting remains separate from ambient capacity

Let

\[
H=\sum_x n(x),\qquad A=\#\{x:n(x)>0\},
\]

and let

\[
B=\sum_x n(x)(\deg_R(x)-1).
\]

Then

\[
H'=H+B,
\]

and because `M=H-A`,

\[
\boxed{\Delta M=B-\Delta A}.
\]

This is the correct finite balance law produced by the toy dynamics. The ambient state capacity `|X_t|` is absent. Consequently R004 still has no theorem identifying cosmological capacity growth with thermodynamic entropy production.

## 3. Stronger generative-identifiability no-go: adaptive interventions do not suffice

The first report showed that finite deterministic towers and finite-horizon rational stochastic processes admit finite latent/pre-sampled completions. The same obstruction survives finite adaptive interventions in the classical rational-kernel setting.

Enumerate every finite context that can occur within a fixed horizon. A context may include time, previous observations, and the currently chosen intervention. Suppose each context `c` has a finite rational response distribution `K_c`.

For every context, clear denominators and make a finite uniform response table with the required outcome multiplicities. Take the Cartesian product of all local tables. One product atom assigns a deterministic response to **every possible context**, including contexts never visited in the realized run.

Sample one product atom at the initial time. An adaptive policy may choose its next intervention from earlier observed responses; at every realized context it simply reveals the already sampled coordinate for that context. The required conditional/interventional response law is reproduced exactly.

Therefore, within this finite classical rational scope:

\[
\boxed{
\text{finite adaptive intervention data}
\not\Rightarrow
\text{online ontic generation}
}
\]

without an additional restriction on admissible latent completions.

The missing ingredient is not merely an intervention syntax. Candidate restrictions must have independent content—for example locality, noncontextuality, causal-independence, bounded initial information resources, or another precisely stated condition. Which restriction is compatible with the Enterprise Math finite ontology and physically defensible is now a Foundation-level question.

This representation mechanism is prior-art-adjacent, not a novelty claim. Functional representation with independent auxiliary randomness and structural-causal intervention semantics are established tools [SRC-LI-ELGAMAL-2017-SFRL; SRC-PEARL-1995-CAUSAL-CALCULUS].

## 4. Refinement itself induces an intrinsic hierarchy geometry

The parent report correctly noted that distinguishability growth does not force an arbitrary adjacency relation. There is nevertheless one geometry that nested refinement produces canonically.

Let

\[
\lambda_0\mid\lambda_1\mid\cdots\mid\lambda_t
\]

be a finite divisibility chain and give each current fine state its compatible sequence of coarse classes. Require these equivalence relations to be nested, require one common precision-one root class, and require the final coordinate to distinguish current states.

For distinct states `x,y`, let `m(x,y)` be the finest level at which their coarse classes still agree. Define

\[
d_t(x,y)=\frac{\lambda_t}{\lambda_{m(x,y)}}.
\]

Then `d_t` is integer-valued and satisfies

\[
d_t(x,z)\le\max(d_t(x,y),d_t(y,z)).
\]

Hence nested precision signatures induce a finite **ultrametric** with no Euclidean embedding and no primitive real-valued distance.

This is a positive emergence theorem but also a warning. Hierarchical geometry is not automatically local macroscopic space.

### Shell-growth false positive

In the binary toy `(1,2,4,8)`, around state 0,

\[
|B(1)|,|B(2)|,|B(4)|,|B(8)|=1,2,4,8.
\]

A naive growth-exponent rule could read this as line-like `|B(r)|=r`. Yet the graph formed by minimum-distance pairs is only

`0--1`, `2--3`, `4--5`, `6--7`,

four disconnected sibling components.

Therefore

\[
\boxed{
\text{ball/shell growth alone}
\not\Rightarrow
\text{connected local or Euclidean-like geometry}
}.
\]

R004 needs additional cross-fiber relations if macroscopic locality is to emerge.

## 5. Task-relative effective precision horizon

A hard physical `lambda_max` remains underdetermined. But one exact operational endpoint can already be defined without pretending that physical refinement stops.

Fix a finest toy layer `X_L` and a declared future signature `sigma` on that layer. A coarser scale `lambda|L` is sufficient exactly when `sigma` is constant on every projection fiber of `p_(L->lambda)`. Define

\[
\lambda_{\mathrm{eff}}(\sigma)
=
\min\{\lambda:\sigma\text{ factors through }p_{L\to\lambda}\}.
\]

This minimum exists because the identity layer always works. At physical toy scale 8, representative future languages yield `lambda_eff=1,2,4,8`.

This is a direct consumer of the P018/P023 future-safe factorization idea. It is a **task/process-relative effective maximum**, not a universal physical minimum length.

## 6. P016 premodel: a first calibration-independent excluded region

The finite environment-record premodel declares

\[
V_{\mathrm{predicted}}=\eta V_{\mathrm{ordinary}},
\qquad 0\le V_{\mathrm{ordinary}}\le1.
\]

Therefore every realization obeys

\[
V_{\mathrm{predicted}}\le\eta.
\]

Pedalino et al. report a representative nanoparticle matter-wave visibility `V=0.10 +/- 0.01` in the stated high-mass regime [SRC-PEDALINO-2026-NANOPARTICLE]. If that published numerical range is read only as `[0.09,0.11]`, then the declared multiplicative premodel cannot reach the reported range for any

\[
\boxed{\eta<0.09}.
\]

This is only an algebraic range exclusion. It is **not** a confidence-level statement, full likelihood analysis, or validation of the model. The decisive missing map is still

`apparatus/environment variables -> finite record generator -> eta`.

Without that independent map, `eta` can be post-fit and the physical model remains too flexible.

## 7. Generic adjunction exists—but is physically non-diagnostic

The optional `1 -> universe -> 1` black-hole route was tested at the weakest categorical level.

For any finite relation `R subset X x Y`, define

\[
\exists_R(A)=\{y:\exists x\in A,\ xRy\}
\]

and

\[
\forall_R(B)=\{x:R[x]\subseteq B\}.
\]

Then the standard powerset Galois connection is

\[
\boxed{
\exists_R(A)\subseteq B
\iff
A\subseteq\forall_R(B)
}.
\]

No functionality, seriality, cosmology, metric, or causal horizon is required. The relation may be arbitrary.

Therefore merely exhibiting an adjunction of this generic kind between a refinement correspondence and a contraction/collapse correspondence supplies no special evidence for a Big-Bang/black-hole physical duality. A meaningful physical duality must include additional structure that is not free for every relation, together with an independent event-horizon/causal criterion.

## 8. Expanded executable validation

The reconstructed R004-local suite now has **43 tests**, all passing under both `unittest` and `pytest`.

The executable surface contains:

- 392 nonzero small serial-relation cases for `W_k` monotonicity;
- 735 nonzero small cases for exact collision/merge defect decomposition through `k=4`;
- the 7-versus-49 history-resurrection exhaustion;
- finite adaptive response-table completion;
- ultrametric geometry and fail-closed nesting/root checks;
- task-relative effective horizons;
- P016 premodel schema/claim guards;
- all 256 adjunction instances formed from every `2 x 2` finite relation and all source/target subset pairs.

Across the six R004 `precision_*` modules there are zero true-division operators and zero floating-point literals.

These are `EXECUTABLE_CHECKED` regressions, not theorem certificates. No Lean status is claimed: the current runtime does not expose a Lean toolchain, so R004 did not add uncompiled formalization merely to satisfy a checkbox.

## 9. Revised research frontier

After these results, the main unknown is sharper than at the start of R004.

The difficult question is no longer whether one can draw a finite refinement universe. One can. Nor is it whether branching and irreversible history merge can coexist. They can, with exact integer accounting.

The decisive open question is:

> **What independently motivated finite structural restriction prevents the complete latent/pre-sampled completion, while also producing connected/local geometry and a predeclared P016 observable?**

Without such a restriction, “new distinguishability is genuinely created” remains interpretation. With one, the project would have a concrete theorem/experiment interface capable of moving the precision-opening idea beyond a finite re-description of hidden variables.
