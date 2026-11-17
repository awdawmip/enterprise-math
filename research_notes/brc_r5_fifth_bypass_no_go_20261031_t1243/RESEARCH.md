# R5 — An independent fifth bypass monomial cannot repair the rank-four hull gap

**Author mathematical result (2026-10-31, Asia/Shanghai)**: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is an algebraic auxiliary control/observer model. A strictly positive P/Q stopping-process realization is NOT asserted; no native Heartbeat/X6 transfer is asserted.

## Fixed inputs

GLOBAL_KNOWLEDGE_V1 canonical main d714c46128c9083261f4235fc1909325d19a1bd6; Enterprise Math canonical main cf4dc7ae3d5c91f3659bc16d603877164db812ec (both actually read in this turn). P000 and ACTIVE worldview held unchanged. Predecessor: research_notes/brc_r5_two_tail_affine_no_go_20261031_t1136/RESEARCH.md at immutable aac1c4442231d25b3cc891999a69bb8814921fec, Draft PR #1663. Its four-monomial rank-four no-go is reused, not repeated.

## Question, positive monomial carrier and scope

Add one bypass decision u0 independently of downstream decision u1 to the predecessor's two-tail algebra. FULL has independent real actions x,u1,vD,vY,u0 in [0,1], recording (a,b,c,d,z)=(x,x*u1,x*vD,x*u1*vY,u0). Seedless LR identifies u0=u1=u and vD=vY=v, recording (x,x*u,x*v,x*u*v,u). The five labelled action monomials retain distinct provenance until final readout. The theorem applies if the COMPLETE four-observer output of both classes is a COMMON real affine map O=b0+M(a,b,c,d,z), with M 4×5. This describes a conditional mathematical interface, not an independently verified finite two-law stochastic transition table or P000 coordinate representation. The selected final readout may compress these labels only for its stated observer; future-operation-safe compression is not asserted.

## Lemma — exact FULL polytope and LR simplex

The actual FULL monomial set is P_F × [0,1] where P_F={(a,b,c,d): 0<=b<=a<=1, 0<=c<=a, 0<=d<=b}. Its 14 vertices are all z=0,1 copies of seven points:
(0,0,0,0), (1,0,0,0), (1,0,1,0), (1,1,0,0), (1,1,1,1), (1,1,0,1), (1,1,1,0).

Proof: every behavioral tuple satisfies the displayed inequalities. Conversely put x=a; u1=b/a and vD=c/a for a>0 (zero otherwise), vY=d/b for b>0 (zero otherwise), and u0=z. These reconstruct every feasible tuple; endpoints enumerate the seven four-coordinate vertices.

The LR convex hull is the 5-simplex on six affinely independent vertices, in coordinate order (a,b,c,d,z):
L0=(0,0,0,0,0); Lz=(0,0,0,0,1);
L1=(1,0,0,0,0); L2=(1,0,1,0,0);
L3=(1,1,0,0,1); L4=(1,1,1,1,1).
Its unique affine barycentric coefficients, in this order, are

lambda(Y)=(1-a-z+b, z-b, a-b-c+d, c-d, b-d, d).

They sum to 1 and give each LR vertex its own unit coefficient. Therefore membership in the LR hull is equivalent to all six coefficients being nonnegative. Multi-affinity makes its hull the hull of those deterministic vertices.

## THEOREM — universal rank-four no-go

For EVERY real 4×5 matrix M of rank 4 and every real b0 in R4,
conv O_FULL != conv O_LR.
If rank(M)<4, the four-observer affine dimension cannot be 4. Thus this entire independent-bypass fifth-monomial class fails the joint full-rank/equal-hulls target.

Proof. Suppose equality with rank(M)=4. Let nonzero k span ker(M); let mu=lambda(Y+k)-lambda(Y). We have sum(mu)=0. For each FULL vertex W, equality requires a real t_W such that lambda(W)+t_W*mu >=0 componentwise, since the projected fibre W+Rk must intersect the LR simplex.

Choose three FULL vertices, whose barycentrics are exact:
A=(1,0,0,0,1), lambda(A)=(-1,1,1,0,0,0);
B=(1,1,1,1,0), lambda(B)=(1,-1,0,0,0,1);
C=(1,1,0,1,1), lambda(C)=(0,0,1,-1,0,1).

Write the barycentric components with zero-based indices 0,...,5, and let mu1 denote the Lz coefficient. From A, tA*mu0>=1, and tA*mu3,tA*mu4,tA*mu5>=0, because lambda3(A)=lambda4(A)=lambda5(A)=0. Thus mu0 is nonzero. From B, tB*mu1>=1, and tB*mu2,tB*mu3,tB*mu4>=0, because lambda2(B)=lambda3(B)=lambda4(B)=0. Thus mu1 is nonzero.

If mu0 and mu1 have the same sign, tA and tB share that sign. All six mu components have that same weak sign: mu0 from A, mu1 from B, mu2 from B, mu3 and mu4 from both, and mu5 from A. With mu0,mu1 strictly nonzero, this contradicts sum(mu)=0.

If mu0 and mu1 have opposite signs, tA and tB have opposite signs. Their shared zero-coordinate inequalities force mu3=mu4=0. But lambda3(C)=-1 remains unchanged along every kernel fibre (since mu3=0), so C cannot project into the LR hull. Contradiction. QED.

## Exact rational regression and a concrete separator

Take O=(a,b,c,d+z), rank(M)=4. The LR projected vertices have a nonzero 4×4 affine rank minor +1. For H(O)=-2*O3+O4, the exact maxima are max_FULL=2 and max_LR=1, gap=1; C is the FULL witness. The sibling standalone Python stdlib Fraction verifier enumerated all 32 binary FULL and all 8 binary LR action assignments, deduplicated them to 14 and 6 monomial vertices, checked the three barycentric vectors and a nonzero affine minor, and exactly computed the support gap. It was actually executed; see VERIFY.py and EXACT_OUTPUT.txt. The all-real universal statement rests on the algebraic kernel proof, not finite matrix sampling.

## BRC interpretation, boundaries, next step

This uses provenance-labelled positive action weights as a mathematical carrier, and signed H only AFTER the observer map; it does not allow negative path mass or cancellative branch merging. A physical P/Q two-measure model with positive, normalized likelihood-ratio path flows and a complete four-observer factorization is a separate **unproved** correspondence obligation. No formal check in Lean, native source Claim/Result, or independent Driver review took place. Native em_status reported research_authority_granted=false; active Owner lookup returned CONTROL_QUOTA. This publication is author-side evidence storage, not registered role-bound execution or project mathematical admission.

The new reusable certificate is the **kernel-line barycentric sign test**: a small set of FULL vertices can rule out every rank-four projection of a candidate higher-monomial LR simplex at once. The next model must make the additional monomial interact with a second chance merger (not a free product z), derive strictly positive exact P/Q paths and observed four-vector, and then require either exact rational <=5-LR-vertex convex certificates for EVERY FULL deterministic observation or an exact Farkas separator. Only after all-signed hull equality and rank four should actual real LR image nonmembership be tested.
