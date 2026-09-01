# R005-B — Cubic Oppermann × Kadiri–Lumley × Prime-Gap Certificate Cover

Status: `PROVED R005 REDUCTION + EXTERNAL FINITE/EFFECTIVE INPUTS / NOT CANONICAL`  
Date: `2026-08-12`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: R005-A T-A19; R005-B Supplements 15, 17, 18

## 1. Main result

Supplement 18 extended the complete cubic full-forcing classification to the
finite Oppermann endpoint

\[
2{,}150{,}153{,}225.
\]

The endpoint is not intrinsic.  The candidate q<=k region admits a second
certificate that begins automatically exactly where finite Oppermann coverage
ends.

Using Kadiri–Lumley's effective prime-interval theorem at

\[
x_0=e^{59},\qquad \Delta=1{,}946{,}282{,}821,
\]

together with the same current Prime Gap List data layer as Supplement 15, the
complete classification extends to

\[
\boxed{2\le k\le5{,}838{,}848{,}460.}
\]

There are still exactly five exceptional basins:

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

No new exception occurs between the Oppermann endpoint and the new effective
interval endpoint.

## 2. External inputs

### 2.1 Finite Oppermann computation

Sorenson and Webster computationally verified Oppermann's conjecture through

\[
N=7.05\cdot10^{13}.
\]

R005-A T-A19 shows that a cubic candidate q<=k is forced whenever

\[
\left\lceil\sqrt{k^3/q}\right\rceil\le N.
\]

### 2.2 Kadiri–Lumley effective interval at e^59

Kadiri and Lumley prove that for every x>x0 there is a prime p satisfying

\[
(1-\Delta^{-1})x<p<x,
\]

with effective Delta depending on x0.  Their stated value at

\[
x_0=e^{59}
\]

is

\[
\boxed{\Delta=1{,}946{,}282{,}821.}
\]

### 2.3 Current finite prime-gap computation

The q>k region continues to consume Supplement 15's external finite data:
exhaustive prime-gap analysis through 10^20 together with the maximal-gap cap
1724 and the exact Enterprise Math prefix certificate.

## 3. B59 — Oppermann failure automatically activates the Kadiri–Lumley scale

Fix k>=3 and a candidate prime q<=k.  Put

\[
A=k^3,\qquad U=(k+1)^3-1,
\]

and let

\[
N=70{,}500{,}000{,}000{,}000.
\]

There are exactly two cases.

### Case I — qN^2>=A

Then

\[
\sqrt{A/q}\le N,
\]

so

\[
\left\lceil\sqrt{A/q}\right\rceil\le N.
\]

R005-A T-A19 plus the finite Oppermann verification forces q.

### Case II — qN^2<A

Set the cofactor interval endpoints

\[
x=A/q,\qquad y=U/q.
\]

Then

\[
y>\frac{UN^2}{A}>N^2.
\]

But

\[
N^2
=4{,}970{,}250{,}000{,}000{,}000{,}000{,}000{,}000{,}000
>e^{59}.
\]

Therefore every q that has just escaped the finite Oppermann computation is
automatically above the Kadiri–Lumley x0 scale at its cofactor upper endpoint.

There is no uncovered size gap between the two certificate languages.

This complementarity is exact: the same inequality qN^2>=A / qN^2<A selects
which certificate is available.

## 4. B60 — exact Kadiri–Lumley fit condition for one cubic basin

Kadiri–Lumley applied at

\[
y=U/q
\]

produces a prime r with

\[
y(1-\Delta^{-1})<r<y.
\]

For r to lie strictly above the lower cofactor endpoint x=A/q, it suffices and
is algebraically equivalent to

\[
U(1-\Delta^{-1})>A.
\]

Since

\[
U-A=3k(k+1),
\]

this becomes

\[
\boxed{
3(k+1)(\Delta-1)>k^2.
}
\]

For q<=k,

\[
x=A/q\ge k^2>F_3(k),
\]

so the prime r is automatically outside the candidate-small-prime horizon.
Thus qr is an e=1 exclusive collision and q is forced.

The condition is independent of q.

## 5. B61 — exact e^59 endpoint

Freeze

\[
\Delta=1{,}946{,}282{,}821.
\]

The largest integer k satisfying

\[
3(k+1)(\Delta-1)>k^2
\]

is

\[
\boxed{K_{KL}=5{,}838{,}848{,}460.}
\]

Exact endpoint margins are

\[
3(K_{KL}+1)(\Delta-1)-K_{KL}^2
=5{,}838{,}848{,}460>0,
\]

whereas

\[
3(K_{KL}+2)(\Delta-1)-(K_{KL}+1)^2=-1.
\]

Hence K_KL is the exact final cubic basin certified by this particular
Kadiri–Lumley table row.

## 6. B62 — q>k remains inside the current finite gap database

For q>k,

\[
\left\lfloor\frac{k^3}{q}\right\rfloor\le k^2-k.
\]

At K_KL,

\[
\boxed{
K_{KL}^2-K_{KL}
=34{,}092{,}151{,}333{,}005{,}523{,}140
<10^{20}.
}
\]

Therefore every lower cofactor point arising from q>k remains inside the
current Prime Gap List exhaustive range throughout the new interval.

The same B57 decomposition from Supplement 18 applies:

- q>S is forced by q^2;
- k<q<=S in the lower band is forced by Supplement 15;
- k<q<=S in the upper band is forced by the 1724 maximal-gap cap once k leaves
  the already-completely-classified prefix.

At K_KL the exact cubic horizon drift is already 114,619, far above 1724.

## 7. B63 — three-certificate full classification theorem

Take any

\[
2\le k\le5{,}838{,}848{,}460
\]

and candidate prime q<=F_3(k).

### q<=k

- If qN^2>=k^3, finite Oppermann transport forces q.
- If qN^2<k^3, B59 puts y=U/q above e^59 and B60–B61 make the
  Kadiri–Lumley interval fit entirely inside the cubic cofactor interval, so q
  is forced.

### q>k

B62 plus the existing factor-horizon / finite-gap decomposition forces q.

Thus every candidate is forced after the old explicit finite exceptions.
Combining with Supplement 17 gives the complete classification stated in
Section 1.

## 8. Certificate-language interpretation

The strongest point is not the numerical factor 2.7 increase in k range.  It is
the exact cover relation

\[
\boxed{
qN^2\ge k^3
\Rightarrow
\text{finite Oppermann certificate},
}
\]

\[
\boxed{
qN^2<k^3
\Rightarrow
U/q>N^2>e^{59}
\Rightarrow
\text{effective Kadiri–Lumley certificate}.
}
\]

The two certificate languages meet with no scale hole.

The remaining q>k region is handled by a third, orthogonal certificate language
based on factor horizon and finite prime-gap data.

So the cubic finite theorem now has the architecture

\[
\boxed{
\text{vertical square-interval certificate}
+\text{effective relative-interval certificate}
+\text{horizontal factor-gap certificate}.
}
\]

This is an explicit Prime Toolkit example in which certificate composition is
strictly stronger than any single arithmetic input.

## 9. Boundary

This supplement does not prove Oppermann's conjecture, does not reprove
Kadiri–Lumley's theorem, and does not reprove the external prime-gap
computation.

The endpoint

\[
5{,}838{,}848{,}461
\]

is not asserted to be a counterexample.  It is the first k at which the single
Kadiri–Lumley row x0=e^59, Delta=1,946,282,821 no longer fits by the uniform
relative-width inequality.

Other Kadiri–Lumley table rows or other explicit interval theorems may extend
the finite cover further.  The asymptotic cube-root knife-edge remains open.
