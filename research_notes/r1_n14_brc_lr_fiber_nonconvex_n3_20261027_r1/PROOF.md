# R1/N14 — LR-constant fibers still permit nonconvex two-law terminal images at N=3

Date: 2026-10-27. Evidence class: AUTHOR MATHEMATICAL PROOF + EXECUTED EXACT RATIONAL CHECK; no native Result/CLAIM, independent Driver review, Lean formalization or P000/X6 correspondence.

## Frozen source and question

GLOBAL_KNOWLEDGE_V1 main@`8ec98188025f60aafe48055520ba3a57c29cdb2c`; P000 projection checked against original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`; Enterprise Math initial scientific snapshot main@`dffe386cee25fb9c650d4aa46ff6f501c3745e8a`. Exact predecessors: `research_notes/r1_n14_brc_two_law_fresh_coin_nonconvex_n2_20261027_r1t11/PROOF.md` and `research_notes/brc_n3_predecessor_kernel_rank_tv_20261027_r5/PROOF.md`. Current `docs/PORTABLE_RESEARCH_PROTOCOL.md` applies.

Let P,Q be strictly positive rational probability laws on a finite symbol tree. A time-typed x(h) updates deterministically from its current value and next symbol. On **every** fiber `x(h)=x(h')`, assume Q(h)/P(h)=Q(h')/P(h'). A quotient stopping/decision policy sees only x, uses a new fresh random coin at each state, retains no ex-ante lottery selector, and applies the SAME kernel under both laws. Its observer reports `(T,o(x(H_T)),D)`. Is the joint P/Q attainable observer set convex?

We prove: the answer is **NO at N=3**, even under the LR-constant-fiber restriction. But **YES for N<=2** under the same one-root conventions, so N=3 is sharp in horizon for general finite non-IID laws. This is not a claim about the narrower IID subclass.

## Theorem A — N<=2 joint convexity under terminal LR constancy

At N<=2 assume only that each final time-2 fiber x=y has constant Q/P ratio r_y (the stronger LR-on-all-fibers condition certainly implies this). Then the paired attainable image of fresh-coin x-only policies for the full observer `(T,x,D)`, and hence every coarsening, is convex.

**Proof.** Take any two quotient policies A,B and lambda in [0,1]. Let u_A,u_B be root continuation probabilities, and let u=lambda*u_A+(1-lambda)*u_B. Mix root stopping-decision masses linearly. For every time-1 state x, when u>0 set

`pi_C(action|x)=[lambda*u_A*pi_A(action|x)+(1-lambda)*u_B*pi_B(action|x)]/u`.

When u=0 time-1 kernels do not matter. For each *ordered* length-one history h, multiplication by u shows that all survival, continuation and stop-decision probabilities of C are exactly the appropriate mixtures pathwise, without regard to whether P or Q supplies its cylinder mass. Consequently the law-weighted incoming mass at each terminal time-2 compressed state y satisfies

`m_L,C(y)=lambda*m_L,A(y)+(1-lambda)*m_L,B(y), L=P,Q.`

For m_P,C(y)>0 choose C's terminal decision distribution by P-incoming-mass weighting,

`pi_C(d|y)=[lambda*m_P,A(y)*pi_A(d|y)+(1-lambda)*m_P,B(y)*pi_B(d|y)]/m_P,C(y).`

Use any distribution if the denominator is zero. Since Q(h)=r_y*P(h) on every history h reaching y, `m_Q,s(y)=r_y*m_P,s(y)` for s=A,B,C. Thus the SAME law-independent kernel matches the Q terminal decision masses. Root and time-one terminal masses already matched pathwise. All full `(T,x,D)` masses under P and Q are the prescribed convex mixture. The N=0,1 cases omit the terminal time-2 step. QED.

## Theorem B — exact LR-fiber-constant N=3 nonconvexity witness

Alphabet `{0,1,2}`, horizon N=3. The first two symbols are each uniform on `{0,1,2}` under both laws, conditional on any preceding observations. At the third draw the strictly positive conditional law depends only on the FIRST symbol i:

| i | P(last=0,1,2 | i) | Q(last=0,1,2 | i) |
|---|---|---|
| 0 | `(1/4,1/4,1/2)` | `(1/2,1/4,1/4)` |
| 1 | `(1/12,3/4,1/6)` | `(1/6,3/4,1/12)` |
| 2 | `(1/6,1/2,1/3)` | `(1/3,1/2,1/6)` |

For every first symbol i, the Q row is the P row multiplied componentwise by `r=(2,1,1/2)`. Every row is positive and sums to one. P is not Q. Hence every prefix h of length <=2 has Q(h)/P(h)=1, and each full length-3 history ending in symbol j has Q(h)/P(h)=r_j.

Define the time-typed recursive compression

`x(empty)=(0,*), x(i)=(1,i), x(ia)=(2,*), x(iaj)=(3,j).`

Here the time-one state remembers the first symbol; all time-two histories collapse to a single state; each terminal time-three state remembers only the last symbol. The map is recursively updatable from current x and next symbol, and the ratio Q/P is constant on **every** x fiber. Set `o(t,z)=z`, and report T separately. The observer sees the first symbol at T=1, sees * at T=2, and sees the last symbol at T=3.

Two admissible deterministic quotient policies (fresh-coin family includes deterministic endpoints):

* **A**: at t=1 continue iff first i=0, otherwise stop D=0; at t=2 continue surely; at t=3 stop D=1.
* **B**: at t=1 continue iff first i=1, otherwise stop D=0; at t=2 stop D=0 surely.

Let M denote the midpoint of A and B's paired terminal-observer probability vectors. Under both P and Q the t=1 stop masses with D=0, indexed by first symbol i=0,1,2, are exactly `(1/6,1/6,1/3)`. The t=2 stop D=0 mass is `1/6` and total t=3 mass is `1/6`, all with D=1. At t=3 last symbol j=0, M has mass `1/24` under P and `1/12` under Q.

Consider any x-only common fresh-coin policy C realizing M. Let c_i be its time-one probability of continuing after symbol i. Each first symbol i has probability 1/3 and is individually observable when T=1. The three required t=1 stop masses force

`c_0=c_1=1/2, c_2=0.`

All length-two histories occupy the unique state x=(2,*), so C must use a SINGLE common time-two continuation probability c. The mass reaching time two is `(1/3)*(c_0+c_1+c_2)=1/3`. As M requires total T=3 mass 1/6, necessarily `c=1/2`.

The forced total terminal mass with final j=0 is then, under P,

`(1/3)*(1/2)*(1/2)*(1/4+1/12) = 1/36,`

and under Q,

`(1/12)*(1/2+1/6) = 1/18.`

These are strictly below M's required terminal **D=1** masses `1/24` and `1/12`. The respective exact deficits are

`1/24-1/36=1/72 (P); 1/12-1/18=1/36 (Q).`

No choice of terminal D kernel can create additional arrival mass at j=0. Thus **every real-valued permitted quotient policy fails**; this is a universal algebraic impossibility certificate, not failure to find a solution on a finite grid. M lies outside the quotient image although A,B lie inside. So the paired image is NONCONVEX. Combined with Theorem A, N=3 is horizon-minimal for the stated LR-fiber class. QED.

## Method reuse, exact validation, and boundary

This is positive-rational **BRC ordered-path** arithmetic. The t=2 state erases first-symbol provenance: the Q last-symbol predecessor kernels at i=0 and i=1 differ, with exact total variation distance 1/2. We **reuse the rank/minor algebra** of `research_notes/brc_n3_predecessor_kernel_rank_tv_20261027_r5/PROOF.md` but do **not** conflate that source's predecessor *LR classes* with our first-symbol predecessor *state labels*. Rank failure alone would not establish image nonconvexity; the forced-observer contradiction above supplies the genuinely additional no-go.

The actually executed standalone `VERIFY.py` uses CPython `fractions.Fraction` and exhausts all `1+3+9+27=40` ordered prefixes. It checks positive normalized P/Q kernels, path probability recursion, recursive x update, LR constancy within **every** compressed-state fiber, both deterministic source strategies and their midpoint, and both exact gaps. `RESULT.json` contains its actual stdout. The infinite family of permissible **real-valued** quotient kernels is excluded by the handwritten proof rather than by those finite tests. Independent review, Lean proof, native X6 embedding and canonical mathematical acceptance remain pending.

Method/tool reuse: `REUSE_APPLIED` for BRC positive-rational ordered paths and predecessor-kernel rank/minor; `NO_NEW_TOOL_FAMILY`. No IID theorem, signed/complex BRC cancellation or physical inference is claimed.

## Next scientific question

Whether nonconvexity persists for positive **IID** P/Q with LR-fiber-constant recursively updated x and a coarse observer. Find an exact N>=3 witness with an all-real certificate, or prove an explicitly specified subclass convex. Distinguish fresh-coin-only from persistent ex-ante selector policies; see `NEXT_TASK.md`.
