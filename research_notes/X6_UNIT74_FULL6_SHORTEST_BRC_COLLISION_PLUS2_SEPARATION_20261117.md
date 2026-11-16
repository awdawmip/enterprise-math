# Unit74 — full native X6: equal shortest positive BRC need not preserve the next all-length coefficient

Date: 2026-11-17. Parent: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Exact Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Author-side science: **AUTHOR-EXACT / SCOPED-ORIGINAL-EXECUTED / FINITE-EXHAUSTIVE-CUBE / UNREVIEWED / NOT_ADMITTED**.

Scientific source is frozen native P000 V5 signed six-axis Cell torsor at `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`. Historical comparison source: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Native BRC implementation: `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, exact frozen Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. Six signed axes are **all native**, not a three-axis independent plane.

## Exact new obstruction and counterexample

For a raw signed displacement `z ∈ Z^6` from a fixed Cell anchor, let `h=min(z)`, `r=z-h·1_6`, `G=Σz_i²`, `T=Σ|z_i|`. The passive observer is `O_6(z)=(r,G,T)`. Put

`A=(-6,-6,-2,2,2,7)`; `B=(-5,-5,-1,3,3,8)=A+1_6`.

Both have **exactly the same** `r=(0,0,4,8,8,13)`, `G=133`, `T=25`; their depths are `-6,-5`. In fact `R=Σr_i=33`, `Q=Σr_i²=313`, `D=R²+6(G-Q)=9`; the two integer roots `h=(-R±√D)/6` are exactly `-6,-5` and satisfy the same `T`. Their absolute coordinate multisets differ:

- `sorted(|A|)=(2,2,2,6,6,7)`.
- `sorted(|B|)=(1,3,3,5,5,8)`.

Nevertheless both exact **positive natural** shortest signed-path BRC multiplicities equal

`C_25(A)=C_25(B)=25!/[ (2!)³(6!)²7! ]=25!/[1!(3!)²(5!)²8!]=742096122768000`.

The first longer permissible original native path count already separates them:

| Original frozen `endpoint_multiplicity` | A | B |
|---|---:|---:|
| shortest length 25 | 742,096,122,768,000 | 742,096,122,768,000 |
| length 27 (one reverse pair) | **734,913,692,436,924,000** | **752,485,468,486,752,000** |

The exact positive gap is `17,571,776,049,828,000` (B minus A). Thus even on the *complete native signed six-axis X6*, passive `(can6,G,T)` plus the **exact shortest positive N-BRC mass** does not determine the next uniform positive path-multiplicity coefficient. A consumer requiring all-length native BRC cannot elide the missing depth merely from shortest-mass equality. This strengthens Units69–73 and is a concrete LP019/023/026 operation-safe obstruction; it does **not** assert an unlocated historical wrong call site.

## General first-return coefficient law (all six signed axes)

For any `z∈Z^6`, write `a_i=|z_i|`, `T=Σa_i`. Each length-`T+2` word reaching `z` inserts exactly one cancelling signed `+e_i,-e_i` pair for one of the six named axes. The frozen native `endpoint_multiplicity` formula, with `K=1`, gives the exact integer identity

`C_(T+2)(z) = C_T(z) · (T+1)(T+2) · Σ_{i=1}^6 1/(a_i+1)`,

where `C_T(z)=T!/Πa_i!`. Every summand is a **nonnegative count**, not signed cancellation. For A, the sum is `79/56`; for B, `13/9`, proving the two distinct length-27 counts above. All coefficients and the identity are exact, no floating approximation. This is a simple first-excess specialization of the pre-existing all-excess formula, not claimed as a new all-length counting theorem. **The new scientific contribution is the explicit full-X6 nonfactorization witness and its bounded-smallest classification.**

## Finite sharpness in a declared cube

Enumerated *all sorted* six-component integer triples (six-tuples) `a_1≤...≤a_6`, each component in `[-M,M]`, for `M=1,...,8`. If `a` and `b=a+c·1_6` are distinct and share exact `G`, then `c=-Σa_i/3≠0`; exchange endpoints to take `c>0`, which requires `Σa_i<0` divisible by 3. Translation preserves sorted order, so every axis-permutation class is represented. For each candidate ensure both lie in the cube, `T(a)=T(b)`, exact factorial shortest BRC equality, and differing multisets `sorted(|a|)≠sorted(|b|)`. This is a complete finite exhaustiveness argument, not an infinite minimality claim.

No such exceptional pair occurs for any `M≤7`. At `M=8`, exactly **two sorted directed pairs** appear, related by simultaneous sign-reversal and endpoint exchange:

`(-8,-3,-3,1,5,5) -> (-7,-2,-2,2,6,6)`, and
`(-6,-6,-2,2,2,7) -> (-5,-5,-1,3,3,8)`.

The exact census for `M=1,...,8` is in the attached JSON certificate. This certifies `M=8` as the smallest integer sup-norm cube admitting a full-X6 *equal shortest mass / differing absolute multiset* double-depth pair, up to the enumerated permutation orientation. The theorem about failure of all-length factorization is established by the explicit pair alone.

## Genuine source execution and reproducibility

Executed a separately written exact integer enumerator and the **original frozen module itself**. The original local source was byte-for-byte verified using its Git blob SHA1 `300a96e3dc24bf6fff73743037a0347a8bc83176`; then actually invoked its `spatial_norm_squared`, `shortest_event_count`, `shortest_path_multiplicity`, and `endpoint_multiplicity` on A and B. Its first excess matched the independent K=1 combinatorial oracle and the reciprocal formula. The complete bounded census and witness checks were executed under standard Python, `-O`, and `-OO`, yielding identical certificate SHA256 `95d626065ff47de4ea5710352d6c0c8102a3b5b9e49f124bee73795b59c51129`; zero failed guards. This is an original-source **two-endpoint scoped** check and an independent finite census, not a rerun of frozen R063/Helly full benchmarks.

Checker: `research_checks/X6_UNIT74_FULL6_BRC_COLLISION_PLUS2_CHECK_20261117.py` (run as `python checker.py /path/to/exact-frozen/signed_brc.py` to engage and hash-validate original module); JSON: `research_checks/X6_UNIT74_FULL6_BRC_COLLISION_PLUS2_RESULTS_20261117.json`.

## Native/Source and parent frontier

Prior Source semantic request `onhour-20261117-0259-x6-unit69-71-native-progress-v1` was independently read as `SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED`, actual commit `0c1fdb23d6566f8bb74f96759099899016d015d7`. The same Research lane SID `MCP-082892eb480e45dea6d4b9fcc0491034`, Researcher `EM-X6-FB6990`, CLAIM `MCP-579c8e23625448582b421831`, RUN `RUN-fb25028676f9692ab1bacaee` has original authenticated resume `onhour-20261117-0430-x6-own-run-resume-after-unit72-v1` `SUCCEEDED / RUN_READY` generation3. **Native Units72–73** original request `onhour-20261117-0447-x6-unit72-73-native-semantic-progress-v1` was last observed **RUNNING / WAIT_ORIGINAL**, and new own read-only continuation request `onhour-20261117-0432-x6-source-continuation-v1` was QUEUED; preserve both original IDs and reconcile their actual effects rather than duplicate publication. This Unit74 author-side evidence must obtain its **separate current native semantic checkpoint** only with real source-validated current execution authority.

Remaining mother work: exact historic LP011 wrong native singleton dominant-axis caller and LP019 allegedly subtracting positive native N-BRC mass still `UNRESOLVED_PROVENANCE`; finish 28-LP actual downstream consumer census and independently owned Driver `REQUEST_REVISION`. Do not mutate accepted R063, frozen input, P000, maintenance lane identity, original schedule/notifications, or already verified work.
