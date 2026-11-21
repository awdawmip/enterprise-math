# EC49FVW — Exact second-order residual spectrum at rational phase anchors

**Track:** EC49AS / frozen BRC16943, portable mathematical continuation of EC49FVU.
**Immutable scientific parent:** `awdawmip/enterprise-math@ac3bdb073b8ccd821cd23e830bcb9ccaf8d09529:research_notes/portable_direct/EC49FVU_RATIONAL_ANCHOR_DETERMINANT_ONE_THEOREM.md`.
**Inputs retained:** `U=4822040484/8132285009`, `Gamma=141024/1653649`, the complete mod-11 projective exclusion rule of EC49FVU. No repinning of upstream mathematical or worldview inputs.
**Status:** AUTHOR_PROVED / EXACT_FINITE_RESIDUE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED. An internal rational-phase certificate theorem; no new physical X6 transfer is asserted.

## Theorems

Define the certificate predicate on positive integers by

\[
C_{11}(h,n)\iff (h\bmod10,n\bmod10)\in P_{10}\quad\&\quad 9h+10n\not\equiv0\pmod {11},
\]
where the exact 44-entry set `P10` is reconstructed from the frozen projective equations (script below). Let `S_H` be the certified reduced fractions `h/d` with `0<h<d<=H` and `C11(h,d-h)`.

**Theorem A (arbitrary fixed rational anchor).** Let `a/b in (0,1)` be reduced, `b>=2`. For all integer `H>16b`, let `x_-(H)<a/b<x_+(H)` be the actual nearest *strict* certified neighbors from EC49FVU. Write the corresponding denominators `q_±(H)=H-r_±(H)`. Then `0<=r_±(H)<=8b`, and both integer deficit functions have period dividing `110b`. Defining the anchor bracket `B(H)=x_+(H)-x_-(H)` and

\[
\rho_{a/b}(H)=\frac{r_-(H)+r_+(H)}{b},
\]
we have the **exact finite-height identity**

\[
B(H)=\frac{2}{bH}+\frac{\rho_{a/b}(H)}{H^2}
+\frac{1}{bH^2}\left(\frac{r_-^2}{H-r_-}+\frac{r_+^2}{H-r_+}\right).
\]

The displayed remainder is nonnegative and at most `128b/(H^2(H-8b))`. Consequently

\[
0\le H^2\bigl(B(H)-2/(bH)\bigr)-\rho_{a/b}(H)
\le \frac{128b}{H-8b}.
\]

For each residue class `H mod 110b`, the second-order rescaled bracket converges to the corresponding exact rational value of the periodic function `rho`. If the anchor is uncertified, `B(H)` is an *actual adjacent gap* of `S_H`; if it is certified, `B(H)` is the span of the two adjacent gaps around that anchor. For moving anchors `b=o(H)`, the displayed error tends to zero uniformly, although the particular periodic functions depend on the anchor.

**Theorem B (exact spectrum at the missing anchor 1/2).** For every integer `H>32`, the middle gap `G_{1/2}(H)=B(H)` is an actual gap because `C11(1,1)=false`. The two deficits have exact period 220, satisfy `0<=r_±<=5`, and their second-order coefficient

\[
\rho(H)=\frac{r_-(H)+r_+(H)}2
\]

has **minimal period 220** and takes the values 0,1,2,3,4 with the following exact frequencies in each block of 220 consecutive heights:

| `rho` | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Count | 54 | 99 | 55 | 11 | 1 |

Its period mean and variance are exactly `123/110` and `8741/12100`. More sharply,

\[
0\le H^2(G_{1/2}(H)-H^{-1})-\rho(H)\le\frac{25}{H-5}.
\]

For `H=220m+3`, `m>=1`, both deficits vanish and `G_{1/2}(H)=1/H` exactly. For `H=220m+82`, `m>=0`, the deficits are `(r_-,r_+)=(5,3)`, so

\[
G_{1/2}(H)=\tfrac12\bigl((H-5)^{-1}+(H-3)^{-1}\bigr),
\qquad \lim_{m\to\infty}H^2(G_{1/2}(H)-1/H)=4.
\]

Thus `H G_{1/2}(H)->1`, but the next `H^-2` coefficient has a genuine 220-height structural residual and **does not converge to a single constant**. Averaging that coefficient over a full residue period gives `123/110`; replacing it by its average loses exact finite-height information.

## Proof

**A.** The EC49FVU determinant-one theorem gives the exact nearest neighbors `(a q_- -1)/(b q_-)` and `(a q_+ +1)/(b q_+)`, with `H-8b<=q_±<=H`. Its certificate predicate depends only on `(h mod 10,n mod 10,9h+10n mod 11)`. Along each determinant-one line, consecutive admissible denominators differ by `b` and the certificate repeats after 110 steps, so `q_±(H+110b)=q_±(H)+110b` and the deficit functions are periodic. The exact bracket is `(1/b)(1/(H-r_-)+1/(H-r_+))`. Apply the identity

\[
\frac1{H-r}=\frac1H+\frac r{H^2}+\frac{r^2}{H^2(H-r)}
\]

twice. The bound follows from `r_±<=8b`, i.e. `r_-^2+r_+^2<=128b^2`. This proof also establishes the stated uniformity when `b=o(H)`.

**B.** For anchor 1/2, determinant-one admissibility forces the denominator `q` to be odd and the numerator `h=(q+s)/2` for each side sign `s in {-1,+1}`. For each sign compute the complete set `R_s` of qualifying odd `q mod 220` via the **frozen** `C11`. Since `(h,n)` changes by `(110,110)` when `q` changes by 220, the certificate repeats exactly. The accompanying checker independently reconstructs `P10` from all 11 original finite-field projective rows, compares the simplified certificate with all 12,100 positive residue pairs, and enumerates both `R_s` completely. Each has exactly 80 elements and maximum cyclic spacing 6 in denominator units, so the most recent qualifying denominator lies within 5 of `H`. For every `H=1,...,220` determine its two deficits by scanning backwards at most five integers modulo 220. Full enumeration gives the displayed histogram, its period minimality (all proper divisors of 220 fail), and `r(3)=(0,0)`, `r(82)=(5,3)`. The exact mean and variance are obtained from the histogram:

\[
E\rho=(99+2\cdot55+3\cdot11+4)/220=123/110,\quad
E\rho^2=217/110,
\quad \operatorname{Var}\rho=8741/12100.
\]

The universal identity A with `b=2`, `r_±<=5` gives the sharper remainder bound `25/(H-5)`. The two displayed progressions and nonconvergence follow. All period calculations use integers and exact fractions, and every finite domain is explicit.

## Validation and scientific boundaries

The companion `EC49FVW_SECOND_ORDER_SPECTRUM_VERIFY.py` uses only Python standard-library exact arithmetic. It verifies 12,100 direct projective comparisons, both complete 220-class signed denominator sets, the 220-value frequency table and minimal period, moments, four independent complete reduced-Farey neighbor enumerations (`H=33,82,223,302`), and four additional rational-anchor periodicity checks (`1/3,2/3,3/7,5/11`). Original output ends `ALL PASS`.

The new second-order result is mathematical and **conditional on the inherited EC49FVU determinant-one neighbor theorem and its BRC16943-to-projective reduction**. There is no independent review yet, and no new claim of physical native X6/time behavior. No change to P000, ACTIVE worldview, underlying task publication or frozen inputs.

**Next mathematical question:** classify second-order spectra across families of rational anchors, especially `b` growing with `H`, and determine whether the observed global maximum-gap conjecture `H G_max(H)->1` can be controlled via determinant-one corridors or a suitable non-anchor argument. Retain the full signed residue pair `(r_-,r_+)` as the minimal direct carrier of exact left and right gap information; its sum suffices only for this second-order bracket observer, not for arbitrary future operations.
