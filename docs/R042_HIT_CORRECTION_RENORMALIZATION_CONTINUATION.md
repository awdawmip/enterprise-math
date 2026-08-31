# R042 continuation — Exact Hit Correction Cocycle and Pell-Unit Renormalization

Status: `L2 CONTINUATION SEMANTIC CHECKPOINT / PROVED + EXECUTABLE_CHECKED / NOT CANONICAL`

Researcher-ID: `EM-R042-963283`

Official task: `RS-R042-POLYGONAL-NONSQUARE-BRANCH-LIMIT-PELL-RECURRENCE`

Taskbook source lock: `enterprise-math@5e95b8b589ffa75975de165b46f70139b2e0720b`

Consumed frozen first-stage owner head: `fb03a917f8ea343428d5805348f045910fc28752`

Historical first-stage Researcher-ID: `EM-R042-290D7A` (provenance only; not reused)

Return classification:

`HIT_ANCESTRY_ONTOLOGY_REPLACED / SMALLER_EXACT_RECURRENCE_OBJECT_FOUND / NOT_CANONICAL`

## 0. Continuation contract

This is a continuation of the same R042 task after deletion of the first research conversation. It does **not** reopen any first-stage result.

Frozen and consumed without re-research:

1. for nonsquare integer `r>=5`, `s!=4`, finite nonempty positive initial support,
   \[
   \dim_H K=\underline{\dim}_B K=\overline{\dim}_B K
   =\frac{\log 2}{\log\sqrt r};
   \]
2. an infinite-hit branch-limit subset, if nonempty, has Hausdorff dimension zero;
3. it has zero positive-survival conditioned Bernoulli measure;
4. finite nonconsecutive exact-hit revisits exist;
5. infinite branchwise exact-hit recurrence is equivalent to an infinite directed ray in the exact hit-ancestry forest.

The only frontier addressed here is whether such an infinite reachable hit ray can exist.

No finite-height theorem is claimed below, and no bounded no-witness scan is promoted into a nonrecurrence theorem.

## 1. Discriminant-lattice notation

Keep the R040/R042 notation

\[
a=s-2,\qquad m=2a,\qquad c=s-4,\qquad
\alpha=\sqrt r,\qquad
B=(r-1)c^2,
\]

and

\[
z_k=mk-c\in\Lambda_s=m\mathbf Z-c.
\]

For a legal branch `k_0 -> k_1 -> ...`, write

\[
z_t:=z_{k_t}.
\]

The exact endpoint oracle brackets

\[
W(z)=\sqrt{rz^2-B}
\]

by adjacent points of `Lambda_s`. Thus every legal transition satisfies

\[
|z_{t+1}-W(z_t)|<m
\]

unless it is an exact hit, in which case equality with `W(z_t)` holds.

An exact hit at time `t` is exactly

\[
z_{t+1}^2-rz_t^2=-B.
\]

## 2. A finite exact correction alphabet

Define the one-step linearization error

\[
e_t:=z_{t+1}-\alpha z_t.
\]

Since `z_t>=z_1=s>|c|`,

\[
0<\alpha z-W(z)
=\frac{B}{\alpha z+W(z)}
\le
\frac{B}{\alpha s+W(s)}
=:G.
\]

Therefore every legal branch has the uniform bound

\[
|e_t|<m+G.
\]

Now define the **two-step correction digit**

\[
\boxed{q_t:=z_{t+2}-r z_t.}
\]

Because

\[
q_t
=(z_{t+2}-\alpha z_{t+1})
+\alpha(z_{t+1}-\alpha z_t)
=e_{t+1}+\alpha e_t,
\]

we obtain

\[
\boxed{|q_t|<Q:=(1+\alpha)(m+G).}
\]

Moreover all `z_t == -c (mod m)`, so

\[
\boxed{q_t\equiv(r-1)c\pmod m.}
\]

Hence, for every fixed nonsquare cell `(s,r)`, every legal correction digit belongs to the finite certified outer alphabet

\[
\mathcal Q^{\rm out}_{s,r}
=
\{q\in\mathbf Z:
|q|<Q,\ 
q\equiv(r-1)c\pmod m\}.
\]

Claim status: `PROVED`.

This is only an outer alphabet. A word in this finite set is **not** declared dynamically legal merely from its digits; legal transitions remain certified by the exact endpoint oracle.

That distinction is essential: this construction does not reintroduce the forbidden fixed-modulus residue-only automaton.

## 3. The smaller exact recurrence object

Define the quadratic-field transition element

\[
\boxed{\xi_t:=z_{t+1}+\alpha z_t\in\mathbf Z[\alpha].}
\]

Then the two-step correction identity becomes the exact affine cocycle

\[
\boxed{\xi_{t+1}=\alpha\xi_t+q_t.}
\]

Its conjugate is

\[
\overline{\xi_t}=z_{t+1}-\alpha z_t=e_t,
\]

so the conjugate coordinate stays uniformly bounded along every legal branch.

Its norm is

\[
N(\xi_t)
=
(z_{t+1}+\alpha z_t)(z_{t+1}-\alpha z_t)
=
z_{t+1}^2-rz_t^2.
\]

Therefore

\[
\boxed{\text{time }t\text{ is an exact hit}\iff N(\xi_t)=-B.}
\]

Claim status: `PROVED`.

Thus the R042 recurrence problem may be reformulated exactly as:

> Can one **dynamically legal finite-correction orbit**
> \[
> \xi_{t+1}=\alpha\xi_t+q_t
> \]
> with `q_t in Q_out(s,r)` and every transition certified by the endpoint oracle return to the fixed norm shell `N=-B` infinitely often?

This is strictly smaller than “ambient Pell solutions”: the correction digits and the endpoint oracle carry branch accessibility inside the state evolution itself.

## 4. Exact reverse state: growing-modulus divisibility

Write a transition state as

\[
\xi_t=Y+\alpha Z
\qquad
(Y,Z)=(z_{t+1},z_t).
\]

One reverse step asks for `X=z_{t-1}`. From

\[
q_{t-1}=z_{t+1}-r z_{t-1}=Y-rX
\]

we get the exact formula

\[
\boxed{X=\frac{Y-q_{t-1}}r.}
\]

Consequently a candidate reverse digit `q` is valid only if all of the following hold:

1. `q` is a legal correction value;
2. `Y == q (mod r)`;
3. `X=(Y-q)/r` is a positive affine-lattice endpoint;
4. the exact endpoint oracle certifies `Z in E_s(rP_s(X))`.

Claim status: `PROVED`.

The two-step recurrence decouples parity:

\[
z_{t+2n}
=
r^n z_t+
\sum_{j=0}^{n-1}r^{n-1-j}q_{t+2j},
\]

\[
z_{t+2n+1}
=
r^n z_{t+1}+
\sum_{j=0}^{n-1}r^{n-1-j}q_{t+2j+1}.
\]

Thus a depth-`2n` reverse ancestry is a **base-`r`, growing-modulus correction address** plus exact local accessibility checks. It is not a state depending on one fixed residue modulus.

This gives the first ontology replacement:

`hit-ancestry forest -> legal correction cocycle + growing-modulus reverse address`.

## 5. Pell-unit renormalization: finitely many reduced hit seeds

At an exact hit,

\[
\xi=Y+\alpha Z>0,\qquad
N(\xi)=-B,
\qquad
Y,Z\equiv-c\pmod m.
\]

Let

\[
\varepsilon=u+v\alpha>1
\]

be the fundamental positive Pell unit `u^2-rv^2=1`. Let `p` be the least positive period for which the Pell matrix acts trivially modulo `m`, and put

\[
\eta=\varepsilon^p=U+V\alpha.
\]

Then

\[
U^2-rV^2=1
\]

and

\[
\begin{pmatrix}
U&rV\\
V&U
\end{pmatrix}
\equiv I\pmod m.
\]

Hence multiplication by `eta` preserves the norm `-B` and the affine residue class. It generates ambient residue-compatible hits, exactly as in the first-stage Pell analysis.

The crucial new step is to quotient these ambient hits by the inverse unit while retaining the positive polygonal endpoint domain.

For a positive hit pair `(Y,Z)`, multiplication by `eta^{-1}=U-Valpha` gives

\[
Y^- = UY-rVZ,\qquad
Z^- = UZ-VY.
\]

Because `Y/Z<alpha`,

\[
Z^- >(U-V\alpha)Z=\eta^{-1}Z>0.
\]

For the first coordinate,

\[
Y^->0
\iff UY>rVZ.
\]

Squaring positive sides and using `Y^2=rZ^2-B`,

\[
U^2(rZ^2-B)>r^2V^2Z^2
\iff
rZ^2(U^2-rV^2)>BU^2,
\]

so

\[
\boxed{Y^->0\iff rZ^2>BU^2.}
\]

Also `Z^->eta^{-1}Z`. Therefore if both

\[
rZ^2>BU^2
\quad\text{and}\quad
Z>s\eta,
\]

the inverse-unit pair is again a positive `k>=1`, residue-compatible exact hit.

It follows that every hit that cannot be reduced one further positive unit step satisfies

\[
Z\le
\max\left(U\sqrt{B/r},\,s\eta\right).
\]

There are only finitely many affine-lattice `Z` in that interval.

Hence:

> **Finite Pell-seed theorem.**  
> For every fixed nonsquare `r>=5`, `s!=4`, there is a finite set
> `Sigma_(s,r)={sigma_1,...,sigma_M}` of positive residue-compatible reduced exact hits such that every ambient positive exact hit has a unique representation
> \[
> \boxed{\xi=\eta^m\sigma_i,\qquad m\in\mathbf Z_{\ge0}.}
> \]

Claim status: `PROVED`.

The pair

\[
\boxed{(i,m)=(\text{reduced seed class},\text{Pell-unit rank})}
\]

is therefore a finite-class/unbounded-rank coordinate on every exact hit.

This is not an accessibility theorem: unit translation creates ambient hits, and a translated hit is dynamically reachable only if its exact predecessor chain certifies it.

## 6. Hit-to-hit correction blocks

Suppose a legal branch goes from an exact hit `xi` to a later exact hit `xi'` after `d>=1` endpoint steps.

Iterating

\[
\xi_{t+1}=\alpha\xi_t+q_t
\]

gives

\[
\boxed{
\xi'
=
\alpha^d\xi+P,
\qquad
P=
\sum_{j=0}^{d-1}\alpha^{d-1-j}q_{t+j}.
}
\]

For

\[
C:=\frac{Q}{\alpha-1},
\]

the finite digit bound gives

\[
\boxed{|P|<C\alpha^d.}
\]

Also

\[
P\ne0.
\]

Indeed `P=0` would give `xi'=alpha^d xi`, but then

\[
N(\xi')
=
N(\alpha)^dN(\xi)
=
(-r)^d(-B)\ne-B
\]

for `B>0,r>=5,d>=1`, contradicting that both endpoints are exact hits.

Claim status: `PROVED`.

This nonzero algebraic-integer correction is the basic gap object below.

## 7. Fixed Pell-unit diagonals contain only finitely many reachable hit edges

Write the two hit endpoints in the finite Pell coordinate:

\[
\xi=\eta^m\sigma_i,
\qquad
\xi'=\eta^n\sigma_j,
\qquad
h:=n-m.
\]

Fix `i,j,h`. Then a hit-to-hit edge would satisfy

\[
\eta^m\left(\eta^h\sigma_j-\alpha^d\sigma_i\right)=P
\]

and hence

\[
\left|
\frac{\eta^h\sigma_j}{\alpha^d\sigma_i}-1
\right|
<
\frac C{\eta^m\sigma_i}.
\]

For fixed `i,j,h`, define

\[
\delta_{ijh}
:=
\inf_{d\ge1}
\left|
\frac{\eta^h\sigma_j}{\alpha^d\sigma_i}-1
\right|.
\]

This infimum is strictly positive.

Reason:

- as `d->infinity`, the displayed expression tends to `1`;
- only finitely many small `d` remain;
- equality at any `d>=1` is impossible, because
  \[
  \eta^h\sigma_j=\alpha^d\sigma_i
  \]
  would give equal left/right norms `-B` and `(-r)^d(-B)`, which are unequal.

Therefore every such edge obeys

\[
\eta^m
<
\frac C{\sigma_i\delta_{ijh}},
\]

so only finitely many source ranks `m` occur.

Hence:

\[
\boxed{
\text{For fixed seed classes }i,j
\text{ and fixed unit-rank difference }h,
\text{ only finitely many reachable hit-to-hit edges exist.}
}
\]

Claim status: `PROVED`.

Equivalently, the exact hit ancestry relation on

\[
\Sigma_{s,r}\times\mathbf Z_{\ge0}
\]

is finite on every fixed Pell-unit diagonal `n-m=h`.

This kills every recurrence mechanism based on repeating a fixed Pell translation pattern.

It does **not** kill edges whose unit-rank jump changes without bound.

## 8. Algebraic norm gap forces rank acceleration

The previous theorem is qualitative. The algebraic norm of `P` gives a uniform quantitative restriction.

Since `P in Z[alpha]` is nonzero,

\[
|N(P)|\ge1.
\]

At an exact hit `N(xi)=-B`, so

\[
\bar\xi=-\frac B\xi,
\qquad
\bar\xi'=-\frac B{\xi'}.
\]

Conjugating

\[
P=\xi'-\alpha^d\xi
\]

gives

\[
\bar P
=
-\frac B{\xi'}
-
(-\alpha)^d\left(-\frac B\xi\right).
\]

Assume the source is high enough that

\[
\xi\ge2C.
\]

Then from `|P|<C alpha^d`,

\[
\frac12\alpha^d\xi
<
\xi'
<
\frac32\alpha^d\xi.
\]

Thus

\[
|\bar P|
\le
\frac B\xi\left(\alpha^d+2\alpha^{-d}\right).
\]

Combining with `|P|<C alpha^d`,

\[
1
\le
|N(P)|
<
\frac{CB}{\xi}\left(\alpha^{2d}+2\right).
\]

Since `d>=1` and `alpha^{2d}=r^d>=r`,

\[
\boxed{
\xi
<
D\,\alpha^{2d},
\qquad
D:=CB\left(1+\frac2r\right).
}
\]

Therefore

\[
\boxed{
d
>
\frac{\log\xi-\log D}{2\log\alpha}.
}
\]

So a hit at height `xi` cannot return to the exact-hit shell again after a uniformly bounded number of endpoint steps. Any later exact-hit gap must grow at least like `(1/2) log_alpha xi`.

Now substitute the Pell coordinates

\[
\xi=\eta^m\sigma_i,
\qquad
\xi'=\eta^{m+h}\sigma_j.
\]

The ratio estimate above gives

\[
\alpha^d
<
2\frac{\xi'}{\xi}
=
2\eta^h\frac{\sigma_j}{\sigma_i}.
\]

Together with `xi<D alpha^{2d}`,

\[
\eta^m\sigma_i
<
4D\eta^{2h}
\left(\frac{\sigma_j}{\sigma_i}\right)^2.
\]

Hence for every seed pair `i,j`,

\[
\boxed{
h
>
\frac m2-C_{ij}
}
\]

for an explicit cell-dependent constant `C_ij`.

Since the seed set is finite, there is one cell constant `C_*` such that every sufficiently high reachable hit-to-hit edge obeys

\[
\boxed{
n=m+h
>
\frac32m-C_*.
}
\]

Claim status: `PROVED`.

### Consequence for a hypothetical infinite hit ray

If an infinite reachable exact-hit ray exists, let `m_j` be the Pell-unit rank of its successive hits after discarding a finite initial segment.

Then

\[
m_{j+1}
>
\frac32m_j-C_*.
\]

Thus once `m_j` is beyond a fixed threshold, the ranks grow geometrically.

In particular:

- the unit-rank jumps `h_j=m_{j+1}-m_j` must tend to infinity;
- the endpoint-step gaps between successive hits must also tend to infinity;
- the `j`-th recurrent hit height grows at least doubly exponentially in `j` after a finite prefix;
- equivalently, a hypothetical recurrent branch has at most `O(log log X)` hits with transition height at most `X`.

These are necessary conditions, not existence claims.

## 9. What the new object rules out — and what it does not

### Killed

`FIXED_PELL_TRANSLATION_RECURRENCE`

No fixed seed-pair/unit-gap pattern can generate infinitely many dynamically reachable hit edges.

`BOUNDED_UNIT_GAP_INFINITE_RAY`

An infinite hit ray cannot have Pell-unit rank jumps in any bounded set.

`BOUNDED_BRANCH_GAP_INFINITE_RAY`

A recurrent branch cannot revisit exact hits with uniformly bounded endpoint-step gaps.

### Still open

A ray whose successive hit transitions make increasingly large Pell-unit jumps is not excluded.

The proof does not show that every residue-compatible unit translate eventually loses all predecessor ancestry.

The proof does not show that all reachable hit-to-hit edges lie among Pell-reduced seeds.

The bounded experiments below support that stronger possibility in tested regions, but they are not upgraded to theorem status.

## 10. Exact computation used only as a structural probe

New checker:

`tools/r042_hit_correction_renormalization.py`

It imports the first-stage exact endpoint oracle and adds:

- exact quadratic-field pair arithmetic;
- exact correction digits `q_t`;
- exact hit cocycle certificates;
- exact reverse correction/divisibility state;
- residue-preserving Pell unit computation;
- exact reduced-seed/unit-rank coordinates;
- exact unit translates of ambient hits;
- bounded unit-orbit predecessor exploration.

Focused tests:

`tests/test_r042_hit_correction_renormalization.py`

Local result for this continuation checkpoint:

`6 tests / PASS`.

The four frozen nonconsecutive revisit witnesses give the exact correction blocks:

1. `(s,r)=(6,11)`, `2->6->20->65`
   \[
   q=(4,12,-20),
   \qquad
   P=24+12\sqrt{11},
   \qquad
   N(P)=-1008.
   \]

2. `(s,r)=(6,15)`, `1->3->10`
   \[
   q=(-12,-28),
   \qquad
   P=-28-12\sqrt{15},
   \qquad
   N(P)=-1376.
   \]

3. `(s,r)=(7,7)`, the frozen eleven-step revisit has
   \[
   q=(-2,8,-2,-32,-12,28,8,8,18,18,18).
   \]

4. `(s,r)=(8,14)`, `4->14->51->190`
   \[
   q=(-8,-20,4).
   \]

These are `EXECUTABLE_CHECKED`; they are not needed to prove the general theorems.

A separate exact bounded probe over the declared triangular-cell representatives

\[
(s,r)=(3,6),\qquad
\text{reduced seed representatives }1,3,
\qquad
0\le n\le200
\]

found only the already-known base edge `1->3`; no target with positive tested unit rank had a hit ancestor. The largest fully checked predecessor depth in that declared translated set was `32`.

Status: `BOUNDED_EXHAUSTIVE_FOR_DECLARED_UNIT_TRANSLATES_ONLY`.

No nonrecurrence conclusion is drawn from this absence.

## 11. Prior-art boundary

Generic generalized-Pell unit orbits remain prior art. Generic finite-digit/beta-numeration and quadratic-field continued-fraction machinery may be useful for the next attack, but neither ambient Pell solvability nor generic numeration theory supplies branch accessibility.

The project-local contribution asserted here is the exact coupling:

`endpoint oracle -> finite correction cocycle -> fixed norm return -> finite Pell seed quotient + rank acceleration`.

No claim of novelty is made for generic Pell units, algebraic norms, beta expansions, or quadratic continued fractions.

## 12. Disposition against the requested frontier

The requested finite-height theorem was **not** proved.

An infinite reachable hit ray was **not** constructed.

Instead, the hit-ancestry ontology has been replaced by the strictly smaller exact state:

\[
\boxed{
(\text{Pell seed class }i,\ 
\text{unit rank }m,\ 
\text{legal finite correction address})
}
\]

with exact local reverse accessibility

\[
X=(Y-q)/r
\]

and exact endpoint-oracle certification.

The remaining frontier is now:

> Can there be an infinite legal sequence of hit-to-hit correction blocks on the finite seed quotient whose unit ranks satisfy the forced acceleration
> \[
> m_{j+1}>\frac32m_j-C_*
> \]
> and whose base-`r` growing-modulus reverse addresses remain exactly endpoint-accessible at every block?

This is materially narrower than asking whether the ambient Pell conic has infinitely many solutions, and materially sharper than the first-stage hit-ancestry forest alone.

## 13. Driver return

Primary return:

`HIT_ANCESTRY_ONTOLOGY_REPLACED / SMALLER_EXACT_RECURRENCE_OBJECT_FOUND / NOT_CANONICAL`

Subclaims:

- `FINITE_CORRECTION_ALPHABET_PROVED`
- `EXACT_CORRECTION_COCYCLE_PROVED`
- `GROWING_MODULUS_REVERSE_ADDRESS_PROVED`
- `FINITE_PELL_REDUCED_SEED_QUOTIENT_PROVED`
- `FIXED_UNIT_DIAGONAL_ACCESSIBILITY_FINITE_PROVED`
- `HIT_TO_HIT_NORM_GAP_PROVED`
- `PELL_UNIT_RANK_ACCELERATION_PROVED`
- `INFINITE_REACHABLE_HIT_RAY_OPEN`
- `FINITE_HEIGHT_THEOREM_NOT_FORCED`

Recommended next attack:

1. work on the **growing-modulus correction address**, not a fixed residue automaton;
2. test whether exact endpoint legality gives an `r`-adic/Ostrowski obstruction to the accelerated unit-rank jumps;
3. alternatively search for a genuinely nested sequence of accessible hits whose unit ranks satisfy the proved acceleration law;
4. do not return to global dimension, support entropy, or ambient Pell existence.
