# Nollm Visual Toolkit 0.3.0

**Research workbench / important research infrastructure candidate.**
[中文说明](README.zh-CN.md)

An offline, inspectable tool for integer hex-carrier studies and explicitly supplied six-component X6 data. It separates **record identity, observation, and rendering**. Version 0.3.0 adds a complete static-web generation and local-preview workflow while preserving the 0.2.0 observer contract. This is software infrastructure, not mathematical admission, a production Nollm integration, or a claim that six dimensions embed injectively in three.

## Quick start

From this directory, with Python 3.10 or later:

```sh
python -m pip install .

# Generate one self-contained workbench and preview it locally.
nollm-viz demo --out study.html --preview

# Generate a static landing page plus both built-in demo workbenches.
nollm-viz site --out preview-site --preview
```

`--preview` writes the artifact first, then starts a local HTTP server bound to `127.0.0.1` and asks the default browser to open it. Press Ctrl-C to stop. Generated workbench pages remain self-contained: no CDN, telemetry, account, or remote service is required.

Generation without a server remains available:

```sh
nollm-viz demo --out study.html
nollm-viz render data.json --out study.html
nollm-viz site --out preview-site
```

## Web generation and preview

### Single workbench

```sh
nollm-viz render data.json --out study.html --preview
nollm-viz render data.csv  --out study.html
```

Each HTML document embeds the complete canonicalized dataset, its SHA-256 fingerprint, and the workbench program. Dataset titles and fields remain data payloads; they are not executed as HTML or JavaScript.

### Static research site

```sh
# No inputs: built-in 65,536-integer hex demo plus 729-state X6 demo.
nollm-viz site --out preview-site

# Multiple user datasets become separate workbench pages under one landing page.
nollm-viz site run-a.json run-b.csv --out comparison-site --title "Experiment comparison"

# Smaller built-in site, with optional X6 omission.
nollm-viz site --out quick-site --hex-count 4096 --no-x6
```

The generated directory contains:

- `index.html` — a responsive landing page with an embedded workbench preview switcher;
- one self-contained workbench HTML per dataset;
- `manifest.json` using `NOLLM_VISUAL_SITE_V1`, recording toolkit version, page name, data kind, record count, and canonical dataset fingerprint.

The landing-page iframe is only an observer/page switcher. It does not merge datasets or rewrite identities. Each workbench can still be opened and distributed independently. For the same ordered datasets and title, site metadata and the landing page are deterministic: no timestamp, host path, or random value is embedded.

### Preview an existing HTML file or site directory

```sh
nollm-viz preview study.html
nollm-viz preview preview-site
nollm-viz preview preview-site --port 8000 --no-open
```

The default is `--host 127.0.0.1 --port 0`; port 0 selects a free local port. Single-file preview is scoped to that HTML file and does not expose sibling files in its directory. Directory preview intentionally serves the selected site directory. Non-loopback binding is rejected unless it is explicit:

```sh
nollm-viz preview preview-site --host 0.0.0.0 --port 8000 --allow-remote
```

That expands the access boundary and should only be used on a trusted network.

## Workbench capabilities

- Hexagonal cells, rotatable A2 cube-plane observation, and explicitly typed layer stacks.
- Six FCC carrier line families / twelve signed rays for supplied X6 coordinates, plus selected-three-coordinate observation and a true slice option. Full six-component records remain available.
- Integer, prime/background, remainder classes, Q16 quotient/remainder, one-unit weight difference, valuation and custom numeric layers.
- Exact coordinate slices, slice animation, camera rotation, coordinate and ID/number lookup, coincident-record cycling, neighborhoods and multiplication trajectories.
- Existing relation edges remain data; filtering is nondestructive. Prime display retains the composite background. Zero valuation is null, not a fabricated finite value.
- JSON and documented CSV round trips, PNG capture, visible-glyph SVG export, and dataset-bound view sessions. SVG does not promise the complete UI, legend or relation overlay. PNG pixels are not an inverse-data format.
- Integer validation, projection collision audit and deterministic data generation. All displayed records are submitted to rendering without sampling; finite screen pixels can overlap.

Optional Matplotlib export remains available with `python -m pip install '.[static]'`.

## Coordinate and observer contract

The hex demo uses `F(4n+d)=2 R60 F(n)+(d&1,d>>1)`, with `R60(q,r)=(-r,q+r)`. Its six nearest-neighbor directions belong to a two-dimensional A2 implementation carrier. `(q,r,-q-r)` is a plane in three display coordinates, not six independent native spatial axes. The synthetic radix depth in the demo is **not** a Nollm physical layer.

For X6, all six signed integer components are required. The six drawing vectors are `(1,1,0)`, `(1,-1,0)`, `(1,0,1)`, `(1,0,-1)`, `(0,1,1)`, `(0,1,-1)`. Their linear sum is a **declared 3D display observer**, not the completed global native/FCC bridge. Native components, IDs, relations and metadata are retained. Multiple identities at one projected center are explicitly grouped, never merged. A three-coordinate observation is not a native slice unless omitted relative components are zero.

This follows the current project boundary in `definitions/00_CURRENT_NATIVE_FOUNDATION.md`, `definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md`, and `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`. Screen coordinates, camera orientation, Euclidean rendering, and web preview do not redefine native axes, metric, time, or Cell identity. No project definition is modified by this tool.

## Data

```json
{"schema":"NOLLM_VISUAL_DATA_V2","kind":"hex","title":"Example","metadata":{},"records":[{"id":"object-A","n":9,"coord":[2,3],"fields":{"score":7}}],"relations":[]}
```

Use `kind: "x6"` and exactly six supplied coordinates for X6. IDs must be unique strings, not row numbers; `n` is optional. Records can contain `layer` and arbitrary JSON metadata. Relationships use existing `source` and `target` IDs. Integer coordinates are limited to ±1,000,000 and the current tool accepts 1–200,000 records; general JSON integers must be exactly representable by browser numbers. These are implementation limits, not native-space limits. Nonfinite floats and incomplete coordinates are rejected.

CSV begins with `#nollm-meta=<JSON>` and columns `id,coord_json,extra_json`. Use the tool exporter rather than an arbitrary flattened CSV. It preserves extra record fields, metadata, relations and nulls. A view-session fingerprint describes its browser-normalized dataset, not a server signature; canonical JSON bytes and original source bytes remain separate provenance. The included SHA-256 fallback is a standard fingerprint implementation, not a cryptographic novelty or authentication mechanism.

```sh
nollm-viz validate data.json
nollm-viz convert data.json --out data.csv
nollm-viz profile data.json --axis s --out slices.json
nollm-viz import-legacy interactive_65536.html --out recovered.json
```

The legacy importer decodes a JSON literal only; it does not execute HTML or JavaScript. The prototype's zero valuation sentinel is repaired to null. The standard-library API is available from `nollm_visual_toolkit`; 0.3.0 also exports `build_site`, `demo_site`, `preview_server`, and `serve_preview`.

## Verification and limits

```sh
python -m unittest discover -s tests -v
```

The 0.3.0 offline regression ran 36 unit tests: 35 passed and one optional Matplotlib static-export test was skipped because Matplotlib was not installed in the current execution environment. All 10 new web-generation/preview tests passed. An installed-CLI smoke also completed `demo -> validate -> site`, checking generated artifacts, dataset fingerprint preservation, and the `NOLLM_VISUAL_SITE_V1` manifest.

The 43 Chromium UI checks recorded for 0.2.0 remain prior evidence for the unchanged workbench front-end logic; they were not relabeled as a new browser certification for this web-shell increment. Native iOS Safari, physical touch hardware, arbitrary third-party datasets, repository-wide CI, live Nollm workloads, and performance at the 200,000-record limit remain **uncertified**.

Large SVG export or frequent animated redraws may be slow. Timing/animation is an observer aid, not simulation of native time. Multiplication trajectories follow declared integer labels; they do not prove that coordinate multiplication implements ordinary integer multiplication. The local preview server is a research convenience, not a production web server.

## Version boundary

- **0.2.0** introduced explicitly typed hex/X6 modes and repaired local zoom, row-index identity assumptions, zero valuation, projection identity loss, and dataset-bound session restoration.
- **0.3.0** preserves those mathematical/observer contracts and adds static-site generation, embedded landing-page preview, a manifest, localhost HTTP preview, single-file access scoping, explicit non-loopback opt-in, and continuous `demo/render/site --preview` workflows.

BRC is `NOT_APPLICABLE` to this HTTP/static-page engineering layer; this increment does not compress or replace the integer, coordinate, valuation, relation, or other mathematical carriers.

License: MIT, inherited from Enterprise Math.
