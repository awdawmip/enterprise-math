# P019 — Focusing Concentration, Supplement 07: Equal Total Contraction Does Not Mean Equal Microscopic Focusing

Status: `ACTIVE RESEARCH NOTE`  
Depends on: P011 collision spectrum, P019 Overlap-Spectrum Focusing Supplement 06  
Scope: prove that total focusing excess `C` ceases to be complete at three sources and define higher-order integer concentration observables  
Discipline: these quantities describe concentration of future-target multiplicity. They are not assigned Ricci/shear/energy meanings at this stage.

## 1. Problem

The previous stages established

\[
\Xi=B-C
\]

and

\[
C=J_2-J_3+J_4-\cdots.
\]

This raises a natural question:

> If two local causal structures have the same current-section size `N`, the same branching surplus `B`, the same total focusing `C`, and the same expansion `Xi`, must their microscopic focusing structure be the same?

No. The first failure already occurs with three sources.

## 2. P019-FC-T01 — With at most two sources, the coarse quantities reconstruct the multiplicity profile

Status: `PROVED`

If

\[
|A|\le2,
\]

then every future-target multiplicity satisfies

\[
m_w\in\{1,2\}.
\]

In that regime

\[
C=\sum_w(m_w-1)
\]

is exactly the number of multiplicity-2 targets.

The total outgoing-incidence count is

\[
E=N+B,
\]

and the number of future targets is

\[
F=E-C=N+B-C.
\]

Therefore

\[
\boxed{
\#\{m=2\}=C,
}
\]

and

\[
\boxed{
\#\{m=1\}=F-C=N+B-2C.
}
\]

Thus for `N<=2`, the data `N,B,C` completely determine the future-target multiplicity multiset.

There is no room yet for equal total focusing with distinct higher-order structure.

## 3. P019-FC-T02 — Three sources are the minimal threshold where the total ceases to be complete

Status: `PROVED BY T01 + EXPLICIT COUNTEREXAMPLE`

Take a current section

\[
A=\{a,b,c\}
\]

and two future targets `x,y`.

### Structure D: diffuse pair focusing

Use edges

\[
a\to x,
\quad b\to x,
\quad a\to y,
\quad c\to y.
\]

The future multiplicities are

\[
(2,2).
\]

Hence

\[
N=3,
\quad E=4,
\quad B=1,
\quad F=2,
\quad C=2,
\quad\Xi=-1.
\]

The collision spectrum is

\[
(J_1,J_2,J_3)=(4,2,0).
\]

### Structure H: concentrated triple focusing

Use edges

\[
a\to x,
\quad b\to x,
\quad c\to x,
\quad a\to y.
\]

The future multiplicities are

\[
(3,1).
\]

Again

\[
N=3,
\quad E=4,
\quad B=1,
\quad F=2,
\quad C=2,
\quad\Xi=-1.
\]

but the collision spectrum is

\[
(J_1,J_2,J_3)=(4,3,1).
\]

Therefore

\[
\boxed{
(N,B,C,\Xi)_{D}
=(N,B,C,\Xi)_{H}
}
\]

while

\[
\boxed{
(J_2,J_3)_{D}\ne(J_2,J_3)_{H}.
}
\]

By T01 this cannot occur for `N<=2`. Hence

\[
\boxed{N=3}
\]

is the smallest source cardinality at which coarse focusing data cease to recover microscopic multiplicity structure.

If current and future layers are required to be vertex-disjoint, the witness needs only three current vertices and two future vertices, for five graph vertices total.

## 4. P019-FC-T03 — Higher-order concentration `H=J_2-C`

Status: `PROVED`

Define

\[
\boxed{
H(A)=J_2^{\rm out}(A)-C(A).
}
\]

For one multiplicity `m`,

\[
\binom m2-(m-1)
=
\frac{(m-1)(m-2)}2
=
\binom{m-1}2.
\]

Hence

\[
\boxed{
H(A)
=
\sum_w\binom{m_A(w)-1}{2}.
}
\]

Therefore

\[
H(A)\ge0,
\]

and, exactly,

\[
\boxed{
H(A)=0
\iff
m_A(w)\le2\text{ for every future target }w.
}
\]

So `H>0` is an exact **higher-order focusing witness**: it appears iff at least one future target is jointly hit by three or more current incidences.

For the two structures in T02:

- diffuse `(2,2)`: `H=0`;
- concentrated `(3,1)`: `H=1`.

## 5. P019-FC-T04 — Quadratic focusing concentration `Q=2J_2-C`

Status: `PROVED`

Define

\[
\boxed{
Q(A)=2J_2^{\rm out}(A)-C(A).
}
\]

Since

\[
2\binom m2-(m-1)
=m(m-1)-(m-1)
=(m-1)^2,
\]

we obtain

\[
\boxed{
Q(A)
=
\sum_w(m_A(w)-1)^2.
}
\]

`C` is the first-order total of excess multiplicity,

\[
C=\sum_w(m_w-1),
\]

while `Q` is the sum of squares of the same excesses.

At fixed `C`, `Q` is therefore more sensitive to whether focusing is concentrated into a small number of high-multiplicity targets.

In T02:

- `(2,2)` has excess `(1,1)`, so `Q=2`;
- `(3,1)` has excess `(2,0)`, so `Q=4`.

Both have total focusing `C=2`, but `Q` separates diffuse from concentrated focusing.

This remains an integer multiplicity-concentration observable, not an automatic physical shear or curvature scalar.

## 6. P019-FC-T05 — `C` is not a complete local focusing invariant

Status: `PROVED`

T02 gives two finite causal sections with identical

\[
N,
\quad B,
\quad C,
\quad\Xi,
\]

but different

\[
J_2,J_3,\ldots,
\quad H,
\quad Q,
\quad\mu=\max_wm_w.
\]

Therefore

\[
\boxed{
C\text{ alone is not a complete local focusing invariant.}
}
\]

Likewise `Xi=B-C` is sufficient to determine the net change of section cardinality but insufficient to reconstruct the microscopic overlap structure that produced the change.

This agrees with the P011 completeness theorem: reconstructing the fiber-size multiset requires the full collision spectrum rather than a low-order aggregate.

## 7. Constraint on shear-like / curvature-like research

This stage imposes a necessary condition on any later geometric-source interpretation. If two local graphs have equal `N,B,C,Xi` but different `J_k` spectra, then any proposed “discrete curvature” depending only on `C` or `Xi` cannot distinguish them.

That does **not** justify the reverse assignments

- `H` is shear;
- `Q` is curvature;
- high `J_3` is a particular matter source.

The next missing structure is **directional/local-subsection information**: whether equal multiplicity concentration is distributed differently across intrinsic directions or graph neighborhoods.

The next step should therefore construct directional refinement rather than add more directionless scalars.

## 8. Relation to P011

P011 already proves that the full collision spectrum

\[
(J_2,\ldots,J_N)
\]

together with domain size recovers the fiber-size multiset.

P019-FC specializes that result to the causal incidence map:

> the full spectrum recovers the multiplicity distribution describing how many current causal incidences jointly hit each future target.

Novelty discipline remains explicit:

- collision-spectrum completeness comes from P011;
- the minimal three-source witness, the use of `H/Q` inside P019 causal focusing, and the later directional source decomposition belong to the current integration program.

## 9. Stage ledger

- `P019-FC-T01`: for at most two sources, `N,B,C` reconstruct the multiplicity profile — `PROVED`
- `P019-FC-T02`: three sources are the minimal cardinality for equal coarse focusing with different higher-order spectra — `PROVED`
- `P019-FC-T03`: `H=J2-C=sum binom(m-1,2)`, with `H=0` iff all multiplicities are at most 2 — `PROVED`
- `P019-FC-T04`: `Q=2J2-C=sum(m-1)^2` — `PROVED`
- `P019-FC-T05`: total focusing `C` is not a complete local focusing invariant — `PROVED`

Executable checks:

- `src/enterprise_math/focusing_concentration.py`
- `tests/test_focusing_concentration.py`

## 10. Next stage

At this point the total focusing quantity has been resolved far enough that adding further directionless scalars has rapidly diminishing value.

The next priority is a **directional overlap spectrum**:

1. equip primitive outgoing incidences with direction/adjacency classes that do not depend on continuous angles;
2. compare `J_k,H,Q` on directional subsections;
3. define a pure-integer anisotropy witness;
4. determine its transformation law under graph automorphisms;
5. only then compare its structural behavior with continuum shear.

Only after that stage should any integer term be discussed as genuinely shear-like.
