# R5 — Sharp global two-tail capacity and common two-key observer parallelogram

Date: 2026-11-07, Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific inputs unchanged: Global a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e.
Immediate exact scientific predecessor: 62fcf041afeaee6ef84c04c77918e5c2cb43db4c, research_notes/brc_r5_global_high_key_support_plane_20261107_t0941/RESEARCH.md.
Current normative controls read 2026-11-07: Global canonical main d6810437e506ff02c4df175071901edfb5e87a59, EM canonical main e13b05d592897846a6f826f2327bde7c31021bc4; P000, ACTIVE Heartbeat World, joint relation observer preservation, portable research and current task research method. This is the frozen four-stage P/Q-BRC observer, with no asserted native X6 dynamics.

## Model and domain

Let g,a,b,u,v,w,z be real. The lawful FULL_HIST early and pooled continued Q masses obey:

  0<=a,b<=g<=1;
  0<=u<=13a/40+b/80; 0<=v<=a/10+9b/40; 0<=w<=3a/40+21b/80;
  0<=z<=a/10; 0<=v-z<=9b/40.

The four-observer stopping times are

  TQ = 1+g+(a+b)/2+u+v+w,
  TP = 1+g+(3a+5b)/8+u/2+v+3w/2.

Seven stopped LR keys: r=(1/10,1/2,3/4,1,5/4,3/2,19/10).
Retain the two extreme stopped Q masses

  M0=(509/900)u+(47/180)z+(67/162)(v-z)+w/100,
  M6=u/100+(47/180)z+(67/162)(v-z)+(509/900)w.

For legal declarations 0<=Ej<=Mj, eQ=sum(Ej), 1-eP=sum(rj*Ej).
FULL_HIST distinguishes central branch-A flow z from branch-B flow v-z; seedless LR shares continuation probabilities across histories with the same current LR. History/provenance is retained until a stated four-observer equivalence is proved.

## Theorem 1 — new global low-LR supporting plane

Every legal real FULL_HIST strategy obeys

  M0 <= (10563/36000)(TQ-1) - (6802/36000)(TP-1).          (1)

This plane is sharp on a nontrivial seedless LR continuous equality family.

Define the following six nonnegative legality slacks:

  S0=g-a,                 S1=g-b,
  S2=13a/40+b/80-u,      S3=a/10+9b/40-v,
  S4=3a/40+21b/80-w,     S5=9b/40-v+z.

Let B=3761/36000. The following exact affine identity holds for all real g,a,b,u,v,w,z, even without their legality constraints:

  B(TQ-1) - (3401/18000)(TP-TQ) - M0
    = (283/4800)S0+(3277/72000)S1+(6599/18000)S2
      +(5639/36000)S3+(247/1620)S5.                       (2)

All displayed multipliers are positive. Formula (2) rearranges to (1), and equality occurs iff S0=S1=S2=S3=S5=0. Solving gives g=a=b=s; u=27s/80; v=13s/40; z=s/10; w=q, where 0<=q<=27s/80 and 0<=s<=1. These flows are realized by seedless LR: at each shared low and central LR node continue with probability one, and at the high side node continue with common probability q/(27s/80) when s>0 (zero when s=0). Observations are

  TQ=1+213s/80+q,
  TP=1+399s/160+3q/2,
  M0=7441s/24000+q/100.

## Theorem 2 — sharp global two-tail capacity

For EVERY legal real FULL_HIST strategy,

  M0+M6 <= (3761/18000)(TQ-1).                             (3)

At each real t in [1,4], the sharp maximum of M0+M6 subject to TQ=t is precisely (3761/18000)(t-1), attained by seedless LR. Equality at t>1 forces the observer-relevant continuation-flow variables to be

  g=a=b=s=(t-1)/3;
  u=w=27s/80; v=13s/40; z=s/10.

An exact global certificate is the sum of (2) and the pinned predecessor's high-key certificate:

  (3761/18000)(TQ-1)-M0-M6
    = (147/2000)S0+(1219/9000)S1
      +(6599/18000)S2+(5639/18000)S3
      +(6599/18000)S4+(247/810)S5.                        (4)

Every coefficient is positive, so (4) proves the bound and the unique equality flow. This flow has TP=TQ=1+3s and M0=M6=(3761/12000)s, therefore saturates (3). Also 1<=TQ<=4 from the stage capacities. These equalities and inequalities are exact over ALL real admissible parameters.

## Corollary — complete common two-tail-only declaration slice

Fix real t in [1,4] and restrict declarations to the two LR keys 1/10 and 19/10: E1=E2=E3=E4=E5=0. On the slice TP=TQ=t, the FULL_HIST and seedless LR four-observer reachable sets are identical, exactly

  { (1-x/10-19y/10, x+y, t, t):
      0<=x<=B(t-1), 0<=y<=B(t-1) }, B=3761/36000.          (5)

Necessity: the global low-key plane (1) reduces to M0<=B(t-1) at TP=TQ; the predecessor's global high-key plane M6<=(3401/18000)(TP-1)-(3041/36000)(TQ-1) reduces to M6<=B(t-1). Thus x=E0<=M0 and y=E6<=M6 each satisfy the rectangle bounds. Sufficiency: choose the Theorem 2 equality flow, which is seedless LR and simultaneously has M0=M6=B(t-1); then independently choose any real E0=x, E6=y and zero elsewhere. This covers the entire continuous parallelogram, including irrational targets and all boundary points.

For t=31/10, both simultaneous extreme capacities equal 26327/120000. Formula (5) extends the predecessor's high-key one-dimensional ray to a two-dimensional four-observer region. The two-key declaration support is part of this corollary's hypothesis. The general seven-key R5 mother comparison remains open.

## Exact checks, provenance and continuation

Companion VERIFY.py was executed in Python standard-library Fraction arithmetic; EXACT_OUTPUT.txt is execution stdout. It verifies both identities on all seven affine basis vectors, the full stopped LR mass normalization and Q/P moments, five rational sharp equality policies with 80 two-tail label choices, 72 rational FULL_HIST interior policies, and the t=31/10 exact capacities. Universal claims rest on the written affine identities, positivity and explicit constructions, not the finite diagnostic samples.

The high/low extremal terminal capacities are simultaneously saturable with one seedless LR timing policy, so a separation witness must exploit other LR stop keys or a nontrivial time geometry. The next unit is specified in NEXT_UNIT.md.

Actual GitHub actor: awdawmip with push/admin. Native em_status and em_control_tasks returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / operation_sent=false. Current R5 active Owner and formal CLAIM are unconfirmed. This is author-side mathematical evidence pending independent review and admission.
