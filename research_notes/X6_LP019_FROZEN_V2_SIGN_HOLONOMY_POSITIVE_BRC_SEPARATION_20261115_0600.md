# X6 LP019 — frozen six-axis V2: chart-sign holonomy does not cancel positive BRC count (2026-11-15 06:00 +08:00)

**Mother:** `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`. Original researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-30a8f5fd123215e08bd4a7cf`, RUN `RUN-3356cbe3c2b4916d79399941`. These identifiers are attribution, not proof of current write authority.

**Frozen science:** signed X6 P000-V5 Cell torsor `Z^6` and independently typed relative/chart/BRC observers at `59538f585d037d09ef687b28715c4bc1a3f9fe03`; pre-rebase corpus `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. This note tests a *new, previously unlisted frozen V2 executable family*; it does not reopen earlier inspected tool-discovery sources or superseded PR #1257.

**Evidence status:** AUTHOR-SOURCE-VERIFIED plus an independent exact JavaScript integer/enumeration check in the research conversation; UNREVIEWED / NOT_ADMITTED. The original Python checker, R063 C3/C4 and other earlier benchmarks were **not executed** in this unit.

## 1. Exact frozen and current-source provenance

At both frozen `fd2bcff...` and read-back current main, the following file Git blobs are identical:

| File (under `experiments/six_axis_foundation_v2_20260905/`) | Git blob SHA-1 | Relevant function/lines |
| --- | --- | --- |
| `six_axis.py` | `2a16d04bd6c5e6d50e0fdd20e455f854b71bdcf4` | `ChartSignConnection`, lines 75–103; `normalize_counts` and `CountAtlas`, lines 105–206; `TypedArrow`/`arrow_product`, lines 210–242; conditional `quadratic_extension`, lines 245–253 |
| `vendor/atlas_brc.py` | `881a34d1919da64a85e6e06902ec3f23654a147e` | `BranchKey`, lines 137–174; positive histogram `validate_histogram/add/multiply/relabel/moment`, lines 190–230; typed two-active-axis `sector_norm_squared`, lines 233–242 |
| `ports.py` | `fd9b558e007a24c1ced932da0a53b4b78b5ffef0` | Formal rational Schur ports and determinant/parameter-specialization guards; neither a natural-BRC signed-cancellation operator nor a signed native-axis selector |
| `check_six_axis.py` | `b410ac9dadfaf2a5588f4bdf8242c1fdcd2399db` | Gauge/triangle tests around lines 57–80; three-chart/gluing and frame/branch tests separated; original source inspected only |

The `six_axis.py` comment expressly types the connection as a **scalar sign bundle on the chart graph, not native spatial transport**. The vendor header types the six-label trace/atlas as a BRC research prototype, **not native metric**. There is no bridge call in the inspected `six_axis.py` that supplies `ChartSignConnection.signs` as multiplicity coefficients to `vendor.add`, `vendor.multiply` or `arrow_product`.

## 2. A complete exact gauge/holonomy certificate

Let the four K4 chart vertices be A,B,C,D and the ordered edges be AB,AC,AD,BC,BD,CD. A chart connection assigns six signs `sigma_uv in {+1,-1}`. A vertex gauge `eps_v in {+1,-1}` changes the edge signs by
`sigma'_uv=eps_u sigma_uv eps_v`. For any triangle `uvw`, the character `H_uvw=sigma_uv sigma_vw sigma_wu` is gauge invariant, because every `eps_v` occurs twice.

The product of the four K4 triangle characters is `+1`: every edge occurs in exactly two triangles. Conversely, a spanning-tree gauge normalization leaves three independent cotree-edge signs, so all eight compatible triangle-character patterns occur, each on exactly eight of the 64 edge-sign assignments. In particular **exactly eight** connections have `H_ABC=H_ABD=H_ACD=H_BCD=-1`; one is `sigma=(-1,-1,-1,-1,-1,-1)`. These are scalar chart holonomies, not negative BRC counts or full X6 Cell returns.

An independent exact Boolean/integer enumeration using the original K4 edge and triangle order iterated all `2^6=64` sign assignments and all `2^4=16` vertex gauges; it verified `64*16=1024` gauge transformations and `1024*4=4096` triangle-character equalities, with **zero mismatches**. It counted 8 triangle-character patterns and 8 assignments per pattern, with 8 all-negative-triangle assignments. This is a reimplemented finite verification of the algebra above, **not an execution of the historical Python checker**.

## 3. Separation from exact positive natural BRC counts

The actual `vendor.atlas_brc.BranchKey` requires **strictly positive** rational weight. A histogram has strictly positive integer coefficients `c`; `vendor.add` performs `out[k]+=c`, `vendor.multiply` performs `out[x.then(y)]+=c*d`. Likewise `six_axis.arrow_product` uses `out[z]+=c*d` on matching typed endpoints. Induction over this declared constructor algebra shows every produced nonzero coefficient is positive and no operation consumes the above chart-connection sign. The `sector_norm_squared` function explicitly rejects a trace outside its declared two-active-axis sector; it is not the P000 signed-native six-axis absolute-coordinate `argmax`.

Concrete source-typed contrast: for one valid positive `BranchKey b`, the two histograms `{b:1}` and `{b:1}` add to `{b:2}`. Assigning a separate derived character `+1` to one occurrence and `-1` to the other would give signed **character readout** `(+1)+(-1)=0`, while the original **natural path count remains 2**. Such a character readout may be useful if separately declared; it is not a replacement for positive N-BRC multiplicity.

**Result for the mother ledger:** exclude this identified, exact frozen V2 `ChartSignConnection -> BranchKey/TypedArrow` family from the alleged LP019 *positive-natural-count signed cancellation* wrong-caller candidates. Its sign algebra, count algebra, and conditional sector metric are separately typed. The file-level inspection also found no LP011 **absolute signed-native-coordinate argmax** in these interfaces. Classification `PRESERVE_OBSERVER / PRESERVE_PATH_BRC / EXCLUDE_FALSE_POSITIVE`, with frozen path/function/line and Git blobs above. This bounded exclusion does **not** settle uninspected historical PR-only/dynamic callers or the original LP011/LP019 alleged wrong invocation.

## 4. Remaining exact actions

1. In remaining frozen historical PR-only executable branches and current dynamic consumers, identify an actual `relative/min-zero max -> signed-native absolute argmax` caller (LP011) or `chart sign -> subtraction of natural positive shortest-path multiplicity` caller (LP019), with original commit, full path, callsite line, operands and counterexample; absent such a caller, retain `UNRESOLVED_PROVENANCE`.
2. Complete the 28-LP downstream consumer ledger and submit the bounded evidence to independent Driver `REQUEST_REVISION`, without self-review.
3. The R063 same-object C3/C4 original 512-case benchmark remains independently pending authorized runner support in Issue #2416. Do not replace it with this gauge check or change the frozen input object.
4. Keep the 17:00 host-denied research prose mutation stopped; this newly scoped note is independent new-source analysis, not a retry of that denied report.

**Scientific classification:** exact finite and source-typed research evidence; no Foundation, Result or Review admission.
