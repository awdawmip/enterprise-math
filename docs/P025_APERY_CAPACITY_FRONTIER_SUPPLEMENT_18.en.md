# P025 Supplement 18 — Finite Apéry Capacity Frontiers for the Exact Preperiod

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-access-tail-stage18`  
Base checkpoint: P025 Stage 17 at `6220a5a`  
Depends on: P025 Supplements 16–17; A3/A4 antichain language; P023 task-relative precision  
Hard block: `NONE`

## 1. What Stage 17 still leaves open

Supplement 17 stores, for each defect residue `j mod P`, the Apéry value `a_j` and

\[
q_j(0)=\left\lceil\frac{L_j(0)}2\right\rceil,
\]

where `L_j(0)` is the minimum nonnegative `L_infinity` factorization radius of `a_j`.

This is exactly enough to certify when the **Apéry element itself** fits the signed-access cube. It does not directly describe how access behaves before that tail begins, because a later defect

\[
a_j+kP
\]

can admit a much better bounded factorization than simply adding `k` copies of the all-ones vector to an Apéry factorization.

Example: for row `(1,6)`, residue `j=5` has `a_j=5`, `L_j(0)=5`, hence `q_j(0)=3`. For target `N=2`, the base radius is only `r_0=1`, so the Apéry element does not fit. But one period later the defect is `12=6+6`, whose minimum factorization radius is only `2`, and the exact signed access radius is already `2`.

The preperiod therefore needs a structured finite refinement beyond a single tail threshold.

## 2. P025-D10 — shifted Apéry factorization radius

For every `k>=0` define

\[
\boxed{
L_j(k)
=
\min\left\{
\|y\|_\infty:
 y\in\mathbb N^d,
\ b\cdot y=a_j+kP
\right\}.
}
\]

For a target `N` with

\[
j\equiv-N\pmod P,
\qquad
r_0=\frac{N+a_j}{P},
\]

using access radius `r_0+k` creates defect `a_j+kP` and coordinate capacity `2(r_0+k)`.

Hence this radius is feasible exactly when

\[
L_j(k)\le2(r_0+k).
\]

Equivalently define the **capacity threshold**

\[
\boxed{
q_j(k)
=
\max\left(
0,
\left\lceil
\frac{L_j(k)-2k}{2}
\right\rceil
\right).
}
\]

Then

\[
\boxed{
r_0+k\text{ is feasible}
\iff
q_j(k)\le r_0.}
\]

## 3. P025-T53 — exact access from the capacity sequence

For every nonnegative target `N` in residue `-j`,

\[
\boxed{
\kappa_b(N)
=
r_0+\min\{k\ge0:q_j(k)\le r_0\}.
}
\]

### Proof

At candidate radius `r_0+k`, Supplement 16's signed/nonnegative transform gives defect `a_j+kP` and cap `2(r_0+k)`. By definition of `L_j(k)`, feasibility is equivalent to `L_j(k)<=2(r_0+k)`, which is equivalent to `q_j(k)<=r_0`. Taking the first feasible `k` gives the minimum radius. ∎

Thus the entire preperiod and tail are one threshold-crossing problem in a single finite sequence.

## 4. P025-T54 — the capacity sequence is monotone and finitely reaches zero

Take a factorization of `a_j+kP` attaining `L_j(k)`. Add one to every coordinate. Because `P=sum b_i`, this gives a factorization of `a_j+(k+1)P` with `L_infinity` radius at most `L_j(k)+1`. Therefore

\[
\boxed{
L_j(k+1)\le L_j(k)+1.
}
\]

Consequently

\[
L_j(k+1)-2(k+1)
\le
L_j(k)-2k-1,
\]

and hence

\[
\boxed{
q_j(k+1)\le q_j(k).
}
\]

Moreover, inductively

\[
L_j(k)\le L_j(0)+k,
\]

so

\[
L_j(k)-2k\le L_j(0)-k.
\]

Thus by `k=L_j(0)` one has `q_j(k)=0` at the latest.

Therefore every residue has a finite exact capacity sequence.

## 5. P025-D11 — capacity Pareto frontier

If two consecutive shifts have the same threshold, the later one is useless: it costs a larger `k` while requiring no smaller base radius.

Delete every repeated threshold and retain only the first occurrence of each strict drop:

\[
\boxed{
\mathcal C_j
=
\{(k,q_j(k)):
 k=0\text{ or }q_j(k)<q_j(k-1)\}.
}
\]

As `k` increases, retained `q` strictly decreases. Hence the points are pairwise incomparable in the componentwise order and form a finite Pareto antichain.

For any base radius `r_0`, the exact extra shift is simply the first frontier point with

\[
q\le r_0.
\]

So `C_j` is a complete finite semantic summary for exact access in that residue.

Because `q_j(0)=ceil(L_j(0)/2)` and retained thresholds are distinct nonnegative integers,

\[
\boxed{
|\mathcal C_j|
\le
\left\lceil\frac{L_j(0)}2\right\rceil+1.
}
\]

## 6. Examples

### 6.1 `(1,6)`, target residue `2`

Here `P=7`, defect residue `j=5`, and

\[
a_5=5.
\]

The exact sequence begins

\[
(L_5(0),q_5(0))=(5,3),
\]

while

\[
(L_5(1),q_5(1))=(2,0)
\]

because `12=6+6`.

Thus

\[
\boxed{
\mathcal C_5=\{(0,3),(1,0)\}.
}
\]

For `N=2`, `r_0=1`; the first point with `q<=1` is `(1,0)`, giving

\[
\kappa(2)=1+1=2.
\]

For `N=16`, `r_0=3`; `(0,3)` already applies, giving `kappa(16)=3`.

### 6.2 `(5,2)`, the unique Stage-16 exceptional residue

For defect residue `6`,

\[
\boxed{
\mathcal C_6
=\{(0,2),(1,1),(2,0)\}.
}
\]

So the preperiod is not an arbitrary lookup table; it is a three-level monotone capacity frontier.

### 6.3 `(2,5,7,8)`

For defect residue `6`,

\[
\boxed{
\mathcal C_6=\{(0,2),(1,0)\}.
}
\]

Target `16` has base radius `1`, so the extra shift is one and `kappa(16)=2`; target `38` has base radius `2`, so shift zero already works and `kappa(38)=2`.

## 7. P025-T55 — finite exact response without a target-indexed exception table

Collect all residue frontiers:

\[
\boxed{
\Sigma_{\rm cap}(b)
=
\left(
P,
(a_j,\mathcal C_j)_{j\bmod P}
\right).
}
\]

Given any `N>=0`, recover `j=-N mod P`, compute `r_0=(N+a_j)/P`, find the first `(k,q) in C_j` with `q<=r_0`, and return

\[
\boxed{
\kappa_b(N)=r_0+k.
}
\]

Therefore `Sigma_cap` is a finite exact state reconstructing the entire infinite nonnegative access response.

This does not invalidate Supplement 17's `tail + exception table` representation; it gives a more structural residue-space representation of the same full exact language.

No claim is yet made that `Sigma_cap` is the P023-coarsest possible encoding.

## 8. Relation to A3/A4 antichains and P023

The frontier `C_j` is another worked instance of the already-used antichain pattern:

- one coordinate is extra access shift `k`;
- the other is required current/base precision `q`;
- dominated points can be erased permanently for the declared threshold language.

P025 does not create a new generic Pareto theory. It consumes the antichain language already present in A3/A4 and the task-relative sufficiency rule owned by P023.

The new content is the exact signed-access specialization and its finite defect-capacity reduction.

## 9. Prior-art boundary

Numerical-semigroup Apéry sets, specified-generator factorization statistics, `L_infinity` factorization lengths, and their eventual behavior are prior art, including the sources already registered in Supplements 16–17.

The elementary inequality `L_j(k+1)<=L_j(k)+1` follows from adding the all-ones factorization vector and is not presented as a historical priority claim.

The P025 architecture candidate is the finite precision interface

\[
\boxed{
\text{signed certificate access}
\to
\text{shifted Apéry factorization capacities}
\to
\text{finite Pareto threshold frontier}.
}
\]

Its historical novelty remains `NOVELTY_UNVERIFIED`.

## 10. Executable assets

Added on the Stage-18 owner generation:

- `src/enterprise_math/abc_apery_capacity_frontier.py`
  - exact shifted `L_j(k)` capacity sequence;
  - monotone finite threshold sequence;
  - nondominated capacity frontier;
  - exact full access reconstruction;
  - frontier cardinality bound.
- `tests/test_abc_apery_capacity_frontier.py`
  - `(1,6)` preperiod collapse;
  - `(5,2)` three-level frontier;
  - Stage-17 `(2,5,7,8)` exception reconstruction;
  - full-response comparison with the independent exact access oracle;
  - exhaustive small two-variable checks.

## 11. Next frontier

No hard block exists. Continue with:

1. determine whether `Sigma_cap` has a P023-minimal quotient for the full scalar-access language;
2. characterize which capacity-frontier points can occur from actual arithmetic-derivative block rows rather than arbitrary positive rows;
3. study composition/product laws for several independent block targets;
4. compare capacity frontiers with P024's action-boundary frontiers without merging their distinct semantics;
5. test whether similar shifted-capacity antichains arise for non-abc certificate systems.
