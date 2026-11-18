# X6 Unit147 — diagonal residual wake, one-step observer depth tomography and cyclotomic non-descent

Date: 2026-11-19; Task RS-X6-LEGACY-PLANE-RECONCILIATION; Publication TP2-B4A441B23DA3159232C2; parent PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Author EM-X6-FB6990; original SID MCP-082892eb480e45dea6d4b9fcc0491034; researcher lane chatgpt-research-onhour-enterprise-math-20260923. **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Exact source and scope

Native signed X6 Cell torsor and min-zero triple observers are frozen at `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`. Historical comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Actual current derived cyclotomic consumer: `experiments/x6_cyclotomic_compatibility_20260910/verify.py`, Git blob `0d4ea1d29281236c80ae8502de7d75a5d76c39e9`. Previous author's U-order-seven and H invariance are reused from `research_notes/x6_cyclotomic_shape_control_and_index_gate_20260910.md`, blob `fdab10f9925d715d2329d94e2869d7771befa1a4`. Unit146 proved seven-phase G rigidity; this unit addresses distinct future-observer and quotient-descent questions. U remains an **auxiliary declared integer transport, not a native P000 time evolution or rotation**.

Define V=Z^6, D=(1,1,1,1,1,1), Δ=ZD, q(z)=can6(z)=z-min_i(z_i)D and U(z0,...,z5)=(-z5,z0-z5,z1-z5,z2-z5,z3-z5,z4-z5). For each three-coordinate subset S of {0,..,5}, Obs_S(z)=can3((z_i)_{i in S}). These are 20 declared coordinate observers, not 20 established FCC circle-cell realizations; the four-star carrier theorem retains its original narrower status.

## Theorem A — exact residual orbit and minimal invariant-kernel closure

Direct substitution gives
```
U^0 D=D;  U^r D=-e_(r-1) for r=1,2,...,6; U^7 D=D.
```
In particular UΔ is not contained in Δ. Thus U does **not** induce a deterministic map V/Δ→V/Δ. More strongly, if K≤V contains Δ and U(K)⊆K, then every -e_i=U^(i+1)D lies in K and hence K=V. Therefore **the only additive U-equivariant quotient of V whose kernel kills all diagonal common-depth shifts is the trivial quotient**. This is a precise entire-seven-phase no-go for that quotient class; it neither forbids finer observers retaining depth nor says U is an admitted primitive action.

## Theorem B — observer visibility after each derived U phase

Two states z and z+kD (k≠0 integer) are indistinguishable to all twenty Obs_S at phase zero. For r=1..6 their difference after applying U^r is -k e_(r-1). Therefore
```
Obs_S(U^r(z+kD)) != Obs_S(U^r z)  iff  r-1 ∈ S   (1≤r≤6).
```
The proof uses equality of min-zero triples iff their raw triples differ by a common scalar; an isolated nonzero coordinate cannot be a common scalar on a three-element S. Exactly C(5,2)=10 of twenty triples distinguish the depth at any one nonzero phase, and the other ten do not. A fixed S distinguishes in exactly its three corresponding phases among r=1..6, with zero distinction at phases r=0,7.

## Theorem C — two observations reconstruct the missing integer depth

Write z=q(z)+hD, h=min_i z_i. Set w=q(z). For any S containing coordinate0 and another j, observe A=Obs_S(Uz). The difference of two output coordinates equals the corresponding raw difference. From Uz=Uw-h e0,
```
h = (Uw)_0 - (Uw)_j - [A_0-A_j].
```
Thus the pair (q(z), Obs_S(Uz)) determines the **exact native z** for any of the ten S containing 0. Conversely when S excludes 0, Obs_S(Uz)=Obs_S(Uw), independent of h, so that pair cannot recover h. This is an operation-conditioned observable residual, not a seventh spatial axis or proof of native U dynamics. A similar formula holds for phase r with S containing coordinate r-1.

## Native BRC witness

For a diagonal difference kD, native shortest length is 6|k| and positive shortest-path N-BRC is (6|k|)!/(|k|!)^6. After phases 1..6 the difference is -k e_i: native shortest length |k|, N-BRC 1. For k=1 the exact BRC orbit across r=0..7 is [720,1,1,1,1,1,1,720]. This independently certifies the typed failure of any unqualified transfer of native primitive/path multiplicity through derived U. It retains native length and BRC as P000 observers, not as auxiliary U invariants.

## Reproducible finite verification

The independent, source-exact isolated checker `research_checks/X6_UNIT147_CYCLOTOMIC_RELATIVE_DEPTH_OBSERVER_CHECK_20261119.py` checks all z∈{-1,0,1}^6 (729), k∈{-2,-1,1,2}, phases 0..7, all 20 three-coordinate subsets. It computes 2916 state pairs, 466560 exact triple comparisons (174960 visible, 291600 hidden), and 29160 one-step depth reconstruction checks. Normal Python, -O and -OO each exited 0 with identical canonical JSON SHA256 `06ecaa9ce9dfe1d8cf9df03f5e2437136fce4f8d0e4f54959caf78cf3164b724`. The checker employs always-on exceptions, not optimization-removable asserts. This finite census checks implementation consistency; the algebraic propositions are proved for all signed integers.

## Parent reconciliation and continuation

This is **one newly typed current actual downstream consumer** (derived cyclotomic U versus the native min-zero/common-depth observer and native N-BRC), not completion of the 28-LP corpus. LP011 alleged historical signed dominance bad caller and LP019 alleged positive natural N-BRC subtraction bad caller remain `UNRESOLVED_PROVENANCE` until original exact frozen commit:path:line is found. Existing R063 six-file benchmark and independent Driver REQUEST_REVISION remain separate. Nothing here updates locked P000, original J(N) ideal-lattice result, Source Result, independent review or admission. Next: authenticate current Unit146 Native PROGRESS original request; checkpoint Unit147 only under fresh winning owner/run generation; then expand genuine uninspected 28-LP consumer provenance.
