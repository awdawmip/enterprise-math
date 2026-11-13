# R5 — Source-asymmetric terminal tails cannot repair the third-key separation

Date: 2026-11-01 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Immutable scientific inputs and typed scope

GLOBAL_KNOWLEDGE_V1 main@9bbf60485958d1b838ac447bd8322e2a135c0d64 (canonical 00_BOOTSTRAP.md, OPERATING_MANUAL.md, ACTIVE worldview, mathematics/BRC/activity rules). Enterprise Math main@813d9a8c66c9facccbafd5492d439f1288ade1cd (P000, current project and portable research rules). Predecessor: PR #1663 head f41b34020195656248f6f41d416922c08f35e0ff, research_notes/brc_r5_law_sensitive_answer_changing_20261101_t1740/RESEARCH.md, VERIFY.py and EXACT_OUTPUT.txt.

This is an auxiliary classical finite two-measure stopping model, not a native Heartbeat/X6 implementation or a P000 assertion. The BRC reuse is precise nonnegative P/Q source/path branch mass and typed observer O=(eP,eQ,TP,TQ), not a native toolbox execution. A signed dual linear form is applied only after observer projection; masses do not become signed.

## Model and source-specific final tail

Initial P/Q masses: A1=(1/8,1/8), A2=(1/8,1/8), B=(1/4,1/8), C=(1/2,5/8). A1/A2 meet at decision I=(time 1,LR 1), then via a low nature branch at J=(2,2), then via a tail-P path at K=(3,8/5). At I, origin i stops P at t=1 under p_i; continuing nature sends high (P/Q conditional 1/2,3/4) to Q answer t=2 and low (1/2,1/4) to J. At J q_i stops P at t=2; continuing nature sends tail-Q (3/5,1/2) to Q answer t=3 and tail-P (2/5,1/2) to a final split, fraction 1-epsilon answering P at t=3 and epsilon reaching K. At K k_i stops P at t=3; otherwise source i enters its own fixed conditional terminal mechanism. B at J has (1/4,1/8), and chooses stop P at t=2 with qB or P at t=3. C with (1/2,5/8) stops Q at t=1 with r or else P at t=3. Each real policy parameter lies in [0,1], identically used under P/Q. FULL may use p1,p2,q1,q2,qB,r,k1,k2. LR has p1=p2=p, q1=q2=qB=q, k1=k2=k, and r.

The source-i continuation at K contains no further *behavioral* decision; it can be source-specific and P/Q-law-specific. Define u_i=Pr_P(final answer Q | K continued, source i), dPi=E_P(T-3 | K continued,i), dQi=E_Q(T-3 | K continued,i), all finite. Require valid positive P/Q branch masses and terminal-answer consistency at any coincident (time,LR) terminal key. Let gamma_i=-u_i+dPi-dQi and alpha_i=epsilon gamma_i. Let O=(Pr_P(answer P),Pr_Q(answer Q),E_P T,E_Q T), H=5eP+5TP-8TQ.

## Main theorem — exact all-real gap monotonicity

For any 0<epsilon<1, all such source-specific fixed terminal mechanisms, and **all real** legal behavioral policies,

min_FULL H = -35/8 + [min(0,alpha1)+min(0,alpha2)]/8;

min_LR H = -33/8 + min(0,alpha1+alpha2)/8.

Therefore the exact signed FULL-over-LR support gap in direction -H equals

G = min_LR H - min_FULL H
  = 1/4 + {min(0,alpha1+alpha2)-min(0,alpha1)-min(0,alpha2)}/8
  >= 1/4.

If alpha1 and alpha2 are opposite in sign, G=1/4+min(|alpha1|,|alpha2|)/8; otherwise G=1/4. The whole FULL/LR four-observer convex hulls are **strictly different**. LR four-dimensional affine rank is exactly 4 (the k=1 slice has coefficient determinant |det|=59/20480). Every FULL H-minimizing witness W obeys dist_infinity(W,conv LR)>=G/18>=1/72.

### Proof

Before the K decision, origin i has P mass x_i=epsilon*(1-p_i)*(1-q_i)/40 and Q mass (5/8)x_i, so its likelihood ratio is 8/5. Relative to stopping P at time 3, source-i continuation changes eP by -x_i u_i, TP by x_i dPi, and TQ by (5/8)x_i dQi, multiplied by (1-k_i). Hence delta H=5*x_i gamma_i*(1-k_i)=alpha_i*(1-p_i)*(1-q_i)*(1-k_i)/8. The exact positive-flow enumeration of the unchanged I/J/B/C branches yields

H_FULL=-33/8 + SUM_i{13*p_i/16-p_i*q_i/8+q_i/8+alpha_i*(1-p_i)*(1-q_i)*(1-k_i)/8}-qB/4+5*r/2.

LR restrictions produce

H_LR=-33/8+(13*p-2*p*q)/8+(alpha1+alpha2)*(1-p)*(1-q)*(1-k)/8+5*r/2.

Both are multi-affine on a finite cube, so all minima are attained at deterministic vertices. For an individual FULL source, p=q=0 contributes alpha_i*(1-k)/8, p=0,q=1 contributes 1/8, and p=1 contributes at least 11/16; therefore its minimum is min(0,alpha_i)/8. Independently choose qB=1 and r=0, proving the FULL identity. Under LR, p=0,q=0 gives (alpha1+alpha2)*(1-k)/8, p=0,q=1 gives 0, and p=1 contributes at least 11/8; choose r=0, proving the LR identity. The inequality min(0,x+y)>=min(0,x)+min(0,y) proves the gap bound, with strict excess min(|x|,|y|) for opposite signs. Convexification does not change extrema. Holder with ||H||_1=5+5+8=18 proves the distance bound. K=stop (k=1) restores the predecessor's exact four-dimensional full-rank LR chart, independent of the terminal law. QED.

## Exact strictly positive and source-asymmetric example

Set epsilon=1/2. On source i, conditional K continuation ends Q at t=4 with P/Q probabilities (a_i,b_i) or ends P at t=3+h_i with complementary probabilities. Choose (a1,b1,h1)=(3/4,1/4,2), (a2,b2,h2)=(1/4,3/4,6). All natural P/Q branch probabilities are strictly positive; K terminal likelihood ratios are (24/5 at t=4 Q, 8/15 at t=5 P) for source 1 and (8/15 at t=4 Q, 24/5 at t=9 P) for source 2. Thus even coincident LR values at *different times* have no conflicting terminal answer. The two K continuation advantages are alpha1=-5/8 and alpha2=9/8.

Exact extrema: min_FULL H=-285/64, min_LR H=-33/8; G=21/64, a strictly *larger* gap. FULL witness p1=p2=q1=q2=r=0, qB=1, k1=0,k2=1 yields W=(253/320,113/512,169/64,1383/512), H(W)=-285/64. Hence dist_infinity(W,conv LR)>=7/384. The k=1 LR rank determinant remains |det|=59/20480.

## Verification and boundary

Standalone standard-library Fraction verifier VERIFY.py enumerates *exact* positive two-law branch mass, checks normalization, all 256 FULL and 16 LR deterministic observations on 72 exact parameter cases, plus the 272 vertices of the displayed example: **19,856 exact observation computations**, 24 opposite-sign cases. It independently checks both symbolic H evaluation formulae, extremal formulae, rank, and witness. EXACT_OUTPUT.txt is the actual captured program stdout. Finite checks are regression evidence only; the all-real theorem is analytic.

The result excludes *fixed, terminal-only* source-sensitive repairs to this unchanged I/J/K architecture. It does NOT exclude a genuinely new shared behavioral decision after K, changing earlier I/J coupling, changing source masses, or other model families. The original R5 four-observer mother problem remains OPEN. No independent review, source Claim, native Result, X6 attribution or mathematical admission is asserted.

Next task: change the **behavioral coupling topology** or earlier source geometry. Reconstruct exact four-observer deterministic vertices, require LR rank 4 and exact all-signed FULL-vertex-to-LR-convex-hull rational certificates (<=5 LR vertices each), or one Farkas separating witness. Only with full convex hull equality seek actual real behavioral image nonmembership. Preserve P000/worldview and branch sources.
