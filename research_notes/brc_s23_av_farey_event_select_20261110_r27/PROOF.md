# R27 — Farey-regime last-survivor event theorem and trillion-step affine-run generator

Date: 2026-11-10 Asia/Shanghai. Role: direct TASK_RESEARCH author-side research; independent review pending. Frozen scientific source: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Immediate predecessor: R26 `research_notes/brc_s23_av_farey_floorsum_fast_risk_20261110_r26/PROOF.md` at `c50ad8594e8840476d10f51d73067ab5ec62a654`. This is the auxiliary irrational-circle S23/AV observer with historical size `m=128`; it is not native X6 time dynamics.

## 1. Precise domain

For any irrational `0<theta<1`, let `P_n={{t theta}:0<=t<n}` in increasing circular order; `m>=2`, `n>=m`. Historical arcs `I` are oriented consecutive phase arcs of `P_m`. Let `M_n(I)` be the greatest elementary `P_n` gap contained in `I`. Set `R_n=1-sum_I M_n(I)`, `Delta R_n=R_n-R_(n-1)` for `n>m`.

Fix consecutive enclosing Farey neighbors `a/i < theta < c/j` of order `n-1`, where `i*c-j*a=1`, `i,j<n<=i+j`. Define positive gaps `u=i theta-a`, `v=c-j theta`, `w=u+v`. The established R26 three-translation formula gives sources of the three elementary-gap types:

- `u`: `0<=t<n-i`;
- `w`: `n-i<=t<j`;
- `v`: `j<=t<n`.

A **Farey regime** is the maximal consecutive integer range of `n` sharing this exact bracket. It ends at `n=i+j`; the next bracket first applies at `n=i+j+1`. The currently considered portion can be truncated by a requested horizon `N`.

## 2. New theorem: one last-survivor event per historical arc and Farey regime

Fix a Farey regime and a start `n_0>=m` with `max(i,j)<n_0<=i+j`. For every historical arc `I`, define its retained source set
```
T_I={ t in [n_0-i, j) : {t theta} is in I }.
```
If `T_I` is empty, `M_n(I)` never changes within this regime. If nonempty, let `t_I=max T_I` and `n_I=i+t_I+1`. Then for the complete regime, whenever `n_I<=i+j`, the **only** positive increment from arc `I` within `n_0<n<=i+j` occurs at `n=n_I`, and equals
```
M_(n_I-1)(I)-M_(n_I)(I)=w-max(u,v)=min(u,v)>0.
```
For every other insertion `n_0<n<=i+j`, this arc contributes zero. When the investigated regime is truncated at `N<i+j`, only events with `n_I<=N` are emitted. Different historical arcs give different `n_I`.

**Proof.** For a fixed Farey bracket, `u,v,w` are constant in `n`, and `w>u,v`. When `n` increases by one, the unique old `w` gap with source `t=n-1-i` is removed. The new cut `n-1` splits this gap into an `u` gap with the same old source and a `v` gap with source `n-1`. All three gaps lie in the same historical arc because `n-1>=m` and an old elementary `P_(n-1)` gap cannot cross a historical cut. Thus an arc containing any `w` gap retains maximum `w`, regardless of all earlier subdivisions. Its last `w` gap is removed precisely when `n-1-i=t_I`, i.e. `n=n_I`. At that insertion both new `u` and `v` gaps lie in the same arc, and thereafter that arc has no `w` gap and its maximum is `max(u,v)`; later insertions within this bracket only split other arcs' `w` gaps. An arc containing no `w` at the beginning receives no subdivision inside the regime. The source `t=n-1-i` is unique at each step and is owned by one historical arc, proving event uniqueness. QED.

**Observer sufficiency.** The full historical-arc source ownership is retained until the event positions are determined. After exact last-survivor selection, the sparse event map suffices to recover this scalar risk throughout the declared horizon; it is not a quotient for arbitrary later provenance-sensitive or native-X6 operations.

## 3. Exact rank/select implementation and regime transitions

R26 gives `Count_I(L,H)` in integer Euclidean floor sums for the half-open range `L<=t<H`; the identity works for wrapping historical arcs and negative shifted arguments. To compute `t_I`, first ask whether `Count_I(n_0-i,j)>0`; if so, binary search the greatest `t` for which `Count_I(t,j)>0`. Counts are monotone under suffix restriction. The returned `t` is checked by `Count_I(t,t+1)=1`, then `n_I=i+t+1` is emitted if within the current horizon. All interval memberships, gap types, and winner comparisons must be certified for the parameter interval.

At a transition `n=i+j+1` the Farey bracket changes, so the fixed-regime argument is restarted. The implementation computes this single transition's exact `Delta R` by the independent R26 floor-sum risk oracle, then continues at the next regime. Initial `R_m=0`. Merging consecutive equal exact increments, including implicit zero increments, generates maximal affine runs. Each run stores `(n0,n1,A0,B0,dA,dB)` for `R_n=A0+(n-n0)dA+[B0+(n-n0)dB]theta`.

Important interval refinement: the sign of `u-v` need only be fixed across the frozen theta enclosure **when a last-survivor event is emitted**. In the final investigated bracket the sign of `u-v` actually crosses the enclosure, but no last-survivor event occurs before `N`; the plateau and its affine coefficients remain uniformly certified. An unconditional precomparison of `u` and `v` in every regime would incorrectly reject this valid case.

## 4. Correctness, complexity and actual computation

For one regime with `m` historical arcs and Farey denominator `j`, the search invokes `O(m log j)` arc-count queries. Each count invokes a constant number of Euclidean floor sums using `O(log Q)` integer-reduction iterations when the rational comparison representative has denominator `Q`; operands require up to `O(log(NQ))` bits. Computing the next Farey bracket by accelerated Stern–Brocot and the one transition risk oracle has its separate arithmetic cost; the total includes `K` regimes, output events and run reconstruction. This is a non-enumerative-in-`N` generator for a fixed exact parameter bracket; the number `K` of Farey regimes and the output size are actual resource parameters.

Frozen theta enclosure:
```
262204504569236716045286 / 10^24 < theta <
262204504569236716045287 / 10^24.
```
The tested complete horizon is `m=128`, `N=1000000000128`. From 78 Farey regimes, the program generated 9,697 strictly positive risk increments and exactly 298 maximal integer-affine runs. The generated `AFFINE_RUNS_R27.tsv` is **byte-for-byte identical** to the earlier independently implemented R16 `AFFINE_RUNS_1T.tsv`: SHA256 `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`. The final exact value is
```
R_N=-4017401528447+15321634290944 theta.
```
The last investigated regime spans `752555238040..1000000000128`, contains **zero last-survivor events**, and is compatible with the earlier 247,444,762,089-step plateau.

The actual Python `Fraction` run additionally reconstructed every complete phase partition at `128<=n<=500`, independently checked the exact R26 oracle at the start/end of every regime, compared 1,642 selected positions with the R16 table and checked the complete 298-row file for equality. Observed event-generation time was 8.804 seconds (single local environment; includes regime oracle checks and excludes some file verification steps). These author checks preserve pending independent mathematical review.

## 5. Next research unit

Find the 128 historical arcs' last-survivor ranks in aggregate, bypassing `m` independent binary searches. Group Farey regimes by convergent/semiconvergent denominator to jump across repeated regimes such as the 14,298-step family; aim to generate **298 maximal affine runs directly**, avoiding the intermediate 9,697 individual positive events. Prove the claimed rank/select cost in bit operations, and test the structural mechanism for repeated `67/36/61` and `q-164` patterns. Keep the frozen scientific pin, exact history ownership, and separate author/review/promotion status.

Researcher-ID: `EM-DIRECT-9864F2`; Research-Activity-ID: `RA-2146F43C2F98ECB6C2C9AC66`. No shared TASK CLAIM, Result/Review, Working Truth, or Foundation assertion.
