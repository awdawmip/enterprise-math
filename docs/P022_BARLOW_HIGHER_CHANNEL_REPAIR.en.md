# P022 — Higher-Channel Orbit-Path Repair Is Mixed-Radix, Not Intrinsically Binary

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE PATH-LIFT THEOREM / CROSS-ROUTE GENERALIZATION CANDIDATE`  
Owner: `program/p022-geometry-v2`  
Depends on: `B_2/C_2` Weyl-quotient repair; signed-channel microscopic dynamics  
Cross-route relevance: A2/P023 quotient-path lifting; A4 witness multiplicity; P024 typed precision

## 1. Why test more than two channels

The two-sided Barlow repair theorem has the striking form

\[
|O^{-1}(h)|=2^{E(h)+B(h)}.
\]

That can tempt an incorrect abstraction:

> every symmetry-breaking repair event is fundamentally one binary bit.

The rank-two model does not justify that conclusion.  This note extends the exact orbit-path calculation to `d` labelled signed channels and shows that non-binary local branching appears immediately at `d=3`.

The correct primitive is an **integer path-lift multiplicity**.  Binary repair is a special factorization of that integer in rank two.

---

## 2. Microscopic and coarse state

Let

\[
x=(x_1,\ldots,x_d)\in\mathbb Z^d.
\]

At one microscopic step every labelled channel changes by one sign:

\[
x_i\mapsto x_i+\epsilon_i,
\qquad
\epsilon_i\in\{-1,+1\}.
\]

There are exactly

\[
2^d
\]

microscopic step choices from every labelled state.

Let the hyperoctahedral group `B_d` act by arbitrary coordinate permutations and independent sign flips.  The canonical orbit representative is

\[
\boxed{
q(x)=\operatorname{sort}(|x_1|,\ldots,|x_d|)
}
\]

in the discrete chamber

\[
0\le a_1\le\cdots\le a_d.
\]

This is the direct higher-rank analogue of the existing two-channel coordination quotient.

---

## 3. P022-HR01 — local transition multiplicity is well defined on the quotient

Fix chamber states

\[
p=(p_1,\ldots,p_d),
\qquad
r=(r_1,\ldots,r_d).
\]

Choose any labelled lift `x` of `p` and define

\[
m(p,r)
=
\#\left\{
\epsilon\in\{\pm1\}^d:
q(x+\epsilon)=r
\right\}.
\]

This number is independent of the chosen labelled lift.

### Proof

Any two lifts `x,x'` of the same chamber state differ by an element `g` of the signed-permutation group `B_d`.

The microscopic step set

\[
\{\pm1\}^d
\]

is invariant under `g`, and

\[
q(gz)=q(z).
\]

Therefore

\[
\epsilon\mapsto g\epsilon
\]

is a bijection between microscopic steps from `x` landing in orbit `r` and microscopic steps from `x'` landing in orbit `r`.

Hence `m(p,r)` is a quotient-transition invariant. ∎

For every fixed `p`,

\[
\boxed{
\sum_r m(p,r)=2^d.
}
\]

---

## 4. P022-HR02 — exact coefficient formula

For a previous chamber coordinate `p_i`, a microscopic sign sends its absolute magnitude to either

\[
|p_i-1|
\]

or

\[
p_i+1.
\]

If `p_i=0`, the two signs both land at magnitude one and therefore produce a coefficient two.

Introduce commuting formal variables

\[
z_0,z_1,z_2,\ldots.
\]

Then

\[
\boxed{
P_p(z)
=
\prod_{i=1}^d
\left(
 z_{|p_i-1|}+z_{p_i+1}
\right).
}
\]

If the target chamber `r` contains magnitude `j` exactly `c_j(r)` times, write

\[
z^r=\prod_j z_j^{c_j(r)}.
\]

Then

\[
\boxed{
m(p,r)=[z^r]P_p(z).}
\]

This is an exact finite integer coefficient.

Grouping equal coordinates of `p` gives the equivalent form

\[
P_p(z)
=(2z_1)^{c_0(p)}
\prod_{a\ge1}
(z_{a-1}+z_{a+1})^{c_a(p)}.
\]

Thus local repair is controlled entirely by the multiplicity pattern of the chamber state.

---

## 5. P022-HR03 — complete path fibers multiply local radices

Let

\[
h=(p_1,p_2,\ldots,p_N)
\]

be a legal chamber path, with the implicit initial state

\[
p_0=(0,\ldots,0).
\]

Every labelled microscopic lift of `p_(t-1)` has exactly

\[
m(p_{t-1},p_t)
\]

outgoing microscopic steps that realize the declared next chamber state, by HR01.

Induction over the time-labelled path therefore gives

\[
\boxed{
|\operatorname{Lift}(h)|
=
\prod_{t=1}^{N}
m(p_{t-1},p_t).
}
\]

Define the local repair-radix sequence

\[
\boxed{
\mathcal M(h)
=
\bigl(
 m(p_0,p_1),
 m(p_1,p_2),
\ldots,
 m(p_{N-1},p_N)
\bigr).
}
\]

Then `mathcal M(h)` is an exact mixed-radix repair coordinate: at transition `t`, one must distinguish one of `m(p_(t-1),p_t)` microscopic lift branches if the future language requires a labelled lift.

No logarithm is needed as primitive state.

---

## 6. P022-HR04 — rank two is the binary special case

For `d=2`, all reachable local multiplicities are

\[
\boxed{1,2,4.}
\]

The existing event theorem classifies those powers of two by zero-wall and diagonal-split events.  Consequently

\[
\prod_t m_t
=2^{E+B}.
\]

Thus the old binary repair dimension is exactly the base-two factorization of the more primitive path-lift product in rank two.

This reinterprets, rather than replaces, the established `E+B` theorem.

---

## 7. P022-HR05 — rank three immediately produces a non-binary radix

Take

\[
p=(1,1,1).
\]

Then

\[
P_p(z)=(z_0+z_2)^3.
\]

For target chamber

\[
r=(0,0,2),
\]

the coefficient is

\[
\boxed{
m(p,r)=3.}
\]

Indeed, exactly one of the three labelled coordinates moves outward from magnitude one to two while the other two move inward to zero.

Therefore a path beginning

\[
(0,0,0)
\to
(1,1,1)
\to
(0,0,2)
\]

has local radices

\[
\boxed{(8,3)}
\]

and total microscopic fiber

\[
\boxed{24.}
\]

This fiber is not a power of two.

Hence:

\[
\boxed{
\text{higher-channel exact repair is not intrinsically a bit count.}
}
\]

Already at rank four one obtains a local factor six, for example

\[
(0,1,1,1)\to(0,0,1,2).
\]

---

## 8. Precision consequence

The correct hierarchy is now:

### Rank two

\[
\text{local lift multiplicity}
\in\{1,2,4\}
\Longrightarrow
\text{binary event bits}.
\]

### General rank

\[
\boxed{
\text{local lift multiplicity}
=m(p,r)\in\mathbb N_{>0}
}
\]

with no reason for `m` to be a power of two.

So a generic precision framework should store an integer branch coordinate, finite witness set, or mixed-radix state.  Converting it immediately to `ceil(log_2 m)` bits can introduce representational slack and hide the actual composition law.

This is directly relevant to P023/P024: **minimal repair is an exact finite state, not necessarily a number of binary flags.**

---

## 9. Relation to the earlier higher-dimensional negative boundary

The coordination-history program had already shown that scalar quadratic-energy history reconstructs the hidden unordered state in two channels but fails at three channels.

HR05 gives a second, independent rank-two boundary:

- state observability by one quadratic history breaks at rank three;
- binary factorization of path-lift repair also breaks at rank three.

These failures have different proofs, but they point in the same direction:

> rank two is unusually compressible and must not be used as evidence that higher-dimensional precision remains one scalar plus a few bits.

---

## 10. Cross-route mother-theorem candidate

The proof of HR01 and HR03 uses only:

1. a finite group acting on a microscopic state space;
2. an invariant transition set;
3. a time-labelled orbit quotient;
4. local lift multiplicity independent of the chosen orbit representative.

That suggests a more general theorem:

> for a `G`-equivariant finite-branching transition system, a quotient path has lift count equal to the product of its local orbit-transition multiplicities.

That statement no longer needs Barlow geometry and therefore should **not** become a P022 mother theorem if promoted.  Its likely homes are A2/P023 quotient-path precision and/or A4 witness multiplicity after owner audit.

P022 retains the exact `B_d` signed-channel specialization and the rank-three non-binary counterexample.

---

## 11. Prior-art boundary

Finite group actions, hyperoctahedral/Weyl groups, orbit graphs, invariant transition systems, polynomial coefficient counting, and path lifting are established mathematical ideas.

No historical-priority claim is made for those ingredients.

The P022-specific result is the exact signed-channel chamber transition polynomial, the product lift formula in this geometry, and its use to prove that the binary repair architecture is a rank-two special case.

Historical novelty of that combination remains `NOVELTY_UNVERIFIED`.

---

## 12. Executable assets

Added:

- `src/enterprise_math/p022_barlow_higher_channel_repair.py`;
- `tests/test_p022_barlow_higher_channel_repair.py`.

The tests verify:

- each transition spectrum sums to `2^d`;
- transition multiplicity is independent of signed/permuted representative;
- the rank-two formula reproduces the existing exact `2^(E+B)` fibers;
- complete rank-three microscopic path grouping agrees with the product formula through short horizons;
- exact local factors three and six appear in ranks three and four.
