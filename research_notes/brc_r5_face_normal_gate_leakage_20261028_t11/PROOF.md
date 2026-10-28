# R5 — Exact exposed-normal gate and terminal-action leakage (2026-10-28)

**State:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. **Author scope:** local research contribution, not a Source-issued CLAIM or an independent Driver review. **Object:** external finite, passive P/Q sequential observation tree and the four-coordinate observer O=(e_P,e_Q,T_P,T_Q). No native Heartbeat-World X6 dynamics, cell embedding, or calibrated physical heartbeat time is asserted.

**Frozen input:** GLOBAL_KNOWLEDGE_V1 main@020bd2ca67f227956f8d2193519050eaad67e110; Enterprise Math main@273b7e88039e201423957924000c52b9ee683d3e. Immediate predecessor: research_notes/brc_r5_exposed_face_rank_terminal_repair_20261028_t11/RESEARCH.md at 2ea525e27882e26a64cf6d3573b5e230da87f708. Earlier work established the conditional rank-three bilinear patch criterion and an apparent six-leaf false positive, but did not establish that the four patch corners lie in an actual *maximizing* exposed face. This note closes that missing gate for the six-leaf input and proves a general filter.

## Theorem A — signed-time normal obstruction

Consider a passive two-law tree with two histories h+ and h- distinguishable by (time, likelihood ratio) at t=1, having positive masses p_i=P(h_i), q_i=Q(h_i), with

p+ - q+ > 0 > p- - q-.

Both histories allow a choice to stop at t=1 or to continue one observation step and stop at t=2; every other t=1 history can stop immediately. Let a feasible no-persistent-seed LR strategy patch be

B(x,y)=B00+x*u+y*v+x*y*w,  x,y in [0,1].

Suppose rank[u,v,w]=3 and each of its four corners satisfies T_P=T_Q. Then **no nonzero real linear functional** can have all four corners in a common maximizing exposed face of the complete-history policy image. In fact for every nonzero c the full-policy support value along lambda=c*(0,0,1,-1) exceeds the patch value by at least

|c|*min(p+ - q+, q- - p-) > 0.

**Proof.** Put ell=(0,0,1,-1). All patch corners have ell·B=0; bilinearity yields ell·u=ell·v=ell·w=0. Because rank is three, u,v,w span the three-dimensional kernel of ell in R4. Any lambda that has all four corners on one level must be orthogonal to all three directions and is therefore c*ell. A pure LR policy that stops at all t=1 histories except h+ and continues only h+ to t=2 has T_P-T_Q=p+-q+>0. Likewise continuing only h- gives a negative contrast p--q-<0. Either sign of nonzero c has a feasible pure LR policy strictly better than all B corners. Hence none of the proposed normal directions exposes them. QED.

The two explicit witness policies obviate full extreme-point enumeration for this *rejection*. Coplanarity is not global Bellman optimality. This theorem is scoped to first-stage histories with independent legal stop/continue actions; it is not a theorem about all multi-collision topologies.

## Lemma B1 — terminal-label tie sieve

At a reachable terminal history h with conditional likelihood ratio r=P(h)/Q(h) and unconditional Q mass q>0, switching the terminal declaration from P to Q changes observations by

t_h=(q*r,-q,0,0).

For lambda=(lambda1,lambda2,lambda3,lambda4), the score change is

lambda·t_h=q*(lambda1*r-lambda2).

Thus a reached terminal declaration is lambda-tied precisely when lambda1*r=lambda2; otherwise its preferred label is fixed by the sign when maximizing lambda·O. For lambda1=lambda2=0 every reached terminal label is tied. A purported two-variable maximizing face must explicitly account for such degrees of freedom or prove their exact observer redundancy.

## Theorem B — neutral constant-mass terminal action leaks out of a bilinear patch

Let B(x,y)=B00+x*u+y*v+xy*w have rank[u,v,w]=3, and suppose all corners lie on the same hyperplane H={v:lambda·v=M}, lambda≠0. Suppose an *independent* feasible LR action of constant nonzero observation increment t, lambda·t=0, produces every

F(x,y,z)=B(x,y)+z*t,  (x,y,z) in [0,1]^3.

Then F([0,1]^3) contains a nonempty relatively open three-dimensional region of H, whereas B([0,1]^2) has empty relative three-dimensional interior. Consequently B cannot describe every feasible LR observation lying on H.

**Proof.** The rank-three directions u,v,w span the tangent space of H. Write t=alpha*u+beta*v+gamma*w, with not all coefficients zero. In this basis the determinant of the three Jacobian columns (u+y*w, v+x*w, t) equals gamma-alpha*y-beta*x; this nonzero affine polynomial is nonzero at an interior (x,y), and remains nonzero for interior z. The inverse-function theorem gives a three-dimensional open set in H in F's image. B is polynomial and Lipschitz on a compact square; subdividing into n² squares and covering their images by balls of radius O(1/n) bounds total 3D volume by O(1/n). Hence B has zero 3D volume and cannot contain a relatively open set. QED.

Scope caution: t must be independent of x,y and realizable by a genuine additional action. A terminal state with reach probability depending on x or y does not automatically fit this lemma.

## Six-leaf exact test; two independent rejection certificates

The reused strictly positive rational observation tree has t=1 histories U:(Q,r)=(1/2,1/2), V:(1/2,3/2). Thus (pU,pV)=(1/4,3/4). At t=2 their structural descendants are U.C:(1/6,1), U.O:(1/3,1/4), V.C:(1/4,1), V.O:(1/4,2); both laws conserve mass within each parent. In the earlier frozen-terminal patch, x is the U.C continuation and y the shared LR=1 continuation at t=3. The exact four-dimensional coefficients are

B00=(1/12,2/3,9/4,9/4)
u=(0,0,1/6,1/6)
v=(1/32,-1/8,1/4,1/4)
w=(1/24,-1/12,1/6,1/6).

The (eP,eQ,TQ) determinant is exactly 1/2304. Yet Theorem A applies. Two feasible LR pure policies are:

(A) stop U at t=1; continue V to t=2 and stop: (TP,TQ)=(7/4,3/2), TP-TQ=+1/4.
(B) stop V at t=1; continue U to t=2 and stop: (TP,TQ)=(5/4,3/2), TP-TQ=-1/4.

Each B corner has TP-TQ=0, so neither sign of the *only* possible exposing normal can maximize there; the certified support gap is at least |c|/4. This is a strict *global-exposure* failure in addition to the predecessor's terminal-label repair.

For an independent extra terminal action, the always-reached U.O history at t=2 has masses (P,Q)=(1/12,1/3) and originally declares Q. Switch fraction z toward declaring P, obtaining

t=(-1/12,1/3,0,0),  F(x,y,z)=B(x,y)+z*t.

The exact LR-feasible point L=F(0,0,1/2)=(1/24,5/6,9/4,9/4) lies strictly outside the frozen B patch, because eQ(B)=2/3-y/8-xy/12<=2/3 on the whole square. Thus

inf_{0<=x,y<=1} ||L-B(x,y)||_infinity >= 1/6.

At x=y=1/2, the determinant of the (eP,eQ,TQ) Jacobian of F is -1/3456, an independent exact full-rank leakage witness. **L is itself an LR-feasible point**, not a mother-problem nonrealizability witness; the 1/6 gap is *only relative to the artificially frozen patch*.

## Method and exact verification

BRC use: REUSE_APPLIED to the external finite strictly positive rational **labelled branch carrier**, retaining Q mass, P/Q ratio, terminal label, source provenance and observation time until the final four-coordinate readout. No hidden-source quotient, LN, floating-point step, native X6 propagation, or physical attribution is used. This external Fraction calculation does not execute native Heartbeat/BRC–Shor arithmetic.

The accompanying Python standard-library Fraction script verifies: both-law parent/leaf conservation; the bilinear coefficients on a finite exact regression grid; the determinant 1/2304; the two t=1 stopping witnesses; the terminal-label affine identity; the off-patch rational point and its 1/6 inequality; and the Jacobian -1/3456. Theorems A/B cover real strategy parameters by algebraic proof, not finite-grid interpolation. This result only **rejects an invalid candidate exposure**; it does not establish convex-hull equality or true-image inequality for any new multi-collision model.

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. Source Owner, formal CLAIM, Source Result and independent Driver review not inferred from a GitHub commit.

**Next:** construct a two-interacting-collision rational tree. First compute the rank-three normal; reject immediately if any admissible stop/continue strategy improves its score. At all reached terminal leaves test lambda1*r-lambda2; account for all tied label actions. Only after actual all-policy exposure is proved, attempt all-direction convex-hull equality and a true-image nonrealizability certificate.