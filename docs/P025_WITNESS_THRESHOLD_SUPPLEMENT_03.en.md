# P025 Supplement 03 — Coarsest Precision Chain for Witness Thresholds

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Nature: direct consequence of P023 minimal repair; no abc-specific mathematics required

## 1. Finite threshold tasks do not require the full witness cost

Let `X` be a state space with an existing coarse quotient

\[
q:X\to Q,
\]

and let every state carry a witness cost

\[
\mu:X\to\mathbb N\cup\{\infty\}.
\]

Fix a task radius `K>=0`. If the future only asks

\[
h_j(x)=1_{\mu(x)\le j},
\qquad 0\le j\le K,
\]

define the truncated cost

\[
\boxed{
\tau_K(x)=\min\{\mu(x),K+1\},
}
\]

with infinity mapped to `K+1`.

## 2. P025-T08 — truncated cost is exactly equivalent to the full threshold family

For any `x,y in X`,

\[
\boxed{
\tau_K(x)=\tau_K(y)
\iff
h_j(x)=h_j(y)\quad\forall\,0\le j\le K.
}
\]

If the truncated values agree, every predicate “truncated value <= j” agrees, and for `j<=K` this is exactly `mu<=j`. Conversely, if all threshold predicates agree, then a cost at most `K` is recovered as the first radius where the profile becomes true; if the profile is always false, the truncated value is `K+1`.

Thus `tau_K` is not a heuristic compression. It is a complete minimal label for this finite family of future observables.

## 3. P025-T09 — coarsest P023 repair relative to an existing q

Define

\[
\boxed{
r_K(x)=\bigl(q(x),\tau_K(x)\bigr).}
\]

Then:

1. `r_K` refines `q`;
2. every `h_j`, `j<=K`, descends through `r_K`;
3. if another quotient `s` refines `q` and every `h_j`, `j<=K`, descends through `s`, then `s` necessarily refines `r_K`.

For the third point, `s(x)=s(y)` gives equal base states and equal threshold profiles; P025-T08 therefore gives equal truncated costs and hence equal `r_K` states.

Therefore

\[
\boxed{r_K=(q,\tau_K)}
\]

is the coarsest repair for the finite witness-threshold task family.

This is an exact instance of P023-T02: restore only information that the selected future actually needs.

## 4. P025-T10 — threshold precision forms a projection chain

If `0<=K<L`, then

\[
\boxed{
\tau_K(x)=\min\{\tau_L(x),K+1\}.
}
\]

Hence higher threshold precision projects exactly to lower threshold precision and

\[
r_L\text{ refines }r_K.
\]

This yields a genuine task-horizon precision chain

\[
r_0\preceq r_1\preceq r_2\preceq\cdots.
\]

Increasing `K` has a precise meaning: the future task asks for discrimination of higher witness costs, so the quotient splits only where necessary.

## 5. The minimal repair of P025-N02 is now explicit

For

\[
A:1+2=3,\qquad \mu(A)=1,
\]

and

\[
B:1+8=9,\qquad \mu(B)=2,
\]

the radical coarse states are equal.

If the task asks only `mu<=0`, the two states may still remain collapsed:

\[
\tau_0(A)=\tau_0(B)=1.
\]

Once the task is upgraded to ask `mu<=1`, however,

\[
\tau_1(A)=1,
\qquad
\tau_1(B)=2,
\]

so the states must split for the first time exactly at that task precision.

This gives a concrete Enterprise Math conclusion:

\[
\boxed{
\text{whether two states must be distinguished is determined by the future task horizon, not permanently by the objects alone.}
}
\]

## 6. Foundation feedback

Earlier P025 stages required `Sigma_add` or `Sigma_flag` to recover the full witness generator structure. P025-T09 shows that this can be seriously over-fine when the task is weaker and asks only finite witness thresholds.

The architecture should therefore distinguish:

- **generator precision** — enough information to reconstruct the entire witness lattice/flag;
- **decision precision** — only enough information to answer certificate predicates within a selected horizon.

The latter has the exact coarsest realization `tau_K` in this setting.

This is not a new abc theorem. It is a reusable P023 precision theorem extracted by the abc pressure test.

## 7. Executable assets

- `src/enterprise_math/witness_threshold_precision.py`
  - truncated cost `tau_K`;
  - threshold profiles;
  - exact projection across horizons;
  - repair `(q,tau_K)`;
  - finite audit of coarsest-repair semantics.
- `tests/test_witness_threshold_precision.py`
  - profile/truncation equivalence;
  - coalescence of infinity and large costs at finite horizon;
  - projection chain;
  - first split between `mu=1` and `mu=2` at `K=1`;
  - finite coarsest-repair regression.

## 8. Current shortest architecture chain

After three P025 compressions, the current structure is

\[
\boxed{
\text{fine relation-state}
\to
\text{coarse state}
\to
\begin{cases}
\text{generator signature},&\text{if the certificate space must be reconstructed};\\
\tau_K,&\text{if only finite certificate thresholds must be answered}.
\end{cases}
}
\]

This is more flexible than demanding exact preservation of every future operation, and more information-efficient than restoring the full fine state whenever a collapse fails.

The next step is to relay this threshold-repair theorem to P023/A2 so the mother layer can decide whether it should become a generic canonical tool. P025 should continue to use abc/Mason/Pasten as pressure tests without taking ownership of the mother-layer theorem.
