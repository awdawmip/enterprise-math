# R061 Stage 1R — Reproducibility Proof

Task-ID: `RS-R061-STAGE1R-NATIVE-LINE-TRACE-CHECKER-REPLAY`  
Taskbook source: `2fd179aa22db7fdc292817f24cb7f65008eb4b16`  
Owner branch: `research/r061-stage1r-native-line-checker-replay`

## Executable replay

Exact checker command sequence used in this replay:

```text
python3 scripts/r061_stage1r_validate_native_line_trace.py --out research_results/R061_STAGE1R --phase native
python3 scripts/r061_stage1r_validate_native_line_trace.py --out research_results/R061_STAGE1R --phase stage0
python3 scripts/r061_stage1r_validate_native_line_trace.py --out research_results/R061_STAGE1R --phase finalize
```

Exit statuses: `native=0`, `stage0=0`, `finalize=0`.

The checker is self-contained. It does not read the Stage 1 summary or copy old
digests as generated values. Frozen/claimed digests are comparison targets only
after the corresponding datasets have been independently regenerated.

The checker also provides an all-phase re-exec mode, but this recorded replay
used the three explicit phase invocations above so that each phase exit status
is independently auditable. The phases are memory-isolated and share only the
checker's freshly generated temporary certificates; no Stage 1 result artifact
is read as an input.

## Stage 0 frozen regression replay

- coordinate fiber `N=0..100000`: `0f4bccc2ff3fd7e7ae22ccd9e4abf248cf215bffea7bdd02aabca9b8c2bb8338`
- coordinate frozen-hash match: `True`
- Euclid square-hypotenuse audit through `r<=4096`: mismatches `0`
- explicit shuffle through `a+b<=22`: `8388607` words
- explicit shuffle SHA256: `572562117dbc2ba388543fbbeaa73bd26359ef47c26ef7ff31314ee92b318f93`
- shuffle frozen-hash match: `True`
- compressed Pascal through `a+b<=512`: `780c833ed685c707b2e57d70a2ecf015e56bc5196ee8e62a646720eb0707d002`
- Pascal frozen-hash match: `True`

## Origin / affine replay

- incident cells at `O_E`: `3`
- exact pairwise center spacing: `True`
- exact origin radius squared `1/3`: `True`
- no fourth boundary center: `True`
- exactly one anchor per open 120-degree sector: `True`
- affine typed replay mismatch count: `0`

## Native trace replay

- pair count: `190`
- formal linearizations: `524287`
- three-sector paths: `1572861`
- replay SHA256: `359474ba6b53ffbb3c326cf331d55dd3ed098837451a46b0754926b7c642d702`
- replay claimed-hash match: `True`
- non-neighbor transitions: `0`
- endpoint errors: `0`
- sector-prefix errors: `0`
- duplicate trajectories within trace pair: `0`

Compressed trace SHA256 through `a+b<=256`:

`aa0e3761f7446cf89e782c74b8020157b41713a37022daf44a2f8e95179e4ead`

Claimed compressed-hash match: `True`.

## Structural replay

- third-direction `(1,1)` classification: `CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE`
- local commuting diamonds tested: `570`, mismatches `0`
- axis identities through radial 18: `57`
- adjacent-sector axis trajectory duplicates: `0`
- scaling cases through parameter 8: `729`
- concatenation cases through parameter 8: `6561`
- commutation-closure words explicitly checked through total 16: `131071`
- composition mismatches: `0`

## N=25

Generated branch counts:

- `(3,4)`: `35`
- `(4,3)`: `35`
- `(0,5)`: `1`
- `(5,0)`: `1`
- fixed-sector total: `72`

## Final result

`STAGE1R_REPRODUCIBILITY_PASS = true`

Mismatch count: `0`.

The committed executable replay reproduces every material Stage 1 deterministic claim required by the Stage 1R taskbook. Stage 1 may return to Driver for final acceptance.

No Stage 2 is opened.
