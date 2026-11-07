# Stage306-B — optimal three-future-visit private-label compression

**Status:** PORTABLE_RESEARCH_CONTINUATION / UNREVIEWED / NOT_ADMITTED. This handoff does not create or claim a canonical Task.

## Frozen scientific frontier
Stage305-B `PROOF_STAGE305B.md` and its exact executed `REPRO_STAGE305B.py`/stdout at the immutable GitHub commit of this handoff. Inputs: global `main@8a90490344dbf310db7764d8c53cb8274f0cd904`, project `main@5256fc460df9a8dd3cc0945999ac56830d42582b`, Stage304-B `3ab137c9f602101564cc0fce2be1c87d301d02a4`. Rebase current control, owner and author activity when continuing; do not silently change this theorem's original source assumptions.

## Exact source and state
Original S is fair; `p_S∈{1/4,3/4}`; `Pr(J=1|S=0)=1/8`, `Pr(J=1|S=1)=7/8`; `Pr(W=S)=3/4`; immutable original first F bit Y1 has rate p_S. Future examiner sees W,Y1 but not S,J until an explicitly terminal audit. It chooses H (fresh fair output) or F (source Bernoulli output) from visible history. A controller may read (J,W,Y1), choose **one rate** `t_{J,W,Y1}∈[0,1]` and generate all future F bits independently given that fixed rate. All source/branch weights are strictly positive rationals. Source-tagged observer constraints are separate from public `(W,Y1,actions,outputs)`.

## Proven and do not redo
For two future visits the positive rational rate table:
`(W,Y1)=00: t0=9/40,t1=3/5; 01/10: t0=1/4,t1=3/4; 11: t0=2/5,t1=31/40` preserves **all public history-adaptive traces exactly** by matching conditional first two moments. It has tagged two-visit risks `R_J=111/1600, R_S=5487/102400,R_SJ=549/6400`. For three fixed future F visits the same table has a third-moment discrepancy `±63/16000` on 00/11 and exact public TV `63/6400`. That number is a **witness**, not yet an optimum. Sequential Bayesian posterior updating can exactly preserve all pooled public future traces; terminal S or J audits remain a different observer language. The mean-only IID port has two-visit public risk `651/16384`. Exact per-history fixed-IID J-audit optimum at two visits is `-89/64+√142/16+3√2/8+√22/32`.

## First research unit
Find the **global** minimizer of public full-ordered three-F total variation over the 8 real locked rates `t_{j,w,y}`, with weights `Pr(J=j,W=w,Y1=y)` pinned above. Prove a tight analytic lower bound (prefer exact algebraic certificate) and construct an attaining parameter table. Investigate whether matching the first two moments is compatible with an optimal approximation of the third; do not assume it is. Use four conditional public-prefix independent minimizations when justified by preserved W,Y1.

## Evidence and acceptance
Specify all observer fields, action policies, rate/independence constraints and TV; derive a proof of optimality or an explicitly limited counterexample; execute exact `Fraction`/symbolic or certified interval checks with actual logs; preserve P000-X6 and native BRC boundary. Store proof, runnable program, actual stdout and next question on the existing Draft PR branch; perform immutable readback and report activity/journal statuses separately. Native Source CLAIM, Result, Driver admission and X6 transfer each require their own actual authorization/proof.
