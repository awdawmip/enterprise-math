# P000 six-axis simultaneous C1/C2 AP pairability — Return

- Task: `RS-P000-SIX-AXIS-P11-SIMULTANEOUS-C1-C2-AP-PAIRABILITY`
- Publication: `TP2-61B5B36EBD10274CD5F8`
- Parent accepted Result: `RR-952CD6287F68219D7782`
- Researcher: `EM-P000P11S1-A7C4E2`
- Claim: `chatgpt-p000p11s1-20260902-1400-a7c4e2`
- Execution branch: `research/p000-p11-simultaneous-c1-c2-ap-em-p000p11s1-a7c4e2`
- Execution branch base: `cf27a726108f6324046a5027e4d293072134daee`
- Execution record: `ER-1943F3CDC14761230A7B`
- Result: `RR-DA840CA11911B721506F`

## Terminal verdict

`SIMULTANEOUS_GENUINE_C1_C2_EXISTENCE_REDUCED_TO_EXACT_ARITHMETIC_COMPONENT`

The bounded zero observation in the parent is false as a global nonexistence heuristic: simultaneous genuine C1/C2 integer points do exist.  A primitive point already appears in the precommitted full-integer root-height control `B=64`:

\[
H=(41,44,47),\qquad T=(0,210,420).
\]

Its eight outer root pairs are

\[
\begin{array}{ccc}
(0,41)&(6,35)&(20,21)\\
(0,44)&\text{center omitted}&(14,30)\\
(0,47)&(5,42)&(12,35).
\end{array}
\]

A second, arithmetically different primitive point is

\[
H=(-105,0,105),\qquad T=(-10816,-5800,-784),
\]

with outer root pairs

\[
\begin{array}{ccc}
(-169,64)&(-145,40)&(-112,7)\\
(-104,104)&\text{center omitted}&(-28,28)\\
(-64,169)&(-40,145)&(-7,112).
\end{array}
\]

More importantly, the eight square/parity predicates admit an exact necessary-and-sufficient reduction to **two integer right triangles of the same area, coupled by two additional square cuts and one AP row-coupling equation**.  This is a much smaller arithmetic normal form than the raw eight discriminant-square system.  For fixed area it sits inside the classical congruent-number arithmetic; globally it is an equal-area Pythagorean fiber product with exact divisibility, square and parity cuts.

No claim is made that the two primitive points displayed above exhaust all primitive integral points globally.  The hard target is closed at the task-authorized third terminal class: existence is proved, common root scaling is exact, and the unresolved global integral-point classification is isolated to a precise arithmetic component rather than a search bound.

No native orientation, Pfaffian slot, dimension reduction, factorization mechanism, Full-Cell dynamics, Working Truth, Foundation authority, or canonical promotion is asserted.

---

## 1. Frozen AP grid

Write

\[
H=(h-d,h,h+d),\qquad T=(t-e,t,t+e)
\]

with `d>0`, `e>0`.

For a cell `(q,p)`, pairability is exactly

\[
q^2-4p=\delta^2\ge 0,\qquad \delta\equiv q\pmod 2.
\]

The task requires pairability at every outer cell of the `3 x 3` grid and makes no requirement at the center `(h,t)`.

Choose the nonnegative discriminant roots

\[
\begin{array}{ccc}
a&b&c\\
\mu&-&\nu\\
f&g&k
\end{array}
\]

for the eight outer cells in row/column order.  Thus, for example,

\[
a^2=(h-d)^2-4(t-e),\quad
b^2=(h-d)^2-4t,\quad
c^2=(h-d)^2-4(t+e).
\]

Because `e>0`,

\[
a^2-b^2=b^2-c^2=4e,
\]

and similarly

\[
f^2-g^2=g^2-k^2=4e.
\]

Hence

\[
a^2+c^2=2b^2,\qquad f^2+k^2=2g^2.
\]

The same-row parity condition implies `a,b,c` all have the parity of `h-d`, and `f,g,k` all have the parity of `h+d`.

---

## 2. Equal-area Pythagorean compression

Define

\[
x=\frac{a+c}{2},\qquad y=\frac{a-c}{2},
\]

and

\[
X=\frac{f+k}{2},\qquad Y=\frac{f-k}{2}.
\]

These are integers because the discriminant roots in a row have the same parity.

Since `e>0`, one has `a>b>c>=0`.  In fact `c=0` is impossible: it would force `a^2=2b^2` with `a,b` nonzero integers.  Therefore

\[
x>y>0.
\]

Likewise `X>Y>0`.

Now

\[
x^2+y^2=\frac{a^2+c^2}{2}=b^2
\]

and

\[
X^2+Y^2=g^2.
\]

Moreover,

\[
xy=\frac{a^2-c^2}{4}=2e,
\]

and likewise

\[
XY=2e.
\]

Therefore the top and bottom rows canonically determine two integer right triangles

\[
(x,y,b),\qquad (X,Y,g)
\]

with **equal area**

\[
\frac{xy}{2}=\frac{XY}{2}=e.
\]

Conversely, for any integer right triangle `(x,y,b)` with `x>y>0`, setting

\[
a=x+y,\qquad c=x-y
\]

gives

\[
a^2-b^2=b^2-c^2=2xy.
\]

Thus requiring `xy=2e` reconstructs exactly the top-row AP square spacing, and the same statement holds for the bottom row.

This is an exact equivalence; it is not a heuristic parameter choice.

---

## 3. Complete simultaneous normal form

### Theorem 3.1 — equal-area Pythagorean normal form

A strict AP datum

\[
H=(h-d,h,h+d),\quad T=(t-e,t,t+e)
\]

is simultaneously genuine in the task sense (all eight outer cells pairable) if and only if there exist integers

\[
x>y>0,\quad X>Y>0,\quad b>0,\quad g>0,\quad d>0,
\]

integers `h,mu,nu`, and the derived quantities

\[
a=x+y,\quad c=x-y,\quad f=X+Y,\quad k=X-Y
\]

such that all of the following hold.

**Equal-area Pythagorean core**
\[
x^2+y^2=b^2,
\]
\[
X^2+Y^2=g^2,
\]
\[
xy=XY=2e.
\]

**AP row coupling**
\[
K:=g^2-b^2=4hd.
\]

Because `xy=XY`, the same `K` automatically satisfies
\[
K=f^2-a^2=k^2-c^2.
\]

**Middle-row square cuts**
\[
2\mu^2=a^2+f^2-2d^2,
\]
\[
2\nu^2=c^2+k^2-2d^2.
\]

**Parity**
\[
a\equiv b\equiv c\equiv h-d\pmod 2,
\]
\[
\mu\equiv\nu\equiv h\pmod 2,
\]
\[
f\equiv g\equiv k\equiv h+d\pmod 2.
\]

Finally define
\[
t=\frac{(h-d)^2-b^2}{4}.
\]

Then `e=xy/2` and the above parity conditions make `e,t` integers, and the simultaneous datum is exactly

\[
H=(h-d,h,h+d),\qquad T=(t-e,t,t+e).
\]

### Proof — necessity

Start from a simultaneously genuine datum.  Section 2 gives the two Pythagorean triples and `xy=XY=2e`.

The middle column top/bottom products are both `t`, so

\[
(h-d)^2-b^2=(h+d)^2-g^2.
\]

Therefore

\[
g^2-b^2=(h+d)^2-(h-d)^2=4hd.
\]

Because `xy=XY`,

\[
f^2-a^2
=(X^2+Y^2+2XY)-(x^2+y^2+2xy)
=g^2-b^2,
\]

and similarly `k^2-c^2=g^2-b^2`.

For the middle-left discriminant,

\[
\mu^2=h^2-4(t-e).
\]

Using

\[
4t=(h-d)^2-b^2,\qquad 4e=2xy,
\]

one obtains

\[
\mu^2
=h^2-(h-d)^2+b^2+2xy
=2hd-d^2+(x+y)^2.
\]

Since `4hd=f^2-a^2`, this is

\[
\mu^2=\frac{a^2+f^2}{2}-d^2.
\]

The same calculation on the right gives

\[
\nu^2=\frac{c^2+k^2}{2}-d^2.
\]

Multiplying by two gives the displayed integral square cuts.  The parity conditions are precisely the original pairability parity conditions.

### Proof — sufficiency

Conversely assume the normal-form equations.

For the top-middle cell,

\[
(h-d)^2-4t=b^2.
\]

Because `4e=2xy`,

\[
(h-d)^2-4(t-e)=b^2+2xy=(x+y)^2=a^2,
\]

and

\[
(h-d)^2-4(t+e)=b^2-2xy=(x-y)^2=c^2.
\]

Thus all three top cells are pairable.

For the bottom-middle cell,

\[
(h+d)^2-4t
=(h+d)^2-(h-d)^2+b^2
=4hd+b^2
=g^2.
\]

Adding/subtracting `4e=2XY` gives discriminants `f^2` and `k^2`.  Thus all three bottom cells are pairable.

Finally the two assumed middle square cuts are exactly

\[
\mu^2=h^2-4(t-e),\qquad
\nu^2=h^2-4(t+e).
\]

The parity assumptions recover integer roots in every outer cell.  Hence all eight outer cells are pairable.

This proves necessity and sufficiency.

---

## 4. Exact arithmetic component

For each positive integer `e`, define the integral equal-area triangle set

\[
\mathcal T_e
=
\{(x,y,b)\in\mathbf Z_{>0}^3:
x>y,\ x^2+y^2=b^2,\ xy=2e\}.
\]

Then every simultaneous datum is exactly a choice of

\[
P=(x,y,b)\in\mathcal T_e,\qquad
Q=(X,Y,g)\in\mathcal T_e,
\]

together with integers `d>0,h,mu,nu` satisfying

\[
g^2-b^2=4hd,
\]

\[
2\mu^2=(x+y)^2+(X+Y)^2-2d^2,
\]

\[
2\nu^2=(x-y)^2+(X-Y)^2-2d^2,
\]

and the explicit parity chamber of Theorem 3.1.

Equivalently one may eliminate `h` and require

\[
4d\mid g^2-b^2,\qquad
h=\frac{g^2-b^2}{4d}\in\mathbf Z,
\]

followed by the two square cuts and parity.

This is the exact remaining arithmetic component.

Classically, `e` is the area of a rational (here integral) right triangle.  The congruent-number curve

\[
E_e:\quad Y^2=X^3-e^2X
\]

encodes rational right triangles of area `e`.  Therefore the simultaneous locus may be viewed as an **integral equal-area fiber product** of two congruent-number triangle representations, cut further by the `d`-divisibility equation and two integral square conditions.  Congruent-number elliptic curves, Pythagorean triples and their classical parameterizations are prior mathematics; no novelty claim is made for that classical machinery.

The task-local contribution is the exact equivalence between the eight outer P11 pairability predicates and this equal-area fiber-product normal form.

---

## 5. AP involution becomes triangle swap

The parent involution is

\[
I(H,T)=((-h_2,-h_1,-h_0),T).
\]

On AP coordinates this is simply

\[
(h,d,t,e)\mapsto(-h,d,t,e).
\]

In the equal-area normal form it is

\[
(x,y,b;\ X,Y,g;\ h,d,\mu,\nu)
\longmapsto
(X,Y,g;\ x,y,b;\ -h,d,\mu,\nu).
\]

Indeed triangle swap sends

\[
K=g^2-b^2\mapsto -K,
\]

so `4hd=K` becomes `4(-h)d=-K`.  Both middle square cuts are symmetric under the swap.

Thus the AP specialization exposes a stronger quotient description: the C1/C2 involution is literally exchange of the two equal-area triangle factors.

### Fixed locus

The swap-fixed locus is exactly `h=0`.

If the two triangles are equal, then `K=0`, hence `h=0` because `d>0`.

Conversely if `h=0`, then `K=0`, so `b=g`.  Together with

\[
xy=XY,\qquad x^2+y^2=X^2+Y^2
\]

and positive ordering, this determines the same unordered leg pair, hence

\[
(x,y,b)=(X,Y,g).
\]

Therefore

\[
h=0
\quad\Longleftrightarrow\quad
P=Q.
\]

On this diagonal component the normal form reduces to one integer right triangle plus

\[
\mu^2=(x+y)^2-d^2,
\]

\[
\nu^2=(x-y)^2-d^2.
\]

The second primitive witness lies exactly on this fixed diagonal.

No geometric/native orientation meaning is assigned to this swap.

---

## 6. Primitive common-root normalization

For every pairable outer cell with row sum `q` and discriminant root `delta`, the recovered unordered root pair is

\[
\left\{
\frac{q-\delta}{2},
\frac{q+\delta}{2}
\right\}.
\]

Let `R` be the multiset of all sixteen recovered outer roots and define

\[
m=\gcd\{|r|:r\in R\}.
\]

The parity conditions make every root integral, and `e>0` prevents all roots from vanishing.

Scaling every root by `m` gives

\[
H\mapsto mH,\qquad T\mapsto m^2T.
\]

Conversely, if all recovered roots share a positive common divisor, every row sum and every column product has exactly that induced scaling.  Therefore dividing all roots by their gcd gives a simultaneous datum again.

Hence each simultaneous datum has a unique positive primitive representative with

\[
\gcd(R)=1.
\]

This normalization is complete and includes zero roots: zero entries simply do not change the gcd.

---

## 7. Primitive witnesses and scaling families

### 7.1 Off-diagonal / zero-column primitive point

Take

\[
H=(41,44,47),\qquad T=(0,210,420).
\]

Here

\[
h=44,\quad d=3,\quad t=210,\quad e=210.
\]

Top discriminants are

\[
(a,b,c)=(41,29,1),
\]

so

\[
(x,y,b)=(21,20,29).
\]

Bottom discriminants are

\[
(f,g,k)=(47,37,23),
\]

so

\[
(X,Y,g)=(35,12,37).
\]

Both triangles have area

\[
\frac{21\cdot20}{2}
=
\frac{35\cdot12}{2}
=210.
\]

The coupling is

\[
K=37^2-29^2=528=4\cdot44\cdot3.
\]

The middle discriminants are

\[
(\mu,\nu)=(44,16),
\]

and indeed

\[
2\cdot44^2=41^2+47^2-2\cdot3^2,
\]

\[
2\cdot16^2=1^2+23^2-2\cdot3^2.
\]

Its outer root gcd is `1`, so it is primitive.

The involutive partner is

\[
H=(-47,-44,-41),\qquad T=(0,210,420),
\]

which simply swaps the two equal-area triangles.

For every positive integer `m`, common root scaling gives the valid family

\[
H_m=(41m,44m,47m),
\]

\[
T_m=(0,210m^2,420m^2),
\]

and its involutive partner.  Only `m=1` is primitive.

This proves that the zero-root boundary is not an excluded degeneracy: it supports genuine simultaneous points.

### 7.2 Diagonal / mixed-sign primitive point

Take

\[
H=(-105,0,105),
\]

\[
T=(-10816,-5800,-784).
\]

Here

\[
h=0,\quad d=105,\quad t=-5800,\quad e=5016.
\]

Both top and bottom triangle factors are the same:

\[
(x,y,b)=(176,57,185),
\]

with area

\[
\frac{176\cdot57}{2}=5016.
\]

The top/bottom discriminants are

\[
(233,185,119),
\]

and the middle discriminants are

\[
(\mu,\nu)=(208,56).
\]

The exact square cuts are

\[
208^2=233^2-105^2,
\]

\[
56^2=119^2-105^2.
\]

Its outer root gcd is `1`, so it is primitive.

For every positive integer `m`,

\[
H_m=(-105m,0,105m),
\]

\[
T_m=(-10816m^2,-5800m^2,-784m^2)
\]

is a simultaneous scaling family, with `m=1` the primitive representative.

This diagonal example has all three products negative, so every nonzero outer root pair has opposite signs.  Thus negative-product/sign-crossing strata genuinely occur and cannot be removed.

On the entire diagonal `h=0` component, middle-row pairability gives

\[
-4(t-e)=\mu^2\ge0,\qquad
-4(t+e)=\nu^2\ge0.
\]

Hence

\[
t-e<t<t+e\le0.
\]

So the diagonal fixed component lies entirely in the nonpositive-product chamber (with the final column possibly zero).

---

## 8. Zero, sign, even and parity strata

The exact normal form keeps all integer populations.

### Zero roots

A recovered root is zero exactly when its column product is zero.  Because the same `T_j` is shared by every row, a zero-product column produces zero roots throughout all pairable cells in that column.

The primitive point

\[
(41,44,47;\ 0,210,420)
\]

proves that this boundary supports simultaneous genuineness.

### Negative and mixed signs

For `T_j<0`, the two roots in every pairable cell of that column have opposite signs.  The diagonal primitive point with all `T_j<0` proves this chamber supports simultaneous genuineness.

The involutive partner of the first witness also supplies the all-negative-sum / positive-product sign chamber.

### Parity and even roots

The normal form never divides out parity classes.  In each row the three discriminants have exactly the row-sum parity.  The Pythagorean legs cannot both be odd because `x^2+y^2` would be `2 mod 4`; hence `xy` is automatically even and `e=xy/2` is integral.

The first primitive witness contains zero, even, odd, prime-factor-rich and composite roots simultaneously.  Scaling either primitive witness by `2` gives a valid all-even nonprimitive datum.  No primitive datum can have every recovered root even, because that would contradict the defining common-root gcd `1`.

Thus even/composite/zero/small-prime values are structural data, not preprocessing noise.

---

## 9. Exact finite regression and falsification

Before inspecting any outcomes for this task, the full-integer control was fixed at

\[
B=64,
\]

meaning every unordered root pair `(r,s)` with

\[
-B\le r\le s\le B
\]

is included.  No prime/composite, sign, zero or parity filtering is applied.

The exact checker enumerates all pairable `(h,t)=(r+s,rs)` from that complete root catalog, then searches every strict AP `H` and strict AP `T` for which all eight outer cells occur in the catalog.

Results:

| root height | raw simultaneous data | primitive data |
|---:|---:|---:|
| `B=20` | `0` | `0` |
| `B=64` | `2` | `2` |
| `B=256` | `11` | `3` |

The `B=20` row reproduces the parent's bounded zero observation.

The precommitted `B=64` control already finds exactly the primitive witness

\[
(41,44,47;0,210,420)
\]

and its triangle-swap involutive partner.

The exploratory `B=256` census additionally finds the diagonal primitive witness

\[
(-105,0,105;-10816,-5800,-784).
\]

A non-load-bearing extended exact run at `B=1024` found `48` raw solutions and still only these three primitive data (the first witness, its involutive partner, and the diagonal witness).  The task-local checker can reproduce this with `--extra-bound 1024`; it is intentionally not part of the default fast regression.

None of these finite counts is used as a global completeness theorem.

---

## 10. Why the task closes at the arithmetic-component terminal class

The requested global nonexistence alternative is decisively false.

Existence is not merely computational: each displayed witness is verified cell-by-cell by exact integer roots and also satisfies the exact normal-form equations.  Common root scaling is completely normalized by the gcd of all recovered outer roots.

A complete elementary parametrization of every primitive integral point is not claimed.  The remaining global classification problem has, however, been reduced exactly from eight square/parity predicates to:

1. two integer right triangles with the same area `e`;
2. one integral row-coupling equation `g^2-b^2=4hd`;
3. two explicit middle-row square equations;
4. a finite parity chamber;
5. quotient by common root scaling and triangle-swap involution.

For fixed `e`, the first layer is the integral part of the classical congruent-number arithmetic associated with

\[
Y^2=X^3-e^2X.
\]

The further `d,mu,nu` cuts are explicit.  This is the precise arithmetic component on which any stronger global enumeration theorem must act.

Therefore the correct terminal class is

`SIMULTANEOUS_GENUINE_C1_C2_EXISTENCE_REDUCED_TO_EXACT_ARITHMETIC_COMPONENT`.

---

## 11. Method and novelty boundary

Used as prior mathematics:

- integer root recovery from sum/product;
- Pythagorean triples and the identity converting three squares in arithmetic progression to a right triangle;
- classical congruent-number interpretation of rational right triangles of fixed area;
- gcd normalization;
- exact finite integer enumeration as falsification/regression only.

Task-local derived result:

- the necessary-and-sufficient equal-area Pythagorean normal form for the simultaneous eight-cell AP pairability locus;
- the identification of the AP C1/C2 involution with triangle-factor swap;
- the exact fixed-locus criterion `h=0 <=> top triangle = bottom triangle`;
- the two primitive simultaneous witnesses and their scaling orbits;
- the explicit separation of zero-root and negative-product solution strata.

No historical novelty claim is made.

---

## 12. Durable outputs

The immutable Result binds:

- this Return;
- `research_checks/P000_SIX_AXIS_P11_SIMULTANEOUS_C1_C2_AP_PAIRABILITY_CHECK_20260902.py`;
- `research_artifacts/P000_SIX_AXIS_P11_SIMULTANEOUS_C1_C2_AP_PAIRABILITY/certificate_20260902.json`;
- execution record `ER-1943F3CDC14761230A7B`.

The Researcher lane makes no downstream task decision.  Driver review is required.
