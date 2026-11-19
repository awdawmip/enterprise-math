# X6 Unit152 — lossless min-zero lift and native signed-step conjugacy; exact observer-BRC boundary

**Date:** 2026-11-19 (Asia/Hong_Kong). **Mother:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. **Author lane:** `chatgpt-research-onhour-enterprise-math-20260923` (existing `EM-X6-FB6990`, Source SID `MCP-082892eb480e45dea6d4b9fcc0491034`; authority requires live revalidation for native writes). **Status:** AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. No Foundation, P000, frozen Result, or benchmark mutation.

## Exact source and type

- Frozen native X6: `59538f585d037d09ef687b28715c4bc1a3f9fe03:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`. Chosen Cell-relative spatial states are `z in Z^6`; primitive spatial steps are the twelve labelled `±e_j`.
- Frozen `signed_brc.py`: `59538f585d037d09ef687b28715c4bc1a3f9fe03:experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. Native squared component length `G(z)=sum_i z_i^2`, native shortest signed step count `N(z)=sum_i |z_i|`, shortest N-BRC multiplicity `N(z)!/prod_i|z_i|!`.
- Historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3:definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md`, blob `11f47f9d2d70439fdada6d59242790fdcf46929e`, §§2–8: derived `Z^3 / Z(1,1,1)` and min-zero section retain a separate semantic type from native Cell addresses. The current R062 BRC bridge remains an enriched typed-path-to-N-to-Boolean tower.
- Earlier Units147–151 already prove depth wake under auxiliary `U`, one-step scalar collision, quotient endpoint BRC pushforward, bidirectional path reversal, and directed-gauge triangle/reversal bounds. Unit152's **new obligation** is the labelled **native step-by-step lossless transition conjugacy**, including exactly when quotient transitions close without hidden depth and when they do not. This is not a rerun of their tests.

## Proposition 1 — all-integer labelled native-step conjugacy

Set `D=(1,1,1,0,0,0)`. For a chosen Cell-relative signed `z=(z_0,...,z_5) in Z^6`, write
`h=min(z_0,z_1,z_2)`,
`w=(z_0-h,z_1-h,z_2-h)`, and `v=(z_3,z_4,z_5)`.
Then `min(w)=0` and
`Phi:Z^6 -> A_min0 × Z × Z^3`, `Phi(z)=(w,h,v)`
is a bijection, with inverse `Phi^{-1}(w,h,v)=(w+h(1,1,1),v)`.

For a native step `s e_j`, `s∈{-1,+1}`:
- If `j<3`, put `u=w+s e_j^{(3)}`, `t=min(u)`. The exact lifted transition is
  `T_{j,s}(w,h,v)=(u-t(1,1,1), h+t, v)`.
- If `j>=3`, it is `T_{j,s}(w,h,v)=(w,h,v+s e_{j-3}^{(3)})`.

**Identity:** `Phi(z+s e_j)=T_{j,s}(Phi(z))` for every `z in Z^6`, all twelve labels, with `t∈{-1,0,+1}` for any one step. The proof is the integer min translation law `min(h(1,1,1)+u)=h+min(u)`; the remaining axes are independent. The inverse formula proves bijectivity. Induction preserves the exact raw signed endpoint and complete ordered label word at every time: the skew lift is a conjugacy of labelled native transition graphs, not an identification of primitive Cell positions with observer classes.

## Proposition 2 — precise quotient dynamical interface

The observer `pi(z)=(w,v)` is a quotient by `Z D`. From the formulas above, `pi(z+s e_j)` depends only on `pi(z)` and the step label, **not** on hidden `h`. Therefore any process selecting the signed label with probabilities/weights determined by the quotient state alone has a well-defined quotient step kernel and is strongly lumpable through `pi`. In particular, the uniform 12-label native walk admits an exact quotient walk, and the natural-number sum of native path counts over a quotient endpoint fiber is the observed N-BRC count; every source label and ordered path can still be retained in a richer Path-formal lift.

The qualification on label weights matters. For example, define a state-dependent deterministic rule selecting `+e_0` at even `h` and `-e_0` at odd `h`. The raw states `0` and `D` have the same min-zero observer `w=0` but distinct next observed states `(1,0,0)` and `(0,1,1)`. Thus **an arbitrary h-dependent update need not descend to the quotient**, although every declared primitive signed-step label does. This gives an exact acceptance test for downstream 28-LP consumers: specify the observer, retained label/weights, and whether their update is constant on `ZD` fibers.

## Proposition 3 — exact depth is necessary for the native scalar fiber

For any positive integer `q`, `z=0` and `z'=qD` have the same `(w,v)`, and `h≡h' (mod q)`; nevertheless
`G(z)=0` while `G(z')=3q²`,
`N(z)=0` while `N(z')=3q`, and
`B_min(qD)=(3q)!/(q!)^3 > 1=B_min(0)`.
Consequently **no fixed finite residue `h mod q` appended to the min-zero observer suffices to reconstruct these unbounded native invariants on all of `Z^6`**. The full integral depth `h`, or an equivalent lossless augmentation, restores every native endpoint and its derived scalar invariants; nothing here postulates a new spatial axis, force, time or primitive segment.

## Executed finite certificate

Actual standalone CPython checker on these formulas: `research_checks/X6_UNIT152_SIGNED_MINZERO_LIFT_CONJUGACY_CHECK_20261119.py`, exactly pinned to Git blob `94a1f1cb6c8b6f7fb5a276de23ee2d21b7160884` at commit `fb52378b546a24c869e92764c835f198ab09ead8`. Certificate `research_checks/X6_UNIT152_SIGNED_MINZERO_LIFT_CONJUGACY_RESULTS_20261119.json`, exact executed bytes Git blob `173dfa90f47b552c63c78633942fc6d722a385d6` at commit `b7762ae6c3802f09ddaefb7632c51dcafbe5d5b1`.

- All **15,625** states in `[-2,2]^6`, each of twelve signed labelled transitions: **187,500** exact integer comparisons of native updates with skew updates and inverse reconstruction.
- All **55,987** first-three-axis signed labelled words of lengths `0..6`, retaining each complete prefix endpoint, passed.
- Independently accumulated signed three-axis raw-endpoint and quotient walk kernels up to length 8. Observed/native zero-class counts: at `L=3`, `12/0`; at `L=6`, `2040/1860` (hidden=180); at `L=8`, `54810/44730`.
- Twelve finite residue witness tests for `q=1,...,12`; the all-`q` proof is the formula above.
- CPython normal, `-O`, `-OO` each exit 0, byte-identical stdout SHA256 `9152a625834d9f18148734b0369189f28ef4ba5c5569118fd8f00779ba7cf2fc`. All checker requirements use explicit `ensure`, not stripped `assert`.
- The checker is a **source-independent mathematical implementation**; it did **not import frozen signed_brc.py or run the original R063 six-file/512-case benchmark**. The general theorem is the all-integer proof above; finite tests certify the declared domains only.

## Reconciliation disposition and exact debts

**PRESERVE_OBSERVER:** historical min-zero/diagonal chart as a typed derived displacement observer. **PRESERVE_NATIVE:** the six-axis Cell torsor, signed primitive labels, `G,N,B_min` and labelled native transitions. **PRESERVE_PATH_BRC:** BRC pushforward works after preserving endpoint/step provenance; Boolean support is a further forgetful map. **RECOMPUTE / UNRESOLVED_PROVENANCE:** an actual downstream h-dependent consumer must be tested for fiber invariance before promotion. There is no evidenced LP011 erroneous signed argmax or LP019 erroneous natural N-BRC subtraction caller in this unit, and no blanket negative result for the full historical corpus.

**Unfinished mother work:** trace exact still-uninspected historical/current 28-LP callers with commit:path:line, particularly LP011 and LP019; verify the original distinct R063 six-file/512-case native benchmark under its frozen conditions; obtain independent Driver review/admission. Existing Source Native PROGRESS is certified through Unit148 (`9e80d79f719d17053397f00f4eebdbafbfd5133f`). Original Unit149 publish request `onhour-20261119-1000-x6-own-unit149-native-progress-v1` terminated `FAILED/GITHUB_PRIMARY_RATE_LIMIT`; do not replay it. Original continuation `onhour-20261119-1021-x6-own-cont-after-unit148-149-rate-v1` completed `SUCCEEDED/OWN_RECORDED_RUN_AVAILABLE` but is not fresh writer authority. Unit149–152 author science remains distinct from Native semantic publication.

Next: consume current own Source owner/RUN/generation when available, handle the failed original Unit149 without disguised replay, and continue exact native-vs-observer consumer source audit. The local source-level proof and finite certificate are already safely persisted; maintain the original owner/contribution history and independent-review boundary.
