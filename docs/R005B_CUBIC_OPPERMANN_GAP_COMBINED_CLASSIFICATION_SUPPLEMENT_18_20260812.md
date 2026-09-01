# R005-B — Cubic Oppermann × Prime-Gap Combined Full-Forcing Classification

Status: `PROVED R005 REDUCTION + TWO EXTERNAL FINITE COMPUTATION INPUTS / NOT CANONICAL`  
Date: `2026-08-12`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: R005-A T-A19; R005-B Supplements 15 and 17

## 1. Main result

The complete cubic full-forcing classification from Supplement 17 extends from

\[
2\le k\le5{,}848{,}035
\]

to

\[
\boxed{2\le k\le2{,}150{,}153{,}225}
\]

without introducing any new exceptional basin.

Under the two declared external finite-computation inputs below, the complete
non-forced candidate set is empty for every k in that range except exactly

\[
\boxed{23,64,120,138,1005,}
\]

where it remains respectively

\[
\boxed{
\{109\},\quad
\{509\},\quad
\{1303,1307\},\quad
\{1621\},\quad
\{31859\}.
}
\]

The result is a finite classification theorem.  It does not imply eventual
cubic full forcing.

## 2. External finite inputs

### 2.1 Sorenson–Webster finite Oppermann verification

Sorenson and Webster report computational verification of Oppermann's
conjecture for every index

\[
n\le 7.05\cdot10^{13}.
\]

R005-A T-A19 transports the first-half Oppermann interval to every cubic
candidate prime q<=k.  Its exact endpoint conversion gives

\[
\boxed{K_O=2{,}150{,}153{,}225.}
\]

At the endpoint,

\[
\left\lceil\sqrt{k^3/2}\right\rceil
=70{,}499{,}999{,}996{,}893,
\]

while the next k requires

\[
70{,}500{,}000{,}046{,}075.
\]

Thus every candidate q<=k is forced throughout 2<=k<=K_O.

### 2.2 Current Prime Gap List finite coverage

Supplement 15 consumes the current 2026 Prime Gap List data layer:

- exhaustive consecutive-prime-gap analysis through 10^20;
- maximal gap at most 1724 below that boundary;
- an exact Enterprise Math prefix sieve through 190,000,000 showing that the
  only gap with g^3>27a is 1327->1361, which the reciprocal carry rejects.

Therefore Supplement 15 proves:

> no cubic lower-band e=1 failure can occur when the start a of the relevant
> consecutive cofactor-prime gap is below 10^20.

## 3. B56 — q<=k / q>k split removes the old q=2 data bottleneck

Fix

\[
2\le k\le K_O
\]

and a candidate prime

\[
q\le F_3(k).
\]

### Case A — q<=k

R005-A T-A19 plus the finite Oppermann computation forces q.

### Case B — q>k

Then q>=k+1.  Put

\[
x=\frac{k^3}{q}.
\]

The exact worst cofactor coordinate satisfies

\[
\left\lfloor x\right\rfloor
\le
\left\lfloor\frac{k^3}{k+1}\right\rfloor
=
\boxed{k^2-k},
\]

because

\[
(k+1)(k^2-k+1)=k^3+1.
\]

At the endpoint K_O,

\[
\boxed{
K_O^2-K_O
=4{,}623{,}158{,}888{,}827{,}747{,}400
<10^{20}.
}
\]

So every lower-band cofactor point for every remaining q>k stays inside the
current Prime Gap List exhaustive range.

This is the decisive improvement over Supplement 15's deliberately conservative
q=2 bound k^3/2: the verified Oppermann computation removes the entire small-q
region first.

## 4. B57 — four-way forcing decomposition for q>k

Let

\[
A=k^3,\quad U=(k+1)^3-1,\quad
S=\lfloor\sqrt A\rfloor,\quad
F=\lfloor\sqrt U\rfloor.
\]

Take q>k.

### B57.1 q>S

Then q^2>A.  Since q<=F,

\[
q^2\le F^2\le U.
\]

Hence q^2 itself is a pure exclusive collision and q is forced.

### B57.2 k<q<=S and qF<=A — lower cofactor band

The cofactor point x=A/q satisfies

\[
x<k^2
\]

and in fact the exact integer bound above gives floor(x)<=k^2-k.

Since k<=K_O, every relevant consecutive cofactor-prime gap starts below
10^20.  Supplement 15 therefore supplies an e=1 exclusive cofactor certificate.

Thus every lower-band candidate q>k is forced.

### B57.3 k<q<=S and qF>A — upper horizon band

Let

\[
R=\operatorname{nextprime}(F).
\]

For the already-classified prefix k<=5,848,035, Supplement 17 is exact.

For k>=5,848,036, the factor-horizon drift alone exceeds the external maximal
gap cap 1724.  Indeed

\[
F-S
>
(k+1)^{3/2}-k^{3/2}-2
>
\frac32\sqrt{k}-2
>1724.
\]

Also F<K_O^{3/2}<10^20, so the Prime Gap List cap gives

\[
R-F\le1724.
\]

The exact upper opening threshold satisfies

\[
g_0=U/S-F\ge F-S.
\]

Therefore

\[
R-F<g_0,
\]

which is equivalent to

\[
RS\le U.
\]

Hence every q<=S satisfies qR<=U and obtains an e=1 exclusive cofactor
certificate.

Thus every upper-band candidate is forced once k leaves the already-classified
prefix.

These cases exhaust q>k.

## 5. B58 — combined classification theorem

Take any

\[
2\le k\le2{,}150{,}153{,}225.
\]

- If k<=5,848,035, Supplement 17 gives the complete truth value and candidate
  set.
- If k>=5,848,036, q<=k is forced by finite Oppermann transport, while every
  q>k is forced by B57.

Therefore no new non-forced candidate appears after the old finite prefix and
before the Oppermann endpoint.

Hence

\[
\boxed{
\operatorname{ForcedCore}_{3,k}
=
\{q\text{ prime}:q\le F_3(k)\}
}
\]

for every k in the full combined interval except exactly

\[
23,64,120,138,1005.
\]

At those five k, the complete non-forced sets are exactly the five sets stated
in Section 1.

## 6. Exact arithmetic bridge constants

The companion module/test freezes only the Enterprise Math arithmetic
conversion, not either external computation:

```text
OPPERMANN_INDEX_LIMIT = 70,500,000,000,000
COMBINED_K_MAX = 2,150,153,225
PRIME_GAP_COVERAGE_LIMIT = 10^20
PRIME_GAP_CAP = 1724
OLD_COMPLETE_PREFIX_MAX = 5,848,035
```

It checks exactly:

- the Oppermann endpoint and first excluded k;
- `floor(k^3/(k+1))=k^2-k`;
- `K_O^2-K_O<10^20`;
- the upper closing inequality at the first post-prefix k and at K_O.

No floating-point value is used as a theorem oracle.

## 7. Interpretation

The former 5.8-million endpoint was not an arithmetic phase transition.  It was
an artifact of asking the prime-gap database to cover the q=2 cofactor point.

Once R005-A's independent q<=k Oppermann certificate is composed with R005-B,
the dangerous cofactor range contracts from order k^3 to order k^2:

\[
\boxed{
q\le k\ \text{handled vertically by Oppermann};
\qquad
q>k\ \text{handled horizontally by factor/gap geometry}.
}
\]

This is a concrete example of resource composition in the Prime Toolkit: two
incomplete certificate languages cover complementary candidate coordinates and
produce a much stronger full-forcing theorem than either route alone.

## 8. Boundary

This supplement does not prove Oppermann's conjecture and does not reprove the
Prime Gap List computation.  It is conditional on those finite verified inputs.

The endpoint `2,150,153,226` is not asserted to be a counterexample.  It is the
first cubic basin beyond the selected finite Oppermann transport range.

The asymptotic cube-root prime-gap knife edge from Supplements 09–13 remains
unchanged.
