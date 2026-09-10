# Nollm Visual Toolkit 0.2.0

**Research workbench / important research infrastructure candidate.**
[中文说明](README.zh-CN.md)

An offline, inspectable tool for integer hex-carrier studies and explicitly supplied six-component X6 data. It separates **record identity, observation, and rendering**. This is a versioned software publication, not mathematical admission, a production Nollm integration, or a claim that six dimensions embed injectively in three.

## Start

From this directory, with Python 3.10 or later:

```sh
python -m pip install .
nollm-viz demo --out study.html
nollm-viz demo --kind x6 --out six_axes.html
```

Open the generated HTML in a browser. Each document includes its data and application code; there is no CDN, telemetry, account, or server dependency. The default demonstration contains all 65,536 integers from 0 to 65,535. The X6 demonstration is a separate, explicitly synthetic 729-state signed cube; missing X6 coordinates are never invented for the hex demonstration.

Optional static export: `python -m pip install '.[static]'`.

## Workbench

- Hexagonal cells, rotatable A2 cube-plane observation, and explicitly typed layer stacks.
- Six FCC carrier line families / twelve signed rays for supplied X6 coordinates, plus selected-three-coordinate observation and a true slice option. Full six-component records remain available.
- Integer, prime/background, remainder classes, Q16 quotient/remainder, one-unit weight difference, valuation and custom numeric layers.
- Exact coordinate slices, slice animation, camera rotation, coordinate and ID/number lookup, coincident-record cycling, neighborhoods and multiplication trajectories.
- Existing relation edges remain data; filtering is nondestructive. Prime display retains the composite background. Zero valuation is null, not a fabricated finite value.
- JSON and documented CSV round trips, PNG capture, visible-glyph SVG export, and dataset-bound view sessions. SVG does not promise the complete UI, legend or relation overlay. PNG pixels are not an inverse-data format.
- Integer validation, projection collision audit and deterministic data generation. All displayed records are submitted to rendering without sampling; finite screen pixels can overlap.

## Coordinate and observer contract

The hex demo uses `F(4n+d)=2 R60 F(n)+(d&1,d>>1)`, with `R60(q,r)=(-r,q+r)`. Its six nearest-neighbor directions belong to a two-dimensional A2 implementation carrier. `(q,r,-q-r)` is a plane in three display coordinates, not six independent native spatial axes. The synthetic radix depth in the demo is **not** a Nollm physical layer.

For X6, all six signed integer components are required. The six drawing vectors are `(1,1,0)`, `(1,-1,0)`, `(1,0,1)`, `(1,0,-1)`, `(0,1,1)`, `(0,1,-1)`. Their linear sum is a **declared 3D display observer**, not the completed global native/FCC bridge. Native components, IDs, relations and metadata are retained. Multiple identities at one projected center are explicitly grouped, never merged. A three-coordinate observation is not a native slice unless omitted relative components are zero.

This follows the current project boundary in `definitions/00_CURRENT_NATIVE_FOUNDATION.md`, `definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md`, and `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`. Screen coordinates, camera orientation, and Euclidean rendering do not redefine native axes, metric, time or Cell identity. No project definition is modified by this tool.

## Data

```json
{"schema":"NOLLM_VISUAL_DATA_V2","kind":"hex","title":"Example","metadata":{},"records":[{"id":"object-A","n":9,"coord":[2,3],"fields":{"score":7}}],"relations":[]}
```

Use `kind: "x6"` and exactly six supplied coordinates for X6. IDs must be unique strings, not row numbers; `n` is optional. Records can contain `layer` and arbitrary JSON metadata. Relationships use existing `source` and `target` IDs. Integer coordinates are limited to ±1,000,000 and the current tool accepts 1–200,000 records; general JSON integers must be exactly representable by browser numbers. These are implementation limits, not native-space limits. Nonfinite floats and incomplete coordinates are rejected.

CSV begins with `#nollm-meta=<JSON>` and columns `id,coord_json,extra_json`. Use the tool exporter rather than an arbitrary flattened CSV. It preserves extra record fields, metadata, relations and nulls. A view-session fingerprint describes its browser-normalized dataset, not a server signature; canonical JSON bytes and original source bytes remain separate provenance. The included SHA-256 fallback is a standard fingerprint implementation, checked against Python hashlib, not a cryptographic novelty or authentication mechanism.

```sh
nollm-viz validate data.json
nollm-viz render data.json --out study.html
nollm-viz convert data.json --out data.csv
nollm-viz profile data.json --axis s --out slices.json
nollm-viz import-legacy interactive_65536.html --out recovered.json
```

The legacy importer decodes a JSON literal only; it does not execute HTML or JavaScript. The prototype's zero valuation sentinel is repaired to null. The standard-library API is available from `nollm_visual_toolkit`.

## Verification and limits

```sh
python -m unittest discover -s tests -v
# Optional UI verification: Playwright plus a local Chromium executable.
python tests/browser_smoke.py --out /tmp/nollm-ui
```

The release verification records 26 unit tests and 43 Chromium acceptance checks. It covers the full 65,536-label dataset, Q16 reconstruction, data round trips, slices, trajectory and neighbor identities, 135 coincident-projection groups in the X6 demo, session restoration, exports and 390-pixel mobile layout. The browser host supplied the self-contained HTML through `set_content`; network/file navigation was unavailable. Native iOS Safari, physical touchscreen behavior, arbitrary third-party datasets, repository-wide CI, live Nollm workloads and performance at the 200,000-record limit are **not certified**. One frame with every record does not guarantee distinct screen pixels for every identity.

The renderer may be slower on large full SVG exports or frequent animated redraws. Timing/animation is an observer aid, not simulation of native time. Multiplication trajectories follow declared integer labels; they do not prove that coordinate multiplication implements ordinary integer multiplication.

## Version boundary

0.2.0 replaces the prototype's misleading three-Cartesian-axis 'six-axis' view with explicitly typed hex and X6 modes. It fixes local zoom bounds, row-index assumptions, zero valuation, projection-identity loss and dataset-bound session restoration. Source, tests, manifests and demo generators are included; large generated HTML datasets need not be committed. This tool does not rewrite the old prototype, historical research activity, Nollm architecture or accepted theorem registry.

License: MIT, inherited from Enterprise Math.
