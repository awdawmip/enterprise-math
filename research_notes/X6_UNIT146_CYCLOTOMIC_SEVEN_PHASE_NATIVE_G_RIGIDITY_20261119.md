# X6 Unit146 — cyclotomic seven-phase native-metric rigidity and typed BRC consumer

Date: 2026-11-19 (Asia/Hong_Kong). Parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; Task `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`; Researcher `EM-X6-FB6990`, original SID `MCP-082892eb480e45dea6d4b9fcc0491034`; Research conversation `chatgpt-research-onhour-enterprise-math-20260923`. **AUTHOR_PROVED / FINITE_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Actual source, scientific pins and previously proven results

Frozen current native-P000 science: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` original blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`. Historical pre-rebase comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. A chosen Cell anchor represents native displacement by signed `z in Z^6`, native quadratic `G(z)=sum z_i²`, primitive signed word length `T(z)=sum |z_i|`, and positive shortest-path N-BRC `M(z)=T(z)!/prod_i |z_i|!`.

**Actual current X6 downstream executable consumer**: `experiments/x6_cyclotomic_compatibility_20260910/verify.py`, main Git blob `0d4ea1d29281236c80ae8502de7d75a5d76c39e9`. It defines a six-by-six cyclotomic integer matrix `U` by `U[i+1,i]=1` for `i=0..4` and `U[i,5]=-1` for `i=0..5`. The previously saved original author's `research_notes/x6_cyclotomic_shape_control_and_index_gate_20260910.md` (blob `fdab10f9925d715d2329d94e2869d7771befa1a4`, author `EM-X6CM-F01144`) already proved `U^7=I`, preservation of derived `H(z)=7G(z)-(sum z_i)^2`, and nonisometry at `e5` where `G(Ue5)=6` and `G(e5)=1`. This Unit146 consumes rather than duplicates those results.

The new exact question is whether any *particular nonzero signed native displacement* nevertheless retains its native `G` throughout the **complete seven-step orbit**, and how such a derived `U` operation interacts with shortest native primitive words and N-BRC.

## Seven-phase rigidity theorem (all signed integers)

Let `U(z0,...,z5)=(-z5,z0-z5,z1-z5,z2-z5,z3-z5,z4-z5)`, `G(z)=sum_i z_i²`, `H(z)=7G(z)-(sum_i z_i)^2`. Then for all `z in Z^6`,

```
U^7 z = z,
H(U^r z) = H(z)                         for every integer r,
sum_{r=0}^6 G(U^r z) = 2 H(z),
[G(U^r z)=G(z) for r=0,...,6]  iff  z=(0,0,0,0,0,0).
```

The third identity is a **native-G orbit aggregate**, and the last equivalence is a global seven-phase obstruction, strictly stronger than the old single `e5` nonisometry witness.

**Proof.** Embed `z` as seven integers `v=(z0,...,z5,0)`. Put `S=sum_{j=0}^6 v_j`, `C=sum_{j=0}^6 v_j²`. A single `U` action cyclically shifts the seven positions and subtracts the newly selected reference coefficient, with the new reference at zero. Hence its entire seven-phase orbit has exactly the following multiset of native quadratic values:

```
F_j = sum_{k != j} (v_k-v_j)^2 = C - 2 S v_j + 7 v_j²,
j = 0,...,6.
```

Cycling seven times restores the original anchored `z`, proving `U^7=I`. The derived variance `7C-S²=H(z)` is unchanged by reference shifts and permutations, proving `H` invariance. Summing the exact displayed `F_j` gives `7C-2S²+7C=2H(z)`.

If `F_j` is independent of `j`, each of seven `v_j` is a root of one quadratic `7t²-2St+(C-F)=0`, hence there are at most two distinct values. Suppose two distinct values `a != b` occur, with `p` entries equal to `a`. Viète gives `a+b=2S/7`, while direct summation gives `S=p a+(7-p)b`. Thus `(2p-7)(a-b)=0`. Since `p` is an integer and 7 odd, this is impossible. Therefore all seven `v_j` coincide. The explicitly adjoined final `v_6=0` forces every `z_i=0`. Conversely zero has constant zero native quadratic. QED.

## Exact first-step condition, native primitive and BRC effect

Direct substitution of the literal current source matrix yields

```
G(Uz)-G(z) = z5(5 z5 - 2(z0+z1+z2+z3+z4)).
```

A first step preserves `G` exactly when `z5=0` or `5z5=2sum_{i<5}z_i`. Such preservation is not stable under an entire seven-phase orbit unless `z=0`.

For the first native coordinate unit `e0=(1,0,0,0,0,0)`, the seven orbit representatives have

```
phase r:                       0  1  2  3  4  5    6
native quadratic G:           1  1  1  1  1  1    6
native minimum path length T: 1  1  1  1  1  1    6
positive shortest N-BRC M:   1  1  1  1  1  1  720
```

Phase 6 is `(-1,-1,-1,-1,-1,-1)`; its shortest native signed word has length six and `6!=720` ordered path realizations. This is an exact **native action/path observer nonintertwining**: `U` is a valid separately declared cyclotomic/ideal-lattice operator, but cannot be imported as a native-P000 primitive one-step action, native quadratic isometry, or one-to-one shortest-BRC word transport. The 720 is positive N-BRC path mass (not signed cancellation), and no native rotation law is admitted here.

## Executed finite source-specific check and boundary

Saved checker `research_checks/X6_UNIT146_CYCLOTOMIC_U7_NATIVE_QUADRATIC_ORBIT_CHECK_20261119.py` transcribes the exact six-coordinate `U` and uses always-on checks (not optimized-away `assert`). **Executed** for the entire integer box `[-2,2]^6`: 15,625 input displacements, 109,375 U-phase calculations. It verifies `U^7 z=z`, every phase's H invariance, the seven-phase G sum identity, and the literal first-step defect. There is exactly **one** full-orbit constant-native-G input (zero); **3,366 nonzero inputs** have the first two native norms equal yet a later phase differs. The `e0` path/BRC witness above is checked exactly. Executed normal, `-O`, `-OO` with exit 0 and identical JSON stdout SHA256 `93fdafa39e89cede2082bd6766be3d8e0a9e22d27d7e77a08f352578eb0dabef`; certificate `research_checks/X6_UNIT146_CYCLOTOMIC_U7_NATIVE_QUADRATIC_ORBIT_RESULTS_20261119.json`.

Scope: this is **an isolated exact current-source U transcription and independent checker**, not the original 2026-09-10 `verify.py` full source-import/ideal-lattice benchmark; universal theorem follows from the algebraic proof. The consumer already labels U as derived/non-native, so no speculative code patch is justified.

## Parent 28-LP reconciliation disposition and remaining debt

`LP022 / LP026 / LP028: KEEP_DERIVED_CYCLOTOMIC_IDEAL_LATTICE; RETAIN_NATIVE_G_T_NBRC; REJECT_UNTYPED_NATIVE_ISOMETRY_IMPORT`. This is one newly inspected actual current six-axis consumer plus a precise universal type boundary, not total 28-LP source closure. Source provenance of the allegedly wrong **historical** LP011 signed-native dominant singleton-axis argmax and LP019 subtraction of positive natural N-BRC remains `UNRESOLVED_PROVENANCE`, pending exact frozen `commit:path:line`; an independent Driver `REQUEST_REVISION` is still open. Original signed BRC/Helly/R063 six-file 512-case run and all Units1–145 must be consumed, not repeated. No P000/Foundation/frozen Result modification or mathematical acceptance follows from this author unit.
