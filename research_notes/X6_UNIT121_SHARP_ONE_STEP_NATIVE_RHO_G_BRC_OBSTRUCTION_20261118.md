# X6 Unit121 — sharp one-step obstruction for the native rho/G/BRC observer

Date: 2026-11-18. Source/task: `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. Author: `EM-X6-FB6990`, Research lane `chatgpt-research-onhour-enterprise-math-20260923`. P000 V5 frozen source `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical pre-rebase source `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

Classification: **AUTHOR-PROVED / EXACT-INTEGER-EXECUTED / UNREVIEWED / NOT_ADMITTED**. This is an observer/future-operation test, not the original R063/Helly benchmark or a task Result.

## Theorem — no well-defined named signed native step on (rho,G)

For `z in Z^6`, let `rho(z)=z-min_i(z_i)*1_6`, `G(z)=sum_i z_i^2`, and natural shortest-path multiplicity `B(z)=(sum_i |z_i|)! / prod_i |z_i|!`. A named signed unit operation is `U_(j,e)(z)=z+e*e_j`, `j in {0,...,5}, e in {-1,+1}`.

For any **distinct** `x,y in Z^6` with `(rho(x),G(x))=(rho(y),G(y))`, there is a nonzero integer `c` with `y=x+c*1_6`. Then for every named signed unit operation:

`rho(U_(j,e)(x)) = rho(U_(j,e)(y))`, while

`G(U_(j,e)(y)) - G(U_(j,e)(x)) = 2*e*c != 0`.

Proof: equal `rho` means `x-min(x)1=y-min(y)1`, hence `y=x+c1` with integer `c=min(y)-min(x)`. Expand both squares after `e*e_j` and cancel the equal current norms, obtaining exactly `2ec`. Relative observation commutes with a common diagonal translation. Thus no deterministic future-(rho,G) update descends through this observer on its entire native domain.

Equal current norms force `6c²+2c sum_i x_i=0`, whence `sum_i x_i=-3c`. For integral coordinates `G(x)>=sum_i |x_i|>=|sum_i x_i|=3|c|>=3`. The **minimum possible initial G is exactly 3**.

## Sharp BRC-preserving input witness and strict output split

`x=(-1,-1,-1,0,0,0)`, `y=(0,0,0,1,1,1)`. Both have `rho=(0,0,0,1,1,1)`, `G=3`, and **the same current N-BRC multiplicity 6**. Apply the *same* source-labelled native operation `+e_0`:

`U(x)=(0,-1,-1,0,0,0)`, `rho(U(x))=(1,0,0,1,1,1)`, `G(U(x))=2`, `B(U(x))=2`.

`U(y)=(1,0,0,1,1,1)`, `rho(U(y))=(1,0,0,1,1,1)`, `G(U(y))=4`, `B(U(y))=24`.

Therefore even the stronger present-state observer `(rho,G,B)` fails to determine the next native norm or N-BRC under a named signed step. The G=3 example is globally sharp. The one-bit recovery of the exact six-dimensional endpoint from `(rho,G,sign(sum z_i))` in Unit120 supplies a sufficient repair; its effectiveness follows by reconstructing the native state before applying the step. This is a joint native-state / path-multiplicity distinction, not an assertion about the old positive-sector R063 modulo map.

## Exact finite author evidence

The independently executed Python checker enumerated every integer state of `[-2,2]^6` (15,625 states), grouped by the complete `(rho,G)`, and checked **every 12 named signed steps** on **all** double fibers. Results: 14,883 fibers; 742 two-element fibers; 562 pairs have equal current BRC, 180 have different BRC; **8,904 signed-step checks, zero violations**. Minimum nontrivial fiber norm is G=3. The checker ran in CPython ordinary, `-O`, `-OO` modes; certificate bytes were identical, SHA256 `0ccff8a95ec69fbfc79bf16a45bfc23271276091600b4f2293238e88a1a2227a`. The universal claim follows from the algebraic proof, not the cube search.

Executable: `research_checks/X6_UNIT121_ONE_STEP_SHARP_CHECK_20261118.py`.
Machine certificate: `research_checks/X6_UNIT121_ONE_STEP_SHARP_RESULTS_20261118.json`.

## Bounded current consumer attribution

At current-main Git blob `aec58e8e0ebfc803138c74e02cc91967272274d2`, `research_checks/X6_LP028_G25_PATHSQRT_NATIVE_OBSERVER_COLLISION_BOUNDARY_20261113.py` defines relative min-zero `rho` at line 22, groups native endpoints at line 59, and calls `brc(z)` on **full native signed six-component states** during its G=25 collision analysis. That observed consumer correctly distinguishes native BRC from the lossy observer and is **not** a witnessed illegal rho-to-native lift. The separate current original importer at Git blob `db46dde5a962b93b65775bf2b4d8f52d5e3f83b9`, `X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py`, explicitly constructs signed native deltas (lines 45–65) and performs its BRC comparisons on those deltas (lines 78–81); its optimized-mode assert-elision was already characterized in Unit117 and its versioned strict runner is Unit118. **No new duplicate source repair is claimed here.**

## Continuing the mother task

The scoped LP023/LP028 interface rule is now exact: to use `rho,G` as a current observer, retain the signed native state (or Unit120's one-bit recovery coordinate) across named signed future steps; current N-BRC counts alone do not repair the transition defect. Next, execute the **already saved Unit118** pinned original-module strict LP028 three-mode integration, and locate an actual unsafe consumer with an exact original `commit:path:line` before proposing a current-code mutation. Keep LP011 / LP019 original bad-callsite provenance and Driver `REQUEST_REVISION` open, and independently review the exact six-blob R063 512/512 author benchmark evidence in Issue #2416 instead of repeating it. No changed P000, no new scheduler, no maintenance conversation identity.
