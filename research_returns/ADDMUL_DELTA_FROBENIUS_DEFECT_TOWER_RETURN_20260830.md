# ADDMUL δ_p / Frobenius defect tower — research return

Task: `RS-ADDMUL-DELTA-FROBENIUS-DEFECT-TOWER`  
Researcher-ID: `EM-AMDELTA-3B2016`  
Publication: `TP2-67960F557231FE3B1910`  
Frozen taskbook blob: `sha1:b3a6f2efc600f9f35ed5a9eee1b6d90e2d8eb44f`

## Terminal verdict

`PRIME_INDEXED_DEFECT_TOWER_CLASSIFIED`

Hard-target disposition:

`PASS / P2_EXACT_ALL_Z / ODD_P_SEMANTIC_IMAGE_PRODUCT_RECOVERY_OFF_S_ZERO / ODD_P_S_ZERO_INFINITE_FIBER / P_ADIC_VALUATION_AND_FINITE_LOG_RESIDUE_CLASSIFIED`

The prime-indexed defect family is a useful exact addition–multiplication bridge, but its strength is sharply typed:

- `p=2`: `D_2(x,y)=-xy` recovers multiplication globally on `Z^2`.
- every odd prime `p`: `(s,D_p)` with `s=x+y != 0` uniquely recovers `q=xy` on the semantic image of integer pairs;
- the unique odd-prime product-recovery singular hyperplane is `s=0`, where every `(a,-a)` maps to `(0,0)` and `q=-a^2` is lost;
- the raw cocycle is an exact coboundary, hence has zero unprojected associator holonomy;
- at the index prime `p`, unequal input valuations obey an exact closed valuation law, while the equal-valuation cancellation residue is controlled mod `p` by the classical finite logarithm / Mirimanoff polynomial.

No Foundation, Working Truth, or canonical-promotion authority is claimed.

---

## 1. Frozen definitions and standard prior-art boundary

For a prime `p` and `n,x,y in Z`, define

\[
\delta_p(n)=\frac{n-n^p}{p},
\qquad
D_p(x,y)=\delta_p(x+y)-\delta_p(x)-\delta_p(y),
\]

and write the positive-sign cross-effect

\[
C_p(x,y):=-D_p(x,y)
=\frac{(x+y)^p-x^p-y^p}{p}.
\]

These are standard `p`-derivation / Frobenius-lift identities. In particular, the facts that
`n^p == n (mod p)`, that `delta_p(Z) subset Z`, and that
`phi(n)=n^p+p delta_p(n)=n` is the canonical Frobenius lift on `Z`
are prior art, not Enterprise novelty. A convenient reference is Bhargav Bhatt,
*Lecture II: δ-rings*, Definition 1.1 and the example of `Z`.

Likewise, the finite logarithm / Mirimanoff polynomial used in §7 below is classical.
Relevant references include Besser, *Finite and p-adic polylogarithms*
(arXiv:math/0006051), Avitabile–Mattarei, *Generalized finite polylogarithms*
(arXiv:1809.01237), and Grohmann, *On the Zeros of Fermat Quotients and
Mirimanoff Polynomials* (arXiv:math/0604427).

The task-level contribution here is the exact integer fiber/reconstruction classification,
the valuation split, and the typed integration with existing Enterprise defect transport.

---

## 2. Integrality and the mixed-coefficient formula

For `1 <= i <= p-1`,

\[
c_{p,i}:=\frac{\binom p i}{p}\in\mathbb Z.
\]

Because `p` is prime,

\[
v_p\!\left(\binom p i\right)=1,
\qquad
v_p(c_{p,i})=0.
\]

Therefore

\[
D_p(x,y)
=
-\sum_{i=1}^{p-1}c_{p,i}x^iy^{p-i}
\in\mathbb Z[x,y].
\]

This proves both integer closure and the important valuation fact that every mixed
coefficient is a `p`-adic unit.

---

## 3. The global `p=2` bridge

Direct expansion gives

\[
D_2(x,y)=-xy.
\]

Hence

\[
xy=-D_2(x,y)
\]

for every `x,y in Z`, including `x+y=0`.

Thus the `p=2` member is a globally exact multiplication observable; no sum coordinate,
division, root selection, or exceptional locus is needed.

---

## 4. Odd-prime symmetric form

Let

\[
p=2m+1,\qquad s=x+y,\qquad q=xy.
\]

Let `P_n(s,q)=x^n+y^n`. Then

\[
P_0=2,\quad P_1=s,\quad P_n=sP_{n-1}-qP_{n-2}.
\]

The standard power-sum expansion is

\[
P_p(s,q)=
\sum_{j=0}^{m}
(-1)^j
\frac{p}{p-j}\binom{p-j}{j}
q^j s^{p-2j}.
\]

After cancelling the `j=0` term from `s^p-P_p`, one obtains

\[
C_p(x,y)=s\,T_p(s,q),
\]

where

\[
T_p(s,q)=
\sum_{j=1}^{m}
(-1)^{j+1}
A_{p,j}q^j s^{p-2j-1},
\qquad
A_{p,j}:=\frac{1}{p-j}\binom{p-j}{j}\in\mathbb Z.
\]

The integrality of `A_{p,j}` can also be read structurally:
`C_p/s` is a symmetric integer polynomial in `x,y`, hence lies in
`Z[s,q]`.

In particular,

\[
D_p(x,y)=-sT_p(s,q).
\]

### Low primes

\[
D_3=-sq=-xy(x+y).
\]

\[
D_5=-sq(s^2-q)
=-xy(x+y)(x^2+xy+y^2).
\]

\[
D_7=-sq(s^2-q)^2
=-xy(x+y)(x^2+xy+y^2)^2.
\]

The compact `p=5,7` pattern does not persist unchanged. For example,

\[
\frac{C_{11}}{s}
=
q(s^8-4qs^6+7q^2s^4-5q^3s^2+q^4).
\]

---

## 5. Exact odd-prime reconstruction theorem

### Theorem 5.1 — strict product monotonicity

Fix an odd prime `p=2m+1` and a real nonzero sum `s`.
On the entire real pair-product domain

\[
q\le \frac{s^2}{4},
\]

the polynomial `q -> T_p(s,q)` is strictly increasing.

### Proof

Take real roots `x,y` of

\[
t^2-st+q=0.
\]

At fixed `s`, for `x != y`,

\[
\frac{\partial}{\partial q}(x^p+y^p)
=
-p\,\frac{x^{p-1}-y^{p-1}}{x-y}.
\]

Since

\[
T_p(s,q)=\frac{s^p-(x^p+y^p)}{ps},
\]

we get

\[
\frac{\partial T_p}{\partial q}
=
\frac{x^{2m}-y^{2m}}{(x-y)(x+y)}
=
\sum_{k=0}^{m-1}x^{2(m-1-k)}y^{2k}.
\]

Every summand is nonnegative. Because `s=x+y != 0`, the pair `(x,y)` is not `(0,0)`,
so the sum is strictly positive. The repeated-root boundary follows by continuity
(or direct evaluation), completing the proof.

Because `T_p(s,0)=0`, the same theorem also gives

\[
\operatorname{sgn} T_p(s,q)=\operatorname{sgn}q.
\]

### Corollary 5.2 — exact semantic-image recovery

For odd prime `p` and `s != 0`, the observation pair

\[
(s,D_p)
\]

determines `q=xy` uniquely among real pairs, hence uniquely among integer pairs.

Indeed,

\[
T_p(s,q)=-D_p/s,
\]

and strict monotonicity supplies at most one admissible `q`.
For an actual integer pair, existence is automatic.

Once `q` is known, the unordered pair `{x,y}` is recovered from

\[
t^2-st+q=0.
\]

For an arbitrary candidate observation `(s,D)`, integer-pair image membership additionally
requires

1. `s | D`;
2. the unique monotone root `q` is integral and `q <= floor(s^2/4)`;
3. `Delta=s^2-4q` is a nonnegative square;
4. `s` and `sqrt(Delta)` have matching parity.

Therefore, on unordered integer pairs, `(x,y) -> (x+y,D_p(x,y))` is injective for `s != 0`.
For ordered pairs the only remaining ambiguity is the expected swap `(x,y)<->(y,x)`.

### The unique odd-prime singular hyperplane

If `s=0`, then `y=-x`. Since `p` is odd,

\[
D_p(x,-x)=0
\]

for every integer `x`, while

\[
q=-x^2
\]

varies. Thus all pairs `(a,-a)` collapse to the same observation `(0,0)`.
This is an infinite fiber and is exactly the lost-product locus.

There are no other real product-recovery singularities because Theorem 5.1 is strict
everywhere on `s != 0`.

### Integer inversion, not a rational isomorphism

- `p=3`: `T_3=q`, so `q=-D_3/s` is direct exact integer division.
- `p>=5`: `T_p` has degree `(p-1)/2` in `q`. The inverse is not globally a rational
  polynomial/rational map. It is the unique admissible integer root on the semantic image.

A fully integer recovery algorithm follows immediately: set
`hi=floor(s^2/4)`, find a sufficiently negative `lo` with
`T_p(s,lo) <= -D/s`, and binary-search the strictly increasing integer polynomial.
No floating point and no algebraic root approximation are required.

The semantic-domain restriction is essential. Example: for `p=5`, `s=2`,
`T_5=q(4-q)`. The value `3` has ambient polynomial roots `q=1,3`, but `q=3`
violates `q<=s^2/4=1`, so only `q=1` is a realizable pair product.

---

## 6. Exact real zero set and the Eisenstein-norm factor

For odd prime `p`, since `C_p=sT_p` and `T_p(s,q)` has the sign of `q` when `s!=0`,

\[
C_p(x,y)=0
\quad\Longleftrightarrow\quad
x=0\ \text{or}\ y=0\ \text{or}\ x+y=0
\]

over the real numbers.

Equivalently,

\[
C_p(x,y)=xy(x+y)E_p(x,y),
\]

and

\[
E_p(x,y)>0
\]

whenever `x y (x+y) != 0`.

### Exact cyclotomic multiplicity for `p>3`

Let

\[
N(x,y)=x^2+xy+y^2.
\]

For every prime `p>3`,

\[
N(x,y)^{e_p}\mid C_p(x,y)
\]

with exact exponent

\[
e_p=
\begin{cases}
1,&p\equiv5\pmod6,\\
2,&p\equiv1\pmod6.
\end{cases}
\]

Proof: dehomogenize
`f_p(t)=(1+t)^p-t^p-1` and evaluate at a primitive cube root
`omega`, for which `1+omega=-omega^2`.
For `p>3`, `f_p(omega)=0`. The first derivative vanishes exactly when
`p==1 (mod 3)`; in that case the second derivative is nonzero, giving exact
multiplicity two. Otherwise the root is simple. Homogenization yields the claim.

This cyclotomic factor is elementary prior art. Its task-level significance is that
the defect tower automatically contains an Eisenstein-norm support channel whose
multiplicity is controlled by `p mod 6`; this observation does **not** promote the
norm form to P000/Foundation geometry.

---

## 7. `p`-adic valuation footprint at the index prime

Let `v_p` denote the ordinary `p`-adic valuation and assume `x,y != 0`.
Write

\[
a=v_p(x),\qquad b=v_p(y).
\]

Because every mixed coefficient `c_{p,i}` is a `p`-adic unit, the `i`-th term of `D_p`
has valuation

\[
ia+(p-i)b.
\]

### Theorem 7.1 — unequal valuations

If `a != b`, the minimum term valuation is unique, so cancellation is impossible and

\[
\boxed{
v_p(D_p(x,y))
=
(p-1)\min(a,b)+\max(a,b)
}.
\]

Thus the unequal-valuation sector is completely rigid.

### Equal valuations and the finite logarithm

If `a=b=t`, write

\[
x=p^tu,\qquad y=p^tv
\]

with `u,v` `p`-adic units. Then

\[
v_p(D_p(x,y))
=
pt+v_p(D_p(u,v)).
\]

Modulo `p`,

\[
\frac{\binom p i}{p}
\equiv
\frac{(-1)^{i-1}}{i}\pmod p.
\]

Let

\[
z=-u/v\in\mathbb F_p^\times
\]

and define the classical finite logarithm / Mirimanoff polynomial

\[
L_p(z)=\sum_{i=1}^{p-1}\frac{z^i}{i}\in\mathbb F_p.
\]

Then

\[
\boxed{
D_p(u,v)/v^p \equiv L_p(-u/v)\pmod p
}.
\]

Therefore extra `p`-divisibility in the equal-valuation sector occurs exactly when
the projective ratio `-u/v` is a root of `L_p`.

This separates three mechanisms cleanly:

1. `z=1`: the visible `x+y` factor;
2. roots of `z^2-z+1`: the Eisenstein-norm factor when present modulo `p`;
3. additional finite-log roots: genuine arithmetic cancellation not explained by the
   two forced polynomial factors.

Concrete witness for mechanism 2:

\[
p=7,\quad (x,y)=(2,1),\quad D_7=-294=-6\cdot7^2,
\]

so `v_7(D_7)=2`, exactly matching the squared norm factor
`2^2+2+1=7`.

Concrete witness for mechanism 3:

for `p=59`, the finite-log roots are

`0,1,4,5,12,15,16,21,39,44,45,48,55,56`.

For `(x,y)=(3,1)`, `z=-3=56 mod 59`, hence

\[
v_{59}(D_{59}(3,1))=1,
\]

while

\[
59\nmid(x+y)=4,\qquad
59\nmid(x^2+xy+y^2)=13.
\]

Thus the finite-log residue is strictly richer than the forced sum/norm support.

---

## 8. Cocycle and coherence classification

By definition,

\[
D_p(x,y)=\delta_p(x+y)-\delta_p(x)-\delta_p(y),
\]

so `D_p` is a normalized symmetric `2`-coboundary on the additive group of integers.
Consequently,

\[
D_p(x,y)+D_p(x+y,z)
=
D_p(y,z)+D_p(x,y+z)
\]

identically.

More generally, for any finite list `(x_1,...,x_r)`,

\[
\delta_p\!\left(\sum_i x_i\right)-\sum_i\delta_p(x_i)
\]

is independent of the binary parenthesization, because every edge-defect sum
telescopes to the same endpoint expression.

Hence the raw, unprojected defect has:

`EXACT_ASSOCIATIVE_COHERENCE / ZERO_RAW_LOOP_HOLONOMY / COHOMOLOGICALLY_TRIVIAL`.

This is a standard coboundary fact, not a new cohomology class.

A nontrivial visibility/route residue can only be introduced after a downstream
non-homomorphic observation such as quotienting, precision projection, or valuation
compression. That downstream question is not a reason to invent a new holonomy tool.

---

## 9. Enterprise tool-reuse resolution

### `T9_HOLONOMY_COCOYCLE_GLUING`

Matched method:
`holonomy.precision_defect_transport`
via `src/enterprise_math/precision_signed_holonomy.py`.

Resolution: `REUSE_EXECUTED`.

For each tested `p,x,y`, set

\[
b=\delta_p(x)+\delta_p(y),\qquad d=D_p(x,y),
\]

so `b+d=delta_p(x+y)`. For a positive modulus `M`, the existing function

` signed_defect_transport(M,b,d) `

returns exactly

\[
\left\lfloor\frac{\delta_p(x+y)}M\right\rfloor
-
\left\lfloor\frac{\delta_p(x)+\delta_p(y)}M\right\rfloor.
\]

The existing staged/direct coherence checker is also reused.

Hard boundary preserved: this is signed finite-integer defect visibility under quotient
transport; it does not turn the raw coboundary into a new Foundation holonomy object.

### `T1_SCALE_ENUMERATION_VALUATION`

Resolution: `REUSE_APPLIED`.

The task-specific `p`-adic valuation law is recorded as a valuation footprint using the
existing valuation family. No new valuation tool family is opened.

### `T5_PRECISION_REFINEMENT`

Resolution: `NOT_APPLICABLE` to the full raw input domain because the frozen task permits
signed `x,y in Z`, while the core `precision.py` projection API is typed to nonnegative
states. The signed T9 transport path is the correct reusable interface.

Method harvest: `RESULT_ONLY`.

---

## 10. Exact checker

Frozen checker:

`research_checks/ADDMUL_DELTA_FROBENIUS_DEFECT_TOWER_CHECK_20260830.py`

It uses only integer arithmetic and the existing Enterprise signed-defect transport module.

Local deterministic run:

`PASS`

with `32,281` instantiated assertion-family checks, including:

- `341` integrality / coefficient-unit checks;
- `2,500` explicit `p=2,3,5,7` formula checks;
- `1,734` general odd symmetric-polynomial identity checks;
- `7,070` strict semantic-domain derivative checks;
- `6,660` odd-prime product-reconstruction checks;
- `9,126` cocycle checks;
- `9` exact Eisenstein-norm multiplicity checks;
- `1,752` unequal-valuation exact-law checks;
- `380` finite-log residue congruence checks;
- the `p=7` norm and `p=59` extra-root witnesses;
- `2,704` exact calls through existing `T9` signed transport/coherence.

The checker is evidence for the stated exact formulas and bounded regressions; theorem
proofs are the symbolic arguments above, not the finite enumeration alone.

---

## 11. Closure and residual frontier

### Closed by this task

- integer closure of `delta_p` and `D_p`;
- general mixed-coefficient formula;
- global `p=2` product recovery;
- exact `p=3,5,7` expansions;
- general odd-prime `s,q` form;
- exact odd-prime semantic-image product recovery for `s!=0`;
- exact identification of `s=0` as the unique odd-prime infinite product-loss fiber;
- exact raw cocycle/coherence classification;
- exact index-prime valuation law when input valuations differ;
- finite-log/Mirimanoff control of equal-valuation first cancellation;
- forced Eisenstein-norm support and exact multiplicity for `p>3`;
- reuse of existing signed defect transport.

### Residue not promoted

- For `p>=5`, no claim of a global rational/polynomial inverse for `q`; recovery is
  unique root selection on the semantic image.
- Full classification of roots and higher multiplicities of the finite logarithm for
  arbitrary primes is a classical arithmetic problem and is not solved here.
- No statement here promotes δ-rings, the Eisenstein norm, finite logarithms, or this
  defect tower into P000/Foundation primitives.
- No successor task is required merely because this task passed; Driver should first
  compare the result against the other add/mul bridge arms and decide whether the
  finite-log residual layer has discriminating portfolio value.

## Recommended Driver intake

Accept as `RESULT_ONLY` with the terminal classification

`PRIME_INDEXED_DEFECT_TOWER_CLASSIFIED`.

For bridge comparison, preserve the strongest exact statement:

> `p=2` is globally multiplicative; odd `p` is also product-complete once the sum
> coordinate is nonzero, and its only infinite loss fiber is the anti-diagonal
> `x+y=0`. The first genuinely extra arithmetic information beyond `(s,q)` geometry
> appears in the `p`-adic cancellation depth, whose equal-valuation residue is the
> classical finite logarithm.
