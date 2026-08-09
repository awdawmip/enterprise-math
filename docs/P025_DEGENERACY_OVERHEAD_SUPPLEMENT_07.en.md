# P025 Supplement 07 — Additive Radius versus Non-Degenerate Witness Radius

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-degeneracy-overhead`  
Parent dependency: `program/p025-witness-precision-bracket@44f260d7`  
Prior-art status: finite integer-lattice minima are established mathematics; P025 use is a task-state pressure test

## 1. Goal

Supplement 06 brackets the exact non-degenerate witness precision `mu` between an arithmetic demand floor `lambda_abc` and a sparse generator ceiling `U_2`.

A natural possible simplification remains:

> Perhaps all of the gap above arithmetic demand is already explained by the additive relation lattice `T=ker_Z(alpha)`, so the degeneracy sublattice `T^circ` can be discarded once the shortest additive radius is known.

This supplement gives an exact counterexample. The answer is no.

## 2. Additive-lattice radius

Define

\[
\boxed{
\rho(a,b,c)
=
\min\{\|x\|_\infty:x\in T,\ x\ne0\}.
}
\]

By definition, the non-degenerate witness set is a subset of the nonzero additive lattice:

\[
T\setminus T^\circ
\subseteq
T\setminus\{0\}.
\]

Therefore

\[
\boxed{\rho\le\mu.}
\]

Together with Supplement 06:

\[
\boxed{
\max(\lambda_{abc},\rho)
\le
\mu
\le
U_2.
}
\]

Define the **non-degeneracy overhead**

\[
\boxed{
\eta_{nd}
=
\mu-\max(\lambda_{abc},\rho)
\ge0.
}
\]

If `eta_nd>0`, then neither arithmetic demand nor the first nonzero additive-lattice state is sufficient to answer the future query “does a non-degenerate certificate exist at this radius?”.

## 3. P025-N04 — exact non-degeneracy barrier at `1+53=54`

Consider

\[
1+53=54.
\]

The prime-labelled coordinates are

\[
(2,3,53).
\]

For the relation-adapted arithmetic derivative, the primitive additive normal is

\[
\boxed{
\alpha=(27,54,-1).
}
\]

Indeed,

\[
d^\psi(54)=27x_2+54x_3,
\qquad
 d^\psi(53)=x_{53},
\]

and relation additivity gives

\[
\boxed{
x_{53}=27x_2+54x_3=27(x_2+2x_3).}
\]

For the complementary pair `(1,53)`, the Wronskian is simply `d^psi(53)`, so a primitive degeneracy normal is

\[
\boxed{
\beta=(0,0,1).
}
\]

Thus non-degeneracy is exactly

\[
x_{53}\ne0.
\]

### Additive radius

The vector

\[
(-2,1,0)
\]

lies in `T`, so `rho<=2`.

There is no nonzero additive vector of radius one. If all coordinates lie in `{-1,0,1}`, then the equality

\[
x_{53}=27(x_2+2x_3)
\]

and `|x_53|<=1` force `x_2+2x_3=0`; within `{-1,0,1}` this implies `x_2=x_3=0`, and then `x_53=0`.

Hence

\[
\boxed{\rho=2.}
\]

### Non-degenerate witness radius

If the witness is non-degenerate, `x_53` is a nonzero multiple of `27`. Therefore

\[
\|x\|_\infty\ge |x_{53}|\ge27.
\]

The explicit vector

\[
(1,0,27)
\]

satisfies the additive relation and is non-degenerate. Consequently

\[
\boxed{\mu=27.}
\]

### Arithmetic demand floor and sparse upper certificate

Here

\[
m(54)=9,
\]

while the normalized complementary capacity for target `54` and pair `(1,53)` is

\[
K_{1,53}=1.
\]

Therefore

\[
\lambda_{54}=9
\]

and the other orientations do not exceed it, so

\[
\boxed{\lambda_{abc}=9.}
\]

The nonzero generator minors with the `53` coordinate give the cheapest sparse witness cost

\[
\boxed{U_2=27.}
\]

Thus the complete exact profile is

\[
\boxed{
\lambda_{abc}=9,
\qquad
\rho=2,
\qquad
\mu=27,
\qquad
U_2=27.
}
\]

and therefore

\[
\boxed{\eta_{nd}=27-9=18.}
\]

This is a strict finite counterexample to any rule that replaces the full flag `T^circ subset T` by arithmetic demand plus the additive-lattice shortest radius.

## 4. A second independent barrier: `1+36=37`

On coordinates `(2,3,37)`,

\[
\alpha=(36,24,-1),
\qquad
\beta=(3,2,0).
\]

The additive equation is

\[
x_{37}=36x_2+24x_3=12(3x_2+2x_3).
\]

The shortest additive vector is

\[
(-2,3,0),
\]

so

\[
\rho=3.
\]

But this vector is degenerate because `3(-2)+2(3)=0`. Non-degeneracy requires `3x_2+2x_3 neq 0`, hence `x_37` is a nonzero multiple of `12`, giving

\[
\mu\ge12.
\]

The vector `(1,-1,12)` attains the bound, so

\[
\mu=12.
\]

Supplement 06 gives

\[
\lambda_{abc}=6,
\qquad
U_2=24.
\]

Therefore

\[
\boxed{
(\lambda_{abc},\rho,\mu,U_2)=(6,3,12,24),
\qquad
\eta_{nd}=6.
}
\]

This example differs structurally from `1+53=54`: the degeneracy row lives on the `(2,3)` coordinates rather than on the single complementary prime coordinate. The independent barrier is therefore not an artifact of one support placement.

## 5. Architecture consequence — three different future questions

The exact examples separate three future languages:

1. **Arithmetic demand:** how large must any certificate be merely to carry the multiplicity load? Answered by `lambda_abc`.
2. **Additive feasibility:** at what radius does the relation lattice `T` contain any nonzero state? Answered by `rho`.
3. **Non-degenerate certification:** at what radius does a state escape `T^circ` and actually produce a usable Wronskian certificate? Answered by `mu`.

The implication chain is only

\[
\lambda_{abc}\le\mu,
\qquad
\rho\le\mu.
\]

There is no equality principle

\[
\mu=\max(\lambda_{abc},\rho)
\]

in general.

Therefore the degeneracy/Pluecker information retained by the full witness flag is not redundant for the certificate language.

This directly supports the earlier architectural separation

\[
\boxed{
\text{relation lattice state}
\ne
\text{non-degenerate certificate state}.
}
\]

It is exactly the kind of future-language distinction demanded by P023: an erasure that is safe for “does any additive state exist?” can be unsafe for “does a usable certificate exist?”.

## 6. What this does not prove

The examples do not show that `eta_nd` is asymptotically large on abc-exceptional triples, nor that it is unbounded over all primitive triples.

They establish only the necessary structural boundary:

\[
\boxed{\eta_{nd}\text{ can be strictly positive and materially large on exact finite states}.}
\]

Any asymptotic statement about the distribution or growth of `eta_nd` requires separate proof.

## 7. Executable assets

This generation adds:

- `src/enterprise_math/witness_precision_layers.py`;
- `tests/test_witness_precision_layers.py`.

The executable layer computes the exact bounded additive radius `rho`, combines it with `lambda_abc`, `mu`, and `U_2`, and locks the two explicit degeneracy-barrier examples above.

Finite enumeration is used only as an oracle for the stated bounded examples; the numerical values in Sections 3--4 are proved directly from their integer relation equations.

## 8. Ownership / prior-art boundary

Shortest vectors in integer lattices, nested sublattices, and relative minima are established mathematics. P025 does not claim them as new.

The project-specific value is the exact pressure-test result that the existing P025 generator flag has a real future-language obligation: its degeneracy component cannot be discarded merely because the additive kernel and arithmetic demand are already known.

This remains a P025 specialization / Foundation-boundary witness, not a new generic lattice-theory mother theorem.

## 9. Next frontier

The remaining high-value questions are now narrower:

1. characterize `mu` as a relative minimum of the quotient/flag `T/T^circ` without overclaiming novelty;
2. determine when `eta_nd=0` from the generator signature alone;
3. test whether `eta_nd>0` correlates with the proof-loss shells from Supplement 05;
4. search high-quality triples specifically for cases where the witness-pressure floor is strengthened by non-degeneracy rather than arithmetic demand alone;
5. route the exact counterexamples to Foundation FQ-004 as evidence for keeping relation and certificate layers distinct.
