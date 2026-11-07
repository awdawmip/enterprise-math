# S23/AV: exact finite-future saturation plateau through horizon 2500

Date: 2026-11-08 Asia/Shanghai. Status: `AUTHOR_SIDE_EXACT_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED`.

Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34` (unchanged).

## Theorem

For the two-point S23/AV iid auxiliary likelihood-sign observer defined below, let

\[
T_h=\{10^i/7^s:0\le i\le s\le h\}
\]

and let \(N(h)\) be the least common padded prefix length whose attainable likelihood-sign values meet every open cell of the threshold partition induced by \(T_h\). Then

\[
\boxed{N(h)=2\,455\,069\quad\text{for every integer }510\le h\le2500.}
\]

The predecessor certificate proved \(N(510)=2\,455\,069\) and \(N(h)=2\,455\,069\) through \(h=2000\). This note extends the exact endpoint certificate to \(H=2500\); by threshold nesting, one endpoint proves the whole interval.

## Auxiliary experiment and exact observer

The one-step laws on ordered labels \((1,3,4)\) are

\[
P_0=(1/2,1/4,1/4),\qquad P_1=(5/7,1/4,1/28).
\]

A prefix with \(k\) occurrences of label 1 and \(\ell\) occurrences of label 4 has likelihood ratio

\[
\Lambda(k,\ell)=\frac{7^{k+\ell}}{10^k};
\]

label 3 pads a prefix without changing this ratio. Put

\[
r=\frac{\log 7}{\log(10/7)},\qquad E(k,\ell)=k-r\ell.
\]

A threshold \(10^i/7^s\) is represented in reflected logarithmic coordinates by

\[
t(v,j)=rv-j,\qquad v=s-i,\quad j=i,\quad v+j=s\le h.
\]

Thus the threshold set has the same order as
\(\{t(v,j):v,j\ge0,\ v+j\le h\}\), and a prefix occupies an open threshold cell exactly when \(E(k,\ell)\) lies strictly between its two endpoint coordinates. This is the auxiliary finite-future likelihood-sign observer; it is not the full six-source/ten-label mother experiment.

The threshold sets are nested. Refining a threshold partition cannot reduce the least prefix length needed to hit every open cell, so \(N(h)\) is nondecreasing in \(h\). The already verified predecessor theorem \(N(510)=2\,455\,069\) therefore gives

\[
N(h)\ge2\,455\,069\qquad(h\ge510).
\]

It remains to certify the matching upper bound at \(H=2500\).

## Exact rational enclosure for the logarithmic coordinate

With \(Q=10^{26}\), the verifier proves

\[
\frac{545569623581288298975349314}{Q}
<r<
\frac{545569623581288298975349315}{Q}.
\]

No floating-point logarithm is used. For \(0<z<1\),

\[
2\operatorname{atanh}(z)
=2\sum_{j=0}^{44}\frac{z^{2j+1}}{2j+1}+R,
\qquad
0<R<
\frac{2z^{91}}{91(1-z^2)}.
\]

The exact identities are

\[
\log2=2\operatorname{atanh}(1/3),\quad
\log(5/4)=2\operatorname{atanh}(1/9),\quad
\log(8/7)=2\operatorname{atanh}(1/15),
\]
\[
\log7=3\log2-\log(8/7),\qquad
\log(10/7)=\log(5/4)+\log(8/7).
\]

All partial sums and remainders are rational `Fraction` values. The strict interval is converted to integer cross-multiplication bounds with the displayed \(Q\).

## Complete endpoint certificate at \(H=2500\)

There are

\[
M=\frac{2501\cdot2502}{2}=3\,128\,751
\]

distinct thresholds and \(M+1=3\,128\,752\) open cells. Distinctness follows from irrationality of \(r\): a rational value of \(r\) would imply \(7^{p+q}=10^p\) for positive integers \(p,q\), contradicting prime factorization.

### 1. Complete threshold order

The verifier sorts all \((v,j)\) by the rational lower key
\(lo\cdot v-Q\cdot j\), then checks all \(3\,128\,750\) adjacent strict comparisons. For a neighboring pair with difference \((\Delta v,\Delta j)\), it checks

\[
(lo\ \text{if }\Delta v\ge0\text{ else }hi)\,\Delta v
>Q\,\Delta j.
\]

Because \(lo/Q<r<hi/Q\), every checked inequality is the true strict order for \(rv-j\). This certifies the complete ordering, including the two unbounded outer cells.

### 2. Explicit witnesses for the translated near-resonance cells

Reuse the determinant-one integer basis

\[
u=(79,431),\qquad w=(380295,2074774),
\qquad \det(u,w)=1.
\]

Write \(p=2\,074\,774\), \(q=380\,295\), and \(n_*=p+q=2\,455\,069\). For every nonnegative shift \((v_0,j_0)\) with

\[
v_0+j_0\le H-510=1990,
\]

the verifier checks that \((v_0,j_0)\) and \((v_0+79,j_0+431)\) are consecutive thresholds in the complete \(T_{2500}\) ordering. There are exactly

\[
\frac{1991\cdot1992}{2}=1\,983\,036
\]

such special cells.

For each one, the explicit prefix counts

\[
(k,\ell)=(p-j_0,\ q-v_0)
\]

are nonnegative and have length

\[
k+\ell=n_*-(v_0+j_0)\le n_*.
\]

The verifier certifies strict cell membership using the adverse rational endpoints:

\[
(k+j_L)Q>hi(\ell+v_L),\qquad
(k+j_R)Q<lo(\ell+v_R),
\]

where \((v_L,j_L)\) and \((v_R,j_R)\) are the cell endpoints. The SHA-256 digest of the ordered `(cell-index,k,ell)` special-witness stream is

`d95b402f8c3b030cf7fe5e4bf9400c5a27703af60e0a14a1abdb98919c67f26e`.

### 3. Exact witnesses for every remaining cell

The remaining number of cells is

\[
3\,128\,752-1\,983\,036=1\,145\,716.
\]

For each such cell, the verifier searches prefixes with \(k+\ell\le15\,000\). A rational key is used only to locate a candidate interval; a cell is marked only after both strict integer inequalities above (or the applicable one-sided inequality for an outer cell) pass. Thus every accepted witness is certified against the true irrational coordinate, not merely its approximate sorting key.

The search certifies all \(1\,145\,716\) remaining cells. The maximum short-witness length is \(13\,640\), and the maximum label-4 count is \(463\). The SHA-256 digest of the ordered `(cell-index,k,ell)` short-witness stream is

`b8d1c552ba3e204e1a99402bd97dd89bc88f70c9fffd0705f53d2e3487c5fcbf`.

At termination, the verifier asserts that the set of unmarked cells is **exactly** the special-cell set. Therefore every open cell of \(T_{2500}\) has a prefix witness of length at most \(n_*\). Padding with label 3 gives a common prefix length \(n_*\), proving

\[
N(2500)\le n_*.
\]

Combining this with the inherited lower bound yields \(N(2500)=n_*\). Monotonicity and \(N(510)=n_*\) now give the theorem for every integer \(510\le h\le2500\).

## Verification scope and limits

`VERIFY_H2500.py` was executed under Python 3.13.5 using only the standard library (`Fraction`, integer arithmetic, `bisect`, and SHA-256). It checked:

- the strict rational enclosure for \(r\);
- all 3,128,750 adjacent threshold-order comparisons;
- all 1,983,036 translated-gap adjacencies and their exact witnesses;
- all 1,145,716 remaining cells with strict integer witness checks;
- exact equality between the unmarked-cell set and the special-cell set.

The actual stdout and source SHA-256 are in `RUN_EVIDENCE.txt`. This is an exact finite certificate for the stated endpoint plus the inherited analytic lower bound; it is not a floating-point extrapolation.

BRC observer reuse is explicit: the joint \((\#1,\#4)\) count is retained and label-3 padding is kept as a distinct no-change operation. For this exact likelihood-sign output, each ordered word's likelihood ratio factors through that joint count; the declared future horizon is finite and explicit. This is not a factor-only erasure of a composite/background direction, and no broader quotient is claimed. The current P000 V5 and joint-relation observer-preservation contract remain unchanged. This auxiliary statistical result does not establish native X6/Heartbeat geometry, full-lawful \(\delta_4\), or a lawful transfer to the six-source/ten-label mother decoder.

## Next question

Find the first \(h>2500\) for which \(N(h)>2\,455\,069\), or extend the endpoint certificate further. In parallel, retain the independent full-lawful \(\delta_4\) minimax equality question and the source/time-typed six-source/ten-label mother-model bridge.
