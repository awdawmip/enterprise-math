# R5 — Exact sixteen-leaf Jensen obstruction and rational convex-hull separation

Date: 2026-10-27 (Asia/Shanghai). Classification: PORTABLE AUTHOR / UNREVIEWED / NOT_ADMITTED. This is an external two-measure finite stopping model, statically tagged by native X6 Cell paths; it is not a native Heartbeat evolution, formal Task/CLAIM/Result or independent Driver finding.

## Authority, frozen sources, and typed observer

GLOBAL_KNOWLEDGE_V1 pinned main@7eaef593eacb7df71be2b29f4405e3249ab80405: bootstrap, operating manual, P000, ACTIVE worldview, mathematics/code and research-persistence rules. Project source pinned main@340fc6c451d0d0ddb2f55b5c18a60672b465d615: AGENTS, original P000, native X6/time and joint-relation preservation, portable/autonomous research. Direct predecessors: research_notes/brc_lr_adjoint_curvature_20261027_r5/PROOF.md, brc_lr_curvature_dual_ternary_chambers_20261027_r5/PROOF.md, brc_lr_affine_circuit_duality_20261027_r5/PROOF.md. Native owner task query returned CONTROL_QUOTA. Connected GitHub identity was awdawmip; no current canonical owner, CLAIM, Result or Driver authority is inferred from it. This is independently computed portable author material.

Use the positive exact BRC Q/P branch mass and full ordered history provenance; conditional hidden-kernel differences are signed observer errors, not positive mass. Observer: R_t=P(history)/Q(history), full decisions on history; seedless LR decisions on (t,R_t); terminal O=(P(D=Q),Q(D=P),E_P tau,E_Q tau). The future operation set is finite stop/continue/declare. Time t is separately typed, not a seventh spatial coordinate.

At an arbitrary six-axis native X6 Cell anchor o, the sixteen paths are three ordered *primitive* steps:
o -> o+e_g -> o+e_g+e_(3+j) -> o+e_g+e_(3+j)+d_k,
where g=A/B selects e1/e2; j=0/1 selects e3/e4; and d=(e5,-e5,e6,-e6). All sixteen terminal cells differ. These paths are static synthetic tags for external probabilities; no native transition law, plane, diagonal primitive or full-X6 physical inference is asserted.

## Sixteen-leaf strictly positive rational model

At t=1: hidden A,B, each Q=P=1/2. At t=2: j=0,1 conditional Q=P=1/2. Thus every first- and second-time history has R=1. Terminal likelihood ratios:
Y=(1/10,99/100,101/100,19/10).

Let K(p)=(p,1/2-p,1/2-p,p) for 0<p<1/2. The four history kernels use
p_A0=2/5, p_A1=3/8, p_B0=1/100, p_B1=1/50.
For g,j,k set Q(g,j,k)=K(p_gj)_k/4 and P(g,j,k)=Y_k Q(g,j,k). Because sum K(p)=sum Y_k K_k(p)=1, all 16 Q/P leaf masses are strictly positive and each measure sums to 1.

## Theorem 1 — complete Bellman and Jensen gap for a two-group family

For any strictly positive mean-one terminal kernels on the stated equal-mass branching topology and any real s>=0, minimize
J_s = P(D=Q)+Q(D=P)+s E_Q tau.
The terminal optimal declaration is Q for y<1 and P for y>1, and stopping at ratio 1 has Q-cost 1. Define
G_gj=1-E_{K_gj}[min(Y,1)]; G_g=(G_g0+G_g1)/2;
Gbar=(G_A+G_B)/2; x_+=max(x,0).

The **unrestricted** full-history and seedless-LR Bellman minima satisfy, for every real s>=0,

V_full(s)=1+s-(1/2)sum_g [ (1/2)sum_j(G_gj-s)_+ - s ]_+,    (1)
V_LR(s)=1+s-(Gbar-2s)_+.                                      (2)

Proof: At t=1, stop cost 1+s. At t=2, stop cost 1+2s; continue and terminal-Bayes declare costs 1-G_gj+3s. Thus the optimal time-2 gain is (G_gj-s)_+. A full t=1 observer with label g continues if its mean time-2 gain exceeds one extra stage cost s; averaging over A,B yields (1). A seedless LR policy cannot select the hidden g at t=1 nor j at t=2 because every observed LR equals 1. Its terminal kernel is the four-row mean, with terminal gain Gbar, and it either stops initially or samples twice; (2) follows. A possibly randomized decision has affine conditional expected cost; finite Bellman simplex minimization attains deterministic actions. Thus (1) and (2) include **all real local randomization parameters**, not just tested fractions. QED.

Under the explicitly checkable condition

G_g/2 <= min(G_g0,G_g1) for g=A,B,                     (3)

the group term in (1) equals (G_g-2s)_+ for all s>=0. If s<=G_g/2, both gains G_gj exceed s and the equality follows by averaging. At s=G_g/2 the group benefit vanishes; since (1/2)sum_j(G_gj-s)_+-s decreases with s, it cannot become positive again. Hence

V_full(s)=1+s-[(G_A-2s)_+ +(G_B-2s)_+]/2,            (4)
Delta(s)=V_LR-V_full
        =[(G_A-2s)_+ +(G_B-2s)_+]/2 -(Gbar-2s)_+ >=0. (5)

The last inequality is Jensen convexity of x -> x_+. If G_A>G_B, the **exact complete phase diagram for all real s>=0** is:
Delta=0 on [0,G_B/2];
Delta=s-G_B/2 on [G_B/2,Gbar/2];
Delta=G_A/2-s on [Gbar/2,G_A/2];
Delta=0 on [G_A/2,infinity).
It has maximum (G_A-G_B)/4 at s=Gbar/2. For the class satisfying (3), equality of every four-observer linear support direction requires G_A=G_B, a necessary condition only in this model class. The information discarded by LR is the conditional group Bayes-gain difference, made visible by early-stop options.

## Theorem 2 — actual rational separating hyperplane

For our symmetric kernels G(p)=1/200+(89/100)p. Exact values:
G_A0=361/1000; G_A1=271/800;
G_B0=139/10000; G_B1=57/2500;
G_A=2799/8000; G_B=367/20000; Gbar=14729/80000.
Both conditions (3) are strict. Gap >0 precisely on
367/40000 < s < 2799/16000.
Its maximum, at s*=14729/160000, is Delta(s*)=13261/160000.

Witness full deterministic policy: continue t=1 from A, stop t=1 from B declaring P; at t=2 continue both A children; terminal declare Q when Y<1 and P when Y>1. Direct leaf summation gives

O*=(1201/16000,3/4,2,2).
lambda*=(1,1,0,14729/160000).
lambda* · O*=40367/40000=161468/160000.

Every seedless LR policy q with arbitrary REAL local randomization, and every convex mixture of such policies, satisfies

lambda* · O(q) >= V_LR(s*)=174729/160000.

The exact rational separation gap is 13261/160000>0. Therefore
O* is NOT in conv(O_LR), so conv(O_LR) differs from O_full in this 16-leaf candidate. This is an *all-real* convex-hull exclusion, not a projection-error numerical anecdote. At s=2/25 the exact minima are V_full=15761/16000, V_LR=84471/80000 and Delta=2833/40000.

## Verification scope and next problem

The adjacent actually executed Python fractions.Fraction checker builds all 16 distinct X6-tagged positive leaf P/Q masses, verifies normalization and exact LR prefix ratios, gains, the rational four-observer separating vector, and 9 s-values including all 3 symbolic breakpoints. It enumerates 64 full binary stop/continue descriptions (using justified optimal terminal declarations) and all 144 LR deterministic descriptions: 3 actions at t=1, 3 at t=2, and 2^4 terminal declarations. All compared exact objective values match (1)-(5). Its literal stdout is in EXACT_OUTPUT.txt; the universal real claims rest on the displayed symbolic Bellman proof, not finite enumeration. Lean, independent review, native session/CLAIM and physical X6 calibration remain outside the claim.

The mother question remains to find an N>=3 strictly positive rational model with equal full/LR support hulls but unequal real seedless LR images. Use the Jensen test first to rule out differing group Bayes-gain profiles; then require *exact rational full-vector convex-hull membership* for all full extreme vectors before a real-semialgebraic image nonattainability test. See NEXT_TASK.md.
