# R5 — central-history split convex order and exact fixed-flow extremal reduction

Date: 2026-11-07 Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Scientific inputs remain frozen: Global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Exact predecessor: 6313f3bed2ddb6cee5da912686837c73d111fce0, research_notes/brc_r5_full_hist_supporting_face_20261107_t0743/RESEARCH.md. Current norms: Global 00_BOOTSTRAP.md and OPERATING_MANUAL.md; P000/ACTIVE world view; Enterprise Math docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context, docs/PORTABLE_RESEARCH_PROTOCOL.md and research_priorities/research_method.json. This is a theorem about the frozen four-stage P/Q-BRC observer model, not a derivation of native X6 dynamics. History branches A/B are retained up to application of their differing terminal kernels.

## 1. Sharp one-variable reduction

Fix lawful early continued Q masses 0<=a,b<=g<=1 and stage-three pooled continued Q masses x0,x1,x2. The stage-three branch capacity vectors are

  VA=(13a/40, a/10, 3a/40),  VB=(b/80, 9b/40, 21b/80).

For the central LR=1 key put A=a/10, B=9b/40, s=x1, z=xA1, xB1=s-z. The exact feasible z interval is

  z_min=max(0,s-B) <= z <= z_max=min(A,s).

Side LR-key terminal rows are identical across branches; their capacities may be split in any legitimate way without changing the four selected observations. The times are

  TQ=1+g+(a+b)/2+x0+s+x2,
  TP=1+g+(3a+5b)/8+x0/2+s+3x2/2.

The stopped likelihood-ratio keys are r=(1/10,1/2,3/4,1,5/4,3/2,19/10); Q stop mass at key j is Mj(z). Declarations have 0<=Ej<=Mj and the error pair is (eQ,1-eP)=(sum Ej,sum rj Ej).

Central terminal rows differ:

  A1=(47/180,43/90,47/180),
  B1=(67/162,14/81,67/162),
  A1-B1=(-247/1620,247/810,-247/1620).

For every feasible z1<z2 let eta=(247/1620)*(z2-z1)>0. Exact mass identity:

  M(z1)-M(z2)=eta*(1,0,0,-2,0,0,1).                       (1)

The two outer keys have mean LR 1, since (1/10+19/10)/2=1. Thus z1 has more mass at the extreme likelihood ratios and less at the central key.

## 2. Theorem — strict nesting, full-history exact extremizer

Define the fixed-flow two-error image

  Z(z)={(sum Ej, sum rj Ej): 0<=Ej<=Mj(z)}.

For ALL real legal flows and z1<z2 in the permitted interval,

  Z(z2) is a STRICT subset of Z(z1).                       (2)

Consequently the entire FULL_HIST four-observer image at fixed (g,a,b,x0,x1,x2) is exactly the image with the single B-first central allocation

  xA1=z_min=max(0,x1-9b/40),  xB1=x1-z_min.                 (3)

Proof of inclusion. Write Mlo=M(z2), Mhi=M(z1). By (1), Mhi0=Mlo0+eta, Mhi6=Mlo6+eta, Mhi3=Mlo3-2eta; all other masses are unchanged. For any legal declaration Elo let p=Elo3/Mlo3 in [0,1]. When Mlo3=0 necessarily eta=0 and equality is trivial. Define

  Ehi0=Elo0+eta*p,
  Ehi3=Elo3-2eta*p=p*Mhi3,
  Ehi6=Elo6+eta*p,
  Ehi_j=Elo_j for j other than 0,3,6.                     (4)

Each new E stays between zero and its corresponding new M. The sum of declarations is unchanged. The LR-weighted sum changes by eta*p*(1/10-2+19/10)=0. TP,TQ depend on pooled flows, so they also remain unchanged. This constructs an exact observer-preserving seed of every point from Z(z2) in Z(z1).

Proof of strictness. At z1 declare only the entire maximal LR bin 6 as P. Then (eQ,1-eP)=(M6(z1),(19/10)*M6(z1)). Every other LR is strictly less than 19/10, hence any policy reproducing equality 1-eP=(19/10)*eQ must have Ej=0 for j<6 and E6=eQ. But M6(z2)=M6(z1)-eta<eQ. Thus the point lies outside Z(z2). This proves strict inclusion without numerical optimization.

The pooled seedless LR policy at the SAME fixed early and pooled flows must use the common central continuation probability c=s/(A+B), when A+B>0, so z_LR=A*s/(A+B), a feasible z. Its two-error image is contained in the B-first FULL_HIST image, and the inclusion is strict whenever A,B>0 and 0<s<A+B. If the central split is forced (A=0, B=0, s=0 or s=A+B), the images coincide at those fixed totals. This is an exact reduction of one FULL_HIST continuous history variable for this four-observer search, not a quotient of the full provenance-sensitive process.

## 3. Exact rational local obstruction and its global LR rescue

Take g=a=b=1, x0=x2=0, x1=1/10. The B-first FULL_HIST split is xA1=0,xB1=1/10. Seedless LR at the same totals uses xA1=2/65,xB1=9/130. Their high-key capacities are

  M6(FULL)=67/1620,  M6(LR at fixed flows)=11/300,
  difference=19/4050>0.

The FULL_HIST strategy declaring P only at high key 19/10 attains

  W_test=(eP,eQ,TP,TQ)=(14927/16200,67/1620,31/10,31/10), (5)

and the predecessor supporting functional is L(W_test)=127835/6>0. The high-key cap proves no SAME-FLOW seedless LR strategy can attain this W.

However, changing early and pooled flows produces an exact seedless LR realization of the SAME W_test. Choose

  g=1,a=1,b=1/2; (x0,x1,x2)=(1/20,1/8,7/40).
  xA=(13/265,1/17,7/110),
  xB=(1/1060,9/136,49/440),

where all side and central histories use common continuation probabilities at each shared LR key, as required by seedless LR. Every flow meets its branch capacity. The resulting M6=29009/204000>67/1620. Choose E6=67/1620 and all other Ej=0, yielding exactly W_test and TP=TQ=31/10. Hence (5) is NOT a global separation witness. This is a rigorous illustration that fixed-flow information loss can be compensated by alternative LR timing/continuation.

As an independent nonconstant-declaration example, start with E_j=M_j(z_min)*((j mod 3)+1)/5 in the g=a=b=1 case. Formula (4) produces a pooled LR policy preserving W=(451/800,161/400,31/10,31/10) with L(W)=799104/25>0.

## 4. Evidence and continuation

The standard-library Fraction program VERIFY.py was executed locally; EXACT_OUTPUT.txt contains actual output. It checks (1)'s coefficient, the key mean, all rational flow and declaration capacities, normalized Q/P stop masses, both four-observer matches and strict fixed-flow top-key obstruction. The all-real theorem is algebraic (1)–(4), not inferred from tested points.

The mother question O4(FULL_HIST)=?O4(seedless LR) remains OPEN away from the shared face. Next, use (3) to optimize FULL_HIST maximum high-key Q mass at fixed TP,TQ and compare to a GLOBAL seedless LR optimum over all early and pooled flows. This avoids treating a local fiber obstruction as global separation. See NEXT_UNIT.md.

Control: actual GitHub actor awdawmip with push permission; native em_status and em_control_tasks returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / operation_sent=false. Active R5 Owner/CLAIM unconfirmed; these artifacts are independent author-side evidence, not a native Result, Review or mathematical admission.
