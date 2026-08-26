# P017 — A6 Five-Ninth Root-Edge P2 Package

Status: `PROVED_WIP SOURCE-DECIMAL ENCLOSURE + EXACT PARAMETER/POWER CERTIFICATE / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- H. Iwaniec and M. Laborde, *P2 in short intervals*, Ann. Inst. Fourier 31 (1981), especially the simplified p. 53–54 main coefficient and Lemma 4;
- `docs/P017_P2_W1_SOURCE_FORMULA_AUDIT_20260826.md`;
- the exact P017 carry bridge and super-root complement/collision supplements.

This note deliberately avoids the `a=4` unsimplified `W_1` normalization that was corrected on 2026-08-26. It instead revisits the later `a=6`, `b>=3` Laborde-simplified family and chooses a parameter packet whose high-prime endpoint is **exactly** the square-root horizon.

The main-term certificate below is a rigorous enclosure **conditional only on the standard prefix interpretation of the decimals printed in Iwaniec–Laborde 1981**. Direct recovery of the underlying Laborde 1979 constants remains desirable and would remove that provenance dependency.

---

## 1. Root-edge parameter choice

Freeze

\[
\theta=\frac{4999}{10000},
\qquad
D=X^{5/9},
\qquad
a=6,
\]

and choose

\[
\boxed{
b=\frac{22}{5},\qquad c=\frac{27}{5}.}
\]

Then

\[
b+c+1
=\frac{22}{5}+\frac{27}{5}+1
=\frac{54}{5}
=\frac{a}{5/9},
\]

so the Lemma-1 relation is exact.

The induced prime cut points are

\[
z=D^{1/a}=X^{5/54},
\]

\[
D^{b/a}=X^{11/27},
\]

and

\[
\boxed{D^{c/a}=X^{1/2}.}
\]

Thus the terminal weighted-prime endpoint is exactly the P017 square-root visibility boundary. Also

\[
\frac{11}{27}<\theta<\frac12<\frac32\theta,
\]

and

\[
3<b<c<a.
\]

---

## 2. Selberg auxiliary level

The analytic Lemma-6 ceiling has base exponent

\[
\frac{3\theta-1}{2},
\]

while

\[
z^2=X^{5/27}.
\]

For the present package

\[
\frac{5}{27}<\frac{3\theta-1}{2}.
\]

Hence the legal auxiliary Selberg level is capped by `z^2`, not by the larger analytic ceiling. Suppressing an arbitrarily small strictness loss, write

\[
\delta_1=\frac{5}{27}.
\]

A fully effective implementation should use `5/27-eta_1` and charge the resulting arbitrarily small loss explicitly. The main enclosure below uses the limiting exponent `5/27` as the asymptotic coefficient target.

---

## 3. Source-decimal enclosure of the Laborde constants

Iwaniec–Laborde print their `theta=0.45` optimum in the form

\[
c_0=5.1828\ldots,
\qquad
b_0=4.8698\ldots,
\qquad
G_0=0.00177\ldots.
\]

Interpret these printed ellipses as the prefix intervals

\[
\frac{51828}{10000}\le c_0\le\frac{51829}{10000},
\]

\[
\frac{48698}{10000}\le b_0\le\frac{48699}{10000},
\]

\[
\frac{177}{100000}\le G_0\le\frac{178}{100000}.
\]

At the published reference point

\[
\theta_0=\frac9{20},
\qquad
d_0=\frac{19}{35},
\qquad
\alpha_0=\frac{13}{63},
\]

the first-order condition in `c` gives

\[
B_1
=\frac12\left[
\frac{c_0-189/38}{(147/152)^2}
-\frac16\log\frac{13}{63}
\right].
\]

Using the exact rational atanh enclosure for every logarithm gives

\[
0.24330708978205\ldots
< B_1
<0.24336054898888\ldots.
\]

It is not necessary to isolate `B_2`: subtract the published reference identity from the new one.

Let

\[
N_0(c)
=-\frac c6\log\frac{189}{38}
-\frac{6-c}{6}\log\frac{39}{38}
-2\left(
\frac{c(19/35)-27/10}{21/20}
\right)^2.
\]

For the new root-edge packet, put

\[
\alpha=\frac{5009}{44991},
\]

so that

\[
\frac6{1+\alpha}=\frac{134973}{25000},
\qquad
\frac{6\alpha}{1+\alpha}=\frac{15027}{25000}.
\]

Define

\[
N_*(c)
=-\frac c6\log\frac{134973}{25000}
-\frac{6-c}{6}\log\frac{15027}{25000}
-2\left(
\frac{cd/6-\theta}{5/27}
\right)^2.
\]

Then the new simplified coefficient can be written without `B_2` as

\[
\boxed{
G_*
=G_0
+B_1\bigl[(c-b)-(c_0-b_0)\bigr]
+N_*(c)-N_0(c_0).
}
\]

The companion exact-rational interval verifier encloses every logarithm by

\[
\log x
=2\sum_{j=0}^{N}\frac{z^{2j+1}}{2j+1}+R_N,
\qquad
z=\frac{x-1}{x+1},
\]

\[
|R_N|
\le
\frac{2|z|^{2N+3}}{(2N+3)(1-z^2)}.
\]

With `N=30`, it proves

\[
0.11480971345\ldots
<G_*
<0.11495463931\ldots.
\]

In particular,

\[
\boxed{G_*>\frac{287}{2500}=0.1148.}
\]

### Provenance boundary

This is stronger than a floating-point optimizer diagnostic: all downstream arithmetic is exact rational interval arithmetic. However, it still relies on reading the 1981 printed decimal ellipses as prefix intervals. Until the underlying Laborde constants are recovered directly from their defining source, label this `SOURCE-DECIMAL ENCLOSURE`, not an independent exact reconstruction of `B_1,B_2`.

---

## 4. The refined exponent pair is unnecessary

For effectivity, freeze

\[
\varepsilon=\frac1{200}
\]

and choose the bilinear split

\[
\boxed{
M=X^{31/72},
\qquad
N=X^{1/8}.
}
\]

Then

\[
MN=X^{31/72+1/8}=X^{5/9}=D.
\]

### Condition A2

The sufficient diagonal condition is

\[
M<yX^{-6\varepsilon}.
\]

Its exact exponent margin is

\[
\theta-6\varepsilon-\frac{31}{72}
=\boxed{\frac{3541}{90000}}
\approx0.0393444>0.
\]

### Condition A3

\[
MN^2=X^{31/72+1/4}=X^{49/72}<X,
\]

with margin

\[
\boxed{\frac{23}{72}}.
\]

### Condition A4

The original trivial `(1/2,1/2)` zone requires

\[
MN^2
\le
y^{5/2}X^{-1/2-4\varepsilon}.
\]

The exact exponent margin is

\[
\frac52\theta-rac12-4\varepsilon-rac{49}{72}
=\boxed{\frac{1771}{36000}}
\approx0.0491944>0.
\]

Therefore the delicate `(1/14,11/14)` refinement is not on the critical path for this packet.

---

## 5. Structural power saving of one bilinear block

The displayed diagonal estimate in the Lemma-4 proof gives, after Cauchy, the `|S|^2` exponent

\[
\frac{31}{72}-\theta+3\varepsilon
=-\boxed{\frac{4891}{90000}}.
\]

Hence

\[
\boxed{
\delta_{\rm diag}
=\frac{4891}{180000}
\approx0.0271722.
}
\]

For the trivial off-diagonal estimate, the `|S|^2` exponent is

\[
2(d-\theta)
+\frac{1-\theta}{2}
+3\varepsilon
-\frac{31}{72}
=-\boxed{\frac{1951}{36000}}.
\]

Thus

\[
\boxed{
\delta_{\rm off}
=\frac{1951}{72000}
\approx0.0270972.
}
\]

So, before explicit analytic constants and logarithmic multiplicities,

\[
\boxed{
|S(H,M,N)|
\ll X^{-1951/72000+o(1)}.
}
\]

This is substantially more power room than the four-sevenths trivial-pair packet, whose corresponding off-diagonal structural saving is `1073/56000 ~= 0.0191607`.

---

## 6. Why this packet is now the preferred effectivity candidate

The corrected 2026-08-26 source audit invalidated the old `a=4, d=5/9` positive claim but did not invalidate the `a=6` Laborde-simplified family.

The present root-edge package has four attractive properties simultaneously:

1. total level `D=X^(5/9)` is shallower than `X^(4/7)`;
2. the terminal weighted-prime endpoint is exactly `X^(1/2)`;
3. the original trivial exponent pair already gives a structural saving about `0.0271`;
4. the source-decimal enclosure still leaves `G_*>0.1148`.

The last number and the corrected `a=4` coefficient `>0.1066` arise from two presentations of the Iwaniec–Laborde main term. Before making a strict statement that one numerical reserve dominates the other, their normalization should be checked onto one common final sieve-count scale. The bilinear exponent comparison, however, is direct.

---

## 7. P017-specific reductions remain active

The exact P017 bridge remains

\[
O_m(K)-\frac Km=r_K(m)-r_K(2m).
\]

Above the root, the same remainder can also be represented as a discrepancy of disjoint reciprocal complement windows. Distinct-prime reuse is confined to the Boolean shared-small-core collision kernel; the exact-Mobius top-third and `t=1` sectors collapse further.

Therefore the correct finite-threshold strategy is not to pay the generic Lemma-4 constant uniformly over the whole `D=X^(5/9)` support. It is to:

1. strip exact anchor factors when an adaptive interval length permits it;
2. remove the coefficient-uniform additive `O(sqrt(K))` root halo by the quadratic-excess estimate;
3. collapse the exact top-third / first-packet collision sectors;
4. invoke the generic trivial-pair bilinear bound only on the residual sector that survives these exact square-specific reductions.

---

## 8. Remaining gates

1. Recover/directly certify the Laborde constants behind the 1981 printed `B_1,B_2`, replacing the source-decimal enclosure.
2. Put the `a=6` simplified `G_*` and the `a=4` corrected coefficient on one explicit final-count normalization.
3. Extract actual numerical constants for the trivial `(1/2,1/2)` terminal exponential-sum estimate and the Lemma-2 bilinear-form multiplicity.
4. Quantify how much support is removed by the P017 complement/collision/anchor reductions before those constants are charged.
5. Compare the resulting explicit threshold with the conservative finite splice `X≈1.3458153218e34`.

No P2-in-every-square theorem, no Legendre theorem, and no finite analytic threshold is claimed here.
