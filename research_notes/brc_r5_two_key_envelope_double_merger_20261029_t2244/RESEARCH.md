# R5: Two-key hull rigidity and dominated-descendant double merger

2026-10-29 Asia/Shanghai. **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.** Author-side portable research only; no native CLAIM, Result, independent Driver review or Foundation change.

## Frozen inputs, authority and scope

GLOBAL_KNOWLEDGE_V1 main@d5508d486945b177bc81f0f1f0a7f54df273e4ef; Enterprise Math canonical main@13c96bdc2c883b5f9e5aa6c75ecfd0b7b26d4048. Read both global entries, project AGENTS, P000, ACTIVE residual-faithful worldview, joint-relation preservation, Heartbeat X6+time, BRC preference, current control authority and portable research protocol. Predecessor: PR #1663 at 24861434625d0fc0bb2304d95dafcc0e9c799afa. This run's native status and owner calls returned BACKEND_IDENTITY_CHECK_UNAVAILABLE / operation_sent=false; actual active Source owner remains unverified.

External finite absorbing two-law P/Q stopped experiments with FULL history-dependent action and seedless LR behavior depending only on (time, exact likelihood ratio). Four observers O=(eP,eQ,TP,TQ). BRC reuse: exact nonnegative P/Q source, path and branch masses, never fictitious signed probabilities. This mathematical model makes no native X6/physical claim.

## Theorem 1: isolated two-key convex-hull equality forces real-image equality

For arbitrary A,X,Y,Z in any finite-dimensional real observable vector space, let

F={ A+xX+aZ+bY : 0<=a<=x<=1, 0<=b<=1 },
L={ A+xX+y(Y+xZ) : 0<=x,y<=1 }.

This is the exact positive-flow normal form for a binary upstream key with continue probability x, and a later key receiving an upstream-visited stream (a=xv for history-conditioned v) and an independent bypass stream (b); LR must use one common y for both. Actions outside this two-key scope are fixed. Claim: **conv(F)=conv(L) implies F=L for all real behavior probabilities.** When rank span{X,Y,Z}>=2, hull equality requires either Y=0, Z=0, or Z=tY with t>=0.

Proof. F is already convex: it is the affine image of the polytope 0<=a<=x<=1,0<=b<=1. L is a bilinear image of the square, so its convex hull K consists of the four LR corner vectors A, B=A+Y, C=A+X, D=A+X+Y+Z. The two additional FULL vertices are E=A+X+Y and G=A+X+Z. Thus hull equality is equivalent to E,G in K.

If Y!=0 and Z is not parallel to Y, project modulo span(Y). K projects to the convex hull of {0,u,u+z}, z!=0. One of the distinct u, u+z is a uniquely exposed extremal projected point. If it is u, the fiber of K over u is exactly {C}; but E=C+Y is distinct and projects to u. If it is u+z, the fiber is {D}; but G=D−Y is distinct and projects there. Either contradicts both E,G in K. Therefore Z=tY if Y!=0.

For rank>=2 with Z=tY, X must be independent of Y. The K fiber over the projected X is the segment [C,D], with scalar Y-coordinate between 0 and 1+t. E and G have coordinates 1 and t. Both lie in that interval only when t>=0; if t<0, one lies outside. Conversely for t>=0 and fixed x, FULL has s=b+ta ranging through [0,1+tx], and LR realizes every such s by y=s/(1+tx). The cases Y=0 and Z=0 use y=a/x (arbitrary at x=0) and y=b, respectively. Thus F=L. If rank<=1, L is a compact connected image of the square into a line, hence the entire interval K between the extreme LR corners. Convex F and equal hulls imply F=K=L. QED.

This eliminates isolated source-sensitive bypass/visited collision candidates with independent Y,Z without facet enumeration. It is NOT a claim for unrestricted further consequential LR decisions.

## Lemma 2: direction-specific dominated descendants

For a fixed signed w, append binary stop/continue descendants to existing terminal histories. If continue-minus-stop expected w·O is nonnegative at each full history (using its actual P/Q masses), both FULL and LR minima remain unchanged. FULL can replace each continuation by stop; at a merged LR key the same replacement changes cost by the nonnegative sum of the full-source increments. This works for real behavioral probabilities. With multiple descendants apply reverse-time local optimization. The result concerns this w-support, not equality of full observer images or source-independent kernels.

## Strictly positive, source-sensitive interacting double merger

Two origins via and bypass initially have P=Q=1/2 each. Via has k=(time1,r=1): stop error0/time1; continue to l. Bypass arrives directly at l=(time2,r=1). Stop at l error0/time2. Continue emits intermediate bit z at t3 with conditional bit-one kernel (via P=1/4,Q=3/4; bypass P=3/4,Q=1/4). Both outcomes are positive under both measures.

At time3 the exact LR keys are m_3 and m_{1/3}. For k=l=continue, m_3 receives via/z0 and bypass/z1, each with P mass 3/8 and Q mass 1/8, ratio3. The other key receives via/z1 and bypass/z0, each with P mass1/8,Q mass3/8, ratio1/3. Both are real positive colliding sources. At m, stop with final error z,time3, or continue to t4 and resample final Bernoulli error with source-dependent kernels via (P=1/4,Q=1/16) and bypass (P=3/8,Q=1/32); all primitive kernels and complements are strictly positive. Both merger stages are source-sensitive and interact by reachability.

For w=(1,-8,1,1), at any m full source-history with intermediate bit z, actual positive masses MP,MQ, and new P/Q error probabilities p',q', the cost of continue minus stop is
MP*(1+p'−z)+MQ*(1−8q'+8z)>0.
If z=0 both coefficients are positive because q'<1/8; if z=1 they are p'>0 and 9−8q'>0. Thus every w-minimizing FULL or LR policy stops at m (except unreachable irrelevant keys). This applies the dominated-descendant lemma without deleting m from the model.

With m stopped, exact source-mass equations are
eP=xv/8+3b/8; eQ=3xv/8+b/8; TP=TQ=(3+x+xv+b)/2,
where x is k continuation and v,b are FULL source-specific l continuations. Consequently
w·O_FULL=3+x−(15/8)xv+(3/8)b >=17/8,
with equality x=1,v=1,b=0 and O*=(1/8,3/8,5/2,5/2).
For LR the common l continuation y gives
w·O_LR=3+x−(15/8)xy+(3/8)y >=5/2,
by its four bilinear corner values 3,27/8,4,5/2. Dominance extends this to every real m continuation.

Hence EXACT ALL-REAL support gap: **5/2−17/8=3/8**.
Every real LR observer satisfies the integer inequality
8eP−64eQ+8TP+8TQ >=20,
whereas the legal FULL witness gives 17. Therefore its L-infinity distance to the LR image is at least **3/88**. This is a **strict-hull-inequality exclusion**, not the requested equal-hull/different-real-image mother counterexample.

## Executed checks and boundaries

VERIFY.py was actually executed using stdlib fractions.Fraction; EXACT_OUTPUT.txt contains its real output. It verifies all primitive kernels, four positive collision-source P/Q masses, m dominance, exhaustive **16 LR and 128 FULL deterministic policies**, signed minima, witness and distance. Each key is met at most once per trajectory, hence each real behavior output is multi-affine in the independent key probabilities and is a convex interpolation of the deterministic corners. Thus finite exhaustive extrema certify the all-real support values in this finite model, independently of the algebraic derivation.

The same executed code exhaustively tested **15,625** triples of integer 2D vectors X,Y,Z from [-2,2]^2 by exact integer hull membership, found **2,225** with equal corners' convex hull and zero rank>=2 nonnegative-ray violations. The finite grid is a regression, NOT the proof of the dimension-free theorem above.

No Lean checker, independent mathematical review, physical bridge or originality priority. Conceptual prior art: perfect-recall behavioral/mixed equivalence (Kuhn), and intrinsic/product-form generalizations (Heymann, de Lara, Chancelier, arXiv:2006.14838 and arXiv:2104.05249); their work is not claimed to contain this exact specialized geometric lemma.

## Next unresolved step

For the mother target, construct a strictly positive rational double-merger model with **at least three simultaneously consequential decision keys** not reduced by safe lumpability, this two-key theorem, known bypass normal-cone separators or dominated descendants. First enumerate exact deterministic LR/FULL observer vectors and give a rational convex-combination certificate or Farkas separator for EVERY FULL vertex in the entire LR hull, including affine-hull equalities and all signed directions. Only then seek an all-real polynomial nonmembership proof including boundaries and unreachable keys, retaining P/Q origin provenance.
