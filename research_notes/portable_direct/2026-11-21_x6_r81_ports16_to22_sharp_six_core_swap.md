# X6 R81 — 四通道正权 BRC：16–21 Port 与 22 Port 的精确六候选核心及临界替换

Date: 2026-11-21 (Asia/Shanghai)
Scientific status: FINITE_EXHAUSTIVE_EXACT_INTEGER_PROOF / AUTHOR_CHECKED / NOT_INDEPENDENTLY_REVIEWED.
Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.
Direct predecessor: [R80](2026-11-21_x6_r80_sharp_five_core_ports11_15.md) and R72–R79 for problem context. This theorem's proof does **not** rely on R72's 28-candidate covering.

## Observer, quantifiers, and exact theorem

The conditional positive-count degree-four BRC star-histogram observer has four channels, unknown common additive offset, and arbitrary weights `w=(A,B,C,D) in R_{>0}^4`. For an integer high-degree histogram difference `a=(a2,a3,a4) != 0`, define

```
q(a)=max(sum_{d=2}^4 max(a_d,0), sum_{d=2}^4 max(-a_d,0)),
z(a)=(0,2a2+6a3+12a4,6a2+24a3+60a4,14a2+78a3+252a4),
g_ij(a)=|z_i(a)-z_j(a)|/2  (i<j, i,j=1..4),
F(a;w)=max_{i<j} g_ij(a)/(w_i+w_j).
eta*(p,w)=min_{a in Z^3\{0},q(a)<=p} F(a;w).
```

The six pair gaps are ordered `12,13,14,23,24,34`.

**Theorem A (six-core, entire 16–21 window).** For **every** integer `16<=p<=21` and **every** strictly positive real four-weight vector,

```
eta*(p,w) = min_{a in S16} F(a;w),
S16 = {(3,-4,1),(3,-7,2),(6,-4,1),(9,-5,1),(10,-5,1),(15,-6,1)}.
```

**Theorem B (six-core, 22 Port).** For **every** strictly positive real four-weight vector,

```
eta*(22,w) = min_{a in S22} F(a;w),
S22 = {(3,-4,1),(6,-4,1),(9,-5,1),(10,-5,1),(15,-6,1),(21,-7,1)}.
```

**Sharp cardinality**: for each specified Port count, the displayed family has cardinality six and cannot be reduced or replaced by a universally sufficient family with fewer than six *feasible integer-difference directions up to the equivalence a~−a*. Each member uniquely wins at a positive-integer four-weight profile against **every feasible integer difference** (up to ±), not merely against this chosen six-core.

The new 22-Port direction `(21,-7,1)`, with six-gap vector `(6,9,0,3,6,9)`, coordinatewise dominates the previously essential `(3,-7,2)`, whose gaps are `(6,15,0,9,6,15)`, once q=22 is feasible. Thus the minimal core undergoes an exact **replacement**, not an increase from six to seven.

## Complete finite proof and reproducibility

For p<=22, q(a)<=p implies |a2|, |a3|, |a4|<=p. The saved standalone verifier enumerates the inclusive integer cube [-22,22]^3, discards zero, retains exactly **37,994** signed nonzero differences with `q<=22`, of which **33,152** satisfy `q<=21`. These are complete domains, since no feasible integer difference lies outside the cube.

At p=21, the program checks **six exact componentwise inequalities** for every one of 33,152 signed differences against S16 and finds one suitable S16 member. The deterministic first-witness allocation is `[31198,104,1718,26,104,2]` in the displayed order. Every S16 member has q<=16, so the same witness covers *every* 16<=p<=21. At p=22 the analogous certificate for all 37,994 signed differences uses S22, and the first-witness counts are `[35814,1916,66,184,2,12]`. Both six-integer counts sum to their complete populations. For all weights w>0, componentwise gap dominance implies F(s;w)<=F(a;w) because all denominators w_i+w_j are strictly positive, establishing the universal real-weight conclusion without extrapolating from a finite parameter sample.

For minimality, the verifier independently evaluates the exact rational objective for each full signed domain at six explicitly supplied positive integer weights. It uses BigInt cross products, not floating point. At each weight, the unique minimizers are exactly ± the corresponding family member, with the following precise witness table. The last column is the smallest cost of any other integer difference, showing an actual strict gap.

| p | Essential difference | q | w=(A,B,C,D) | eta* | second cost |
|---|---|---:|---|---:|---:|
| 16–21 | (3,-4,1) | 4 | (18,12,1,1) | 9/19 | 1/2 |
| 16–21 | (3,-7,2) | 7 | (1,12,30,1) | 15/31 | 1/2 |
| 16–21 | (6,-4,1) | 7 | (1,1,1,24) | 12/25 | 1/2 |
| 16–21 | (9,-5,1) | 10 | (1,1,6,12) | 6/13 | 1/2 |
| 16–21 | (10,-5,1) | 11 | (1,1,1,1) | 1/2 | 3 |
| 16–21 | (15,-6,1) | 16 | (1447,167,166,1850) | 1/336 | 1/333 |
| 22 | (3,-4,1) | 4 | (18,12,1,1) | 9/19 | 1/2 |
| 22 | (6,-4,1) | 7 | (1,1,1,24) | 12/25 | 1/2 |
| 22 | (9,-5,1) | 10 | (1,1,6,12) | 6/13 | 1/2 |
| 22 | (10,-5,1) | 11 | (1,1,1,1) | 1/2 | 1 |
| 22 | (15,-6,1) | 16 | (1447,167,166,1850) | 1/336 | 1/333 |
| 22 | (21,-7,1) | 22 | (1,179,153,15) | 9/154 | 1/16 |

At w=(1,12,30,1), the strict Port-21 winner `(3,-7,2)` gives eta*=15/31. At Port 22 the new direction `(21,-7,1)` dominates it, and the exact minimum becomes **6/13**, a real phase transition. All conclusions hold for the defined conditional BRC observation only.

## Evidence files and tests

The verifier regenerates all six-gap vectors directly from the displayed z formula, enumerates the complete signed domains, checks componentwise domination and the unique winning ± pairs, and asserts the stated phase transition. It uses only built-in JavaScript BigInt and throws on violation.

- [Full exact verifier](x6_r81_ports16_22_two_sharp_six_cores_verify.js): immutable commit `68e0dfab66e59f26e00f5183c324cd56c50bfcc3`, blob `ba7c59d988b19f3cdb35b3d4dcc94c46b497aea9`.
- [Full output certificate](x6_r81_ports16_22_two_sharp_six_cores_results.json): immutable commit `8532d7580c7e1664ef8690763718e8dc10126f1b`, blob `12b1119567ae97911434c09ec8347710f1ccb41d`.
- Recompute using `node x6_r81_ports16_22_two_sharp_six_cores_verify.js`; compare full JSON. The author also checked selected profiles with an independent Python Fraction implementation. Exact finite coverage and reproducible enumeration are author-side proof evidence, **not independent scientific review**.

## P000 and native semantics

The frozen P000/ACTIVE Heartbeat World remains six-dimensional in native space with optional separate time, no native plane, native 120° angle, and whole triadic primitive balance. The above positive-count BRC histogram projection is an independently scoped *observer*. It has not been proved to preserve named Cell/Link/Port, native rotation, triadic event sign/phase, complete joint path or future operations. It should not be promoted to native physical precision or a formal X6 Result. This project paper and related R80 are portable research artifacts and do not authorize a formal CLAIM, Activity checkpoint or review status.

## Remaining work

Determine the exact minimal weighted cores as p extends from 23 toward 124, where a new direction may dominate, tie or replace earlier winners. Independently inspect the native X6 whole-event observer fibers at a specified time/branch horizon. Preserve original scientific pins and external source provenance.
