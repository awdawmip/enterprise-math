# X6 LP003/LP011/LP026 current fixed Cell-slice consumer: exact sharp metric distortion

2026-11-14, TASK_RESEARCH author-side second scientific unit. Parent `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Model: registered **fixed two-generator source chart** `Z^2`, not arbitrary signed native `Z^6`. `UNREVIEWED / NOT_ADMITTED`, original-code exact check PASS. No original native benchmark target is replaced.

## Real current consumer and immutable code evidence

The current main source files were read through the connected GitHub path, with observed original blobs:
- `src/enterprise_math/_cell_slice_codec.py` SHA1 `2aa70d8f8509dc31d73f6891b97f9fdf7377df2a`, functions `encode` lines 11–24, `decode` lines 27–37, and `code_step` lines 40–65.
- `src/enterprise_math/cell_address.py` SHA1 `fc77f374ed8b7948dac2d5a0bfcad87ee828e97b`; explicit `FRAME = X6_FIXED_E1_E2_CHART`, `encode_raw_slice` 75–79, `decode_raw_slice` 81–83, `step_cell` 85–89, `cell_squared_distance` 91–93 and `cell_step_distance` 95–99.
- `src/enterprise_math/geometry.py` SHA1 `a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152`; `l1_distance` uses exact raw integer-coordinate differences.

The public six-digit `FinalCellAddress` is a registered representation of the selected **two-dimensional** chart. The current `cell_step_distance` correctly decodes before using the native-coordinate L1 backend; it does **not** take L1 of the six public digits. This is a real downstream consumer typing confirmation, not proof of complete X6 signed-native injectivity or full LP ledger closure.

## New theorem: globally sharp two-sided metric distortion of the actual codec

Let `F(m,n)=(a,b,c,0,0,0)` be exactly the three-region `_cell_slice_codec.encode`, and `d_2` and `d_6` be standard integer L1 distance on the source pair and six public digits respectively. For **all** `p,q∈Z²`:

```text
(1/2) * d_2(p,q) <= d_6(F(p),F(q)) <= 3 * d_2(p,q).
```

Both constants **1/2 and 3 are attained**, hence are sharp for this actual registered codec. Neither six-digit L1 is the exact source metric nor are these inequalities a general all-X6 native geometry statement.

### Universal upper bound

Set `p=(m,n)`. Direct case reduction of the original three-region encoder gives the equivalent exact formulas

```text
a=max(0, m+max(-n,0))
b=max(0, n+max(1-m,0))
c=max(0, 1-min(m,n)).
```

Each of `a,b,c` changes by at most one under any single primitive source step `±e1,±e2` (because `min`, `max` and unit affine changes are 1-Lipschitz in each stepped variable). Thus every source edge changes the public code by at most three in L1, and summing along a shortest source path yields `d_6(Fp,Fq)<=3d_2(p,q)`.

### Universal lower bound

The original decoder has three disjoint valid-code cases: `A:a=0,b,c>=1` with `(m,n)=(1-c,b-c)`; `B:b=0,a,c>=1` with `(m,n)=(a+1-c,1-c)`; `C:c=0,a,b>=1` with `(m,n)=(a,b)`. For two codes in the same case, direct coordinate difference and triangle inequalities give `d_2<=2d_6`. For cross-cases:
- `A/B`, with `t=c_B-c_A`, `d_2=|t-a_B|+|t+b_A-1|<=2|t|+a_B+b_A<=2d_6`.
- `A/C`, `d_2=(a_C+c_A-1)+|b_A-c_A-b_C|<=a_C+|b_A-b_C|+2c_A<=2d_6`.
- `B/C`, `d_2=|a_B+1-c_B-a_C|+(b_C+c_B-1)<=|a_B-a_C|+b_C+2c_B<=2d_6`.
This exhausts source points by the exact decoder regions. Hence `d_6(Fp,Fq)>=(1/2)d_2(p,q)` for every pair.

### Witnesses of sharpness

```text
p=(-1,-1) -> F(p)=(0,1,2,0,0,0)
q=( 0, 0) -> F(q)=(0,1,1,0,0,0)
source L1=2; public-digit L1=1 (lower constant 1/2).

p=(-1,-2) -> F(p)=(1,0,3,0,0,0)
q=(-1,-1) -> F(q)=(0,1,2,0,0,0)
source L1=1; public-digit L1=3 (upper constant 3).
```

## Exact original-source execution

The original `_cell_slice_codec.py` **complete source body** was locally reconstructed from current GitHub bytes and independently checked using `git hash-object`: **`2aa70d8f8509dc31d73f6891b97f9fdf7377df2a`**, exactly the GitHub current blob. The newly executed `research_checks/X6_LP003_FIXED_CELL_SLICE_SHARP_METRIC_DISTORTION_20261114.py` verifies the original dependency's blob before loading its original `encode/decode/code_step`.

Actual execution: **`PASS_X6_LP003_FIXED_CELL_SLICE_SHARP_BILIPSCHITZ_ORIGINAL_CODEC`**, exit 0; 6,724 primitive directed edges on `[-20,20]^2` (public code edge-distance counts `{1:4080,2:2563,3:81}`); 25,200 unordered pairs in `[-7,7]^2`; two exact sharpness witnesses; zero mismatches. The new checker local SHA256 `85e760cf8df94cb28ebe48aa248b6d1c4f3a0ade1740a6a27d84b215077da03e`, Git blob `0133e8784c5b4caa083e866c9b1143110fecbb3a`, publication commit `acb52ea8b83703d80fabec619580683ee6fd09c4` read back with identical blob. Finite tests corroborate; **the all-pair theorem follows from the preceding exact universal derivation**, not from extrapolating the grid.

## Current consumer disposition and continuing Source obligations

- **KEEP / TYPED_FIXED_CHART**: `cell_address.py` correctly validates the six-digit registered fixed slice and decodes before distance. Misusing six-digit raw L1 as native distance would incur a sharp distortion factor (1/2 to 3), so native signed `Z^6` calls still require an actual typed embedding, not an implied identity.
- No identified **wrong** current call site or justified repository patch in these three original modules; no accepted frozen output edited. This new bound is not the unresolved historical LP011 signed-native `argmax|delta|` wrong caller, nor LP019 positive BRC signed-cancellation wrong caller.
- Parent frontier: frozen P000 V5 and old `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, existing R061/R062 positive BRC and R063 PathSqrt, current 28-LP crosswalk, previous original signed/coordinate 115,513 assertions, and the same-turn five-file frozen LP019 feedback/cycle typed audit already GitHub-published. Do not re-prove them.
- Current unfinished objective: remaining actual X6 native signed call-site provenance/consumer graph, LP011/LP019 exact wrongful caller if it existed, and independent Driver `REQUEST_REVISION`; support/native semantic checkpoint is separate from this author-side note.
- Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`; original source Researcher `EM-X6-FB6990` SID `MCP-082892eb480e45dea6d4b9fcc0491034`. New continuation read original request `onhour-20261114-0608-x6-source-continuation-v1` was still `RUNNING / WAIT_ORIGINAL` at last same-turn observation; no new winning CLAIM was inferred or posted. Reconcile the original request, then authorize subsequent native action using its exact claim/CAS. Never use the maintenance conversation identity.
- Next **new** science target: precise active/frozen downstream caller of R061/R062 min-zero, `Sigma_O^(ij)`, positive N-BRC or PathSqrt when consumed as **signed native X6**; verify exact file/line/types before any correction. Retain the frozen benchmark and missing provenance as open rather than replaced.

This is an author-side mathematical and Source provenance artifact only; no Native PROGRESS, independent review, Result, P000 or task scheduler change is asserted.
