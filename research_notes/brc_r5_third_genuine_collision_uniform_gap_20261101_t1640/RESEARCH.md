# R5 — A genuine third time–likelihood-ratio collision retains a uniform convex-hull gap

Date: 2026-11-01, Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is a finite classical two-law auxiliary stopping model; no native X6/heartbeat or typed BRC arithmetic is claimed.

## Frozen inputs and actual authority
GLOBAL_KNOWLEDGE_V1 canonical main@7e623e2746c8af0a97a8b6fcff6ebf7f93f2dff0: 00_BOOTSTRAP.md, OPERATING_MANUAL.md, ACTIVE worldview, BRC and mathematical/portable-research routing. Enterprise Math canonical main@c1b3200a053883f81951d54f5d55356daec114ce: AGENTS.md, P000, ACTIVE worldview, joint-observer preservation and portable research protocol. The exact predecessor is PR #1663 commit 6053f56ed68d9a045823515e13c1fd39f8538beb, research_notes/brc_r5_second_source_terminal_split_20261101_t1540/RESEARCH.md and VERIFY.py. Current native owner lookup returned CONTROL_QUOTA; no authenticated live owner, CLAIM, Result or independent review was obtained. Protected P000 and worldview remain unchanged.

## Question
The R5 mother target asks for a strictly positive, time/P-over-Q-likelihood-ratio stopped two-law process in which the four LR observer coordinates (eP,eQ,TP,TQ) have affine dimension four; the FULL/LR convex hulls coincide for every real behavioral policy; yet their actual real observation images differ. Here we ask whether a *third genuine shared time/LR stopping key*, modifying stop time but not terminal answer, suffices to erase the two-key gap. We prove a continuous-family NO-GO, not an impossibility theorem for all third-key models.

## Source-labeled exact probability model
Initial source P/Q masses: A1=(1/8,1/8), A2=(1/8,1/8), B=(1/4,1/8), C=(1/2,5/8). At time 1, A1/A2 meet at I=(time=1,likelihood-ratio=1), independently stopping with answer P under FULL probabilities p1,p2. Continuing A paths take nature high with P/Q probabilities (1/2,3/4), stopping at time 2 with answer Q; low with probabilities (1/2,1/4) reaches time-2 J. B also reaches J. Its true shared key is J=(2,2); FULL probabilities of stopping with answer P are q1,q2,qB. B continuing at J stops time 3 with answer P.

Each A continuing at J has *identical, strictly positive* response fractions: tail P has conditional P/Q mass (2/5,1/2), tail Q has conditional P/Q mass (3/5,1/2); tail Q stops time 3 answering Q. For any real 0<epsilon<1, split each A-tail-P mass by a new nature event with the same P/Q probabilities (1-epsilon, epsilon). The direct part stops time 3 answering P; the epsilon part from BOTH sources enters the third common key K=(3,8/5). FULL stopping probabilities at K are k1,k2; stop answers P at time 3, continue deterministically to time 4 and answer P. C independently stops at time 1 with answer Q, probability r, otherwise at time 3 with answer P. Every behavioral coin is shared between the two laws, even when FULL conditions it on hidden source.

The LR policy identifies p1=p2=p, q1=q2=qB=q, k1=k2=k, with independent r. FULL retains all eight parameters. Before its direct/K split, each A-tail-P source has exact masses
    P_i=(1-p_i)(1-q_i)/40,
    Q_i=(1-p_i)(1-q_i)/64,
so the incoming key K always has P/Q=8/5, independent of prior behavioral choices (for reachable positive masses). I and J likewise have ratios 1 and 2. Other time-3 terminal ratios are 12/5 for A-tail-Q (answer Q), 2 for B-tail-P (answer P), and 4/5 for C-tail-P (answer P). The direct and K-stop events share (3,8/5) and both answer P; time 4 has (4,8/5) answer P. Thus no equal (time,LR) key demands different answer maps. All *nature* transition alternatives have strictly positive P and Q probabilities for epsilon in (0,1), and no policy key repeats along one trajectory. Source/path labels are retained in the model; projection to the four observers is declared and scoped.

## Exact theorem — full-rank strict separation for every real epsilon in (0,1)
Define eP=Pr_P(final answer P), eQ=Pr_Q(final answer Q), TP=E_P(stop time), TQ=E_Q(stop time). The LR observation image has affine rank exactly four. The legal deterministic FULL observation
    W=(27/80,53/64,29/16,49/32)
has for every real epsilon in (0,1) the exact certified lower bound
    dist_infinity(W,conv(LR)) >= (118-39 epsilon)/15520 >79/15520.
Furthermore, the signed support advantage of FULL over LR in direction minus L below is at least (118-39 epsilon)/236 >79/236. Consequently the FULL and LR convex hulls are unequal in this entire genuine three-key positive-nature family.

## Proof: all-real polynomial identity and four-rank slice
In the predecessor at identical tails a=2/5 and d=1/2, the LR observation has multi-affine form
    O_old(p,q,r)=O0+p B+q C+pq D+r E.
Its affine determinant is
    det[B C D E]=(199-140a-50d)/40960=59/20480, not zero.
In the new model the two A-tail-P masses give exactly one additional unit of stop time when K continues. Summing both A sources yields the exact identity, for all real p,q,r,k,epsilon in [0,1],
    O_new=O_old+epsilon(1-p)(1-q)(1-k) V,
    V=(0,0,1/20,1/32).
At k=1, the old entire rank-four subset is recovered, so the new LR image has full affine rank 4. This argument does not assume injectivity of the new four-parameter chart.

## Proof: exact signed support certificate
Define the old chart inverse row
    L=(-1760/59,-1392/59,-400/59,328/59)
and affine functional s(O)=L dot (O-O0). The predecessor chart gives s(O_old)=p q. Direct rational arithmetic gives
    L dot V=(-400/59)(1/20)+(328/59)(1/32)=-39/236.
Therefore the *exact all-real identity* is
    s(O_new)=p q - (39 epsilon/236)(1-p)(1-q)(1-k).
Because p q is nonnegative and the second product lies between zero and 1, its exact minimum over the entire real LR behavior cube is -39 epsilon/236, attained at p=q=k=0 (r arbitrary). The linear functional has that same exact minimum on the whole LR convex hull.

The FULL strategy (p1,p2,q1,q2,qB,r,k1,k2)=(0,0,1,0,0,1,1,1) gives W above. Its added time shift vanishes for every epsilon, and direct source mass accounting yields s(W)=-1/2. Thus every Z in conv(LR) satisfies
    s(Z)-s(W) >= 1/2-39 epsilon/236=(118-39 epsilon)/236 >79/236.
Taking signed support direction -L proves strict convex-hull separation. Since ||L||_1=3880/59, Holder's inequality yields
    ||W-Z||_infinity >= (s(Z)-s(W))/||L||_1
                        >= (118-39 epsilon)/15520 >79/15520.
No finite sampled direction search is needed. QED.

## Executable exact verification and inference boundary
VERIFY.py is an executed standalone Python fractions.Fraction proof check. It evaluates the full probability-flow observer independently, checks 32 Boolean corners of the five-variable identity, and checks rank, the FULL witness, signed functional and exact minimum for four rational epsilon settings. The degree of each variable p,q,r,k,epsilon is at most one on any trajectory (policy key encountered once and a single nature split); therefore the two compared formulas are multiaffine. Equality at all 2^5 Boolean corners proves the polynomial identity for *all real* arguments. It additionally examines all 16 deterministic LR and all 256 deterministic FULL policies at each of four epsilon values: 1088 exact deterministic strategy regression evaluations. These regressions are distinct from the all-real analytic proof, and do not purport to validate native X6 or physical time. EXACT_OUTPUT.txt preserves the actual stdout for the exact remote verifier source.

## What was excluded, and what is still open
Adding a real third source-shared stop-time key by nature-thinning a common terminal-P tail cannot repair the prior signed convex-hull gap, even if epsilon tends to 1. The third key affects the existing inverse-chart normal by at most 39/236, less than the explicit FULL witness advantage 1/2. This does not imply *all* three-key couplings are impossible. A next candidate must change source-conditional support geometry, not merely add a bounded one-unit delay with unchanged answer. The original R5 mother objective remains OPEN. Author proof, exact arithmetic, native Result and independent review are separate states.
