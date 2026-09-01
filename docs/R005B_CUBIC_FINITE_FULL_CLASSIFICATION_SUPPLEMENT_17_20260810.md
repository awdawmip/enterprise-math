# R005-B — Complete Cubic Full-Forcing Classification through k=5,848,035

Status: `PROVED R005 REDUCTION + EXACT FINITE CERTIFICATE + EXTERNAL PRIME-GAP DATA / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Supplements 06, 15, 16

## 1. Main result

The finite full-forcing band from Supplement 16 can be sharpened from a coarse
uniform-gap certificate into a complete classification.

Under the same declared external prime-gap data used in Supplements 15–16:

\[
\boxed{
2\le k\le5{,}848{,}035
}
\]

has full cubic candidate forcing at **every** k except

\[
\boxed{
23,\ 64,\ 120,\ 138,\ 1005.
}
\]

The exact non-forced candidate sets are:

\[
\boxed{
\begin{array}{c|c}
k&\text{non-forced candidate primes}\\
\hline
23&\{109\}\\
64&\{509\}\\
120&\{1303,1307\}\\
138&\{1621\}\\
1005&\{31859\}
\end{array}
}
\]

Thus, conditional on the stated finite external prime-gap computations,

\[
\boxed{
\operatorname{ForcedCore}_{3,k}
=\{q\text{ prime}:q\le F_3(k)\}
}
\]

for every

\[
2\le k\le5{,}848{,}035
\]

outside those five explicit basins.

This is stronger than merely exhibiting a long saturation interval: it
classifies the complete full-forcing truth value and complete non-forced
candidate set on the entire certified prefix.

The endpoint `5,848,036` is not asserted to be a counterexample; it is simply the
first k whose q=2 cofactor reach leaves the selected current `10^20` external
exhaustive range.

---

## 2. Lower band is already completely closed

Supplement 15 proves that for every

\[
2\le k\le5{,}848{,}035
\]

and every candidate prime q satisfying

\[
qF_3(k)\le k^3,
\]

q has an e=1 exclusive cofactor certificate.

Therefore **no exception in the present classification can come from the lower
cofactor band**.

All finite exceptions must lie in the upper band

\[
qF_3(k)>k^3.
\]

For p=3, Supplements 04 and 06 already give an exact characterization of upper
non-forcing via the prime slice / boundary-prime criterion.

---

## 3. B53 — scale-dependent maximal-gap cap

Supplement 16 used the uniform cap 1328 everywhere, which was deliberately
simple but extremely wasteful at small factor horizons.

The current Prime Gap List maximal-gap table gives a much smaller scale-dependent
cap.  For example, the confirmed record staircase begins

\[
\begin{array}{c|c}
\text{record start}&\text{maximal gap}\
\hline
1327&34\\
9551&36\\
15683&44\\
19609&52\\
31397&72\\
155921&86\\
360653&96\\
370261&112\\
492113&114\\
1349533&118\\
1357201&132\\
2010733&148\\
4652353&154\\
17051707&180\\
20831323&210\\
47326693&220\\
122164747&222\\
189695659&234\\
191912783&248\\
387096133&250\\
436273009&282\\
1294268491&288\\
1453168141&292\\
2300942549&320\\
3842610773&336\\
4302407359&354\\
10726904659&382\\
20678048297&384
\end{array}
\]

Only records through 10,726,904,659 are needed at the final basin endpoint,
because

\[
F_3(5{,}848{,}035)=14{,}142{,}137{,}522
<20{,}678{,}048{,}297,
\]

the start of the next record gap 384.

For any factor horizon F, let

\[
G_{\max}(F)
\]

be the current confirmed maximal-gap staircase value whose record start is the
largest one not exceeding F.

The upper-closing certificate is then

\[
\boxed{
(F+G_{\max}(F))S\le U.
}
\]

An exact integer scan through the complete finite prefix finds

\[
\boxed{
\text{last k not closed by this scale-dependent cap}=5501.
}
\]

Thus **every upper band at k>=5502 is automatically forced** by the external
record-gap staircase, without needing actual prime enumeration at each k.

---

## 4. B54 — exact direct classification below k=5502

Once the record-cap scan reduces the unresolved prefix to

\[
k\le5501,
\]

the largest factor horizon is only

\[
F_3(5501)=408113.
\]

A direct exact Eratosthenes sieve slightly beyond that value is therefore tiny.

For each k define:

\[
S_k=\lfloor\sqrt{k^3}\rfloor,
\qquad
F_k=F_3(k),
\]

\[
Q_k=\max\{q\le S_k:q\text{ prime}\},
\]

and

\[
R_k=\min\{r>F_k:r\text{ prime}\}.
\]

Supplement 06 gives

\[
\boxed{
\text{upper non-forcing exists}
\iff
Q_kF_k>k^3
\quad\text{and}\quad
Q_kR_k>(k+1)^3-1.
}
\]

When this holds, the complete non-forced prime slice is

\[
\boxed{
\max\left(
\left\lfloor\frac{k^3}{F_k}\right\rfloor,
\left\lfloor\frac{(k+1)^3-1}{R_k}\right\rfloor
\right)
<q\le S_k.
}
\]

The direct scan through k=5501 finds exactly five exceptional basins and no
others:

\[
23,64,120,138,1005.
\]

The corresponding complete prime slices are exactly the five rows in the main
table.

This independently recovers all previously discovered small cubic upper
exceptions; none were inserted by hand into the search.

---

## 5. B55 — complete finite-prefix classification theorem

Let

\[
2\le k\le5{,}848{,}035.
\]

Take any candidate prime

\[
q\le F_3(k).
\]

### If q is in the lower band

Supplement 15 forces q by e=1.

### If q is in the upper band and k>=5502

The current maximal-gap staircase satisfies the exact upper-closing inequality,
so Supplement 16 forces q by either q^2 or qR.

### If q is in the upper band and k<=5501

The direct prime sieve gives the exact upper non-forced slice.  It is empty
except at the five stated k, where it is exactly the stated candidate set.

Therefore no other non-forced candidate exists anywhere in the certified prefix.
∎

---

## 6. Reproducible certificate

The companion artifact

`experiments/r005b_cubic_finite_full_classification.py`

contains:

1. the frozen confirmed maximal-gap staircase needed through the endpoint
   factor horizon;
2. a standard-library Eratosthenes direct upper scan through k=5501;
3. the record-cap upper scan through k=5,848,035.

Frozen command:

```text
python experiments/r005b_cubic_finite_full_classification.py --k-limit 5848035 --direct-limit 5501 --assert-current-certificate
```

asserts:

```text
endpoint_factor_horizon = 14,142,137,522
last_record_cap_uncertified_k = 5,501
exceptions = {
  23: [109],
  64: [509],
  120: [1303,1307],
  138: [1621],
  1005: [31859]
}
```

No floating-point arithmetic is used.

A separate unit regression independently reconstructs the complete exception
set through k=1100 from a fresh prime sieve, locking all five known exceptions
without consuming the hard-coded external record-gap staircase.

---

## 7. What changed conceptually

The finite cubic picture is now much sharper than the asymptotic statement
alone suggests.

Asymptotically, p=3 still sits on the difficult cube-root prime-gap knife edge:
current theory does not decide eventual full forcing.

But on the complete verified prefix through 5.8 million:

\[
\boxed{
\text{lower mechanism never fails, and upper failure occurs at only five k.}
}

This is an extreme finite sparsity pattern:

\[
\boxed{
5\text{ exceptional basins among }5{,}848{,}034\text{ tested k values}.
}

This finite ratio is **not** used as probabilistic or asymptotic evidence.  It
is simply the exact finite classification count.

The mathematically important point is that the same structural phase laws make
this classification cheap:

- lower failures are reduced to cube-root-supercritical cofactor gaps;
- upper failures are reduced to the scale-dependent maximal-gap staircase;
- only the tiny residual prefix requires literal prime enumeration.

---

## 8. Relation to the normalized order parameter

The five finite exceptions occur in the upper mechanism.  They do not contradict
Supplement 10's conditional limsup phase law.

The current classification reinforces the architecture:

\[
\text{finite data regime}
\to
\text{almost complete saturation with five explicit upper exceptions},
\]

while

\[
\text{asymptotic regime}
\to
\text{critical dependence on normalized prime gaps near constants }3/2,3.
\]

Finite saturation cannot by itself settle the limsup problem, and the limsup
problem is not needed to classify a large verified prefix.

---

## 9. External-data boundary

The maximal-gap staircase is external computational number theory.  Its current
values are taken from the Prime Gap List project's confirmed record-gap table,
whose exhaustive-analysis page reports coverage through `10^20` in 2026.

The lower-band closure separately consumes the current `1724 / 10^20` data
layer documented in Supplement 15.

R005-B does not reprove those external computations.  It proves the reduction
showing exactly how much of the external data is sufficient, and supplies
reproducible internal integer compilers for the remaining finite checks.

No canonical or Lean-checked status is claimed.
