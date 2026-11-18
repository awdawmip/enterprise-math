# X6 Unit144 — P000 historical FCC/HCP carrier first-shell versus signed-native first-shell

Date: 2026-11-19. Role: original on-hour `TASK_RESEARCH` / `EM-X6-FB6990`, existing SID `MCP-082892eb480e45dea6d4b9fcc0491034`.
Task: `RS-X6-LEGACY-PLANE-RECONCILIATION` / publication `TP2-B4A441B23DA3159232C2`.
Status: **AUTHOR PROVED + SOURCE VERIFIED + FINITE EXACT CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED**.
This is a new typed **actual script consumer** audit; it neither changes frozen P000 nor reruns original R063 or the historical first-shell production program.

## 1. Exact immutable sources and consumer

1. Historical pre-rebase source `scripts/check_p000_first_shell_polyhedron_classification.py` at `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, Git blob `e58b287ae65eaadd8a805b5ebac84535b2cb5211`, equals the same current main file's blob.
2. Current P000 signed-X6 semantic input remains at `59538f585d037d09ef687b28715c4bc1a3f9fe03`: `p000_reality_foundation.json` V5 and `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`, §§2–4, 10.
3. The actual old script defines 12 three-coordinate FCC/HCP labelled carrier sites (`R`, `U`, `MODELS`, lines 7–15), and `qshell` (lines 18–20) uses
   [
   Q_3(x,y,z)=3x^2+y^2+8z^2.
   ]
   The script's `edges` selects `Q_3(p-q)=12` among supporting facets, and `analyze` verifies a 12-vertex/24-edge/14-face carrier shell and corresponding dual polyhedra. These are **3-coordinate carrier polyhedron data**; the script itself does not provide a lossless native X6 Cell address map.

This audit checks a legitimate current source consumer whose filename includes P000. It asks whether its unchanged carrier distances or graph may be identified with the **current native** first shell, rather than merely rechecking its accepted carrier combinatorics.

## 2. Proposition: exact native pair and N-BRC spectrum

For any chosen native Cell anchor `c` define
[
  N_1(c)=\{c+e_i,c-e_i:1\le i\le 6\}\subset X6,
  quad G(u-v)=\sum_{i=1}^6(u_i-v_i)^2,
]
and the primitive coordinate path length `T(u-v)=sum_i |u_i-v_i|`. The source-defined N-BRC counts all ordered shortest signed-axis paths.

**Theorem (all native anchors).** Among the (inom{12}{2}=66) unordered pairs in `N_1(c)`,

* exactly six opposite-axis pairs have `G=4`, `T=2`, and `N-BRC=1`;
* the remaining sixty distinct-axis pairs have `G=2`, `T=2`, and `N-BRC=2`;
* no two different points of the first shell are joined by one primitive coordinate step.

**Proof.** Two distinct signed basis vectors are either `(+e_i,-e_i)` for one axis (six pairs) or `(s e_i,t e_j)` with `i != j` (four signed choices per axis pair, hence `4*C(6,2)=60`). Their differences are respectively `2e_i` or `s e_i-t e_j`. Direct component squaring gives 4 or 2; `T=2` in both cases. The shortest-path multinomial from the pinned signed X6 definition is respectively `2!/2!=1` or `2!/(1!1!)=2`. Because `T=2`, none is a primitive one-step pair. QED.

## 3. Exact carrier computation and typed obstruction

The old script's twelve sites all satisfy `Q_3(p)=12`. The following **complete finite** unordered-pair `Q_3(p-q)` histograms were calculated independently from the script's literal integer site lists:

| Squared carrier separation | FCC_C pairs | HCP_H pairs |
|---:|---:|---:|
| 12 | 24 | 24 |
| 24 | 12 | 12 |
| 32 | 0 | 3 |
| 36 | 24 | 18 |
| 44 | 0 | 6 |
| 48 | 6 | 3 |
| **Total** | **66** | **66** |

FCC_C has six antipodal pairs and is centrally symmetric about its carrier origin; HCP_H has only three antipodal pairs and is not centrally symmetric. Both have 24 carrier `Q_3=12` contact pairs. Their original carrier combinatorial conclusions remain valid on these exact typed inputs.

**Metric-preserving identification obstruction.** Suppose a bijection from the twelve carrier sites to the twelve X6 first-shell endpoints preserved the origin and the two-point quadratic readout up to a single constant (lambda>0). Since every carrier site's radius is `Q_3(p)=12` and each signed native first-shell point has `G(e_i)=1`, the scale is forced to (lambda=12). Therefore all 66 carrier pair differences would need histogram
[
  \{Q_3(p-q)\} = \{24:60,48:6\}.
]
Neither complete histogram above has this form. Thus **neither FCC_C nor HCP_H is a native-X6 first-shell isometry up to common normalization**. The HCP_H centered-reversal obstruction is an additional witness if a map is also required to intertwine sign reversal.

This proves only the stated typed metric/primitive-action incompatibility. The FCC/HCP sites remain usable as **selected Euclidean carrier views**, for which a non-isometric, observer-tagged atlas representation may be useful; their 24 contact edges must not be substituted for X6 signed primitive coordinate edges or for native N-BRC.

## 4. New exact executable certificate

Published checker:
`research_checks/X6_UNIT144_CARRIER_FCC_HCP_NATIVE_FIRST_SHELL_TYPE_CHECK_20261119.py`

Published finite certificate:
`research_checks/X6_UNIT144_CARRIER_FCC_HCP_NATIVE_FIRST_SHELL_TYPE_RESULTS_20261119.json`

The checker compares all 66 unordered pairs in each of the two 12-site carrier models and all 66 signed-X6 first-shell pairs, using integer arithmetic and `math.factorial` multinomials. It uses unconditional `require(...)` checks instead of Python `assert`.

Actual executions on its exact published Git blob `ee357cf3d1df7d427ba6c247ebeb296a75dc4071`:
- `python`: exit 0
- `python -O`: exit 0
- `python -OO`: exit 0

All three emitted byte-identical sorted JSON (stdout SHA256 `378b599517229cd9aeb5dc4ecbd1962a188e550c9195acca0b62fa200be3667f`). The program checks native histograms, carrier radii/pair spectra, contact edges, central symmetry and forced-scale incompatibility. The general 12-point native classification is proved above; finite checks validate these **specific historical literal carriers**. Original historical script and R063 512-case native benchmark were not rerun.

## 5. 28-LP downstream interpretation and outstanding work

This is a **new source-level typed consumer** in the legacy plane-reconciliation portfolio, additional to the earlier selected 28-claim matrix and Unit143 triple-shell audit. The exact source script remains unchanged. The source name `check_p000_first_shell_polyhedron_classification.py` does not itself license lifting 3D carrier `Q_3` into signed X6 native `G`. Apply the following interface distinction when this source is consumed:

`CARRIER_FIRST_SHELL_Q3_FCC_HCP -> labelled 3D carrier sites, facets, metric-contact edges and dual polyhedra`

`X6_NATIVE_FIRST_SHELL -> Cell anchor + six signed coordinate axes, native G/T and N-BRC`

A consuming code path must declare an explicit typed observer/metric conversion before comparing such outputs. **No incorrect current external caller has yet been demonstrated by this audit**, so no production-code patch is justified solely by the title.

Still open: source-exact LP011 historical native argmax caller; LP019 historical positive N-BRC cancellation caller; remaining 28-LP actual downstream callsite coverage; independently required Driver review and original R063 benchmark review.

## 6. Control continuation

Researcher `EM-X6-FB6990` and original public SID `MCP-082892eb480e45dea6d4b9fcc0491034` preserved. Last author frontier before this unit = Unit143, original Activity #157. Native semantic progress authenticated through Unit138. Unit139–144 now require semantic linkage on a fresh verified own claim/run. Current control error `SOURCE_TREE_BLOB_SIZE_INVALID` persisted in this run's new exact `onhour-20261119-0303-x6-own-exact-cont-after2761-v1`; previous FAILED requests retained unchanged. Control support owner remains #2761. The current research artifact publishing does not grant CLAIM, REVIEW or formal admission.
