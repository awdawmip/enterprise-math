# Prime Fusion — Independent Replication Return

Status: `FROZEN`
Date: `2026-08-23`
Researcher-ID: `EM-PFREP-28D707`
Task-ID: `RS-PRIME-FUSION-INDEPENDENT-REPLICATION`
Owner branch: `research/prime-fusion-independent-replication`
Hard target: `PRIME_FUSION_CORE_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED`

Final classification: `FULL_STRUCTURAL_REPLICATION`

## 1. BLINDNESS_STATUS

`BLINDNESS_STATUS = CLEAN`

Before this return was frozen, the only mathematical repository files read were:

1. `research_tasks/PRIME_FUSION_INDEPENDENT_REPLICATION_20260823.md`
   at `28d707f475a8247d2b77b9ed3c6154278f857198`;
2. `research_inputs/PRIME_FUSION_BLIND_INDEPENDENT_REPLICATION_PACKET_20260823.md`
   at `096d7f4f3a6347b79bee58ae0973cea518780efa`;
3. `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`
   at `88d86e2146c01cbe7a62432e9488b2b4621ec9fa`, as explicitly permitted by the blind packet.

Repository/branch metadata was queried only to locate `awdawmip/enterprise-math`, confirm the owner branch, and confirm that the two intended output paths did not already exist. No theorem package, source-run checker, PR #597, PR discussion, Driver comparison, journal summary, source-research conversation, source-result commit message, or source-result code search was opened. No external literature was used.

All algebra, proofs, counterexample searches, and checker code below were independently derived from the blind object.

## 2. Independently introduced definitions

Work in the single native sector `S_12` with positive integer interior coordinates `(a,b)` and

\[
A=A(a,b)=a^2+b^2,\qquad
B=B(a,b)=a^2-ab+b^2.
\]

A cell is **primitive** when

\[
\gcd(a,b)=1.
\]

A cell is **simultaneously prime** when both `A` and `B` are ordinary primes.

For a primitive positive interior cell define

\[
N:=AB.
\]

Because `a` and `b` are each coprime to both `A` and `B` (proved below), `b` is a unit modulo `N`. Define the **marked finite carrier**

\[
\mathcal C(a,b):=
\left(\mathbf Z/N\mathbf Z,\,[r]\right),
\qquad
r\equiv a\,b^{-1}\pmod N.
\]

For a prime `l`, let `n_A(l)` and `n_B(l)` be the numbers of projective nonzero directions `[a:b] in P^1(F_l)` on which `A` and `B`, respectively, vanish.

For finite modular reduction define

\[
F_M(a,b):=\mathbf 1_{\gcd(A(a,b)B(a,b),M)=1}
\]

on `(Z/MZ)^2`.

## 3. Theorem statements and proofs

### Theorem 1 — Three exact identities and exact common divisor

For all nonnegative integers `a,b`,

\[
A-B=ab,
\]

\[
2B-A=(a-b)^2,
\]

and

\[
3A-2B=(a+b)^2.
\]

Moreover, with `g=gcd(a,b)`,

\[
\gcd(A,B)=g^2.
\]

Hence

\[
\gcd(a,b)=1
\iff
\gcd(A,B)=1.
\]

#### Proof

The three displayed identities follow by direct expansion.

Write `a=gu`, `b=gv` with `gcd(u,v)=1`. Then

\[
A=g^2(u^2+v^2),\qquad
B=g^2(u^2-uv+v^2).
\]

Let a prime `p` divide both reduced forms. Their difference is `uv`, so `p|uv`. If `p|u`, then from `p|(u^2+v^2)` one gets `p|v`, contradicting `gcd(u,v)=1`; the case `p|v` is identical. Therefore the two reduced forms are coprime, and `gcd(A,B)=g^2`. ∎

### Theorem 2 — Exact recoverability of the coordinates

Set

\[
D^2:=2B-A,\qquad
S^2:=3A-2B.
\]

For a cell coming from nonnegative integer coordinates,

\[
D=|a-b|,\qquad S=a+b.
\]

Therefore

\[
\{a,b\}
=
\left\{
\frac{S-D}{2},
\frac{S+D}{2}
\right\}.
\]

Thus the pair `(A,B)` recovers the unordered coordinates exactly.

Conversely, an integer pair `(X,Y)` is in the image of the nonnegative-coordinate map if and only if

- `2Y-X` and `3X-2Y` are nonnegative perfect squares,
- with nonnegative square roots `D,S`,
- `(S-D)/2` and `(S+D)/2` are nonnegative integers.

In that case those two numbers reproduce `(X,Y)`.

For positive interior coordinates one additionally has `X-Y=ab>0`.

The ordered pair is not recoverable from `(A,B)` alone, because both readouts are invariant under `(a,b)<->(b,a)`.

#### Proof

The forward statement is Theorem 1. Conversely, define

\[
u=(S-D)/2,\qquad v=(S+D)/2.
\]

Then

\[
u^2+v^2=\frac{S^2+D^2}{2}=X
\]

and

\[
uv=\frac{S^2-D^2}{4}=X-Y,
\]

so

\[
u^2-uv+v^2=X-(X-Y)=Y.
\]

Swap invariance is immediate from the two quadratic forms. ∎

### Theorem 3 — A single marked finite quotient reconstructs a primitive interior cell

Let `(a,b)` be primitive and positive. Then

\[
\gcd(a,N)=\gcd(b,N)=1.
\]

In the marked carrier

\[
\mathcal C(a,b)=\left(\mathbf Z/N\mathbf Z,[r]\right),
\quad
r\equiv a b^{-1}\pmod N,
\]

one has the exact recovery formulas

\[
A=\gcd\!\left(N,r^2+1\right),
\]

\[
B=\gcd\!\left(N,r^2-r+1\right).
\]

Consequently one marked residue class `[r]` in the single quotient `Z/NZ` recovers the labeled channel split `(A,B)`, then Theorem 2 recovers `{a,b}`.

The same marker also recovers the coordinate order. If `a!=b`, swapping coordinates replaces `r` by `r^{-1}` modulo `N`, and these are distinct.

Thus, in the natural metric “number of distinguished carrier elements”, zero extra marks are insufficient in general, while one marked residue class suffices. No claim is made here about bit-optimal encoding.

#### Proof

If a prime divides `b` and `A`, then it divides `a^2`, hence `a`, contradicting primitivity; the same argument applies to `B`, and similarly for `a`. Thus `a,b` are units modulo `N`.

Modulo `A`,

\[
r^2+1\equiv (a^2+b^2)b^{-2}\equiv0.
\]

Modulo `B`,

\[
r^2-r+1\equiv(a^2-ab+b^2)b^{-2}\equiv0.
\]

For any integer representative `r`,

\[
\gcd(r^2+1,r^2-r+1)=1,
\]

because a common divisor divides their difference `r`, and then also divides `r^2+1`, hence is `1`.

Since primitive cells have `gcd(A,B)=1`, the first polynomial captures all of `A` and no factor of `B`, while the second captures all of `B` and no factor of `A`. This proves the gcd formulas.

Under coordinate swap the marked ratio becomes

\[
b a^{-1}\equiv r^{-1}\pmod N.
\]

If `r=r^{-1}` and `a!=b`, then `r^2=1 mod N`. But modulo `A` one also has `r^2=-1`, hence `A|2`. A positive primitive cell with distinct coordinates has `A>=5`, contradiction. If `a=b`, primitivity forces `(a,b)=(1,1)`, where the two orders coincide anyway. ∎

### Theorem 4 — Scalarization to `N=AB` loses genuine cell information

The unmarked scalar `N=AB` does not determine even the unordered primitive cell.

An explicit collision is

\[
(a,b)=(14,43):
\quad
(A,B)=(2045,1443),
\]

and

\[
(a,b)=(31,38):
\quad
(A,B)=(2405,1227),
\]

with both cells primitive and

\[
2045\cdot1443
=
2405\cdot1227
=
2,950,935.
\]

These cells are not coordinate swaps of one another.

Therefore the direction/channel information carried by `[r]` in Theorem 3 is genuine and is destroyed by scalarization to `N`.

∎

### Theorem 5 — Exact prime-modulus direction classes

Let `l` be prime. No projective zero direction for either form lies at `b=0`; hence all such directions can be written `[r:1]`.

For `A`, the condition is

\[
r^2+1=0.
\]

Hence

\[
n_A(l)=
\begin{cases}
1,&l=2,\\
2,&l\equiv1\pmod4,\\
0,&l\equiv3\pmod4.
\end{cases}
\]

For `B`, the condition is

\[
r^2-r+1=0.
\]

Hence

\[
n_B(l)=
\begin{cases}
0,&l=2,\\
1,&l=3,\\
2,&l>3,\ l\equiv1\pmod6,\\
0,&l>3,\ l\equiv5\pmod6.
\end{cases}
\]

For `l>3`, the two roots of the `B` polynomial are exactly the elements of order `6` in `F_l^*`.

#### Proof

The `A` statement is the standard elementary classification of the square root of `-1`, with the direct special calculation at `l=2`.

For `B` and `l>3`,

\[
(r+1)(r^2-r+1)=r^3+1.
\]

A root cannot be `r=-1`, because the quadratic then equals `3`, nonzero modulo `l`. Therefore a root has `r^3=-1`, hence exact multiplicative order `6`. Such elements exist iff `6|(l-1)`, and then there are `phi(6)=2` of them. At `l=3`, the discriminant vanishes and the unique double root is `r=2`. At `l=2` there is no root. ∎

### Corollary 5.1 — Which primes can divide a channel of a primitive cell

For a primitive cell:

- a prime `l` can divide `A` iff `l=2` or `l≡1 mod 4`;
- a prime `l` can divide `B` iff `l=3` or `l≡1 mod 6`.

These are existence statements as well as necessary conditions: choose a projective root `[r:1]` and the primitive integer cell `(r,1)`.

For primes `l>3`, the combined modulus `12` gives:

| `l mod 12` | may divide `A` | may divide `B` |
|---|---:|---:|
| `1` | yes | yes |
| `5` | yes | no |
| `7` | no | yes |
| `11` | no | no |

For a fixed primitive cell the same prime cannot divide both channels because `gcd(A,B)=1`.

### Theorem 6 — Exact fixed-slice root counts

On the slice

\[
(a,b)=(t+k,t)
\]

one has

\[
A_k(t)=2t^2+2kt+k^2,
\]

\[
B_k(t)=t^2+kt+k^2.
\]

For an odd prime `l`:

- if `k=0 mod l`, each channel has exactly one root `t=0`;
- if `k!=0 mod l`, the number of `A` roots is `n_A(l)` and the number of `B` roots is `n_B(l)`.

For `l=2`:

- `k=0`: `A_k` vanishes for both `t` values, while `B_k` has one root;
- `k=1`: neither channel has a root.

#### Proof

For odd `l`, the discriminants are

\[
\Delta_A=-4k^2,\qquad
\Delta_B=-3k^2.
\]

When `k!=0`, these give exactly the projective classifications of Theorem 5. When `k=0`, the forms reduce to `2t^2` and `t^2`. The `l=2` cases follow by direct reduction. ∎

### Theorem 7 — Forced congruence and quadratic-reciprocity relations for simultaneous primes

Let

\[
P=A(a,b),\qquad Q=B(a,b)
\]

be primes with `P>2` and `Q>3`.

Then the cell is primitive and

\[
P\equiv1\pmod4,\qquad
Q\equiv1\pmod6.
\]

Moreover the exact square identities force

\[
2Q\equiv(a-b)^2\pmod P,
\]

\[
-2Q\equiv(a+b)^2\pmod P,
\]

\[
-P\equiv(a-b)^2\pmod Q,
\]

\[
3P\equiv(a+b)^2\pmod Q,
\]

and all four right-hand sides are nonzero modulo the indicated prime.

Therefore, with Legendre symbols,

\[
\left(\frac{Q}{P}\right)
=
\left(\frac{P}{Q}\right)
=
\left(\frac{2}{P}\right)
=
\left(\frac{-1}{Q}\right)
=
\left(\frac{3}{Q}\right).
\]

Equivalently, the prime residues satisfy the exact coupling

\[
(P\bmod8,\ Q\bmod12)
\in
\{(1,1),(5,7)\}.
\]

#### Proof

A nonprimitive cell has both readouts divisible by `gcd(a,b)^2`, so simultaneous primality forces primitivity. The congruences `P≡1 mod4` and `Q≡1 mod6` follow from Corollary 5.1.

Reducing Theorem 1's two square identities modulo `P` and `Q` gives the four displayed quadratic residues.

The relevant squares are nonzero: for example, `a≡b mod Q` would imply `Q|a^2` from the `B` form, contradicting primitivity; `a≡-b mod Q` would imply `Q|3b^2`, impossible because `Q>3`; the `P` cases are similar.

Thus

\[
(Q/P)=(2/P),
\]

\[
(P/Q)=(-1/Q)=(3/Q).
\]

Since `P≡1 mod4`, quadratic reciprocity gives `(Q/P)=(P/Q)`, proving the common-symbol chain.

Finally, for `P≡1 mod4`, `(2/P)=1` exactly at `P≡1 mod8` and is `-1` at `P≡5 mod8`. For `Q≡1 mod6`, `(-1/Q)=1` exactly at `Q≡1 mod12` and is `-1` at `Q≡7 mod12`. This gives the two allowed residue pairs. ∎

No asymptotic statement is inferred from this theorem.

### Theorem 8 — Exact one-sector nearest-neighbor component bound

Inside one `S_12` carrier chart, the nearest-center displacement vectors are exactly

\[
(\pm1,0),\quad(0,\pm1),\quad(1,1),\quad(-1,-1).
\]

The induced nearest-neighbor graph on simultaneously-prime positive interior cells has maximum degree `1`; hence every connected component has size at most `2`.

The bound is sharp.

#### Proof

The sector-local carrier squared displacement is

\[
x^2-xy+y^2.
\]

Nearest-center spacing is `1`, so solve

\[
x^2-xy+y^2=1.
\]

Equivalently,

\[
(2x-y)^2+3y^2=4,
\]

whose integer solutions are precisely the six vectors above.

Now let a simultaneously-prime cell have `A>2`. Since `A=a^2+b^2` is an odd prime, exactly one of `a,b` is even. A horizontal or vertical unit move flips only one parity, making the two new coordinates have the same parity. Then the new `A` is even; the only possible prime value would be `2`, but `(1,1)` has `B=1`, not prime. Therefore every simultaneously-prime edge is diagonal.

For `B>3`,

\[
B(a,b)\equiv(a+b)^2\pmod3,
\]

so `a+b` is nonzero modulo `3`. A diagonal move changes `a+b` by `+2` or `-2`. Exactly one of the two diagonal neighbors has coordinate sum divisible by `3`, hence its `B` is divisible by `3` and cannot be prime unless that neighbor has `B=3`.

The positive solutions of

\[
a^2-ab+b^2=3
\]

are exactly `(1,2)` and `(2,1)`. They are simultaneously prime because `A=5`. Their only simultaneously-prime diagonal partners are `(2,3)` and `(3,2)`, respectively; the next forward cells `(3,4)` and `(4,3)` have `A=25`. Thus the ramified `B=3` cases also have degree `1`.

Hence every vertex has degree at most `1`, so every component is an isolated vertex or a single edge. The components

\[
(1,2)\leftrightarrow(2,3)
\]

and its coordinate swap show that size `2` occurs. ∎

This is strictly sector-local. No cross-sector seam claim is made.

### Theorem 9 — Exact finite modular dimensional reduction

For every integer `M>=1` and every function `F` on `(Z/MZ)^2`,

\[
\sum_{a,b\bmod M}F(a,b)
=
\sum_{k,t\bmod M}F(t+k,t).
\]

Hence for the survivor indicator `F_M`,

\[
\frac1{M^2}\sum_{a,b\bmod M}F_M(a,b)
=
\frac1M\sum_{k\bmod M}
\left[
\frac1M\sum_{t\bmod M}F_M(t+k,t)
\right].
\]

Thus the exact two-dimensional modular survivor density is the mean of the exact one-dimensional slice survivor densities.

#### Proof

The linear map

\[
(t,k)\mapsto(a,b)=(t+k,t)
\]

has inverse

\[
(a,b)\mapsto(t,k)=(b,a-b)
\]

over `Z/MZ` for every `M`. Therefore it is a bijection and preserves the total sum exactly. ∎

### Theorem 10 — Exact local survivor counts and CRT product

For a prime `l`, the nonzero zero-directions of `A` and `B` are disjoint. Their only common zero in `F_l^2` is `(0,0)`.

Therefore the number `S_l` of pairs `(a,b) mod l` with neither channel divisible by `l` is

\[
S_l
=
(l-1)\bigl(l+1-n_A(l)-n_B(l)\bigr).
\]

Explicitly:

\[
S_2=2,\qquad S_3=6,
\]

and for `l>3`,

\[
S_l=
\begin{cases}
(l-1)(l-3),&l\equiv1\pmod{12},\\
(l-1)^2,&l\equiv5\pmod{12},\\
(l-1)^2,&l\equiv7\pmod{12},\\
l^2-1,&l\equiv11\pmod{12}.
\end{cases}
\]

For squarefree

\[
M=\prod_{l|M}l,
\]

the exact survivor count is

\[
S_M=\prod_{l|M}S_l.
\]

More generally, if

\[
M=\prod_l l^{e_l},
\]

then

\[
S_M
=
\prod_l l^{2(e_l-1)}S_l,
\]

because the survivor predicate depends only on reduction modulo each prime.

For an odd prime `l`, the exact slice survivor count is

\[
s_l(k)=
\begin{cases}
l-1,&k=0,\\
l-n_A(l)-n_B(l),&k\ne0.
\end{cases}
\]

For `l=2`, `s_2(0)=0` and `s_2(1)=2`.

These formulas average exactly to `S_l` as required by Theorem 9.

#### Proof

If both channel forms vanished at a nonzero pair modulo `l`, then their difference gives `ab=0`. If `a=0`, then `A=b^2=0`, so `b=0`; similarly if `b=0`. Thus the only common zero is the origin.

Each projective root direction contains `l-1` nonzero vectors. Inclusion-exclusion gives

\[
|Z_A\cup Z_B|
=
1+(n_A+n_B)(l-1),
\]

and subtracting from `l^2` gives the formula.

The CRT and prime-power lifting formulas are immediate from independence of residue coordinates. The slice formula follows from Theorem 6 and disjointness of the two channel root sets when `k!=0`. ∎

This is a finite exact identity only; it is not an asymptotic prime theorem.

## 4. Failed conjectures and counterexamples

### F1 — “The scalar product `N=AB` uniquely identifies the primitive cell”

False.

Counterexample:

- `(14,43)` gives `(A,B)=(2045,1443)`;
- `(31,38)` gives `(A,B)=(2405,1227)`;

yet both give `N=2,950,935`.

### F2 — “The ordered coordinates are recoverable from `(A,B)` alone”

False.

Coordinate swap preserves both readouts. For example,

\[
(2,5)\quad\text{and}\quad(5,2)
\]

both give

\[
(A,B)=(29,19).
\]

The marked ratio `r` of Theorem 3 repairs exactly this loss.

### F3 — “Every simultaneously-prime cell is isolated”

False.

\[
(1,2):\ (A,B)=(5,3)
\]

is a nearest carrier neighbor of

\[
(2,3):\ (A,B)=(13,7).
\]

The correct uniform statement is component size at most `2`.

### F4 — “Prime `2` and prime `3` follow the generic root-count formulas without exceptions”

False.

At `l=2`, `A` has one projective zero direction and `B` has none; on the `k=0` slice, `A_k` vanishes for both values of `t`.

At `l=3`, `B` has one double projective root rather than two distinct order-6 roots.

### F5 — “Primitive coprimality conclusions extend unchanged to nonprimitive cells”

False.

At `(a,b)=(2,2)`,

\[
(A,B)=(8,4),\qquad \gcd(A,B)=4=\gcd(a,b)^2.
\]

Thus the two channels can share prime divisors in the nonprimitive case.

### F6 — “Channel-dividing primes occupy disjoint residue classes modulo 12”

False as a global statement across different cells.

Prime `13` can divide the `A` channel, e.g. `A(2,3)=13`, and can also divide the `B` channel, e.g. `B(1,4)=13`.

The correct statement is that on one fixed primitive cell the two channel values are coprime.

### F7 — “The marked ratio construction extends unchanged to an axis cell”

False / undefined in that chart choice.

If `b=0`, the marker `a b^{-1}` is undefined. Axis cells also satisfy

\[
A=B=a^2
\]

(or symmetrically `b^2`) and therefore no positive axis cell is simultaneously prime. The marked-carrier theorem is intentionally scoped to positive interior primitive cells.

### F8 — Global seam continuation

No global seam theorem was asserted. The permitted primitive definition explicitly leaves cross-sector chart transitions unresolved. Therefore the sector-local adjacency theorem was not globalized.

## 5. Executable checker and actual finite ranges

Independent checker:

`experiments/prime_fusion_independent_replication_checker.py`

Checker commit before return freeze:

`d82849c725553f4fd177a64e3956b858f8b2b19d`

The checker uses exact integer arithmetic only and was authored without reading the source-run checker.

Actual executed ranges:

- identities / gcd / unordered recovery:
  `0 <= a,b <= 300`, excluding `(0,0)`;
- marked-carrier reconstruction:
  every primitive positive cell in `1..180` in each coordinate,
  `19,759` cells;
- scalar collision search:
  primitive unordered cells in box `<=80`;
- prime-modulus direction, root, and survivor classifications:
  every prime `<=199`;
- allowed divisor-class witness construction:
  every prime `<=199`;
- simultaneous-prime congruence / reciprocity:
  positive box `1..350`,
  `3,610` cells with `P>2,Q>3`;
- sector-local adjacency:
  positive box `1..350`,
  `3,612` simultaneously-prime nodes;
- finite two-dimensional / slice mean and CRT checks:
  `M in {6,30,210,385}`;
- mandatory negative/degeneracy tests:
  nonprimitive case, axes through `99`, coordinate swap,
  small primes `2,3`, and explicit adjacency counterexample.

Actual execution result:

```text
PASS identities/recovery/gcd: 0<=a,b<=300, excluding (0,0)
PASS marked carrier reconstruction: 19759 primitive positive cells in box 1..180
PASS scalarization collision search: box<= 80; N=2950935; cells=[(14, 43, 2045, 1443), (31, 38, 2405, 1227)]
PASS modular direction/root/survivor classifications: every prime <= 199
PASS allowed prime-divisor classes have primitive witnesses through p<=199
PASS simultaneous-prime congruence/reciprocity: 3610 cells in box 1..350
PASS sector-local adjacency: 3612 nodes, max component=2, box 1..350; B=3 exceptions=[(1, 2), (2, 1)]
PASS finite dimensional-reduction mean identity + squarefree CRT counts: M=(6, 30, 210, 385)
PASS mandatory negative/degeneracy tests
ALL CHECKS PASS
```

Finite computation is used only as audit evidence; the general statements above are proved algebraically.

## 6. Unresolved claims / deliberate non-claims

1. **Cross-sector seam/global graph:** unresolved because no explicit current chart-transition rule was permitted/provided. No global three-sector component bound is claimed.
2. **Bit-optimal finite encoding:** not proved. What is proved is marker-count minimality in the natural quotient model: unmarked `Z/NZ` fails globally, while one distinguished residue `[r]` suffices.
3. **Classification of all scalar collisions `AB=N`:** not attempted. One exact collision suffices to refute scalar uniqueness.
4. **Higher reciprocity beyond the proved elementary quadratic relations:** not classified.
5. **Asymptotic simultaneous-prime density or infinitude:** no claim. The dimensional-reduction statement is finite and exact only.

## 7. Final classification

`FULL_STRUCTURAL_REPLICATION`

Reason:

- R1: exact identities, exact gcd law, and necessary/sufficient coordinate recovery were proved;
- R2: a natural single finite quotient with one marked residue was constructed, scalarization loss was explicitly refuted by collision, and ordered reconstruction was proved;
- R3: prime-direction classes, divisor congruence classes, combined modulus `12`, and exact slice root counts were proved including `2,3`;
- R4: simultaneous-prime congruence and quadratic-reciprocity constraints were proved exactly;
- R5: the one-sector nearest-neighbor graph was classified with a sharp uniform component bound `2` and the `B=3` exceptions were handled;
- R6: an exact finite 2D-to-1D slice mean identity and exact modular survivor counts were proved;
- mandatory negative tests produced explicit counterexamples and scope restrictions;
- an independently authored exact-integer checker passed all stated finite audit ranges.

Hard target:

`PRIME_FUSION_CORE_INDEPENDENTLY_RECONSTRUCTED_OR_REFUTED = ACHIEVED`

This return is frozen before any source-package comparison. Per taskbook, no theorem package comparison is performed here.
