# X6 Unit105 — Johnson residue + exact native length and metric still lose N-BRC multiplicity

**Date:** 2026-11-18 (Asia/Hong_Kong). **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. **Author status:** `AUTHOR-PROVED / EXACT-FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED`.

**Frozen scientific pins:** P000 V5 `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. This is an X6 native signed Cell path/observer typing test. P000 and historical artifacts are unchanged.

## 1. Exact original consumers and claim

Historical `research_checks/P000_SIX_AXIS_JOHNSON_TROPICAL_ARITHMETIC_INTEGRATION_CHECK_20260830.py` (Git blob `62ea223dcbbb118186513737243ead040b77adc0`) defines complementary pairs `(0,5),(1,4),(2,3)` and, at lines 82–87, the exact finite Johnson residue

`rho_J(z)=((z0-z5) mod 2,(z1-z4) mod 2,(z2-z3) mod 2,(sum z_i) mod 3)`.

The same source defines `q_orbit(z)` from the three complementary-pair products `t_j=z_i z_k`: let `S=t_1+t_2+t_3` and `q_orbit=sort(S-2t_1,S-2t_2,S-2t_3)`. Its declared use is a **carrier/finite observer**, not a native path endpoint.

At the frozen P000 baseline `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` (blob `300a96e3dc24bf6fff73743037a0347a8bc83176`), `shortest_event_count`, `spatial_norm_squared` and `shortest_path_multiplicity` define

`L_1(z)=sum_i |z_i|,quad L_E^2(z)=sum_i z_i^2,quad B_min(z)=L_1(z)! / prod_i |z_i|!`.

**Unit105 proposition:** Even the enlarged joint observer `K(z)=(rho_J(z),q_orbit(z),L_1(z),L_E^2(z))` does not determine `B_min(z)` for general signed native X6 displacements. Therefore equal finite Johnson/carrier readout, equal shortest path *length*, and equal P000 squared length do not certify equal natural N-BRC shortest path multiplicity.

## 2. Exact globally valid witness and proof

Take the two native signed displacements

`a=(-3,0,3,0,0,0)` and `b=(-1,-4,-1,0,0,0)`.

For both, every complementary pair product is zero, so `q_orbit=(0,0,0)`. Direct integer evaluation gives

`rho_J(a)=rho_J(b)=(1,0,1,0)`,

`L_1(a)=L_1(b)=6`, and `L_E^2(a)=L_E^2(b)=18`.

The signed native shortest word counts, keeping the distinct primitive axis names and signs, are

`B_min(a)=6!/(3!3!)=20` and `B_min(b)=6!/(4!1!1!)=30`.

Thus `K(a)=K(b)` while `B_min(a) != B_min(b)`. This explicit pair disproves global factorization of native shortest-path N-BRC multiplicity through `K`, without assuming a finite search covers unbounded X6.

**Constructive count-level repair.** If a consumer requires the numeric shortest-path multiplicity but not the full path-word provenance, retain the exact factorial denominator `F(z)=prod_i |z_i|!` along with `L_1(z)`. Then `B_min(z)=L_1(z)!/F(z)`. For fixed `L_1`, equality of `B_min` is equivalent to equality of `F`. The current collision has `F(a)=36` and `F(b)=24`; the missing count-level residual is explicit. For full path-formal BRC the ordered word labels still require richer information.

## 3. Reproducible finite census

An independently executed standard-library Python checker enumerated **all** signed six-coordinate vectors in each integer cube `[-B,B]^6` for `B=1,2,3,4`. For each vector it computed `K` and native shortest-path `B_min` with exact factorial arithmetic, grouped by the full `K` tuple and tested whether a fiber contains differing multiplicities. Every runtime check uses explicit `raise` logic, active in all optimization modes.

| Cube bound B | States | Distinct K packets | Conflicting K fibers |
|---:|---:|---:|---:|
| 1 | 729 | 94 | 0 |
| 2 | 15,625 | 903 | 0 |
| 3 | 117,649 | 4,758 | 0 |
| 4 | 531,441 | 17,822 | 3 |

At `B=4`, 48 enumerated states have a different multiplicity from their observation fiber's lexicographically first representative; the minimal colliding shortest length in this cube is `L_1=6`. The bounded result proves `B=4` is the first failure among these exhaustive boxes; the two explicit vectors prove failure without a bound.

The program was executed with CPython normal, `-O`, and `-OO`. All three output files were byte identical: SHA256 `254a53cc3aaa25a3700cd492a96f96a52b458d89f6521c27f880f46f6d7f7f2e`.

Source: `research_checks/X6_UNIT105_JOHNSON_BRC_FIXED_LENGTH_NORM_COLLISION_CHECK_20261118.py`, commit `f6997c7dbe6201ac4270d5c8b81c0cd1dfa20814`, blob `45674250d69a2e241601c7509f37e0f59e7d183c`, local SHA256 `c11b9e8d60682b7699ad7e1595b34eba2b476cb31cc630650624c94394d9d66a`.

Certificate: `research_checks/X6_UNIT105_JOHNSON_BRC_FIXED_LENGTH_NORM_COLLISION_RESULTS_20261118.json`, commit `6f200054e9f499326943b91b6bbc50b526d50cb5`, blob `794ac001c0c0c549f3dc2921f358ea1ea316c075`.

This is an independently executed finite integer check, not a rerun of the original R063/Helly native benchmark. The original Johnson program is an appropriately typed observer computation. This unit detects a **necessary downstream type guard**, not an already-proven defective caller.

## 4. Mother objective and next exact work

The LP019 historical allegation of **subtraction of positive natural N-BRC counts** remains `UNRESOLVED_PROVENANCE`; different multiplicities in this counterexample arise from distinct **positive** native shortest-word collections, not signed cancellation. LP011 alleged defective native `argmax` callsite is likewise unresolved. Retain the independent Driver `REQUEST_REVISION` for historical source claims.

For LP003/005/023/028 and any theorem-facing downstream consumer using Johnson residues, inspect the exact `commit:file:line` where a numeric native shortest BRC count is requested. If it uses `K` as a complete native-state key, this new witness is a discriminating regression; if it only uses `K` for carrier invariants, retain that correct interface. Preserve original signed endpoint and contributor/observer labels until safe quotient.

Original research identity `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-3e221a50dc8818f914e228f6`, RUN `RUN-95866d78d35721116c362956`; original Source pins and contributions are unchanged.

**Do not repeat:** Units64–104 results, original R063/Helly native benchmark, the prior successful Units102–103 semantic PROGRESS, or unknown/rejected mutations. **Next executable action:** evaluate the precise surviving Johnson/FCC-derived consumers for native path-count factorization and actual LP011/LP019 historical bad callers; save a typed downstream source:line ledger, with a real minimal repair only on evidence of a defective executable interface.
