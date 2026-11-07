# R5 — sharp global high-key mass supporting plane and common symmetric-time error ray

Date 2026-11-07 Asia/Shanghai. Status AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen science: Global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Exact predecessor: 988c0524dacefed4a741c895c27ebb01229f2905, research_notes/brc_r5_central_history_convex_order_20261107_t0842/RESEARCH.md and VERIFY.py. Normative control read from Global main a1db6a6a57f9c5eb7df1fcd3b8e36d9ef18f8636 and EM main 6001d51da1d3dc32897cd67e8fc7d32eabf0248b (P000, ACTIVE worldview, research continuation, portable research and current method). This is an internal result for the frozen 4-stage P/Q-BRC observer, not a claim about native X6 dynamics.

## Model and exact proposition

Use early continued Q masses 0<=a,b<=g<=1 and stage-three pooled continued Q masses x0,x1,x2, with central history-A continued mass z. Legal constraints:
  0<=x0<=13a/40+b/80;
  0<=x1<=a/10+9b/40;
  0<=x2<=3a/40+21b/80;
  0<=z<=a/10; 0<=x1-z<=9b/40.

The two expected stopping times and stopped Q mass at the unique maximal LR key 19/10 are:
  TQ=1+g+(a+b)/2+x0+x1+x2;
  TP=1+g+(3a+5b)/8+x0/2+x1+3x2/2;
  M6=x0/100+(47/180)z+(67/162)(x1-z)+(509/900)x2.

Central histories remain separate until their distinct terminal kernels act; side history kernels coincide for these four observers. Seven stopped LR keys are (1/10,1/2,3/4,1,5/4,3/2,19/10). For nonnegative P-declaration stopped Q mass Ej<=Mj, errors are eQ=sum Ej and 1-eP=sum(rj*Ej).

**Theorem A.** For every legal real FULL_HIST policy, with arbitrary early continued masses and central history split,
  M6 <= (3401/18000)(TP-1) - (3041/36000)(TQ-1).               (A)
The inequality is sharp. Every strategy saturating (A), after retaining the four-observer-relevant flow coordinates, is reproducible by a seedless LR strategy.

**Proof.** Set five nonnegative legal slacks
  S0=g-a;
  S1=g-b;
  S2=a/10+9b/40-x1;
  S3=3a/40+21b/80-x2;
  S4=9b/40-x1+z.
The exact affine identity, valid for all real values of the seven variables, is
  (3401/18000)(TP-1)-(3041/36000)(TQ-1)-M6
    = (349/24000)S0+(259/2880)S1+(5639/36000)S2
      +(6599/18000)S3+(247/1620)S4.                           (B)
All five rational multipliers are positive, proving (A). Seven exact affine coefficient checks in VERIFY.py verify (B), while the displayed identity and the nonnegative slacks establish the all-real result.

All multipliers being strictly positive, equality in (A) holds precisely when each Si=0. Solving these five equations under legal bounds gives
  g=a=b=s; x1=13s/40; x2=27s/80; z=s/10;
  x0=q; 0<=q<=27s/80; 0<=s<=1.                                 (C)
Realize the same variables with seedless LR: continue both central histories and both high-side histories with probability 1 and both low-side histories with the common probability c0=q/(27s/80), using c0=0 at s=0. The equality face in (TP,TQ,M6) is therefore exactly parametrized by
  TQ=1+213s/80+q;
  TP=1+453s/160+q/2;
  M6=7441s/24000+q/100.                                       (D)
The observer's four-dimensional future information is the stated four coordinates; this reduction preserves them, without identifying the two original history branches at the process level.

**Theorem B (exact global symmetric-time maximal-key ray).** For every real t in [1,4], the intersection of both global FULL_HIST and global seedless LR four-observer reachable sets with TP=TQ=t and 1-eP=(19/10)eQ is exactly
  { (1-19e/10, e, t, t) : 0<=e<=(3761/36000)(t-1) }.           (E)
For t outside [1,4], no such symmetric-time vector is reachable.

**Proof.** On TP=TQ=t, (A) yields M6<=(3761/36000)(t-1). At the top LR error ray,
  (19/10)eQ-(1-eP)=sum_{j<6}(19/10-rj)Ej=0.
Every summand is nonnegative and has a strictly positive coefficient, hence Ej=0 for j<6 and eQ=E6<=M6. For sharpness set s=(t-1)/3 and q=27s/80 in (C); then stage three always continues at every LR key, TP=TQ=1+3s=t, and M6=3761s/12000. Select E6=e for any real 0<=e<=M6 and Ej=0 otherwise. This is a lawful seedless LR strategy including irrational e and boundary values. Finally 1<=TQ<=4 follows from g<=1, (a+b)/2<=1, and x0+x1+x2<=(a+b)/2<=1. All claims follow.

For t=31/10 the exact sharp eQ-capacity is 26327/120000, attainable by both families. The diagonal maximizing pooled continuation is rigid: at t>1 equality in (A) forces all five Si=0, and TP=TQ forces q=27s/80, with s=(t-1)/3. This says nothing about uniqueness of latent random choices not observed in W.

## Evidence, scope, continuation

The published companion VERIFY.py was executed using Python standard-library Fraction; EXACT_OUTPUT.txt is actual stdout. It checks seven affine basis coefficients, twelve rational points on the LR equality face with normalized Q/P stopped masses and likelihood-ratio moments, and exact endpoints at t=1,9/5,31/10,4. The entire continuum theorem rests on identity (B), inequality signs and construction (C), not finite sampling.

This sharp global bound rules out a separation witness on the symmetric-time highest-LR error ray and exhibits a whole common exposed high-key capacity face. The mother question O4(FULL_HIST)=?O4(seedless LR) remains open off this face. Investigate multi-key declarations with signed objectives or nonsymmetric-time capacity facets next; see NEXT_UNIT.md.

GitHub execution identity awdawmip. Native em_status and em_control_tasks returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false, so native Owner/CLAIM not confirmed. This is author-side evidence pending independent review and admission.
