# X6 / LP019 / R063: exact signed three-axis G=2500 shell (2026-11-15 08:00)

## Scope and original source boundary

Parent task: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`; Researcher `EM-X6-FB6990`, original session `MCP-082892eb480e45dea6d4b9fcc0491034`. Frozen mathematical input: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`, P000 V5 and centered signed three-axis slice. Historical comparison: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. The original R063 Stage 0 two-generator positive-chart path certificate is pinned on branch `research/r063-stage0-path-valued-sqrt-2500` at `research_results/R063_STAGE0/R063_STAGE0_PATH_CARDINALITY_CERTIFICATE.json` (blob `d4278d6c301587330252ff6683e87773d42cf4e2`).

This note is a NEW independent exact signed-slice calculation, not the original R063 Python C3/C4 512-case replay, not the full six-dimensional X6 shell and not an admitted result. It does not supersede or modify the accepted historical positive two-generator certificate.

## Mathematical object and result

Fix one ordered native-axis triple S and its Cell anchor. Embed `(x,y,z) in Z^3` into `Z^6` with exactly zero displacement in the other three coordinates. The exact native squared norm and shortest signed-axis word multiplicity are

`G(x,y,z)=x^2+y^2+z^2` and `B(x,y,z)=(|x|+|y|+|z|)!/(|x|! |y|! |z|!)`.

For `G=2500`, the complete signed selected-slice shell has **150 distinct native Cell endpoints**, and its exact total shortest-word mass is

`M_3(2500)=26860799510260072787603759892561716013678`.

Every endpoint belongs to exactly one of the following sorted absolute-coordinate orbits:

| sorted abs triple | endpoints (signed/permuted) | B per endpoint | orbit B mass |
|---|---:|---:|---:|
| (0,0,50) | 6 | 1 | 6 |
| (0,14,48) | 24 | 29078984349975 | 697895624399400 |
| (0,30,40) | 24 | 55347740058143507128 | 1328345761395444171072 |
| (18,24,40) | 48 | 146667819424252202137117683587961000 | 7040055332364105702581648812222128000 |
| (24,30,32) | 48 | 559453321977660597511933995509550527400 | 26853759454927708680572831784458425315200 |

In particular, the endpoint population partitions by number of nonzero selected native components into `6 + 48 + 96 = 150`. The support-at-most-two B mass is only `1328346459291068570478`; **96 genuine three-axis endpoints** carry the remaining `26860799510260072786275413433270647443200` shortest signed words.

## Exact proof and bounded executable certificate

All integer solutions with `x^2+y^2+z^2=2500` have `|x|,|y|,|z| <= 50`. Sorting the three absolute coordinates gives `0 <= a <= b <= c <= 50`. Since 2500 is divisible by 4 and each square is 0 or 1 modulo 4, all three coordinates must be even; equivalently we enumerate `a'^2+b'^2+c'^2=625`. Exhaustively testing `a,b=0,...,50` and `c=isqrt(2500-a^2-b^2)`, retaining exact perfect squares and enforcing sorted order yields precisely the five listed orbits. Their sign/permutation orbit sizes are 6,24,24,48,48, respectively. These finite exact integer checks prove exhaustive shell coverage.

For a fixed signed endpoint, all shortest words use each signed primitive axis exactly the required absolute number of times, with no opposite-direction backtracking. The multinomial coefficient above is therefore exact, and summing its five orbit contributions proves the stated total.

Independent executed pure-Python check: `research_checks/X6_R063_N2500_FULL_SIGNED_SLICE_SHELL_CHECK_20261115_0800.py`, committed at `64db15e57c61eb1e0a8c1be28e69673c8f3160e0`, Git blob `9383b6ad10fdbe5980c3f7b7f3ecb135a10a1af0`, SHA256 `96ea4cfa115e0113bb95a685a9624b8edf8f221bdc15373868f044e6416dad84`. It builds the full signed shell, independently groups by signed/permuted orbits, checks every integer contribution, and first verifies the frozen `G=25` regression of 30 endpoints and mass 846. The actual local run exited 0 and emitted `PASS_X6_R063_N2500_SIGNED_Z3_SHELL_NOT_ORIGINAL_BENCHMARK`. This code and report are author-side research, not a claimed native R063 program execution.

## Preserved source/observer distinctions and task residual

The original two-generator positive-sector `N=2500` R063 certificate has six ordered positive component roots with exact total `110695538274255714208`. That is a typed restricted chart path mass, not the 150-endpoint signed selected three-axis shell. The earlier six-axis all-pair root inventory (252 signed endpoints across pairs) also has a different population and must not be interchanged with this single fixed three-axis `Z^3` shell. Do not silently erase path branch identity, sign, selected axes, omitted-coordinate status or source provenance by reporting one aggregate scalar.

The new support-three witness is an explicit counterexample to any promotion of a pair-support-only R063 output to *complete signed three-axis slice* BRC. It is not evidence that an actual historical code call made that promotion; the LP019 signed-positive-count wrong-call attribution remains `UNRESOLVED_PROVENANCE`, as does the LP011 historical native argmax wrong-call attribution.

Still required: original authorized, same-object R063 Stage 0 Python replay with `--N 2500 --regression-max-r 512`, all 17 historical gates and exact integer/no-loss cardinality checks; support remains original issue #2416 pending a real runner. Complete 28-LP consumer provenance and independent Driver REQUEST_REVISION. The previously host-denied 17:00 prose write is not retried by this work.

Research status: `AUTHOR-PROVED / EXACT INTEGER CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED`. Frozen inputs and original Result remain unchanged. Next authorized scientific action: independently trace an actual still-executable consumer which upgrades the R063 two-generator mass to signed three-axis native completeness, using this support-three set as an exact discriminating witness; if none is located, preserve that provenance as unknown, and prioritize original same-object 512-case replay.
