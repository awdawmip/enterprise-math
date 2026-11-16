# R5 — Timing-tilt forcing and full-hull rigidity in a common-first-kernel two-gate BRC

Date: 2026-11-05 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Mother objective: exhibit strictly positive finite P/Q lawful stopping with conv O4(FULL)=conv O4(seedless LR) yet O4(FULL)≠O4(seedless LR), where O4=(eP,eQ,TP,TQ). Here a full model family is classified and eliminated as a source of that phenomenon. This result uses the task-frozen scientific pins GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`; current normative rules were read separately. Direct predecessor: `54bf43436208278a89ee10eb8fd57c23861f3746`.

## Model and theorem

There are finitely many hidden sources h with shared strictly positive initial P and Q weights w_h, Σw_h=1, and likelihood ratio 1 at time 1. At time 1 either stop and freely declare P/Q, or continue. Conditional on continuation, the time-2 likelihood-ratio key r_j>0 is drawn under Q from the SAME positive kernel K_j for each source; ΣK_j=1 and ΣK_j r_j=1. Assume at least two distinct time-2 ratios have positive K mass (equivalently, this common experiment is nontrivial). At every time-2 key both declarations and continuation are allowed. On continuation at (h,j), the time-3 terminal Q kernel M_hj(s)>0 on a finite declared common support satisfies Σ_s M_hj(s)=1 and Σ_s s M_hj(s)=r_j. The conditional P kernel is s M_hj(s)/r_j, hence strictly positive. At time 3 P/Q declarations are free. FULL may condition on h; seedless LR sees only (time, likelihood ratio). Independent behavioral randomizations may be arbitrary real numbers in [0,1].

**THEOREM.** Under these hypotheses the following are equivalent:

1. conv O4(FULL)=conv O4(seedless LR);
2. O4(FULL)=O4(seedless LR), with all real behavioral policies;
3. For every shared time-2 key j, M_hj is identical across all sources h.

In particular, the desired equal-hull/unequal-real-image R5 witness cannot arise in this entire common-first-kernel, nontrivial-first-experiment two-gate class. The theorem has no claim for source-dependent first K, a trivial first experiment concentrated at r=1, or more general time/history topologies.

## Proof of (3) => (2)

Take a FULL real behavioral policy. At each time-2 key j, average its STOP/P, STOP/Q and CONTINUE probabilities over sources with weights proportional to their Q occupancy w_h K_j (=w_h times a common factor), obtaining a seedless action law. This preserves time-2 P and Q stopping/continuing masses since their ratio is r_j. When M_hj=M_j for every source, it also preserves each terminal (time=3,ratio=s) Q occupation, hence P occupation. At each terminal ratio s, average the original source/path-dependent declaration probability against these Q occupations. On that fiber P=sQ, so eP,eQ and both mean stopping times are exactly preserved. Reverse inclusion holds because seedless LR is a FULL subclass.

## Proof of (1) => (3): timing tilt

Let k>0 and C_k(r)=max(-r,-k). For a normal n=(-1,-k,-a,-b) define the cost per extra stopping step c(r)=a r+b. Define

G0(k)=Σ_j K_j C_k(r_j)-C_k(1)≥0,
G_hj(k)=Σ_s M_hj(s) C_k(s)-C_k(r_j)≥0,
V_hj=G_hj(k)-c(r_j),
Y_h=G0(k)-c(1)+Σ_j K_j (V_hj)_+.

A Bellman recursion that permits STOP/P, STOP/Q and CONTINUE at both gates gives the exact support formulas

h_FULL(n)=C_k(1)-c(1)+Σ_h w_h (Y_h)_+,
h_LR(n)=C_k(1)-c(1)+[G0(k)-c(1)+Σ_j K_j(Σ_h w_h V_hj)_+]_+.

Suppose two terminal Q laws M_hj0 differ. Their stop-loss transforms E[max(-S,-k)] differ at some k>0: for finite positive laws, the right/left slopes and jumps of E[min(S,k)] recover the distribution. Since C_k(r_j0) is common, the numbers G_hj0(k) are not all equal. Choose m strictly between their minimum and maximum and parameterize
c(r)=m+a(r-r_j0), i.e. b=m-a r_j0.
Then at j0 the values V_hj0=G_hj0(k)-m include both signs, so
J_j0=Σ_h w_h(V_hj0)_+-(Σ_h w_h V_hj0)_+>0.

We can force the *first* gate to choose CONTINUE for every source without altering V_hj0:

- If r_j0≠1, take a with sign and magnitude making c(1)=m+a(1-r_j0) tend to -infinity. Since all (V_hj)_+≥0 and G0≥0, Y_h→+infinity for every h.
- If r_j0=1, the assumed nontrivial common first kernel supplies j' with r_j'≠1. Take a of the appropriate sign making c(r_j')→-infinity. Then every V_hj'→+infinity and K_j'>0, so every Y_h→+infinity, while c(1)=m stays fixed.

For finite sufficiently large |a|, all Y_h>0 and the LR first-gate advantage also is positive: Σ_j K_j(Σ_h w_h V_hj)_+≥0 and, more precisely, the positive advantages at the forcing key grow without bound in the second case; in the first case -c(1)→+infinity. Thus both classes optimally continue at time 1, and subtracting their support functions yields

h_FULL(n)-h_LR(n)
=Σ_j K_j {Σ_h w_h(V_hj)_+-(Σ_h w_h V_hj)_+}
≥K_j0 J_j0>0.

This contradicts equality of the convex hulls. The argument uses signed four-coordinate normals; neither a nor b is required to be positive because both TP and TQ coordinates are being tested as a support direction. All actual stopping actions remain lawful. Therefore (1)=>(3). (2)=>(1) is immediate. QED.

## Exact witness beyond the preceding sufficient inequality

Take source weights w_A=w_B=1/2, time-2 r=(1/2,1,3/2), and common K=(1/16,7/8,1/16). At low r use terminal ratios (1/4,3/4) with Q kernel (1/2,1/2); at high r use (5/4,7/4) with Q kernel (1/2,1/2). At middle r=1 use common terminal ratios (1/2,1,3/2), with M_A=(1/4,1/2,1/4), M_B=(3/8,1/4,3/8). All conditional P/Q masses are positive and normalized.

For k=1, G0=1/32 whereas G_A,mid=1/8 and G_B,mid=3/16, with m=5/32. Thus the earlier predecessor's sufficient inequality G0>m is FALSE (1/32<5/32). Use a=5, b=-155/32, so c(r)=5r-155/32 and n=(-1,-1,-5,155/32).

At time-2 low/mid/high the advantages are V_A=(75/32,-1/32,-85/32) and V_B=(75/32,1/32,-85/32); both sources strictly continue at time 1, with Y_A=11/512 and Y_B=25/512; seedless LR first-gate advantage is 11/512. Exact Bellman values:

h_FULL=-287/256, h_LR=-581/512, difference=7/512>0.

One optimal FULL policy: both sources CONTINUE at t=1; at t=2 both CONTINUE for r=1/2, both STOP/P for r=3/2, source A STOP/Q and B CONTINUE at r=1; at t=3 declare Q for s<1, P for s≥1. Its observer is
W=(141/256, 43/128, 79/32, 5/2).
Then n·W=-287/256 and ||n||_1=379/32. Consequently dist_infinity(W,conv O4(LR))≥7/6064.

The accompanying Python standard-library Fraction verifier checks all transition normalizations, conditional P/Q likelihood-ratio moment identities, Bellman formulas, the explicit real-lawful FULL witness, all 10,368 effective deterministic seedless LR policies, and the exact distance bound. It returns `PASS_EXACT_R5_TIMING_TILT_FULL_RIGIDITY`. The finite enumeration verifies the displayed rational instance; the quantified theorem above is proved analytically.

## Structural meaning and next unit

The four-coordinate timing normal supplies a controllable affine tilt in r. A nontrivial shared first experiment therefore exposes hidden second-gate kernel distinctions in some supporting direction, even if the ordinary classification gain G0 is too small to unlock the early gate under equal TP/TQ costs. The surviving R5 search space includes source-dependent first kernels, trivial first information gates, and richer multi-gate interactions. Next examine the degenerate K concentrated at ratio 1 and source-dependent first K by exact complete-hull certificates, before real-image nonmembership testing. BRC interface reused: source/branch occupation, positive Q weights, P=rQ moment, two-gate Bellman support, four-coordinate observer; this is a model-internal finite stochastic result, not an independent assertion about physical X6 dynamics. No mathematical admission claimed.
