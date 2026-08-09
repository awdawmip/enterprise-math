# P023 — Incidence Repair Monotonicity, Supplement 10

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023, with A4 finite-relation input  
Depends on: P023-S8 image separation, P023-S9 minimal repair cardinality, A4 admissible relations  
Discipline: finite relations, quotient maps, degrees, and monotonicity under inclusion are established mathematics. The project role is to make them a common precision/admissibility interface.

## 1. Setup

Let

\[
R\subseteq I\times X
\]

be a finite nonempty incidence relation. Think of `i in I` as a shell/factor/mode label and `x in X` as the detailed state actually related to that label.

Let

\[
g:X\to Y
\]

be the retained observation.

The task keeps `g(x)` but still wants to recover the realized label `i`.

## 2. Observed incidence relation

Push the relation through the retained observation:

\[
\boxed{
\bar R_g
=
\{(i,y):\exists x,\ (i,x)\in R,\ g(x)=y\}.
}
\]

For each retained observation `y`, define its realized label set

\[
L_{R,g}(y)
=
\{i:(i,y)\in\bar R_g\}
\]

and local label multiplicity

\[
m_{R,g}(y)=|L_{R,g}(y)|.
\]

Define the worst local burden

\[
\boxed{
M(R,g)=\max_{y\in\operatorname{im}g}m_{R,g}(y),
}
\]

where only observation values reached by `R` matter.

## 3. P023-S10-T01 — Incidence degree equals minimum repair alphabet

Status: `PROVED`.

On the tagged state space `R`, take the coarse state to be

\[
(i,x)\mapsto g(x)
\]

and the target state to be

\[
(i,x)\mapsto(g(x),i).
\]

Then the exact minimum alphabet of any extra repair coordinate is

\[
\boxed{
R_{\min}(R,g)=M(R,g).
}
\]

### Proof

One coarse fiber at retained value `y` contains exactly the distinct target label blocks indexed by

\[
L_{R,g}(y).
\]

Hence its split multiplicity is `m_{R,g}(y)`. P023-S9-T03 says the globally minimal repair alphabet is the maximum local split multiplicity over all coarse fibers. Therefore it is exactly `M(R,g)`. ∎

Equivalently, `M(R,g)` is the maximum degree on the observation side of the finite bipartite relation `bar R_g`.

## 4. P023-S10-T02 — Relation enlargement monotonicity

Status: `PROVED`.

If

\[
R\subseteq R',
\]

then for every fixed observation `g`,

\[
\boxed{
M(R,g)\le M(R',g).
}
\]

### Proof

For every `y`,

\[
L_{R,g}(y)\subseteq L_{R',g}(y),
\]

so each local label multiplicity can only increase or remain unchanged. Taking maxima proves the claim. ∎

Thus enlarging an admissible state relation can only increase the shell/label repair burden.

## 5. P023-S10-T03 — Observation coarsening monotonicity

Status: `PROVED`.

Suppose a coarser retained observation `h:X->Z` factors through `g`:

\[
\boxed{h=\phi\circ g}
\]

on all states used by `R`.

Then

\[
\boxed{
M(R,g)\le M(R,h).
}
\]

### Proof

For each fine observation value `y`, every label realized at `y` is also realized at the coarse value `phi(y)`. Hence

\[
L_{R,g}(y)
\subseteq
L_{R,h}(\phi(y)).
\]

The maximum label multiplicity cannot decrease after observation fibers are merged. ∎

Therefore making the retained coordinate coarser can never reduce the extra alphabet needed to recover an unchanged label task.

## 6. P023-S10-T04 — Joint precision/admissibility monotonicity

Status: `PROVED`.

If

\[
R\subseteq R'
\]

and

\[
h=\phi\circ g,
\]

then

\[
\boxed{
M(R,g)\le M(R',h).
}
\]

This follows by T02 and T03.

It gives a two-axis order law:

\[
\boxed{
\text{stricter realizability}
+
\text{finer retained observation}
\Longrightarrow
\text{repair burden cannot increase}.
}
\]

Conversely, relation enlargement and observation coarsening are both conservative operations that may manufacture extra ambiguity.

## 7. P023-S10-T05 — Image separation is the alphabet-one endpoint

Status: `PROVED`.

The shell label is already a function of the retained observation exactly when

\[
\boxed{M(R,g)=1.}
\]

### Proof

A decoder exists exactly when every reached observation value is incident to at most one distinct label. Since every reached value has at least one label, this is exactly maximum observation-side degree one. ∎

Thus P023-S8 is the zero-extra-repair endpoint of the quantitative S9/S10 calculus.

## 8. One-way logic for envelopes

Let `R_actual subset R_envelope`.

T02 gives

\[
M(R_{actual},g)\le M(R_{envelope},g).
\]

Therefore:

- if the **envelope** has `M=1`, then the actual relation certainly has `M=1`;
- if the **actual relation** has `M>1`, then the envelope certainly has a collision;
- but an envelope collision `M>1` does **not** imply an actual collision.

This is the precise logical form of

\[
\boxed{
\text{over-approximation can certify separation,
not realized collision}.
}
\]

## 9. P017 k=6 as the minimal self-correction witness

For the lower-band `p=2,3` raw quotient windows at `k=6`, root observation produces a raw overlap at root 4, so

\[
M(R_{window},R_2)=2.
\]

But the conflicting `p=3,q=16` state is not 3-rough: `3*16=48` has least prime factor 2. After applying the actual least-prime admissibility relation,

\[
\boxed{M(R_{shell},R_2)=1.}
\]

This is exactly the semantic correction discovered while pushing P017 L056: the exact interval envelope was still larger than the realized shell relation.

## 10. Precision interpretation

The theorem separates three independent choices:

1. the admissible relation `R` — which tagged states can actually occur;
2. the retained observation `g` — which state coordinate survives;
3. the target label task — which distinctions must still be recoverable.

The repair burden is not an intrinsic property of any one of these objects in isolation. It is

\[
\boxed{
M(R,g;\text{label task}).
}
\]

This is a relation-theoretic form of task-relative precision.

## 11. Executable specification

- `src/enterprise_math/incidence_repair.py`
- `tests/test_incidence_repair.py`

The tests compare the degree formula with the generic P023-S9 minimal-repair compiler, verify strict examples on both monotonicity axes, recover S8 as the alphabet-one case, and pin the P017 `k=6` raw-envelope versus realized-shell correction.

## 12. Ownership boundary

A4 owns generic finite relation/composition/support structure. P023 owns future-safe quotient and repair semantics. This supplement is the bridge: it consumes an A4-style relation and computes the A2/P023 label-recovery precision burden.

No new generic relation algebra is claimed here.
