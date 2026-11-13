# Stage389-B — independent upstream localization audit and sharper source-left exclusion margin

Date: 2026-11-03 (Asia/Shanghai). Research2 author-side portable result; Draft PR #1736. Frozen scientific inputs: GLOBAL_KNOWLEDGE_V1 `main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; Enterprise Math `main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; original P000 V5 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral reads are distinct: global `main@b59f43c34efcbafa9d25df44f981b963bc0a698a`; EM `main@81d35ba29b24b400c869180624ddcfba520bae5e`. This result concerns the external full-labelled Bernoulli/BRC auxiliary observer, and preserves the native P000 X6, independent time, three-dimensional slice, and future-observer bridge as an open typed target.

## Exact model and question

For k=0,1,2,3 define `B_k(t)=t^k (1-t)^(3-k)`, weights `w=(1,3,3,1)`, targets `m=(61,21,9,9)`, residuals `r_k(x,y)=[4B_k(x)+B_k(y)]/5-m_k/160`, and independent four-channel budget `b(x,y)=(5/32) sum_k w_k|r_k(x,y)|`. Preserve all sixteen source/anchor/word comparisons in `D(a,z)=(1/2)sum_k w_k|B_k(a)-B_k(z)|`, `c(x,y)=[63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)]/256`. Minimize `T(P,Q)=33/1024+c(P)+c(Q)` over `[0,1]^4` under `b(P)+b(Q)<=2 beta_*+11/5000`, where `beta_*=b(q_*)` and `r0(q_*)=r1(q_*)=0` at the isolated central root.

Question: independently audit the upstream Stage368-B full `[0,1]^2` interval localization and Stage369-B source-left exclusion, including exact boundaries, root/reference feasibility, leaf coverage and original certificate digests. Then tighten the Stage369-B strict objective margin using unrounded rational enclosures already present in the same model.

## Result 1 — exact all-real interval audit

An independently implemented **expanded-Horner/Fraction** evaluator uses cubic coefficients `(1,-3,3,-1),(0,1,-2,1),(0,0,1,-1),(0,0,0,1)`. The exact range of each B_k on a closed rational coordinate interval is the minimum/maximum of the two endpoints and the interior stationary point `k/3`, if present. For an interval `[l,u]` enclosing an expression and rational anchor q, `max(0,l-q,q-u)` is a lower bound for `|expression-q|` everywhere in that interval. The independently written checker applies these lower bounds to all four r_k and all 16 labelled audit comparisons, summing only nonnegative channel weights.

A binary subdivision uses **both closed halves**, preserving all real boundary points. The checker separately verifies that the exact summed leaf rectangle area equals the root rectangle area, that each leaf's inequality is strictly positive, and that leaf count = split count + 1. It does not import the earlier Stage368-B or Stage369-B programs.

* Stage368-B: exact full-square enclosure yields `b>377/100000` everywhere and `b>599/100000` for every point outside `R=[219/1000,239/1000] × [51/100,16/25]`. It closes **604 leaves**, with **338 OUTSIDE_FORBIDDEN** and **266 INSIDE_GLOBAL_BOUND**; **603 splits**, max depth **28**, exact total leaf area **1**, zero unclosed boxes. Minimum strict leaf slack is `129187931/13743895347200000`. Exact CSV: **43,413 bytes**, SHA256 `adcca00c9a5cf502ab03fcecf324b321683487dab432b28ac59ee0b549c16040`, identical to the immutable Stage368-B digest.
* Stage369-B: `L=c+(6/5)b` satisfies `L>373/10000` on the complete closed `R`, and `L>753/20000` on `S=[219/1000,577/2500] × [51/100,16/25]`. The independent checker closes **1,191 R leaves** and **113 S leaves**, zero unclosed boxes, checking exact leaf areas `13/5000` and `767/500000`. Minimum strict slacks are `605681/2621440000000000` on R and `330155810305507/1342177280000000000000` on S. Exact CSV: **189,212 bytes**, SHA256 `c60855319b26ba0e842906aa9126489568b001eef5945fd24247e64369f884d9`, identical to the immutable Stage369-B digest.

The root rectangle `(2310839,2310840)/10^7 × (5555086,5555091)/10^7` satisfies all checked r0/r1 corner sign relations. Since r1 increases with x and decreases with y there, its zero graph increases; r0 decreases along that graph, so q_* is unique. On the root, `r2>0>r3` and the exact identity `sum_k w_k r_k=0` imply `beta_*=(15/16)r2(q_*)`. As B2 is increasing throughout the bracket, the checker establishes exact bounds `beta_L<beta_*<beta_U`, where

`beta_L=15116461719181908801/4000000000000000000000`,
`beta_U=60466487110135696287/16000000000000000000000`.

Hence `2beta_*+11/5000 < C_U`, with

`C_U=78066487110135696287/8000000000000000000000 < 61/6250`.

It follows from the Stage368 bounds that any feasible two-source pair lies in `R×R`; source exchange leaves both objective and budget unchanged.

## Result 2 — stronger strict source-left cost margin

Let the exact rational reference be

`P0=(231138/1000000,555681/1000000)`, `Q0=(237807/1000000,575694/1000000)`.

The checker evaluates the original four-channel budget and 16 labelled audit comparisons directly and verifies

`b(P0)+b(Q0)=156126870406900413/16000000000000000000 < 2beta_L+11/5000`,

`c(P0)+c(Q0)=16174439790495832521/256000000000000000000`.

For **every real feasible** `P,Q` with either `P∈S` or `Q∈S`, the R/S certificates give

`L(P)+L(Q) > 753/20000 + 373/10000 = 1499/20000`.

Because `b(P)+b(Q)<=2beta_*+11/5000 < C_U`, removing the shared `lambda=6/5` budget term yields the exact uniform improvement

**`T(P,Q)-T(P0,Q0) > 9379440296847963487/160000000000000000000000`**.

This strengthened positive margin is approximately `0.0000586215018553`; Stage369-B used the weaker `3/62500=0.000048`. The new certified strict margin is over 22% larger because it retains the rational beta upper enclosure and exact reference cost instead of rounding both to coarse caps. It excludes both closed source-left strips including `x=577/2500`, and thus yields `x_P,x_Q>577/2500` for every global minimizer. The feasible set is compact and nonempty by the exact reference, so a global minimizer exists.

## Reproduction, evidence, and precise status

Run `python REPRO_STAGE389B_INDEPENDENT.py --emit-dir OUTPUT_DIR` to regenerate both complete CSV certificates; rerun without arguments to independently replay diagnostics and exact assertions. This run executed both, and its stdout files are byte-identical. Arithmetic is `fractions.Fraction` throughout; floats appear only as optional human interpretation above, never in the checker. The program enforces historical SHA256 equality as well as leaf areas, strict inequalities and the stronger exact margin.

Result classification: **PORTABLE_AUTHOR_PROOF / EXACT_FRACTION_EXECUTED / REPLAY_VERIFIED / UPSTREAM_STAGE368_369_AUDITED / UNREVIEWED / NOT_ADMITTED**. Native Source session/CLAIM is unavailable under the connected gateway's read-only scope; canonical owner enumeration returned `CONTROL_QUOTA`. The GitHub Draft PR is a source preservation/peer-review handoff, not native Result/Driver acceptance.

## Next precise mathematical question

**Stage390-B:** independently audit the load-bearing Stage381-B double-r1/cusp uniqueness argument against the actual closed-boundary conditions and exact marginal comparison, while reusing the now audited Stage368–379 global covers. In parallel, reconcile the Stage366–367 local sharp support proofs against the global candidate without silently promoting an auxiliary 2-coordinate expression into P000 native six-axis/three-dimensional-slice dynamics. A verified exact counterexample or a finite certified critical-point reduction is an acceptable next scientific increment.
