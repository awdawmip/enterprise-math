# Enterprise Math R5 — sharp two-signed Q compensation no-go

Date: 2026-10-30, Asia/Shanghai. Author-side TASK_RESEARCH scientific note, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

## Frozen sources, status and exact scope

GLOBAL_KNOWLEDGE_V1 canonical main@c3e350dcec252c7af28883dc37ee4c20eced7a24 (relevant entry blobs unchanged from 6ad68966c0297376e30f97174805621beb19d191); Enterprise Math canonical main@ba2e1a3e371199ad7aca042b2dc530c1918382b7. Exact predecessor: b778e7c79dea890e5312679e8b892ad56cef26e3:research_notes/brc_r5_q_time_permanent_obstruction_20261030_t0640/RESEARCH.md and VERIFY.js. The pinned global P000 / ACTIVE worldview and project portable research protocol were read. Native control owner listing failed CONTROL_QUOTA; native session_start was denied STATIC_READONLY_SCOPE_DENIED with operation_sent=false. GitHub author-side preservation is not a canonical Source CLAIM, Result or independent review.

Mother target: find a strictly positive finite two-law stopping example whose FULL and seedless (time, likelihood-ratio) LR behavioral strategy observer sets have equal four-dimensional convex hulls but unequal actual real images, where O=(eP,eQ,TP,TQ). THIS RESULT EXCLUDES A FAMILY; IT DOES NOT RESOLVE THE MOTHER TARGET. All masses retain BRC-style source labels and collision identities, but this is an auxiliary two-law stochastic model, not a claimed native X6/BRC physical computation.

## Fully specified natural tree (p360=360 P(h), q360=360 Q(h))

node,t,p360,q360,LR_key,children
A,1,120,240,0,A0 A1
B,1,240,120,1,B0 B1
A0,2,60,180,2,A00 A01
A1,2,60,60,3,A10 A11
B0,2,180,60,4,B00 B01
B1,2,60,60,3,B10 B11
A00,3,30,108,5,-
A01,3,30,72,6,-
A10,3,30,45,7,-
A11,3,30,15,8,-
B00,3,90,36,9,-
B01,3,90,24,10,-
B10,3,20,40,11,-
B11,3,40,20,8,-

All child masses sum to their parents, natural probabilities are strictly positive, t=3 can stop or wait without further random branching for compulsory t=4 stop. A1/B1 share exact t2 L=1; A11/B11 share exact t3 L=2. FULL observes history; LR shares its stop probability across each exact (t,L) collision, with no persistent random seed. Define an arbitrary terminal P Bernoulli error rate p(t,h) strictly in (0,1). Under Q, baseline q0(t,h)=2/5-t/30+(t+2)*L(h)/200, L=P(h)/Q(h). Add precisely:
q(2,A1)=q0+u*eta; q(2,B1)=q0+v*eta; q(3,A11)=q0+eta; q(3,B11)=q0-eta.
Here u,v are any REAL numbers and eta>0, restricted only by all terminal q in (0,1); q=q0 elsewhere. P rates may be independently changed arbitrarily without changing natural masses.

## Exact all-real support envelope theorem (both signs and both parameters)

Let S=eQ-41/100-TP/200+TQ/30 and D=8-TP-TQ. For any real policy, baseline change of measure gives
S/eta = u*Q(A1)*reach_stop(A1,t2) + v*Q(B1)*reach_stop(B1,t2)
      + Q(A11)*reach_stop(A11,t3) - Q(B11)*reach_stop(B11,t3).
Here reach_stop is the conditional stop fraction on the labelled natural cylinder. For s in {+1,-1}, lambda>=0, Psi_s=s*S-lambda*eta*D, let
a2=s*u/6-2*lambda/3, b2=s*v/6-2*lambda/3,
a3=s/24-lambda/8, b3=-s/18-lambda/6.
Then EXACTLY for ALL real behavioral strategies
F_s:=max_FULL(Psi_s/eta)=max(0,a2,a3)+max(0,b2,b3).
L_s:=max_LR(Psi_s/eta)=max over alpha,beta in {0,1} of
-3*lambda*(2-alpha-beta)+max(0,alpha*a2+beta*b2,alpha*a3+beta*b3).

Proof: Every path encounters each time-key only once, so the observer map and each linear functional are multi-affine in the independent behavioral stopping probabilities, even at shared keys. Hence all extrema occur at deterministic corners. At lambda>=0, A0/B0 and unmodified t3 leaf early-stopping rewards are nonpositive and may be discarded. FULL optimizes the two labelled A1 and B1 branches independently, selecting their t2 reward, t3 signed reward or waiting to t4. LR either pays 3 lambda to stop a root at t1 or continues it (alpha,beta). If it continues, the t2 A1/B1 key must be stopped jointly or continued jointly; the t3 A11/B11 key likewise must be stopped jointly or both continued for any surviving roots. These exhaustive options give the displayed envelopes. They depend on eQ and two stopping times, not on any terminal P error.

## Sharp uniform two-direction obstruction

Fix lambda=1/75 and abbreviate c=1/25, k=4/225, a=u/6-2/225, b=v/6-2/225, d=4/75. The above formulas reduce to
Fplus=max(c,a)+max(0,b);
Lplus=max(0,a+b,a-c,b-c);
Fminus=max(0,-a-k)+max(d,-b-k);
Lminus=max(1/75,-a-b-2*k,-a-k-c,-b-k-c).

UNIFORM THEOREM: For EVERY admissible real u,v and every admissible terminal P error, max(Fplus-Lplus, Fminus-Lminus) >= 1/25. The constant is sharp across this two-fixed-direction family, since u=v=0 gives BOTH gaps equal to 1/25.

Complete real-plane proof:
Case 1: a<=0. Fplus=c+max(0,b) and Lplus<=max(0,b), so plus-gap>=c.
Case 2: a>0,b<=-c. Lplus=max(0,a-c) and Fplus=max(c,a); plus-gap=c.
Case 3: a>0,b>-c. Fminus=d because -a-k<0 and -b-k<c-k<d. Lminus=1/75 since -a-b-2k<c-2k=1/225<1/75, and -a-k-c<0, -b-k-c<-k<0. Thus minus-gap=d-1/75=c. All real (a,b) fall into one case; no finite parameter sampling is used for the universal conclusion.

The normals of these two functionals on (eP,eQ,TP,TQ) are (0,+/-1,-/+1/200+eta/75,+/-1/30+eta/75). Since q(3,B11)=7/20-eta>0 implies eta<7/20<3/8, BOTH normals have L1 norm 623/600. Therefore for each admissible pair there EXISTS a legitimate FULL observation with Linf distance from the entire LR convex hull at least 24*eta/623. The witnessing FULL policy may vary with u,v. Convex-hull equality is impossible for the entire Q-at-A1/B1 two-parameter compensation family even if arbitrary P error compensations are allowed.

## Explicit strictly positive rational example and separating integer hyperplane

Choose eta=1/1000, u=1/2, v=1/10; use admissible p0(t,h)=1/5+t/20+(t+1)/(100L(h)). The plus-direction support gap is ZERO because a=67/900>=c and b=7/900>=0 (equivalently u>=22/75,v>=4/75). However minus-direction support gap is 1/25000.

FULL stops only at B11 at t3 and otherwise stops at t4. Its exact four-observer vector is
O*=(799/1800,16087/54000,35/9,71/18).
All real seedless LR strategies and their convex hull satisfy
150000 eQ - 752 TP + 4998 TQ >= 61482.
At O* the left side is 61476, a strict INTEGER GAP OF SIX. The L1 norm of the separator is 155750, proving Linf distance >= 6/155750 = 3/77875. Nontrivial time-2 compensation exists in the underlying Q model, even though this witness avoids stopping at t2.

## Reproduction, limitations, successor

VERIFY.py implements only the standard-library Fraction arithmetic of the typed finite two-law model, checks strict normalized natural kernels, both LR collisions and terminal probabilities, and enumerates 16,384 FULL + 4,096 LR deterministic policies for each of two signs at six rational u/v pairs (245,760 scored policy cases). All support maxima agree EXACTLY with analytic formulas. An additional 441-pair rational formula grid checks the uniform inequality but is not used to infer its universal status. The verified exact observer and separator match the theorem. Actual stdout is EXACT_OUTPUT.txt ending PASS_EXACT_R5_TWO_SIGN_Q_COMPENSATION_UNIFORM_NO_GO. The ALL-REAL result follows from the proof, not these finite checks. No Lean checker, external novelty priority, native X6 bridge, Source result, or independent Driver acceptance is claimed.

NEXT: The present two-parameter Q adjustment space is exhausted; add a genuinely NEW Q terminal-error compensation on A0/B0 t2 or a distinct noncolliding t3 leaf, or change the rational natural source-sensitive transition kernel while retaining both exact LR collisions. First derive BOTH signed support envelopes; any nonzero gap kills a candidate. ONLY if all-signed four-dimensional hull equality can be certified by exact rational positive combinations of at most five LR deterministic vectors for every FULL vertex, investigate unequal actual real behavioral images with semialgebraic methods. Preserve P000, original sources, BRC-labelled masses, actual owner/claim boundary, and independent-review requirements.