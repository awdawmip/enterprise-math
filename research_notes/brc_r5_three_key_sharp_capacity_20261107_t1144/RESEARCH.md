# R5 — Sharp three-key capacity at symmetric stopping time 31/10

Date: 2026-11-07 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen science: Global a01383f825ef9d43b4b754254303298c64041568, Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e (unchanged). Immediate predecessor: enterprise-math commit 999791caf2335ce043aee472f1cbf8f985719f96, research_notes/brc_r5_two_tail_capacity_20261107_t1037/RESEARCH.md and VERIFY.py. Current behavioral source read snapshots: Global main a14ed0ce0c9caa671446bafee7c9f1167feada2b and EM main a629a70f1bb108b65cd305a6000cb43b6b3d897b, with current bootstrap/manual, math/output/code/BRC policies, P000, ACTIVE worldview, RESEARCH_CONTINUATION_PROTOCOL current-normative-context, PORTABLE_RESEARCH_PROTOCOL and research_method. This is the frozen four-stage P/Q-BRC observer model, not a claim of native X6 dynamics.

## Model

All variables are real. Legal FULL_HIST timing/flow variables are g,a,b,u,v,w,z, with

~~~
0 <= a,b <= g <= 1
C0 = 13a/40 + b/80,    0 <= u <= C0
C1 = a/10 + 9b/40,     0 <= v <= C1
C2 = 3a/40 + 21b/80,   0 <= w <= C2
0 <= z <= a/10,        0 <= v-z <= 9b/40.
~~~

Two stopping-time observables (under P and Q respectively):

~~~
TP = 1 + g + (3a+5b)/8 + u/2 + v + 3w/2
TQ = 1 + g + (a+b)/2 + u + v + w.
~~~

The seven stopped likelihood-ratio keys r=(1/10,1/2,3/4,1,5/4,3/2,19/10), indexed from 0 to 6, have stopped Q masses Mj. In particular

~~~
M0 = (509/900)u + (47/180)z + (67/162)(v-z) + w/100
M1 = C0-u
M6 = u/100 + (47/180)z + (67/162)(v-z) + (509/900)w.
~~~

Any declarations 0<=Ej<=Mj yield the four-observer vector W=(eP,eQ,TP,TQ), where eQ=sum_j Ej and 1-eP=sum_j rj*Ej. In the three-key-only declaration class, E2=E3=E4=E5=0, so eQ=E0+E1+E6.

## Theorem A — an all-real global supporting plane with a sharp prescribed-time bound

Every admissible FULL_HIST strategy satisfies

~~~
M0+M1+M6
 <= 6269/11400 + (1312/1425)(TP-31/10)
               - (6887/8550)(TQ-31/10).                (A)
~~~

In particular, for TP=TQ=31/10, the exact maximum of M0+M1+M6 over the entire FULL_HIST strategy family is

~~~
max_FULL_HIST (M0+M1+M6) = 6269/11400.                 (B)
~~~

This maximum is attained by a seedless LR policy, so it is also the exact maximum over seedless LR with the same two stopping-time constraints.

**Exact dual certificate.** Define the left side of (A) minus M0+M1+M6 to be L. Direct substitution gives the algebraic identity

~~~
L = (14473/34200)(g-a)
  + (116/285)(a/10 + 9b/40 - v)
  + (247/810)(9b/40 - v + z)
  + (113/1425)u
  + (3511/11400)(1-g).                                (C)
~~~

Identity (C) holds for every real 7-tuple (no feasibility assumptions). All five terms on its right are nonnegative on the full legal domain, proving (A) and the upper bound in (B). It is a rational supporting-hyperplane/Farkas certificate, not an empirical LP guess.

**Equality flow and sharp seedless construction.** At TP=TQ=31/10, equality in (B) makes every term in (C) vanish, since each coefficient is strictly positive. Therefore g=a=1, u=0, v=a/10+9b/40, z=v-9b/40=a/10. Solving the two time equations uniquely forces b=10/19 and w=9/76. Thus the equality flow is unique in the seven timing variables:

~~~
(g,a,b,u,v,w,z) = (1,1,10/19,0,83/380,9/76,1/10).   (D)
~~~

Its capacities are C0=63/190, C1=83/380, C2=81/380. The pooled likelihood-ratio continuation probabilities are u/C0=0, v/C1=1, w/C2=5/9; the common central continuation is 1 on both merging histories (z=a/10 and v-z=9b/40). The two early continuation probabilities are a/g=1 and b/g=10/19. Thus (D) is genuinely seedless LR. Its complete stopped Q-mass vector is

~~~
(M0,M1,M2,M3,M4,M5,M6)
 = (1739/22800,63/190,0,1351/11400,9/38,9/95,3239/22800).
~~~

All masses are nonnegative, sum to 1, and have likelihood-ratio first moment 1. Their selected sum M0+M1+M6 is exactly 6269/11400.

## Theorem B — an explicit all-real three-key common image

For all real x,y,s satisfying

~~~
0 <= x <= 1739/22800,
0 <= y <= 63/190,
0 <= s <= 3239/22800,
~~~

there exist **both** a FULL_HIST and a seedless LR strategy achieving

~~~
W=(1-x/10-y/2-19s/10, x+y+s, 31/10,31/10).         (E)
~~~

Indeed, use the single seedless timing flow (D), select E0=x, E1=y, E6=s, and let every other Ej=0. This is legal and proves (E) identically for all real values, including irrational points and boundaries. The image is the two-dimensional zonotope projected from a three-dimensional declaration box; it is a certified common *subset*, not an assertion that the complete FULL_HIST and seedless LR images coincide there.

The all-positive declaration corner has the exact observation vector

~~~
Wcorner=(167/300,6269/11400,31/10,31/10).           (F)
~~~

By (B), at these stopping times and with declarations supported on the three indicated likelihood-ratio keys, no FULL_HIST strategy has greater eQ than (F). The seedless LR strategy already reaches this sharp value. This three-key common region complements, but does not replace, the earlier two-tail common parallelogram.

## Verification and next question

Companion VERIFY.py uses only standard-library Fraction. It checks identity (C) on one constant and seven basis vectors (exhaustive for an affine identity), the exact legal seedless policy (D), all seven stopped masses and P/Q moment normalization, 125 additional rational declaration choices, and (F). EXACT_OUTPUT.txt is captured stdout of the executed verifier. The all-real proof rests on identity (C), legality and the explicit construction; the finite declaration checks are diagnostics.

The original R5 mother question, equality or separation of unrestricted FULL_HIST and seedless LR four-observer images with all seven likelihood-ratio declaration keys, remains open. The next unit targets a genuinely mixed signed error objective at rational stop times, checking the globally reoptimized seedless LR family rather than a fixed timing policy; see NEXT_UNIT.md.

Actual GitHub actor: awdawmip (repo push/admin verified). Native em_status/em_control_tasks/em_context_manifest returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false; active R5 owner, native researcher identity, formal CLAIM and independent admission remain unconfirmed. These files preserve author-side research evidence. No credentials, private tokens or sharing changes are included.
