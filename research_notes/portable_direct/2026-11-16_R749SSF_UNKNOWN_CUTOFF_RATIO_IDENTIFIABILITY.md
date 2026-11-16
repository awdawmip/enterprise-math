# R749SSF — Unknown-cutoff exact identifiability from one raw marked-source ratio

**Date:** 2026-11-16 (Asia/Shanghai). **Status:** \`AUTHOR_EXACT_NOT_REVIEWED\`. **Mode:** independent portable auxiliary-source research; no shared task CLAIM. **Frozen auxiliary scientific input:** \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. **Direct predecessor:** R749SSE, immutable commit \`2ca2b25cb64b121748499edcd61eb90cb99faad8\`, paper \`research_notes/portable_direct/2026-11-16_R749SSE_RESTRICTED_FUTURE_OBSERVER_CARRIER.md\`. This uses the same labeled-source population and integer error budgets, while changing the observation interface from smooth-subtracted \`Y_q\` to the **raw rational marked-count ratio**. The original \`Y_q\`-only unknown-cutoff question remains open.

## Model and problem

Fix five distinct source labels with weights \`w=(1,1,2,3,6)\`, marking source 1. For each integer cutoff \`q≥1\`, define

\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:\ k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\qquad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]

Allow independent integer errors \`e,d∈{-2,-1,0,1,2}\` with positive denominator. The observer sees a single **exact rational number**

\[
X(q,e,d)=\frac{T_q+e}{C_q+d},
\]

but knows neither the integer \`q\` nor either error. The source model, budgets and the fact \`q≥6\` are known. The claim concerns exact rational identifiability, not rounded real measurements.

## Theorem: the sharp cutoff 6 also works without knowing q

The map

\[
\boxed{(q,e,d)\longmapsto X(q,e,d)}
\]

is injective for integer \`q≥6\`, \`-2≤e,d≤2\`. This cutoff is sharp: at \`q=5\`, \`C_5=T_5=25\`, and the distinct pairs \`(-2,-2)\`, \`(-1,-1)\` both yield \`X=1\`.

Thus one exact raw ratio determines \`q\` and both integer errors.

### 1. Disjoint interval envelopes for q≥7

For \`q≥6\`, since \`C_q>2\` and \`T_q≥2\`, all raw ratios lie in

\[
I_q=\left[\frac{T_q-2}{C_q+2},\frac{T_q+2}{C_q-2}\right].
\]

The gap between consecutive intervals is positive exactly when

\[
G(q)=(T_{q+1}-2)(C_q-2)-(T_q+2)(C_{q+1}+2)>0.
\]

The exact count recurrence gives \`G(6)=-13\` and \`G(q)>0\` for each integer \`7≤q≤35\`.

For the entire infinite tail, the exact generating functions are

\[
\sum_{q\ge1}C_qz^{q-1}=
\frac1{(1-z)^3(1-z^2)(1-z^3)(1-z^6)}
\]

and

\[
\sum_{q\ge1}T_qz^{q-1}=
\frac{z}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

Upon conversion to denominators \`(1-z^6)^6\` and \`(1-z^6)^7\`, their integer numerator polynomials have degrees at most 22 and 28. Consequently for \`q≥36\`, on each fixed residue class modulo 6, \`C_q\` is an exact polynomial of degree at most 5 and \`T_q\` of degree at most 6 in \`q\`. The nominal degree-11 terms cancel in \`T_{q+1}C_q-T_qC_{q+1}\`; thus \`G(q)\` has degree at most 10 on each residue class.

For each base \`b∈{36,37,38,39,40,41}\` and \`j≥0\`, use the Newton expansion

\[
G(b+6j)=\sum_{i=0}^{10}a_{b,i}{j\choose i},\qquad a_{b,i}=\Delta_6^iG(b).
\]

The attached exact-integer certificate computes all 66 coefficients. **All are strictly positive**; the minimum is 1,959,552 (the common tenth difference). Since the binomial coefficients are nonnegative for integer \`j≥0\`, \`G(q)>0\` for every \`q≥36\`. Together with the finite range, the envelopes \`I_q\` for all \`q≥7\` are strictly ordered and pairwise disjoint.

### 2. The exceptional q=6,7 overlap has no actual rational collision

Exact counts:

\[
(C_5,T_5)=(25,25),\ (C_6,T_6)=(41,50),\
(C_7,T_7)=(65,91),\ (C_8,T_8)=(98,156).
\]

For the 25 discrete rational values at \`q=6\`, the largest is \`4/3\` and second largest \`17/13\`. At \`q=7\`, the smallest is \`89/67\` and second smallest \`90/67\`. Cross multiplication proves

\[
\frac{17}{13}<\frac{89}{67}<\frac43<\frac{90}{67}.
\]

Hence these discrete sets are disjoint even though their continuous interval envelopes overlap. At \`q=8\` the lower interval endpoint is \`77/50>4/3\`, so all higher-\`q\` sets also avoid the \`q=6\` values.

### 3. Within-q error identifiability

R749SSE Theorems 1–2 establish injectivity of \`(e,d)\mapsto(T_q+e)/(C_q+d)\` for each fixed \`q≥6\`. The current certificate independently checks all 25 values at \`6≤q≤47\`; for \`q≥48\`, the exact 216-residue stars-and-bars argument proves \`T_q≥5C_q>4(C_q+2)\`, which gives the injectivity criterion by cross multiplication. The previous two parts determine \`q\`; fixed-\`q\` injectivity determines \`e,d\`. This proves the theorem. \`□\`

## Corollary: unknown-base restricted-future carrier

Let \`r≥6\` also be unknown. For offsets \`h=(0,1,5)\`, let any nonempty indexed \`S⊆{0,1,2}\` produce the tuple \`(X(r+h_i,e_i,d_i))_{i∈S}\`. A single selected coordinate identifies \`r+h_i\` and therefore \`r\`, as well as both selected errors. The full tuple identifies all selected errors.

Assume numerator and denominator errors each are constant on blocks of independently selected partitions \`π_e,π_d\` of \`{0,1,2}\`, with a free integer value in \`[-2,2]\` on every block. The numerical tuple sets (also unioned over unknown \`r≥6\`) agree between two partition pairs **if and only if** their respective equality relations restricted to \`S\` agree. Indeed, each numerical tuple uniquely identifies \`r\` and all its selected errors, so two different assignment sets cannot be equated by selecting different cutoff values. The exact minimal numbers of equivalence classes remain \`1\` for 0 or 1 selected index, \`4\` for 2 indices and \`25\` for all 3—under this raw-ratio observation interface.

This quotient is relative to the declared future observation horizon. Source labels, the selected offsets and numerator/denominator equality relations remain part of its typed provenance.

## Reproducibility, evidence boundary, next problem

\`R749SSF_UNKNOWN_CUTOFF_RATIO_CERT.py\` computes source counts by dynamic programming and an independent 216-residue formula for \`1≤q≤320\`; checks known-cutoff injectivity \`6≤q≤47\`; verifies all integer gaps \`7≤q≤35\`; derives all six eleven-coefficient positive Newton certificates for bases \`36..41\` and checks them at four independent sample indices. Its exact-arithmetic result file is \`R749SSF_UNKNOWN_CUTOFF_RATIO_RESULTS.json\` with status \`PASS\`.

For the predecessor's original smooth-subtracted observer

\[
Y_q(e,d)=q^3X(q,e,d)-q^4\left(\frac16+\frac1{2q}-\frac{115}{36q^2}+\frac{115}{6q^3}-\frac{16315}{108q^4}\right),
\]

the code additionally checks every one of the 7,375 triples \`(q,e,d)\` with \`6≤q≤300\`; no two give an equal exact rational \`Y\` in this finite range. The **infinite unknown-\`q\` question for \`Y\` remains open**, as does the noise tolerance of raw-ratio cutoff recovery.

The five-weight model is a frozen auxiliary labeled-source observer. No claim of a native signed BRC-port map or Heartbeat World/X6 time interpretation is made. A native transfer needs an explicit label/branch-preserving map and observer-safe future update law under P000. Mathematical status is \`AUTHOR_EXACT_NOT_REVIEWED\`.
