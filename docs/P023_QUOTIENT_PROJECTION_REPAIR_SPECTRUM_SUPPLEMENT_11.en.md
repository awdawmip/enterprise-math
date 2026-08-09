# P023 — Quotient-Projection Repair Spectrum, Supplement 11

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023, consuming the canonical P011 collision spectrum  
Scope: finite precision relations and refinement chains  
Discipline: finite equivalence-relation lattices, quotient projections, binomial inversion, and partition block statistics are established mathematics. The project contribution is the exact identification of P011 irreversibility spectra with higher-order P023 repair spectra between precision states.

## 1. Precision refinement creates a canonical many-to-one map

Let `X` be a finite nonempty set and let

\[
F\subseteq E
\]

be equivalence relations on `X`, with `F` finer than `E`.

Every fine class lies inside one unique coarse class. Hence there is a canonical surjection

\[
\boxed{
\pi_{F,E}:X/F\to X/E,
\qquad
[x]_F\mapsto[x]_E.
}
\]

This map is the act of **forgetting the extra precision carried by `F`**.

For a coarse block `B in X/E`, define

\[
\boxed{
s_{E\leftarrow F}(B)
=
|\pi_{F,E}^{-1}(B)|
=
\#\{C\in X/F:C\subseteq B\}.}
\]

By P023-S9, this is exactly the local minimum repair alphabet required, once only `B` is retained, to recover which fine class `C` was present.

## 2. P023-S11-T01 — P011/P023 quotient-projection duality

Status: `PROVED`.

The P011 local fiber multiplicity of the forgetting map `pi_{F,E}` equals the P023 local repair multiplicity of the precision upgrade `E -> F`:

\[
\boxed{
m_{\pi_{F,E}}(B)=s_{E\leftarrow F}(B).}
\]

Consequently,

\[
\boxed{
R(E\to F)
=
\max_B m_{\pi_{F,E}}(B).
}
\]

### Proof

The fiber of `pi_{F,E}` over coarse block `B` is literally the set of fine blocks contained in `B`. P023-S9 says those fine target blocks require distinct repair symbols inside that coarse block and symbols may be reused across different coarse blocks. ∎

Thus every finite precision upgrade has a canonical deterministic map whose P011 irreversibility multiplicities are exactly its P023 repair multiplicities.

## 3. P023-S11-T02 — Higher-order repair spectrum

Status: `PROVED`.

Define

\[
\boxed{
\mathcal R_k(E\leftarrow F)
=
J_k(\pi_{F,E})
=
\sum_{B\in X/E}
\binom{s_{E\leftarrow F}(B)}k.
}
\]

Then:

- `R_1(E<-F)=|X/F|`, the number of fine classes;
- `R_2` counts pairs of distinct fine classes that become indistinguishable after forgetting from `F` to `E`;
- `R_k` counts `k`-subsets of fine classes collapsed into one coarse class.

This is a **relative precision-loss spectrum**. It measures class-level ambiguity created by one declared forgetting map rather than ambiguity among raw states unless `F` is the identity relation.

## 4. P023-S11-T03 — Complete local repair-size reconstruction

Status: `PROVED`.

Let

\[
c_r(E\leftarrow F)
=
|\{B\in X/E:s_{E\leftarrow F}(B)=r\}|.
\]

Then P011 binomial inversion gives

\[
\boxed{
c_r(E\leftarrow F)
=
\sum_{k=r}^{|X/F|}
(-1)^{k-r}\binom kr
\mathcal R_k(E\leftarrow F).}
\]

Therefore the full relative repair spectrum exactly determines how many coarse blocks require repair alphabets of size `1,2,3,...`.

In particular,

\[
\boxed{
R(E\to F)
=
\max\{r:c_r(E\leftarrow F)>0\}.
}
\]

P023-S9 kept only this worst-case maximum. S11 retains the entire distribution and all higher-order ambiguity counts.

## 5. P023-S11-T04 — Relative repair polynomial

Status: `PROVED`.

Define

\[
\boxed{
K_{E\leftarrow F}(t)
=
\sum_{B\in X/E}
\left((1+t)^{s_{E\leftarrow F}(B)}-1\right).
}
\]

Then

\[
\boxed{
K_{E\leftarrow F}(t)
=
\sum_{k=1}^{|X/F|}
\mathcal R_k(E\leftarrow F)t^k.
}
\]

This is exactly the canonical P011 collision polynomial evaluated on the quotient projection `pi_{F,E}`.

Hence the polynomial simultaneously records all higher-order precision classes that are forgotten by `F -> E`.

## 6. Absolute ambiguity as the identity-refinement special case

Take the finest possible relation

\[
F=\Delta_X.
\]

Then `X/F` is canonically `X`, and

\[
\pi_{\Delta,E}:X\to X/E
\]

is simply the observation/quotient map for precision `E`.

Therefore

\[
\boxed{
\mathcal R_k(E\leftarrow\Delta_X)
=
\sum_{B\in X/E}\binom{|B|}k.
}
\]

This one formula contains three existing project views:

- P018 pointwise ambiguity: local value `|B|`;
- P023 worst-case reconstruction: `max_B |B|`;
- P011 collision spectrum: the binomial aggregate over all blocks.

So the three programs were measuring different projections of the same finite partition profile.

## 7. P023-S11-T05 — Precision refinement decreases absolute ambiguity spectrum

Status: `PROVED`.

If

\[
F\subseteq E,
\]

then for every `k>=2`,

\[
\boxed{
\mathcal R_k(F\leftarrow\Delta_X)
\le
\mathcal R_k(E\leftarrow\Delta_X).
}
\]

### Proof

Every coarse `E` block is a disjoint union of fine `F` blocks. Since

\[
n\mapsto\binom nk
\]

is superadditive on nonnegative integers, replacing each coarse block by its fine subblocks can only decrease the sum. ∎

Thus the same spectrum moves in opposite directions under the two foundational processes:

\[
\boxed{
\text{deterministic time postcomposition/coarsening}:
\mathcal R_k\uparrow,
}
\]

\[
\boxed{
\text{precision/task refinement}:
\mathcal R_k\downarrow.
}
\]

No entropy or real-valued information measure is needed to express this dual monotonicity.

## 8. P023-S11-T06 — Exact higher-order precision gain

Status: `PROVED`.

For `F subseteq E`, define

\[
\boxed{
G_k(E\to F)
=
\mathcal R_k(E\leftarrow\Delta_X)
-
\mathcal R_k(F\leftarrow\Delta_X).
}
\]

Then `G_k>=0`, and it counts exactly the `k`-element subsets of raw states that were contained in one coarse `E` block but are split across at least two fine `F` blocks.

### Proof

Inside one coarse block `B`, write its fine subblock sizes as `a_1,...,a_s`. The local gain is

\[
\binom{a_1+\cdots+a_s}{k}
-
\sum_i\binom{a_i}{k},
\]

which by the multinomial Vandermonde identity counts exactly the `k`-subsets using states from at least two fine subblocks. Summing over coarse blocks proves the claim. ∎

This is the precision-direction mirror of the P011 collision increment, which counts `k`-subsets newly merged by time coarsening.

## 9. P023-S11-T07 — Refinement gains telescope

Status: `PROVED`.

For a refinement chain

\[
E_0\supseteq E_1\supseteq\cdots\supseteq E_m,
\]

\[
\boxed{
\mathcal R_k(E_0\leftarrow\Delta_X)
-
\mathcal R_k(E_m\leftarrow\Delta_X)
=
\sum_{j=0}^{m-1}G_k(E_j\to E_{j+1}).
}
\]

This is an exact integer telescoping law for higher-order precision gain. P018's pointwise ambiguity gain is the local `k=1`-style block-size view; S11 supplies the global subset-separation hierarchy for `k>=2`.

## 10. P023-S11-T08 — Refinement-chain projections compose exactly

Status: `PROVED`.

For

\[
G\subseteq F\subseteq E,
\]

the canonical quotient projections satisfy

\[
\boxed{
\pi_{G,E}
=
\pi_{F,E}\circ\pi_{G,F}.
}
\]

For every coarse `E` block `B`, its direct local repair size obeys the exact sum law

\[
\boxed{
s_{E\leftarrow G}(B)
=
\sum_{C\in\pi_{F,E}^{-1}(B)}
s_{F\leftarrow G}(C).
}
\]

Therefore the entire P011 composition calculus applies directly to staged precision forgetting and staged repair.

In particular,

\[
\boxed{
R(E\to G)
\le
R(E\to F)R(F\to G),
}
\]

recovering P023-S9-T04 as the maximum-fiber shadow of the stronger quotient-projection composition law.

## 11. Conceptual consolidation

This result removes an unnecessary separation among three words:

- **collision** in P011;
- **ambiguity** in P018;
- **repair** in P023.

At finite precision they are all derived from the same block/fiber structure. What differs is orientation and task:

- forward dynamics asks how blocks merge;
- observation precision asks how large the current blocks are;
- repair asks how many finer blocks sit inside each retained coarse block.

The canonical quotient projection connects these views without changing the underlying mathematics.

## 12. Executable specification

- `src/enterprise_math/precision_projection_spectrum.py`
- `tests/test_precision_projection_spectrum.py`

The regression checks exact quotient-projection fibers, agreement with the generic P023-S9 minimum alphabet, binomial inversion, exact chain composition, strict product-bound examples, and absolute ambiguity-spectrum monotonicity under refinement.

## 13. Foundation boundary

The spectrum is a theorem about finite partitions, prediction, and reconstruction. It does not imply that physical histories erased by an ontological many-to-one transition remain hidden inside nature. The reverse repair alphabet is an externally defined minimum distinction needed by a declared reconstruction task.
