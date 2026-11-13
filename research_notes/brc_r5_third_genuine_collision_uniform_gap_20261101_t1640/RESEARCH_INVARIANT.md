# R5 supplement — law-proportional delay cone has a signed annihilator; the three-key hull gap is uniform for arbitrary delay length

**Date:** 2026-11-01 Asia/Shanghai. **Status:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This supplements this directory's RESEARCH.md and strengthens its one-unit-delay lower bound. The same frozen GLOBAL_KNOWLEDGE_V1 main@7e623e2746c8af0a97a8b6fcff6ebf7f93f2dff0 and Enterprise Math main@c1b3200a053883f81951d54f5d55356daec114ce govern. This concerns only an auxiliary classical finite two-law stop model; no native BRC–Shor or HEARTBEAT_WORLD computation is asserted.

## Invariant (law-proportional pure-delay lemma)

Suppose a source-labeled event has P/Q entry masses with ratio R>0. Replace its deterministic terminal time by any source-specific, integrable random delay whose conditional delay law is the same under P and Q for that source, without changing its terminal answer. Then its additional expected stop times obey ΔTP = R ΔTQ, while eP,eQ are unchanged. Consequently the linear signed observer H_R=cP eP+cQ eQ+TP-R TQ has unchanged value for arbitrary fixed cP,cQ; any equivalent multiple also works. The proof is sourcewise: ΔTP=P(entry)*E[delay|source], ΔTQ=Q(entry)*E[delay|source]. If many affected sources all share R, contributions still cancel after summation. **Equality of the conditional delay laws, not merely matching incoming likelihood ratio, is required.** P/Q-dependent future nature may invalidate the invariant. This is a reusable positive branch-flow/dual-annihilator lemma, not a declaration that source-level flow information is globally redundant.

## Application: exact all-real separation independent of epsilon and delay h

In the three-key model of RESEARCH.md, both A-tail-P sources reach the genuine decision key K=(3,8/5), with identical conditional sourcewise P/Q delay laws. Continuing from K may delay the final answer-P time by any positive integer h instead of h=1, while thinning nature probability satisfies 0<epsilon<1. The four-observer change involves lambda=h*epsilon and changes only expected stopping times. The signed direction

    H(O)=5 eP+5 TP-8 TQ,    H=(5,0,5,-8)

annihilates the perturbation source by source. For LR the time-delay direction for one unit is V=(0,0,1/20,1/32), with H·V=5/20-8/32=0. The same calculation holds for arbitrary FULL k1,k2; also for arbitrary sourcewise law-neutral finite-mean delays that always end in answer P. In that broader generality, retaining rank four requires a separate assumption, e.g. that an immediate stop at K recovers the original full-rank slice.

Sourcewise accounting under P and Q gives the **all-real FULL support polynomial**, for p1,p2,q1,q2,qB,r in [0,1]:

    H_FULL=-33/8+SUM_(i=1,2)[13 p_i/16-p_i q_i/8+q_i/8]-qB/4+(5/2)r.

Each A source contributes -9/16+13 p_i/16-p_i q_i/8+q_i/8; B contributes 2-qB/4; C contributes -5+(5/2)r. Each bracket is p_i(13/16-q_i/8)+q_i/8 >=0 and -qB/4 >=-1/4. Consequently min_FULL H=-35/8 for every epsilon and h. The minimum occurs at p1=p2=q1=q2=r=0, qB=1, and at K one may set k1=k2=1 (immediate stopping), giving the lawful explicit FULL witness

    Wstar=(4/5,7/32,21/8,43/16),    H(Wstar)=-35/8.

The LR coupling p1=p2=p, q1=q2=qB=q yields exactly, for **every** real p,q,r,k in [0,1],

    H_LR=(-33+13p-2pq+20r)/8
        =-33/8 + p(13-2q)/8 +(5/2)r.

Because 13-2q >=11, the exact LR minimum is min_LR H=-33/8, attained when p=r=0. The minimum of a linear functional over its image equals the minimum over the image's convex hull. Therefore **the exact FULL versus LR signed support gap in direction -H is 1/4** for every real epsilon in (0,1), every integer h>=1 and all real policy parameters. This strengthens the first note's nonannihilating inverse-chart bound (118-39epsilon)/236.

Since ||H||_1=18, every Z in the entire LR convex hull obeys

    ||Wstar-Z||_infinity >= [H(Z)-H(Wstar)] / 18 >=1/72.

The same 1/72 bound applies for the corresponding legal FULL witness with any finite-mean sourcewise law-neutral K-only delay, even if its observed coordinates change, provided the terminal answers remain P. The explicit K stop/continue model retains affine rank exactly four for all epsilon,h because selecting k=1 restores the predecessor LR chart with determinant 59/20480.

## Exact verification, scope and next unknown

VERIFY_INVARIANT.py imports the exact sibling VERIFY.py, uses fractions.Fraction and checks all 2^5 LR and 2^9 FULL Boolean corners of the signed support polynomial identities (544 exact checks). Each polynomial is multi-affine in the declared behavioral parameters and the effective lambda, so all corners together with the direct degree bound establish identities for **all real parameters**, rather than merely finite examples. The program also exhausts 16 LR and 256 FULL pure strategies at each of five strict-positive eps=1/2 configurations with h in {1,2,3,5,10}, totaling 1360 exact regression evaluations; actual stdout appears in INVARIANT_OUTPUT.txt. The more general finite-mean random-delay lemma is proved by conditional expectation sourcewise, not by numerical sampling.

These results exclude only time-only, terminal-P-preserving, sourcewise P/Q law-neutral downstream K delay repairs. They do not exclude a third key with law-sensitive downstream nature, changed terminal answer or rotated source advantage, and do not establish the R5 mother target, native X6/BRC or independent scientific admission. The next unit must change signed support geometry instead of merely increasing the duration of a law-neutral tail.
