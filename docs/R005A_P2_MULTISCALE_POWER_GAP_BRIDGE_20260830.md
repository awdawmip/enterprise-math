# R005-A — p=2 Multiscale Power/Gap Bridge

Status: `PROVED R005 STRUCTURAL + FINITE-BOUNDARY THEOREM UNDER DECLARED EXTERNAL GAP TABLE / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-30`  
Researcher-ID: `R005A-7C2`  
Task: `RS-R005-PRIME-ALGORITHM-LAB`  
Owner generation: existing `research/r005a-prime-algorithm-lab-20260810`

## 1. Purpose

The preceding power-lift checkpoint compressed the worst cofactor scale by choosing a maximal q-power under one fixed gap envelope `(G,X)=(1724,10^20)`. That gave the uniform frontier

`K_PL = 2,263,762,760,542`.

The uniform bound loses information because the exhaustive prime-gap table is strongly scale-dependent. The only q-band that becomes dangerous after `K_PL` can be covered by lower-scale q^2 channels whose certified maximal gaps are substantially smaller than 1724.

This checkpoint consumes the current maximal-gap record table together with the exhaustive `10^20` frontier. It introduces no new external prime-gap result.

External finite data used:

1. `G1=1724`, valid for all cofactor points `x<X1=10^20` under the current exhaustive Prime Gap Searches frontier;
2. `Ga=1132`, valid for all `x<Xa`, where
   `Xa = 43,841,547,845,541,059`
   is the start of the next larger maximal gap 1184;
3. `Gb=916`, valid for all `x<Xb`, where
   `Xb = 1,686,994,940,955,803`
   is the start of the next larger maximal gap 924.

The record starts and gap sizes are in the current maximal-gap table; exhaustive analysis through `10^20` makes these finite envelopes complete in the stated ranges.

---

## 2. Exclusive-collision interval for an exponent e

For the square basin

\[
A=k^2,\qquad U=k^2+2k,
\]

an external envelope `(G,X)` forces a candidate witness q through the collision

\[
q^e r
\]

whenever

\[
\boxed{
A<Xq^e
\quad\text{and}\quad
Gq^e\le2k.
}
\]

Indeed, putting `Q=q^e`, the first inequality gives `x=A/Q<X`; the external gap envelope supplies a prime `r in (x,x+G]`; the second inequality places that prime inside `(A/Q,U/Q]`. Since `Q<=2k/G<k` for every gap envelope used here, `x>k`, hence `r>k` and the candidate support is the singleton `{q}`.

Thus exponent e and resource tier `(G,X)` force all q in the interval

\[
\boxed{
\left(\frac{A}{X}\right)^{1/e}
<q\le
\left(\frac{2k}{G}\right)^{1/e}.
}
\]

This is the multiscale power-gap covering language.

---

## 3. Global 1724 tier leaves only one middle band

Set

\[
T_1=\frac{2k}{1724},
\qquad
L_1=\frac{k^2}{10^{20}}.
\]

Assume the already-established cube-root width gate

\[
1724\,C_3\le2k,
\qquad
C_3=\lfloor U^{1/3}\rfloor.
\]

### Large q

Every cube-root-core prime

\[
q>L_1
\]

is forced with e=1 under `(1724,10^20)`.

### Small q

For

\[
q\le\sqrt{T_1},
\]

let `Q=q^e<=T_1` be the maximal q-power. Then e>=2 and maximality gives

\[
Q>T_1^{e/(e+1)}\ge T_1^{2/3}.
\]

Therefore the global tier also forces the whole small-q region as soon as

\[
T_1^{2/3}>L_1.
\]

Equivalently,

\[
1724^2 k^4<4\cdot10^{60}.
\]

This remains very far from binding at the endpoint below.

Hence, after using all admissible powers under the global tier, the only potentially uncovered q-band is

\[
\boxed{
\sqrt{T_1}<q\le L_1.
}
\]

This is much narrower than the full cube-root core.

---

## 4. Two q^2 bridge intervals

### Tier A: gap 1132

The envelope

\[
(G_a,X_a)
=
(1132,\,43,841,547,845,541,059)
\]

with e=2 forces

\[
\boxed{
\frac{k}{\sqrt{X_a}}
<q\le
\sqrt{\frac{2k}{1132}}.
}
\]

### Tier B: gap 916

The envelope

\[
(G_b,X_b)
=
(916,\,1,686,994,940,955,803)
\]

with e=2 forces

\[
\boxed{
\frac{k}{\sqrt{X_b}}
<q\le
\sqrt{\frac{2k}{916}}.
}
\]

The four intervals

1. global small-power region `q<=sqrt(T1)`;
2. Tier A q^2 interval;
3. Tier B q^2 interval;
4. global e=1 region `q>L1`;

form a continuous cover whenever the following overlaps hold:

\[
1724k<2X_a,
\]

\[
1132k<2X_b,
\]

and

\[
916k^3<2X_1^2.
\]

The first two have large positive margin throughout the range of interest. The third is the active endpoint condition.

---

## 5. Exact new endpoint

The largest integer satisfying

\[
916k^3<2\cdot10^{40}
\]

is

\[
\boxed{
K_{\mathrm{MS}}
=
2,794,976,585,489.
}
\]

Equivalently,

\[
K_{\mathrm{MS}}
=
\left\lfloor
\sqrt[3]{\frac{2\cdot10^{40}-1}{916}}
\right\rfloor.
\]

At `K_MS`, the critical real q-boundaries are approximately

- global small-power upper: `56,942.35887`;
- Tier A: `(13,348.58510, 70,271.76656]`;
- Tier B: `(68,048.92736, 78,118.94113]`;
- global e=1 lower: `78,118.94113`.

Thus the middle band is covered with positive overlap. At `K_MS+1`, the conservative Tier-B/global-e1 cubic overlap inequality fails.

The other exact margins at `K_MS` are positive:

\[
1724K_{MS}<2X_a,
\]

\[
1132K_{MS}<2X_b,
\]

and the global small-power inequality remains far from binding.

No counterexample is asserted at `K_MS+1`; only this uniform multiscale certificate stops there.

---

## 6. Extended least-basis classification

The previously established exact low/mid classification already identifies all no-least basins before the large forced-core tail. They are exactly the same 49 values:

`25, 47, 62, 123, 130, 151, 157, 162, 196, 217, 308, 364, 365, 479, 556, 888, 924, 935, 1008, 1056, 1078, 1162, 1290, 1345, 1454, 1511, 1541, 1577, 1612, 1627, 1679, 1781, 1790, 1865, 1897, 2073, 2164, 2850, 4412, 5833, 5834, 6339, 7289, 8584, 9369, 11226, 11433, 13006, 35901`.

For the large tail, the multiscale interval cover forces every cube-root-core witness. T-A20 then gives empty residual fiber and a unique least safe basis.

Therefore, under the declared exhaustive/maximal-gap finite data:

\[
\boxed{
2\le k\le2,794,976,585,489
}
\]

has no-least behavior exactly at those 49 indices.

Equivalently,

\[
\boxed{
35,902\le k\le2,794,976,585,489
\Longrightarrow
\text{unique least safe divisor-witness basis}.
}
\]

Relative to the previous power-lift endpoint `2,263,762,760,542`, this adds

\[
\boxed{531,213,824,947}
\]

additional k-indices, a `23.466%` frontier increase.

Relative to the original Campbell-based endpoint `11,661,903,789`, the certified endpoint is now about `239.6673` times as large.

---

## 7. Repair complexity

Because the failure set is unchanged and all 49 known failure basins have repair number one,

\[
\boxed{
\tau(\mathcal R_k)\le1
\quad
\text{for every }2\le k\le2,794,976,585,489.
}
\]

The first possible p=2 repair-complexity jump `tau>=2` is pushed beyond `2.7949e12` under the declared external finite computation.

---

## 8. Structural interpretation

The key object is no longer a single prime-gap bound. It is a family of resource rectangles in `(q,e)` space:

\[
A<X_iq^e,
\qquad
G_iq^e\le2k.
\]

Each finite gap tier becomes an interval in q after taking an e-th root. Different exponents and different cofactor scales can be glued to cover the entire witness core.

This is an R005-specific **multiscale resource-cover** interpretation:

`external gap table -> power channels -> q-interval cover -> forced witness core -> least-basis theorem`.

It is stronger than consuming only the single worst global gap.

---

## 9. Prior-art / tooling boundary

External/prior inputs:

- exhaustive consecutive-prime-gap computation through `10^20`;
- maximal-gap record starts and sizes;
- elementary prime-gap interval implication.

R005-specific content:

- singleton-support exclusive-collision semantics;
- exponent channels `q^e r`;
- conversion of scale-dependent gap resources into a witness-core interval cover;
- transport to least-basis and repair-complexity classification.

No historical novelty claim is made. Novelty remains `UNVERIFIED`.

Prime Toolkit disposition:

`REUSE_APPLIED / NEW R005 MULTISCALE THEOREM-LEVEL COMPRESSION / NO_NEW_TOOL_FAMILY`.

No Foundation ownership change, no Lean claim, no canonical promotion.

---

## 10. Next frontier

The active obstruction is now the exact overlap between the Tier-B q^2 channel and the global e=1 channel.

Next actions:

1. inspect whether another certified record-gap tier and/or e>=3 channel bridges the first post-`K_MS` hole;
2. use primality of q to replace continuous interval coverage by prime-only coverage where the real intervals separate narrowly;
3. formulate the interval-cover problem as a finite exact event system driven by record-gap starts and prime-power thresholds.

This is the correct next search surface; rescanning basin composites is dominated by the new resource-cover representation.
