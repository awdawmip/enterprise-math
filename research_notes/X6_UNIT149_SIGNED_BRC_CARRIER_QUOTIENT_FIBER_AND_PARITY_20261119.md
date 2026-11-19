# X6 Unit149 — Signed BRC path mass under a diagonal carrier-class observer

**Status:** AUTHOR_EXACT_PROOF / FINITE_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED (2026-11-19).  
**Mother objective:** PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905; task RS-X6-LEGACY-PLANE-RECONCILIATION, TP2-B4A441B23DA3159232C2.  
**Scientific source pin:** `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.  
**Actual consumers:** current `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` (blob `97ab1403ab04b4fa80034625fb1b2e3ed115e59b`; §§1–5, 7–8), and frozen `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` (blob `300a96e3dc24bf6fff73743037a0347a8bc83176`, functions `endpoint_multiplicity`, `return_multiplicity`, `shortest_path_multiplicity`). Historical `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` at `fd2bcff10ca6e147348b6c1236027fc0d2877df3` (blob `6ec0d73a19e28ec586c59a97d24f5798c9119771`, §§3–8) supplies the fixed positive-sector R062 comparison.

## Typed question and result

Let the native signed six-dimensional lattice be `V=Z^6`, with **twelve** primitive step labels `+e_i,-e_i`, `0<=i<6`. Fix the selected 3-axis carrier-readout diagonal `D=(1,1,1,0,0,0)`. The **derived** additive carrier-class observer is the quotient map `pi_D:V -> V/ZD`; it is not a native Cell-identity equivalence. For a raw signed endpoint `z` and integer word length `L>=0`, let `E_L(z)` be the number of native signed step words of length `L` that end at `z`, as given by the pinned `endpoint_multiplicity` formula. Define the path-augmented observer mass

`M_L([z]_D) = # {signed native words w of length L : pi_D(end(w)) = [z]_D}`.

**Theorem 149A (exact BRC pushforward).** For every integer `L>=0` and `z in Z^6`,

`M_L([z]_D) = sum_{k in Z} E_L(z+kD)`,

with only finitely many nonzero terms. For `z=0`, the summands are positive exactly for integers `k` satisfying

`3|k| <= L` and `k == L (mod 2)`.

Consequently, the observed zero-class mass first strictly exceeds genuine native return mass at `L=3`: `M_3([0])=12`, whereas `E_3(0)=0`. On odd lengths `L>=3`, `M_L([0])>0=E_L(0)`; on even lengths `L>=6`, `M_L([0])>E_L(0)`. The first even-length excess is `M_6([0])-E_6(0)=180`.

**Proof.** The quotient fiber of `[z]_D` is exactly the disjoint set `{z+kD:k in Z}` because `D` is primitive. Every signed word has one and only one raw endpoint, so partitioning its path-formal witnesses by those endpoints gives the displayed sum of natural-number multiplicities. Every step changes the native `L1` norm by at most one and toggles coordinate-sum parity. For `kD`, native shortest word length is `3|k|` and the endpoint parity is `3k == k (mod 2)`, hence the two support conditions are necessary. They are sufficient: use `|k|` steps in each of the first three signed axes to reach `kD`, and append `(L-3|k|)/2` adjacent inverse step pairs. Thus all and only the specified fibers have positive multiplicity. Since `k=0` is the genuine native return fiber, the remaining nonzero `k` are exactly the excess. In particular, at `L=3`, the positive `D` and negative `-D` native endpoints each have `3!=6` words. At `L=6`, the two endpoints `±2D` each have `6!/(2!)^3=90` shortest words. This proves every asserted bound and threshold. QED.

**Exact kernel formula.** Put `a_i=max(z_i,0)`, `b_i=max(-z_i,0)`, `q=(L-sum |z_i|)/2`. If `q` is not a nonnegative integer, `E_L(z)=0`; otherwise

`E_L(z)=L! sum_{q_0+...+q_5=q} prod_{i=0}^{5}[(a_i+q_i)!(b_i+q_i)!]^{-1}`.

This is the mathematical formula in the frozen `signed_brc.py`; it counts signed words, not just shortest words and not positive-only R062 sector traces.

## Exact source-pinned finite check

A standalone independent integer checker evaluated the factorial/weak-composition formula and, separately, full signed-step dynamic programming for all 12 primitive labels through `L=8`. The two routes agreed for **every** `kD` endpoint with `3|k|<=L`; a separate aggregate DP filter matched each carrier-class mass. No floating point arithmetic.

| L | Native return E_L(0) | Class mass M_L([0]) | Hidden extra |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 2 | 12 | 12 | 0 |
| 3 | 0 | 12 | 12 |
| 4 | 396 | 396 | 0 |
| 5 | 0 | 1,080 | 1,080 |
| 6 | 19,920 | 20,100 | 180 |
| 7 | 0 | 93,240 | 93,240 |
| 8 | 1,281,420 | 1,321,740 | 40,320 |

Exact check run `python`, `python -O`, `python -OO`; stdout/file SHA256 for each: `50977bc5674fd4c20ee36bf779f6d2587f6d56796da12fc660a5055a58761a9a`. Independent checker path `research_checks/X6_UNIT149_CARRIER_BRC_FIBER_CHECK_20261119.py`; certificate path `research_checks/X6_UNIT149_CARRIER_BRC_FIBER_RESULTS_20261119.json`.

## Claim-level X6 reconciliation and boundaries

- **PRESERVE_PATH_BRC:** the original R062 positive `(1,1,0)` two-word diamond and `(3,4,0)` thirty-five-word trace counts survive at exactly their signed native shortest-path specialization. Its historical three-positive-axis origin/line identity does not define current native Cell identity.
- **PRESERVE_OBSERVER:** the R062 carrier triangle readout `pi_D(D)=0` may describe a return to the same *carrier class*, while the native path ends at nonzero Cell displacement `D`. In a fully signed `L=3` path population both orientations `D,-D` contribute six words each. The current bridge's positive six-word example is its positive-only sector, not the full class mass.
- **Exact consumer contract:** to count the carrier class, retain path-formal/native endpoint typing, apply the quotient to each endpoint, and **sum multiplicities** over the fiber. Boolean support may then be taken; it cannot reconstruct lost multiplicity and no subtraction rule follows.
- **Unresolved historical provenance:** this analysis does not identify a specific alleged historical LP011 incorrect signed-argmax call or LP019 incorrect N-BRC subtraction call. Their exact `commit:path:line` attribution remains `UNRESOLVED_PROVENANCE`. This proof adds an exact forward aggregation law without inventing a past faulty caller.

This is an exact result for the declared `Z^6/ZD` derived carrier-class observer; full FCC carrier embeddings, original R063 six-file 512-case benchmark, independent Driver review and formal admission remain separate. No P000/Foundation input or existing Research Result is changed.

**Remaining task:** finish historically pinned/current downstream active source:line consumer coverage, exact LP011/LP019 attribution if present, and independent Driver review; keep current author claim/run and frozen pins separate from maintenance lane.
