# R005-A — p=2 Power-Lifted Exclusive-Cofactor Compression

Status: `PROVED R005 STRUCTURAL + FINITE-BOUNDARY THEOREM UNDER DECLARED EXTERNAL GAP INPUT / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-30`  
Researcher-ID: `R005A-7C2`  
Task: `RS-R005-PRIME-ALGORITHM-LAB`  
Owner generation: existing `research/r005a-prime-algorithm-lab-20260810`

## 1. Main correction to the finite-gap transport

The earlier p=2 finite-gap bridge forced a witness `q` using only an e=1 exclusive collision

\[
q r\in(k^2,k^2+2k].
\]

That makes the worst cofactor point occur at `q=2`, namely `x=k^2/2`, so an external gap table valid through cofactor scale `X` only reaches `k~sqrt(2X)`.

This is unnecessarily restrictive.

The R005 witness language already permits exclusive collisions of the form

\[
q^e r,
\]

where `r>k`. By choosing the exponent `e` adaptively, one can simultaneously:

1. keep the available cofactor interval at least as wide as the external gap envelope `G`;
2. push the cofactor point far downward;
3. preserve singleton candidate support `{q}`.

For the current external input `G=1724`, `X=10^20`, this changes the certified p=2 least-basis frontier from order `X^(1/2)` to order `X^(2/3)`.

The previous checkpoint

`docs/R005A_P2_1E20_EXHAUSTIVE_GAP_BOUNDARY_EXTENSION_20260830.md`

remains correct as an e=1 specialization, but its `k=14,142,135,623` endpoint is no longer the active R005-A frontier.

---

## 2. P2-PL1 — maximal admissible q-power

Let

\[
A=k^2,\qquad U=k^2+2k,
\]

and suppose an external finite computation supplies

\[
\boxed{
\forall x<X,\quad
\exists\text{ prime }r\in(x,x+G].
}
\]

For the current application:

\[
G=1724,
\qquad
X=10^{20}.
\]

Define the width budget

\[
T=\frac{2k}{G}.
\]

Fix a prime candidate witness `q` satisfying

\[
q\le T.
\]

Choose `e>=1` maximal such that

\[
Q=q^e\le T.
\]

Then

\[
qQ>T.
\]

The key lower bound is

\[
\boxed{Q\ge\sqrt T.}
\]

### Proof

If `q>=sqrt(T)`, then `Q>=q>=sqrt(T)`.

If `q<sqrt(T)`, maximality gives

\[
Q>T/q>\sqrt T.
\]

Thus the selected q-power never falls below the geometric mean scale `sqrt(T)`.

This bound is uniform in q.

---

## 3. P2-PL2 — power-lifted cofactor compression

Put

\[
x=\frac{A}{Q}.
\]

Because

\[
Q\le T=\frac{2k}{G}<k
\]

for `G>2`, we have

\[
x=\frac{k^2}{Q}>k.
\]

Hence any prime `r>x` automatically satisfies

\[
r>k,
\]

so `q^e r` has exactly one candidate-prime support coordinate, namely `q`.

The available cofactor interval has width

\[
\frac{U-A}{Q}
=
\frac{2k}{Q}
\ge G.
\]

Therefore, if `x<X`, the external gap premise supplies a prime

\[
r\in(x,x+G]
\subseteq
\left(\frac AQ,\frac UQ\right].
\]

Then

\[
A<Qr\le U,
\]

and `Qr=q^e r` is an exclusive collision forcing `q`.

Using P2-PL1,

\[
x
=
\frac{k^2}{Q}
\le
\frac{k^2}{\sqrt T}
=
\sqrt{\frac G2}\,k^{3/2}.
\]

Thus every witness `q<=T` is forced whenever

\[
\boxed{
\sqrt{\frac G2}\,k^{3/2}<X.
}
\]

Equivalently,

\[
\boxed{
Gk^3<2X^2.
}
\]

This is the power-lifted finite-data transfer law.

---

## 4. P2-PL3 — cube-root-core saturation

Let

\[
C_3=\lfloor U^{1/3}\rfloor.
\]

If

\[
GC_3\le2k,
\]

then every cube-root-core prime witness satisfies

\[
q\le C_3\le T.
\]

P2-PL2 therefore forces every such q under the additional cofactor-frontier condition

\[
Gk^3<2X^2.
\]

Hence:

\[
\boxed{
GC_3\le2k
\quad\land\quad
Gk^3<2X^2
\Longrightarrow
\text{entire cube-root witness core is forced.}
}
\]

By the existing T-A20 theorem:

\[
\boxed{
\text{no residual composite exists, so the forced core is the unique least safe basis.}
}
\]

The same argument automatically forces the fourth-root core as a subset.

---

## 5. Current numerical specialization: G=1724, X=10^20

The existing exact p=2 width-gate audit gives the first integer from which

\[
1724\,C_3\le2k
\]

holds continuously:

\[
\boxed{k_0=640,503,066.}
\]

The power-lifted cofactor-frontier endpoint is the exact largest integer satisfying

\[
1724\,k^3<2\cdot10^{40}.
\]

Thus

\[
\boxed{
K_{\mathrm{PL}}
=
\left\lfloor
\sqrt[3]{\frac{2\cdot10^{40}-1}{1724}}
\right\rfloor
=
2,263,762,760,542.
}
\]

At this endpoint:

\[
1724K_{\mathrm{PL}}^3
=
19,999,999,999,981,242,934,731,378,909,949,821,511,712
<2\cdot10^{40},
\]

whereas

\[
1724(K_{\mathrm{PL}}+1)^3
>2\cdot10^{40}.
\]

The endpoint is a conservative certificate boundary of the uniform `sqrt(T)` compression; it is not asserted that `K_PL+1` is a mathematical failure.

---

## 6. Extended p=2 least-basis classification

The already-certified low/mid part determines exactly the same 49 no-least basin indices, all at `k<=35901`.

The large tail now has three overlapping forcing mechanisms:

1. exact / scale-dependent finite gap transfer;
2. the e=1 constant-gap bridge;
3. the new power-lifted q^e cofactor bridge.

P2-PL3 covers the entire tail from `k_0=640,503,066` through `K_PL`.

Therefore, under the declared `10^20` exhaustive prime-gap input:

\[
\boxed{
2\le k\le2,263,762,760,542
}
\]

has no-least behavior **exactly** at the same 49 indices:

`25, 47, 62, 123, 130, 151, 157, 162, 196, 217, 308, 364, 365, 479, 556, 888, 924, 935, 1008, 1056, 1078, 1162, 1290, 1345, 1454, 1511, 1541, 1577, 1612, 1627, 1679, 1781, 1790, 1865, 1897, 2073, 2164, 2850, 4412, 5833, 5834, 6339, 7289, 8584, 9369, 11226, 11433, 13006, 35901`.

Equivalently,

\[
\boxed{
35,902\le k\le2,263,762,760,542
\Longrightarrow
\text{unique least safe divisor-witness basis}.
}
\]

Relative to the immediately previous e=1 endpoint `14,142,135,623`, this is an additional

\[
\boxed{2,249,620,624,919}
\]

basin indices and a factor of approximately

\[
\boxed{160.0722}
\]

in the certified endpoint.

Relative to the older Campbell-based endpoint `11,661,903,789`, the new endpoint is about `194.1161` times as large.

---

## 7. Repair-complexity consequence

The 49 failure basins remain the only residual basins in the certified interval; all have

\[
\tau(\mathcal R_k)=1.
\]

Every other certified basin has empty residual hypergraph.

Hence

\[
\boxed{
\tau(\mathcal R_k)\le1
\quad
\text{for every }2\le k\le2,263,762,760,542.
}
\]

The first possible p=2 repair-complexity jump `tau>=2` is therefore pushed beyond `2.2637e12` under the declared external finite input.

---

## 8. Why this is structurally different from just extending a database

The improvement is not produced by a larger external cofactor table.

The same finite gap resource `(G,X)=(1724,10^20)` is being consumed more efficiently by changing the R005 certificate language:

\[
q r
\quad\longrightarrow\quad
q^e r.
\]

The exponent is selected so that

\[
q^e\approx\text{a maximal q-power below }2k/G.
\]

This yields the geometric-mean compression

\[
q^e\ge\sqrt{2k/G}
\]

and therefore the cofactor-scale law

\[
\boxed{
x_{\max}=O(k^{3/2})}
\]

instead of the e=1 worst case

\[
x_{\max}=O(k^2).
\]

Accordingly a fixed external cofactor frontier `X` supports

\[
k=O(X^{2/3})
\]

rather than only

\[
k=O(X^{1/2}).
\]

This is a genuine R005 observation-language compression theorem, even though the prime-gap input itself is wholly external.

---

## 9. Prior-art / ownership boundary

Prior mathematics/computation:

- consecutive-prime gaps and their exhaustive finite computation;
- integer powers and elementary interval arithmetic.

R005-specific composition:

- exclusive-collision witness semantics;
- candidate-support requirement `r>k`;
- adaptive q-power selection under a width budget;
- transport from finite prime-gap resource to least-basis saturation.

No historical novelty claim is made. Novelty remains `UNVERIFIED`.

Prime Toolkit disposition:

`REUSE_APPLIED / NEW R005 THEOREM-LEVEL COMPRESSION / NO_NEW_TOOL_FAMILY`.

No Foundation ownership change, no Lean claim, no canonical promotion.

---

## 10. Next frontier

The new active bottleneck is no longer the e=1 `q=2` cofactor point.

At the uniform level, the worst selected q-power lives near

\[
q\approx\sqrt{2k/G},
\]

which makes the `sqrt(T)` bound essentially the correct generic lower envelope for a single q-power coordinate.

The next research question is whether the bound can be sharpened by using:

1. the fact that `q` must be prime;
2. scale-dependent actual gap envelopes instead of the single constant `G=1724`;
3. multiple admissible exponents / multiple exclusive-collision channels for the same q;
4. a second witness coordinate when the first q-power channel is near the geometric-mean worst case.

Those routes could push the finite endpoint past the current `O(X^(2/3))` certificate without extending the external exhaustive gap frontier itself.
