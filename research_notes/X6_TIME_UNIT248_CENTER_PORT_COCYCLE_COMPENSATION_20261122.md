# X6 Unit248 — directed centre-Port precision cocycle repair and exact eight-event discriminator

Date: 2026-11-22. Scope: `RS-X6-NATIVE-TIME-DYNAMICS` / `TP2-91D4A7C2F63805BE21A3` / `PO-X6-UPPER-STRUCTURE-20260906`.
Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.
Original research provenance: on-hour `chatgpt-research-onhour-enterprise-math-20260923`; preserved historical SID `MCP-082892eb480e45dea6d4b9fcc0491034`. This GitHub science note is not a new native CLAIM, PROGRESS, physical Port admission, or a Result freeze.

## Exact frozen dependency and scientific question

Frozen P000 scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; signed six-axis Cell torsor, selected centred three-axis native slice, native `TRIADIC_CLOSURE_E`, and ordered BRC event provenance remain intact. Input: [Unit247](https://github.com/awdawmip/enterprise-math/blob/4eace2f3e36042dcf0f7812da498b49aee92acb1/research_notes/X6_TIME_UNIT247_CENTER_PORT_PRECISION_COSET_OBSTRUCTION_20261122_0000.md), the conditional twelve-Cell OUTER ring, original ring additive precision weights `g5=g10=3` and zero otherwise, inverse negative weights, `C_N` with `N=6·2^m`. There is no Source-admitted physical Port/sensor law in these inputs.

Unit247 used **zero** precision increment on both centre edges and found a doubled fixed-Cell C24 precision orbit for 18 of 36 ingress/egress pairs. The operational question is whether the extra bit is inevitable for a centre Port, or whether an explicit local precision update removes it without erasing the signed BRC path.

## Theorem — exact single-pair centre-weight criterion

For even `i,j in {0,2,4,6,8,10}`, let `x_i→P` have additive precision weight `alpha_i`, `P→x_j` weight `beta_j`; the intact labelled-triad occupancy, signed ring steps, serial events and target-empty guard are as in Units240–247. Let
[
d=(j-i)\bmod12,\quad
A(i,j)=\sum_{r=0}^{d-1}g_{(i+r)\bmod12},\quad
w_{ij}=\alpha_i+\beta_j .
]
For any **single-triad** closed path at the same ring Cell, `L` is its signed number of ring steps and `c` its number of complete directed centre passages. With `z=(L+dc)/12 in Z`, exact precision transport is
[
\boxed{\Delta=6z+(w_{ij}-A(i,j))c\pmod N.}
]
Proof: expand each centre passage to its clockwise `d`-ring arc for the scalar weight calculation. The resulting ring-only path winds `z` times with weight `6z`; replace each artificial arc's weight `A` by the actual centre passage `w`. The actual path is never quotient-collapsed; all original signed BRC primitive steps remain source data. A full forward ring realizes `6`, and `x_i→P→x_j` followed by `d` reverse ring events realizes `w-A`; finite modular concatenation generates all their integer combinations. Hence
[
\boxed{G_{ij}=\langle6,\alpha_i+\beta_j-A(i,j)\rangle\subset C_N,\qquad
|G_{ij}|=N/\gcd(N,6,\alpha_i+\beta_j-A(i,j)).}
]
The original `N/6=2^m`-state fixed-Cell precision register is preserved **iff**
[
\boxed{\alpha_i+\beta_j\equiv A(i,j)\pmod6.}
]
The zero-centre model in Unit247 fails this iff condition in precisely 18 of 36 pairs. Thus precision-state inflation depends on the centre update, not solely on its Cell topology.

## Theorem — all 36 directed centre passages at once

Define `B(0)=0`, `B(k)=sum_{r=0}^{k-1}g_r`, so `B(12)=6`. The even-indexed potentials mod6 are exactly
[
(B(0),B(2),B(4),B(6),B(8),B(10))=(0,0,0,3,3,3).
]
When **all six** ingress and **all six** egress edges are present, the closed precision orbit at every fixed ring Cell stays `<6>` iff there exists one `t in C6` such that for every even `i,j`
[
\boxed{\alpha_i\equiv t-B(i),\qquad\beta_j\equiv B(j)-t\pmod6.}
]
Proof of necessity: every `i,j` supplies a centre loop with weight `alpha_i+beta_j-A(i,j)`; preserving the ring-only state count forces it to be divisible by 6. Modulo 6, `A(i,j)=B(j)-B(i)`. Fix an egress `j_0`; the pairwise congruences force `alpha_i+B(i)` to be a common `t` and hence every `beta_j=B(j)-t`. Sufficiency: assign a potential `B(k)` at each ring Cell and `t` at `P`; every allowed directed edge's precision weight equals the endpoint-potential difference mod6. Every closed path has weight 0 mod6, while a 12-step ring still realizes +6. Exact fixed-Cell orbit therefore is `<6>`, cardinality `N/6`.

This is an **explicit Port update repair**, not a modification of P000 or a claim that nature adopts the repair. A representative `t=0` uses ingress weights `alpha_i=-B(i)` and egress weights `beta_j=B(j)`; different integral lifts modulo `N` may be used.

## Eight-native-event source discriminator and empirical requirement

Use the same chronological labelled-triad path as Unit247:
[
x_0\to P\to x_6\to x_5\to x_4\to x_3\to x_2\to x_1\to x_0.
]
It is **eight signed primitive events** in the conditional graph; the last six ring steps have total weight `-3`. The two locally distinct candidate updates make incompatible before/after predictions at the same Cell:

| Port precision law | Centre aggregate weight | C12 delta | C24 delta | C24 fixed-Cell orbit (full centre star) |
|---|---:|---:|---:|---:|
| Unit247 zero-centre model | 0 | 9 | 21 | 8 |
| Exact potential-compensated model `t=0` | +3 | 0 | 0 | 4 |

The experiment requires a **Source-admitted signed whole-triad Cell/Link/Port update**, actual occupancy/environment checks and an *independently measurable* C12/C24 precision register. The path alone validates model-internal predictions, not physical admissibility. If the register exists and the ring contribution is independently calibrated, the observed loop delta determines the centre aggregate `w_{0,6}=Delta+3 mod N`. This is the next exact discriminator: test centre compensation rather than assuming centre weight zero.

## Exact finite validation

A dependency-free JS checker executed in V8 with exact integer modular BFS across `N=6,12,24,48,96,192`, all `36` pair-specific directed centre graphs and the graph with all six ingress/egress spokes simultaneously. Its BFS checks ring-only versus repaired fixed-Cell orbit counts, the 18/18 zero-weight split, the six full-star values and the eight-event predicted residue. Actual integer assertions: **770**, accumulated BFS state visits **76167**, failures **0**. Full 36-case C24 and six-level certificates accompany the checker. This is a finite check of the exact conditional update model; the theorems hold for every `m>=0` by the algebraic proof.

No physical C12/C24 measurement, native six-file R063 benchmark, independent Driver review or formal Result/Source admission was performed. The historical earlier native PROGRESS remains distinct from Activity bookkeeping; source support [#2903](https://github.com/awdawmip/enterprise-math/issues/2903) still governs the materialization/typed continuation blockage.

Next exact action: use an actually Source-authorized physical signed Port and precision update to run/replay the eight-step same-Cell case, inspect environment/force-token conservation, measure the precision change, and decide between zero-centre, compensating and other weight laws. Do not assume either candidate is physical truth.
