# P023 — Relative Repair Spectrum, Supplement 11

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023, with a formal bridge to P011 and P018  
Depends on: P011 collision spectrum, P018 finite precision partitions, P023-S9 minimum repair cardinality  
Discipline: set partitions, quotient maps, binomial inversion, and collision spectra are established mathematics. The project contribution here is the unified finite-precision interpretation and the exact bridge among existing Enterprise Math theorem lines.

## 1. Problem

P023-S9 gives one scalar for a finite refinement: the minimum alphabet needed to upgrade a coarse precision to a finer one.

P011 gives a much richer collision spectrum for an arbitrary many-to-one map.

P018 gives pointwise ambiguity inside observation fibers.

These are not separate structures. A precision refinement itself has a canonical many-to-one quotient projection, so the complete P011 spectrum can be applied directly to a precision upgrade.

## 2. Canonical quotient projection

Let `X` be finite and let `F` refine `E`, written

\[
F\subseteq E.
\]

Then there is a canonical surjection

\[
\boxed{
\pi_{F,E}:X/F\to X/E,
\qquad
[x]_F\mapsto[x]_E.
}
\]

For a coarse block `B in X/E`, define

\[
\boxed{
s_B
=
\#\{C\in X/F:C\subseteq B\}.
}
\]

Thus `s_B` is the number of fine quotient classes forgotten inside one old coarse class.

## 3. P023-S11-T01 — Projection fibers are local minimum repair alphabets

Status: `PROVED`.

For every coarse block `B`,

\[
\boxed{
|\pi_{F,E}^{-1}(B)|=s_B.
}
\]

By P023-S9, `s_B` is exactly the minimum number of repair symbols needed inside that coarse block to recover the fine class.

Therefore the global minimum repair alphabet is

\[
\boxed{
R(E\leftarrow F)
=
\max_{B\in X/E}s_B.
}
\]

The S9 scalar is therefore the maximum fiber size of a canonical quotient projection.

## 4. P023-S11-T02 — Relative repair spectrum

Status: `PROVED`.

Define

\[
\boxed{
\mathcal R_k(E\leftarrow F)
=
\sum_{B\in X/E}\binom{s_B}{k}.
}
\]

Then

\[
\boxed{
\mathcal R_k(E\leftarrow F)
=J_k(\pi_{F,E}),
}
\]

where `J_k` is the P011 collision spectrum.

Hence:

- `R(E<-F)=max_B s_B` is the worst local repair alphabet;
- `R_2` counts pairs of distinct fine classes that the coarse precision forgets into one block;
- higher `R_k` count higher-order sets of fine classes jointly merged by the precision-forgetting projection.

The first coordinate is

\[
\mathcal R_1(E\leftarrow F)=|X/F|.
\]

## 5. P023-S11-T03 — Binomial inversion recovers the full repair-size distribution

Status: `PROVED` by direct specialization of P011-T05.

Let

\[
a_r
=
\#\{B\in X/E:s_B=r\}.
\]

Then

\[
\mathcal R_k
=
\sum_{r\ge k}a_r\binom rk.
\]

Therefore

\[
\boxed{
a_r
=
\sum_{k\ge r}
(-1)^{k-r}\binom kr\mathcal R_k.
}
\]

So the complete relative spectrum determines not merely the worst repair block but the exact histogram of all local repair alphabet sizes.

## 6. P023-S11-T04 — P011 provenance spectrum is the finest-precision endpoint

Take `F` to be the discrete equality relation on the original state set and let `E=ker(T)` for a finite deterministic map

\[
T:X\to Y.
\]

Then each `F`-class is one original state, so

\[
s_B=|T^{-1}(y)|
\]

for the corresponding output block.

Hence

\[
\boxed{
\mathcal R_k(\ker T\leftarrow\Delta_X)
=J_k(T).
}
\]

This gives an exact repair interpretation of P011:

> `|T^{-1}(y)|` is the minimum local alphabet required to recover the original state label after only `T(x)=y` is retained.

Accordingly, P011's entire collision spectrum is also the higher-order provenance-repair spectrum of the forward map.

This is a mathematical reconstruction cost. It does **not** assert that nature physically stores the lost provenance.

## 7. P023-S11-T05 — Precision refinement and history merging move the same spectrum in opposite directions

For any finite partition `E`, define its absolute state-ambiguity spectrum

\[
\boxed{
\mathcal A_k(E)
=
\sum_{B\in X/E}\binom{|B|}{k}.
}
\]

If `F subseteq E` is finer, every `F`-block lies in one `E`-block, and convex binomial counting gives

\[
\boxed{
\mathcal A_k(F)\le\mathcal A_k(E).
}
\]

Define the refinement gain

\[
\boxed{
G_k(E\to F)
=
\mathcal A_k(E)-\mathcal A_k(F).
}
\]

Then `G_k` is exactly the number of `k`-element original-state subsets that were co-observed at precision `E` but are separated at precision `F`.

Thus:

\[
\boxed{
\text{deterministic postcomposition / history merging}
\Longrightarrow
\mathcal A_k\text{ increases},
}
\]

while

\[
\boxed{
\text{task enrichment / precision refinement}
\Longrightarrow
\mathcal A_k\text{ decreases}.
}
\]

The same partition statistic therefore measures forward information loss and backward precision gain with opposite orientation.

## 8. P023-S11-T06 — Refinement-chain composition

Status: `PROVED`.

For

\[
G\subseteq F\subseteq E,
\]

the canonical projections compose:

\[
X/G\longrightarrow X/F\longrightarrow X/E.
\]

If an `E`-block contains `F`-blocks `C_1,...,C_m`, then its number of `G`-blocks is exactly

\[
\boxed{
s^{G/E}_B
=
\sum_{j=1}^{m}s^{G/F}_{C_j}.
}
\]

Consequently

\[
\boxed{
R(E\leftarrow G)
\le
R(E\leftarrow F)R(F\leftarrow G),
}
\]

recovering the P023-S9 staged repair bound as the maximum-fiber shadow of exact quotient-projection composition.

The bound can be strict when the largest split at the first stage and the largest split at the second stage occur on different branches.

## 9. Repair generating polynomial

The relative repair spectrum may be packaged as

\[
\boxed{
K_{E\leftarrow F}(t)
=
\sum_{B\in X/E}\big((1+t)^{s_B}-1\big).
}
\]

Its coefficient of `t^k` is exactly `R_k(E<-F)`.

This is precisely the P011 collision polynomial of the canonical precision-forgetting projection.

Therefore P011 polynomial identities and factor-merger interpretations can be reused for precision projections without introducing a separate polynomial theory.

## 10. Foundational interpretation

A finite precision state is not exhausted by a scalar class count.

For a relative upgrade `E -> F`, there are at least three distinct exact objects:

1. the worst local repair alphabet `max s_B`;
2. the complete local repair-size distribution `a_r`;
3. the higher-order spectrum `R_k` / generating polynomial.

This supplies a task-relative integer information calculus without logarithms, probabilities, hidden real entropy, or a chosen Euclidean scale.

## 11. Executable specification

- `src/enterprise_math/precision_projection_spectrum.py`
- `tests/test_precision_projection_spectrum.py`

The tests reconstruct local repair-size distributions by binomial inversion, verify exact projection composition, compare the S11 maximum with the generic S9 minimum-repair theorem, and pressure-test ambiguity-spectrum monotonicity on small finite partitions.

## 12. Prior-art and novelty discipline

Equivalence-relation quotients, fiber-size spectra, binomial inversion, and partition lattices are established mathematics. P011 already owns the collision-spectrum theorem family inside Enterprise Math.

The new project-level result is the explicit identification

\[
\boxed{
\text{P011 collision spectrum of }\pi_{F,E}
=
\text{relative precision repair spectrum }E\leftarrow F,
}
\]

which closes a previously separate P011/P018/P023 loop. Historical priority of this packaging is not claimed.
