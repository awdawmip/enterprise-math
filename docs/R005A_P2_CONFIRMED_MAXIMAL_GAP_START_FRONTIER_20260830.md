# R005-A — p=2 Confirmed Maximal-Gap-Start Frontier

Status: `PROVED R005 FINITE-BOUNDARY STRENGTHENING UNDER DECLARED CONFIRMED MAXIMAL-GAP TABLE / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-30`  
Researcher-ID: `R005A-7C2`  
Task: `RS-R005-PRIME-ALGORITHM-LAB`  
Owner generation: existing `research/r005a-prime-algorithm-lab-20260810`

## 1. Correction to the global 1724 resource endpoint

The preceding multiscale checkpoint used

\[
(G_1,X_1)=(1724,10^{20})
\]

because Prime Gap Searches has exhaustively analyzed consecutive-prime gaps through `10^20`.

The confirmed maximal-gap record table gives a slightly stronger exact resource boundary. Its consecutive confirmed records include

\[
1724\text{ after }P_{84}=68,068,810,283,234,182,907,
\]

followed by the next larger confirmed maximal gap

\[
1854\text{ after }P_{85}=101,412,319,996,363,309,069.
\]

By the meaning of a confirmed maximal/rising-gap record, no consecutive-prime gap with left endpoint below `P85` exceeds 1724. Hence the finite operational statement used by R005 can be sharpened to

\[
\boxed{
\forall x<P_{85},\quad
\exists\text{ prime }r\in(x,x+1724].
}
\]

This does not claim a new prime-gap theorem. It consumes the confirmed record table as external computation.

The older `X_1=10^20` statement remains valid but is no longer the tight active boundary.

---

## 2. Existing multiscale bridge, with the corrected global frontier

Reuse the already-proved p=2 multiscale power-gap cover:

- global tier: `(G1,X1)=(1724,P85)` with arbitrary admissible powers and e=1 on the large-q side;
- Tier A: `(Ga,Xa)=(1132,43,841,547,845,541,059)` with e=2;
- Tier B: `(Gb,Xb)=(916,1,686,994,940,955,803)` with e=2.

The Tier A and Tier B resource endpoints are themselves the starts of the next larger confirmed maximal gaps 1184 and 924 respectively.

For

\[
A=k^2,
\qquad
C_3=\lfloor(k^2+2k)^{1/3}\rfloor,
\]

the four q-regions cover the complete cube-root witness core once the exact overlap conditions hold:

\[
1724C_3\le2k,
\]

\[
1724^2k^4<4P_{85}^3,
\]

\[
1724k<2X_a,
\]

\[
1132k<2X_b,
\]

and

\[
916k^3<2P_{85}^2.
\]

The last inequality is the active upper-bound constraint in the current range.

---

## 3. Exact strengthened endpoint

The exact largest integer satisfying

\[
916k^3<2P_{85}^2
\]

is

\[
\boxed{
K_{85}=2,821,231,035,570.
}
\]

Equivalently,

\[
K_{85}
=
\left\lfloor
\sqrt[3]{\frac{2P_{85}^2-1}{916}}
\right\rfloor.
\]

At `K85` the exact endpoint margin is positive:

\[
2P_{85}^2-916K_{85}^3
=
14,796,448,080,275,505,124,516,505,522.
\]

At the next integer the sign reverses:

\[
916(K_{85}+1)^3-2P_{85}^2
=
7,075,830,759,794,401,033,527,266,954.
\]

The other bridge inequalities retain positive margin at `K85`.

For orientation, the real q-boundaries at the endpoint are approximately

\[
\sqrt{2k/1724}=57,209.1761,
\]

\[
k^2/P_{85}=78,484.9864,
\]

Tier A:

\[
(13,473.9743,70,601.0420],
\]

Tier B:

\[
(68,688.1410,78,484.9864].
\]

Thus the middle band remains continuously covered, with the Tier-B upper edge just beyond the global e=1 lower edge.

No counterexample is asserted at `K85+1`; only this continuous real-interval certificate stops there.

---

## 4. Strengthened p=2 classification

The exact low/mid computation remains unchanged. The only no-least square basins are the same 49 indices:

`25, 47, 62, 123, 130, 151, 157, 162, 196, 217, 308, 364, 365, 479, 556, 888, 924, 935, 1008, 1056, 1078, 1162, 1290, 1345, 1454, 1511, 1541, 1577, 1612, 1627, 1679, 1781, 1790, 1865, 1897, 2073, 2164, 2850, 4412, 5833, 5834, 6339, 7289, 8584, 9369, 11226, 11433, 13006, 35901`.

On the large tail, the corrected multiscale bridge forces every cube-root-core witness. By T-A20 the residual fiber is empty.

Therefore, under the declared confirmed maximal-gap table:

\[
\boxed{
2\le k\le2,821,231,035,570
}
\]

has no-least behavior exactly at those same 49 indices.

Equivalently,

\[
\boxed{
35,902\le k\le2,821,231,035,570
\Longrightarrow
\text{unique least safe divisor-witness basis}.
}
\]

Relative to the immediately preceding multiscale endpoint

\[
2,794,976,585,489,
\]

this adds

\[
\boxed{26,254,450,081}
\]

additional k-indices, an additional `0.939344%`.

Relative to the original Campbell-based endpoint `11,661,903,789`, the current certified endpoint is about `241.9186` times as large.

---

## 5. Repair complexity

The failure set is unchanged and all 49 failure basins have transversal number one. Every other basin in the certified interval has empty residual hypergraph.

Hence

\[
\boxed{
\tau(\mathcal R_k)\le1
\quad
\text{for every }2\le k\le2,821,231,035,570.
}
\]

The first possible p=2 repair-complexity jump `tau>=2` is therefore beyond `K85` under the declared external finite computation.

---

## 6. Status / provenance boundary

External input:

- the current confirmed maximal/rising prime-gap table and its record starts;
- exhaustive computation underlying those confirmed records.

R005 content:

- exclusive-collision witness semantics;
- power channels `q^e r`;
- the multiscale q-interval cover;
- transport from the confirmed gap-resource frontier to cube-root-core forcing and least-basis classification.

No Prime Toolkit status change, no new tool family, no Foundation promotion, no Lean claim, and no historical novelty claim.

Classification:

`REUSE_APPLIED / CONFIRMED_MAXIMAL_GAP_FRONTIER_STRENGTHENING / NOT CANONICAL / LEAN PENDING`.

---

## 7. Next exact frontier

The continuous real-interval bridge fails first at the Tier-B/global-e1 seam after `K85`.

But q is required to be prime, not an arbitrary real coordinate. Therefore the next exact question is sharper:

> when the real intervals separate, is there actually a prime q in the uncovered strip?

The next search should compute the first prime-only uncovered witness event and test it against all available exponent/tier channels before declaring a new finite endpoint.
