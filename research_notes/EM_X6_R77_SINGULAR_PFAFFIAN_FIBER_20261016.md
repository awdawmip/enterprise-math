# R77 — Singular X6 Pfaffian fibers need growing repair information

Date: 2026-10-16. **Status: AUTHOR-SIDE DRAFT ONLY; NOT A FORMAL SOURCE RESULT; NO CLAIM, DRIVER REVIEW OR THEOREM ADMISSION.**

## Frozen research provenance

- GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge@0523d5b759c61deca93d355655f65a851e81e2a3`
- Enterprise Math: `awdawmip/enterprise-math@1f58caf7c6f930dd75893a3e7d456b8dda40884e`
- Exact signed six-axis N-BRC reference: Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`; R75 typed ordered-branch `(D,A,m)` refinement.
- Inputs: R76 rank-6 Pfaffian-adjugate and future-observer witness. This result strengthens the **rank-4 singular boundary** and does not count the full 18-step population.

## Formal native-X6 branch model

Each path is an ordered word over `±e_1,...,±e_6`; its displacement `D=Σs`, second-order antisymmetric history `A=Σ_{p<q}s_p∧s_q`, and exact positive-rational BRC mass `m=∏w(s)` obey
`D(uv)=D(u)+D(v)`, `A(uv)=A(u)+A(v)+D(u)∧D(v)`, `m(uv)=m(u)m(v)`.
The 15 signed four-axis Pfaffians are `P_ijkl=A_ij A_kl−A_ik A_jl+A_il A_jk`.

These integer matrices are typed **path-history observers in the full native 6D Cell substrate**, not a 2D native plane, independent spatial axes, physical time evolution, or signed/complex amplitude dynamics. The original ordered BRC branch identity and provenance are retained; loss arises only if a proposed observer quotient discards `A`.

## R77.1: unbounded rank-4 fibers at fixed length and exact positive weight

Define `c_ij^+=(+i,+j,-i,-j)`, `c_ij^-=(+i,-j,-i,+j)`. Both are zero-displacement, four-step reduced BRC loops with `A(c_ij^±)=±2e_i∧e_j`. Put `q=c_56^+ c_56^-`, which visits axes 5 and 6 and has `D=A=0`.

For any integer `N≥1` and `0≤m≤N`, define

`w_(N,m)=c_12^+ c_34^+ (c_13^+)^m (c_13^-)^(N−m) q`.

The `N+1` distinct words are **CYCL**, visit all six native axes, and have:

- the same length `n=16+4N`; `D=0`; first signed letter `+1`, last `+6`;
- exactly the same signed counts, positive and negative on axes 1,...,6 respectively `(N+1,1,N+1,1,2,2)`;
- identical exact positive-rational BRC branch mass `q_1^(N+1)q_2 q_3^(N+1)q_4 q_5^2 q_6^2`, where `q_i=w_i^+w_i^->0`;
- history `A12=A34=2`, `A13=4m−2N`, all other `Aij=0`;
- all **15 signed four-axis Pfaffians equal**: `P1234=4`, all others zero; `Pf6=0`, `rank(A)=4`.

The rank claim follows from nonzero Pfaffian of the 1,2,3,4 skew block and zero rows/cols 5,6. The CYCL claim follows by checking the four-step blocks and their boundaries, with no neighboring inverses including the final `+6` and initial `+1`.

## R77.2: one common legal continuation separates the entire fiber

Append the same four-step positive-BRC loop `v=c_25^+=(+2,+5,-2,-5)`. Every `w_(N,m)v` remains CYCL. Since both words close, `A(wv)=A(w)+A(v)` and `A25(v)=2`. Therefore

`P1235(w_(N,m)v)=A12 A35−A13 A25+A15 A23=4N−8m`.

For fixed `N` these are `N+1` distinct integers, despite identical **entire present signed Pfaffian vector**, rank, BRC mass, full signed occupancies, endpoints and boundary letters. In the shortest all-axis case `N=1, n=20`, two paths have current `P1234=4`, but subsequent `P1235=+4` and `−4`.

## R77.3: sharp repair lower bound on this declared population

Any exact observer compression retaining all the public common fields above, plus a repair label of `M` possible values, that purports to preserve **future signed four-axis Pfaffians under common legal ordered append** must distinguish all `N+1` words: `M≥N+1`. Hence extra worst-case bits satisfy

`b≥ceil(log2(N+1))=ceil(log2((n−16)/4+1))`.

The bound is **sharp for this family and second-order future language**: retaining the integer `A13=4m−2N` (equivalently `m`) recovers the full `A`, and `D=0` makes every subsequent `A(wu)=A(w)+A(u)` calculable, along with all Pfaffians. Thus no **fixed number of bits independent of word length** repairs arbitrary rank-4 singular paths from current Pfaffians, even when count, positive mass, rank, boundaries and complete native-axis occupancy are retained. This does **not** assert any lower bound for full physical state, higher path iterated signatures, or arbitrary BRC phase dynamics.

## Verification and exact bounds

`verify_r77.py` (contained in the local reproducibility package) uses R75 typed stream `(D,A,m)`, an independent event-pair `O(n²)` area reconstruction, exact recursive 4-/6-Pfaffian formulas, all-word CYCL, nonuniform rational weights and source-native BRC endpoint kernel. It checks every `m` at `N=1,2,3,4,7,16,32,64`: **137 explicitly constructed paths**, plus each common legal extension. Source-native/typed return-count and exact positive-weight bridge for all words at `n=0,2,4` passes. The unbounded theorem is a universal symbolic derivation, not extrapolation from finite checks.

Coldstart result: `R77_MANIFEST_PASS 8 / R77_COLDSTART_PASS`.
Local reproducibility bundle filename: `EM_X6_R77_SINGULAR_FIBER_20261016.zip`; SHA-256 `9f1a803a2424252efedc0c8d87f291db6fbf111f0bce36ab0373e2d6cf29edbf` (local artifact is **not** remotely uploaded by this note).

## Administrative disposition and next work

Canonical native `RESEARCHER session_start` returned `STATIC_READONLY_SCOPE_DENIED` (required write permission absent); `control_tasks` returned `CONTROL_QUOTA`. Consequently **the active task owner is not verified**, there is no formal Task/CLAIM/Result and no independent Driver acceptance. This branch note is not canonical state-machine visibility.

Next smallest scientific unit: on R75/R76's frozen 18-step `τ=1, K=14/15, rank4` explicit corpus, find exact duplicate full signed Pfaffian vectors at equal occupation and boundary labels, and search a common CYCL-legal extension separating their full second-order histories. This tests finite-length repair without assuming collisions absent from the sample imply globally absent.

## R77.4 (same-turn addendum): fixed 18-step high-support singular collision

Following R77.1–R77.3, an additional deterministic audit loaded the exact **90,000 frozen R75 canonical 18-step CYCL signed-axis words**, verified input SHA-256 `7d744b0e8776e448dfd2a8cd9e78a862350838bebcb1bf371c55eddd290883f7`, recomputed all 15 **signed** 4-Pfaffians for the relevant words, and grouped rank4, K14/15 representatives using `(signed counts, first letter, last letter, full signed Pfaffian vector)`.

Finite-corpus exact results: `rank4,K14=3611`, `rank4,K15=187`; `3790` distinct observer keys; of the 8 duplicate rows, 4 have the same A and 4 have **different A**. All four different-A collisions are K14, and each admits a jointly CYCL-legal four-step continuation separating at least one signed Pfaffian. No different-A K15 collision was seen among these 187 corpus words; no full-population injectivity conclusion follows.

One exact pair (length 18, signed axis occupancy `(2,2,1,1,2,1)` per positive and per negative direction, same first `+1` and last `−3`) is:

```text
w1=(+1,+2,+3,+2,+4,+5,+1,+5,+6,-5,-4,-5,-1,-2,-1,-6,-2,-3)
w2=(+1,+2,+3,+4,+5,-1,-2,+5,+6,-2,-5,-4,-1,-5,+2,-6,+1,-3)
```

Both are X6 zero-displacement, CYCL, `τ=1`, `rank(A)=4`, `Pf6(A)=0`, `K=14`, and have identical full **signed** four-Pfaffian vectors; `P1236=0` is the sole zero. Identical signed occupancy guarantees identical positive rational BRC branch weight for arbitrary asymmetric per-axis weights. Append the **same legal** `v=(+1,+3,−1,−3)` to each: all 22-step extensions remain CYCL, yet

- `P1234(w1v)=−4` versus `P1234(w2v)=−12`;
- `P1235(w1v)=−4` versus `P1235(w2v)=−16`;
- `P1236(w1v)=0` versus `P1236(w2v)=4`.

This provides a concrete short-scale **18-step, K14, rank4** future-indistinguishability obstruction, beyond the unbounded fixed-length fiber theorem. The complete four-pair corpus certificate, two verifiers, source R75 TSV and bundled original N-BRC code were re-run from an independent SHA-256 manifest: `R77_PASS / R77_FIXED18_PASS / R77_MANIFEST_PASS / R77_COLDSTART_PASS`.

Updated local full evidence archive: `EM_X6_R77_SINGULAR_FIBER_20261016.zip`, SHA-256 `9f1a803a2424252efedc0c8d87f291db6fbf111f0bce36ab0373e2d6cf29edbf`. The archive is a conversation artifact, **not remotely uploaded** by this note. Full-population 18-step fiber multiplicity and repair coordinates remain open; official Researcher/owner Source admission remains blocked.
