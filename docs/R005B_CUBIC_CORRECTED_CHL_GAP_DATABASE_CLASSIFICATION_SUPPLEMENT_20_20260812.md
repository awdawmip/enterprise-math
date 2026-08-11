# R005-B — Corrected Cully–Hugill–Lee × Gap-Database Cubic Classification

Status: `PROVED R005 REDUCTION + CORRECTED EFFECTIVE INTERVAL INPUT + EXTERNAL FINITE GAP DATA / NOT CANONICAL`  
Date: `2026-08-12`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: R005-A T-A19; R005-B Supplements 15, 17–19

## 1. Main result

The finite cubic full-forcing classification extends again.

Using:

1. Sorenson–Webster's finite Oppermann verification through
   \(N=7.05\cdot10^{13}\);
2. the **corrected** Cully–Hugill–Lee effective prime-interval theorem, in
   particular the Table-2 row
   \[
   \log x_0=60,\qquad
   \boxed{\Delta=7.69184\cdot10^{10}};
   \]
3. the current Prime Gap List exhaustive consecutive-gap data through
   \(10^{20}\), including the maximal-gap cap 1724 below that bound;
4. the exact small-prefix classification from Supplement 17;

we obtain the complete finite classification

\[
\boxed{2\le k\le10{,}000{,}000{,}000.}
\]

Full cubic candidate forcing holds at every k in this range except exactly

\[
\boxed{23,64,120,138,1005,}
\]

with complete non-forced candidate sets

\[
\boxed{
\{109\},\quad
\{509\},\quad
\{1303,1307\},\quad
\{1621\},\quad
\{31859\}.
}
\]

The new endpoint is not the limit of the corrected effective interval theorem.
It is the exact endpoint of the current \(10^{20}\) **horizontal** cofactor-gap
database certificate.

The next integer k is not asserted to be a counterexample.

---

## 2. Correction audit for the effective interval input

The original Cully–Hugill–Lee paper was later corrected.  The current arXiv v3
explicitly states that it includes corrections to the published paper.
Theorem 1 says that for each pair \((\Delta,x_0)\) in its corrected Table 2,
there is a prime in

\[
\bigl(x(1-\Delta^{-1}),x\bigr]
\]

for every \(x\ge x_0\).

The corrected Table-2 rows relevant here include

\[
\begin{array}{c|c}
\log x_0&\Delta\\
\hline
55&1.02884\cdot10^{10}\\
60&7.69184\cdot10^{10}\\
75&1.74043\cdot10^{11}
\end{array}
\]

and not the much larger constants that appeared in the earlier uncorrected
version.

R005-B therefore freezes

\[
\boxed{\Delta_{60}=76{,}918{,}400{,}000}
\]

as the current effective row used in this supplement.

This correction changes the vertical numerical margin, but it does **not**
change the present finite endpoint: the corrected row is still far stronger
than required through \(k=10^{10}\).

---

## 3. B64 — exact Oppermann/effective-interval complement for q<=k

Let

\[
A=k^3,\qquad U=(k+1)^3-1,
\]

and let

\[
N=70{,}500{,}000{,}000{,}000.
\]

Take a candidate prime \(q\le k\).

### Case I — finite Oppermann covers q

If

\[
\boxed{k^3\le qN^2,}
\]

then

\[
\left\lceil\sqrt{k^3/q}\right\rceil\le N
\]

and R005-A T-A19 forces q from the verified first-half Oppermann interval.

### Case II — finite Oppermann does not cover q

Then

\[
qN^2<k^3.
\]

For the cofactor upper endpoint

\[
y=U/q
\]

we obtain

\[
\boxed{y>N^2.}
\]

Now

\[
N^2
=4{,}970{,}250{,}000{,}000{,}000{,}000{,}000{,}000{,}000
>e^{60}.
\]

Thus every q escaping the finite Oppermann computation automatically lands in
the size domain of the corrected Cully–Hugill–Lee \(\log x_0=60\) row.

There remains no size hole between the vertical certificates.

---

## 4. B65 — corrected CHL row fits far past the current data endpoint

Applying Cully–Hugill–Lee at

\[
y=U/q
\]

gives a prime r with

\[
y(1-\Delta^{-1})<r\le y.
\]

As in Supplement 19, this prime lies strictly above

\[
x=A/q
\]

exactly when

\[
U(1-\Delta^{-1})>A,
\]

equivalently

\[
\boxed{3(k+1)(\Delta-1)>k^2.}
\]

For q<=k, \(x\ge k^2>F_3(k)\), so such r is outside the candidate horizon and
qr is an e=1 exclusive collision.

For the corrected value

\[
\Delta_{60}=76{,}918{,}400{,}000,
\]

the exact largest integer satisfying the fit inequality is

\[
\boxed{230{,}755{,}199{,}997.}
\]

Indeed the margin at that k is

\[
230{,}755{,}199{,}997>0,
\]

and the next margin is exactly \(-1\).

Therefore at the current finite endpoint \(10^{10}\), vertical effective
coverage has enormous slack:

\[
3(10^{10}+1)(\Delta_{60}-1)-10^{20}
=
2{,}207{,}552{,}000{,}200{,}755{,}199{,}997>0.
\]

So q<=k is not the active finite bottleneck.

---

## 5. B66 — exact q>k horizontal-data endpoint

Take q>k.  Then q>=k+1 and

\[
\left\lfloor\frac{k^3}{q}\right\rfloor
\le
\left\lfloor\frac{k^3}{k+1}\right\rfloor
=
\boxed{k^2-k}.
\]

The current exhaustive prime-gap data are available for all gap starts below

\[
10^{20}.
\]

Therefore every q>k lower-cofactor point is inside the frozen database whenever

\[
k^2-k<10^{20}.
\]

The exact final integer satisfying this is

\[
\boxed{K_G=10{,}000{,}000{,}000.}
\]

At K_G,

\[
K_G^2-K_G
=
99{,}999{,}999{,}990{,}000{,}000{,}000
<10^{20},
\]

whereas

\[
(K_G+1)^2-(K_G+1)
=
100{,}000{,}000{,}010{,}000{,}000{,}000
>10^{20}.
\]

Thus the current complete finite theorem is **horizontal-data limited** at
exactly \(10^{10}\).

---

## 6. B67 — upper horizon remains closed throughout the extension

For the complete prefix through Supplement 17, upper non-forcing is already
classified exactly.

For larger k, the external maximal-gap cap gives

\[
R-F\le1724
\]

because the cubic factor horizon remains far below \(10^{20}\).

At

\[
k=10^{10},
\]

we have exactly

\[
S=10^{15},\qquad
F=1{,}000{,}000{,}000{,}150{,}000,
\]

so

\[
\boxed{F-S=150{,}000>1724.}
\]

The exact upper-closing inequality

\[
(F+1724)S\le U
\]

therefore holds with large margin.  The existing monotone/analytic drift bound
from Supplement 18 closes the entire interval from the old classified prefix to
K_G.

Thus no new upper exception is introduced.

---

## 7. B68 — corrected three-certificate complete classification theorem

Take

\[
2\le k\le10^{10}
\]

and candidate prime q<=F_3(k).

### q<=k

- if \(k^3\le qN^2\), finite Oppermann transport forces q;
- otherwise, q escapes Oppermann but automatically has \(U/q>N^2>e^{60}\),
  and the corrected Cully–Hugill–Lee e^60 row fits, so q is forced.

### q>k and q>S

q^2 itself lies in the cubic basin and forces q.

### k<q<=S, lower cofactor band

The cofactor point is at most \(k^2-k<10^{20}\), so Supplement 15's finite
prime-gap closure forces q.

### k<q<=S, upper horizon band

The 1724 gap cap plus factor-horizon drift closes the upper window outside the
already exactly classified small prefix.

These cases exhaust all candidates.

Combining with Supplement 17 yields full forcing for every k through 10^10
except exactly the five previously classified basins and candidate sets.

---

## 8. New finite frontier after 10^10

The next unresolved coordinate is much narrower than the original cubic
problem.

For q>k immediately beyond the current endpoint, the cofactor upper scale can
first enter

\[
\boxed{10^{20}<y=U/q<e^{55}.}
\]

Why this annulus matters:

- below \(10^{20}\), the exhaustive gap database applies;
- from \(e^{55}\) upward, the corrected CHL row
  \[
  \Delta_{55}=1.02884\cdot10^{10}
  \]
  already has enough relative precision near the present k scale;
- the lower-x0 corrected rows do not have sufficient \(\Delta\) at
  \(k\approx10^{10}\).

So after \(10^{10}\), the finite problem is no longer global in q.  It is a
specific **cofactor-scale annulus** between the current exhaustive computation
and the next sufficiently strong effective relative-interval row.

This is the natural next target for finite extension.

---

## 9. Status boundary

This supplement does not reprove:

- Sorenson–Webster's finite Oppermann computation;
- Cully–Hugill–Lee's corrected effective interval theorem;
- the Prime Gap List exhaustive computation.

It proves the exact certificate composition and endpoint conversion.

The endpoint \(10{,}000{,}000{,}001\) is not asserted to be a counterexample.
It is the first k for which the worst q>k cofactor coordinate exceeds the
selected \(10^{20}\) exhaustive-data boundary.

The asymptotic cube-root prime-gap knife edge remains unchanged.
