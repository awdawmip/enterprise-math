# R5 — Adaptive four-observer separator survives K P-delay homogenization

Date: 2026-11-02 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Scientific inputs remain frozen at GLOBAL_KNOWLEDGE_V1 main@a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math main@86149263e38c22292c9def1e0f69092efa1be77e. Immediate exact predecessor: EM commit 4b09c535da2ce38cec946fdb56fdc10470b6b832, research_notes/brc_r5_k_answer_j_facet_20261102_turn11. Current norms read separately from canonical main: GLOBAL 00_BOOTSTRAP / OPERATING_MANUAL; EM RESEARCH_CONTINUATION_PROTOCOL#current-normative-context, P000, ACTIVE worldview, PORTABLE_RESEARCH_PROTOCOL, method and BRC priority.

## Exact two-law stopping model

Shared true-time/likelihood-ratio decision keys I=(1,1), J=(2,1), K=(3,1). Under both P and Q, initial masses 1/2 at I, 1/4 at J via B, 1/4 at K via C. An I continuation branches fairly to J via I or K via I. A J continuation branches fairly to a final time-3 answer or K via BJ/IJ. Stopping at I/J/K returns P at its key time. J final-answer probabilities (p=P(answer P), q=Q(answer P)) are (3/5,2/5) for both sources; K continuation has (p,q)=(1/2,1/2) at time 4/5. K time-5 probabilities: P=t for all four sources C/I/BJ/IJ; Q=(1/8,1/4,1/6,1/3), respectively. All natural P/Q branch and answer probabilities are strictly positive for 0<t<1. Source-labelled BRC flows are kept until the observer.

FULL strategy (x,jB,jI,kC,kI,kBJ,kIJ) ranges over [0,1]^7; LR strategy (x,y,z) ranges over [0,1]^3 and imposes jB=jI=y and all four k=z. The four-observer vector O=(eP,eQ,TP,TQ) has eP=P(answer P), eQ=Q(answer Q), and TM=E_M(terminal time). This is an auxiliary BRC probability model; native X6/HB embedding is not asserted.

## Theorem — complete all-real positive gap in a moving support normal

For every t in [0,1], with strict model positivity on (0,1), define
n(t)=(15-72t,10-48t,-12,12)=(5-24t)*(3,2,0,0)+(0,0,-12,12).

Then the exact support functions over ALL REAL behavioral policies satisfy

    h_LR(n(t))=15-72t,
    h_FULL(n(t))=15-72t+5/16,
    Delta(n(t))=5/16.

An explicit FULL witness, valid for every t, uses
(x,jB,jI,kC,kI,kBJ,kIJ)=(0,0,0,1,0,1,0) and yields

    W(t)=(57/80,27/80,3*(t+9)/8,167/48).

Consequently
dist_infinity(W(t),conv(LR)) >= 5/[16*(5*abs(5-24t)+24)].

At t=1/2: n=(-21,-14,-12,12), W=(57/80,27/80,57/16,167/48),
h_LR=-21, h_FULL=-331/16, distance at least 5/944.
At t=5/24: n=(0,0,-12,12); the unscaled TQ-TP support gap is 5/192,
and the L-infinity distance bound is 5/384. Both parameters are strictly interior.

## All-real algebraic proof

Put B(t)=15-72t and S=n(t)·O-B(t). Direct backward substitution through the complete source-resolved P/Q probability flow gives the identity for EVERY real FULL strategy:

  16*S_FULL =
      jB+(1-jB)*kBJ+4*kC
      -(1-x)*(3*(jI+kIJ-jI*kIJ)+2*kI)-5*x.

The expression is independent of t. The first term is at most 1, kC<=1,
and all subtracted terms are nonnegative because jI+kIJ-jI*kIJ>=0.
Hence S_FULL<=5/16 and the stated explicit FULL policy attains 5/16.

For EVERY real seedless-LR behavioral policy, the same expression becomes

  16*S_LR = -(1-z)*(2*y+x*(5-3*y)) <= 0.

Equality holds for z=1. Thus both maxima, and the gap, are exact.
The distance follows by Holder duality with ||n(t)||_1=5*abs(5-24t)+24.
No finite signed-direction sweep or interpolation from samples is used for the universal inequality.

The previous fixed mixed normal n_old=(2,-1,1,0) has equal FULL/LR
support after homogenizing all K P-delays: at any K source the signed
stop/continue payoffs are respectively 5 and 9/2+t; at J the stop payoff is
4 and both final J-answer payoffs are 18/5. Every downstream Bellman
maximization therefore admits identical optimal decisions for all sources
at a shared key (and I is one shared key). This proves equality in n_old
for all t; our adaptive direction exposes the surviving source residual.

## Four-dimensional structure survives for all t

The five LR deterministic corners 000,001,010,100,101 have exact
four-dimensional affine determinant 3/8192. The FULL observation map at
the interior parameter point (1/2,...,1/2) has Jacobian minor on columns
(x,jB,jI,kC) exactly -1/81920. Each corner observation and each Jacobian
column is affine in t, hence each determinant has degree at most four.
The independent standard-library Fraction checker verifies both stated
constant determinants at the five distinct exact nodes
t=0,1/4,1/2,3/4,1; degree<=4 polynomial identity makes the determinants
constant for every real t. They are nonzero throughout (0,1).

The verifier also exhausts all 128 FULL and 8 LR deterministic policy
corners at the five interpolation nodes, checking both direct score
identities. Each score identity is polynomial degree<=2 in t and
multiaffine in behavioral variables; exact corner coverage therefore
checks the complete real-domain algebra. Four distinct noncorner
regressions and explicit witnesses provide further checks. The direct
factorizations above are the load-bearing support proof.

## Verification, provenance, reusable information and next question

Actually executed standalone Python 3 standard-library Fraction script:
VERIFY.py. Captured stdout: EXACT_OUTPUT.txt. Assertions=1402,
complete source-resolved flow evaluations=757, final marker
PASS_EXACT_R5_COMMON_P_DELAY_ROTATING_OBSTRUCTION_AND_RANK4.

BRC interface applied (REUSE_APPLIED): strictly positive labelled
P/Q mass flow, provenance C/I/BJ/IJ, true-time/LR keys and explicit
four-dimensional observer. The common-P delay route is now exactly
excluded from the mother target of equal four-observer hulls with
unequal real images; the mother problem remains open. Next explore
independent Q time-delay and source-specific P perturbations and run
complete 128-to-8 exact rational convex-combination/Farkas screening
before seeking real-image nonmembership.

At this observation, GitHub login awdawmip has repo push access.
Connected Sites gateway reports static_machine_readonly,
research_authority_granted=false, write_relay_enabled=false. Owner list
lookup returned CONTROL_QUOTA; native owner/CLAIM/Result/Driver review
was not established. This branch result is author-side provenance only.
No P000/worldview change, private credentials, or permission mutation.
