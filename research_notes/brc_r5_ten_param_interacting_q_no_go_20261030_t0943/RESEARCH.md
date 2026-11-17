# R5 — Ten-parameter interacting-branch Q compensation no-go theorem

2026-10-30 Asia/Shanghai. Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is an auxiliary finite two-law stopping model, not an accepted native X6/Heartbeat/physical theorem. The original mother problem remains OPEN. No current service-issued session/CLAIM/Result or independent Driver review is asserted.

## Frozen inputs and problem

GLOBAL_KNOWLEDGE_V1 canonical main **7c41f7da7eb63e8e676365266012d3ecd2059c3d** (00_BOOTSTRAP.md, OPERATING_MANUAL.md, TASK_RESEARCH project router, P000 startup projection, ACTIVE worldview, math/BRC/code policies); canonical P000 blob **770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc** checked. Enterprise Math main **44d1fc5ab0c27940f859ea6918fee86192022ac6** (AGENTS, P000, ACTIVE X6/time, joint-observer preservation, portable research and autonomous operations). Scientific predecessor immutable commit **4314ac1f0ed0b23095887cfc012859d658af35c1**, folder research_notes/brc_r5_private_subtree_q_monotonicity_20261030_t0842, Draft PR #1663; earlier R5 work is disclosed as prior contribution, not an independent review.

Mother target: compare FULL history policies and **seedless LR** policies whose current action depends only on (time,current P/Q likelihood ratio), without a persistent correlated external random seed. For O=(e_P,e_Q,T_P,T_Q), search for **equal convex hulls but unequal actual real behavioral images**. A strict support gap excludes a candidate. This paper excludes an enlarged ten-dimensional family, not the mother target.

## Positive rational two-law model

Optional nodes, masses (360P,360Q) and natural time:

t1 A:(120,240), B:(240,120).
t2 A0:(60,180), A1:(60,60); B0:(180,60), B1:(60,60).
t3 A00:(30,108), A01:(30,72), A10:(30,45), A11:(30,15); B00:(90,36), B01:(90,24), B10:(20,40), B11:(40,20).

All natural masses are strictly positive, normalized and conserved at both measures; t4 is compulsory. LR collision #1: A1/B1 at (t2,L=1). Collision #2: A11/B11 at (t3,L=2). FULL has 14 independent stop/continue decisions; seedless LR has 12 distinct decision keys. A10 and B10 have individually distinct LR keys but are downstream of the shared A1/B1 time-2 stop key.

For an arbitrary legal P terminal error kernel p(t,h) in (0,1), let the Q error be

q(t,h) = 2/5-t/30+(t+2)L(h)/200 + eta*c_h, eta>0.

Fix c_A11=+1,c_B11=-1. The **ten arbitrary real** coefficients are (c_A1,c_B1,c_A0,c_A00,c_A01,c_B0,c_B00,c_B01,c_A10,c_B10); other corrections including compulsory t4 vanish. Every stop-time Q error must lie strictly in (0,1), so c_B11=-1 enforces eta<7/20. P rates may vary arbitrarily, provided legal. The BRC carrier is positive source-labelled P/Q branch mass; no total-only quotient, hidden phase cancellation or unproved X6 transfer is used.

## Theorem — all real parameters and policies

For s=±1, set lambda=1/75,
S=e_Q-41/100-T_P/200+T_Q/30, D=8-T_P-T_Q,
Psi_s=s*S-lambda*eta*D.
Let F_s=max_FULL Psi_s/eta and L_s=max_LR Psi_s/eta over **all real** local stop probabilities [0,1].

For **every** admissible ten-real-parameter Q correction and arbitrary legal P error kernel,

**max(F_+-L_+, F_--L_-) >= 1/25 > 0.**

Hence the FULL and LR convex hulls of the original four-observer are strictly unequal. Some actual FULL observation is at L-infinity distance at least **24eta/623** from the LR convex hull. The uniform constant 1/25 is sharp **among these two fixed signed directions across this ten-parameter family**, attained when all ten free coefficients vanish; no global optimum over arbitrary support normals is claimed.

### Exact Bellman reduction

Since Q(h)*L(h)=P(h) for every stopped trajectory,
e_Q=41/100+T_P/200-T_Q/30+eta*sum_{early stopped h}Q(h)c_h.
Also D=sum_{early stopped h}(4-t(h))*(P(h)+Q(h)).
Thus Psi_s/eta equals the sum of signed stopped-path rewards
r_s(h)=s*Q(h)c_h-lambda*(4-t(h))*(P(h)+Q(h)).

Each time-key appears at most once per natural path, so the reward objective is multi-affine in all real behavioral probabilities despite LR collisions. Its extrema occur at deterministic masks; this is a universal real-policy reduction, not a finite-grid inference.

Define C_A=max(0,r(A0),max(0,r(A00))+max(0,r(A01))) and similarly C_B for the B0 side subtree. Let a2=r(A1),b2=r(B1),a3=r(A11),b3=r(B11),alpha=max(0,r(A10)),beta=max(0,r(B10)). They depend on sign; C_A,C_B,alpha,beta are nonnegative.

Then exactly:

F_s=C_A+C_B+max(0,a2,alpha+max(0,a3))+max(0,b2,beta+max(0,b3)).

L_s=max_{x,y∈{0,1}}{-(2-x-y)/25+x*C_A+y*C_B
    +max(0,x*a2+y*b2,x*alpha+y*beta+max(0,x*a3+y*b3))}.

x,y are root continuation choices. The common A1/B1 decision and A11/B11 decision stay SHARED. A10/B10 are independent only after the t2 common continuation decision. This retains their genuine interaction and prevents an invalid private-subtree shortcut.

Adding C_A,C_B increases FULL support exactly by C_A+C_B and LR support by at most that amount (x,y<=1). So it suffices to prove a lower gap bound at C_A=C_B=0, **without** discarding alpha/beta.

### New all-real, two-sign domination lemma

Set c=1/25,k=4/225,d=4/75,h=1/100, a=c_A1/6-2/225, b=c_B1/6-2/225.
Collision rewards are:
r_+(A11)=c, r_+(B11)=-13/225;
r_-(A11)=-13/300, r_-(B11)=d.
Their signed sums are -k and h. Write alpha,beta>=0 for the positive-sign A10/B10 optimum and A,B>=0 for the negative-sign optimum. The argument even permits these four nonnegative values to vary INDEPENDENTLY, so it automatically covers arbitrary real Q corrections at those nodes.

F_+=max(a,alpha+c)+max(0,b,beta);
L_+=max(0,a+b,alpha+beta,a-c,b-c).

F_-=max(-a-k,A)+max(-b-k,B+d);
L_-=max(-a-b-2k,A+B+h,-a-k-c,-b-k-c,B+d-c).

Proof by three exhaustive real-plane cases:

(1) a<=0. F_+-c >= alpha+max(0,b,beta). This dominates every L_+ term: a+b<=b, a-c<=0, b-c<=b, alpha+beta<=alpha+max(0,b,beta). Thus F_+-L_+>=c.

(2) a>0,b<=-c. L_+=max(alpha+beta,a-c). F_+=max(a,alpha+c)+beta dominates both alternatives plus c, so F_+-L_+>=c.

(3) a>0,b>-c. Since -a-k<0 and -b-k<c-k<d, F_-=A+B+d. Every L_- argument is <=A+B+(d-c)=A+B+1/75: namely -a-b-2k<c-2k=1/225, h=1/100<1/75, -a-k-c<0, -b-k-c<-k<0, and B+d-c<=A+B+d-c. Hence F_--L_->=c.

These three alternatives cover ALL real a,b and ANY nonnegative alpha,beta,A,B, and the private C comparison is exact. This proves the theorem for ALL ten real coefficients and all real behavioral policies. Arbitrary P-only terminal changes cannot alter this Q/time objective. QED.

The support normal of Psi_s on O is (0,s,-s/200+eta/75,s/30+eta/75). Since eta<7/20<3/8 its L1 norm for either sign is exactly 623/600. Norm duality yields (eta/25)/(623/600)=24eta/623. When all ten free coefficients vanish, C_A=C_B=alpha=beta=0 and both gaps equal 1/25, establishing fixed-direction sharpness.

## Strictly legal rational witness

Let eta=1/1000, (c_A1,c_B1)=(1/2,1/10), (c_A10,c_B10)=(1,-1), and (c_A0,c_A00,c_A01,c_B0,c_B00,c_B01)=(1,-1,1,-1,1,-1). For the explicit four-vector use p(t,L)=1/5+t/20+(t+1)/(100L). Every P/Q terminal error probability is strictly between zero and one.

The executed exact program gives F_+=841/1125, L_+=3149/4500, support gap 43/900; negative direction gap 13/300. FULL deterministic mask 14308 (node order in VERIFY.py) yields O*=(2279/6000,10361/30000,35/12,12/5).

Every REAL LR strategy, including every convex mixture, satisfies the INTEGER separating inequality

**4500000 e_Q - 22440 T_P + 150060 T_Q <= 1848629.**

At O* the left side is **1848844**: exact integer violation **215**, L-infinity distance at least **43/934500**.

## Actual checks and limitations

The standard-library Fraction program VERIFY.py checks positivity, normalized mass, both collisions, 14/12 keys, four exact rational examples, the exact Bellman envelopes against all 16,384 FULL and 4,096 LR deterministic masks for BOTH signs in each example (**163,840** exact policy-score evaluations), the explicit FULL four-vector, and a 7^4=2,401 rational parameter-grid regression. Actual execution stdout is EXACT_OUTPUT.txt, ending PASS_EXACT_R5_TEN_PARAMETER_INTERACTING_Q_NO_GO. The finite checks validate the examples and formulas; the continuum theorem is the **three-case proof above**, not the parameter grid.

Status is AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. There is no independent review, formal checker proof, Source CLAIM/Result, or asserted native X6 correspondence. P000 and ACTIVE worldview remain unchanged.

## Smallest next question

This ten-parameter family (plus arbitrary legal P-only modifications) is excluded as a remedy. **Do not resample it.** Change the fixed A11/B11 collision residual coefficients, alter the positive P/Q transition kernel while preserving appropriate collisions, or add a genuinely different interacting LR merger topology. First test ALL signed four-dimensional convex-hull containment: for every FULL deterministic observer produce a nonnegative rational combination of at most five LR deterministic observers or an exact rational Farkas separator. Only after hull equality is established investigate actual real seedless LR image nonmembership by semialgebraic proof; an external persistent randomized mixture is not a legal substitute.