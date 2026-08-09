# A3 Guard-Image Lattice Supplement 03 — Fixed Hidden Rank, Recession Quotients, and Polynomial Branch Geometry

Status: `RESEARCH WIP / GENERAL FIXED-RANK REDUCTION THEOREM + PRIOR-ART COMPLEXITY COROLLARY`

## 1. What rank two was revealing

Supplement 02 gave three exact certificate regimes for `rank L_G=2`:

1. strict recession;
2. a recession ray or line;
3. a bounded polygon.

These are not two-dimensional accidents. They are the low-dimensional form of a general quotient structure.

Let

\[
L_G=W(K_A)\subseteq\mathbb Z^r
\]

have rank

\[
\boxed d.
\]

After taking an exact integer basis of the lattice with standard Hermite/Smith-type reduction, every guard-score vector in one coarse fiber has the form

\[
\boxed{g+Hz,\qquad z\in\mathbb Z^d.}
\]

A fixed threshold pattern `sigma` therefore becomes a finite integer linear system

\[
\boxed{A_\sigma z\ge b_\sigma.}
\]

Thus high-rank A3 branch reachability is integer linear feasibility in exactly `d` hidden variables.

## 2. Homogeneous recession cone

Define the real recession cone

\[
C_\sigma=\{u\in\mathbb R^d:A_\sigma u\ge0\}.
\]

Let

\[
U_\sigma=\operatorname{span}_{\mathbb R}C_\sigma,
\qquad
S_\sigma=U_\sigma\cap\mathbb Z^d.
\]

`S_sigma` is a saturated sublattice of `Z^d`.

Split constraint rows `a_i` into:

- **static rows**: `a_i|_U=0`; they are invariant under every recession-span displacement and depend only on the quotient class `[z] in Z^d/S`;
- **dynamic rows**: `a_i|_U != 0`; they can eventually be made strict by moving in a relative-interior direction of the recession cone.

## 3. A3-G11 — Recession-Quotient Feasibility Theorem

For

\[
Az\ge b,
\qquad z\in\mathbb Z^d,
\]

with `C,U,S` as above,

\[
\boxed{
Az\ge b\text{ has an integer solution}
\iff
\exists[z]\in\mathbb Z^d/S
\text{ satisfying every static inequality}.
}
\]

The forward direction is immediate.

Conversely, let an integer representative `z_0` of such a quotient class satisfy all static rows. Because `C` is a rational polyhedral cone, its relative interior in `U` contains a rational point and therefore, after integer scaling, an integer point

\[
u\in\operatorname{relint}(C)\cap\mathbb Z^d.
\]

Static rows satisfy `a_i u=0`. A dynamic row is not identically zero on `U`; a relative-interior point of `C` therefore satisfies

\[
\boxed{a_i u>0.}
\]

For a sufficiently large integer `N`,

\[
z=z_0+Nu
\]

keeps every static inequality unchanged and satisfies every dynamic inequality. Hence an integer feasible point exists.

## 4. A3-G12 — The static feasible quotient is bounded

Project the static inequalities to the real quotient space

\[
\mathbb R^d/U.
\]

Their feasible set cannot have a nonzero recession direction.

Otherwise a lift `v notin U` would satisfy every static homogeneous inequality. Taking the relative-interior recession direction `u` above and choosing sufficiently large `T` makes all dynamic homogeneous inequalities hold as well, so

\[
v+Tu\in C\subseteq U.
\]

Since `u in U`, this implies `v in U`, a contradiction.

Therefore

\[
\boxed{
\text{after quotienting the full recession span, the remaining feasibility problem is bounded.}
}
\]

Unboundedness is not an infinite source of arithmetic complexity; it can be structurally removed.

## 5. A3-G13 — Pattern arithmetic defect rank

Define

\[
\boxed{
\delta_\sigma=d-\dim U_\sigma.
}
\]

This is not a physical dimension. It is a pattern-specific index of the integer dimension remaining after every recession direction has been removed.

- `delta_sigma=0`: no nontrivial quotient remains, so the pattern is automatically reachable;
- `delta_sigma=1`: only a one-dimensional bounded/static integer interval or congruence problem remains;
- `delta_sigma=2`: a genuinely two-dimensional bounded integer-hole problem remains;
- generally, all arithmetic difficulty is confined to a bounded quotient of rank `delta_sigma`.

The three rank-two certificate regimes of Supplement 02 are exactly

\[
\boxed{\delta_\sigma=0,1,2.}
\]

## 6. General base-independent regime

If

\[
U_\sigma=\mathbb R^d,
\]

then the quotient rank is zero and there are no nontrivial static obligations. Hence

\[
\boxed{
\delta_\sigma=0
\Longrightarrow
\text{the branch pattern is reachable for every affine base score }g.
}
\]

When `delta_sigma>0`, reachability may depend on base-score residue and integer holes in the bounded quotient.

## 7. A3-G14 — Fixed hidden rank gives a polynomial pattern bound

In an exact hidden-lattice basis, each guard that actually varies on the lattice defines one affine hyperplane in parameter space `R^d`.

Let the number of nonconstant guards be `q`. The maximum total face count for `q` affine hyperplanes in `R^d` is the simple/general-position arrangement value

\[
\boxed{
F_d(q)=\sum_{j=0}^{\min(d,q)}2^j\binom qj.
}
\]

It satisfies

\[
F_d(q)=F_d(q-1)+2F_{d-1}(q-1),
\qquad F_0(q)=1.
\]

A binary threshold pattern is constant on every relative-open face. Integer lattice sampling can remove faces but cannot create extra patterns. Therefore

\[
\boxed{
N_{patterns}
\le
\min\left(2^q,F_d(q)\right).
}
\]

For fixed `d`,

\[
\boxed{F_d(q)=O(q^d).}
\]

So hidden rank, not the syntactic number of guards, controls the combinatorial dimension of branch geometry.

Special cases are

\[
F_1(q)=2q+1,
\qquad
F_2(q)=2q^2+1.
\]

This uses standard hyperplane-arrangement face counting and is not an A3 originality claim.

## 8. A3-G15 — Fixed hidden rank is fixed-dimension ILP

After exact lattice-basis reduction, every branch-pattern query is

\[
A_\sigma z\ge b_\sigma,
\qquad z\in\mathbb Z^d.
\]

Thus, for fixed hidden rank `d`, branch reachability is integer linear programming with a fixed number of integer variables.

Lenstra's classical theorem proves polynomial-time solvability in the input length when the number of integer variables is fixed; later fixed-dimension and parametric ILP work extends this tool family.

Therefore, at the algorithm-existence level,

\[
\boxed{
\text{fixed hidden rank}
\Longrightarrow
\text{exact branch reachability has a polynomial-time fixed-dimension ILP solver}.
}
\]

A3 does not reproduce general Lenstra-style ILP machinery. Its responsibility is the exact reduction from future precision to `d=rank W(K_A)` hidden variables. The rank-one and rank-two solvers remain lightweight A3 specializations that avoid a general ILP engine.

## 9. Implementation

Added:

- `src/enterprise_math/guard_pattern_complexity.py`;
- `tests/test_guard_pattern_complexity.py`.

APIs:

- `arrangement_total_face_bound(q,d)`;
- `arrangement_total_face_recurrence(q,d)`;
- `nonconstant_guard_count(...)`;
- `hidden_guard_pattern_bound(...)`.

Tests verify the rank-one and rank-two closed forms, the deletion/restriction recurrence, the degree-`d` finite-difference property, constant-guard elimination, and the sharper `2^q` truth-pattern cap at full hidden rank.

## 10. Boundary with A2/P023

General behavioral equivalence and minimum future-compatible state remain owned by A2/P023.

A3 contributes the computable integer specialization

\[
K_A
\xrightarrow{W}
L_G
\xrightarrow{\text{integer basis}}
\mathbb Z^d
\xrightarrow{\text{thresholds}}
\text{integer polyhedral feasibility}.
\]

Thus:

- hidden rank `d` is a natural A3 future-precision parameter;
- `delta_sigma` is a pattern-specific residual arithmetic rank;
- general fixed-`d` solving should call established HNF/ILP tooling rather than grow a parallel optimization theory inside A3;
- rank-one/rank-two closed solvers remain A3-specific low-overhead specializations.

## 11. Next

1. make `delta_sigma` executable by extracting the recession-span rank and static rows from a branch pattern;
2. for rank three, implement quotient reduction only, not a duplicate general ILP solver;
3. combine actual reachable branches with branch coarse-effect equality into a state-dependent exact branch-erasure checker;
4. connect the required partition directly to relation-rank / relation-quantum precision cost;
5. pressure-test the machinery on an actual P021 or A3-to-A4 staged-support predicate family.
