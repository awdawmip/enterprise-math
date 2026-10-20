# R005-B — Certified Cubic Full-Forcing Band from Finite Gap Caps

Status: `PROVED R005 REDUCTION + EXACT FINITE CERTIFICATE + EXTERNAL COMPUTATION TRANSFER / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Supplements 06, 07, 15

## 1. Main result

Supplement 15 closes the complete **lower cofactor band**

\[
qF_3(k)\le k^3
\]

through

\[
\boxed{k\le5{,}848{,}035}
\]

under the current 2026 Prime Gap List external data.

The remaining question on that finite range is the upper band

\[
qF_3(k)>k^3.
\]

For the upper side we can consume a stronger but smaller-range external gap cap
already present in the R005-A evidence chain:

\[
\boxed{g\le1328\quad\text{below the selected }4\cdot10^{17}\text{ region}.}
\]

The factor horizons in the entire k-range above are only of order \(10^{10}\),
so this older 1328 cap is more than sufficient for the upper side.

An exact integer scan of the upper closing condition finds

\[
\boxed{
\text{last }k\le5{,}848{,}035
\text{ not automatically closed by the 1328 cap}
=783{,}190.
}
\]

Therefore:

\[
\boxed{
783{,}191\le k\le5{,}848{,}035
\Longrightarrow
\operatorname{ForcedCore}_{3,k}
=\{q\text{ prime}:q\le F_3(k)\}.
}
\]

In words:

> **every candidate divisor witness is forced throughout the entire certified
> band 783,191 through 5,848,035.**

This is a genuine finite **full-forcing saturation** theorem, not merely a
least-basis theorem and not merely a lower-core theorem.

The lower endpoint 783,191 is the sharp endpoint of this selected **uniform
1328-gap-cap certificate**, not a claim that 783,190 is an actual full-forcing
counterexample or that no earlier full-forcing interval exists.

---

## 2. B50 — cubic upper candidates split into two explicit certificate forms

Fix one cubic basin and write

\[
A=k^3,
\qquad
U=(k+1)^3-1,
\qquad
F=F_3(k),
\qquad
S=\lfloor\sqrt A\rfloor.
\]

Take an upper-band candidate prime

\[
\boxed{qF>A.}
\]

There are two cases.

### Case I — q^2>A

Since q<=F,

\[
A<q^2\le F^2\le U.
\]

Thus

\[
\boxed{q^2}
\]

lies in the basin and its candidate-prime support is the singleton `{q}`.
So q is forced without any prime-gap input.

### Case II — q^2<=A

Then

\[
q\le S.
\]

Also qF>A, so for any prime R>F,

\[
qR>A.
\]

If an external uniform prime-gap bound gives

\[
R-F\le G,
\]

then

\[
R\le F+G.
\]

Therefore the sufficient basin-upper condition for **every** such q is

\[
\boxed{
S(F+G)\le U.
}
\]

Indeed then

\[
qR\le S(F+G)\le U,
\]

and qR is an e=1 singleton-support certificate because R>F.

Hence:

\[
\boxed{
S(F+G)\le U
\Longrightarrow
\text{every cubic upper-band candidate is forced}.
}
\]

This is exactly the complement of the upper-window opening condition from
Supplement 05.

---

## 3. B51 — exact selected-gap-cap closing predicate

For a declared gap cap G define

\[
\boxed{
\operatorname{UpperClosed}_G(k)
\iff
(F_3(k)+G)\,\lfloor\sqrt{k^3}\rfloor
\le
(k+1)^3-1.
}
\]

This predicate is integer exact.

It should **not** be assumed monotone from its real asymptotic form.  The factor
horizon and lower square root carry integer teeth; adjacent k can occasionally
move the rational threshold in the opposite direction.

Accordingly the finite boundary is certified by direct integer scan rather than
by assuming monotonicity.

The companion experiment

`experiments/r005b_cubic_full_forcing_band.py`

scans the complete selected range.

Frozen command:

```text
python experiments/r005b_cubic_full_forcing_band.py --k-limit 5848035 --upper-gap-cap 1328 --assert-current-certificate
```

returns

```text
last_k_not_closed_by_cap = 783190
certified_upper_closed_start = 783191
certified_full_band_if_lower_closed_through_k_limit = [783191,5848035]
```

No floating-point arithmetic is used.

---

## 4. Why the 1328 cap is valid for the upper side of the whole band

The R005-A external evidence layer already records the conservative premise that
consecutive-prime gaps in the selected double-checked region below

\[
4\cdot10^{17}
\]

are at most 1328.

At the upper endpoint of the new band,

\[
k=5{,}848{,}035,
\]

the factor horizon is only

\[
\boxed{F_3(k)=14{,}142{,}137{,}522.}
\]

Thus the entire post-horizon prime search used in B50 lies vastly inside the
older external range.

So it is legitimate to use:

- the **current 2026 1724 / 10^20** external layer for the far larger lower
  cofactor points `k^3/q`;
- the **older stronger 1328 / 4e17** layer for the much smaller upper factor
  horizon.

This mixed-source finite theorem does not silently upgrade or replace either
external premise; it uses each where it is strongest and already applicable.

---

## 5. B52 — lower/upper assembly theorem

Let

\[
783{,}191\le k\le5{,}848{,}035.
\]

Take any candidate prime

\[
q\le F_3(k).
\]

### Lower band

If

\[
qF_3(k)\le k^3,
\]

Supplement 15 gives an e=1 exclusive cofactor certificate under the current
finite prime-gap data.

Therefore q is forced.

### Upper band

If

\[
qF_3(k)>k^3,
\]

B50 applies.  The exact finite scan proves

\[
(F_3(k)+1328)S_3(k)\le U_k
\]

throughout the entire stated interval.

Therefore q is forced either by q^2 or by qR with R the first prime beyond F.

Since the lower and upper bands partition every candidate prime,

\[
\boxed{
\operatorname{ForcedCore}_{3,k}
=\{q\text{ prime}:q\le F_3(k)\}.
}

This proves full forcing saturation on the entire finite band. ∎

---

## 6. Relation to earlier cubic results

The project now has several logically different finite p=3 statements.

### Prime anchor

External consecutive-cubes computation supplies actual primes in cube basins on
a vastly larger finite range.

### Unique least basis

R005-A cubic-core + finite Oppermann transport proves a unique least divisor-
witness basis through

\[
2{,}150{,}153{,}225.
\]

This requires only a much smaller forced core `q<=k`.

### Full forcing

The present result proves the strictly stronger statement

\[
\boxed{
\text{every candidate }q\le F_3(k)\text{ is mandatory}
}
\]

on the finite interval

\[
\boxed{783{,}191\le k\le5{,}848{,}035.}
\]

These are not contradictory frontiers because they answer different witness-
language questions.

The small explicit cubic non-forcing examples at k=23,64,120,138,1005 also
remain valid.  Therefore the present theorem is a **finite saturation band**,
not a theorem that p=3 is globally or eventually saturated.

---

## 7. Conservative full-forcing sub-band from the older evidence layer alone

If one refuses the current `10^20 / 1724` extension and uses only the older
R005-A conservative prime-gap premise, Supplement 15 closes the lower side only
through

\[
k\le928{,}317.
\]

The same exact upper scan with G=1328 gives

\[
\boxed{
\text{last upper-cap-uncertified k in that range}=783{,}190.
}
\]

Therefore the older evidence layer alone already certifies

\[
\boxed{
783{,}191\le k\le928{,}317
}
\]

as a full-forcing band.

The current 2026 external extension enlarges only the **right endpoint** to
5,848,035; the left endpoint is unchanged because it is controlled by the
stronger 1328 upper-gap cap.

---

## 8. Why this matters for the asymptotic phase picture

The cubic phase now has both an asymptotic and a large finite realization.

Asymptotically, Supplements 08–14 say:

- lower PRE critical constant: 3;
- upper opening constant: 3/2;
- upper saturation constant: 3;
- supercritical lower gaps amplify failures;
- the unresolved knife edge is tied to cube-root-scale prime gaps.

Finitely, the actual verified gap caps are already small enough that both
mechanisms simultaneously disappear on a multi-million-k band.

So the phase diagram is not merely qualitative.  The same constants and exact
integer carries can be used as a certificate compiler against real prime-gap
data.

---

## 9. Status and ownership boundary

The full-forcing assembly is internal R005 mathematics conditional on the stated
external finite prime-gap premises.

The external prime-gap computations remain prior computation and are not
reproved here.  The upper `1328 / 4e17` premise is consumed from the existing
R005-A evidence record; the lower `1724 / 1e20` extension is documented in
Supplement 15.

Generic forced-core / least-basis semantics remain R005-A/A2/A4 ownership.
R005-B owns the factor-horizon partition, upper certificate compiler, finite
integer scans, and lower/upper assembly.

No canonical or Lean-checked claim is made.  No conclusion is drawn for
k=5,848,036 or for k<783,191 not already covered by separate exact evidence.
