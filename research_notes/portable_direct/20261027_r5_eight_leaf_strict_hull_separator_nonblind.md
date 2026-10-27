# R5 — Exact rational four-observer hull separation for the causal eight-leaf tree

Observed: 2026-10-27 (Asia/Taipei). Class: portable, nonblind mathematical crosscheck, **UNREVIEWED / NOT_ADMITTED**. This note uses and preserves the original R5 author's eight-leaf construction rather than claiming a new independent native Driver review or a new official Task/Result. It is not a native X6 dynamics law.

## Source and model

Author's immutable source: `awdawmip/enterprise-math@f4f305809dbd91ea4bbcadb3e54fdfbd73e8a40f:research_notes/brc_r5_general_hinge_zonotope_causal_8leaf_20261027/PROOF.md`, with adjacent `VERIFY.py`, `EXACT_OUTPUT.txt`, and `NEXT_TASK.md`. Global Knowledge/P000 read at `main@cdd8723f1b670a3bfe1f27075649a5b48791801d`; project source read at `f4f305809dbd91ea4bbcadb3e54fdfbd73e8a40f`. The earlier single-breakpoint 16-leaf nonblind note is distinct.

Use exactly the published two-law finite stopping tree. At t=1 the observed branches A/B have P=Q mass 1/2 each and likelihood ratio R=1. At t=2 each branch has one deterministic child A1/B1, still R=1. At t=3 each branch has four positive terminal ports with common ratios

`r=(1/4,3/4,5/4,7/4)`,

conditional Q masses `m=(9,5,11,7)/32` for A and `n=(8,8,8,8)/32` for B, and conditional P masses `r_i*m_i` and `r_i*n_i`. Both conditional laws normalize: `sum m=sum n=sum r*m=sum r*n=1`. **The first permissible stopping epoch is t=1**; terminal declaration is at t=3, and both t=1 and t=2 can stop. Do not add a root t=0 stopping action when comparing these exact policy classes.

The four-observer output is

`O=(P(D=Q), Q(D=P), E_P[tau], E_Q[tau])`.

Full-history actions can depend on A/B. Seedless likelihood-ratio (LR) actions can depend only on `(t,R_t)` and terminal ratio. Randomization is permitted, and comparison is with the **convex hull** of all seedless-LR observations.

## Theorem — this eight-leaf tree is **not** an equal-hull example

For the exact positive rational support direction

`J(O)=P(D=Q)+(3/4)Q(D=P)+(17/256)E_Q[tau]`,

one has

`min_{full-history policies} J = 208/256 = 13/16`,

but

`min_{O in conv(seedless-LR observations)} J = 209/256`.

Hence `conv(O_full)` is strictly larger than `conv(O_seedless-LR)` in this declared four-observer model: a rational separating hyperplane has a **strict gap of 1/256**. This kills this particular eight-leaf tree as a candidate for the mother question “equal four-observer support hull but unequal actual seedless-LR policy image.” It does **not** kill that general mother question, prove a uniform lower bound across trees, or promote any theorem into native admission.

## Analytic all-real proof

For `s=3/4`, the minimal immediate weighted misclassification risk at ratio R=1 is `s`, obtained by declaring P. Conditional terminal risk at branch w is `sum_i w_i min(r_i,s)`. Since the conditional P expectation is one, write `h_w=sum_i w_i max(r_i-s,0)`; then terminal risk equals `1-h_w`. Exact fractions give

`h_m=25/64`, `h_n=24/64=3/8`.

Thus the benefit of looking at the t=3 terminal outcome rather than stopping at t=1, **before** time cost, is `9/64` in A and `8/64` in B. The two-step additional Q-time cost is `2*(17/256)=17/128`, strictly between the two benefits:

`8/64=16/128 < 17/128 < 18/128=9/64`.

The full-history Bayes policy therefore continues branch A and stops branch B at t=1 (declaring P on B). On the continued A branch it declares Q for port 1 (r=1/4), P for ports 2,3,4; port 2 is an indifferent tie. This policy has the **exact** four-vector

`O_*=(9/256, 55/64, 2, 2)`,

and `J(O_*)=208/256`. Branchwise optimality proves no full-history policy can do better.

A seedless-LR policy cannot distinguish A from B at t=1 or t=2 because both have `R=1`. Its t=1 choices are: stop both (P is the optimal declaration), or continue both. A t=2 stop is strictly dominated by the same t=1 declaration because t=2 reveals no information and time cost is positive. The average look-ahead benefit of continuing both is `(9/64+8/64)/2=17/128`, exactly equal to the two-step time cost. Hence either t=1 stop-both or t=3 continue-both has identical minimal risk `209/256`. Any arbitrary real randomized seedless-LR policy, even with correlated external randomization, is a convex mixture of finite deterministic LR action tables for this linear objective and cannot decrease the minimum. This proves strict convex-hull separation, not merely a finite-grid observation.

For independent reproducibility, the 20 seedless deterministic tables consist of four `(t=1/2,declare=P/Q)` stops plus 16 terminal Q/P mappings. Full deterministic tables are the 20 by 20 A/B combinations, 400 in total. Exact `fractions.Fraction` enumeration yields minima `208/256` and `209/256`; three seedless tables tie for the latter (stop P at t=1, and the two terminal rules that differ only at the tied r=3/4 port).

## Compact exact Python reproducer

```python
from fractions import Fraction as F
from itertools import product
r = (F(1,4),F(3,4),F(5,4),F(7,4))
m = (F(9,32),F(5,32),F(11,32),F(7,32))
n = (F(1,4),)*4
qs = (tuple(x/2 for x in m),tuple(x/2 for x in n))
ps = tuple(tuple(x*y for x,y in zip(r,q)) for q in qs)
assert all(sum(x,F())==F(1,2) for x in qs+ps)
actions = [('stop',t,d) for t in (1,2) for d in ('P','Q')]
actions += [('terminal',ds) for ds in product(('P','Q'),repeat=4)]
def obs(b,a):
    p,q=ps[b],qs[b]
    if a[0]=='stop':
        t,d=a[1:]
        return (sum(p,F()) if d=='Q' else F(),
                sum(q,F()) if d=='P' else F(),
                t*sum(p,F()),t*sum(q,F()))
    ds=a[1]
    return (sum((x for x,d in zip(p,ds) if d=='Q'),F()),
            sum((x for x,d in zip(q,ds) if d=='P'),F()),
            3*sum(p,F()),3*sum(q,F()))
def add(u,v): return tuple(x+y for x,y in zip(u,v))
def J(x): return x[0]+F(3,4)*x[1]+F(17,256)*x[3]
full=min(J(add(obs(0,a),obs(1,b))) for a in actions for b in actions)
lr=min(J(add(obs(0,a),obs(1,a))) for a in actions)
w=add(obs(0,('terminal',('Q','P','P','P'))),obs(1,('stop',1,'P')))
assert (len(actions),full,lr,w)==(20,F(13,16),F(209,256),(F(9,256),F(55,64),F(2),F(2)))
print('full',full,'seedless convex-hull',lr,'strict gap',lr-full)
```

Expected stdout: `full 13/16 seedless convex-hull 209/256 strict gap 1/256`.

## Provenance, boundary, and next question

Author-derived source construction is credited to the R5 hinge-zonotope note. The present separation and independently executed 400/20 Fraction audit are a **nonblind portable extension**, not the prior author's reviewed conclusion. No native RESEARCH_DRIVER session/DA/CLAIM, exact-set reference passes, Source Result freeze, or Driver follow-up publication is inferred from GitHub storage. This note has no power to modify existing reviewer/author histories.

P000 and ACTIVE native-X6 worldview remain fixed; the P/Q tree is a declared external stochastic observer model. Positive P/Q masses are not signed defects, and signed terminal hinge differences remain observer errors, not native physical laws. The R5 next research unit should discard this exact eight-leaf tree and seek other strictly positive trees surviving **all** four-observer hull directions; only then investigate seedless-LR image nonattainability by exact all-real methods. Existing author-level tasks should be deduplicated against this certificate, not replicated or converted into official V2 tasks without native admission.
