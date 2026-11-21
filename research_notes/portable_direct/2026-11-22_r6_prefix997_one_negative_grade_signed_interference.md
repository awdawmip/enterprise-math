# PREFIX-997 — First interior signed X6 grade: exact reversal-local amplitude and interference

Date: 2026-11-22 (+08). Status: AUTHOR_ANALYTIC_LEMMA / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Independent portable research; no formal Task CLAIM, Result, or physical law.

## Frozen model

P000 V5 at `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`; native X6 affine Cell torsor with six primitive signed spatial axes. The source-defined Stage46 BRC coherent candidate `research_notes/BRC_HEARTBEAT_PORT_UPDATE_LOCALIZED_MODE_20260923_92DA92.md` has local signed amplitude `C[h,j]=1/6-1[h=j]` on 12 incoming/outgoing signed neighbour ports. The initial normalized incoming edge points from `x0-e_i` to `x0`; choose i=1 for the certificate. Each path advances one primitive signed axis, and distinct final incoming directed ports are orthogonal in the ordered BRC path-pair observer.

PREFIX-996 proves the exact mass and polynomial asymptotic of the outer grade `ell(x-x0)=n`. This note extends to its first interior grade `ell=n-2`, at update length n.

## Theorem 997.1 — One negative step and a radius-one signed weight law

At length `n>=1`, a path reaches grade `ell=n-2` **if and only if** it has exactly one negative primitive axis step.

Write that unique negative direction as `-e_r`, occurring at position s (1-indexed). All other directions are positive. Define the left-neighbour axis a as the preceding positive-step axis if s>1, and as the initial incoming axis i if s=1. Define the right-neighbour axis b as the next positive-step axis if s<n. Then the exact Stage46 signed amplitude of the complete word is

`amp(word) = 6^(-n) (-5)^{1[a=r] + 1[s<n and b=r]}`. **(1)**

In particular, the amplitude depends on the unique negative step's axis and its two immediately adjacent axis labels; the remaining positive history affects the endpoint and number of distinct words, but adds no further signed scattering factors.

**Proof.** Each native positive step increases `ell` by one, and each negative step decreases it by one. If k of n steps are negative then `ell=n-2k`; hence k=1 exactly. At every transition, the incoming neighbour label at the current Cell is the *opposite* signed direction of the preceding step, except at the initial Cell where it is `-e_i`. Stage46 multiplies the word by `(1/6)` unless outgoing direction equals the incoming neighbour label, in which case the factor is `-5/6`. Such a reversal can occur only upon entering or leaving the unique negative step: immediately before it when the positive axis equals r (or when the initial incoming axis is r for s=1), and immediately after it when the next positive axis is r. Therefore the number of reversal factors is the exponent in (1). QED.

## Theorem 997.2 — Exact observer with constructive/destructive interference

Let `F_{n,1}(k,h)` be the integer sum of weights `(-5)^b` from (1) across **all** one-negative-step named paths ending at displacement k with final incoming directed-port label h. Then

`M_{n,1}=36^(-n) sum_{k:sum k_i=n-2} sum_{h in signed-ports} F_{n,1}(k,h)^2`. **(2)**

Formula (2) is the exact full twelve-direction Stage46 candidate probability for the entire first interior grade. The path endpoint may have a negative component, because these are internal relative X6 displacements, not final encoded addresses.

The integer amplitudes can be computed without enumerating the `n*6^n` named words. Start with `A_0((0,...,0),-i,0)=1`, and for any state `(k,h,c)` with numerator A and negative-count c in {0,1}, add `A*(1-6*1[h=j])` to `(k+e_j,-j,c)` for each j in {1,...,6}; if c=0, also add `A*(1-6*1[h=-j])` to `(k-e_j,+j,1)`. Square only **after** summing all state amplitudes in a final endpoint/port fiber with c=1. This recurrence follows exactly from the primitive Stage46 operator, and produces (2) for every n by induction.

## Exact finite experiment and counterexample to incoherent-path propagation

A Python `int`-only dynamic program evaluated (2) through n=12. Independently, every one-negative signed word for n=1,...,5 was explicitly enumerated and grouped by endpoint and final port (a total of 44,790 named words). The exact coherent numerators match in all five independently covered lengths.

| n | Exact M_(n,1) | Coherent numerator over 36^n |
|---|---|---|
| 1 | 5/6 | 30 |
| 2 | 5/6 | 1080 |
| 3 | 25/432 | 2700 |
| 4 | 85/2916 | 48960 |
| 5 | 3355/186624 | 1087020 |
| 6 | 3115/279936 | 24222240 |
| 7 | 7796785/1088391168 | 561368520 |
| 8 | 3945025/816293376 | 13634006400 |
| 9 | 1068458915/313456656384 | 346180688460 |
| 10 | 31737102665/12694994583552 | 9140285567520 |
| 11 | 1155012928645/609359740010496 | see checker/certificate |
| 12 | 675290647405/457019805007872 | see checker/certificate |

The n=3 boundary gives a decisive finite observer contrast: adding the squared weight of each **individual** one-negative path, rather than coherently summing paths sharing endpoint and terminal incoming port, gives numerator **11,880**, whereas (2) gives **2,700**. Thus the incoherent positive-path-mass surrogate exaggerates this declared grade probability by exactly `11880/2700=22/5`. Conversely at n=5 the incoherent diagonal numerator is 816,480 while coherent (2) is 1,087,020; cancellation and enhancement both occur. These values distinguish a signed path-pair BRC observer from a positive-weight-only propagation.

The formula (1) and recurrence are exact for all n; the reported integer evaluations are finite up to n=12. No asymptotic for this inner grade, interacting occupancy closure, or native physical calibration is asserted.

## Source, validation, next

Checker: `research_notes/portable_direct/PREFIX997_R6_SINGLE_NEGATIVE_GRADE_CHECK.py`, exact certificate `PREFIX997_R6_EXACT_RESULTS.json` or local reproduction bundle. Independent word checks enumerate 6, 72, 648, 5184 and 38880 words at lengths 1,...,5. All 12 finite DP fractions are exact.

Next ask whether `M_{n,1}` admits an explicit asymptotic expansion relative to the outer boundary `M_n ~ 9/(8*pi^(5/2)) n^(-5/2)`, and determine how genuine X6 Link/Port occupancy or triadic field data modifies the radius-one signed source law. Mother target `B_fix,odd(32) in {19,20}` remains unresolved. Historical researcher `EM-DIRECT-FBEA5D` identifies provenance only, not an authenticated present execution identity.
