# N14 iid Stage97 — exact nonblind Bellman + primal audit (2026-10-25 15:00 Asia/Taipei)

**Status:** `NONBLIND / UNREVIEWED / NOT_ADMITTED`. This is a neutral research-evidence preservation, **not** an EM native RESEARCH_DRIVER Review, a Reference pass, a synthesis, a Result, a new Task, or a P000-native theorem.

## Provenance and scope

- External finite 3-letter iid sequential-testing auxiliary problem (not the Heartbeat/X6 native model). Horizon 14; P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6).
- Author source: `research_notes/n14_aux_iid_affine_97_20261025/PROOF.en.md`, `certificate97.json`, current EM source `74e2c8f184d60242747a4756a84703e2ceeb967f`; original author source pin `2540a16d415477e0006b18411e08a82c521103db`.
- Verified current global-main ref on read: `dca4319404d29afc12774cd488926733e49782c4`. Gateway static global bundle instead pins `7b33f8066e9993e7c941959a9d738ed405248eb8` (distinct snapshot; do not mix). Current P000 original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`.
- Source/exposure history: the author theorem and rational certificate were read **before** this check; results are nonblind. This run does not assert clean scientific independence, source-native contribution separation, or possessing an active Driver DA. Sites connection reported `static_machine_readonly`, with `source:read/control:read`, `research_authority_granted=false`.

## Independent exact calculation

Reimplemented rational dynamic programming, **without executing or copying the author's Stage97 checker**. For count state `(n,a,b)`, `R=2^(a+b)/3^a` and

```
D(n,a,b) = min(lambda_Q*R, lambda_P, 1 + sum_i P_i*D(child_i))
```

(no continuation at `n=14`), where

```
lambda_Q = 893307577584960 / 619337901137
lambda_P = 838643508957384 / 619337901137
```

All 680 count states were visited with exact rational arithmetic; 1240 nonselected action comparisons were evaluated. There are **1238 strict positive** differences, no negative differences, and two double ties: `(4,4,0): P/C`, `(12,0,1): Q/C`. Minimum positive gap is exactly `19154578828699/237825754036608`. Root:

```
D(0,0,0)=33377638070337837845505597379543/33927652994761948643740090368.
```

It equals `V96+(lambda_P+lambda_Q)*alpha96` at the author's declared rational `alpha96,V96`.

A separate forward state-mass pass (positive P- and Q-probability, exact fractions) computed errors, stopping times and dual slack for policies with A97's `P`-stop probability `u=0,1/2,1` and B's `Q`-stop probability `s=s96+h97*u`. At each point, both errors are equal and exactly `alpha96+eta97*u`, with

```
h97 = 813388768063 / 1671168000000000
eta97 = 619337901137 / 4966767251303694336
```

Dual slack `t_P+lambda_P*e_P+lambda_Q*e_Q-D(root)` equals zero at all three points. In each case `t_P>t_Q`. Both tie-arrival masses are unchanged across the three policies: A=`(1/4096,1/20736)`, B=`(48828125/725594112,48828125/362797056)`. Each of the four metrics is affine at the midpoint by direct equality of the rational midpoint to the endpoint average. Endpoint `t_P` values equal exact `V96` and `V97=757686080746453135/58204303726215168`.

The two tie branches have disjoint prefix cones: A requires four 0 symbols, while B has no 0 symbols. Thus their randomized policy contributions are affine (not merely numerically interpolated) on the entire interval `u∈[0,1]`. Coupled with the exact lower bound and two positive endpoint `t_P-t_Q` values, this validates the interval support-line part within the *declared external auxiliary model*.

## Unverified boundaries and next action

This audit did **not** independently enumerate the 4587 ordered suffix leaves or provide a full standalone uniqueness/sharpness proof beyond `alpha97`; did not verify any original Source-native Result or exact native review set; and did not run an authorized Driver Review/Reference/Synthesis/Follow-up. Mathematically the Stage97 author claim receives a nonblind exact rational crosscheck, **not admission**.

Next: current authorized and contribution-independent Driver must obtain legal current DA, exact frozen Result/review set and preserve immutable prior reviews before native action. Independently, a researcher may proceed to the declared K98 crossing only as a distinct `UNREVIEWED` auxiliary research unit; do **not** publish a duplicate formal Task based only on this note.
