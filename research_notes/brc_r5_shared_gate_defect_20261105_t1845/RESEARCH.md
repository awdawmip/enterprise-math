# R5: exact shared-gate information defect for arbitrary finite incoming histories

2026-11-05, Asia/Shanghai. AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Mother question and provenance

R5 seeks strictly positive finite P/Q stopping BRC with complete four-observer FULL and seedless LR convex hull equality but different **actual real-behavior** images. The observer is O4=(P[declare Q], Q[declare P], E_P[tau], E_Q[tau]). Frozen scientific inputs: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Earlier immutable frontier: enterprise-math@8275f4043ca50e00ca8078d52bb7448c54189243, research_notes/brc_r5_nonlumpable_exposed_face_20261105_t1743/RESEARCH.md. That work proves seedless LR nonconvexity and a full-history hull support difference of 1/400 on a finite strictly positive four-stage model S.

P000 and the ACTIVE worldview remain intact. This is an auxiliary finite positive weighted P/Q observer calculation, not a native X6 physical dynamics law. The carrier retains the history label i until its effect on all relevant future operations is certified.

## Theorem 1 — arbitrary-history exact shared-gate regret identity

At a fixed linear objective direction n in the complete four-observer space, suppose a finite stopping model's relevant choice reduces **exactly** to

    J_LR(a,z) = C + sum_{i=1}^m w_i a_i (A_i+z u_i),

where m>=1, w_i>0, a_i in [0,1] are independently controllable upstream continuation probabilities at distinct observable keys, and z in [0,1] is the one common continuation probability at a later **merged** seedless (time,likelihood-ratio) key. A_i is the first-stage incremental objective value if this history reaches that key and stops there; u_i is the additional increment for continuing at it. FULL_HIST sees incoming history i and can instead select independently z_i in [0,1], giving C+sum_i w_i a_i(A_i+z_i u_i). The objective's other branches are held fixed or independently reduced into C. This is a theorem about such an exact two-gate reduction; an application must independently check legal upstream controls, other stopping actions and any alternative first-stage stopping option.

Write (x)_+=max(x,0) and set

    M_i=max(0,A_i,A_i+u_i);
    L0=sum_i w_i(A_i)_+;
    L1=sum_i w_i(A_i+u_i)_+;
    H=sum_i w_i M_i.

Then the maxima over **all real behavioral probabilities** are

    h_FULL = C+H;
    h_LR   = C+max(L0,L1);
    Delta  = H-max(L0,L1)
           = min(sum_i w_i[M_i-(A_i)_+],
                 sum_i w_i[M_i-(A_i+u_i)_+]) >= 0.

In particular, Delta=0 if and only if either M_i=(A_i)_+ for every positively weighted history i, or M_i=(A_i+u_i)_+ for every such history. Equivalently, there exists a single common deterministic downstream gate z=0 or z=1 that is optimal for all incoming histories (including indifferent histories). Delta>0 precisely when one positively weighted history strictly favors the closed gate and a different one strictly favors the open gate after the independent upstream choices are accounted for.

### Proof

For fixed z, maximizing over each a_i gives (A_i+z u_i)_+. Thus LR optimizes f(z)=sum_i w_i(A_i+z u_i)_+. This is a convex function of z; consequently f(z)<=(1-z)f(0)+zf(1)<=max(f(0),f(1)). Even with arbitrary real randomization, an LR support optimizer exists with z=0 or z=1. Hence its value is C+max(L0,L1). FULL_HIST can choose z_i independently, and each term has exact optimum max(0,A_i,A_i+u_i), yielding C+H. Since M_i is at least either positive part, the two weighted regret sums are nonnegative. Subtracting max(L0,L1) from H yields the min-of-regrets identity. Each regret sum is zero exactly when all of its positive-weight summands vanish, proving the stated equivalence. QED.

The defect is an exact path-provenance residual for the declared four-observer value problem. It is not a general identity for systems in which the upstream a_i are coupled by an additional seedless decision.

## Corollary 2 — crossing preferences make a strict FULL_HIST hull gap

For two histories assume

    w1,w2>0;
    A1>0>A1+u1;
    A2<0<A2+u2.

Then the closed gate is uniquely beneficial for history 1, the open gate for history 2, and

    Delta = min(w1*A1, w2*(A2+u2)) > 0.

This strict gap persists throughout the open coefficient region given by those inequalities. The crossing is therefore a **locally robust strict convex-hull obstruction** in any stopping experiment for which the exact two-gate reduction globally governs the chosen support direction.

If moreover w1*A1=w2*(A2+u2)>0, other first-stage alternatives have strictly lower support, and terminal declaration ties do not alter the timing observer, the LR maximizing exposed face has exactly two timing modes: a=(1,0),z=0 and a=(0,1),z=1. Indeed f(0)=f(1), f strictly decreases near z=0 (u1<0, A2<0) and convexity forces f(z)<f(0) for every interior 0<z<1. At the endpoint z=0 the unique optimal upstream choices are a=(1,0); at z=1 they are a=(0,1). If the two resulting timing pairs differ, the midpoint of their O4 vectors belongs to conv O4(LR), lies on its exposed hyperplane, but has neither possible timing pair of a maximizing LR policy, and so lies outside the actual real-behavior O4(LR). This establishes nonconvexity of the seedless actual image under the stated exact conditions. The same crossed gates have Delta>0, excluding complete FULL_HIST/LR convex-hull equality for that local topology. Other topologies and non-exposed mechanisms remain open.

## Exact positive four-stage application and a new metric lower bound

Reuse the predecessor's strictly positive model S, in which distinct time-two ratio nodes 3/4 and 5/4 merge at the nonterminal time-three ratio 1, and their conditional future kernels differ. At direction

    n=(-1,-1,-3/25,+1/50),

the predecessor's exact Bellman reduction identifies

    C=-43/40,
    (w1,w2)=(1/2,1/2),
    (A1,u1)=(1/200,-9/500),
    (A2,u2)=(-47/400,49/400).

Here A1+u1=-13/1000<0, while A2+u2=1/200>0, so the crossing conditions hold, and both endpoint regrets equal 1/400. Thus

    h_LR(n)   = -43/40+1/400 = -429/400,
    h_FULL(n) = -43/40+1/200 = -107/100,
    Delta = 1/400.

The predecessor also establishes an exact valid FULL_HIST point

    W_hist=(1141/3600,31/72,129/40,129/40)

with n dot W_hist=-107/100. For every V in the complete convex hull conv O4(LR; S), n dot V <= -429/400. Therefore

    1/400 <= n dot (W_hist-V) <= ||n||_1 ||W_hist-V||_infty,
    ||n||_1=1+1+3/25+1/50=107/50,

and a **new quantitative exact exclusion certificate** follows:

    dist_infty(W_hist, conv O4(LR;S)) >= 1/856.

The bound is not claimed to equal the exact minimal distance. It is valid against the complete real-behavior LR convex hull, rather than only a finite grid.

For S, the two exposed LR timing pairs, previously certified, are (19/8,5/2) and (57/20,109/40); the observed LR nonconvexity corresponds to the balanced crossing face. This note explains the earlier witness through a general m-history lemma and strengthens its hull separation from an unnormalized support difference to a four-coordinate distance bound.

## Actual verification and evidence standard

VERIFY.py is an executable Python 3 standard-library Fraction program. It exhaustively checks the exact formulas against deterministic gate enumeration on 240 seeded rational instances (48 at each m=1,...,5); checks the instantiated S coefficients and extrema, both endpoint regrets, the explicit W_hist objective value and the 1/856 bound. Recorded stdout is EXACT_OUTPUT.txt. The m-history theorem and all-real behavior conclusion are analytical; finite checks are targeted implementation checks. S's full positive transition table was checked in the immutable predecessor, and is reused here rather than represented as a newly executed independent exhaustive probability validation.

## Scientific consequence and next exact question

All-direction FULL_HIST/LR hull equality requires *zero applicable gate conflict in every four-observer support direction*, **provided** each reduction's upstream independent actions are globally reachable under optimal play. The new finite decision criterion is to partition direction space into rational Bellman sign cones and calculate two endpoint regret sums on each cone. Seek a strict rational sign-conflict direction (a separating certificate) or prove common-gate compatibility for all cones; one finite direction grid cannot certify complete hull equality. If such equality is achieved, separately test nonconvexity of the actual seedless LR image. The R5 mother objective remains OPEN.

BRC reuse: REUSE_APPLIED — positive weighted path carriers, exact rational conditional likelihood-ratio transitions, labeled incoming ports and observer-sensitive projection. No native task CLAIM, Result, independent Driver review or Foundation promotion follows from this authored research.