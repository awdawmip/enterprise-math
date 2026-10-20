# R042 — Nonsquare Polygonal Branch-Limit Dimension and Pell-Hit Recurrence

Status: `L2 SEMANTIC CHECKPOINT / PROVED + EXECUTABLE_CHECKED + BOUNDED_EXHAUSTIVE / NOT CANONICAL`

Researcher-ID: `EM-R042-290D7A`

Source lock: `enterprise-math@5e95b8b589ffa75975de165b46f70139b2e0720b`

Consumed frozen owner result: `R040@c1753e11f076d4147a677a3dfa8c76520d7957fb`

Return classification:

`NONSQUARE_BRANCH_LIMIT_FULL_DIMENSION_PROVED / PELL_PRUNING_GEOMETRICALLY_SUBCRITICAL / BRANCH_HIT_RECURRENCE_REDUCED_TO_SPARSE_HIT_ANCESTRY_FOREST / INFINITE_RECURRENCE_OPEN / NOT_CANONICAL`

## 1. Disposition

R042 closes Mother Question A in the full declared nonsquare separated regime.

Let

\[
a=s-2,\qquad c=s-4,\qquad \alpha=\sqrt r,\qquad
z_k=2ak-c,\qquad B=(r-1)c^2,
\]

with nonsquare integer `r>=5`, `s!=4`, and finite nonempty positive initial support. Let `K` be the R040 normalized branch-limit set. Then

\[
\boxed{
\dim_H K=\underline{\dim}_B K=\overline{\dim}_B K
=\frac{\log 2}{\log\sqrt r}.}
\]

Claim status: `PROVED`.

The proof does **not** assert that positive binary prefactor alone implies full Hausdorff dimension. The missing geometric ingredient is an exact bounded-multiplicity cylinder lemma supplied here by the discriminant/integer lattice normalization. Positive survival mass plus that bounded multiplicity yields a Frostman measure.

Mother Question B is narrowed but not fully closed. R042 proves that branches with infinitely many exact-hit times, if they exist, form a Hausdorff-dimension-zero exceptional subset and have zero mass for the positive-survival Bernoulli measure. It also gives exact finite nonconsecutive revisit witnesses, so a blanket `no branch ever revisits the hit set` theorem is false. General infinite nonconsecutive recurrence remains `OPEN` and is reduced exactly to an infinite-ray question in a sparse hit-ancestry forest defined by the unique reverse endpoint oracle.

## 2. Frozen inputs from R040/R035

The following are consumed and not reopened.

1. Endpoint dynamics is the affine-lattice bracketing of
   \[
   W(z)=\sqrt{rz^2-B}
   \]
   on `Lambda_s=2a Z-c`.
2. For nonsquare `r`, `c!=0`, the stable Pell strip is
   \[
   0<N<B\Rightarrow\{G-1,G\},\qquad
   N=B\Rightarrow\{G\},\qquad
   N>B\Rightarrow\{G,G+1\}.
   \]
3. For `r>=5`, distinct-parent recoalescence is absent.
4. Every branch has a uniform normalized limit with geometric tail.
5. For every finite nonempty positive support,
   \[
   |S_t|/2^t\to L>0.
   \]
6. Ambient exact hits up to index `X` are `O(log X)` for fixed nonsquare `(s,r)`.
7. R040 already proved
   \[
   \dim_H K\le\overline{\dim}_B K\le\frac{\log2}{\log\alpha}.
   \]

## 3. Exact normalization simplification

R040 writes

\[
\beta=\frac{c(1-\alpha)}{2a},\qquad
\kappa=\frac{\beta}{1-\alpha}.
\]

Here the fixed point simplifies exactly to

\[
\boxed{\kappa=\frac{c}{2a}.}
\]

Therefore

\[
X_t=\alpha^{-t}(k_t-\kappa)
=\frac{z_{k_t}}{2a\alpha^t}.
\]

This is the useful geometry: at a fixed level `t`, distinct integer endpoint indices have normalized centers separated by at least

\[
\boxed{\alpha^{-t}.}
\]

That exact lattice spacing is the ingredient not contained in the raw cardinality prefactor.

## 4. Uniform cylinder localization

Write the exact inverse

\[
\Phi(k)=\frac{c+\sqrt{rz_k^2-B}}{2a}.
\]

Since

\[
\alpha k+\beta=\frac{c+\alpha z_k}{2a},
\]

we have the exact positive curvature gap

\[
D(k):=(\alpha k+\beta)-\Phi(k)
=\frac{B}{2a\left(\alpha z_k+\sqrt{rz_k^2-B}\right)}.
\]

For positive `k`, `z_k` increases, hence `D(k)<=D(1)`. Every legal child brackets `Phi(k)` within one integer step, so

\[
k_{t+1}=\alpha k_t+\beta+e_t,
\qquad |e_t|\le C:=1+D(1).
\]

Consequently

\[
X_{t+1}-X_t=\alpha^{-(t+1)}e_t,
\]

and every continuation of a prefix `v` at level `t` lies in the cylinder enclosure

\[
\boxed{
K_v\subset
\left[X_t(v)-T\alpha^{-t},\ X_t(v)+T\alpha^{-t}\right],
\qquad T=\frac{C}{\alpha-1}.}
\]

Claim status: `PROVED`.

The checker `tools/r042_polygonal_branch_limit.py` additionally constructs outward **rational** enclosures by replacing `sqrt(r)` and the one required square root in `D(1)` by certified integer-square-root rational bounds.

## 5. Bounded cylinder multiplicity

At level `t`, no recoalescence makes prefix indices distinct. Hence normalized centers are `alpha^-t`-separated.

For any real `x`, if a level-`t` cylinder contains `x`, its center lies within `T alpha^-t` of `x`. Therefore the number of level-`t` cylinders containing the same point is uniformly bounded by

\[
M_0\le \lfloor 2T\rfloor+2.
\]

More generally, a ball of radius `rho<=alpha^-t` can intersect at most

\[
M\le \lfloor2(T+1)\rfloor+2
\]

level-`t` cylinders.

Claim status: `PROVED`.

### Consequence: normalized-limit collisions are harmless

Different infinite branch words are not assumed injective in the limit. Instead, the same counting argument gives a uniform finite fibre bound for the coding map `pi` from legal infinite words to `K`: for any `x in K`, `#pi^{-1}(x)<=M_0`.

Thus kill target `no recoalescence => no normalized-limit overlap` is unnecessary. Finite limit identifications may exist, but they cannot create an entropy-sized collapse.

## 6. Positive-survival symbolic set

First take a singleton positive root. Label the lower and upper children of each two-child node by `0,1`. At an exact-hit one-child node, assign the unique child one fixed label, say `0`; the other bit is invalid.

Because there is no recoalescence, every legal level-`t` node corresponds to exactly one legal binary word of length `t`. Let `A_t` be the union of the corresponding dyadic cylinders in `{0,1}^N`, and let `m` be fair Bernoulli measure. Then

\[
m(A_t)=\frac{|S_t|}{2^t}.
\]

The sets `A_t` decrease, so with

\[
A=\bigcap_t A_t,
\]

R040 positive survival yields

\[
\boxed{m(A)=\lim_t\frac{|S_t|}{2^t}=L>0.}
\]

Claim status: `PROVED`, consuming the R040 prefactor theorem.

This precisely identifies what the prefactor means: not merely entropy, but positive fair-Bernoulli mass of the legal infinite coding set.

## 7. Frostman proof of full dimension

Condition Bernoulli measure on legal infinite words:

\[
\nu(E)=\frac{m(E\cap A)}{L},
\]

and push it forward by the branch-limit coding map `pi`:

\[
\mu=\pi_*\nu.
\]

Fix `rho>0` and choose `t` so that

\[
\alpha^{-(t+1)}<\rho\le\alpha^{-t}.
\]

If `pi(omega)` lies in `B(x,rho)`, then the level-`t` center of its prefix lies within

\[
\rho+T\alpha^{-t}\le(1+T)\alpha^{-t}
\]

of `x`. By the lattice spacing, at most `M` legal level-`t` prefixes can occur. Each prefix cylinder has conditional mass at most

\[
\frac{2^{-t}}{L}.
\]

Hence

\[
\mu(B(x,\rho))\le\frac{M}{L}2^{-t}.
\]

Let

\[
d=\frac{\log2}{\log\alpha}.
\]

Then `2^-t=alpha^{-td}` and `alpha^-t<alpha rho`, so `alpha^d=2` gives

\[
\boxed{
\mu(B(x,\rho))\le\frac{2M}{L}\rho^d.}
\]

By the standard mass-distribution/Frostman principle,

\[
\dim_H K\ge d.
\]

Combining with the frozen R040 upper box bound yields

\[
\boxed{
\dim_H K=\underline{\dim}_B K=\overline{\dim}_B K=d.}
\]

For a finite initial support, apply the singleton result to each root component; a finite union preserves the maximum Hausdorff and box dimensions, and each positive singleton root has the same value `d`.

Claim status: `PROVED`.

## 8. What really protects the dimension

The exact mechanism is now isolated.

Positive prefactor alone is **not** promoted as a general theorem. The sufficient abstract package is:

1. a prefix-closed binary coding tree;
2. `liminf N_t/2^t>0`;
3. level-`t` normalized centers separated by `c_0 alpha^-t`;
4. every level-`t` cylinder localized within `T alpha^-t` of its center;
5. `alpha>1`.

Under those hypotheses, the legal coding set has positive Bernoulli mass and the geometric coding map has uniformly bounded ball multiplicity, so the full symbolic dimension survives.

For polygonal R042, `alpha>2` is not used directly in the Frostman step. It enters upstream through the R035/R040 separated-parent and positive-survival theorems.

This disposes of the dimension kill targets as follows.

- `positive binary prefactor => full Hausdorff dimension`: **NARROWED**. False as a generic slogan; true here only with the lattice-cylinder bounded multiplicity.
- `zero-density Pell defects cannot change geometric dimension`: **PROVED IN THIS SYSTEM BY A STRONGER ARGUMENT**. Zero density alone is not used as the final implication.
- `no cross-parent recoalescence => no normalized-limit overlap`: **NOT NEEDED / STRONG FORM UNPROVED**. Uniform finite limit multiplicity is enough and is proved.
- `square deleted-digit IFS transfers verbatim`: **KILLED**. The proof is a positive-survival non-autonomous tree argument, not exact self-similarity.

## 9. Branchwise exact-hit recurrence: exact reduction

Define the ambient hit set

\[
\mathcal H_{s,r}=\{k\ge1:rP_s(k)\in P_s(\mathbf N)\}.
\]

For `r>=5`, every positive endpoint index has at most one parent because distinct-parent recoalescence is absent. The exact integer checker therefore defines a partial reverse map

\[
\operatorname{par}(j)=k\quad\Longleftrightarrow\quad j\in E_s(rP_s(k)).
\]

This yields a sparse **hit-ancestry forest** on `H_{s,r}`: connect a hit `h'` backward to the nearest hit encountered under repeated `par`, if one exists. Record the edge length as the number of endpoint steps between the two hits.

Then:

> An infinite legal branch has infinitely many exact hits iff the hit-ancestry forest contains an infinite directed ray. The requested nonconsecutive recurrence occurs iff infinitely many edges on that ray have length at least `2`.

Claim status: `PROVED` as an exact reformulation.

This is smaller than ambient Pell solvability: Pell supplies candidate hit vertices; the unique endpoint predecessor map supplies branch accessibility.

## 10. Infinite-recurrence exceptional set has dimension zero

Fix `(s,r)` and a singleton root. R040 gives ambient hit count `O(log X)` up to index `X`, while every level-`t` support index is `O(alpha^t)`. Hence the number `H_t` of hit prefixes at level `t` satisfies

\[
H_t=O(t).
\]

Let `R_infty` be the set of limit points admitting a coding with infinitely many hit prefixes. For every `N`,

\[
R_\infty\subset
\bigcup_{t\ge N}\ \bigcup_{v\in S_t\cap\mathcal H_{s,r}}K_v.
\]

Each `K_v` has diameter at most `2T alpha^-t`. Therefore for any `delta>0`,

\[
\mathcal H^\delta_\infty(R_\infty)
\le
\sum_{t\ge N}O(t)(2T\alpha^{-t})^\delta
\longrightarrow0.
\]

Thus

\[
\boxed{\dim_H R_\infty=0.}
\]

Claim status: `PROVED`.

Moreover, under the conditional Bernoulli measure `nu` used above,

\[
\nu(\text{hit at level }t)
\le \frac{H_t2^{-t}}{L}=O(t2^{-t}),
\]

so the sum over `t` converges. Borel-Cantelli gives

\[
\boxed{\nu(\text{infinitely many hit times})=0.}
\]

Claim status: `PROVED`.

This does not prove emptiness. It proves that any infinite recurrence is an arithmetic zero-dimensional exceptional phenomenon and cannot influence the global dimension theorem.

## 11. Exact finite nonconsecutive revisit witnesses

The exact checker finds multiple branches that hit, leave the hit set, and later hit again. These kill any attempted `at most one hit per branch` shortcut.

### Witness A: `(s,r)=(6,11)`

\[
\boxed{2\to6\to20\to65}
\]

Parents `2` and `65` are exact hits; `6,20` are non-hits.

### Witness B: `(s,r)=(6,15)`

\[
\boxed{1\to3\to10}
\]

Parents `1` and `10` are exact hits; `3` is a non-hit.

### Witness C: `(s,r)=(7,7)`

\[
\boxed{
1\to2\to5\to13\to33\to86\to228\to603\to1595\to4220\to11165\to29540.}
\]

The endpoints `1` and `29540` are exact hits, with ten non-hit parents between them.

### Witness D: `(s,r)=(8,14)`

\[
\boxed{4\to14\to51\to190}
\]

Parents `4` and `190` are exact hits; `14,51` are non-hits.

Claim status: `EXECUTABLE_CHECKED` with exact integer arithmetic.

## 12. Bounded exhaustive recurrence holdout

`R042_BRANCH_HIT_RECURRENCE_ATLAS.json` exhaustively checks

- `s=3..10`, excluding `s=4`;
- nonsquare `r=5..20`;
- every ambient exact-hit parent `1<=k<=200000`;
- exact unique-parent ancestry back to termination.

The maximum number of exact-hit parents found on one checked ancestry is `2`. In particular, no checked branch ancestry contains three exact-hit parents.

Claim status: `BOUNDED_EXHAUSTIVE` only.

This result is **not** promoted to general nonrecurrence. The holdout establishes that any infinite recurrence, if present, is not a small-state phenomenon in this region.

## 13. Pell residue action versus branch reachability

Exact hits satisfy

\[
y^2-rz^2=-B,
\qquad y,z\equiv-c\pmod{2a}.
\]

Let `u+v sqrt(r)` be the fundamental positive Pell unit. Its action on `(y,z)` is the integer matrix

\[
A=\begin{pmatrix}u&rv\\v&u\end{pmatrix}.
\]

Modulo `2a`, this matrix has finite order. Therefore some power is the identity modulo `2a`, recovering R040's statement that a residue-compatible Pell solution generates an infinite ambient residue-compatible orbit.

The checker computes this exact matrix period for representative cells.

However, this is only an **ambient generator**. Membership in such an orbit does not imply branch reachability. R042 certifies reachability separately by iterating the exact reverse endpoint oracle `predecessor()`.

### Why congruence state alone cannot be the full reachability automaton

For any fixed modulus `M`, nonsquare `alpha=sqrt(r)` makes `M alpha` irrational. Hence

\[
\lfloor\alpha(k+M)+\beta\rfloor-
\lfloor\alpha k+\beta\rfloor
\]

takes the two adjacent integer values infinitely often as the irrational phase varies. The R040 Pell-strip exceptions occupy only `O(log K)` indices up to `K`, so they cannot remove the two positive-density mechanical phase classes.

Therefore no eventual rule whose complete state is only `k mod M` can reconstruct the full nonsquare mechanical child phase or exact branch reachability.

Claim status: `PROVED` for **fixed-modulus residue-only** state descriptions.

This does not exclude richer exact automata using continued-fraction/Ostrowski state, expanding phase information, or another non-congruence carrier. R042 does not claim such an automaton impossible.

## 14. Exact experiment/checker disposition

New checker:

`tools/r042_polygonal_branch_limit.py`

It provides:

- exact polygonal endpoint children by integer discriminant square root;
- exact hit classification;
- exact stable Pell norm/boundary classification;
- exact unique predecessor certification;
- support-tree enumeration without floating point;
- branch hit ancestry and backward paths;
- rational `sqrt` bounds and rigorous rational normalized-cylinder enclosures;
- Pell fundamental unit and matrix-period modulo `2a`;
- bounded recurrence scans.

Focused tests:

`tests/test_r042_polygonal_branch_limit.py`

Local result at this checkpoint:

`6 tests / PASS`.

Representative experiment summaries and rational enclosure samples are frozen in `R042_DIMENSION_DISPOSITION.json`. The recurrence holdout is frozen in `R042_BRANCH_HIT_RECURRENCE_ATLAS.json`.

Claim status: `EXECUTABLE_CHECKED` / `BOUNDED_EXHAUSTIVE` as tagged in the JSON artifacts.

## 15. Prior-art boundary

R042 claims no novelty for the following generic ingredients:

- the mass-distribution/Frostman principle used to convert a ball-mass bound into a Hausdorff-dimension lower bound; classical rooting: Otto Frostman, *Potentiel d\'équilibre et capacité des ensembles avec quelques applications à la théorie des fonctions* (1935);
- Moran/self-similar Hausdorff-measure constructions; classical rooting: P. A. P. Moran, *Additive functions of intervals and Hausdorff measure*, Proc. Cambridge Philos. Soc. 42 (1946), 15--23, DOI `10.1017/S0305004100022684`;
- Borel--Cantelli; classical rooting: Borel (1909) and Cantelli (1917);
- polygonal-multiple generalized-Pell recurrence and the fact that higher polygonal cells may have no solution while one admissible solution can generate infinitely many; rooting: J. S. Chahal, M. Griffin, N. Priddis, *When are Multiples of Polygonal Numbers again Polygonal Numbers?*, Hardy--Ramanujan Journal (2019), DOI `10.46298/hrj.2019.5107`, arXiv:`1806.07981`;
- generic symbolic coding and prefix-tree measure constructions.

These are `PRIOR_ART` tools.

The project-local mathematical contribution asserted at this checkpoint is the **exact specialization** to the polygonal rounded discriminant-lattice dynamics:

1. positive-survival Bernoulli mass from the R040 support-loss theorem;
2. exact lattice-scale bounded cylinder multiplicity;
3. the resulting full nonsquare dimension theorem despite Pell pruning;
4. uniform finite coding multiplicity without proving injectivity;
5. zero-dimensionality of infinite-hit recurrent branch limits;
6. the exact hit-ancestry-forest reduction separating ambient Pell solvability from legal branch accessibility.

## 16. Provenance and claim classes

Major claim classes:

- full nonsquare Hausdorff/box dimension equality: `PROVED`;
- uniform finite normalized-limit coding multiplicity: `PROVED`;
- infinite-hit recurrent limit subset has Hausdorff dimension zero: `PROVED`;
- recurrent-hit set has zero survival-Bernoulli measure: `PROVED`;
- exact hit-ancestry forest equivalence: `PROVED`;
- finite nonconsecutive hit revisit witnesses: `EXECUTABLE_CHECKED`;
- no three-hit ancestry in the declared holdout: `BOUNDED_EXHAUSTIVE`;
- existence/impossibility of an infinite nonconsecutive recurrent branch: `CONJECTURAL / OPEN`;
- generic Frostman/Pell/symbolic tools: `PRIOR_ART`.

Machine-readable provenance is in `research_outputs/r042/R042_PROVENANCE_MATRIX.json`.

## 17. Unresolved frontier

The only mother-question frontier left by R042 is now sharply isolated:

> For fixed nonsquare `r>=5`, `s!=4`, can the sparse exact-hit ancestry forest contain an infinite ray?

Equivalently, can one branch intersect the generalized-Pell hit set infinitely often after branch accessibility is enforced by the exact predecessor map?

The next useful attack should **not** revisit dimension or global support entropy. It should work directly on the hit-ancestry forest and try one of two exact routes:

1. prove a finite-height theorem for every Pell residue orbit by comparing the reverse endpoint map with Pell-unit growth; or
2. construct an infinite nested sequence of reachable Pell hits, necessarily lying in the zero-dimensional exceptional coding set proved here.

A finite-modulus residue graph alone cannot settle this frontier.
