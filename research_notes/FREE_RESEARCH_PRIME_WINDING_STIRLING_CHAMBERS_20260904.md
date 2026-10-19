# Free Research — Prime-Winding Stirling Chamber Law

Status: `FREE_RESEARCH_FRONTIER / LOG_SIMPLEX_LIMIT / STIRLING_CHAMBER_PARTITION / THREE_FACTORIAL_CORE / TAIL_HALF_RECOVERED / MIXER_COEFFICIENT_ALIGNMENT / INTERTWINER_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_WEIGHTED_TRIPLE_BRANCH_REALIZATION_20260904.md`

## 1. Executive advance

The moving-cutoff tail coefficient `1/2`, the degree-three `3!` provenance core, and the weighted `S_3` mixer coefficient `1/9` fit into one logarithmic chamber geometry.

For prime-power winding weights

\[
u_a=\frac{\Lambda(a)}a,
\qquad
A(X)=\sum_{a\le X}u_a=\log X+O(1),
\]

normalize the action scale by

\[
t_a=\frac{\log a}{\log Y}.
\]

The weighted prime-power cloud converges on bounded scale intervals to Lebesgue measure in the coordinate `t`.  An `r`-fold product constraint

\[
a_1\cdots a_r\le Y^r
\]

therefore becomes the positive simplex

\[
\Delta_r=\{t_i\ge0:\ t_1+\cdots+t_r\le r\}.
\]

Partition this simplex by how many coordinates cross the current cutoff `t=1`.  The chamber volumes are exact Stirling-number coefficients:

\[
\boxed{
\operatorname{Vol}\{t\in\Delta_r:\text{ exactly }k\text{ coordinates exceed }1\}
=rac{S(r,r-k)}{k!}.
}
\]

This is the general cutoff-renormalization law.

---

## 2. Logarithmic equidistribution of winding mass

For each fixed `x>=0`,

\[
\frac{A(Y^x)}{A(Y)}
=\frac{x\log Y+O(1)}{\log Y+O(1)}
\longrightarrow x.
\tag{2.1}
\]

Thus the normalized measure

\[
\nu_Y:=A(Y)^{-1}\sum_a u_a\,\delta_{\log a/\log Y}
\]

converges locally to Lebesgue measure on the positive real axis.

Consequently, for every fixed polytope whose boundary has zero Lebesgue measure, the corresponding finite prime-power product mass converges to its Euclidean volume.

In particular,

\[
\boxed{
A(Y)^{-r}
\sum_{a_1\cdots a_r\le Y^r}
\prod_{i=1}^r\frac{\Lambda(a_i)}{a_i}
\longrightarrow
\operatorname{Vol}(\Delta_r)
=rac{r^r}{r!}.
}
\tag{2.2}
\]

No PNT normalization is required beyond the already established first-mass estimate `A(X)=log X+O(1)`.

---

## PSC-T01 — Fixed overcut-set chamber volume

Fix a prescribed set `K` of `k` coordinates required to exceed `1`.  Let

\[
j=r-k
\]

be the number of coordinates constrained not to exceed `1`.

Shift each overcut coordinate down by one.  The new positive simplex has total budget `j`, while the `j` unshifted coordinates retain the upper bound `1`.  Inclusion-exclusion gives

\[
\begin{aligned}
\operatorname{Vol}(\Delta_{r,K})
&=\frac1{r!}
\sum_{h=0}^{j}(-1)^h\binom jh(j-h)^r\\
&=\frac{j!S(r,j)}{r!}.
\end{aligned}
\tag{3.1}
\]

Hence

\[
\boxed{
\operatorname{Vol}(\Delta_{r,K})
=\frac{(r-k)!S(r,r-k)}{r!}.
}
\tag{3.2}
\]

---

## PSC-T02 — Total chamber volume by cutoff deficiency

There are `choose(r,k)` possible prescribed overcut sets.  Multiplying (3.2) gives

\[
\boxed{
V_{r,k}
:=\operatorname{Vol}\{\text{exactly }k\text{ overcut coordinates}\}
=\frac{S(r,r-k)}{k!}.
}
\tag{4.1}
\]

The chambers partition the full simplex, so

\[
\boxed{
\sum_{k=0}^{r}rac{S(r,r-k)}{k!}
=rac{r^r}{r!}.
}
\tag{4.2}
\]

Multiplying by `r!` yields the integer identity

\[
\boxed{
\sum_{j=0}^{r}S(r,j)\,r^{\underline j}=r^r,
}
\tag{4.3}
\]

where

\[
r^{\underline j}=r(r-1)\cdots(r-j+1).
\]

Combinatorially, the `j`th term counts functions from `r` history positions to `r` scale bins whose image has size exactly `j`: choose the image labels and then choose a surjection onto them.

Thus cutoff deficiency `k=r-j` is the geometric counterpart of missing image labels.

---

## 5. Degree two: the moving-cutoff half

For `r=2`,

\[
S(2,2)=1,
\qquad
S(2,1)=1.
\]

Therefore

\[
V_{2,0}=1,
\qquad
V_{2,1}=1.
\]

The full simplex has volume `2`.  The core square `a,c<=Y` has volume `1`; the cross-tail region has total volume `1`.

There are two orientations for the single overcut coordinate, each of fixed-set volume

\[
\boxed{1/2.}
\]

This recovers the moving-cutoff result

\[
\sum_{a\le Y}u_a\sum_{Y<c\le Y^2/a}u_c
=\frac12U_Y^2+O(U_Y)
\]

as the first nontrivial Stirling chamber coefficient.

---

## 6. Degree three: `3!`, the tail chambers, and `1/9`

For `r=3`, the image-size chamber counts after multiplying volume by `3!` are

\[
\begin{array}{c|c|c|c}
\text{image size }j&\text{cutoff deficiency }k&
3!V_{3,k}&V_{3,k}\\ \hline
3&0&6&1\\
2&1&18&3\\
1&2&3&1/2
\end{array}
\]

Equivalently,

\[
\boxed{3^3=6+18+3.}
\tag{6.1}
\]

The three classes have direct meanings:

- `6=3!`: the bijective/permutation sector, corresponding to the full three-history provenance core;
- `18`: maps using exactly two scale bins, corresponding to one missing bin or one overcut direction;
- `3`: constant maps, corresponding to two missing bins or the deepest overcut chamber.

Normalized by all `3^3=27` maps, the probabilities are

\[
\boxed{
\frac29,\qquad\frac23,\qquad\frac19.
}
\tag{6.2}
\]

The final coefficient `1/9` equals the quadratic survival factor of the global weighted `S_3` lift–transpose–project mixer:

\[
\mathcal E(\mathcal K_3x)=\frac19\mathcal E(x).
\]

At present this equality of coefficients is a structural alignment, not yet an intertwining theorem identifying the surviving standard energy with the deepest chamber mass.  It is the next natural target.

---

## 7. New geometric interpretation of the factorial factor

The coefficient `3!` now has two compatible finite meanings in the same degree-three carrier:

1. six ordered shortest histories recoalesce at one Hamming shell-3 endpoint;
2. six bijections form the full-image chamber among all `3^3` maps from history slots to scale bins.

Therefore

\[
\boxed{
3!
=\text{ordered provenance-fiber size}
=\text{surjective degree-three cutoff-chamber count}.
}
\]

The non-surjective maps are precisely cutoff-degenerate histories.  Prime-winding renormalization extends the factorial core by adjoining these Stirling deficiency chambers.

This sharpens the earlier statement that the factor `6` is not sixfold spatial degeneracy: it is the full-image sector of a finite history/scale map geometry.

---

## 8. Exact formalization and checks

Lean file:

- `EnterpriseMath/Relation/PrimeWindingStirlingChambers.lean`.

It formalizes:

1. the image-size chamber count
   \[
   S(r,j)r^{\underline j};
   \]
2. the total partition
   \[
   \sum_jS(r,j)r^{\underline j}=r^r;
   \]
3. the degree-two chamber counts;
4. the degree-three counts `6,18,3`;
5. the factorial core and normalized deepest fraction `1/9`.

Exact checker:

- `scripts/check_free_research_prime_winding_stirling_chambers.py`.

It verifies with integers and `Fraction`:

1. inclusion-exclusion chamber volumes;
2. equality with Stirling coefficients;
3. the full simplex partition through degree ten;
4. direct enumeration of functions by image size through degree seven;
5. all degree-two and degree-three specializations.

Lean-green status is not claimed until workflow completion.

---

## 9. Updated next theorem

Construct an explicit finite intertwiner between:

- the standard-representation survival of the weighted `S_3` lift–project mixer; and
- the constant-map/deepest cutoff chamber of normalized mass `1/9`.

A successful intertwiner would identify each surviving same-scale fluctuation after one history-mixing step with a doubly overcut history that necessarily descends to a lower scale.  This would convert the coefficient coincidence into a rigorous `1/9` renormalization cascade.
