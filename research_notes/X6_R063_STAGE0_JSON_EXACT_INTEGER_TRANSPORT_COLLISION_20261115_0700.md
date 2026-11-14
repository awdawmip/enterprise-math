# X6 / LP019 / R063 Stage 0 — Loss of exact positive path counts under binary64 JSON decoding (2026-11-15)

## Scope and immutable evidence
Mother task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`, Researcher `EM-X6-FB6990`, own SID `MCP-082892eb480e45dea6d4b9fcc0491034`. This is an **author-observed data-transport counterexample**, not a modification or execution of the original Python R063 benchmark, not an independent Driver review, and not a mathematical acceptance.

Frozen historical owner branch: `research/r063-stage0-path-valued-sqrt-2500`. Source pinned loader blob `b4e000a6377f2858ae434eb0eecd0c25c33e8592`; five ordered parts: `4a69c4d698887bce56323f393cb979609ce4ab0a`, `913078c642b8995bfc135ef0350912387a17cdb8`, `b543e185ec415b512c0ca0421616404cc12a19a7`, `4f1bbf72abed19dc7dc605371872ee31c501cebe`, `a1834a4b39a9d528760e67220b5fe5f368c9e655`.

Exact frozen output artifacts read by authenticated GitHub connector:
- `research_results/R063_STAGE0/R063_STAGE0_PATH_CARDINALITY_CERTIFICATE.json`, blob `d4278d6c301587330252ff6683e87773d42cf4e2`;
- `research_results/R063_STAGE0/R063_STAGE0_REPLAY_SUMMARY.json`, blob `f9d0598dbb410d892b5a03ec00b6baa8b7f1e7ad`;
- `research_results/R063_STAGE0/R063_STAGE0_GENERAL_SQUARE_REGRESSION.json`, blob `0a5627760b960ac1a139b20eedea43664a0fb900`;
- `research_results/R063_STAGE0/R063_STAGE0_DISCOVERY_PHASE_FROZEN.json`, blob `d0bcb21ce0ab4ca86fbe041682dbf3b699affd6a`;
- `research_results/R063_STAGE0/R063_STAGE0_COMPONENT_ROOT_FIBER.json`, blob `fcc8923cf99342650e321d65786cf605a9ac6a07`;
- `research_results/R063_STAGE0/R063_STAGE0_MISMATCHES.json`, blob `6ba6d4dbf7aa45ef9a44ecd5e1257cc6af4601c6`.

## Exact counterexample / observer boundary

The original Python JSON certificate stores exact decimal integer tokens. At `N=2500, r=50`, its six ordered nonnegative component roots are `(0,50),(14,48),(30,40),(40,30),(48,14),(50,0)`. Their path multiplicities are respectively

```text
1
29078984349975
55347740058143507128
55347740058143507128
29078984349975
1
```

These are the exact binomial values `C(a+b,a)`. Their exact sum is **110695538274255714208**. The original Python source `part02.inc` uses integer `math.comb`; the `part04.inc` total gate is exact on those Python integers. The source artifact's decimal tokens agree with this exact sum.

A consumer using standard ECMAScript `JSON.parse` converts JSON numbers to binary64 `Number`. Extracting the exact integral value represented by that Number via `BigInt(parsedValue)`, the two large branch counts become **55347740058143506432** (each **696 below** the source), while the total becomes **110695538274255716352** (**2144 above** source). Converting the decimal *display string* of a rounded Number is not an exact recovery method. The two small non-axis counts `29078984349975` remain exactly representable; the larger fields exceed `Number.MAX_SAFE_INTEGER = 9007199254740991`.

A deliberately important witness: `JSON.parse(raw).branches.reduce((a,b)=>a+b.cardinality,0) === JSON.parse(raw).one_sector_total_path_cardinality` evaluates **true** in the tested ECMAScript consumer, although the parsed values are not the original integers. A floating checksum therefore cannot certify the exact path/N-BRC mass. Reinterpreting the already-rounded `Number` as `BigInt` cannot restore the lost integers.

This is an exact and reproducible type-level information loss in the **downstream JSON-number observer**, not a mathematical error in the original Python R063 certificate and not signed cancellation of positive N-BRC. It identifies an actual unsafe consumer path for LP019 provenance preservation.

## Lossless adapter and bounded reproducibility

1. Read the original UTF-8 JSON bytes and verify the pinned Git blob SHA1. Before conversion to binary64, preserve each decimal integer lexeme as an arbitrary-precision integer (e.g. Python standard `json.load` with integer parser, or a true lossless JSON integer parser). A JSON Schema may instead declare large exact counts as decimal strings in a *new explicitly versioned derivative* while retaining the original frozen artifact intact.
2. Validate each `(a,b)` with `C(a+b,a)` using arbitrary-precision arithmetic and compare the exact six-value sum with `110695538274255714208`. Retain the ordered component identities, trace IDs, path certificate provenance and signed-X6/positive-sector distinction. Never claim that the 2-generator R063 output exhausts the native six-axis P000 world.
3. As an independently checked original-artifact readback, the frozen regression JSON records `r_range=[1,512]`, `tested_r_count=512`, zero C3/C4/combined mismatches and rows digest `51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae`. The frozen summary records all 17 original gates true and discovery digest `6dd26e75436fb6740134590fc243b59ab9eb287cadbc46d417d5bbbb74022f0d`. These are historical artifact observations; no current native replay was run.

## Mother-task handoff

- **Completed:** concrete exact positive BRC integer loss in the JS JSON observation, with real frozen source bytes, six witnesses, and a self-consistent wrong Number checksum. Exact arbitrary-precision observer validation executed in the research turn. `AUTHOR-VERIFIED / UNREVIEWED / NOT_ADMITTED`.
- **Open:** original R063 Stage 0 same-object Python replay under `--N 2500 --regression-max-r 512` on an authorized runner, with unchanged historical six source blobs; execution support [#2416](https://github.com/awdawmip/enterprise-math/issues/2416) remains unassigned as at the checked issue snapshot. LP011 historical incorrect argmax caller, LP019 purported historical signed-positive-count cancellation caller and 28-LP remaining dependencies remain `UNRESOLVED_PROVENANCE`. Independent Driver revision remains open.
- **Do not redo:** original historical accepted 512-case certificate, author-proved LP011 L3 theorem, V2 K4 sign/positive-BRC separation, or completed Source units #1–#25.
- **Next:** original authorized repository runner executes exactly the pinned Python code and enforces its 17 gates, 512 coverage and N=2500, then a **lossless integer** check of output cardinalities; retain output filenames/SHA256 and report native exit. Separately trace uninspected PR-only/current dynamic LP011/LP019 callers with exact source typing.
- **Source continuity:** own SID `MCP-082892eb480e45dea6d4b9fcc0491034`, Researcher `EM-X6-FB6990`, winning claim `MCP-30a8f5fd123215e08bd4a7cf`, run `RUN-3356cbe3c2b4916d79399941` as previously observed. Current authorization requires fresh Source resume; last native publication request `onhour-20261115-0617-x6-lp011-l3-and-v2-gauge-activities41-42-progress-v1` is `SUCCEEDED` with 25 units; exact continuation read `onhour-20261115-0700-x6-current-continuation-v1` was consumed, and neither its readback nor this note creates a fresh CLAIM.
