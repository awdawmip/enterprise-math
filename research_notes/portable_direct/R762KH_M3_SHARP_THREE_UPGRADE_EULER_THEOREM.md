# R762KH — Three-inactive-Port exact upgrade threshold and universal 42-event Euler construction

Date: 2026-11-23. Status: **AUTHOR_PROVED_BY_COMPLETE_EXACT_FINITE_DP / EXACT_INTEGER_CHECKED / NOT_REVIEWED**.

## Source and exact observer
Original immutable science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json` (P000 V5); current Task family `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. The previous author-side R762KF/KG proofs and counterexample are in Draft PR #3012, with verified predecessor source `14d483cb5e4b07e3177e082a49ed479321a72ffd`. These do not grant mathematical review or task CLAIM.

The auxiliary **unsigned** six-axis Port–Euler model has twenty different triple supports `abc` on axes `0,...,5`, fifteen pair-Port vertices `ab`, and a legal color-`abc` edge joining any two *active* Ports among `ab,ac,bc`. Delete the three pairwise-disjoint pair Ports `01,23,45`. The other twelve pair Ports remain active. An all-positive inventory is an integer multiplicity `n_s >= 1` for each triple support. An exact Euler realization is a connected colored multigraph with exactly `n_s` legal events of each color and a positive even degree at each of the twelve active Ports.

The twelve **forced colors** with only one available event edge are:
`012 013 014 015 023 045 123 145 234 235 245 345`.
The eight **flexible colors**, each allowing a triangle of three edges, are:
`024 025 034 035 124 125 134 135`.
Set `U = {s flexible : n_s >= 2}`; every other flexible support is a singleton.

## Theorem KH.1 — Sharp universal forced-count threshold

**For any fixed upgrade set U and any fixed positive flexible counts consistent with U**, the following are equivalent:

1. `|U| >= 3`.
2. **Every** assignment of positive integer counts to the twelve forced colors admits a connected positive-even exact-color Euler realization on all twelve active Ports (with any prescribed active starting Port).

When `|U| <= 2`, for each such U some forced parity assignments are impossible, not all forced assignments.

### Exact reduction
The twelve forced support edges, which are all present at positive count, form three connected four-cycles on disjoint sets of four active Port vertices. Contract them to three vertices `A,B,C`. Each flexible triangle contains precisely one Port in each forced component, so its three legal edges represent respectively the three different component pairs `AB,AC,BC`.

The GF(2) boundary of an event edge `uv` is `2^u XOR 2^v` on the twelve active Port positions. A flexible singleton can contribute one of its three nonzero pair boundaries. For an arbitrary flexible count `n>=2`, exactly four boundaries are possible: zero and those same three pairs (the triangle's even boundary space). Every forced color contributes its unique edge boundary iff its count is odd. Across the `2^12=4096` forced oddness masks there are **512 distinct boundary targets**, all attained by positive forced counts (choose 1 for odd, 2 for even).

### Finite connected-parity lemma and complete computation
For each flexible singleton choose one edge (three possibilities); for each upgraded flexible support first use count 2 and choose an unordered pair of triangle edges with repetition (six possibilities). A choice has exact boundary `b_s` and a three-bit mask `t_s` indicating which of the component pairs `AB,AC,BC` its events use. Starting from `(b,t)=(0,0)`, the exact finite DP recurrence is
`
(b,t) -> (b XOR b_s, t OR t_s).
`
The full graph is connected exactly when `t` contains at least two distinct bits: forced edges have already connected each of the three components, and two different pair types connect all three.

The standalone standard-library program `R762KH_THREE_INACTIVE_UPGRADE_VERIFY.py` constructs legal edges directly from axis/pair incidence and exhausts **all 256 flexible upgrade subsets**, **all 512 forced boundary targets**, and the exact parity/type states. The number of forced targets admitting a *connected* solution is uniform for each size of U:

| upgraded flexible colors | number of U | connected forced boundary targets for every such U |
|---:|---:|---:|
| 0 | 1 | 465 / 512 |
| 1 | 8 | 495 / 512 |
| 2 | 28 | 508 / 512 |
| 3 | 56 | 512 / 512 |
| 4 | 70 | 512 / 512 |
| 5 | 56 | 512 / 512 |
| 6 | 28 | 512 / 512 |
| 7 | 8 | 512 / 512 |
| 8 | 1 | 512 / 512 |

The finite exhaustion is a proof of this stated finite lemma: each legal local multiset is represented, and XOR/OR retain exactly the observables needed for total parity and connectivity. It also checks parity-only states independently and finds that **every forced boundary with a parity solution has a connected solution** in the minimum 1/2 model. Independent direct enumeration of `3^8=6561` all-singleton flexible choices reproduces R762KG's `1881` distinct parity boundaries and its unobtainable boundary `4010`.

The companion verifier reconstructs full connected 20-color event graphs for **4096 distinct forced parity masks** with a particular three-upgrade U, checking exact counts, legality, even positive Port degrees, and connectivity. It also checks 16 arbitrary-larger-count extensions. These concrete graphs test the construction, whereas the full universal theorem follows from the complete finite lemma and the symbolic count extension below.

### Exact symbolic extension to arbitrary upgraded multiplicities
Each minimum-count-2 flexible witness selects either two *equal* triangle edges `(e_i,e_i)` (zero boundary, one component-pair type) or two *distinct* triangle edges `(e_i,e_j)` (the boundary of the third triangle edge, two different component-pair types).

For any even count `n>=2`, retain its two base edges and append `(n-2)/2` duplicate pairs of arbitrary legal edges. For odd count `n>=3`:

- If base was `(e_i,e_i)`, use all three triangle edges once and append duplicate pairs. Its boundary remains zero and it now connects all three forced components.
- If base was `(e_i,e_j)`, write `e_k` for the third edge, use `(e_k,e_i,e_i)` and append duplicate pairs. The exact identity `boundary(e_i) XOR boundary(e_j) = boundary(e_k)` preserves the desired boundary, and both the new and the old supports connect all three forced components.

Keep a singleton flexible event once; repeat every forced color's sole edge to its required positive count. Thus the DP zero-boundary connected graph is lifted to **every** fixed positive inventory respecting U: each exact count and total parity is preserved, and global component connectivity persists. The connected graph's degrees are strictly positive and even, hence Euler's theorem applies.

For each `|U|=0,1,2`, the finite parity-only DP leaves respectively `47,17,4` forced boundary targets unattainable, **for every U of that size**. Since the possible boundary palette of any `n>=2` flexible triangle is exactly the same four vectors, increasing flexible counts does not remove those parity obstructions. Choosing forced multiplicities 1/2 with the missing target proves the converse and exact threshold.

## Corollary KH.2 — All 42-event targets for three disjoint missing Ports

An inventory with five singleton supports, seven triple supports and eight double supports totals 42 events. Since there are only five singletons overall, at least **three of the eight flexible colors** have multiplicity `>=2`. Theorem KH.1 therefore constructs a connected 42-event Euler circuit for **each** of
`
C(20,5)*C(15,7) = 99,768,240
`
labeled inventories for every fixed triple of pairwise-disjoint missing Ports.

The six axes have **15** perfect matchings, all related by `S_6` axis permutations. Hence **1,496,523,600** (named missing-Port matching, labeled inventory) target configurations admit a complete 42-event closed walk.

For any one of the five *marked singleton* colors, adding two copies of a legal edge preserves even degrees and connectivity, giving a marked 44→42 construction. Across all fifteen matchings there are **7,482,618,000** such *marked* constructions. Neither this count nor the proof classifies distinct unmarked 44-event sources or arbitrary initial source histograms.

## Verification, provenance and continuation

Run `python R762KH_THREE_INACTIVE_UPGRADE_VERIFY.py` in Python standard library only. The deterministic output is saved as `R762KH_EVIDENCE.json`. All finite arithmetic is integer XOR/OR and all checks use exact connected components; no rounding or stochastic sampling.

The theorem is solely about the **unsigned composite observation graph**. P000 fixes six signed discrete spatial axes, primitive `TRIADIC_CLOSURE_E` three-force balance, native ordered Cell/Link/Port trajectories and residual BRC provenance. This research has not proved an observer-safe signed-native lift, equivalence or provenance quotient. P000 and the original scientific pin remain unchanged. **Independent review: NOT_REVIEWED**.

**Next:** classify the exact admissible forced parity masks and explicit Euler witnesses when `|U|<=2`, including a compact description of the four exceptional targets for two upgraded supports. Separately build a type-safe signed `TRIADIC_CLOSURE_E` event lift preserving ordered BRC source identity.

Scientific attribution: original Researcher `EM-X6-B1684F`, Session `MCP-04016ce373004d3e80f6bff85d689693`, Activity `RA-6F2C09233DC4F142A2F7795A`. This is a portable author-side scientific source, not protected native PROGRESS or a reviewed Result.
