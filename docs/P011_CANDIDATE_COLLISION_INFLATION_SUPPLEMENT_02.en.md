# P011 Supplement 02 — Candidate-Domain Collision Inflation

Status: `PROVED RESEARCH NOTE`  
Owner: A1 / P011 collision spectrum  
Pressure source: P023 actual-image separation and the candidate-vs-realized gap in P017 L052/L055  
Discipline: binomial identities and Vandermonde convolution are mature combinatorics; no historical priority claim is made for them.

## 1. Setup

Let `I` be a finite label set. For each label `i`, let the realized image and an enlarged candidate set satisfy

\[
A_i\subseteq C_i\subseteq Y.
\]

Project tagged incidences `(i,y)` to `y`, and define

\[
m_A(y)=\#\{i:y\in A_i\},
\qquad
m_C(y)=\#\{i:y\in C_i\},
\]

with candidate thickening

\[
\boxed{\delta(y)=m_C(y)-m_A(y)\ge0.}
\]

The corresponding P011 collision polynomials are

\[
K_A(t)=\sum_y((1+t)^{m_A(y)}-1),
\qquad
K_C(t)=\sum_y((1+t)^{m_C(y)}-1).
\]

## 2. P011-S02-T01 — Exact candidate-domain collision inflation

\[
\boxed{
K_C(t)-K_A(t)
=
\sum_y
(1+t)^{m_A(y)}
\big((1+t)^{\delta(y)}-1\big)
\in\mathbb N[t].
}
\]

Proof is pointwise:

\[
(1+t)^{m_A+\delta}-(1+t)^{m_A}
=(1+t)^{m_A}((1+t)^\delta-1).
\]

Thus candidate enlargement cannot decrease any collision coefficient.

## 3. P011-S02-T02 — Exact inflation at every collision order

Let

\[
J_k(A)=\sum_y\binom{m_A(y)}k,
\qquad
J_k(C)=\sum_y\binom{m_C(y)}k.
\]

Vandermonde gives

\[
\boxed{
J_k(C)-J_k(A)
=
\sum_y\sum_{j=1}^k
\binom{m_A(y)}{k-j}
\binom{\delta(y)}j.
}
\]

Every term is a nonnegative integer, so all collision orders are monotone under candidate enlargement.

## 4. Closed form for false pair collisions

For `k=2`,

\[
\boxed{
J_2(C)-J_2(A)
=
\sum_y
\left(
m_A(y)\delta(y)
+
\binom{\delta(y)}2
\right).
}
\]

The two terms have different meanings:

- `m_A delta`: fake pair collisions between new candidate incidences and realized incidences;
- `binom(delta,2)`: collisions created entirely among candidate-only incidences.

So the cost of replacing realized images by larger candidate sets is an exact integer collision inflation, not merely a vague statement that an upper bound is loose.

## 5. P011-S02-C01 — If actual images are separated, every candidate collision is spurious

If realized shell images are pairwise disjoint, then

\[
m_A(y)\le1,
\]

and therefore for every `k>=2`,

\[
J_k(A)=0.
\]

Any higher-order collision seen after candidate enlargement is then entirely manufactured by the enlargement.

This supplies the P023 image-separation tool with an exact cost language: a true zero-repair system can still acquire a nonzero proof-level collision budget solely because a candidate superset was substituted for the realized state set.

## 6. Exact inflation at P017 k=14

L052 candidate root pairs at `k=14` are

\[
C_2=\{9,10\},
\qquad
C_3=\{8,9\}.
\]

The exact-window realized root images are

\[
A_2=\{9,10\},
\qquad
A_3=\{8\}.
\]

Only at `y=9` do we have

\[
m_A(9)=1,
\qquad
\delta(9)=1.
\]

Hence

\[
\boxed{J_2(C)-J_2(A)=1.}
\]

The candidate layer therefore manufactures exactly one cross-shell pair collision.

This upgrades the P017 lesson “candidate threshold 15 versus actual threshold 9” into a quantitatively exact P011 collision-inflation statement.

## 7. Ownership boundary

- P011/A1 owns the collision polynomial and candidate-domain inflation.
- P023/A2 owns future-compatible quotient, actual-image label erasure, and minimum repair.
- P017 keeps the sharp square-basin specialization.

The result therefore feeds an A2 over-approximation phenomenon back into the existing P011 mother owner rather than duplicating collision theory inside P023.

## 8. Executable audit

- `src/enterprise_math/candidate_collision_inflation.py`
- `tests/test_p011_candidate_collision_inflation.py`

Regression checks the pair formula, nonnegative inflation at every tested order, and the exact one-false-pair `k=14,root=9` witness. Computation is regression only; the proof is the binomial identity above.
