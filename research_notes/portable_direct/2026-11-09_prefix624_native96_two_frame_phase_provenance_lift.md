# PREFIX-624 — Two consecutive native phase frames reconstruct all 96 ports, gates and labelled actions

Date: 2026-11-09. Status: **author-side exact theorem and code-checked evidence; independent Driver review pending**.

Frozen input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original X6 STAR triples `(1,3,6),(1,4,5),(2,3,5),(2,4,6)`, axis weights `(1,1,1,1,0,0)`, 48 native phases, 96 ports, and 576 labelled native actions. Starting four-phase probe `d=e4+e11+e14+e32`, original native embedding `E(d)`. Dependencies: PREFIX-597 native port decoder, PREFIX-622 ([PR #1863](https://github.com/awdawmip/enterprise-math/pull/1863)), PREFIX-623 ([PR #1864](https://github.com/awdawmip/enterprise-math/pull/1864), commit `0ccdeea6c7b5ab9d1ac833990ce6eb40d4db18a6`). These are author-side sources, not independent admissions.

## Exact observer and action scope

Let `A(z)` be the original 96-port nonnegative rational action update, and `Q(z)` its original 48-phase update on the reachable carrier. Native step index `m` counts operations, not physical heartbeat duration. Unknown gates `z_m>=0` and original port states `r_m=A(z_m)r_(m-1)` produce phase readings `v_m=encode(r_m)`. Special phase `g=4`; special destination set `H={3,14,15}`. Set

`L(v)=v[3]+v[14]+v[15]-2*v[2]`.

Individual ports and labelled path flows are **nonnegative masses**. The imbalance `delta_m=r_m[29]-r_m[28]` is a *derived signed difference of observer coordinates*, not a negative path weight.

## Theorem 624.1 — exact two-frame lift

For any native previous port state with `r_(m-1)[8]=r_(m-1)[9]=v_(m-1)[4]` (in particular, every orbit after original embedding), and any `z_m>=0`,

`L(v_m)=3(z_m+3)*v_(m-1)[4]` and
`delta_m=(z_m-1)*v_(m-1)[4]`.

Consequently the entire **current 96-port vector is reconstructed from two successive 48-phase vectors**, without knowing the gate:

`delta_m=L(v_m)/3-4*v_(m-1)[4]`.

For `i!=4` the decoder is

`r_m[2i]=(v_m[i]-1_(i in H)*delta_m)/2`,
`r_m[2i+1]=(v_m[i]+1_(i in H)*delta_m)/2`,

while `r_m[8]=r_m[9]=v_m[4]`.

**Proof.** The exact 576-action enumerator gives equal destination-bit contributions for every source phase other than `4`; the only exception is source `(phase4,bit1)` at marked destinations in `H`, where the destination bit-1 versus bit-0 flow difference equals `(z_m-1)r_(m-1)[9]`. At destination phase 4 the two output ports remain equal. Thus the imbalance/decoder identities follow. On the 48-phase side, expanding the original three incoming source lists at phases `3,14,15` and `2` yields the **operator identity**

`(e_3^T+e_14^T+e_15^T-2e_2^T)*Q(z)=3(z+3)*e_4^T`.

This is an identity of all 48 row coefficients, not an observed numerical coincidence. As an independent exact certificate the checker verifies the complete basis at `z=0,1`; the source-defined `Q(z)` is affine in `z`, so these two checks also prove the general symbolic identity. Eliminate `z` between the two identities. ∎

When `v_(m-1)[4]=0`, the port decoder still returns the exact current ports and `delta_m=0`; the current gate need not be inferable.

## Theorem 624.2 — unknown gates observable on the four-point orbit

For `r_0=E(d)` and **arbitrary nonnegative gates**, `v_m[4]>0` at every `m>=0`; hence

`z_m=L(v_m)/(3*v_(m-1)[4])-3`.

**Proof.** Nonnegative action weights imply `Q(z)>=Q(0)` entrywise. From the frozen original sparse graph, these are strictly positive `Q(0)` phase paths:

- initial `4` at length 0;
- `11->4` at length 1;
- `32->26->4` at length 2;
- `14->40->26->4` at length 3;
- `4->14->40->26->4` a strictly positive length-4 cycle.

All four initial sources have positive mass in `d`. For any `m=4k+r`, concatenate the corresponding length-`r` path with `k` cycles, establishing `(Q(0)^m d)[4]>0`. Comparison with all `Q(z)` proves positivity. Theorem 624.1 then uniquely gives `z_m`. ∎

## Corollary 624.3 — complete phase time trace determines labelled provenance

Given `v_0,...,v_N`, the known starting embedding `E(d)` and no separately supplied gate logs, Theorems 624.1–624.2 recover `z_1,...,z_N` and each 96-port state. Thus every original labelled one-step action flow is exactly recovered:

`J_(m,alpha)=w_alpha(z_m)*r_(m-1)[source(alpha)]`,

for each of the 576 original labels `alpha=(destination phase,source phase,destination bit,source bit)`. Every finite ordered labelled path flow is similarly determined by the recovered source-port mass times the exact product of edge weights. This is an exact conditional **time-series observer** theorem, not an assertion that the present endpoint alone stores all historical provenance or that materializing a full exponential path tensor is cheap.

For an arbitrary admissible carrier with `v_prev[4]=0`, current port reconstruction survives, but the gate itself can remain hidden from phase observations.

## Theorem 624.4 — single-frame insufficiency (sharp temporal window)

The two original five-step histories `A=(1,1,1,1,2)` and `B=(2,1,1,1,1)` have **identical full 48-phase fifth-step observations** but distinct full 96-port fifth-step states. Their bit imbalances are `delta^A_5=16`, `delta^B_5=0`. The fourth-step 48-phase states differ, and each of the corresponding pairs `(v_4,v_5)` reconstructs its own native fifth-step state and latest gate by Theorems 624.1–624.2. Therefore among observers reading a fixed number of **complete consecutive phase frames** with gates unknown, exactly two frames are necessary and sufficient to recover current ports on the four-point reachable family.

## Reproducible evidence and limits

The independent stdlib `fractions.Fraction` checker reconstructs the original STAR phase graph, 96-port kernel and 576 typed actions. It checks **96** basis coefficients for the dual identity at `z=0,1`, the five positive support paths, and 124 deterministic gate sequences including zero, integer and rational gates: **1,740** exact transitions, **167,040** port-coordinate comparisons, **1,002,240** native labelled flow comparisons, plus 1,740 gate inversions. All assertions pass. Exact output: `PREFIX624_two_frame_native_decoder_results.json`; standalone source: `PREFIX624_two_frame_native_decoder_checker.py`.

Finite execution validates the implementation; the exact affine dual-row, native port update and positive-cycle arguments prove all-length mathematical claims. Full-path tensor materialization and large-rational bit complexity are not asserted as constant-cost. No P000 revision, external physics claim or independent mathematical review is made.

## Next targeted question

**Temporal sensor economy:** Can fewer than the six fixed phase sensors of PREFIX-620, sampled across two or more adjacent times, reconstruct the full phase trace and original labelled flows when the initial two gates and probe amplitude are unknown? Specify the observer's exact samples and time window and seek a rank/minimality certificate across all four time residue classes. Distinguish present-state minimality, temporal observability, and size of the requested path tensor. This is independent author-side research; no formal task CLAIM, Native Result or Driver admission follows from this draft.
