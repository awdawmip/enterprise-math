# Causal Absorption 01 — Deriving Linear Algebra, Depth Geometry, and Topology from Future Distinguishability

Status: `CROSS-ROUTE RESEARCH WIP / EXACT INTEGER THEOREMS + EXECUTABLE REFERENCE`

Ownership note: this document is authored on the A3 owner branch as an experiment and proof source. General future-compatible quotient theory remains owned by A2/P023. Any theorem that survives without A3-specific assumptions should be relayed upward rather than maintained as a duplicate mother theory.

## 1. Goal

Reject the pattern:

> traditional linear space / metric / topology first, then attach a `precision` label.

Instead:

1. explicit integer states are primitive;
2. allowed future operations are declared;
3. actual integer observations are declared;
4. ask which state differences any allowed finite future can still distinguish;
5. only after stabilization may traditional `kernel / rank / observability / ultrametric / topology` language appear as derived compression.

Traditional tools become causal shadows rather than foundations.

## 2. Primitive system

State:

\[
X=\mathbb Z^k.
\]

Finite operation family:

\[
\mathcal B=\{B_a\},\qquad B_a\in\mathbb Z^{k\times k}.
\]

Integer observation map:

\[
W:\mathbb Z^k\to\mathbb Z^r.
\]

For an operation word `omega`, write `B_omega` for the corresponding integer matrix product.

## 3. CA-01 — Depth-t causally invisible subgroup

Define

\[
K_t
=
\{\eta\in\mathbb Z^k:
WB_\omega\eta=0
\text{ for every }|\omega|\le t\}.
\]

Then

\[
x\sim_t y\iff y-x\in K_t.
\]

Interpretation: not "error below epsilon", but exact equality under every allowed future experiment up to depth `t`.

Immediately,

\[
K_{t+1}\subseteq K_t.
\]

Longer futures can refine distinguishability but cannot re-merge an already visible distinction.

## 4. CA-02 — Pulling future observations back to the present

Let `V_t` be the rational row span of all

\[
wB_\omega,
\qquad |\omega|\le t.
\]

Then

\[
\boxed{K_t=\mathbb Z^k\cap V_t^\perp.}
\]

Row span and kernel are therefore exact computational compressions of causal distinguishability, not primitive ontology.

If

\[
V_{t+1}=V_t,
\]

then `V_t` is invariant under every declared right action `v -> v B_a`, so no later operation word can add a new observation direction. Hence

\[
\boxed{V_{t+1}=V_t\Longrightarrow K_{t+j}=K_t\quad\forall j\ge0.}
\]

## 5. CA-03 — Finite stabilization on an infinite integer state space

Every `K_t` is a saturated subgroup of `Z^k`: if `n eta in K_t` with nonzero integer `n`, integer linearity forces `eta in K_t`.

If

\[
K_{t+1}\subsetneq K_t,
\]

then two saturated subgroups cannot have the same rank; equal rank would give the same rational span, and saturation of the smaller subgroup would force equality.

Therefore every strict refinement lowers invisible rank by at least one:

\[
\boxed{\text{number of strict future refinements}\le k.}
\]

The state space is infinite, yet the causal distinguishability closure stabilizes through finite integer rank, not through a state box or continuous limit.

## 6. CA-04 — Causal dimension absorbs traditional rank

After stabilization define

\[
K_*=\bigcap_{t\ge0}K_t.
\]

Then

\[
\boxed{
\dim_{causal}(X;\mathcal B,W)
=
\operatorname{rank}(\mathbb Z^k/K_*).
}
\]

Equivalently this is the stable future-visible row rank.

Interpretation:

> causal dimension is the number of independent integer freedoms that the declared future language can eventually distinguish.

Ambient coordinate count need not equal effective dimension. Traditional rank is demoted to a theorem about the stabilized causal structure.

## 7. CA-05 — Observability matrix as a shadow

Traditional linear-systems mathematics may stack

\[
W,\ WB,\ WB^2,\ldots
\]

into an observability matrix.

Here the matrix is not the starting object. The primitive question is whether any allowed future can distinguish two states. The matrix is only a finite coordinate table for those pulled-back future experiments.

Thus

\[
\boxed{
\text{observability rank}
=
\text{causal distinguishability rank}.
}
\]

## 8. CA-06 — Integer causal agreement depth

Do not start from a metric. Define

\[
s(x,y)=\min\{t:x\not\sim_t y\},
\]

and set `s(x,y)=infinity` when the states remain future-equivalent forever.

Because every `~_t` is an equivalence relation,

\[
\boxed{s(x,z)\ge\min(s(x,y),s(y,z)).}
\]

This is an integer non-Archimedean similarity law. A conventional real ultrametric, if desired, is only a monotone numerical recoding of `s`.

## 9. CA-07 — The future filtration generates topology

For every depth `t` and state `x`, define

\[
U_t(x)=[x]_{\sim_t}.
\]

The nested equivalence relations make the family

\[
\mathcal B_{causal}=\{U_t(x)\}
\]

a topology basis: any two intersecting basis classes are ordered by refinement. Every basis class is clopen because its complement is a union of other classes at the same depth.

Thus neighborhood acquires a causal meaning:

> states still indistinguishable from `x` at some finite future depth.

## 10. CA-08 — The T0 quotient is the stable future quotient

Two states have the same complete family of causal-depth neighborhoods iff

\[
x\sim_t y\quad\forall t,
\]

which is stable future equivalence. Therefore the Kolmogorov/T0 quotient of the causal-depth topology is exactly

\[
\boxed{X/\sim_*}.
\]

In the integer-linear setting this is

\[
\boxed{\mathbb Z^k/K_*}.
\]

T0 separation is therefore not an extra axiom in this regime; it is what remains after permanently future-indistinguishable states are collapsed.

## 11. Relation to P012

P012 already demonstrates one successful absorption pattern:

\[
d_G(x,y)=\text{shortest integer length of a primitive operation path}.
\]

`L1` is a closed form derived from one standard generator family, not an a priori norm.

The current document supplies a different causal geometry:

- P012 word/path cost asks how many primitive operations move `x` to `y`;
- agreement depth asks how deep the future must be before `x` and `y` become distinguishable.

They are currently `COMPOSABLE_INDEPENDENT`; do not merge them into one metric without a theorem.

## 12. Absorption standard

A traditional tool enters core only if at least one holds:

1. **Causal derivation** — exact derivation from state + operations + future observations.
2. **Shadow theorem** — it is a special-regime closed form of an Enterprise Math object.
3. **Compression only** — it is merely an algorithm or coordinate representation.
4. **Failure boundary** — if it requires hidden continuum completion or external precision axioms, keep it as comparison tooling.

Current status:

- kernel/rank/observability: passes 1/2/3;
- ultrametric: passes 2/3, with integer agreement depth kept primitive;
- topology: passes 1/2;
- P012 graph metric / L1: passes 1/2/3;
- general Euclidean norm: not absorbed.

## 13. Executable reference

Added:

- `src/enterprise_math/causal_future_module.py`;
- `tests/test_causal_future_module.py`.

Coverage includes multi-operation future-visible closure, exact integer rank, finite rank stabilization on infinite `Z^k`, future indistinguishability, first distinguishing depth, depth-equivalence transitivity, and the strong similarity law.

## 14. Prior-art discipline

Traditional linear observability, automata future equivalence, ultrametric filtrations, and zero-dimensional/clopen topologies all have established prior art. Enterprise Math does not claim those general theories as inventions.

The research claim to test is narrower:

> **Can causal distinguishability be made primitive so that traditional algebraic, metric-like, and topological tools become shadows of one finite future filtration, rather than a traditional substrate decorated with precision annotations?**

Formal novelty claims remain unverified.

## 15. Next

1. Compare `dim_causal` with A3 relation rank and guard-quotient free rank and identify exact coincidence conditions.
2. Absorb traditional basis as a minimal future-probe generator rather than a preselected coordinate frame.
3. Absorb norm as a closed form of translation-invariant causal word cost.
4. Pressure-test which topological properties cannot be represented by a finite future filtration.
5. Relay general results to A2/P023 and geometry consequences to P012/A5.
