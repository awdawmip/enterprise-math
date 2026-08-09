# P011 — Provenance Repair Spectrum Bridge

Status: `PROVED RESEARCH NOTE`  
Owner: P011 irreversibility spectrum, consuming P023-S9/S10 repair semantics  
Scope: finite deterministic maps  
Discipline: this is a mathematical reconstruction-cost interpretation. It does not assert that a many-to-one physical process stores or can physically recover discarded histories.

## 1. Two views of the same fiber

Let

\[
F:X\to Y
\]

be a map from a finite nonempty state set `X`, with `|X|=N`.

P011 writes the size of a nonempty fiber as

\[
m_F(y)=|F^{-1}(y)|.
\]

Now ask a P023-style task question:

> retain only the future state `F(x)`, but require exact recovery of the original state label `x`.

For one reached output `y`, all states in `F^{-1}(y)` share the same retained value and must receive distinct repair symbols.

This identifies P011 history merging and P023 repair complexity on the same partition.

## 2. P011-RS-T01 — Local provenance repair equals fiber multiplicity

Status: `PROVED`.

Let `r_F(y)` be the minimum number of repair symbols required on output fiber `y` to recover the original state label. Then

\[
\boxed{
r_F(y)=m_F(y)=|F^{-1}(y)|.
}
\]

### Proof

Necessity: the `m_F(y)` distinct original states all have the same retained output `y`, so exact provenance recovery needs different repair symbols for all of them.

Sufficiency: enumerate the states in the fiber locally by symbols `0,...,m_F(y)-1`. Symbols may be reused in different output fibers because the retained output already identifies the fiber. ∎

Therefore the global minimum shared alphabet is

\[
\boxed{
R_{\max}(F)=\max_{y\in\operatorname{im}F}m_F(y).
}
\]

This is exactly P023-S9 local split multiplicity applied to the refinement from the `F`-kernel back to the identity partition.

## 3. P011-RS-T02 — Every P011 fiber functional is a repair-cost functional

Status: `PROVED`.

For any integer function

\[
\varphi:\mathbb N_{>0}\to\mathbb Z,
\]

P011 defines

\[
I_\varphi(F)
=
\sum_y\varphi(m_F(y)).
\]

By T01,

\[
\boxed{
I_\varphi(F)
=
\sum_y\varphi(r_F(y)).
}
\]

identically.

Hence P011-T01 may be read as a repair theorem:

> if `phi` is superadditive, any deterministic future postcomposition can only increase or preserve the aggregate superadditive cost of local provenance-repair alphabets.

No new proof is required; this is an exact change of interpretation of the already-proved fiber identity.

## 4. P011-RS-T03 — Collision spectrum is the binomial repair spectrum

Status: `PROVED`.

The canonical P011 collision spectrum is

\[
J_k(F)
=
\sum_y\binom{m_F(y)}k.
\]

Using T01,

\[
\boxed{
J_k(F)
=
\sum_y\binom{r_F(y)}k.
}
\]

Thus:

- `J_1=N` counts all provenance labels;
- `J_2` counts unordered pairs of labels competing inside the same repair fiber;
- `J_k` counts `k`-way local provenance ambiguities;
- the full spectrum is the binomial moment spectrum of local minimum repair alphabet sizes.

This does not change the P011 numbers. It identifies what the same integers mean when read from the P023 reconstruction side.

## 5. P011-RS-T04 — Binomial inversion recovers the complete repair-size distribution

Status: `PROVED`.

Let

\[
c_r(F)
=|\{y:r_F(y)=r\}|.
\]

Then P011-T05 becomes

\[
\boxed{
c_r(F)
=
\sum_{k=r}^N(-1)^{k-r}\binom kr J_k(F).}
\]

Therefore the collision spectrum exactly reconstructs how many reached outputs require a local repair alphabet of each size.

In particular,

\[
\boxed{
R_{\max}(F)
=
\max\{r:c_r(F)>0\}.
}
\]

So the complete P011 spectrum determines the exact global minimum provenance-repair alphabet as well as every local-size multiplicity.

## 6. Three distinct repair summaries already present in P011

### 6.1 Aggregate excess repair capacity

For `phi(r)=r-1`,

\[
\boxed{
N-|\operatorname{im}F|
=
\sum_y(r_F(y)-1).
}
\]

This sums the number of additional local symbols beyond one symbol per reached output.

It is not the same as the global shared alphabet `R_max(F)`, because symbols can be reused across fibers.

### 6.2 Pairwise ambiguity

\[
\boxed{
J_2(F)=\sum_y\binom{r_F(y)}2.
}
\]

This weights large repair fibers quadratically through pairwise competition.

### 6.3 Worst-case alphabet

\[
\boxed{R_{\max}(F)=\max_y r_F(y).}
\]

This is the exact number of globally reusable repair symbols required for worst-case provenance recovery.

These are different observables on the same local repair profile.

## 7. P011-RS-T05 — Exact repair composition law

Status: `PROVED`.

Let

\[
X\xrightarrow{F}Y\xrightarrow{G}Z.
\]

For each reached `z`, define the reached predecessor set

\[
A_z
=
\{y\in\operatorname{im}F:G(y)=z\}.
\]

Then the local repair alphabet after composition is exactly

\[
\boxed{
r_{G\circ F}(z)
=
\sum_{y\in A_z}r_F(y).
}
\]

### Proof

The final fiber is the disjoint union

\[
(G\circ F)^{-1}(z)
=
\bigsqcup_{y\in A_z}F^{-1}(y).
\]

Taking cardinalities and using T01 gives the result. ∎

This is P011's exact fiber-sum law rewritten as repair transport.

## 8. P011-RS-T06 — Sharp product bound for staged repair

Status: `PROVED`.

Let

\[
R_F=\max_y r_F(y)
\]

and let

\[
R_G^{\rm reach}
=
\max_z|A_z|
\]

be the minimum alphabet required to recover the reached `F`-output label from the final `G`-output.

Then

\[
\boxed{
R_{G\circ F}
\le
R_F R_G^{\rm reach}.
}
\]

### Proof

For every `z`, T05 gives

\[
r_{G\circ F}(z)
=
\sum_{y\in A_z}r_F(y)
\le
|A_z|R_F
\le
R_G^{\rm reach}R_F.
\]

Take the maximum over `z`. ∎

This is exactly the P023-S9 repair-chain submultiplicativity theorem for the partition chain

\[
\Delta_X
\subseteq
\ker F
\subseteq
\ker(G\circ F).
\]

### Equality criterion

Equality holds if and only if some reached final output `z` satisfies both:

1. `|A_z|=R_G^reach`;
2. every `y in A_z` satisfies `r_F(y)=R_F`.

Thus worst-case stage costs multiply exactly only when the worst branches align on the same final fiber. Otherwise the direct repair can be strictly smaller than the product of staged worst cases.

## 9. P011-RS-T07 — New collision increments are new cross-repair ambiguities

Status: `PROVED`.

Suppose one final output merges predecessor repair fibers of sizes

\[
a_1,\ldots,a_s.
\]

Then P011's exact collision increment

\[
\Delta J_k
=
\binom{a_1+\cdots+a_s}{k}
-
\sum_i\binom{a_i}{k}
\]

counts exactly the new `k`-subsets of provenance labels that must now compete inside one final repair fiber but previously belonged to different repair fibers.

For pairs,

\[
\boxed{
\Delta J_2
=
\sum_{i<j}a_i a_j.
}
\]

Thus P011 forward irreversibility growth and P023 reverse repair growth are two directions on the same fiber-coarsening event.

## 10. Relation to the incidence repair calculus

Take the identity provenance relation

\[
R_{id}
=
\{(x,x):x\in X\}
\subseteq X\times X.
\]

Observe the second coordinate through `F`. P023-S10 gives

\[
M(R_{id},F)
=
\max_y|F^{-1}(y)|
=
R_{\max}(F).
\]

So this P011 bridge is the identity-label specialization of the more general incidence-repair theorem.

For arbitrary label relations, predecessor label sets can overlap and the deterministic fiber-sum equality becomes a union inequality. Identity provenance is special because the predecessor label sets are disjoint.

## 11. Foundation-level interpretation

The same finite partition has two exact readings:

### Forward reading — irreversibility

How many previously distinct histories have merged into each current state?

### Reverse task reading — repair

If a proof/task now demands the original identity, how many extra discrete symbols would be minimally necessary to distinguish those histories again?

Therefore

\[
\boxed{
\text{history multiplicity}
=
\text{minimum exact provenance-repair multiplicity}
}
\]

at the mathematical level.

This equality must not be misread physically. A mathematical decoder alphabet can be defined from an external comparison of preimages even when the post-transition ontology, under the project's no-hidden-remainder hypothesis, does not contain those labels.

## 12. Executable specification

- `src/enterprise_math/p011_repair_spectrum.py`
- `tests/test_p011_repair_spectrum.py`

The regression reconstructs the full repair-size distribution by binomial inversion, verifies the exact composition sum, exhaustively checks the sharp product bound on three-state maps, pins strict submultiplicativity, and matches the existing P011 collision formulas.

## 13. Prior-art discipline

Function fibers, binomial moments, finite partition refinement, and coding labels within fibers are standard mathematics. No historical novelty is claimed for the general equivalences. The project value is the exact bridge between its integer-first irreversibility layer and its independently developed future-safe precision/minimal-repair layer.
