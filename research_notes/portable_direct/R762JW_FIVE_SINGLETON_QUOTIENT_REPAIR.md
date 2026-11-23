# R762JW — Five singleton colors have universal quotient-parity and quotient-connectivity repair

Date: 2026-11-23 (Asia/Shanghai).
Scientific scope: **six-axis unsigned composite Port–Euler observer**, not native signed X6 Cell/path dynamics.
Status: **AUTHOR_EXACT_FINITE_THEOREM / TWO_EXECUTED_INTEGER_CHECKERS / NOT_REVIEWED**.

## Immutable inputs and provenance

P000 remains ACTIVE_LOCKED. This research continues the independently preserved R762JV five-singleton component classification at enterprise-math Draft PR #2993, commit a01f02bf6244901593d82b3e5afe4dd100ee3d36, research_notes/portable_direct/R762JV_FIVE_SINGLETON_PARITY_CHANNELS.md. The earlier original scientific input remains R762JT@6fda34681d94d915894ec5f1c32d1e3654102865. Neither input is rewritten or promoted.

Let A={0,1,2,3,4,5}; P=the 15 unordered pairs of A (Ports); S=the 20 unordered triples of A (colors). For a color abc, the allowable event edges are the three edges among Ports ab, ac, bc. Let M be an inactive Port matching of size m=0,1,2,3, V=P\M. Every color has two or three active incident Ports. Choose D⊂S of cardinality five; these are exactly the singleton colors. Each color s∈S\D is flexible and will have an integer multiplicity n_s≥2.

Build G_F(D,M) on V using all three candidate sides of every flexible color whose three Ports are active, and no sides from forced two-active-Port colors. Let C_1,...,C_c be its connected components. For edge uv, define its quotient boundary q(uv)=e_{C(u)}+e_{C(v)}∈GF(2)^c. Let E_c be the full even-weight subspace of GF(2)^c (dimension c−1). Let F contain, once each, the quotient edges belonging to every flexible color whose triangle has exactly two active Ports. These forced edges are present in any actual inventory with n_s≥2; their multiplicities will be used separately for parity.

## Theorem JW.1 (complete finite quotient-lifting theorem)

**For every matching M, every five-element D⊂S, and every b∈E_c, one can choose exactly one legal side e_s for each singleton color s∈D such that:**

1. The XOR of the five quotient boundaries equals b.
2. The multigraph on quotient vertices C_1,...,C_c containing the forced edges F and the five selected singleton edges is connected.

Quantifiers are universal in D, M and b. The theorem imposes **no choice of seven triple multiplicities**, so it also covers every (7 triple, 8 double, 5 singleton) inventory obtained from a (8,8,4,0) 44-event inventory by reducing a triple to a singleton, at the precise quotient level.

## Proof by exhaustive exact finite classification

Every m-element inactive Port matching is equivalent under S6 to one of:
m=0: empty; m=1: {01}; m=2: {01,23}; m=3: {01,23,45}.
For each representative enumerate all binomial(20,5)=15,504 sets D. A union-find computes G_F components from candidate triangle sides of the 15 non-singleton colors. If c=1, both claims are automatic; otherwise enumerate all choices of one legal edge per singleton, at most 3^5=243. Compute the five-edge quotient XOR directly and independently test quotient connectivity by union-find after adding forced edges. Assert the set of reachable, connected quotient boundaries equals the entire even subspace E_c.

All **62,016** (m,D) representative cases pass, including **12,652** cases whose flexible candidate graph is disconnected. Complete component-count spectrum, by m:

| m | c=1 | c=2 | c=3 | c=4 | c=5 | c=6 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 15,264 | 240 | 0 | 0 | 0 | 0 |
| 1 | 14,332 | 1,160 | 12 | 0 | 0 | 0 |
| 2 | 11,496 | 3,648 | 356 | 0 | 4 | 0 |
| 3 | 8,272 | 4,752 | 1,584 | 768 | 72 | 56 |

The first checker independently uses GF(2) bitmask dynamic programming, including the exact seven-odd-color forced-parity selection problem (choosing seven triple colors from S\D). It reports zero unreachable forced-parity masks for all 62,016 cases and the same component totals. The second checker enumerates legal singleton edge products directly, checks all of E_c (strictly stronger than only the realizable forced-parity masks), and checks connectivity for every target. Both were run locally using Python standard library without floating-point solvers. Each produced its own JSON output. The second checker has zero parity failures and zero connectivity failures for each m.

## Corollary JW.2 (full-graph even parity, not complete Euler existence)

Fix any such M,D and any multiplicities n_s=1 for s∈D and integers n_s≥2 for s∉D. Use the forced edges n_s times and set b equal to the quotient parity of those forced contributions. Theorem JW.1 supplies singleton-side choices cancelling b, while connecting the quotient components. The remaining parity boundary has even sum in each G_F component; the triangle-side incidence vectors of flexible three-active-Port colors span precisely that subspace.

For each flexible three-active-Port color with multiplicity n_s≥2, one can realize parity 0 or any one of its three pair-boundaries:
- n=2: two copies of a single side give 0; the two sides of a length-two triangle path give any chosen pair boundary.
- n=3: the three distinct triangle sides give 0; three copies of a chosen side give its pair boundary.
- n>3: add paired copies of a chosen side to one of these constructions.

Within each color, the XOR of any collection of its side-boundary generators is again 0 or one side boundary, so a GF(2) spanning representation can be combined into one chosen boundary for that color. Thus **an exact-multiplicity multigraph with even degree at all Ports and a connected graph of flexible-component quotients always exists** for the given five-singleton inventory.

JW.2 does not assert positive degree at every active Port nor that the final choice of flexible-color sides connects all vertices *inside* each flexible component. Those are the remaining requirements for N_(p,V)(n)>0. No 44→42 global theorem is inferred here.

## Exact reproduction and verification evidence

Files:
- R762JW_QUOTIENT_PARITY_DP.py — independent quotient GF(2) dynamic-programming parity screen, 62,016 cases.
- R762JW_QUOTIENT_CONNECTIVITY_BRUTE.py — independent direct legal-side enumeration, parity coverage and forced-edge quotient connectivity.
- R762JW_EVIDENCE.json — observed counts, execution hashes, exact scope and next question.

Run with Python 3.10+ from a writable directory; both checkers print per-m exact totals and write JSON results in the working directory. Output contents were checked after execution and agree on all component distributions.

Next: obtain a **simultaneous full-vertex connectivity and strict-positive-degree lifting theorem** for the flexible colors while respecting each color's actual multiplicity 2 or 3. A failed lifting would require an explicit original 44-event valid witness and a no-42-event proof before contradicting the target; mere quotient rank deficiency no longer suffices. Separately, a P000-native signed path / triadic closure / BRC residual-fidelity lift remains open.
