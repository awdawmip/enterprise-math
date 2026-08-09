# P022 — Barlow Coordination Precision and Quadratic Drift Energy

Status: `ACTIVE RESEARCH NOTE / EXACT INTEGER GEOMETRY / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: Barlow prefix normal form and exact graph-shell language  
Purpose: separate the minimum state required by **vertex cardinality** from the much richer state required by **geodesic path multiplicity**

## 1. Why coordination cardinality deserves a separate precision analysis

The preceding Barlow results showed that shortest-path multiplicity can read a large part of the prefix-imbalance trajectory.

For a radius-`n` whole shell, the exact geodesic path total depends on

\[
(|\delta_{-n}|,\ldots,|\delta_n|).
\]

It would be easy to assume that shell **vertex count** needs comparable information.

It does not.

After forgetting witness multiplicity and asking only which vertices exist on a native graph shell, nearly the entire stacking history disappears. The exact shell cardinality depends only on a single quadratic integer formed from the two extreme prefix imbalances.

This gives a particularly sharp example of task-relative precision inside one and the same intrinsic geometry.

## 2. Vertical-prefix support as a Minkowski sum

Fix a target layer `k`. Put

\[
q=|k|,
\qquad
\delta=\delta_k,
\qquad
d=|\delta|,
\qquad
c=\frac{q-d}{2}.
\]

The vertical witness polynomial has normal form

\[
P_k=(A+3)^cB_\pm^d.
\]

For **support** rather than multiplicity, coefficients are Booleanized.

The support of `A+3` is the origin together with the six triangular primitive steps. Its `c`-fold Minkowski sum is exactly the triangular hex-ball

\[
H_c=\{(u,v):\max(|u|,|v|,|u+v|)\le c\}.
\]

The support of `B_+^d` is the discrete oriented triangle

\[
\Delta_d^+
=\{(i,j):i,j\ge0,\ i+j\le d\},
\]

and `B_-^d` is its reflected translate/orientation.

Therefore

\[
\boxed{
\operatorname{supp}P_k
=H_c+\Delta_d^{\pm}.}
\]

Only `c` and `d` remain. Literal interface order is already gone.

## 3. P022-BC01 — exact vertical-support cardinality

For definiteness take the plus orientation. The Minkowski sum can be written as

\[
H_c+\Delta_d^+
=
\{(q,r):
-c\le q\le c+d,
-c\le r\le c+d,
-c\le q+r\le c+d
\}.
\]

Start from the square

\[
[-c,c+d]^2.
\]

It has side length in lattice points

\[
2c+d+1.
\]

The two forbidden corner triangles are

\[
q+r<-c
\]

and

\[
q+r>c+d.
\]

Each contains

\[
\binom{c+d+1}{2}
\quad\text{or the corresponding reflected count,}
\]

and direct simplification gives

\[
\boxed{
K(c,d)
=3c^2+3(d+1)c+\binom{d+2}{2}.}
\]

The same count holds for the minus orientation by reflection.

Equivalent form in terms of vertical length `q` and absolute imbalance `d`:

\[
\boxed{
4K
=3q^2+6q+4-d^2.}
\]

Thus even the extreme-layer support does not need the sign of the imbalance; only its square remains in cardinality.

## 4. P022-BC02 — every non-extreme shell layer is stacking-independent

Now fix a whole graph-shell radius `n` and a target layer with

\[
q=|k|<n.
\]

A shortest path to this shell layer contains

\[
t=n-q>0
\]

in-layer triangular steps.

At the support level, multiplying by `A^t` expands the hex-ball component:

\[
H_c+\Delta_d
\longrightarrow
H_{c+t}+\Delta_d.
\]

The exact shell layer is the difference between the radius-`t` and radius-`t-1` expansions. Therefore

\[
S_n(k)
=K(c+t,d)-K(c+t-1,d).
\]

Using BC01,

\[
K(s,d)-K(s-1,d)=6s+3d.
\]

Substitute

\[
s=c+t
=\frac{q-d}{2}+n-q.
\]

The `d` terms cancel exactly:

\[
\boxed{
S_n(k)=3(2n-q),
\qquad |k|<n.}
\]

This is a strong universality theorem:

> **every non-extreme horizontal layer of a Barlow graph shell has the same number of vertices, independent of the stacking word and independent of its prefix imbalance.**

Stacking information survives in shell cardinality only at the top and bottom extreme layers.

## 5. P022-BC03 — extreme layers retain one quadratic drift coordinate

For an extreme layer `|k|=n`, no in-layer expansion occurs. BC01 gives

\[
\boxed{
S_n^{\mathrm{ext}}(k)
=
\frac{3n^2+6n+4-\delta_k^2}{4}.}
\]

Since only `delta_k^2` appears, horizontal-layer cardinality erases the orientation/sign of the stacking drift.

Conversely,

\[
\boxed{
\delta_k^2
=3n^2+6n+4-4S_n^{\mathrm{ext}}(k).}
\]

Because `|delta_k|` is a non-negative integer with the parity of `n`, the extreme-layer vertex count reconstructs `|delta_k|` exactly.

Thus for an identified top or bottom extreme layer, the minimum stacking state for its cardinality language is

\[
\boxed{|\delta_{\pm n}|}
\]

up to finite relabeling.

## 6. P022-BC04 — whole-shell cardinality needs only one drift energy

The central layer and all non-extreme positive/negative layer pairs sum to

\[
9n^2-3n.
\]

Add the two extreme layers. Define the radius-`n` quadratic drift energy

\[
\boxed{
Q_n=\delta_n^2+\delta_{-n}^2.}
\]

Then the whole coordination shell has exact cardinality

\[
\boxed{
4S_n=42n^2+8-Q_n.}
\]

Equivalently,

\[
\boxed{
S_n
=\frac{21n^2}{2}+2-rac{Q_n}{4}.}
\]

This formula is valid for every finite two-sided Barlow stacking window. No periodicity is required.

It is also exactly invertible:

\[
\boxed{
Q_n=42n^2+8-4S_n.}
\]

Therefore the complete whole-shell **vertex-count language at one radius** factors through one integer and no smaller exact quotient can identify two distinct represented values of `Q_n`:

\[
\boxed{
\text{minimum shell-cardinality state}=Q_n
}
\]

up to finite relabeling.

The whole shell loses how that energy is split between the two sides. For example, `(5,1)` and `(1,5)` have the same `Q_n=26` and hence the same shell cardinality.

## 7. FCC and HCP are immediate special cases

### FCC / constant drift

For the constant-sign stacking,

\[
|\delta_n|=|\delta_{-n}|=n,
\]

so

\[
Q_n=2n^2.
\]

Hence

\[
\boxed{S_n^{FCC}=10n^2+2.}
\]

This recovers the historical `A_3` shell formula.

### HCP / alternating stacking

For HCP,

\[
|\delta_{\pm n}|=
\begin{cases}
0,&n\text{ even},\\
1,&n\text{ odd}.
\end{cases}
\]

Therefore

\[
S_n^{HCP}
=
\begin{cases}
\frac{21n^2}{2}+2,&n\text{ even},\\
\frac{21n^2}{2}+\frac32,&n\text{ odd},
\end{cases}
\]

or compactly

\[
\boxed{S_n^{HCP}=\left\lfloor\frac{21n^2}{2}\right\rfloor+2.}
\]

This reproduces the known HCP coordination sequence.

## 8. P022-BC05 — crystal-ball cardinality needs only cumulative quadratic energy

Let

\[
B_n=\sum_{r=0}^{n}S_r
\]

be the number of vertices in the native graph ball, and define cumulative drift energy

\[
\boxed{
E_n=\sum_{r=1}^{n}Q_r
=\sum_{r=1}^{n}(\delta_r^2+\delta_{-r}^2).}
\]

Summing BC04 yields

\[
\boxed{
4B_n
=4+7n(n+1)(2n+1)+8n-E_n.}
\]

The inverse is again exact:

\[
\boxed{
E_n
=4+7n(n+1)(2n+1)+8n-4B_n.}
\]

So if the future language asks only for the **single ball cardinality at radius `n`**, all shell-resolved stacking history collapses to one integer cumulative energy `E_n`.

If ball counts are queried at every radius, then successive differences recover the individual `Q_r`; again the required state depends on the declared query set.

## 9. Strict comparison with geodesic multiplicity precision

At the same radius `n`, the exact shell **path total** generally requires

\[
(|\delta_{-n}|,\ldots,|\delta_n|),
\]

because each intermediate target layer contributes a different multiplicity factor.

The exact shell **vertex count** needs only

\[
Q_n=\delta_n^2+\delta_{-n}^2.
\]

Thus

\[
\boxed{
\text{coordination cardinality precision}
\ll
\text{geodesic multiplicity precision}.}
\]

This is not a heuristic comparison. Explicit different stacking words can have the same `Q_n` and therefore the same shell cardinality while their intermediate imbalance trajectories—and hence their path totals and multiplicity spectra—differ.

The geometry itself has not changed; only the future observable has.

## 10. P022-BC06 — asymptotic shell and ball growth read an `L^2` drift statistic

Assume the one-sided absolute drift densities exist:

\[
\mu_+=\lim_{n\to\infty}\frac{|\delta_n|}{n},
\qquad
\mu_-=\lim_{n\to\infty}\frac{|\delta_{-n}|}{n}.
\]

Divide BC04 by `n^2`:

\[
\boxed{
\lim_{n\to\infty}\frac{S_n}{n^2}
=
\frac{21}{2}
-rac{\mu_+^2+\mu_-^2}{4}.}
\]

Likewise, since

\[
E_n
\sim
\frac{\mu_+^2+\mu_-^2}{3}n^3,
\]

BC05 gives

\[
\boxed{
\lim_{n\to\infty}\frac{B_n}{n^3}
=
\frac72
-rac{\mu_+^2+\mu_-^2}{12}.}
\]

So asymptotic coordination growth reads the squared Euclidean size of the two-sided drift vector

\[
(\mu_+,\mu_-).
\]

By contrast, the preceding aperiodic geodesic-growth theorem reads

\[
\mu_*=\max(\mu_+,\mu_-),
\]

the `L^infinity` size of that same vector.

Two observables therefore probe genuinely different summaries of the same hidden stacking state.

## 11. P022-BC07 — combined asymptotic observables reconstruct both drift magnitudes

Let

\[
C_S
=\lim_{n\to\infty}\frac{S_n}{n^2}.
\]

BC06 gives

\[
\boxed{
R_2:=\mu_+^2+\mu_-^2
=42-4C_S.}
\]

Let the shell-total geodesic multiplicity growth constant be

\[
\Lambda
=\lim_{n\to\infty}T_n^{1/n}.
\]

The aperiodic drift theorem gives

\[
\Lambda=2+2^{(1+M)/2},
\qquad
M=\max(\mu_+,\mu_-).
\]

The right-hand side is strictly increasing for `M in [0,1]`, so `Lambda` determines `M` uniquely.

Then the smaller drift magnitude is

\[
\boxed{
m=\sqrt{R_2-M^2}.}
\]

Therefore the pair of asymptotic observables

\[
\boxed{(C_S,\Lambda)}
\]

recovers the unordered hidden drift pair

\[
\boxed{\{\mu_+,\mu_-\}.}
\]

The top/bottom label is not recoverable from whole-shell observables because those observables are symmetric under exchanging the two sides. A one-sided shell or extreme-layer observable restores that orientation information.

This is a concrete reconstruction theorem: two different low-precision shadows, neither sufficient alone, become jointly sufficient for the two drift magnitudes.

## 12. Periodic exact coefficients

For a periodic stacking of period length `L` and absolute period drift `|D|`, both sides have

\[
\mu=|D|/L.
\]

The shell quadratic coefficient is the exact rational number

\[
\boxed{
\frac{21}{2}-\frac{\mu^2}{2}
=
\frac{21L^2-D^2}{2L^2}.}
\]

The ball cubic coefficient is

\[
\boxed{
\frac72-\frac{\mu^2}{6}
=
\frac{21L^2-D^2}{6L^2}.}
\]

These can be stored by reduced integer numerator/denominator pairs. No floating-point asymptotic state is needed for periodic stackings.

## 13. Precision ladder exposed by one geometry

The Barlow family now gives several exact state requirements for different observables:

### Coordinate-sensitive endpoint distance + path count on layer `k`

\[
\delta_k.
\]

### Whole horizontal-layer geodesic path total

\[
|\delta_k|.
\]

### Whole radius-`n` geodesic path total

\[
(|\delta_{-n}|,\ldots,|\delta_n|).
\]

### Identified extreme-layer vertex count

\[
|\delta_{\pm n}|.
\]

### Whole radius-`n` shell vertex count

\[
Q_n=\delta_n^2+\delta_{-n}^2.
\]

### One radius-`n` ball vertex count

\[
E_n=\sum_{r\le n}Q_r.
\]

### Periodic geodesic-growth exponent

\[
|D|/L.
\]

### Aperiodic asymptotic coordination coefficient

\[
\mu_+^2+\mu_-^2.
\]

There is no single scalar called “the precision of the geometry” that dominates these requirements correctly. Precision is indexed by the declared operation/observation language.

This concrete hierarchy is one of the strongest P022 specializations so far of the P023/P024 future-language principle.

## 14. Executable assets

Added:

- `src/enterprise_math/p022_barlow_coordination.py`;
- `tests/test_p022_barlow_coordination.py`.

The tests compare the support and shell formulas against explicit Barlow polynomial/contact-graph enumeration for all short periodic patterns, verify FCC/HCP specializations, and check the exact inverse maps from shell/ball cardinalities back to quadratic drift energies.
