# Enterprise Math — Finite Recurrent Weighted-BRC Foundation

Status: `CANONICAL FOUNDATION ADDENDUM CANDIDATE / MAIN-BACKED RESEARCH / FINITE-RATIONAL ONLY`
Effective: `2026-09-02`
Research evidence: PR `#1112`, merge `9d91c769bd3d3086b6f27a843cbf4341659c9b88`
Parent foundation: `ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md`

## 1. Scope

This addendum extends the positive Weighted-BRC foundation from finite DAGs and one-state recurrence to **arbitrary finite non-negative rational transition-mass matrices**.

It does not replace the CWM layer and does not promote spectral radius, Perron eigenvectors, probability semantics, signed amplitudes, or infinite-state recurrence to primitive Enterprise Math objects.

Freeze:

```text
FINITE_NONNEGATIVE_RATIONAL_RECURRENCE = COVERED
INFINITE_STATE_RECURRENCE = NOT_COVERED
SIGNED_OR_AMPLITUDE_RECURRENCE = NOT_COVERED
ARBITRARY_REAL_WEIGHT_RECURRENCE = NOT_COVERED
SPECTRAL_RADIUS = CLASSICAL_EXTERNAL_EQUIVALENT, NOT REQUIRED CERTIFICATE
```

## 2. Transition-mass matrix

Let the finite state set be `1,...,n`. For every positive rational branch `e:i->j` with weight `w_e`, define the one-step total-mass matrix

\[
W_{ij}=\sum_{e:i\to j} w_e\in\mathbb Q_{\ge0}.
\]

For every `k>=0`, the total positive weight of all length-`k` walks from `i` to `j` is exactly

\[
(W^k)_{ij}.
\]

Hence the all-depth mass object is the monotone matrix series

\[
W^*=I+W+W^2+\cdots.
\]

The recurrent system is **total-mass stable** when every entry of this series is finite.

This matrix records only the positive total-mass projection. Path count, provenance and dominant-path coordinates remain separately typed CWM information.

## 3. Exact rational potential criterion

For finite `W in M_n(Q_{>=0})`, the following are equivalent:

1. `W^*` is finite entrywise;
2. there exists `h in Q_{>0}^n` such that
   \[
   Wh<h
   \]
   coordinatewise;
3. `I-W` is invertible and
   \[
   x=(I-W)^{-1}{\bf1}
   \]
   has strictly positive rational coordinates.

When these conditions hold,

\[
\boxed{W^*=(I-W)^{-1}}
\]

exactly, and the canonical potential

\[
\boxed{x=W^*{\bf1}}
\]

satisfies

\[
Wx=x-{\bf1}<x.
\]

Interpretation: `x_i` is the exact total positive mass of all finite walks beginning at state `i` and ending anywhere, including the empty walk.

No floating eigenvalue evaluation is required.

## 4. Gauge-local stability

For any positive rational potential `h`, let

\[
H=\operatorname{diag}(h_1,\ldots,h_n),
\qquad
B=H^{-1}WH.
\]

Then

\[
B_{ij}=W_{ij}\frac{h_j}{h_i}
\]

and

\[
\sum_j B_{ij}=\frac{(Wh)_i}{h_i}.
\]

Therefore

\[
\boxed{
W^*<\infty
\iff
\exists H>0\text{ rational diagonal such that every row sum of }H^{-1}WH\text{ is }<1.
}
\]

The ordinary raw row-sum test is only the special gauge `h=(1,...,1)`.

For the canonical potential `x`, the normalized row sum is

\[
1-\frac1{x_i},
\]

so the exact local deficit is `1/x_i`.

Along a path `i_0->...->i_k`, gauge factors telescope:

\[
\prod B_e
=
\frac{h_{i_k}}{h_{i_0}}\prod W_e.
\]

Hence every closed-cycle product is gauge-invariant. The stabilizing gauge redistributes state scale; it does not hide closed-loop growth.

## 5. Pure integer stability certificate

Choose a positive common denominator `D` and write

\[
W=\frac AD,
\qquad A\in M_n(\mathbb N_0).
\]

Then total-mass stability is equivalent to the existence of a finite positive integer certificate

\[
\boxed{
\exists h\in\mathbb N_{>0}^n:\ Ah<Dh.
}
\]

Equivalently, coordinatewise,

\[
(Ah)_i\le Dh_i-1.
\]

For one state this reduces exactly to the previous law `S=N/D<1`.

The canonical rational potential need not be primitive as an integer vector. Example: a canonical potential `(10,18)` has primitive integer certificate `(5,9)` on the same positive ray.

## 6. Exact stable/divergent integer alternative

Exactly one of the following certificate classes exists:

### Stable

\[
\exists h\in\mathbb N_{>0}^n:\ Ah<Dh.
\]

### Divergent

\[
\exists y\in\mathbb N_0^n\setminus\{0\}:\ y^\top A\ge D y^\top.
\]

They cannot coexist: pairing the stable strict inequality with `y>=0` gives `y^T Ah < D y^T h`, while the divergent inequality paired with `h>0` gives the reverse weak inequality.

Completeness is the finite-dimensional rational Gordan–Stiemke/Farkas alternative applied to the strict positive system. Rational feasible rays may be cleared to integer certificates.

A divergence certificate implies

\[
y^\top W^k\ge y^\top
\]

for every `k`, so the all-depth positive mass cannot converge.

Thus the recurrent phase has finite exact witnesses on **both** sides.

## 7. Stable raw-supercritical example

Let

\[
W=\begin{pmatrix}
0&1/2\\
1/2&2/3
\end{pmatrix}.
\]

Its raw row sums are

\[
1/2,\qquad7/6,
\]

so a naive local test fails.

But

\[
(I-W)^{-1}
=
\begin{pmatrix}
4&6\\
6&12
\end{pmatrix},
\]

and

\[
x=(10,18),\qquad Wx=(9,17)<x.
\]

The primitive integer stability certificate is `(5,9)`. In the canonical gauge the row sums are

\[
9/10,\qquad17/18.
\]

So a state may appear locally supercritical in one representation while the globally stable system admits an exact subcritical gauge.

## 8. Dominant-path stability is weaker

Total-mass stability implies dominant-path contraction after the same stabilizing gauge, because every individual positive branch weight is bounded by the corresponding total one-step mass contribution.

The converse fails.

For

\[
W=\begin{pmatrix}
3/5&3/5\\
3/5&3/5
\end{pmatrix},
\]

every individual length-`k` path has weight `(3/5)^k -> 0`, but total mass from each state grows as `(6/5)^k`.

The vector `y=(1,1)` is an exact divergence certificate:

\[
y^\top W=(6/5)y^\top\ge y^\top.
\]

This is multiplicity-driven instability. In the symmetric presentation the dominant log contribution `ln(3/5)` is overcome by the two-way recoalescence surplus `ln 2`, giving `ln(6/5)>0`.

## 9. Strong connectivity is not required

None of the exact criteria above requires irreducibility or strong connectivity. They apply to any finite non-negative rational transition-mass matrix.

SCC decomposition remains useful operationally, but it is not a theorem hypothesis. Feed-forward and recurrent blocks can therefore share the same exact matrix certificate interface.

## 10. Prior-art and novelty boundary

Neumann series, non-negative matrix stability, M-matrices, Perron–Frobenius positive-vector criteria, and Gordan–Stiemke/Farkas alternatives are classical mathematics.

Enterprise Math does not claim novelty for those generic theorems.

The project-specific reusable structure is:

```text
POSITIVE WEIGHTED BRC
-> FINITE RATIONAL TRANSITION-MASS MATRIX
-> EXACT RATIONAL POTENTIAL
-> PROJECTIVE STATE GAUGE
-> INTEGER STABLE/DIVERGENT CERTIFICATES
```

This gives the existing Weighted-BRC foundation an exact finite recurrent interface without making a floating spectral quantity part of the native state.

## 11. Hard boundaries

This addendum does not cover:

- infinite state spaces;
- signed/amplitude cancellation;
- complex weights or complex logarithm branches;
- arbitrary non-rational real weights as exact native data;
- finite recurrent natural path-count closure (path count can be infinite while total mass is finite);
- probability/Markov interpretation;
- a claim that all spectral information is reducible to the certificate;
- a canonical minimal integer potential.

Use the exact theorem-ledger addendum and `t0.weighted_brc_finite_recurrent` tool interface for current scope.
