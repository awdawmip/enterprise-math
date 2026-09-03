# R005-A — p=2 bounded-deficit prime-gap shadow inversion

Status: `PROVED STRUCTURAL CONTINUATION / EXACT EXECUTABLE REDUCTION / q=78553 CATALOG-BLOCKED / NOT CANONICAL / LEAN PENDING`  
Date: `2026-09-02`  
Task: `RS-R005-PRIME-ALGORITHM-LAB`  
Track: `R005-A / p=2 least-basis frontier`  
Source repository: `awdawmip/enterprise-math`  
Source branch inspected: `research/r005a-prime-algorithm-lab-20260810`  
Source commit: `14db099861661d3a57133374c2fb3b7cfe6012ec`

## 0. Result in one paragraph

The previous exact patch certified the seven one-unit seams

\[
q\in\{78487,78497,78509,78511,78517,78539,78541\}
\]

and stopped immediately before the prime \(q=78553\), where floor widths can be
\(914\) or \(915\).  This continuation proves an exact **gap-shadow theorem**:
when the local maximal consecutive-prime gap is at most \(G\), a floor-width
\(G-d\) interval can fail only in a finite shadow of gaps of length at least
\(G-d+1\).  For \(G=916,d\le2\), the only dangerous objects are exact
916-gaps, and each such gap contributes only the two possible floors \(a\) and
\(a+1\).  The floor-square map is then inverted exactly, reducing billions of
seam events to at most two integer-square-root tests per catalogued gap.  A
fail-closed executable and exhaustive small-domain regressions are supplied.
No new frontier endpoint is claimed because the public record-gap tables found
in this round do not constitute a complete list of **all** exact 916-gaps in
the required narrow band.

## 1. Exact setting

Let

\[
I=\left(\frac{A}{Q},\frac{U}{Q}\right],\qquad
n=\left\lfloor\frac A Q\right\rfloor,
\qquad
D=\left\lfloor\frac U Q\right\rfloor-n.
\]

For the R005 p=2 seam,

\[
A=k^2,\qquad U=k^2+2k,\qquad Q=q^2.
\]

Let \(a\) be the largest prime satisfying \(a\le n\), let \(b\) be the next
prime, and write

\[
g=b-a,\qquad t=n-a.
\]

Thus \(g\) is a consecutive-prime gap and \(t\) is the offset of the floor
from its left prime endpoint.

## 2. R005A-P2-DSI1 — exact gap-shadow equivalence

### Theorem

The interval \(I\) contains no prime if and only if

\[
\boxed{g>D+t.}
\]

### Proof

Because \(a\le n<b\), the first possible prime strictly to the right of
\(A/Q\) is \(b\).  If \(b\le n+D=\lfloor U/Q\rfloor\), then
\(A/Q<b\le U/Q\), so \(b\in I\).  Conversely, if \(b>n+D\), then the integer
\(b\) is strictly larger than \(U/Q\), while no prime lies between \(a\) and
\(b\); hence \(I\) is prime-free.  Finally,

\[
b>n+D
\iff a+g>a+t+D
\iff g>D+t.
\]

This is exact and has no asymptotic or floating-point input. \(\square\)

## 3. R005A-P2-DSI2 — bounded-deficit finite shadow theorem

Assume every relevant consecutive-prime gap has length at most \(G\).  Write

\[
D=G-d,\qquad g=G-\delta,
\]

with \(d\ge1\) and \(\delta\ge0\).  DSI1 gives

\[
G-\delta>G-d+t
\iff
\boxed{t+\delta\le d-1.}
\]

Therefore a gap \((a,a+g)\) contributes precisely the finite dangerous shadow

\[
\boxed{
S_d(a,g)=
\{a+t:0\le t\le d-1-(G-g)\}
}
\]

when \(g\ge G-d+1\), and contributes nothing otherwise.

The first layers are:

| deficit \(d\) | floor width | gaps that can matter | dangerous floors |
|---:|---:|---|---|
| 1 | \(G-1\) | exact \(G\)-gap | \(a\) |
| 2 | \(G-2\) | exact \(G\)-gap | \(a,a+1\) |
| 3 | \(G-3\) | \(G\)-gap; \((G-2)\)-gap | \(a,a+1,a+2\); \(a\) |

For prime floors above 3, all nontrivial prime gaps are even.  Thus with
\(G=916\) and \(d\le2\), “gap at least 915” is exactly “gap 916” under the
known maximal-gap bound.

This theorem strictly generalizes the previous one-unit statement.  It also
specifies the correct continuation interface: a bounded-deficit seam needs a
complete catalog only of near-maximal gaps, together with their finite offset
shadows.

## 4. R005A-P2-DSI3 — exact inverse of the floor-square map

For fixed \(Q>0\) and floor target \(m\ge0\),

\[
\left\lfloor\frac{k^2}{Q}\right\rfloor=m
\]

if and only if

\[
\boxed{
\left\lceil\sqrt{mQ}\right\rceil
\le k\le
\left\lceil\sqrt{(m+1)Q}\right\rceil-1.
}
\]

In the current R005 seam, \(2k+1>Q\), so \(k\mapsto\lfloor k^2/Q\rfloor\)
is strictly increasing by at least one at each step.  Consequently every
shadow floor has at most one candidate \(k\), recovered by one exact integer
square root and one upper-bound check.

Combining DSI2 and DSI3 changes the search dimension from

\[
\text{all seam }k\text{ or all compressed }j
\]

to

\[
\text{near-maximal gap rows}\times\text{a shadow of length at most }d.
\]

The exact work is therefore

\[
O\!\left(\sum_{(a,g)}\max(0,d-(G-g))\right),
\]

apart from independent verification of the external gap catalog.

## 5. Exact floor-deficit classification in the q² seam

Put \(G=2H\) and

\[
k=HQ-s,\qquad 0<s<Q,
\qquad s^2=jQ+r,
\qquad 0\le r<Q.
\]

Then

\[
\begin{aligned}
D(k)
&=\left\lfloor\frac{k^2+2k}{Q}\right\rfloor
 -\left\lfloor\frac{k^2}{Q}\right\rfloor\\
&=G+\left\lfloor\frac{r-2s}{Q}\right\rfloor.
\end{aligned}
\]

Hence

\[
\boxed{
D(k)=G-d
\iff
(d-1)Q<2s-r\le dQ.
}
\]

Two consequences matter:

1. The previous predicate \(r<2s\) characterizes \(D=G-1\) only when the
   upper inequality \(2s-r\le Q\) is automatic.  A sufficient whole-seam
   condition is \(2s_{\max}\le Q\).
2. Once \(2s_{\max}>Q\), deficit two is possible and the one-unit executable
   must reject that seam instead of relying on its \(D=G-1\) assertion.

The supplied patch adds this missing boundary guard to
`r005a_p2_discrete_gap916_patch.cpp`.

## 6. Exact q=78553 reduction

Using

\[
P_{85}=101412319996363309069,
\qquad q=78553,
\qquad Q=q^2,
\qquad G=916,
\qquad H=458,
\]

exact integer arithmetic gives:

| quantity | exact value |
|---|---:|
| \(Q\) | 6,170,573,809 |
| \(k_g=\lceil\sqrt{P_{85}q}\rceil\) | 2,822,453,183,434 |
| \(k_w=458Q\) | 2,826,122,804,522 |
| last seam index | 2,826,122,804,521 |
| \(s_{\max}=k_w-k_g\) | 3,669,621,088 |
| safe deficit bound | \(d_{\max}=2\) |
| first cofactor floor | 1,291,005,053,866,736 |
| last cofactor floor | 1,294,364,244,470,160 |

The required gap-start band includes the one-step shadow below the first
floor:

\[
\boxed{
1291005053866735
\le a\le
1294364244470160.
}
\]

Within this band, a complete list of all consecutive gaps of length at least
916 suffices.  Under the declared maximal-gap bound \(G=916\), these are exact
916-gaps.  Each catalog row \((a,916)\) generates only the two floors
\(a,a+1\); inverse-floor filtering usually eliminates both immediately.

For orientation only, the real width first reaches 915 at

\[
\left\lceil\frac{915Q}{2}\right\rceil
=2,823,037,517,618.
\]

Thus the initial real-width-below-915 prefix has length 584,334,184, while the
remaining pre-916 tail has length 3,085,286,904.  This split does **not** say
that every index in the prefix has floor deficit two; the executable evaluates
\(D(k)\) exactly for each inverted candidate.

## 7. Executable contract and fail-closed boundary

`experiments/r005a_p2_gap_shadow_inversion.py` requires a catalog with:

- exact left-endpoint coverage of the required band;
- completeness for every gap at least the derived threshold;
- a maximal-gap bound covering the same band;
- a canonical SHA-256 of sorted `(start,gap)` rows;
- an explicit completeness attestation;
- optional deterministic verification that each supplied row has prime
  endpoints and no interior prime.

It returns one of

- `CERTIFIED_UNDER_ATTESTED_CATALOG`;
- `COUNTEREXAMPLE_FOUND` xwith exact \(k\), floor, width, gap and shadow offset;
- `FAIL_CLOSED_INCOMPLETE_OR_INVALID_CATALOG`.

The template supplied for \(q=78553\) intentionally has
`completeness_attestation=false`; the current run exits with code 3 rather
than silently treating an empty or first-occurrence-only list as complete.

## 8. Validation completed

The regression suite completed successfully:

- exhaustive floor-square inverse checks for \(Q\le79\), \(m<300\);
- 54,165 exact interval checks of DSI1;
- 1,008 exact checks of the q² deficit formula;
- a small-scale complete comparison between brute-force seam enumeration and
  gap-shadow inversion;
- exact frontier constants for \(q=78541\) and \(q=78553\);
- explicit fail-closed rejection of an unattested catalog;
- compiled C++ regression proving the old one-unit guard accepts \(q=78541\)
  and rejects \(q=78553\).

The known first 916-gap beginning at 1,189,459,969,825,483 was independently
verified by deterministic uint64 Miller-Rabin on both endpoints and every odd
interior integer.  It lies outside the \(q=78553\) band and does not supply the
missing completeness certificate.

## 9. External-data audit

The record-gap sources inspected establish the first record gap 916 at
1,189,459,969,825,483 and the next larger record gap 924 at
1,686,994,940,955,803.  This supports the local upper bound \(G=916\) below the
latter start, subject to the declared source.  It does **not** enumerate every
later repetition of gap 916.

The inspected `primegap-list-project/prime-gap-list` repository describes its
SQL as a list of known first occurrences and high-merit records.  Its schema is
keyed by gap size and record/merit status, so it is not a complete consecutive-
gap stream and cannot by itself discharge the q=78553 catalog obligation.

Accordingly:

\[
\boxed{
\text{record-gap upper bound}
\neq
\text{complete exact-916 occurrence catalog}.
}
\]

## 10. Claim discipline

Proved in this checkpoint:

- DSI1 exact gap-shadow equivalence;
- DSI2 bounded-deficit finite-shadow theorem;
- DSI3 exact floor-square inversion and singleton specialization;
- exact q=78553 reduction to an attested gap-916 catalog;
- one-unit executable boundary bug and its guard patch;
- executable fail-closed scanner and exact regressions.

Not claimed:

- no new classical theorem about the global distribution of prime gaps;
- no proof that the required q=78553 band contains no exact 916-gap;
- no extension of the certified least-basis frontier beyond
  2,822,453,183,433;
- no canonical promotion;
- no Lean formalization.

Classification:

`EXACT ENTERPRISE SPECIALIZATION / SEARCH-DIMENSION COLLAPSE / NOVELTY NOT CLAIMED`.

## 11. Next decisive action

Produce or obtain an independently auditable catalog of **all** consecutive
prime gaps \(\ge916\) with left endpoint in

\[
[1291005053866735,1294364244470160].
\]

Then run:

```bash
python3 experiments/r005a_p2_gap_shadow_inversion.py \
  --q 78553 \
  --catalog <complete-gap-catalog.json> \
  --output <result.json>
```

If the result is `CERTIFIED_UNDER_ATTESTED_CATALOG`, the whole q=78553 seam is
closed without a billions-event scan.  If it returns a counterexample, the
first exact failing \(k\) is emitted directly.
