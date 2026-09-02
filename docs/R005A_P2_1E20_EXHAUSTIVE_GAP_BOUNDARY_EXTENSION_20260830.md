# R005-A — p=2 Exhaustive Prime-Gap Frontier Extension to 10^20

Status: `PROVED R005 FINITE-BOUNDARY EXTENSION UNDER DECLARED EXTERNAL COMPUTATION / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-30`  
Researcher-ID: `R005A-7C2`  
Task: `RS-R005-PRIME-ALGORITHM-LAB`  
Owner generation: existing `research/r005a-prime-algorithm-lab-20260810`

## 1. Purpose

The current R005-A p=2 finite classification uses Peter J. Campbell's operational consequence

`every real x < 6.8e19 has a prime in (x, x+1724]`

to force the fourth-root and cube-root witness cores up to

`k = 11,661,903,789`.

That boundary is no longer the strongest declared finite computational input available in August 2026.

The Prime Gap List / Prime Gap Searches project reports that **all consecutive-prime gaps with left endpoint below `10^20` were exhaustively analyzed by 8 May 2026**. The current maximal-gap table records:

- gap `1724` after prime `68,068,810,283,234,182,907`;
- the next larger maximal gap, `1854`, only after prime `101,412,319,996,363,309,069 > 10^20`.

Therefore the updated external computational consequence is

\[
\boxed{
\forall x<10^{20},\quad
\exists\text{ prime }p\in(x,x+1724].
}
\]

This checkpoint transports that stronger finite frontier through the already-proved R005 p=2 witness-core machinery. It introduces no new prime-gap theorem.

External data sources:

- Prime Gap List, Exhaustively analyzed gaps: `https://primegap-list-project.github.io/fully-analyzed/`;
- Prime Gap record/maximal-gap tables: `https://www.pzktupel.de/RecordGaps/Risinggap.php`;
- Brian Kehrig, `prime-gaps-cuda`, for current computation provenance and the 1676/1724/1854 maximal-gap sequence.

---

## 2. E20-1 — current finite prime-gap operational bound

Let `p<=x<p'` be consecutive primes with real `x<10^20`.

The left endpoint satisfies `p<10^20`. Exhaustive analysis through `10^20`, together with the maximal-gap record sequence above, gives

\[
p'-p\le1724.
\]

Hence

\[
p'\le p+1724\le x+1724,
\]

so

\[
\boxed{
\text{there is a prime in }(x,x+1724]
\text{ for every }x<10^{20}.
}
\]

This is a **finite computational input**, not an unconditional analytic prime-gap theorem beyond the analyzed range.

---

## 3. Transport to the p=2 witness cores

Set

\[
A=k^2,\qquad U=k^2+2k.
\]

For a candidate prime witness `q` whose pure power does not already supply an exclusive basin collision, the e=1 cofactor interval is

\[
\left(\frac Aq,\frac Uq\right]
\]

with width

\[
\frac{U-A}{q}=\frac{2k}{q}.
\]

The existing R005 p=2 finite transport already established that the constant-gap input `1724` is sufficient for all relevant cube-root-core witnesses once

\[
1724\left\lfloor U^{1/3}\right\rfloor\le2k.
\]

The exact first integer satisfying this is

\[
\boxed{k_0=640,503,066.}
\]

For `q` above `A^(1/3)` but inside the `U^(1/3)` core, `q^3` itself lies in the square basin and forces `q`; therefore the e=1 gap bridge only needs the lower part of the core.

The largest cofactor point that must be covered is at `q=2`:

\[
\frac{A}{q}\le\frac{k^2}{2}.
\]

Thus the new `10^20` gap frontier applies simultaneously to every relevant cofactor point whenever

\[
\frac{k^2}{2}<10^{20}.
\]

The exact last integer satisfying this is

\[
\boxed{
K_{20}
=
\left\lfloor\sqrt{2\cdot10^{20}-1}\right\rfloor
=
14,142,135,623.
}
\]

Indeed

\[
14,142,135,623^2
=199,999,999,979,325,598,129
<2\cdot10^{20},
\]

while

\[
14,142,135,624^2
=200,000,000,007,609,869,376
>2\cdot10^{20}.
\]

---

## 4. E20-2 — extended fourth-root residual-arity range

The earlier R005-A exact prefix / scale-dependent gap certificates already cover the lower range and overlap the constant-1724 bridge.

Replacing only the old `6.8e19` external cofactor ceiling by the currently exhaustive `10^20` ceiling extends the established fourth-root-core forcing range to

\[
\boxed{
2\le k\le14,142,135,623.
}
\]

Therefore, under the declared external finite-gap computation:

\[
\boxed{
\text{every p=2 residual in this entire range, if one exists, has }\Omega=3.
}
\]

No claim is made for `k=14,142,135,624`.

---

## 5. E20-3 — extended least-basis classification

The stronger cube-root-core consequence is what matters for least-basis failure.

The existing exact low/mid classification proves that the only no-least square basins through the beginning of the large forced-core tail are the same 49 values:

`25, 47, 62, 123, 130, 151, 157, 162, 196, 217, 308, 364, 365, 479, 556, 888, 924, 935, 1008, 1056, 1078, 1162, 1290, 1345, 1454, 1511, 1541, 1577, 1612, 1627, 1679, 1781, 1790, 1865, 1897, 2073, 2164, 2850, 4412, 5833, 5834, 6339, 7289, 8584, 9369, 11226, 11433, 13006, 35901`.

For the large tail, the updated constant-gap bridge forces the entire cube-root core. By T-A20, no residual composite exists there.

Hence the finite classification strengthens to:

\[
\boxed{
2\le k\le14,142,135,623
}
\]

with **exactly the same 49 no-least basin indices**.

Equivalently,

\[
\boxed{
35,902\le k\le14,142,135,623
\Longrightarrow
\text{unique least safe divisor-witness basis}.
}
\]

The previous certified endpoint was

\[
11,661,903,789.
\]

The new endpoint adds exactly

\[
\boxed{2,480,231,834}
\]

additional basin indices, a `21.2678%` extension of the certified `k` frontier.

---

## 6. E20-4 — repair-complexity extension

The existing finite classification had

\[
\tau(\mathcal R_k)=1
\]

exactly at the 49 no-least basins and `0` elsewhere through the old endpoint.

Since the extended tail has empty residual hypergraph by cube-root-core forcing, the same statement now holds through the new endpoint:

\[
\boxed{
\tau(\mathcal R_k)\le1
\quad
\text{for every }2\le k\le14,142,135,623.
}
\]

Thus the first possible p=2 repair-complexity jump

\[
\tau\ge2
\]

is pushed beyond

\[
\boxed{14,142,135,623}
\]

under the declared external finite computation.

---

## 7. What changed, and what did not

Changed:

- the external finite cofactor frontier: `6.8e19 -> 1e20`;
- the certified p=2 k frontier: `11,661,903,789 -> 14,142,135,623`;
- the first possible `tau>=2` location is moved past the same new endpoint.

Unchanged:

- the 49 exact failure basin indices;
- T-A20/T-A21 witness-core mathematics;
- pair closure and residual hypergraph structure;
- the quarter-power obstruction theorem;
- Prime Toolkit status;
- Lean status;
- historical novelty status.

This is a **resource-boundary improvement**, not a new analytic theorem on prime gaps.

---

## 8. Reuse / prior-art disposition

The prime-gap computation is external prior computation. The arithmetic transport reuses existing R005-A machinery and the accepted Prime Toolkit domain facade.

Disposition:

`REUSE_APPLIED / EXTERNAL_FINITE_DATA_FRONTIER_UPDATED / NO_NEW_TOOL_FAMILY`.

Status remains:

`PROVED R005 FINITE-BOUNDARY EXTENSION UNDER DECLARED EXTERNAL COMPUTATION / NOT CANONICAL / LEAN PENDING`.

---

## 9. Next frontier

The old `6.8e19` Campbell cutoff is no longer the active finite bottleneck.

The new hard finite-data boundary is the exhaustive consecutive-prime-gap frontier at `10^20`.

Beyond `k=14,142,135,623`, a further unconditional finite extension requires at least one of:

1. a larger **exhaustively analyzed** consecutive-prime-gap range with a certified maximum-gap envelope;
2. a stronger explicit short-interval theorem on the relevant cofactor scales;
3. an R005-internal higher-power exclusive-collision argument that avoids needing the worst `q=2` e=1 cofactor point.

The third route is mathematically the most interesting because it could reduce dependence on brute-force external gap coverage.
