# R5 bypass BRC: exact factor-two information-order criterion and crossing window

Date: 2026-11-04. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Sources and scope

Continue the strictly positive, source-sensitive, unrestricted-P/Q-declaration two-merger bypass BRC at predecessor immutable commit `68c058b10b8ec6d4ad75affffb7ac5c1aca4fab1`, `research_notes/brc_r5_bypass_unrestricted_real_image_20261104_t1635/RESEARCH.md` (PR #1767). The R5 mother objective is equal *complete four-observer convex hulls* but unequal *actual real-policy images* for FULL versus seedless likelihood-ratio (LR) strategies. Scientific frozen pins: Global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current norms were read separately. This is an auxiliary finite BRC, without a claimed native X6 embedding. P000 and ACTIVE worldview remain unchanged.

## Exact P/Q model and observation

At time 1, source histories A1,A2, each with initial Q and P mass 1/4, share observed key (time,r)=(1,1). Source B, initial Q and P mass 1/2, bypasses to time 2. A histories that continue and B then share observed key (2,1). At each such key one can stop and declare P, stop and declare Q, or continue, with behavioral randomization. FULL observes source/history and LR observes only (time,r), with no externally shared seed. At time 3, continuing histories terminate in a finite strictly positive Q-law likelihood-ratio lottery E_A (for each A) or E_B (for B), each with E_Q[r]=1. The corresponding P probabilities are r times Q probabilities. Every terminal permits free P/Q declaration. LR shares one terminal declaration probability for any identical (3,r) key. The observation is O4=(eP=P[declare Q],eQ=Q[declare P],TP=E_P[t],TQ=E_Q[t]). All branching and initial masses are positive under both laws.

## Theorem 1: exact criterion, arbitrary finite terminal kernels

For any pair of such finite positive mean-one terminal experiments, define for every signed (alpha,beta) in R²

    v(r)=max(alpha*r,beta)
    DA(alpha,beta)=E_A[v(r)]-v(1)
    DB(alpha,beta)=E_B[v(r)]-v(1).

Jensen implies DA,DB>=0. The following are **equivalent** for all real randomized behavioral policies:

(i) O4(FULL)=O4(seedless LR).
(ii) conv O4(FULL)=conv O4(seedless LR).
(iii) DA(alpha,beta)<=2 DB(alpha,beta) for every signed (alpha,beta).

### Proof, (iii) implies (i)

Let x be mean A continuation at time 1, z mean A time-1-and-time-2 continuation occupancy, and y be B continuation at time 2. Precisely the FULL feasible region is 0<=z<=x<=1, 0<=y<=1; indeed set both A time-1 probabilities x and both conditional time-2 probabilities z/x (zero if x=0). The observed times satisfy

    TP=TQ=3/2+(x+z+y)/2, f=x+z+y in [0,3].

Write K(r)=conv{(r,0),(0,1)} and let E_A[K(r)] be the Q-weighted Minkowski sum of those terminal segments; similarly B. At fixed (x,z,y), the *complete* error fiber is

    E(x,z,y)=[1-(z+y)/2]K(1)+(z/2)E_A[K(r)]+(y/2)E_B[K(r)].

The same formula holds for LR subject to z=xy; equal (time,r) terminal keys can aggregate their colinear K(r) segments without losing any error vectors. For every signed error normal (alpha,beta),

    h(E(x,z,y))=v(1)+(z DA+y DB)/2.    (1)

At fixed f, permissible y lies in [max(0,f-2),min(1,f)], and z<=(f-y)/2. Equality for a given y is attained by x=z=(f-y)/2. Under DA<=2DB, (1) is maximized by y*=min(1,f). The maximizing occupation triple, *independent of the signed error normal*, is realized by a seedless LR timing policy:

    0<=f<=1: (x*,z*,y*)=(0,0,f);
    1<=f<=3: (x*,z*,y*)=((f-1)/2,(f-1)/2,1).

Here z*=x*y*. The FULL fixed-f error set is a compact convex polytope: encode continuation flows and stopping/terminal declaration masses with linear conservation and bounds 0<=declared_mass<=arrival_mass, then project at fixed f. For all signed normals its support is that of the *single* LR error polygon at the displayed policy. Equality of compact convex sets follows from support-function separation. Each FULL observation thus has an LR real-behavioral realization, and LR⊆FULL proves (i). In fact the same LR timing probability pair works for every target error vector at its f; one varies only freely chosen terminal/early declarations.

### Proof, (ii) implies (iii)

Assume DA>2DB for a signed normal (alpha,beta), and choose tau=(DA+2DB)/4. The full four-observer direction n=(alpha,beta,-tau,0) has support at occupancy (x,z,y) equal to

    v(1)-3tau/2+[DA*z+DB*y-tau*(x+z+y)]/2.

FULL may use (x,z,y)=(1,1,0), whose normalized variable reward is DA-2tau=(DA-2DB)/2. A seedless LR has z=xy; the variable reward DA*xy+DB*y-tau*(x+xy+y) is multi-affine in x,y, so its maximum on the unit square occurs at a corner. At the four corners (0,0),(1,0),(0,1),(1,1) the rewards are 0,-tau,DB-tau,DA+DB-3tau, whose maximum is (DA-2DB)/4. Hence

    h_FULL(n)-h_LR(n) >= (DA-2DB)/8 >0.    (2)

In fact equality in (2) follows because (x,z,y)=(1,1,0) is also a FULL global maximizer for this tau: the other FULL timing vertices have no larger variable reward. Thus convex hulls differ, proving (ii) implies (iii). The direction and FULL timing point give an explicit certificate.

## Theorem 2: crossing information orders with *equal actual images*

Choose parameters 0<a<=b<1, 0<w<1/2 and the positive normalized Q-terminal experiments

    E_A: likelihood ratios (1-a,1+a) with Q masses (1/2,1/2);
    E_B: likelihood ratios (1-b,1,1+b) with Q masses (w,1-2w,w).

Then, for the complete unrestricted-declaration model:

    conv O4(FULL)=conv O4(LR)  iff  w>=a/(4b).

Whenever these hulls are equal, **O4(FULL)=O4(LR)** for actual real behavioral policies as well. At 0<w<a/(4b), a strict four-observer separator exists.

Proof: the excess Jensen call option functions k_t(r)=(r-t)_+ are

    C_A(t)=(a-|t-1|)_+/2,
    C_B(t)=w*(b-|t-1|)_+.

For alpha>0, the excess of max(alpha*r,beta) equals alpha*C(t), t=beta/alpha. For alpha<0 it is |alpha| times the put-option excess, which equals the call excess by mean-one put-call parity; alpha=0 gives zero. Thus the universal criterion DA<=2DB reduces to C_A(t)<=2C_B(t) for every real t. On 0<=s=|t-1|<a, their ratio is (a-s)/(2w(b-s)), maximized at s=0 because a<=b; beyond s>=a, C_A=0. The criterion is exactly w>=a/(4b). QED.

The usual convex-order relation E_A<=cx E_B holds exactly when w>=a/(2b). Therefore the nonempty window

    a/(4b)<=w<a/(2b)

exhibits *crossing* terminal information orders: neither terminal experiment dominates the other for all convex payoffs, yet FULL and seedless LR have the same **actual** O4 image. The predecessor's DA<=DB hypothesis has thus been sharpened to DA<=2DB.

## Exact rational instances and executed evidence

Set a=1/2, b=3/4. At w=1/5, the threshold a/(4b)=1/6 is met while call excesses cross: at t=1, (C_A,C_B)=(1/4,3/20); at t=3/8 they are (0,1/40). Equality holds at the boundary w=1/6 as well. At w=1/8, DA(1,1)=1/4 and DB(1,1)=3/32, and the separator direction is n=(1,1,-7/64,0). The legal FULL policy continuing all A to terminal and stopping B at time 2 gives W=(3/8,3/4,5/2,5/2), and

    h_FULL(n)=109/128, h_LR(n)=27/32, GAP=1/128,
    dist_inf(W,conv O4(LR))>=1/270.

The `VERIFY.py` standard-library Fraction verifier was executed locally; `EXACT_OUTPUT.txt` records its actual output. It checks signed-direction gaps and all piecewise-linear breakpoints, both endpoint/boundary cases, exact P/Q normalization, fixed-time canonical policies, a separate exact FULL Bellman recursion, and *all 288* deterministic LR policies for the separating instance. Finite tests corroborate the all-real analytic proof. No external scientific result beyond elementary convex support geometry, Jensen and exact occupancy-flow arithmetic is required.

## Continuation

The single bypass resource yields an exact factor-two criterion; within this topology, convex-hull equality already supplies an LR real-policy reconstruction even when terminal information orders cross. The next discriminating unit changes the flow geometry (an additional independent resource or split/remerge), preserves full P/Q declarations and positive kernels, and tests complete four-dimensional hull equality before nonlinear actual-image membership. This is a model-internal theorem, with no native Result/admission or independent review claimed.
